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
└── geometry/
    ├── sheets/
    └── answers/
```

## Conventions

- **Numbering:** two-digit, zero-padded (`sheet01`, not `sheet1`) so ordering
  stays correct past sheet 9.
- **Branding:** locked to *"Competition & Exam Prep"* everywhere. Edit
  `\SpeedExamLine` in `shared/preamble.tex` once if this ever needs to change
  — don't hand-edit individual sheets.
- **Author credit:** `\SpeedCredit` in `shared/preamble.tex`, linking
  `https://www.linkedin.com/in/cerealdev/`. Same rule — edit once, applies
  everywhere.
- **Every sheet/answer file starts the same way:**
  ```latex
  \documentclass[11pt,a4paper]{article}
  \input{../../shared/preamble}
  \SpeedHeader{<Pillar>}{<worksheet number>}

  \begin{document}

  \SpeedTitleBlock{Daily <Pillar> Drill \#<N>}
  \noindent\textit{New toolkit today: ...}
  ```
  Answer files use `\SpeedTitleBlock{Daily <Pillar> Drill \#<N> --- Answers \& Investigations}`
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

## Migration changelog (this reboot)

The original 7 algebra sheets + 7 answer files had drifted inconsistently
over time. Fixed during this migration, all silently, no question content
touched:

- **Branding split:** sheets 1–7 said *"TMUA & UKMT"*; answers 2–7 had
  already moved to *"TMUA & SMC"* while answer 1 and the Section D
  difficulty tag (all 7 sheets) were still on UKMT. Standardized to **SMC**
  everywhere, matching the majority/most recent usage.
- **Header bug:** every single file had a duplicate `\fancyhead[R]{...}`
  call (or was missing one side entirely), so **no compiled PDF ever
  actually showed both the worksheet number and the author credit
  together** — one silently overwrote the other. Fixed via one shared
  `\SpeedHeader` macro.
- **Column header drift:** table header alternated between "Topic" and
  "Focus" across files. Standardized to **"Topic"**.
- **Toolkit-line phrasing drift:** *"New Concepts:"* / *"New concepts
  today:"* / *"Toolkit:"* / *"New toolkit today:"* all appeared at
  different points. Standardized to **"New toolkit today:"**.
- **Stray file:** `ans1.tex` was sitting outside the `answers/` folder at
  the project root — moved into `algebra/answers/ans01.tex` like its
  siblings.
- **Duplicated preamble:** every file carried its own full copy of
  packages/colours/box-environments (~40 lines each). Extracted once into
  `shared/preamble.tex` so future edits (or new pillars) can't drift the
  same way again.
- **Strict Verification & Question Design:** Created a robust `CONTRIBUTING.md`
  that strictly mandates computational/script-based verification for all
  answers, and clearly defines the TMUA, MAT, SMC, and BMO1 question styles
  to guide future question generation.

All 14 files were recompiled after migration to confirm no content was lost
or altered — only structure and branding changed.
