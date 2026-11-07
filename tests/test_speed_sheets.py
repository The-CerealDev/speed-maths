"""The Speed Sheet is the answers file recompiled, so its links must land on the right question."""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.build_speed_sheets import answer_item_numbers, jobs, speed_title  # noqa: E402


def test_answer_item_numbers_counts_only_numbered_items():
    tex = (r"\begin{enumerate}\item Q1 \begin{itemize}\item[A)] x \item[B)] y\end{itemize}"
           r"\ans{A}\item Q2 \ans{2}\end{enumerate}")
    assert answer_item_numbers(tex) == [1, 2]


def test_answer_item_numbers_catches_nested_numbered_list():
    tex = (r"\begin{enumerate}\item Q1 \begin{enumerate}\item a \item b\end{enumerate}"
           r"\ans{1}\item Q2 \ans{2}\end{enumerate}")
    assert answer_item_numbers(tex) != [1, 2]


@pytest.mark.parametrize("path", sorted(REPO_ROOT.glob("*/answers/ans*.tex")),
                         ids=lambda p: str(p.relative_to(REPO_ROOT)))
def test_every_answers_file_maps_question_n_to_item_n(path):
    nums = answer_item_numbers(path.read_text(encoding="utf-8"))
    assert nums == list(range(1, len(nums) + 1))


def test_speed_title():
    tex = r"\SpeedTitleBlock{Daily Logic Drill \#2 --- Answers \& Investigations}{David}"
    assert speed_title(tex) == r"Daily Logic Drill \#2 --- Speed Sheet"


def test_speed_title_rejects_unexpected_title():
    with pytest.raises(ValueError):
        speed_title(r"\SpeedTitleBlock{Daily Logic Drill \#2}{David}")


def test_jobs_algebra_01():
    j = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "01")
    assert j.out_pdf == REPO_ROOT / "algebra/sheets/sheet01-speed.pdf"
    assert j.url == "https://speedmaths.co.uk/algebra/answers/ans01.pdf"
    assert len(jobs(REPO_ROOT, ["algebra"])) == 7
