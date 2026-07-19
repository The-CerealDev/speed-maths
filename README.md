# Speed Maths — Daily Drill Series

TMUA & SMC preparation, built one pillar at a time: **Algebra** (done, 7 sheets),
**Combinatorics** (done, 7 sheets), **Number Theory** (not started), **Geometry** (not started).

## Structure

```
Speed-Maths/
├── shared/
│   ├── preamble.tex      ← single source of truth for header, footer,
│   │                        colours, answer/investigate boxes, title table
│   └── speed-logo.png    ← logo asset (not currently wired into the header)
├── algebra/
│   ├── sheets/           sheet01.tex … sheet07.tex  (+ compiled .pdf)
│   └── answers/          ans01.tex  … ans07.tex     (+ compiled .pdf)
├── combinatorics/
│   ├── sheets/           sheet01.tex … sheet07.tex (+ compiled .pdf)
│   └── answers/          ans01.tex  … ans07.tex     (+ compiled .pdf)
├── number-theory/
│   ├── sheets/
│   └── answers/
├── geometry/
│   ├── sheets/
│   └── answers/
├── prompts/
│   ├── AI_PROMPTS.md          ← Instructions for LLMs generating content
│   └── BUILD_CORPUS_PROMPT.md ← Instructions for LLMs scraping past papers
├── tools/
│   ├── build_website.py       ← Statically builds the frontend index.html
│   ├── compile_pdfs.sh        ← Bulk recompiles all LaTeX sheets
│   └── similarity_check.py    ← Plagiarism checker against research corpus
├── template.html              ← The HTML skeleton of the website
├── style.css                  ← CSS for the website frontend
└── index.html                 ← Auto-generated frontend (DO NOT manually edit)
```

## Website Architecture

This repository doubles as a static PDF-archive website (like PMT or MadasMaths). The website is served completely automatically without any database or client-side JavaScript.

- **`template.html`**: This is the source code for the website's layout. If you want to change the title, add a footer, or redesign the UI, edit this file.
- **`style.css`**: The extremely minimal, academic stylesheet.
- **`tools/build_website.py`**: When run, this Python script reads `template.html`, scans the repo for `.pdf` files, dynamically injects the download links, and saves the final result as `index.html`.
- **`index.html`**: The final artifact. It is automatically overwritten every time the build script runs. **Do not manually edit this file.**

## Conventions

- **Numbering:** two-digit, zero-padded (`sheet01`, not `sheet1`) so ordering
  stays correct past sheet 9.
- **Branding:** locked to `\textbf{Speed Maths:} Competition \& Exam Prep` everywhere. Edit
  `\SpeedExamLine` in `shared/preamble.tex` once if this ever needs to change.
- **Series Editor credit:** `\SpeedCredit` in `shared/preamble.tex`. This stays on every page.
- **Sheet Author credit:** Passed as the second argument to `\SpeedTitleBlock`.
- **Every sheet/answer file starts the same way:**
  ```latex
  \documentclass[11pt,a4paper]{article}
  \input{../../shared/preamble}
  \SpeedHeader{<Pillar>}{<worksheet number>}

  \begin{document}

  \SpeedTitleBlock{Daily <Pillar> Drill \#<N>}{<Author Name>}
  \noindent\textit{New toolkit today: ...}
  ```
  Answer files use `\SpeedTitleBlock{Daily <Pillar> Drill \#<N> --- Answers \& Investigations}{<Author Name>}`
  and the `\ans{}` / `\method{}` / `\inv{}` commands for each question.
- **Closing block:** every sheet/answer ends with
  `\SpeedClosing{<quote text>}` — this generates the rule/quote/cross-promo
  block consistently; don't hand-write it.
- **Compiling:** run `pdflatex` from inside the `sheets/` or `answers/`
  folder itself (the `\input{../../shared/preamble}` path is relative to
  that). If uploading to Overleaf, keep the whole `Speed-Maths/` folder
  structure intact — don't flatten it.

## Starting a new pillar

1. Copy the skeleton of `algebra/sheets/sheet01.tex`, swap `\SpeedHeader{Algebra}{1}`
   for `\SpeedHeader{Combinatorics}{1}` (etc.), and write new questions.
2. Keep the same A/B/C/D difficulty-table structure unless the pillar
   genuinely needs different section names — if so, just write the
   `tabular` directly instead of calling `\SpeedTitleBlock`.
3. Match it with an answer file using `\ans` / `\method` / `\inv`.



## Roadmap (Planned Expansions)

While the initial four pillars cover the core Olympiad syllabus (SMC / BMO1), the ultimate vision for this repository is to provide 100% comprehensive coverage of the UK university admissions ecosystem (TMUA, MAT, STEP). 

Once the core pillars are complete, the project will expand to include:
- **Speed Calculus**: Differentiation and integration (optimization, tangents, area).
- **Speed Logic**: The foundation of TMUA Paper 2 (truth tables, necessary/sufficient conditions, counterexamples).
- **Speed Sequences**: Arithmetic/geometric progressions, recurrence relations, and series.
- **Speed Graphs**: Advanced curve sketching, trigonometric identities, and function intersections.
