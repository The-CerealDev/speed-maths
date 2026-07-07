# Contributing to Speed Maths

New questions and new sheets are welcome. The bar is: a student aiming
for BMO1 qualification and a TMUA 9 should be able to trust every sheet
blind. These rules keep that true.

## The non-negotiables

1. **Never hand-edit the header, footer, branding, or boxes.** All of it
   lives in `shared/preamble.tex` (`\SpeedHeader`, `\SpeedTitleBlock`,
   `\ans`/`\method`/`\inv`, `\SpeedClosing`). If a sheet looks wrong,
   the fix goes in the preamble once — not in your file.

2. **No verbatim past-paper questions.** This repo is public; UKMT, TMUA
   and MAT questions are copyrighted. Adapt the *structure*, change the
   numbers and context, and credit the source in the question line:
   `\textit{\small(after SMC 2025 Q12)}`. If your question is
   indistinguishable from the original, rewrite it.

3. **Every sheet file starts the same way** (copy an existing sheet):
   `\documentclass[11pt,a4paper]{article}` →
   `\input{../../shared/preamble}` → `\SpeedHeader{<Pillar>}{<N>}`.
   Numbering is zero-padded: `sheet08.tex`, never `sheet8.tex`.

## Sheet anatomy

| Section | Role | Count / time |
|---|---|---|
| A — Rapid Recognition | recall & speed; stays EASY on every sheet | 10Q, 2:30 |
| B — Manipulation Drills | one-rule setups, direct manipulation | 10Q, 8 min |
| C — Substitution & Structure | case splits, the sheet's new tool | 8Q, 10 min |
| D — Challenge | insight over computation; the ramp | 5Q, 15 min |

- Section A never ramps — it trains recognition speed. Difficulty
  progression across a pillar lives in C and D.
- Section D carries an honest per-sheet tag: `(TMUA / SMC difficulty)`,
  `(SMC difficulty)` or `(SMC / BMO1 difficulty)`. Tag what the
  questions actually are, not what sounds impressive.
- The last D questions *should* resist a first attempt. The intended
  workflow is: try, get stuck, learn the tool, come back tomorrow.

## Answer files

Every question gets all three:
- `\ans{...}` — the answer, nothing else
- `\method{...}` — the fast route, not the textbook route
- `\inv{...}` — an extension that points somewhere real (a harder
  variant, the actual SMC/BMO1 question it came from, next sheet's tool)

## Found a mistake?

Mistake reports are among the most valuable contributions — a wrong
answer key actively damages a student mid-prep.

- **Wrong `\ans{}` values are highest priority.** Open an issue named
  by file and question (e.g. `algebra ans03, B7: answer should be −2`)
  and include your working — or just PR the fix directly with the
  working in the PR description.
- **Check the whole entry, not just the answer.** A correct `\ans{}`
  above a flawed `\method{}` still teaches the wrong thing. Same for an
  `\inv{}` that claims something false.
- **Ambiguous ≠ wrong.** If a question can be read two ways, propose a
  rewording that kills the second reading — don't silently change what
  the question means, because someone may have already done it the
  other way.
- Fix the `.tex`, recompile the PDF, commit both. Never renumber
  existing questions in a published sheet — students reference them.

## AI policy

AI assistance is allowed and actively encouraged. It is the fastest way
to find question archetypes you've never met, generate variants at a
target difficulty, and draft `\inv{}` extensions beyond your own
toolkit. This repo itself is built AI-assisted. But AI output is a
draft, never a deliverable — the standards are:

1. **Solve everything yourself before committing.** Every question you
   submit, you have personally solved start to finish, under something
   like the section's time budget. If you can't reproduce the method
   without the AI, either learn it first or drop the question.
2. **Verify every answer computationally.** Whenever mathematically
   feasible, write a short Python script to brute-force or verify your
   solution. If computational verification is strictly impossible, you must
   rigorously recompute by hand from scratch. An unverified `\ans{}` is
   the one thing that must never reach `main`.
3. **Assume AI output may plagiarise.** Models reproduce real
   competition questions from memory, sometimes verbatim. Before
   treating a generated question as original, search for it; if it
   resembles a known past-paper question, apply rule 2 of the
   non-negotiables (adapt + credit, or rewrite).
4. **Difficulty tags are a human judgement.** AI is systematically bad
   at judging how hard a question feels under exam pressure. You place
   it in A/B/C/D and you defend the section tag, based on having done
   it yourself.
5. **Say so in the PR.** A one-liner like "questions drafted with AI,
   all solved and verified by hand" tells reviewers where to focus.
   Heavy AI use with verification is welcome; undisclosed AI use that a
   reviewer catches via a wrong answer burns trust permanently.

## Before you open a PR

- [ ] Compiles with `pdflatex` **run from inside** `sheets/` or
      `answers/` (the preamble path is relative)
- [ ] Both `.tex` and the compiled `.pdf` are committed
- [ ] Adapted questions carry their `(after ...)` credit
- [ ] Answers verified computationally via script (or strictly by hand if
      programming is mathematically impossible) — a wrong `\ans{}` is worse
      than no sheet
- [ ] AI assistance disclosed if used
