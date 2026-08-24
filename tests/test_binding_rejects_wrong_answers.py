"""Negative controls for the comparison layer.

test_answer_binding.py only ever shows `bind()` correct values. On its own that
is not enough: a comparison that returned True unconditionally would pass all
1,155 cases. Then the one thing standing between a wrong `\\ans{}` and a green
build would itself be unverified, which is the same mistake as the checks that
fetch their answer key and ignore it — just moved one level down.

So these tests do the opposite. For every published answer, perturb it and
require `bind()` to reject it. That is what gives the mutation suite something
to kill in tools/answer_binding.py: break the comparison and these fail.
"""

import re
import sys
from pathlib import Path

import pytest
import sympy

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.answer_binding import (  # noqa: E402
    DRIFT_ONLY, EXACT, EXEMPT, as_tuple_list, bind, is_proof_marker, mcq_letter,
    normalise_prose,
)
from tools.latex_bridge import extract_tex_answers, parse_tex_math  # noqa: E402

PILLARS = ["algebra", "combinatorics", "logic", "number-theory", "sequences"]


def _every_answer():
    for pillar in PILLARS:
        for n in range(1, 8):
            tex = REPO_ROOT / pillar / "answers" / f"ans{n:02d}.tex"
            if not tex.exists():
                continue
            for label, raw in sorted(extract_tex_answers(str(tex)).items()):
                yield pytest.param(raw, id=f"{pillar}/sheet{n:02d}:{label}")


def _perturb(published):
    """A value that is definitely not the published answer."""
    if isinstance(published, bool):
        return not published
    if isinstance(published, str):
        return "certainly not the published answer"
    if isinstance(published, (list, tuple)):
        return [sympy.Integer(987654321)] * len(published)
    try:
        return sympy.sympify(published) + sympy.Integer(987654321)
    except Exception:
        return None


@pytest.mark.parametrize("raw", list(_every_answer()))
def test_a_wrong_value_is_rejected(raw):
    published = parse_tex_math(raw)
    if is_proof_marker(raw):
        # Nothing to compare; documented as EXEMPT rather than silently passing.
        assert bind(raw, published, "anything at all").kind == EXEMPT
        return
    wrong = _perturb(published)
    if wrong is None:
        pytest.skip("answer shape cannot be perturbed mechanically")
    result = bind(raw, published, wrong)
    assert not result.ok, (
        f"bind() accepted a wrong value for {raw!r}: it treated {wrong!r} as "
        f"matching, so a wrong answer key would pass CI"
    )


@pytest.mark.parametrize("raw", list(_every_answer()))
def test_the_published_value_is_accepted(raw):
    """The other direction, so a comparison that rejects everything also fails."""
    published = parse_tex_math(raw)
    if is_proof_marker(raw):
        return
    if mcq_letter(raw):
        expected = mcq_letter(raw)
    elif as_tuple_list(raw) is not None:
        # A solution set binds as numbers, so the value a check should produce is
        # the tuples themselves.
        expected = as_tuple_list(raw)
    elif isinstance(published, bool):
        # A True/False answer binds as a bool, which is stronger than comparing
        # the word, so a check for one of these must return a bool.
        expected = published
    elif not re.search(r"\$|\\[a-zA-Z]", raw):
        # Plain prose. The value a check should produce is the wording itself,
        # not whatever parse_latex made of it — it mangles prose into products
        # of one-letter symbols.
        expected = raw
    else:
        expected = published
    assert bind(raw, published, expected).ok, (
        f"bind() rejected the published answer {raw!r} compared against itself"
    )


def test_returning_nothing_is_never_a_match():
    assert not bind("$42$", sympy.Integer(42), None).ok


def test_mcq_binds_on_the_letter_not_the_prose():
    raw = "C) $n=17$."
    published = parse_tex_math(raw)
    assert bind(raw, published, "C").ok
    assert not bind(raw, published, "B").ok
    # The value inside the option is not the answer; the option is.
    assert not bind(raw, published, sympy.Integer(17)).ok


def test_mcq_letter_reads_both_spellings():
    assert mcq_letter("A) none of them") == "A"
    assert mcq_letter("(B) something") == "B"
    assert mcq_letter("c") == "C"
    assert mcq_letter(sympy.Symbol("D")) == "D"
    assert mcq_letter("17") is None
    assert mcq_letter(None) is None


def test_prose_only_ever_reports_drift():
    raw = "All integers $n\\geq 1$."
    published = parse_tex_math(raw)
    result = bind(raw, published, "All integers $n \\geq 1$")
    assert result.ok and result.kind == DRIFT_ONLY, (
        "a prose answer can only be checked for drift; claiming EXACT would "
        "overstate what was verified"
    )
    assert not bind(raw, published, "All integers n >= 2").ok


def test_numeric_equality_is_mathematical_not_structural():
    x = sympy.Symbol("x")
    raw = "$x^2-1$"
    published = parse_tex_math(raw)
    assert bind(raw, published, (x - 1) * (x + 1)).ok, (
        "equivalent-but-differently-written answers must bind, or every "
        "factorised answer becomes a false failure"
    )
    assert not bind(raw, published, (x - 1) * (x + 2)).ok


def test_list_answers_do_not_bind_to_a_single_value():
    raw = "$x=5$ or $x=-2$"
    published = parse_tex_math(raw)
    assert isinstance(published, list)
    assert not bind(raw, published, sympy.Integer(5)).ok
    assert bind(raw, published, [sympy.Integer(5), sympy.Integer(-2)]).ok
    assert bind(raw, published, [sympy.Integer(-2), sympy.Integer(5)]).ok, (
        "order is not meaningful in an 'or' answer"
    )
    assert not bind(raw, published, [sympy.Integer(5), sympy.Integer(2)]).ok


def test_bool_answers_compare_as_bools():
    assert bind("True", True, True).ok
    assert not bind("True", True, False).ok


def test_normalise_prose_folds_latex_spelling_but_not_content():
    assert normalise_prose("$k=\\tfrac{1}{2}$") == normalise_prose("$k= 1 2 $")
    assert normalise_prose("all integers") != normalise_prose("no integers")


def test_solution_tuples_bind_as_numbers_not_text():
    raw = r"$(4,12), (6,6), (12,4)$"
    published = parse_tex_math(raw)
    got = [(4, 12), (6, 6), (12, 4)]
    result = bind(raw, published, got)
    assert result.ok and result.kind == EXACT, (
        "a Diophantine solution set must compare as numbers; comparing it as "
        "prose would force every check to echo the printed spelling"
    )
    # Order is not meaningful in a solution set.
    assert bind(raw, published, [(12, 4), (4, 12), (6, 6)]).ok
    # But membership and multiplicity are.
    assert not bind(raw, published, [(4, 12), (6, 6)]).ok
    assert not bind(raw, published, [(4, 12), (6, 6), (12, 5)]).ok
    assert not bind(raw, published, [(4, 12), (6, 6), (6, 6)]).ok


def test_a_lone_solution_tuple_may_be_returned_bare():
    raw = "$(3,2)$"
    published = parse_tex_math(raw)
    assert bind(raw, published, (3, 2)).ok
    assert bind(raw, published, [(3, 2)]).ok
    assert not bind(raw, published, (2, 3)).ok
    assert not bind(raw, published, (3, 2, 1)).ok


def test_tuples_embedded_in_prose_are_not_half_read():
    # Anything beyond tuples and separators must fall through to the prose path,
    # rather than being silently reduced to the tuples it happens to contain.
    assert as_tuple_list("$(1,2)$") == [(1, 2)]
    assert as_tuple_list("$(1,2), (3,4)$") == [(1, 2), (3, 4)]
    assert as_tuple_list("exactly one solution, $(1,2)$") is None
    assert as_tuple_list("$x=5$") is None
    assert as_tuple_list("Proof: see method.") is None


def test_exact_is_reported_for_values_and_drift_for_prose():
    assert bind("$7$", parse_tex_math("$7$"), sympy.Integer(7)).kind == EXACT
    assert bind("Some words", "Some words", "Some words").kind == DRIFT_ONLY
