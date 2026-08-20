# Speed Maths

Daily drill worksheets for **TMUA**, **SMC** and **BMO1** — 35 sheets, 1,155
questions, every answer checked by a script that has to agree with it.

**📄 [Browse and download the sheets](https://the-cerealdev.github.io/speed-maths/)**

Free, open source, and made to be printed. One sheet is one sitting.

---

## Why the answers are trustworthy

Worked solutions written by hand — or by a language model — are wrong more often
than anyone admits, and a wrong answer in a revision resource is worse than no
resource at all: you lose the question *and* trust the mistake.

So every question here has a matching check in `<pillar>/verify/sheetNN_verify.py`
that computes the answer independently of the text. If the sheet says 240 and the
script says 238, the sheet does not ship.

```console
$ python3 algebra/verify/sheet01_verify.py
All 33 checks passed.
```

**1,155 questions. 1,155 checks. Currently all passing.** You can run them
yourself — they need nothing but Python, and no packages:

```console
$ python3 algebra/verify/run_all.py
All 7 sheet verify scripts passed.
```

Every check declares in its docstring whether it is an `EXHAUSTIVE PROOF` (all
cases tested) or a `SAMPLED CHECK` (spot-tested), so you can see how strong any
individual guarantee is. `tools/validate_verify_scripts.py` enforces that.

This is the whole reason the project exists. An earlier version of these sheets
was drafted through a chat window with no verification step, and some of its
solutions were confidently wrong. Everything here was rebuilt against scripts.

## What's in it

| Pillar | Sheets | Questions | Covers |
|---|---|---|---|
| **Algebra** | 7 | 231 | Polynomials, inequalities, functional equations |
| **Combinatorics** | 7 | 231 | Counting, probability, discrete structures |
| **Number Theory** | 7 | 231 | Divisibility, modular arithmetic, primes |
| **Logic** | 7 | 231 | Conditionals, proof techniques, counterexamples |
| **Sequences** | 7 | 231 | Recurrences, series, limiting behaviour |

Every sheet is the same shape, so the difficulty ramp is predictable:

| Section | Questions | Target time | What it is |
|---|---|---|---|
| **A** — Rapid Recognition | 10 | ≤ 15s each | Should be automatic |
| **B** — Manipulation Drills | 10 | ≤ 50s each | Standard technique, under time |
| **C** — Substitution & Structure | 8 | ≤ 90s each | The day's new tool |
| **D** — Challenge | 5 | — | TMUA / SMC / BMO1 difficulty |

Each sheet also comes with an answer booklet containing a full method, not just
a final value, plus an *Investigate further* prompt that extends the idea.

## How to use it

1. Download a sheet from [the archive](https://the-cerealdev.github.io/speed-maths/).
2. Do it **timed**, in one sitting, without notes.
3. Only then open the answers.

Work a pillar in order — sheet 1 to 7 — because each day's Section C introduces a
tool that later days assume you have.

## Contributing

Three doors, and the first two need no Git, no LaTeX and no Python.

### 🔴 Something is wrong

Open a [wrong answer report](https://github.com/The-CerealDev/speed-maths/issues/new?template=wrong-answer.yml).
You do not need to be certain — if it looks wrong, say so. A wrong answer key
damages someone mid-revision, so these get looked at first.

### 🧮 I have a question to add

Write it in plain text via
[propose a question](https://github.com/The-CerealDev/speed-maths/issues/new?template=new-question.yml)
and someone will handle the LaTeX. You keep the credit.

Prefer to do it yourself? Open any sheet's `.tex` on GitHub, press the edit
pencil, and choose **Propose changes** — that opens a pull request from your
browser. You will not be able to compile the PDF that way, and that is fine:
CI compiles it for you and attaches the result to your PR. Say in the PR that
you need it committed.

Two rules decide whether a question can be used at all:

- **No verbatim past-paper questions.** UKMT/TMUA/MAT papers are copyrighted
  and this repo is public. Adapt the structure, change the numbers, and credit
  the source — `(after TMUA 2019 Paper 2 Q4)`.
- **Every question needs a check** in the pillar's `verify/` script, so its
  answer proves itself. If you cannot write Python, say so in the PR — that is
  a normal thing to say, and someone will add it with you.

### 🛠 I want to work on the tooling

`tools/build_website.py` builds the site, the `verify/` scripts check the maths,
`tools/validate_verify_scripts.py` checks *those*, and `shared/preamble.tex`
holds every macro. Issues tagged
[`good first issue`](https://github.com/The-CerealDev/speed-maths/labels/good%20first%20issue)
are scoped to one file each.

[`CONTRIBUTING.md`](CONTRIBUTING.md) has the full standard, including the
reviewer checklist and the AI-disclosure policy. It is long because the bar is
"a student can trust every sheet blind" — but you do not need to read it to
report a mistake.

## Building it yourself

```bash
# Compile one sheet — run from inside the sheets/ folder, the
# \input{../../shared/preamble} path is relative to it
cd algebra/sheets && pdflatex sheet01.tex

# Check the maths
python3 algebra/verify/sheet01_verify.py

# Rebuild the website
python3 tools/build_website.py
```

`index.html` and `classic.html` are **generated** — edit `template-archive.html`
or `template.html` instead, then re-run the build. Sheet titles and topic tags
come from a `\SpeedMeta{topic}{tools}` line in each sheet's own `.tex`, so the
site can never disagree with the repo.

## Repository layout

```
speed-maths/
├── shared/preamble.tex     single source of truth for every macro and style
├── <pillar>/
│   ├── sheets/             sheet01.tex … sheet07.tex  (+ compiled .pdf)
│   ├── answers/            ans01.tex   … ans07.tex    (+ compiled .pdf)
│   └── verify/             sheetNN_verify.py — the checks
├── tools/
│   ├── build_website.py    scans the repo, writes index.html + classic.html
│   ├── compile_pdfs.sh     bulk recompile
│   └── similarity_check.py plagiarism check against a research corpus
├── template-archive.html   layout for index.html      ← edit this
├── template.html           layout for classic.html    ← or this
├── tokens.css              colours, radii, shadows — the only place hexes live
├── archive.css             layout for the current design
└── style.css               layout for the classic design
```

## Writing conventions

- **Numbering** is two-digit and zero-padded (`sheet01`), so order survives past 9.
- **Every sheet opens the same way:**
  ```latex
  \documentclass[11pt,a4paper]{article}
  \input{../../shared/preamble}
  \SpeedHeader{<Pillar>}{<N>}

  \begin{document}

  \SpeedTitleBlock{Daily <Pillar> Drill \#<N>}{<Author>}
  \SpeedMeta{<what this sheet teaches>}{<tool, tool, tool>}
  \noindent\textit{New toolkit today: ...}
  ```
- **Answer files** use `\SpeedTitleBlock{... --- Answers \& Investigations}` with
  `\ans{}` / `\method{}` / `\inv{}` per question.
- **Closing block:** end with `\SpeedClosing{<quote>}` — never hand-write it.
- **Branding** lives in `\SpeedExamLine` and `\SpeedCredit`. Change it once, there.

Starting a whole new pillar? [`PILLAR-PLAYBOOK.md`](PILLAR-PLAYBOOK.md) is the
seven-day build process, written down.

## Roadmap

- **Calculus** and **Graphs** — drafted, held back pending review.
- Questions as HTML as well as PDF, so they are searchable and linkable.
- Broader coverage of the UK admissions ecosystem (TMUA, MAT, STEP).

Note that MAT is discontinued from 2026 entry, so Oxford maths and CS applicants
now sit TMUA — the sheets are weighted accordingly.

## Licence

[MIT](LICENSE) for the code and the sheets. Questions adapted from past papers
are credited inline; the papers themselves belong to their respective boards.
