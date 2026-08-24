#!/usr/bin/env python3
"""Static gate: every published question's check must actually verify something.

Run from the repo root:

    python3 tools/check_binding.py              # gate, honours the baseline
    python3 tools/check_binding.py --full       # ignore the baseline, show everything
    python3 tools/check_binding.py --write-baseline

Why this exists. `run_all.py` reports PASS for a check whose body is `pass`, and
for a check that reads the published answer into a variable it never uses. Both
happened, at scale: of 1,155 published answers, 16 had no verification at all
and 622 were never compared against the `\\ans{}` printed in the PDF. Every one
of them reported PASS, and the docstrings said "EXHAUSTIVE PROOF".

A passing test suite cannot detect this — the checks pass. It is a property of
the source, so it is checked in the source.

Four ways a check fails the gate:

  EMPTY_BODY      body is empty or only `pass`. Verifies nothing whatsoever.
  NO_ASSERTION    no `assert` anywhere. Computes and then shrugs.
  VACUOUS_ASSERT  every assertion compares literals (`assert 8 * 7 == 56`).
                  True regardless of the code under test, so it survives any
                  mutation and proves nothing about the published answer.
  UNBOUND         nothing connects the check to the answer printed in the PDF.
                  Two ways to be bound, and either satisfies the gate:
                    * `return <value>` — the harness compares what the check
                      returns against the `.tex`. Preferred for new checks:
                      the comparison lives in one reviewed place instead of
                      being re-derived by every author.
                    * the value from `get_answer(...)` reaches an `assert` —
                      the older convention, still sound.
                  A check doing neither can compute beautifully and still pass
                  with a wrong `\\ans{}`, which is the case for 622 of them.

Exemptions. 77 answers read "Proof: see method" — a pointer, not a value, so
nothing can be returned or compared. Those are listed in
verify/BINDING_EXEMPTIONS.md with the method claims asserted instead. The
exemption covers UNBOUND only: an exempt check still has to assert something
real.

The baseline. verify/BINDING_BASELINE.json records the violations that already
existed when the gate was introduced, so CI can enforce it immediately as a
ratchet: a new violation fails the build, and a label that leaves the baseline
can never come back. The baseline may only ever shrink.
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BASELINE_PATH = REPO_ROOT / "verify" / "BINDING_BASELINE.json"
EXEMPTIONS_PATH = REPO_ROOT / "verify" / "BINDING_EXEMPTIONS.md"

EMPTY_BODY = "EMPTY_BODY"
NO_ASSERTION = "NO_ASSERTION"
VACUOUS_ASSERT = "VACUOUS_ASSERT"
UNBOUND = "UNBOUND"

# "algebra/sheet03 C7" — how a single question is named in the baseline and the
# exemptions file.
_ENTRY_RE = re.compile(r"\b([a-z-]+)/sheet(\d{2})\s+([A-D]\d{1,2})\b")


def published_sheets():
    """Sheets the site actually serves, from sheets.json.

    Drafts are excluded deliberately: holding an unfinished pillar to the
    published bar would make the gate something contributors route around.
    """
    data = json.loads((REPO_ROOT / "sheets.json").read_text(encoding="utf-8"))
    out = []
    for pillar in data:
        if pillar.get("status") != "live":
            continue
        for sheet in pillar.get("sheets", []):
            script = REPO_ROOT / pillar["slug"] / "verify" / f"sheet{sheet['n']}_verify.py"
            if script.exists():
                out.append((pillar["slug"], sheet["n"], script))
    return sorted(out)


def _is_constant_expr(node):
    """True if the expression is built only from literals and operators.

    `8 * 7` is constant. `n * 7` is not. Used to spot assertions whose truth
    does not depend on any value the check computed.
    """
    for sub in ast.walk(node):
        if isinstance(sub, (ast.Name, ast.Call, ast.Attribute, ast.Subscript,
                            ast.comprehension, ast.Lambda)):
            return False
    return True


def _assert_is_vacuous(node):
    """True for assertions that cannot fail because of the code under test."""
    test = node.test
    if isinstance(test, ast.Constant):
        return True                      # assert True / assert 1
    return _is_constant_expr(test)


def _own_statements(fn):
    """Every statement belonging to `fn` itself, not to a function nested in it.

    Checks routinely define local helpers (`def poly_add(...): return ...`), and
    a helper's `return` says nothing about what the check reports. Walking the
    whole tree counted those and marked 118 checks as bound when none of them
    were.
    """
    NESTED = (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)
    stack = list(fn.body)
    while stack:
        node = stack.pop()
        yield node
        # A nested definition is yielded (so callers can see it is there) but
        # never descended into: its body belongs to the helper, not the check.
        if isinstance(node, NESTED):
            continue
        stack.extend(ast.iter_child_nodes(node))


def _returns_a_value(fn):
    """True if the check itself returns something other than None."""
    for sub in _own_statements(fn):
        if isinstance(sub, ast.Return):
            if sub.value is None:
                continue
            if isinstance(sub.value, ast.Constant) and sub.value.value is None:
                continue
            return True
    return False


def _names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _answer_reaches_assertion(fn):
    """True if a value read from `get_answer(...)` is used by some assertion.

    Follows assignment through a few hops, because the established idiom binds
    in two steps:

        expected_ans = get_answer(TEX_PATH, 'A1')
        target = expected_ans.rhs if isinstance(...) else expected_ans
        assert sympy.simplify(computed - target) == 0

    Catching only a direct reference would report that as unbound.
    """
    tainted = set()
    for stmt in ast.walk(fn):
        if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Call):
            func = stmt.value.func
            if getattr(func, "id", getattr(func, "attr", None)) == "get_answer":
                tainted |= {t.id for t in stmt.targets if isinstance(t, ast.Name)}
    if not tainted:
        return False
    for _ in range(4):                      # propagate through derived names
        for stmt in ast.walk(fn):
            if isinstance(stmt, ast.Assign) and (_names(stmt.value) & tainted):
                tainted |= {t.id for t in stmt.targets if isinstance(t, ast.Name)}
    return any(_names(a.test) & tainted
               for a in ast.walk(fn) if isinstance(a, ast.Assert))


def inspect_check(fn):
    """Violations for one `check_<label>` function, worst first."""
    body = [s for s in fn.body
            if not (isinstance(s, ast.Expr)
                    and isinstance(s.value, ast.Constant)
                    and isinstance(s.value.value, str))]      # drop the docstring
    if not body or all(isinstance(s, ast.Pass) for s in body):
        return [EMPTY_BODY, UNBOUND]

    found = []
    asserts = [s for s in ast.walk(fn) if isinstance(s, ast.Assert)]
    if not asserts:
        found.append(NO_ASSERTION)
    elif all(_assert_is_vacuous(a) for a in asserts):
        found.append(VACUOUS_ASSERT)
    if not (_returns_a_value(fn) or _answer_reaches_assertion(fn)):
        found.append(UNBOUND)
    return found


_internally_bound = None


def internally_bound_labels():
    """Questions whose check compares the answer key itself, without returning.

    tests/test_answer_binding.py needs this to tell the older convention apart
    from a check that simply ignores its answer key. Both return None; only one
    of them has verified anything.
    """
    global _internally_bound
    if _internally_bound is None:
        found = set()
        for pillar, num, path in published_sheets():
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for fn in tree.body:
                if (isinstance(fn, ast.FunctionDef)
                        and fn.name.startswith("check_")
                        and _answer_reaches_assertion(fn)):
                    found.add(f"{pillar}/sheet{num} {fn.name[len('check_'):]}")
        _internally_bound = found
    return _internally_bound


def scan():
    """{ 'pillar/sheetNN LABEL': [violations] } across every published sheet."""
    findings = {}
    for pillar, num, path in published_sheets():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for fn in tree.body:
            if not (isinstance(fn, ast.FunctionDef) and fn.name.startswith("check_")):
                continue
            problems = inspect_check(fn)
            if problems:
                label = fn.name[len("check_"):]
                findings[f"{pillar}/sheet{num} {label}"] = problems
    return findings


def load_entries(path):
    """Question keys named anywhere in a text file, so the files stay readable."""
    if not path.exists():
        return set()
    return {f"{p}/sheet{n} {lab}"
            for p, n, lab in _ENTRY_RE.findall(path.read_text(encoding="utf-8"))}


def load_baseline():
    if not BASELINE_PATH.exists():
        return {}
    return json.loads(BASELINE_PATH.read_text(encoding="utf-8")).get("violations", {})


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--full", action="store_true",
                    help="report every violation, ignoring the baseline")
    ap.add_argument("--write-baseline", action="store_true",
                    help="record the current violations as the baseline")
    args = ap.parse_args()

    findings = scan()
    exempt = load_entries(EXEMPTIONS_PATH)

    # An exemption excuses only the missing return. A "Proof: see method" answer
    # still has to be backed by real assertions.
    for key, problems in list(findings.items()):
        if key in exempt and UNBOUND in problems:
            problems.remove(UNBOUND)
            if not problems:
                del findings[key]

    total_checks = sum(1 for _ in published_sheets()) * 33

    if args.write_baseline:
        BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
        BASELINE_PATH.write_text(json.dumps({
            "_comment": [
                "Violations of tools/check_binding.py that predate the gate.",
                "This file may only ever shrink. Removing an entry means the",
                "check was fixed; a label that leaves must never come back.",
                "Regenerating it to silence a new failure defeats the point.",
            ],
            "total_published_checks": total_checks,
            "violations": dict(sorted(findings.items())),
        }, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {BASELINE_PATH.relative_to(REPO_ROOT)} "
              f"with {len(findings)} of {total_checks} checks recorded.")
        return 0

    baseline = {} if args.full else load_baseline()

    new = {k: v for k, v in findings.items() if k not in baseline}
    worsened = {k: sorted(set(v) - set(baseline.get(k, [])))
                for k, v in findings.items()
                if k in baseline and set(v) - set(baseline[k])}
    worsened = {k: v for k, v in worsened.items() if v}
    fixed = sorted(k for k in baseline if k not in findings)

    by_kind = {}
    for problems in findings.values():
        for p in problems:
            by_kind[p] = by_kind.get(p, 0) + 1

    print(f"Published checks: {total_checks}")
    print(f"  clean:            {total_checks - len(findings)}")
    print(f"  with violations:  {len(findings)}")
    for kind in (EMPTY_BODY, NO_ASSERTION, VACUOUS_ASSERT, UNBOUND):
        if by_kind.get(kind):
            print(f"      {kind:<16} {by_kind[kind]}")
    if not args.full:
        print(f"  on the baseline:  {len(findings) - len(new) - len(worsened)}")

    if fixed:
        print(f"\n{len(fixed)} baselined check(s) now pass. Drop them from "
              f"{BASELINE_PATH.relative_to(REPO_ROOT)}:")
        for key in fixed[:20]:
            print(f"  {key}")
        if len(fixed) > 20:
            print(f"  ... and {len(fixed) - 20} more")

    if new or worsened:
        print("\nFAIL — these are not covered by the baseline:")
        for key, problems in sorted(new.items()):
            print(f"  {key:<28} {', '.join(problems)}")
        for key, problems in sorted(worsened.items()):
            print(f"  {key:<28} {', '.join(problems)}  (new for an already-baselined check)")
        print("\nA check must assert something that depends on its own computation,")
        print("and return the value it claims is the answer so the harness can")
        print("compare it against the .tex. See CONTRIBUTING.md -> Verification")
        print("pipeline. Do not regenerate the baseline to silence this.")
        return 1

    if args.full and findings:
        print("\nAll violations (--full):")
        for key, problems in sorted(findings.items()):
            print(f"  {key:<28} {', '.join(problems)}")
        return 1

    print("\nOK — no new binding violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
