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
   You must also claim authorship of the sheet in the title block:
   `\SpeedTitleBlock{Daily <Pillar> Drill \#<N>}{Your Name}`.
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

## Competition Styles & Question Design

When drafting new questions (whether by hand or with AI assistance), you must match the tone, syllabus, and specific flavor of the target competitions:

- **TMUA (Test of Mathematics for University Admission):** Focuses on AS-Level pure math and strict mathematical logic (especially for Paper 2). Questions should require systematic, multi-step reasoning rather than routine calculation. Emphasize logic, proof, and spotting errors in mathematical arguments.
- **MAT (Mathematics Admissions Test):** Tests depth over breadth. Questions should take foundational concepts (polynomials, basic calculus, sequences) and force students to apply them in unfamiliar, non-standard contexts. Design questions that lead the student through a creative logical leap.
- **SMC (Senior Mathematical Challenge):** Fast-paced, non-standard problem-solving. Use foundational topics (number theory, algebra, geometry, combinatorics) but frame them in ways that require precision of thought and arithmetic fluency rather than formula recall.
- **BMO1 (British Mathematical Olympiad Round 1):** The gold standard for Section D. Questions must require rigorous, formal written proofs and deep mathematical insight. Focus on non-linear Diophantine equations, Euclidean geometry, advanced polynomials, and combinatorics.

Always remember: **No calculators are allowed in any of these exams.** Design numbers to cancel cleanly, factor nicely, or telescope elegantly. If a computation gets bogged down in ugly arithmetic, the question is poorly designed.

### The research corpus (mandatory)

New sheets must be grounded in real past papers, not written from memory
of "what these exams are like":

1. **Fetch before you write.** A local corpus lives in `research/`
   (SMC, BMO1, TMUA, MAT papers + mark schemes, with `pdftotext`
   extracts in `research/txt/` and per-competition archetype indexes
   `research/INDEX-*.md`). If a competition or year you need is
   missing, fetch it first — official sources: `ukmt.org.uk`,
   `bmos.ukmt.org.uk`, `esat-tmua.ac.uk`, `maths.ox.ac.uk`.
2. **Ground every section.** Each sheet's question archetypes must be
   ones that actually occur in the corpus for its target competition
   (A/B ↔ TMUA/SMC-early, C ↔ SMC-mid, D ↔ SMC-late/BMO1). Close
   adaptations carry the `(after SMC 2024 Q19)` credit as usual.
3. **The corpus is local-only.** `research/` is gitignored because the
   papers are UKMT/OCR/Oxford copyright and this repo is public. Never
   commit or paste paper content into tracked files — only your own
   original/adapted questions.
4. **Run the similarity check before opening a PR.**
   `python3 tools/similarity_check.py <sheet-or-answers.tex>` compares
   every question and `\method{}` against the corpus and flags anything
   that reads too close to a source with no `(after ...)` credit — see
   the AI policy below for how to act on a flag.

## Answer files

Every question gets all three:
- `\ans{...}` — the answer, nothing else
- `\method{...}` — the fast route, not the textbook route
- `\inv{...}` — an extension that points somewhere real (a harder
  variant, the actual SMC/BMO1 question it came from, next sheet's tool)

## Verification pipeline

"Verify every answer computationally" is only real if it leaves a trace.
Ad hoc scripts you ran once and threw away are not verification anyone
else can trust or re-check — they're a claim. This repo verifies by
committed, re-runnable script, not by self-report.

**Convention:**
- One file per sheet: `<pillar>/verify/sheetNN_verify.py` (stdlib Python
  only — no dependencies to install, no friction for contributors who
  aren't primarily programmers).
- One `check_<label>()` function per question that gets a script (label
  matches the sheet, e.g. `check_A1`, `check_D5`).
- Each function must:
  1. **Independently re-derive the `\ans{}` value** — brute force, direct
     computation, or a full DP/game-tree solve. Never just re-type the
     method's arithmetic and assert it equals itself.
  2. **Assert every checkable factual or numeric claim in the `\method{}`**,
     not only the final answer. A `\method{}` can state a wrong
     intermediate fact (a modular claim, a factorisation, an identity)
     while the final `\ans{}` still happens to be right — the script must
     catch that, because a reviewer skimming prose won't reliably.
  - Claims that are pure framing or motivation ("this is startling",
    "the surest way to find a recurrence") are not checkable statements
    and are left alone — that stays a human judgement call.
- **Every script's `main()` must open with an `if not __debug__:` guard
  that refuses to run** (see `combinatorics/verify/sheet07_verify.py`).
  `python -O` or `PYTHONOPTIMIZE=1` strips every `assert` at compile
  time — since assertions are the entire verification mechanism, running
  under either would silently report every check as PASS while checking
  nothing. This has to be an `if`, never an `assert`, or the guard itself
  gets stripped too.
- Run a whole pillar's sheets with `python3 <pillar>/verify/run_all.py`.
  **A nonzero exit is a merge blocker, full stop** — this is the actual
  gate, not the honesty-system checklist item it used to be.
- Commit the verify script alongside the `.tex` and `.pdf` in the same PR.
- **If an AI agent drafted the `\method{}`, a different agent (fresh
  context, no memory of drafting it) must write the verify script for
  it — never the same agent that wrote the method.** An agent checking
  its own output shares its own blind spots: it can write an assertion
  that technically passes while quietly checking something easier than
  the actual claim, and there's no independent eye to catch it. Feed the
  second agent only the question and the `\method{}` text, not the
  drafting conversation, and have it write the checks cold.
  **This is unenforceable by inspection — a reviewer cannot tell from
  the diff whether it actually happened.** So say it explicitly in the
  PR description ("method: agent A, verify script: agent B, fresh
  context") alongside the AI-disclosure line below. Treat it as a
  disclosed claim you're trusting the contributor on, same as "I solved
  this myself" — not a gate the process itself enforces.
- **Before submitting, break your own script on purpose once and confirm
  it fails.** Change one asserted value, or the claim it's checking, and
  re-run. If it still says PASS, the check is vacuous (a stray early
  return, a tautological assertion, a variable that's shadowed and never
  actually used) — this is the one cheap step that catches a check that
  looks real but verifies nothing.
- **Every check must state its strength, not just pass/fail.** A script
  that brute-forces or DP-solves the full case (like D5's `n=2025` game
  tree) is exhaustive proof. A script that samples many random trials
  (like D2's 2000 reduction orders) is strong evidence, not proof, of a
  universally-quantified claim. Say which one it is in the function's
  docstring — reporting both as a bare "PASS" hides exactly the
  distinction a reviewer needs.

**Why this matters more once AI drafts `\method{}` text:** a method
adapted from a real past-paper solution can carry over an insight that no
longer holds once the numbers are morphed (a triangle that isn't 3-4-5
anymore, a sum that no longer telescopes) — while the final numeric
answer still happens to check out by brute force. AI-assisted `\method{}`
drafting is allowed under the AI policy below, but every checkable claim
it makes must have a corresponding assertion in the verify script before
a human review is complete. An AI-drafted method with an unverified
intermediate claim is not ready for review, regardless of how confident
the prose sounds.

See `combinatorics/verify/sheet07_verify.py` for a worked example
covering three different techniques: a brute-forced recurrence (A1), an
algebraic identity plus Monte Carlo simulation of the actual claimed
theorem (D2), and a full game-tree DP that independently re-solves the
$n=2025$ case rather than trusting the proof's induction (D5).

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
toolkit. This repo itself is built AI-assisted. **(For a quick start, check out the [AI Workflow & Prompts Guide](prompts/AI_PROMPTS.md) we've created for new contributors!)** But AI output is a
draft, never a deliverable — the standards are:

1. **Solve everything yourself before committing.** Every question you
   submit, you have personally solved start to finish, under something
   like the section's time budget. If you can't reproduce the method
   without the AI, either learn it first or drop the question.
2. **Verify every answer — and every checkable claim in the method —
   computationally.** Whenever mathematically feasible, write a
   `<pillar>/verify/sheetNN_verify.py` check (see "Verification
   pipeline" above) that independently re-derives the `\ans{}` and
   asserts each factual claim the `\method{}` makes. If computational
   verification is strictly impossible, you must rigorously recompute by
   hand from scratch and say so in the script's docstring. An unverified
   `\ans{}`, or a `\method{}` with an un-asserted checkable claim, is the
   one thing that must never reach `main`. **If AI wrote the `\method{}`,
   AI may also write the verify script — but it must be a different
   agent instance, given only the question and the method text, not the
   conversation that drafted it.** The same agent grading its own
   homework is not verification.
3. **Assume AI output may plagiarise — check it with `tools/similarity_check.py`,
   not just a memory-search.** Models reproduce real competition
   questions from memory, sometimes verbatim, and a human skimming for
   "does this ring a bell" misses close-but-not-identical reproductions.
   Run `python3 tools/similarity_check.py <your-file.tex>` before
   opening a PR — it word-shingle-compares every question (and every
   `\method{}`) against the full local corpus and flags anything with
   high overlap and no `(after ...)` credit tag. A high-overlap result
   *with* a credit tag is expected and fine (that's what a credited
   adaptation looks like); a high-overlap result with no credit tag
   means compare it to the source by hand and either credit it or
   rewrite it per rule 2 of the non-negotiables. This tool only works
   locally — it reads the gitignored `research/txt/` corpus and cannot
   run in any public CI for the same copyright reason the corpus itself
   isn't committed.
4. **Difficulty tags are a human judgement.** AI is systematically bad
   at judging how hard a question feels under exam pressure. You place
   it in A/B/C/D and you defend the section tag, based on having done
   it yourself.
5. **Say so in the PR.** A one-liner like "questions drafted with AI,
   all solved and verified by hand" tells reviewers where to focus.
   Heavy AI use with verification is welcome; undisclosed AI use that a
   reviewer catches via a wrong answer burns trust permanently.

## Reviewer checklist

Reviewing means re-deriving, not skimming. A review that only confirms
"a script exists and passes" is checking paperwork, not mathematics —
the script's coverage is exactly what's in question.

- [ ] Run `python3 <pillar>/verify/run_all.py` yourself. A pass is the
      floor, not the approval.
- [ ] Open the verify script and check its coverage against the
      `\method{}` prose: does every checkable claim (a factorisation, a
      modular fact, an identity, a stated intermediate value) actually
      have an assertion? A script that only checks the final `\ans{}`
      is incomplete, even if it's green.
- [ ] **Pick one assertion yourself and mutate it — change the expected
      value or comment it out — then re-run and confirm it fails.** This
      is the real safety net, not the "different agent wrote it" claim
      above: you can't verify from a diff whether two agents were
      actually used, but you can always verify, yourself, in under a
      minute, whether the check in front of you is real or vacuous. Do
      this regardless of who or what wrote the script.
- [ ] Independently re-derive at least the D-section questions yourself
      before approving — for A/B/C you may spot-check, but D is where a
      confidently-wrong `\method{}` does the most damage.
- [ ] If the question is an adaptation, confirm the `(after ...)` credit
      is present and that the morph didn't quietly break an intermediate
      claim borrowed from the original (see "Verification pipeline").
- [ ] Would you defend the D-tag yourself if a student pushed back on it?
      If not, it's not ready to merge.

## Before you open a PR

- [ ] Compiles with `pdflatex` **run from inside** `sheets/` or
      `answers/` (the preamble path is relative)
- [ ] Both `.tex` and the compiled `.pdf` are committed
- [ ] Adapted questions carry their `(after ...)` credit
- [ ] `python3 tools/similarity_check.py <file>` run, and every flagged
      block is either credited or rewritten
- [ ] `<pillar>/verify/sheetNN_verify.py` committed, and
      `python3 <pillar>/verify/run_all.py` exits 0 — a wrong `\ans{}` or
      an unverified `\method{}` claim is worse than no sheet
- [ ] AI assistance disclosed if used
