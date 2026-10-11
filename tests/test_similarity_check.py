import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import similarity_check as sc  # noqa: E402

SOURCE = (r"A tangent to the circle $x^2 + y^2 = 144$ passes through the point $(20, 0)$ and "
          r"crosses the positive $y$-axis. What is the value of $y$ at the point where the "
          r"tangent meets the $y$-axis?")


@pytest.fixture
def json_corpus(tmp_path):
    # the real banks store the stem under "text" and the options as a list of dicts
    (tmp_path / "official.json").write_text(json.dumps([{"id": "official-2017-p1-q6", "text": SOURCE,
                                                         "options": [{"letter": "A", "text": "$12$"}]}]))
    (tmp_path / "open.json").write_text(json.dumps({"questions": [{"id": "mock-q1", "question": "Unrelated."}]}))
    return tmp_path


def _run(tex, json_dir, tmp_path):
    f = tmp_path / "sheet.tex"
    f.write_text(tex)
    # No research/txt, as in CI: the papers are copyright and never committed.
    out = subprocess.run([sys.executable, str(Path(sc.__file__)), str(f), "--json-corpus", str(json_dir),
                          "--txt-corpus", str(tmp_path / "no-txt")],
                         capture_output=True, text=True)
    return out.stdout


def test_json_corpus_loads_each_question_as_a_document(json_corpus):
    corpus = sc.load_json_corpus(json_corpus)
    assert set(corpus) == {"official.json:official-2017-p1-q6", "open.json:mock-q1"}
    assert corpus["official.json:official-2017-p1-q6"][-1] == "12"          # options are part of the document


def test_credited_verbatim_copy_is_flagged(json_corpus, tmp_path):
    tex = ("\\begin{enumerate}\n\\item " + SOURCE + r" \textit{\small(after TMUA 2017 Paper 1 Q6)}"
           "\n\\end{enumerate}\n")
    out = _run(tex, json_corpus, tmp_path)
    assert "official.json:official-2017-p1-q6" in out
    assert "near-verbatim" in out


def test_reworded_copy_with_the_same_data_is_flagged(json_corpus, tmp_path):
    # Same circle, point and options as the source; every sentence reworded.
    tex = ("\\begin{enumerate}\n\\item Some line touching $x^2+y^2=144$ goes through $(20,0)$ and hits the upper "
           r"half of the vertical axis at $T$. Find $T$'s height. \textit{\small(after TMUA 2017 Paper 1 Q6)}"
           "\n\\begin{itemize}\n\\item[A)] $12$\n\\item[B)] $15$\n\\item[C)] $\\tfrac{49}{3}$\n\\item[D)] $20$\n"
           "\\end{itemize}\n\\end{enumerate}\n")
    (json_corpus / "official.json").write_text(json.dumps([{"id": "official-2017-p1-q6", "text": SOURCE,
        "options": [{"text": t} for t in ("$12$", "$15$", "$\\frac{49}{3}$", "$20$", "$\\frac{64}{3}$")]}]))
    out = _run(tex, json_corpus, tmp_path)
    assert "[data]" in out and "official.json:official-2017-p1-q6" in out


def test_real_perturbation_is_not_flagged(json_corpus, tmp_path):
    tex = ("\\begin{enumerate}\n\\item The tangents from $P(0,t)$ to $x^2+y^2=144$ touch it at points "
           "$12$ apart along the chord of contact. Find every possible value of $t$, and say which one "
           r"gives the larger kite formed with the centre. \textit{\small(after TMUA 2017 Paper 1 Q6)}"
           "\n\\end{enumerate}\n")
    out = _run(tex, json_corpus, tmp_path)
    assert "near-verbatim" not in out and "REVIEW" not in out


def test_diagram_coordinates_are_not_data(json_corpus, tmp_path):
    # TikZ coordinates and an answer-key tail share number runs, but that is not copying.
    (json_corpus / "open.json").write_text(json.dumps([{"id": "mock-q20", "text": "Find x. 21 Answer key 3 4 5 6 7 8 9 10 11"}]))
    tex = ("\\begin{enumerate}\n\\item Prove that every face is acute.\n\\begin{tikzpicture}\n"
           "\\draw (3,4) -- (5,6) -- (7,8) -- (9,10) -- (11,3);\n\\end{tikzpicture}\n\\end{enumerate}\n")
    assert "[data]" not in _run(tex, json_corpus, tmp_path)


def test_number_runs_common_across_the_bank_do_not_count(tmp_path):
    # Runs that many bank questions share (answer-key tails, pi/3-style options) are not evidence of copying.
    bank = [{"id": f"q{i}", "text": f"Answer key {i} 3 4 5 6 7 8"} for i in range(40)]
    bank.append({"id": "src", "text": "Circle 144 through 20 options 12 15 49 3 20"})
    (tmp_path / "open.json").write_text(json.dumps(bank))
    tex = "\\begin{enumerate}\n\\item Numbers 3 4 5 6 7 8 and then 97.\n\\end{enumerate}\n"
    assert "[data]" not in _run(tex, tmp_path, tmp_path)


def test_a_long_source_that_merely_contains_the_numbers_is_not_a_match(tmp_path):
    # A bank entry with a 100-number answer table contains almost any short run of numbers.
    table = " ".join(str(n) for n in range(3, 400))
    (tmp_path / "open.json").write_text(json.dumps([{"id": "keytable", "text": "Answer key " + table},
                                                          {"id": "other", "text": "Solve 77 and 55 and 99 for 88"}]))
    tex = "\\begin{enumerate}\n\\item Take 17 18 19 20 21 and 22.\n\\end{enumerate}\n"
    assert "[data]" not in _run(tex, tmp_path, tmp_path)


def test_lightly_reworded_copy_is_flagged_against_the_bank(json_corpus, tmp_path):
    # Every sixth word or so changed: no 8-word run survives, but 5-word runs do.
    tex = ("\\begin{enumerate}\n\\item A tangent to the circle $x^2 + y^2 = 144$ goes through the point "
           "$(20, 0)$ and then crosses the positive $y$-axis. Find the value of $y$ at the point where "
           "this tangent meets the $y$-axis.\n\\end{enumerate}\n")
    out = _run(tex, json_corpus, tmp_path)
    assert "[bank]" in out and "official.json:official-2017-p1-q6" in out
