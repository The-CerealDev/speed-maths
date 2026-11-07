"""The archive offers each sheet's Speed Sheet; the classic view keeps the originals."""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import build_website  # noqa: E402


@pytest.fixture
def site(tmp_path, monkeypatch):
    sheets, answers = tmp_path / "algebra" / "sheets", tmp_path / "algebra" / "answers"
    sheets.mkdir(parents=True)
    answers.mkdir()
    (sheets / "sheet01.tex").write_text(
        "\\SpeedMeta{Topic}{tool}\n\\begin{enumerate}\\item Q\\end{enumerate}\n", encoding="utf-8")
    for f in (sheets / "sheet01.pdf", sheets / "sheet01-speed.pdf", answers / "ans01.pdf"):
        f.write_bytes(b"%PDF")
    monkeypatch.setattr(build_website, "ROOT_DIR", str(tmp_path))
    return tmp_path


def _algebra():
    return next(p for p in build_website.scan() if p["slug"] == "algebra")


def test_scan_does_not_count_speed_sheet_as_a_sheet(site):
    alg = _algebra()
    assert [s["n"] for s in alg["sheets"]] == ["01"]
    assert alg["sheets"][0]["speed"] == "algebra/sheets/sheet01-speed.pdf"


def test_archive_row_offers_speed_sheet_and_answers(site):
    html = build_website.render_rows(_algebra())
    assert ">Speed Sheet</a>" in html and "sheet01-speed.pdf" in html
    assert ">Answers</a>" in html and ">Questions</a>" not in html


def test_archive_row_falls_back_to_questions_without_a_speed_sheet(site):
    (site / "algebra" / "sheets" / "sheet01-speed.pdf").unlink()
    html = build_website.render_rows(_algebra())
    assert ">Questions</a>" in html and "Speed Sheet" not in html
