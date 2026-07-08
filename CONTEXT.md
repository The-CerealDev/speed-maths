# Speed Maths — Daily Drill Series

TMUA & SMC exam prep. Four pillars: Algebra (done), Combinatorics (in progress),
Number Theory, Geometry (both empty, not started).

## Structure
Speed-Maths/
├── shared/preamble.tex   ← single source of truth: header/footer, colours,
│                            answer/investigate boxes, title-table macro
├── algebra/sheets/        sheet01.tex … sheet07.tex (+ compiled pdf)
├── algebra/answers/       ans01.tex  … ans07.tex   (+ compiled pdf)
├── combinatorics/{sheets,answers}/   ← sheet01 / ans01 done
├── number-theory/{sheets,answers}/   ← empty, README placeholder only
└── geometry/{sheets,answers}/        ← empty, README placeholder only

## Hard rules
- Every file starts: `\documentclass[11pt,a4paper]{article}` →
  `\input{../../shared/preamble}` → `\SpeedHeader{<Pillar>}{<N>}` → `\begin{document}`
- Never hand-edit header/footer/colours per-file — edit `shared/preamble.tex` once.
- Branding is locked: **"Exam and Competition Prep"**, credit links
  `linkedin.com/in/cerealdev/`, author "David Akinyele-Aje". Don't drift this again
  (it drifted badly before a full audit fixed it — see README changelog).
- Numbering: zero-padded (`sheet01`, not `sheet1`).
- Sheet skeleton: Section A Rapid Recognition (10Q, 2:30) → B Manipulation Drills
  (10Q, 8min) → C Substitution & Structure (8Q, 10min) → D Challenge (5Q, 15min,
  "insight over computation"). Use `\SpeedTitleBlock{...}` to generate this table.
- Answers use `\ans{}` `\method{}` `\inv{}` (investigate-further extension) per question.
- Every sheet/answer ends with `\SpeedClosing{<quote>}` (rule + quote + cross-promo).
- Compile from inside `sheets/` or `answers/` (relative `\input` path depends on it).
- **Strict Verification:** All generated answers must be verified computationally via a short script, and questions must strictly adhere to TMUA/MAT/SMC/BMO1 styles (see `CONTRIBUTING.md`).
- **Mandatory research corpus:** new sheets are grounded in the fetched past-paper
  corpus in `research/` (SMC/BMO1/TMUA/MAT papers + txt extracts + INDEX-*.md
  archetype catalogues). It is gitignored — copyrighted papers must never reach the
  public repo. Fetch missing papers before writing (CONTRIBUTING.md → "The research
  corpus" lists the official sources).

## Difficulty design (agreed 2026-07-07)
- Training goal: SMC → BMO1 qualification + TMUA 9. "Mathematical excellence training."
- Section A stays FLAT across all sheets of a pillar — it trains recall/recognition/speed,
  never ramps. The ramp lives in C and especially D.
- Section D ramps per pillar: early sheets = SMC mid/late paper; mid sheets add
  "show that / prove" phrasing; final 2 sheets = BMO1 Q1-level "determine, with proof",
  answers modelling a full written argument. Philosophy: student tries the sheet; if the
  last D questions resist, they sit with them a day, learn the tool, then return.
- D difficulty tags are per-sheet HONEST labels, standard form
  `\hfill{\normalfont\small(<tag> difficulty)}`. Algebra 1–4 = "TMUA / SMC",
  algebra 5–7 = "SMC / BMO1", combinatorics 1 = "SMC" (escalates later sheets).
- Questions adapted from real papers get an italic small credit, e.g. "(after SMC 2025 Q12)".
  Never copy verbatim — the repo is open source; adapt structure, change numbers.

## Current state
Algebra = 7 complete sheets, toolkit progression already runs: sum/diff of squares →
Vieta's/nested surds → Remainder-Factor thm/AM-GM → geometric series/parity →
partial fractions/Cauchy-Schwarz → Schur's/integer polys → weighted AM-GM/Vieta jumping.

Combinatorics = sheet01 + ans01 done (multiplication principle / factorials /
permutations / cases). Planned progression for 02–07: combinations & complementary
counting → restricted/circular arrangements → binomial theorem & Pascal → stars-and-bars
& inclusion-exclusion → pigeonhole & double counting → recurrences, bijections, invariants.

**Do not generate new pillar content unprompted** — wait for explicit direction on
which pillar + how many sheets before writing questions.
