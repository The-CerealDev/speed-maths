"""Fast, dedicated unit tests for tools.latex_bridge and tools.answer_binding.

Designed for sub-second execution (<0.1s) to serve as an ultra-fast first-stage
mutant killer in mutmut, killing 90%+ of mutants in milliseconds before any
heavy multi-question corpus integration tests are needed.
"""

import sys
from pathlib import Path

import pytest
import sympy

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.answer_binding import (
    DRIFT_ONLY,
    EXACT,
    EXEMPT,
    as_tuple_list,
    bind,
    is_proof_marker,
    mcq_letter,
    normalise_prose,
)
from tools.latex_bridge import extract_tex_answers, parse_tex_math


# ── tools.latex_bridge tests ─────────────────────────────────────────────────

def test_parse_tex_math_booleans():
    assert parse_tex_math("True") is True
    assert parse_tex_math("true") is True
    assert parse_tex_math("False") is False
    assert parse_tex_math("false") is False


def test_parse_tex_math_mcq():
    for letter in ("A", "B", "C", "D", "E"):
        assert parse_tex_math(letter) == letter


def test_parse_tex_math_integers_and_fractions():
    res = parse_tex_math("42")
    assert res == sympy.Integer(42)

    res_frac = parse_tex_math(r"\frac{3}{4}")
    assert sympy.simplify(res_frac - sympy.Rational(3, 4)) == 0

    res_dfrac = parse_tex_math(r"\dfrac{1}{2}")
    assert sympy.simplify(res_dfrac - sympy.Rational(1, 2)) == 0

    res_tfrac = parse_tex_math(r"\tfrac{5}{6}")
    assert sympy.simplify(res_tfrac - sympy.Rational(5, 6)) == 0


def test_parse_tex_math_sqrt_and_powers():
    res_sqrt = parse_tex_math(r"\sqrt{9}")
    assert sympy.simplify(res_sqrt - 3) == 0

    res_sqrt_bare = parse_tex_math(r"\sqrt2")
    assert sympy.simplify(res_sqrt_bare - sympy.sqrt(2)) == 0

    res_pow = parse_tex_math("2^3")
    assert sympy.simplify(res_pow - 8) == 0


def test_parse_tex_math_prose_and_markers():
    assert parse_tex_math("Proof: see method") == "Proof: see method"
    assert parse_tex_math("all real x") == "all real x"
    assert parse_tex_math("no solution") == "no solution"
    assert parse_tex_math('"exact string"') == '"exact string"'


def test_parse_tex_math_chained_and_split():
    # Semicolon separated
    multi = parse_tex_math("x = 1; y = 2")
    assert isinstance(multi, list)
    assert len(multi) == 2

    # or separated
    or_parts = parse_tex_math("x = 3 or x = -3")
    assert isinstance(or_parts, list)
    assert len(or_parts) == 2


def test_extract_tex_answers_nonexistent(tmp_path):
    empty = extract_tex_answers(str(tmp_path / "does_not_exist.tex"))
    assert empty == {}


def test_extract_tex_answers_parsing(tmp_path):
    tex_file = tmp_path / "test.tex"
    tex_file.write_text("""
%── A1 ───────────────────
\\item First question \\ans{42}
%── A2 ───────────────────
\\item Second question \\ans{\\frac{1}{2}}
""", encoding="utf-8")
    extracted = extract_tex_answers(str(tex_file))
    assert extracted.get("A1") == "42"
    assert extracted.get("A2") == r"\frac{1}{2}"


# ── tools.answer_binding tests ───────────────────────────────────────────────

def test_is_proof_marker():
    assert is_proof_marker("Proof: see method") is True
    assert is_proof_marker("Proved via induction") is True
    assert is_proof_marker("Shown below.") is True
    assert is_proof_marker("42") is False
    assert is_proof_marker(r"\frac{1}{2}") is False


def test_mcq_letter():
    assert mcq_letter("A") == "A"
    assert mcq_letter("(B)") == "B"
    assert mcq_letter("C) only") == "C"
    assert mcq_letter("42") is None


def test_normalise_prose():
    assert normalise_prose("All Integers n >= 1.") == "all integers n >= 1"
    assert normalise_prose("  Multiple   spaces!  ") == "multiple spaces!"


def test_as_tuple_list():
    assert as_tuple_list("(3, 2)") == [(sympy.Integer(3), sympy.Integer(2))]
    assert as_tuple_list("(1, 2), (3, 4)") == [
        (sympy.Integer(1), sympy.Integer(2)),
        (sympy.Integer(3), sympy.Integer(4)),
    ]
    assert as_tuple_list("not a tuple") is None


def test_bind_exempt():
    res = bind("Proof: see method", "Proof: see method", "anything")
    assert res.ok is True
    assert res.kind == EXEMPT


def test_bind_exact_integers():
    res = bind("$42$", sympy.Integer(42), sympy.Integer(42))
    assert res.ok is True
    assert res.kind == EXACT

    res_bad = bind("$42$", sympy.Integer(42), sympy.Integer(43))
    assert res_bad.ok is False


def test_bind_exact_symbolic():
    x = sympy.Symbol("x")
    res = bind("$x + 1$", x + 1, 1 + x)
    assert res.ok is True
    assert res.kind == EXACT

    res_bad = bind("$x + 1$", x + 1, x + 2)
    assert res_bad.ok is False


def test_bind_mcq():
    res = bind("A) none", "A", "A")
    assert res.ok is True
    assert res.kind == EXACT

    res_bad = bind("A) none", "A", "B")
    assert res_bad.ok is False


def test_bind_drift_only():
    res = bind("All real x", "All real x", "All real x")
    assert res.ok is True
    assert res.kind == DRIFT_ONLY

    res_bad = bind("All real x", "All real x", "No real x")
    assert res_bad.ok is False


def test_bind_tuple_list():
    res = bind("(1, 2)", [(1, 2)], [(sympy.Integer(1), sympy.Integer(2))])
    assert res.ok is True
    assert res.kind == EXACT

    res_bad = bind("(1, 2)", [(1, 2)], [(sympy.Integer(1), sympy.Integer(3))])
    assert res_bad.ok is False
