# Speed Sheet Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a "Speed Sheet" PDF for every published sheet (answers hidden in the margin, each linking to its worked answer) and make it the default download on the archive site.

**Architecture:** No new `.tex` per sheet. `tools/build_speed_sheets.py` compiles each existing `ansNN.tex` with a command-line prelude that sets three macros and, via `\AtBeginDocument`, inputs `shared/speed.tex`, which overrides `\ans`, `\method`, `\inv`, `\SpeedTitleBlock`, `\section*` and top-level `\item`. Links target hyperref's existing `Item.N` destinations in the published answers PDFs. Checks read the built PDFs with `qpdf --json` (links) and `pdftotext -bbox` (layout).

**Tech Stack:** pdfLaTeX (TeX Live), Python 3 stdlib + pytest, `qpdf` and `poppler-utils` (both apt; `qpdf` is new to CI).

**Spec:** `docs/superpowers/specs/2026-11-07-speed-sheet-design.md`

## Global Constraints

- Output: `<pillar>/sheets/sheetNN-speed.pdf`, A4, compiled from `<pillar>/answers/ansNN.tex` with no edits to any existing `.tex`, `shared/preamble.tex` or answers PDF.
- Working space under each question: Section A 3cm, B 4.5cm, C 6cm, D 7cm. Before the first "Section …" heading (or with none, e.g. `number-theory` Day 3): 3cm.
- Answer: text `Ans: <answer>`, `\rotatebox{180}`, `\fontsize{4}{5}`, colour `black!22`, right edge 16mm into the 22mm right margin (6mm from the paper edge).
- Link URL: `https://speedmaths.co.uk/<pillar>/answers/ansNN.pdf#nameddest=Item.<N>`, N = the question's number in the answers file.
- Tap area of each link: at least 15mm wide and 5mm tall (Claude's call; the text itself stays 4pt).
- Title: the answers title with `Answers \& Investigations` replaced by `Speed Sheet`.
- Not printed: `\method`, `\inv`, and everything from the first starred section that is not "Section A–D" (Top 5 Patterns, Common Traps, `\SpeedClosing`) to the end.
- Keep together: never break a page between a question and its working space; never leave a section heading at the bottom of a page.
- Archive site (`index.html`): **Speed Sheet** replaces **Questions**; **Answers** stays. `classic.html` unchanged. `sheetNN.pdf` stays hosted.
- PDFs are built locally and committed (repo convention); CI rebuilds and flags, never pushes.

## Review Focus

1. `number-theory/answers/ans03.tex` has no Section A–D headings: it must still build with 33 links, 3cm spaces, and no "Top 5 Patterns". Tests: Task 2 (builds, nothing cut early) and Task 4 `--check` (33 links).
2. Answers wider than 16mm (long expressions, prose): the box must shift left into the text area, never off the paper. Checked by `check()` in Task 3 (every link's right edge ≤ page width − 3mm), run on all 42 in Task 4.
3. Geometry sheets add `\input{../geometry-preamble}` and TikZ figures inside questions: must build and pass checks. Test in Task 2 (build geometry 01).
4. MCQ options (`itemize`) and `\item[...]` labels inside a question must not get keep-together breaks or step the link number. Test in Task 3 (links are exactly `Item.1…Item.33` in order).
5. A future answers file that nests a numbered `enumerate` inside a question would shift every later link. Guard in Task 1.

---

### Task 1: Source guards and builder skeleton

**Files:**
- Create: `tools/build_speed_sheets.py`
- Test: `tests/test_speed_sheets.py`

**Interfaces:**
- Produces:
  - `answer_item_numbers(tex: str) -> list[int]`: for each `\ans{` in order, the number of numbered top-level `enumerate` items before it (count `\item` only when the innermost open environment is `enumerate` and it has no `[...]` label; ignore `%` comments). A clean file returns `[1, 2, …, 33]`.
  - `speed_title(tex: str) -> str`: the first `\SpeedTitleBlock` argument with `Answers \& Investigations` replaced by `Speed Sheet`; raises `ValueError` if that phrase is absent.
  - `SpeedJob` (frozen dataclass): `pillar: str`, `n: str` (e.g. `"01"`), `answers_tex: Path`, `out_pdf: Path`, `url: str`, `title: str`.
  - `jobs(root: Path, pillars: Iterable[str]) -> list[SpeedJob]`: one per `<pillar>/answers/ansNN.tex` that has a matching `<pillar>/sheets/sheetNN.tex`; `out_pdf = <pillar>/sheets/sheetNN-speed.pdf`; `url` per Global Constraints without the `#…` part.

- [ ] **Step 1: Write the failing tests**

```python
def test_answer_item_numbers_counts_only_numbered_items():
    tex = (r"\begin{enumerate}\item Q1 \begin{itemize}\item[A)] x \item[B)] y\end{itemize}"
           r"\ans{A}\item Q2 \ans{2}\end{enumerate}")
    assert answer_item_numbers(tex) == [1, 2]

def test_answer_item_numbers_catches_nested_numbered_list():
    tex = (r"\begin{enumerate}\item Q1 \begin{enumerate}\item a \item b\end{enumerate}"
           r"\ans{1}\item Q2 \ans{2}\end{enumerate}")
    assert answer_item_numbers(tex) != [1, 2]

@pytest.mark.parametrize("path", sorted(REPO_ROOT.glob("*/answers/ans*.tex")), ids=str)
def test_every_answers_file_maps_question_n_to_item_n(path):
    nums = answer_item_numbers(path.read_text(encoding="utf-8"))
    assert nums == list(range(1, len(nums) + 1))

def test_speed_title():
    tex = r"\SpeedTitleBlock{Daily Logic Drill \#2 --- Answers \& Investigations}{David}"
    assert speed_title(tex) == r"Daily Logic Drill \#2 --- Speed Sheet"

def test_jobs_algebra_01():
    j = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "01")
    assert j.out_pdf == REPO_ROOT / "algebra/sheets/sheet01-speed.pdf"
    assert j.url == "https://speedmaths.co.uk/algebra/answers/ans01.pdf"
    assert len(jobs(REPO_ROOT, ["algebra"])) == 7
```

- [ ] **Step 2: Run** `.venv/bin/python -m pytest tests/test_speed_sheets.py -q`. Expected: FAIL, `ModuleNotFoundError: tools.build_speed_sheets`.
- [ ] **Step 3: Implement the four interfaces** in `tools/build_speed_sheets.py` (module docstring in the repo's style: say *why* there is no second `.tex`). `answer_item_numbers` is a single regex scan over `\begin{…}`, `\end{…}`, `\item`, `\item[` and `\ans{` keeping an environment stack.
- [ ] **Step 4: Run** the same command. Expected: all pass (the 42-file guard passes today; checked 2026-11-07).
- [ ] **Step 5: Commit** `feat(speed): source guards and job list for Speed Sheets`.

### Task 2: `shared/speed.tex` and the build

**Files:**
- Create: `shared/speed.tex`
- Modify: `tools/build_speed_sheets.py`
- Test: `tests/test_speed_sheets.py`

**Interfaces:**
- Consumes: `SpeedJob`, `jobs` (Task 1).
- Produces:
  - `build(job: SpeedJob, out_dir: Path | None = None) -> Path`: runs, from `job.answers_tex.parent`, `pdflatex -interaction=nonstopmode -halt-on-error -jobname=sheetNN-speed -output-directory=<out_dir or job.out_pdf.parent> "<prelude>\input{ansNN.tex}"` twice, removes `.aux/.log/.out` on success, raises `RuntimeError` (with the log tail) on failure, returns the PDF path. Prelude: `\def\SpeedAnsURL{<url>}\def\SpeedSheetTitle{<title>}\AtBeginDocument{\input{<absolute path to shared/speed.tex>}}`.
  - CLI: `python3 tools/build_speed_sheets.py [ansNN.tex …]` builds the given files, or all live pillars (`PILLARS` from `tools/build_website.py`, status `live`) with none.
  - Macros consumed by `speed.tex`: `\SpeedAnsURL`, `\SpeedSheetTitle`.
  - Test helpers in `tests/test_speed_sheets.py`: `needs_tex = pytest.mark.skipif(shutil.which("pdflatex") is None, reason="needs pdflatex")` and `pdftotext(pdf: Path) -> str` (runs `pdftotext <pdf> -`).

`shared/speed.tex` is input at `\begin{document}`, so it cannot `\usepackage`; graphicx, hyperref, xcolor and enumitem are already loaded by the preamble. What it must do (the non-obvious parts as code):

```latex
\makeatletter
\newlength{\SpeedSpace}\setlength{\SpeedSpace}{3cm}
% \Needspace without the package: break now if less than #1 is left on the page
\newcommand{\Speed@need}[1]{\par\penalty-100\begingroup\dimen@=#1\relax
  \dimen@ii=\pagegoal\advance\dimen@ii-\pagetotal
  \ifdim\dimen@>\dimen@ii\ifdim\dimen@ii>\z@\break\fi\fi\endgroup}
% Keep each top-level question with its space; MCQ options and sub-parts sit at \@listdepth>1
\let\Speed@item\item
\renewcommand{\item}{\ifnum\@listdepth=\@ne\Speed@need{\dimexpr\SpeedSpace+3cm\relax}\fi\Speed@item}
% \section*: "Section A|B|C|D ..." sets the space and keeps the heading with a question;
% any other starred section (Top 5 Patterns ...) ends the document there.
\let\Speed@section\section
\renewcommand{\section}{\@ifstar\Speed@ssection\Speed@section}
\newcommand{\Speed@ssection}[1]{\Speed@setspace{#1}...}  % \in@{Section A}{#1} etc.; else \end{document}
\makeatother
```

`\Speed@setspace` sets 3/4.5/6/7cm for A/B/C/D, calls `\Speed@need{\dimexpr\SpeedSpace+6cm\relax}`, then `\Speed@section*{#1}`. `\ans` adds `\vspace{\SpeedSpace}`, then puts `\href{\SpeedAnsURL\#nameddest=Item.\arabic{Item}}{…}` around a box at least 15mm×5mm whose right-aligned content is the rotated answer, placed with `\hfill\rlap{\hspace{\dimexpr16mm-\wd<box>\relax}<box>}`. `\method` and `\inv` gobble their argument. `\SpeedTitleBlock` keeps its layout but prints `\SpeedSheetTitle`.

- [ ] **Step 1: Write the failing tests** (skip when `shutil.which("pdflatex")` is None)

```python
@needs_tex
@pytest.mark.parametrize("pillar,n", [("algebra", "01"), ("geometry", "01"), ("number-theory", "03")])
def test_build_produces_a_clean_speed_sheet(tmp_path, pillar, n):
    job = next(j for j in jobs(REPO_ROOT, [pillar]) if j.n == n)
    text = pdftotext(build(job, out_dir=tmp_path))
    assert "Speed Sheet" in text
    for gone in ("Method:", "Investigate further", "Top 5 Patterns", "Common Traps"):
        assert gone not in text
    assert not list(job.answers_tex.parent.glob("sheet*-speed.*"))  # nothing left beside the source
```

- [ ] **Step 2: Run** `.venv/bin/python -m pytest tests/test_speed_sheets.py -q -k build`. Expected: FAIL (`build` undefined).
- [ ] **Step 3: Write `shared/speed.tex` and `build()`/CLI.**
- [ ] **Step 4: Run** the same. Expected: 3 passed. Open `/tmp/…/sheet01-speed.pdf` and compare page 1 with the #13 screenshot.
- [ ] **Step 5: Commit** `feat(speed): shared/speed.tex overrides and pdflatex build`.

### Task 3: PDF checks

**Files:**
- Modify: `tools/build_speed_sheets.py`
- Test: `tests/test_speed_sheets.py`

**Interfaces:**
- Consumes: `build`, `jobs`.
- Produces:
  - `Link` (frozen dataclass): `page: int`, `uri: str`, `rect: tuple[float, float, float, float]` (PDF points, x0, y0, x1, y1).
  - `links(pdf: Path) -> list[Link]`: URI link annotations in page order, from `qpdf --json`.
  - `Word` (frozen dataclass): `page: int`, `text: str`, `y: float` (top, points from page top).
  - `layout_problems(words: list[Word], page_height: float) -> list[str]`: pure. Body = words with 71 < y < page_height − 71 (25mm margins). Problems: a page after the first whose first body word is not a question number (`^\d+\.$`) or `Section`; a page whose last `Section` heading has no question number below it.
  - `words(pdf: Path) -> tuple[list[Word], float]`: parses `pdftotext -bbox`.
  - `check(job: SpeedJob, pdf: Path) -> list[str]`: link URIs must be exactly `f"{job.url}#nameddest=Item.{i}"` for i = 1…`len(answer_item_numbers(job.answers_tex.read_text()))`; each rect ≥ 42.5pt × 14.2pt; each `x1 ≤ page_width − 8.5`; plus `layout_problems`.
  - CLI `--check`: run `check` on every built Speed Sheet, print problems, exit 1 if any.

- [ ] **Step 1: Write the failing tests**

```python
def test_layout_flags_orphan_answer_page():
    ws = [Word(1, "1.", 100), Word(2, "Ans:", 100)]
    assert layout_problems(ws, 842) != []

def test_layout_flags_heading_alone_at_page_bottom():
    ws = [Word(1, "1.", 100), Word(1, "Section", 760), Word(2, "2.", 100)]
    assert layout_problems(ws, 842) != []

def test_layout_accepts_clean_pages():
    ws = [Word(1, "Section", 90), Word(1, "1.", 120), Word(2, "2.", 90)]
    assert layout_problems(ws, 842) == []

@needs_tex
def test_algebra_01_links_and_layout(tmp_path):
    job = next(j for j in jobs(REPO_ROOT, ["algebra"]) if j.n == "01")
    pdf = build(job, out_dir=tmp_path)
    ls = links(pdf)
    assert [l.uri for l in ls] == [f"{job.url}#nameddest=Item.{i}" for i in range(1, 34)]
    assert check(job, pdf) == []
```

- [ ] **Step 2: Run** `.venv/bin/python -m pytest tests/test_speed_sheets.py -q`. Expected: FAIL (names undefined).
- [ ] **Step 3: Implement** the interfaces above.
- [ ] **Step 4: Run** the same. Expected: all pass.
- [ ] **Step 5: Commit** `feat(speed): link and layout checks for Speed Sheets`.

### Task 4: Build and commit all 42

**Files:**
- Create: `<pillar>/sheets/sheetNN-speed.pdf` × 42 (algebra, combinatorics, number-theory, logic, sequences, geometry)

- [ ] **Step 1: Run** `.venv/bin/python tools/build_speed_sheets.py`. Expected: 42 PDFs, exit 0.
- [ ] **Step 2: Run** `.venv/bin/python tools/build_speed_sheets.py --check`. Expected: no problems, exit 0. Fix `speed.tex` (back to Task 2/3 tests) for any failure; never hand-edit a PDF.
- [ ] **Step 3: Spot-check** one sheet per pillar visually; send algebra 01 to David for an iPad tap test before merging.
- [ ] **Step 4: Commit** `feat(speed): Speed Sheets for all 42 published sheets`.

### Task 5: Website

**Files:**
- Modify: `tools/build_website.py` (`scan`, `render_rows`)
- Regenerate: `index.html`, `classic.html`, `sheets.json`, `sitemap.xml` (via `python3 tools/build_website.py`)
- Test: `tests/test_build_website.py`

**Interfaces:**
- Produces: each sheet dict in `scan()` gains `'speed': '<pillar>/sheets/sheetNN-speed.pdf'` or `None`; `scan()` lists only files matching `^sheet(\d+)\.pdf$` as sheets.

- [ ] **Step 1: Write the failing tests** (monkeypatch `build_website.ROOT_DIR` to a `tmp_path` tree with `algebra/sheets/sheet01.pdf`, `sheet01.tex`, `sheet01-speed.pdf`, `algebra/answers/ans01.pdf`)

```python
def test_scan_does_not_count_speed_sheet_as_a_sheet(site):
    alg = next(p for p in build_website.scan() if p["slug"] == "algebra")
    assert [s["n"] for s in alg["sheets"]] == ["01"]
    assert alg["sheets"][0]["speed"] == "algebra/sheets/sheet01-speed.pdf"

def test_archive_row_offers_speed_sheet_and_answers(site):
    alg = next(p for p in build_website.scan() if p["slug"] == "algebra")
    html = build_website.render_rows(alg)
    assert ">Speed Sheet</a>" in html and "sheet01-speed.pdf" in html
    assert ">Answers</a>" in html and ">Questions</a>" not in html
```

- [ ] **Step 2: Run** `.venv/bin/python -m pytest tests/test_build_website.py -q`. Expected: FAIL (speed sheet counted as a second sheet; no `speed` key).
- [ ] **Step 3: Implement.** In `render_rows`, the first link is **Speed Sheet** → `s['speed']` when present, else **Questions** → `s['pdf']`. `render_classic` untouched.
- [ ] **Step 4: Run** the tests, then `python3 tools/build_website.py`. Expected: pass; `git diff --stat` shows `index.html` and `sheets.json` changed, `classic.html` link targets unchanged.
- [ ] **Step 5: Commit** `feat(web): Speed Sheet is the default download on the archive`.

### Task 6: CI

**Files:**
- Modify: `.github/workflows/compile.yml`

- [ ] **Step 1:** Add `shared/speed.tex` and `tools/build_speed_sheets.py` to `on.pull_request.paths`; add `qpdf` to the apt install.
- [ ] **Step 2:** Add a step after "Compile, and compare": for every changed `*/answers/ansNN.tex` (or all of them when `shared/preamble.tex`, `shared/speed.tex` or `tools/build_speed_sheets.py` changed), run `python3 tools/build_speed_sheets.py <files>` into the working tree, compare `pdftotext` of each with `git show HEAD:<pillar>/sheets/sheetNN-speed.pdf` exactly like the existing step, copy stale ones to `/tmp/out/`, then run `python3 tools/build_speed_sheets.py --check` and fail the job on problems.
- [ ] **Step 3: Verify** `python3 -c "import yaml,sys;yaml.safe_load(open('.github/workflows/compile.yml'))"` succeeds, and run the new step's shell body locally against `algebra/answers/ans01.tex`. Expected: "current", check passes.
- [ ] **Step 4: Commit** `ci: rebuild and check Speed Sheets on PRs`.
