"""The sheet, its answer key and its checks must describe the same questions."""

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.check_sheet_consistency import check  # noqa: E402
from tools.check_binding import included_drafts, published_sheets  # noqa: E402

STEM = r"The line $y=2x+1$ meets the $x$-axis at $P$. Find the $x$-coordinate of $P$."
OPTIONS = r"""\begin{itemize}
\item[A)] $-\tfrac12$
\item[B)] $\tfrac12$
\item[C)] $1$
\item[D)] $2$
\end{itemize}"""
CHECK = '''
from fractions import Fraction
def check_C1():
    options = {"A": Fraction(-1, 2), "B": Fraction(1, 2), "C": 1, "D": 2}
    x = Fraction(-1, 2)
    assert [k for k, v in options.items() if v == x] == ["A"]
    return "A"
'''


def _pillar(tmp_path, items, answers, check=CHECK):
    """A one-sheet pillar in tmp_path/demo; items/answers are the Section C bodies."""
    base = tmp_path / "demo"
    for sub in ("sheets", "answers", "verify"):
        (base / sub).mkdir(parents=True)
    (base / "sheets" / "sheet01.tex").write_text(
        "\\section*{Section C \\quad Structure}\n\\begin{enumerate}\n"
        + "\n".join(items) + "\n\\end{enumerate}\n\\SpeedClosing{x}\n", encoding="utf-8")
    (base / "answers" / "ans01.tex").write_text(
        "\\section*{Section C \\quad Structure}\n\\begin{enumerate}\n"
        + "\n".join(answers) + "\n\\end{enumerate}\n\\end{document}\n", encoding="utf-8")
    (base / "verify" / "sheet01_verify.py").write_text(check, encoding="utf-8")
    return tmp_path


def _rules(problems):
    return sorted({p.split(": ")[1] for p in problems})


def test_consistent_pillar_passes(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"],
                   [f"\\item {STEM}\n\\ans{{A) $-\\tfrac12$}}\n\\method{{m}}"])
    assert check("demo", root=root) == []


def test_answer_without_letter_is_flagged(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"],
                   ["\\item \\ans{$-\\tfrac12$}"])
    assert _rules(check("demo", root=root)) == ["letter"]


def test_equal_option_values_are_flagged(tmp_path):
    opts = OPTIONS.replace(r"\item[D)] $2$", r"\item[D)] $\tfrac{2}{4}$")
    chk = CHECK.replace('"D": 2', '"D": Fraction(1, 2)')
    root = _pillar(tmp_path, [f"\\item {STEM}\n{opts}"], ["\\item \\ans{A) $-\\tfrac12$}"], chk)
    assert _rules(check("demo", root=root)) == ["distinct"]


def test_equal_values_behind_a_parenthetical_are_flagged(tmp_path):
    opts = (r"\begin{itemize}" "\n"
            r"\item[A)] $\tfrac{1}{\sqrt5}$ (inside)" "\n"
            r"\item[B)] $\tfrac{\sqrt5}{5}$ (inside)" "\n"
            r"\item[C)] $1$ (tangent)" "\n"
            r"\end{itemize}")
    chk = 'def check_C1():\n    options = {}\n    return "C"\n'
    root = _pillar(tmp_path, [f"\\item {STEM}\n{opts}"], ["\\item \\ans{C) $1$ (tangent)}"], chk)
    assert "distinct" in _rules(check("demo", root=root))


def test_prose_options_sharing_leading_maths_are_not_equal(tmp_path):
    opts = (r"\begin{itemize}" "\n"
            r"\item[A)] $x$ has two possible values whose difference is $5$" "\n"
            r"\item[B)] $x$ has only one value" "\n"
            r"\end{itemize}")
    chk = 'def check_C1():\n    options = {}\n    return "A"\n'
    root = _pillar(tmp_path, [f"\\item {STEM}\n{opts}"],
                   ["\\item \\ans{A) $x$ has two possible values whose difference is $5$}"], chk)
    assert check("demo", root=root) == []


def test_restated_stem_with_different_data_is_flagged(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"],
                   [f"\\item {STEM.replace('2x+1', '2x+3')}\n\\ans{{A) $-\\tfrac12$}}"])
    assert _rules(check("demo", root=root)) == ["restated-stem"]


def test_restated_stem_reworded_with_same_maths_passes(tmp_path):
    reworded = STEM.replace("meets the", "crosses the")
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"],
                   [f"\\item {reworded}\n\\ans{{A) $-\\tfrac12$}}"])
    assert check("demo", root=root) == []


def test_restated_option_that_differs_is_flagged(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"],
                   [f"\\item {STEM}\n{OPTIONS.replace('$1$', '$3$')}\n\\ans{{A) $-\\tfrac12$}}"])
    assert _rules(check("demo", root=root)) == ["restated-options"]


def test_check_options_that_disagree_with_the_sheet_are_flagged(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"], ["\\item \\ans{A) $-\\tfrac12$}"],
                   CHECK.replace('"C": 1', '"C": 3'))
    assert _rules(check("demo", root=root)) == ["check-options"]


def test_mcq_check_without_options_dict_is_flagged(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"], ["\\item \\ans{A) $-\\tfrac12$}"],
                   'def check_C1():\n    return "A"\n')
    assert _rules(check("demo", root=root)) == ["check-options-missing"]


def test_duplicate_questions_are_flagged(tmp_path):
    item = f"\\item {STEM}\n{OPTIONS}"
    chk = CHECK + CHECK.replace("check_C1", "check_C2")
    root = _pillar(tmp_path, [item, item],
                   ["\\item \\ans{A) $-\\tfrac12$}", "\\item \\ans{A) $-\\tfrac12$}"], chk)
    assert _rules(check("demo", root=root)) == ["duplicate"]


def test_letter_balance_only_when_asked(tmp_path):
    items, answers, chk = [], [], ""
    for i in range(1, 5):
        s = STEM.replace("2x+1", f"2x+{i}")
        items.append(f"\\item {s}\n" + OPTIONS.replace("-\\tfrac12", f"-\\tfrac{{{i}}}{{2}}"))
        answers.append(f"\\item \\ans{{A) $-\\tfrac{{{i}}}{{2}}$}}")
        chk += CHECK.replace("check_C1", f"check_C{i}").replace("Fraction(-1, 2)", f"Fraction(-{i}, 2)")
    root = _pillar(tmp_path, items, answers, chk)
    assert check("demo", root=root) == []
    assert "balance" in _rules(check("demo", root=root, balance=True))


def test_sheet_filter_limits_per_question_rules(tmp_path):
    root = _pillar(tmp_path, [f"\\item {STEM}\n{OPTIONS}"], ["\\item \\ans{$-\\tfrac12$}"])
    assert check("demo", sheets={"02"}, root=root) == []


def test_included_drafts_reads_environment(monkeypatch):
    monkeypatch.setenv("SPEEDMATHS_INCLUDE_DRAFTS", "geometry, calculus")
    assert included_drafts() == {"geometry", "calculus"}
    monkeypatch.delenv("SPEEDMATHS_INCLUDE_DRAFTS")
    assert included_drafts() == set()


def test_published_sheets_includes_opted_in_draft(monkeypatch, tmp_path):
    # A throwaway repo with one draft pillar: no real pillar is a draft with sheets any more.
    import tools.check_binding as cb
    (tmp_path / "sheets.json").write_text(json.dumps([{"slug": "demo", "status": "draft", "sheets": [{"n": "01"}]}]))
    (tmp_path / "demo" / "verify").mkdir(parents=True)
    (tmp_path / "demo" / "verify" / "sheet01_verify.py").write_text("")
    monkeypatch.setattr(cb, "REPO_ROOT", tmp_path)
    monkeypatch.delenv("SPEEDMATHS_INCLUDE_DRAFTS", raising=False)
    assert not any(p == "demo" for p, _, _ in published_sheets())
    monkeypatch.setenv("SPEEDMATHS_INCLUDE_DRAFTS", "demo")
    assert any(p == "demo" for p, _, _ in published_sheets())


def test_equations_with_the_same_right_hand_side_are_not_equal(tmp_path):
    opts = (r"\begin{itemize}" "\n"
            r"\item[A)] $5x-3y=1$" "\n"
            r"\item[B)] $5x+3y=1$" "\n"
            r"\item[C)] $x^2+y^2-6x+4y-3=0$" "\n"
            r"\item[D)] $x^2+y^2+6x-4y-3=0$" "\n"
            r"\end{itemize}")
    chk = 'def check_C1():\n    options = {}\n    return "A"\n'
    root = _pillar(tmp_path, [f"\\item {STEM}\n{opts}"], ["\\item \\ans{A) $5x-3y=1$}"], chk)
    assert check("demo", root=root) == []


def test_check_value_is_only_compared_with_a_numeric_option(tmp_path):
    opts = (r"\begin{itemize}" "\n"
            r"\item[A)] $y=-\tfrac32x+1$" "\n"
            r"\item[B)] $\tfrac{16-\pi}{24}$" "\n"
            r"\end{itemize}")
    chk = ('import sympy\n'
           'def check_C1():\n'
           '    options = {"A": sympy.Rational(-3, 2), "B": sympy.Rational(2, 3) - sympy.pi / 24}\n'
           '    return "A"\n')
    root = _pillar(tmp_path, [f"\\item {STEM}\n{opts}"], ["\\item \\ans{A) $y=-\\tfrac32x+1$}"], chk)
    assert check("demo", root=root) == []


LIVE_CONSISTENT = ["geometry"]


@pytest.mark.parametrize("pillar", LIVE_CONSISTENT)
def test_live_pillar_is_consistent(pillar):
    assert check(pillar, balance=True) == []
