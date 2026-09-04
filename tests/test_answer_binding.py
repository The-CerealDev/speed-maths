"""Every published answer, compared against the check that claims to verify it.

One parametrised test over all 1,155 questions. This is the runtime half of the
binding guarantee; `tools/check_binding.py` is the static half.

The split matters. The static gate can see that a check never looks at its
answer key, but it cannot see whether the value it produces is *right*. This
test runs the check, takes the value it returns, and compares that against the
`\\ans{}` in the `.tex` using tools.answer_binding — one reviewed comparison for
the whole corpus instead of 1,155 authors each writing their own.

It also gives the mutation suite something real to kill. `latex_bridge` and
`answer_binding` are library code, and these 1,155 cases are their consumers, so
a mutant that breaks answer parsing or comparison gets caught here. The previous
mutmut configuration pointed at the check scripts themselves — a function cannot
be both the mutant and its own executioner, which is why all 9,016 mutants came
back "no tests".

Checks recorded in verify/BINDING_BASELINE.json are xfailed rather than skipped,
so a check that starts binding shows up as XPASS and `check_binding.py` tells
you to drop its baseline row.
"""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

def _find_repo_root() -> Path:
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "sheets.json").is_file() and (p / "tools").is_dir():
            return p
        p = p.parent
    if (Path.cwd() / "sheets.json").is_file():
        return Path.cwd().resolve()
    return Path(__file__).resolve().parent.parent


REPO_ROOT = _find_repo_root()

# Ensure mutants/tools takes precedence if running under mutmut, followed by REPO_ROOT
_test_parent = Path(__file__).resolve().parent.parent
if (_test_parent / "tools").is_dir() and str(_test_parent) not in sys.path:
    sys.path.insert(0, str(_test_parent))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.answer_binding import (  # noqa: E402
    DRIFT_ONLY, EXACT, EXEMPT, bind, is_proof_marker,
)
from tools.check_binding import internally_bound_labels  # noqa: E402
from tools.latex_bridge import extract_tex_answers, parse_tex_math  # noqa: E402

_module_cache = {}


def _load(script):
    """Import a verify script by path.

    By path, not by name, for two reasons: every pillar names its scripts
    `sheetNN_verify.py`, so importing by name collides (that is the 38
    collection errors), and `number-theory` contains a hyphen so it can never
    be a package.
    """
    key = str(script)
    if key not in _module_cache:
        name = "speedmaths_verify_" + script.relative_to(REPO_ROOT).as_posix().replace(
            "/", "_").replace("-", "_").removesuffix(".py")
        spec = importlib.util.spec_from_file_location(name, script)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        _module_cache[key] = module
    return _module_cache[key]


def _baseline():
    path = REPO_ROOT / "verify" / "BINDING_BASELINE.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("violations", {})


def _cases():
    """(pillar, sheet, label) for every question on a live pillar."""
    sheets = json.loads((REPO_ROOT / "sheets.json").read_text(encoding="utf-8"))
    baseline = _baseline()
    out = []
    for pillar in sheets:
        if pillar.get("status") != "live":
            continue
        slug = pillar["slug"]
        for sheet in pillar.get("sheets", []):
            num = sheet["n"]
            script = REPO_ROOT / slug / "verify" / f"sheet{num}_verify.py"
            tex = REPO_ROOT / slug / "answers" / f"ans{num}.tex"
            if not (script.exists() and tex.exists()):
                continue
            for label in sorted(extract_tex_answers(str(tex))):
                key = f"{slug}/sheet{num} {label}"
                marks = []
                # Only UNBOUND is a runtime concern. A vacuous assertion or a
                # missing one is invisible from here — the check still runs and
                # its answer still binds or does not — so xfailing on those
                # would report an XPASS that means nothing. tools/check_binding.py
                # owns those two.
                if "UNBOUND" in baseline.get(key, []):
                    marks.append(pytest.mark.xfail(
                        reason=f"on the binding baseline: {', '.join(baseline[key])}",
                        strict=True))
                out.append(pytest.param(slug, num, label, script, tex,
                                        marks=marks, id=key.replace(" ", ":")))
    return out


@pytest.mark.parametrize("pillar,sheet,label,script,tex", _cases())
def test_published_answer_is_bound(pillar, sheet, label, script, tex):
    module = _load(script)
    check = getattr(module, f"check_{label}", None)
    assert check is not None, (
        f"{pillar}/sheet{sheet} publishes answer {label} but "
        f"{script.name} defines no check_{label}"
    )

    # Running the check is itself part of the test: its own assertions fire
    # here, so a check that verifies internally fails this test by raising.
    computed = check()

    raw = extract_tex_answers(str(tex))[label]

    if is_proof_marker(raw):
        # The printed answer is "Proof: see method" — a pointer, not a value, so
        # there is nothing to compare. All that can be asked at runtime is that
        # the check ran without an assertion firing, which it just did. That the
        # check asserts something real, rather than nothing, is enforced
        # statically by tools/check_binding.py, and the question is listed in
        # verify/BINDING_EXEMPTIONS.md with the method claims it covers.
        return

    if computed is None:
        # No returned value. That is acceptable only for a check that compares
        # the answer key itself — the older convention, where the assertion that
        # just ran did the binding. Anything else is unbound and belongs on the
        # baseline, not passing quietly.
        assert f"{pillar}/sheet{sheet} {label}" in internally_bound_labels(), (
            f"{pillar}/sheet{sheet} {label}: check_{label}() returned nothing and "
            f"never compares get_answer() against its own result, so no wrong "
            f"answer in ans{sheet}.tex could ever fail it.\n"
            f"  .tex prints: {raw}\n"
            f"  Return the value you verified, or assert against get_answer()."
        )
        return

    published = parse_tex_math(raw)
    result = bind(raw, published, computed)

    assert result.ok, (
        f"{pillar}/sheet{sheet} {label}: the verification does not agree with "
        f"the published answer.\n"
        f"  .tex prints: {raw}\n"
        f"  check gives: {computed!r}\n"
        f"  {result.detail}"
    )
    assert result.kind in (EXACT, DRIFT_ONLY, EXEMPT)
