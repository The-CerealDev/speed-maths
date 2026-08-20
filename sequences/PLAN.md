# Sequences Pillar — Build Plan

Status as of 2026-08-12: branch `pillar/sequences` created off `main`. Corpus research
done and corrected. **Blocked on one open confirmation before Day 1 drafting starts**
(see "Open question" below). Everything else here is settled and actionable.

The general conventions referenced below (MCQ split, cross-referencing, territory map,
mistake-linking, build process, ship checklist) now live in
[`PILLAR-PLAYBOOK.md`](../PILLAR-PLAYBOOK.md) at the repo root — they apply to every
pillar, not just this one. This file restates the parts relevant to Sequences so it stays
readable standalone, but the playbook is the source of truth if the two ever disagree.

If you are a fresh agent picking this up with no conversation context: read this whole
file before touching any `.tex` file. It is the distilled output of a full corpus-frequency
research pass plus a cross-pillar duplication sweep — skipping it risks repeating exactly
the mistakes that got the original Logic pillar rejected (fabricated citations,
cross-pillar duplication, internal duplication).

## Audience

Students aiming for a top TMUA score (~9.0 on TMUA's 1.0–9.0 scale), with BMO1
aspirations and potentially further (STEP etc.). Calibrate difficulty at genuine
TMUA/BMO1/SMC level throughout — this is not remedial content.

## Repo conventions (unchanged from other pillars)

- `sequences/sheets/sheet0N.tex` (33 Q: A10/B10/C8/D5) + `sequences/answers/ans0N.tex`
  (`\ans{}`/`\method{}`/`\inv{}` per question). See `CONTRIBUTING.md`.
- Exactly 33 `check_` functions per `sequences/verify/sheet0N_verify.py`, run via
  `verify/run_all.py`. `if not __debug__:` as the literal first line of `main()`.
- `(after <Competition> <Year> [Paper N] Q<N>)` citation format — only for genuine,
  hand-verified adaptations. **Every citation must be independently checked against the
  actual source PDF before use — never trust `research/INDEX-*.md` alone.** The logic
  pillar shipped with fabricated citations once already from trusting an index/agent
  claim without checking the PDF directly.
- `tools/similarity_check.py` before shipping each sheet.
- Anything scrapped goes to `sequences/vault/`, never deleted.

## New conventions for this pillar (and going forward — see memory files)

1. **`\seealso{}` mistake-linking** (see `feedback_mcq_proof_split` sibling ask from the
   user about linking Top-5-mistakes sections to question locations — not yet built as a
   macro; if starting fresh, check whether `shared/preamble.tex` has gained a `\seealso{}`
   macro since this was written, and add one if not). Every `Top 5 Patterns`/`Common Traps`
   bullet at the end of `ans0N.tex` must reference the question label(s) where that
   pattern/trap actually shows up in that sheet.
2. **Sheets build on each other.** Section A/B of Day N>1 should fold in 1-2 genuine
   recognition-level questions that reuse a technique from an *earlier* day in this same
   pillar, for speed/interleaving — not just `\inv{}` extension pointers, actual graded
   questions. Don't let a day's toolkit disappear once its "new toolkit" day is over.
3. **MCQ/proof split — ~2/3 MCQ overall, but Section A is never MCQ.** Rationale from the
   user: easy MCQs create false confidence; TMUA and SMC are MCQ exams so the pillar
   should lean MCQ, but BMO1-flavored proof content (mainly Days 6-7) should stay written
   proofs. Proposed section-by-section shape (see "Open question" — not yet confirmed):
   - A (10): always non-MCQ, short-answer/fill-in.
   - B (10): majority MCQ (~7/10), rest free-response where the technique must be written out.
   - C (8): fully MCQ, TMUA/SMC-hard (existing pillar-wide convention already).
   - D (5): MCQ-leaning on Days 1-5, proof-heavy on Days 6-7 (BMO1 capstone).
   - Any MCQ, anywhere, must be genuinely hard (TMUA/SMC difficulty or harder) — never a
     softball recognition MCQ, and must stay on-spec.

## MCQ/proof split — locked in

The user stepped away before explicitly confirming the section-by-section breakdown in
point 3, and asked to proceed autonomously ("lets go on with it"). Per this file's own
contingency instruction, the breakdown above is now the operating default: A never MCQ,
B ~7/10 MCQ, C fully MCQ, D MCQ-leaning Days 1-5 / proof-heavy Days 6-7. Treat it as
confirmed-by-default, not a guess to keep re-litigating — but if the user pushes back on
it later, that's a real correction, not a misunderstanding to defend.

## Cross-pillar collision map — confirmed by direct inspection, not assumed

Do not re-derive this from scratch — it was built by actually reading the other pillars'
`.tex` files, not guessed from topic names.

| Territory | Owned by | Evidence |
|---|---|---|
| Telescoping (sums and products) | Algebra | 5 of 7 answer files (`ans01,02,03,04,05,07`), including sum-of-squares via telescoping |
| Binomial theorem (coefficient extraction, Pascal's rule, substitution) | Combinatorics Day 4 | Full day, titled exactly this |
| Recurrence-as-counting-tool (tiling, binary strings, Fibonacci counting, Catalan numbers, derangements) | Combinatorics Day 7 | Full day, titled "Recurrences & Fibonacci Counting" |
| Fibonacci-mod-m periodicity (Pisano period via Pigeonhole) | Number Theory `ans04` | Direct worked example, F(2026) mod 3 |
| Fibonacci as an induction-proof vehicle | Logic Days 5-6 | F6=8 counterexample, alternating-sum identity proof |
| Induction-proving of *given* sum formulas (Σi, Σ(2i-1), Σ1/(i(i+1))) | Logic Day 6 | Direct questions in `sheet06.tex` |

**If a draft day starts drifting into any of the above, that's a signal it's duplicating
another pillar — pull back toward the series/algebraic-behavior framing below.**

## The 7-day arc

Grounded in `research/INDEX-tmua-sequences.md` (dedicated corpus pass, corrected —
see note on TMUA "2016" below) plus frequency counts over the 1305-question community
corpus (`variant_retriever/open_coded2.json`).

**Citation correction to carry forward:** `tmua_2016_1.txt`/`tmua_2016_2.txt` are
byte-identical to the TMUA Practice Paper (same paper code D513/11) — there is no real
2016 TMUA sitting. Any content sourced from those rows must be credited as **"TMUA
Practice Paper 1/2"**, never "TMUA 2016."

1. **Arithmetic sequences & series** — nth term, sum formula, integer/Diophantine
   constraints on an AP. Anchor: TMUA 2019 P2 Q11. Corpus notes: the
   "AP-and-GP-share-a-first-term combined sequence" archetype (specimen_1 Q19, Practice
   Paper 1 Q14, 2017_1 Q7, 2020_1 Q4, 2021_1 Q3) is the single most repeated TMUA
   sequences archetype — worth anchoring here and/or Day 3.

2. **Binomial & trinomial expansion, series framing only** — Pascal's triangle as a
   sequence array, row-sum/alternating-sum identities (TMUA 2019 P1 Q3, "sum of binomial
   coefficients" filed under arithmetic series), generalized binomial series → bridges
   into Day 3's geometric series via `(1-x)^{-1} = Σxᵏ`, trinomial/multinomial
   coefficients (TMUA 2020 P1 Q13, Practice Paper 1 Q19's trinomial-bracket variant).
   **Must not re-teach plain coefficient extraction** — that's Combinatorics Day 4's job;
   the differentiator is "binomial coefficients as a sequence/series object," not "pick
   the coefficient by counting."

3. **Geometric series & convergence** — ratio recognition, sum-to-infinity, the `|r|<1`
   condition as the actual object of study (not just a formula to apply), explicitly
   closing the loop from Day 2's `(1-x)^{-1}`. Anchors: TMUA 2022 P1 Q8, 2023 P1 Q18,
   2023 P2 Q15 (base-2 recurring decimal). Corpus note: convergence is usually wrapped in
   a "for which parameter values is S finite" framing, not asked directly.

4. **Recurrence relations via characteristic equation** — forming a recurrence, solving
   linear recurrences algebraically (e.g. `aₙ = aₙ₋₁ + c·aₙ₋₂`-type via the characteristic
   polynomial), closed-form derivation. This is the one technique none of the other four
   pillars touch — confirmed by the collision map above, and also confirmed absent from
   real TMUA (which tests periodicity/cycle-detection, not closed-form solving — see
   corpus note below). Treat this day as building a skill TMUA doesn't directly test but
   BMO1/MAT do (MAT is the strongest real-paper source for "derive the recurrence
   yourself," e.g. MAT 2014 Q5, MAT 2023 Q5's Fibonacci fast-doubling identities).

5. **Behaviour of sequences** — monotonicity, boundedness, fixed points, non-modular
   periodicity (rational/Möbius-map cycles — deliberately NOT mod-m, since Number Theory
   already owns Pisano-period pigeonhole), pathological floor/ceiling/digit-defined
   sequences, spot-the-flaw. Anchor: TMUA 2021 P2 Q10 (integer-sequence counterexample).
   Corpus note: MAT owns pathological floor/ceiling sequences almost outright (MAT 2013
   Q1J, MAT 2023 Q1J) — TMUA's own analogues are thin, lean on MAT here.

6. **BMO1 capstone I — constrained sequence construction** — integer-mean sequence
   construction (BMO1 2018 Q6), alternating recurrence behaviour (BMO1 2021 Q1).
   Deliberately non-counting-flavored to stay clear of Combinatorics Day 7. Proof-heavy
   per the MCQ/proof split. Corpus note: BMO1 recurrences are *always* a proof/construction
   tool (integrality, boundedness, invariants) — never "compute term N."

7. **Mixed synthesis capstone** — circular/periodic product-constraint sequences (BMO1
   2019 Q2), full week combined at BMO1/SMC pressure. Proof-heavy.

## Process to follow (reused from the Logic pillar rebuild — it worked)

1. Draft a day's `sheet0N.tex` + `ans0N.tex`.
2. Compile both to PDF, fix LaTeX errors.
3. Run `tools/similarity_check.py` against the day's content.
4. Dispatch a subagent (the user has previously asked for the external `agy` CLI —
   `agy -p "<prompt>"` — to be used specifically for writing verify scripts and
   calibration/review reports, if available) to write `verify/sheet0N_verify.py`
   (exactly 33 `check_` functions) and to produce a calibration report checking for
   internal duplication, cross-pillar duplication, and citation accuracy.
5. **Independently re-verify every claim the subagent/report makes** — check citations
   against the actual source PDF yourself, don't trust the index or the agent's word.
   Past sessions caught real errors this way (a wrong "revert to X" suggestion, a false
   duplication-positive, factual errors in `research/INDEX-*.md` itself).
6. Apply fixes, recompile, re-verify.
7. Proactively grep other pillars for overlap **before** finalizing a day's content, not
   after a full draft — Day 7 of Logic lost significant time discovering 9/33 duplicate
   questions only after drafting was "done."

## Ship checklist (do all of this before considering the pillar done)

- `python3 verify/run_all.py` — all 231 checks (33 × 7) pass.
- `tools/similarity_check.py` across all 14 files — investigate every flag, don't just
  suppress them.
- Clean stray LaTeX build artifacts (`.aux`, `.log`, `.out`, etc.) from `sheets/` and
  `answers/`.
- Anything scrapped during calibration goes to `sequences/vault/`, never deleted.
- Commit and push `pillar/sequences`. Do not merge to `main` without the user's explicit
  go-ahead (same pattern as Logic — merge was a separate, explicitly-requested step).

## Explicitly out of scope for this branch

The user has flagged that Algebra, Combinatorics, and Number Theory likely need the same
audit that caught Logic's fabricated citations (they were built off a one-time generic
`research/INDEX-*.md` batch from 2026-07-08, never a dedicated per-pillar research pass —
Algebra has zero traceable citations at all). That audit is a separate future undertaking
("the great refurbish") and is **not** part of this branch's work. Don't scope-creep into
touching those pillars from here.
