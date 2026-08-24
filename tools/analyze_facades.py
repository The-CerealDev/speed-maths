#!/usr/bin/env python3
"""Report checks whose assertions cannot fail because of the code under test.

    python3 tools/analyze_facades.py            # advisory report, exit 0
    python3 tools/analyze_facades.py --strict   # exit 1 if anything is flagged

This is the *detailed* view. `tools/check_binding.py` is the gate — it owns the
baseline and the exit code that CI depends on, so there is only ever one list to
keep honest. Use this tool to see which individual assertions are the problem in
a check the gate flagged.

What counts as a facade here:

  EMPTY           body is empty or only `pass`.
  NO_ASSERTION    no `assert` anywhere in the check's own body.
  ALL_TRIVIAL     every assertion compares literals, so it is true no matter
                  what the check computed:

                      expected_ans = get_answer(TEX_PATH, 'B4')
                      assert 3**40 > 4**30

                  Both lines are inert. The first is never read; the second is a
                  fact about two constants that holds whether or not the answer
                  key agrees. 33 published questions are in this state.

The previous version of this tool was regex-based and reported 11 facades. It
missed every `pass`-only body (13 of them), skipped the sequences pillar
entirely, only recognised a trivial assertion of the exact shape `\\d+ op \\d+ ==
\\d+`, and always exited 0 — so it could never gate anything, and its "11" was
read as the whole problem for as long as it was believed.
"""

import argparse
import ast
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.check_binding import (  # noqa: E402
    _assert_is_vacuous, _own_statements, published_sheets,
)

EMPTY = "EMPTY"
NO_ASSERTION = "NO_ASSERTION"
ALL_TRIVIAL = "ALL_TRIVIAL"


def analyse(fn, source):
    """(verdict, [rendered trivial assertions]) for one check, or (None, []).."""
    body = [s for s in fn.body
            if not (isinstance(s, ast.Expr)
                    and isinstance(s.value, ast.Constant)
                    and isinstance(s.value.value, str))]
    if not body or all(isinstance(s, ast.Pass) for s in body):
        return EMPTY, []

    asserts = [s for s in _own_statements(fn) if isinstance(s, ast.Assert)]
    if not asserts:
        return NO_ASSERTION, []

    trivial = [a for a in asserts if _assert_is_vacuous(a)]
    rendered = []
    for a in trivial:
        try:
            rendered.append(ast.get_source_segment(source, a).strip())
        except Exception:
            rendered.append(f"line {a.lineno}")

    if len(trivial) == len(asserts):
        return ALL_TRIVIAL, rendered
    return None, rendered      # has real assertions; trivia is just padding


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any check verifies nothing")
    args = ap.parse_args()

    facades = []
    padding = 0
    checks = 0

    for pillar, num, path in published_sheets():
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        flagged = []
        for fn in tree.body:
            if not (isinstance(fn, ast.FunctionDef) and fn.name.startswith("check_")):
                continue
            checks += 1
            verdict, trivial = analyse(fn, source)
            if verdict:
                label = fn.name[len("check_"):]
                flagged.append((label, verdict, trivial))
                facades.append(f"{pillar}/sheet{num} {label}")
            elif trivial:
                padding += len(trivial)
        if flagged:
            print(f"\n[{pillar} sheet {num}] {len(flagged)} check(s) verify nothing:")
            for label, verdict, trivial in sorted(flagged):
                print(f"  {label}: {verdict}")
                for line in trivial[:3]:
                    print(f"      {line}")
                if len(trivial) > 3:
                    print(f"      ... and {len(trivial) - 3} more trivial assertion(s)")

    print(f"\n{checks} published checks examined.")
    print(f"  verify nothing:            {len(facades)}")
    print(f"  trivial assertions used as"
          f" padding beside real ones: {padding}")
    if facades:
        print("\nA check must assert something that depends on a value it computed.")
        print("See CONTRIBUTING.md -> Verification pipeline. The gate that fails a")
        print("build for these is tools/check_binding.py.")
        return 1 if args.strict else 0
    print("\nNo facade checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
