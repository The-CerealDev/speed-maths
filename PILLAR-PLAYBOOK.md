# Pillar Playbook

Read this before drafting a new pillar or refurbishing an existing one. `CONTRIBUTING.md`
covers file structure, citation format, and the verification pipeline — this file covers
the process and pedagogical conventions that sit above that: how deep the research has to
go, how pillars avoid stepping on each other, how MCQ and proof format get balanced, and
the standing plan for auditing the pillars that predate this playbook.

If you're an agent about to write or revise sheets in any pillar, read the relevant
sections below first. If you're refurbishing an existing pillar, read all of it, plus
`sequences/PLAN.md` as a worked example of what a properly-scoped pillar plan looks like.

## 1. Research depth requirement

`research/INDEX-tmua.md`, `INDEX-bmo1.md`, `INDEX-mat.md`, `INDEX-smc.md` are a **generic,
one-time batch** (all four created within two minutes of each other, 2026-07-08) — they
were never built as a dedicated pass for any specific pillar's topics, and `INDEX-tmua.md`
in particular is explicitly scoped to "counting, combinatorics, discrete logic, probability,
pigeonhole." Do not treat them as sufficient grounding for a pillar outside that scope.

- **Every pillar needs its own dedicated index** — `research/INDEX-tmua-<pillar>.md` — built
  by actually reading the raw corpus (`research/txt/*.txt`) for that pillar's specific
  themes, not inferred from filenames or the generic indexes. `INDEX-tmua-logic.md` and
  `INDEX-tmua-sequences.md` are the two that exist so far; both were built this way.
- Where feasible, back it with **frequency counts** (which archetypes actually recur, how
  often) rather than a flat list — this is what lets you weight a 7-day arc by what the
  exam actually tests, instead of a generic topic-by-topic template.
- **Every citation must be independently verified against the actual source PDF before
  it's used** — never trust an index row, and never trust another agent's claim that a
  citation checks out. The generic indexes have had real factual errors (e.g. BMO1 2019
  Q1 and BMO1 2022 Q6 rows that didn't match the actual PDF content when checked directly).
  The original Logic pillar shipped with fabricated `(after ...)` citations once already
  from skipping this step.
- **Watch for `tmua_2016_1`/`tmua_2016_2`** specifically — they are byte-identical to the
  TMUA Practice Paper (same paper code, D513/11). There is no real TMUA 2016 sitting.
  Anything sourced from those files must be credited as "TMUA Practice Paper 1/2," never
  "TMUA 2016."

## 2. Cross-pillar territory map

Before finalizing a day's content, grep every *other* pillar for the technique you're
about to teach. A topic name overlapping is not disqualifying by itself — what matters is
whether the *specific technique and framing* is already someone else's signature move.
Confirmed by direct inspection (not assumed) as of the Sequences pillar build:

| Territory | Owned by | Evidence |
|---|---|---|
| Telescoping (sums and products), partial fractions | Algebra | 5 of 7 answer files (`ans01,02,03,04,05,07`) |
| Binomial theorem — coefficient extraction, Pascal's rule, substitution (the *counting* framing) | Combinatorics Day 4 | Full day, titled exactly this |
| Recurrence-as-counting-tool — tiling, binary strings, Fibonacci counting, Catalan numbers, derangements | Combinatorics Day 7 | Full day, "Recurrences & Fibonacci Counting" |
| Fibonacci-mod-m periodicity (Pisano period via Pigeonhole) | Number Theory | `ans04`, direct worked example |
| Fibonacci as an induction-proof vehicle | Logic Days 5-6 | F6=8 counterexample, alternating-sum identity proof |
| Induction-proving of *given* sum formulas (Σi, Σ(2i-1), Σ1/(i(i+1))) | Logic Day 6 | Direct questions in `sheet06.tex` |
| AP/GP series, binomial series (the *sequence/series-object* framing), recurrence relations via characteristic equation, non-modular periodicity | Sequences | in progress — see `sequences/PLAN.md` |

**Update this table whenever a pillar claims new territory.** A future Geometry, Calculus,
or Graphs pillar should add rows here before drafting, and check existing rows first.

## 3. MCQ / proof-format policy (all pillars, not just one)

Roughly a **2/3 MCQ to 1/3 proof/written-answer** split overall, reflecting that TMUA and
SMC are both MCQ exams while BMO1 is proof-based:

- **Section A is never MCQ**, regardless of the rest of the split. Easy multiple-choice
  questions let a student pattern-match or guess without real understanding — worse than
  no question at all at the point where fluency is being built. A stays short-answer/fill-in.
- **Section C stays fully MCQ** (existing convention, unchanged).
- **Section B should lean majority MCQ** (~7 of 10), keeping the rest free-response where
  the technique itself has to be written out (e.g. "derive the closed form").
- **Section D**: MCQ-leaning on early/TMUA-flavored days, but proof-heavy on BMO1-flavored
  capstone days (typically the last 1-2 days of a pillar's arc) — don't force a BMO1-style
  problem into MCQ format just to hit a quota; the proof-writing is the point there.
- **Any MCQ, anywhere, must be genuinely hard** — TMUA/SMC difficulty or harder, never a
  softball recognition MCQ — while staying on-spec for the syllabus.

## 4. Sheets build on each other

A pillar's 7 sheets are not independent worksheets. Day N>1's Section A/B should fold in
1-2 genuine, graded recognition-level questions that reuse a technique from an *earlier*
day in the same pillar, for interleaved retention — not a token callback, an actual
question testing the earlier skill at speed. This is distinct from the existing `\inv{}`
extension pointers (optional, investigate-further); this convention is graded, in-sheet
content that keeps an earlier day's toolkit alive instead of dropping it once that day's
"new toolkit" framing is over.

## 5. Mistake-linking (`\seealso{}`)

Every pillar's `ans0N.tex` ends with `Top 5 Patterns` and `Common Traps` sections (5 items
each). These must reference the question label(s) in that same sheet where the
pattern/trap actually shows up, so a reviewer can jump straight from the summary to the
worked example.

- **Not yet implemented as a macro.** Action item: add `\seealso{}` to `shared/preamble.tex`
  (e.g. rendering as `\hfill\textit{\footnotesize(see B6, D2)}`), then retrofit every
  existing `Top 5 Patterns`/`Common Traps` bullet across every pillar with the correct
  reference — this requires reading the actual question, not guessing the mapping.
- **Also not yet implemented:** `tools/check_error_links.py` — a structural guardrail that
  parses every `\seealso{}` reference and confirms the referenced question label actually
  exists in that sheet, run the same way `run_all.py` gates the verify scripts.
- **Current coverage gap** (as of the Sequences pillar build): Algebra has the section in
  7/7 sheets (but no links yet), Combinatorics 6/7 (missing sheet01), Number Theory 1/7
  (only sheet07), Logic 0/7. Every new pillar should ship with linked Top 5/Traps from
  day one rather than needing this backfilled later.

## 6. Build process (per day, any pillar)

1. Draft `sheet0N.tex` + `ans0N.tex`.
2. Compile both to PDF, fix LaTeX errors.
3. Run `tools/similarity_check.py` against the day's content.
4. Dispatch a **fresh-context subagent** to write `verify/sheet0N_verify.py` (exactly 33
   `check_` functions, per `CONTRIBUTING.md`) and a calibration report checking internal
   duplication, cross-pillar duplication (against the territory map above), and citation
   accuracy. Never the same agent/context that drafted the content — see `CONTRIBUTING.md`'s
   verification pipeline for why.
5. **Independently re-verify every claim the subagent/report makes** — check citations
   against the actual source PDF yourself, don't trust the report's word. This has caught
   real errors before: a wrong "revert to X" suggestion, a false duplication-positive, and
   factual errors in the research indexes themselves.
6. Apply fixes, recompile, re-verify.
7. **Grep other pillars for overlap before finalizing a day's content, not after a full
   draft.** Drafting a full day and only then discovering 9/33 questions duplicate earlier
   material (as happened once) wastes far more time than a five-minute grep sweep up front.

## 7. Ship checklist (any pillar, new or refurbished)

- `python3 <pillar>/verify/run_all.py` — every check passes, nonzero exit is a blocker.
- `tools/similarity_check.py` across every file in the pillar — investigate every flag,
  don't just suppress or ignore it.
- Clean stray LaTeX build artifacts (`.aux`, `.log`, `.out`, etc.) from `sheets/` and
  `answers/` before committing.
- Anything scrapped during drafting or calibration goes to `<pillar>/vault/` — **never
  delete it.**
- Commit and push the pillar's branch. Merging to `main` is a separate, explicit step —
  don't do it without the user asking for it directly.

## 8. Target audience (every pillar)

Students aiming for a top TMUA score (around 9.0 on TMUA's 1.0–9.0 scale), with BMO1
aspirations and potentially further (STEP etc.). Calibrate difficulty at genuine
TMUA/BMO1/SMC level throughout, every pillar — this is not remedial content, and easy
content (per the MCQ policy above) is actively counterproductive for this audience.

---

## The Refurbish — standing plan for the pre-playbook pillars

Algebra, Combinatorics, and Number Theory were all built before any of the conventions
above existed, off the one-time generic corpus batch described in §1. None of them have
had a dedicated research pass, a cross-pillar collision check, or a citation audit. Logic
originally shipped with fabricated citations and heavy duplication before a full rebuild
caught it — these three pillars have never been checked to that standard, and there's no
reason to assume they don't have the same class of problem.

**Evidence this hasn't happened yet** — traceable `(after ...)` citations per pillar:

| Pillar | Citation tags | Notes |
|---|---|---|
| Algebra | 0 | Zero traceable grounding to any real paper |
| Combinatorics | 5 | Thin, off the generic index |
| Number Theory | 26 | Strongest of the three, still off the generic index |
| Logic (post-rebuild) | 17 | The only pillar audited to the current standard |

**Audit process per pillar** (mirrors the Logic rebuild):

1. Build a dedicated `research/INDEX-tmua-<pillar>.md` if one doesn't already exist.
2. For every existing `(after ...)` citation, verify it against the actual source PDF
   directly — fix or strip anything that doesn't check out.
3. Run `tools/similarity_check.py` fresh across every file in the pillar, investigate
   every flag.
4. Grep every *other* pillar for topic overlap against the territory map in §2 — fix any
   duplication found, and add the pillar's own confirmed territory to that table.
5. Check for *internal* duplication — the same technique reused across multiple days in
   the same pillar without acknowledgment.
6. Retrofit missing `Top 5 Patterns`/`Common Traps` sections and `\seealso{}` links (see
   §5's coverage gap table) — this needs the `\seealso{}` macro and the coverage gaps
   fixed regardless of whether a full content audit happens at the same time.
7. Vault anything scrapped — never delete.
8. Run the full ship checklist (§7) before considering the pillar "refurbished."

**Suggested order:** Number Theory first (richest existing citation base, likely the
fastest, lowest-risk audit), then Combinatorics, then Algebra last (zero citations, the
largest unknown, likely the biggest job).

**Status: not yet started.** Not in scope for the `pillar/sequences` branch — see that
branch's `sequences/PLAN.md` for an explicit note not to scope-creep into this from there.
