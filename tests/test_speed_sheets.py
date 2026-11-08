"""The Speed Sheet is the answers file recompiled, so its links must land on the right question."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.build_speed_sheets import (  # noqa: E402
    Link, Word, answer_item_numbers, answer_spaces, build, check, content, jobs, layout_problems, links,
    same_layout, speed_title)

needs_tex = pytest.mark.skipif(shutil.which("pdflatex") is None, reason="needs pdflatex")


def pdftotext(pdf: Path) -> str:
    return subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True,
                          text=True, check=True).stdout


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
    assert speed_title(tex) == r"Daily Logic Drill \#2"  # the same title as the plain sheet


def test_speed_title_rejects_unexpected_title():
    with pytest.raises(ValueError):
        speed_title(r"\SpeedTitleBlock{Daily Logic Drill \#2}{David}")


def test_jobs_algebra_01():
    j = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "01")
    assert j.out_pdf == REPO_ROOT / "algebra/sheets/sheet01-speed.pdf"
    assert j.url == "https://speedmaths.co.uk/algebra/answers/ans01.pdf"
    assert len(jobs(REPO_ROOT, ["algebra"])) == 7


@needs_tex
@pytest.mark.parametrize("pillar,n", [("algebra", "01"), ("geometry", "01"), ("number-theory", "03")])
def test_build_produces_a_clean_speed_sheet(tmp_path, pillar, n):
    job = next(j for j in jobs(REPO_ROOT, [pillar]) if j.n == n)
    text = pdftotext(build(job, out_dir=tmp_path))
    assert "Daily" in text and "Drill #" in text and "Speed Sheet" not in text
    for gone in ("Method:", "Investigate further", "Top 5 Patterns", "Common Traps"):
        assert gone not in text
    assert not list(job.answers_tex.parent.glob("sheet*-speed.*"))  # nothing left beside the source


def test_layout_flags_orphan_answer_page():
    ws = [Word(1, "1.", 100), Word(2, "Ans:", 100)]
    assert layout_problems(ws, 842) != []


def test_layout_flags_heading_alone_at_page_bottom():
    ws = [Word(1, "1.", 100), Word(1, "Section", 760), Word(2, "2.", 100)]
    assert layout_problems(ws, 842) != []


def test_layout_flags_answer_above_every_question_on_its_page():
    ws = [Word(1, "1.", 100), Word(2, "Ans:", 90), Word(2, "2.", 200)]
    assert layout_problems(ws, 842) != []


def test_layout_ignores_superscript_above_question_number():
    ws = [Word(1, "1.", 100), Word(2, "2", 95), Word(2, "4.", 99)]
    assert layout_problems(ws, 842) == []


def test_layout_accepts_clean_pages():
    ws = [Word(1, "Section", 90), Word(1, "1.", 120), Word(2, "2.", 90)]
    assert layout_problems(ws, 842) == []


@needs_tex
def test_algebra_01_links_and_layout(tmp_path):
    job = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "01")
    pdf = build(job, out_dir=tmp_path)
    answer_links = [l.uri for l in links(pdf) if l.uri.startswith(job.url)]  # footers link elsewhere
    assert answer_links == [f"{job.url}#nameddest=Item.{i}" for i in range(1, 34)]
    assert check(job, pdf) == []


@needs_tex
@pytest.mark.parametrize("pillar,n", [("geometry", "01"), ("sequences", "03"), ("logic", "03")])
def test_tall_questions_keep_their_answer_on_the_same_page(tmp_path, pillar, n):
    job = next(j for j in jobs(REPO_ROOT, [pillar]) if j.n == n)
    assert check(job, build(job, out_dir=tmp_path)) == []


def test_answer_spaces_follow_the_section_headings():
    tex = (r"\begin{enumerate}\item Q \ans{1}\end{enumerate}"
           r"\section*{Section B \quad Drills}\begin{enumerate}\item Q \ans{2}\end{enumerate}"
           r"\section*{Section D \quad Challenge}\begin{enumerate}\item Q \ans{3}\end{enumerate}")
    assert [round(x / 28.4528, 1) for x in answer_spaces(tex)] == [3.0, 4.5, 7.0]  # pt -> cm


@pytest.mark.skipif(shutil.which("qpdf") is None or shutil.which("pdftotext") is None,
                    reason="needs qpdf and pdftotext")
@pytest.mark.parametrize("job", [j for j in jobs(REPO_ROOT, ["algebra", "combinatorics", "number-theory",
                                                          "logic", "sequences", "geometry"])
                                 if j.out_pdf.exists()],
                         ids=lambda j: str(j.out_pdf.relative_to(REPO_ROOT)))
def test_committed_speed_sheet_is_clean(job):
    assert check(job, job.out_pdf) == []


@needs_tex
def test_same_layout_ignores_build_time_but_not_links(tmp_path):
    from dataclasses import replace
    job = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "02")
    a = build(job, out_dir=tmp_path / "a")
    b = build(job, out_dir=tmp_path / "b")
    moved = build(replace(job, url=job.url.replace("ans02", "ans03")), out_dir=tmp_path / "c")
    assert same_layout(a, b)
    assert not same_layout(a, moved)  # pdftotext alone cannot see a link change
    assert pdftotext(a) == pdftotext(moved)


def test_content_ignores_positions_from_a_different_tex_version():
    # CI's TeX Live sets words a fraction of a point away from a local build
    a = content([Word(1, "1.", 100.0, 110.0)], [Link(1, "u#nameddest=Item.1", (1.0, 2.0, 3.0, 4.0))])
    b = content([Word(2, "1.", 101.3, 111.2)], [Link(2, "u#nameddest=Item.1", (1.4, 2.2, 3.1, 4.5))])
    assert a == b


def test_content_sees_a_changed_link_target():
    w = [Word(1, "1.", 100.0)]
    assert content(w, [Link(1, "u#nameddest=Item.1", (0, 0, 1, 1))]) != \
        content(w, [Link(1, "u#nameddest=Item.2", (0, 0, 1, 1))])
