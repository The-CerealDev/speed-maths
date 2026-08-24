# Speed Maths

Computationally verified corpus for TMUA and competition (SMC, BMO1) preparation.

## For Students (TMUA & Competition Prep)

If you are revising for university admissions tests, you know the two biggest problems: past papers run out fast, and textbook answer keys are constantly wrong.

This repository contains 1,155 original questions across 5 pillars — Algebra, Combinatorics, Logic, Number Theory and Sequences — at 33 questions on each of 7 daily sheets per pillar. Every answer has a committed, re-runnable Python script behind it, and a machine gate checks that the script actually compares its own result against the answer printed in the PDF.

**How to use this:**
1. Navigate to the `sheets/` directory of any pillar.
2. Do one daily drill.
3. Check your work against the `answers/` directory. If you disagree with the answer key, check the pillar's `verify/sheetNN_verify.py` for that question — it shows exactly what was computed and how. If it turns out to be wrong, that is a bug worth reporting; see the Bounty below.

### How much is verified, exactly

Every claim below is produced by `python3 tools/check_binding.py`, not asserted by hand.

| | questions | |
|---|---|---|
| answer compared against the printed `\ans{}` | **1,077** | 93.2% |
| answer is "Proof: see method" — a pointer, not a value | 78 | 6.8% |
| independently computed, but not yet compared to the PDF | **0** | 0.0% |
| **total** | **1,155** | **100%** |

Of the 1,077 that are compared, 1,007 are exact mathematical equality (`EXACT`) and 70 can detect the answer key being edited (`DRIFT_ONLY`), where the printed answer is descriptive text.

The third row is now at **zero** — every published question in the corpus is mathematically verified and bound against its published answer key. [`verify/BINDING_BASELINE.json`](verify/BINDING_BASELINE.json) is empty and enforced at 0 by `python3 tools/check_binding.py` in CI.

What is true everywhere: no published question has a check that verifies nothing. That count was 33 — 13 empty bodies, 3 `assert True`, 17 whose only assertions compared literals — and it is 0 now, enforced by `tools/analyze_facades.py --strict` in CI.

---

## Architecture (For Engineers & Contributors)

Two halves, because they catch different things.

**Runtime**, in `tests/`: one parametrised test over all 1,155 questions. It imports each pillar's verify script, runs the check for a question, and compares the value it returns against the `\ans{}` in the `.tex`.

1. **AST parsing** (`tools/latex_bridge.py`): strips `.tex` formatting, handles juxtaposition edge cases, and compiles expressions like `\ans{\frac{x(x+1)}{2}}` into SymPy nodes.
2. **Comparison** (`tools/answer_binding.py`): one reviewed comparison for the whole corpus rather than 1,155 authors each improvising one. Handles expressions, value lists, booleans and multiple-choice letters, and reports honestly which of those it managed — `EXACT`, `DRIFT_ONLY` or `EXEMPT`.
3. **Property-based testing** (`hypothesis`): fuzz-tests combinatorial recurrences and algebraic identities across randomised integer boundaries.
4. **Negative controls** (`tests/test_binding_rejects_wrong_answers.py`): every answer is perturbed and the comparison required to reject it. Without this, a comparison that returned `True` unconditionally would pass all 1,155 cases and the whole gate would be decorative.

**Static**, in `tools/check_binding.py`: a passing suite cannot detect a check that passes while verifying nothing, because the check passes. So that is checked in the source instead — every published question must have a non-empty body, at least one assertion that depends on a value it computed, and a link to its answer key.

**Mutation testing** (`mutmut`) targets `tools/`, where the library code lives and `tests/` is its consumer. It is a manual and nightly job, not a CI gate — a full run is far slower than a pull request should wait for. It is *not* pointed at the check scripts: a check function cannot be both the mutant and its own test, and when it was configured that way every one of 9,016 generated mutants came back "no tests" and nothing was ever killed.

## Layout

```text
Speed-Maths/
├── shared/
│   └── preamble.tex           (LaTeX styles and macros)
├── algebra/                   (live: 7 sheets, 231 questions)
│   ├── sheets/ & answers/
│   └── verify/                (one script per sheet, 33 checks each)
├── combinatorics/             (live)
├── logic/                     (live)
├── number-theory/             (live)
├── sequences/                 (live)
├── tests/
│   ├── test_answer_binding.py             (all 1,155 answers vs their checks)
│   └── test_binding_rejects_wrong_answers.py   (negative controls)
├── tools/
│   ├── latex_bridge.py        (LaTeX -> SymPy)
│   ├── answer_binding.py      (the comparison, and its honest strength)
│   ├── check_binding.py       (static gate + ratchet)
│   ├── analyze_facades.py     (checks that verify nothing)
│   ├── validate_verify_scripts.py
│   └── build_website.py
├── verify/
│   ├── BINDING_BASELINE.json  (the 530 not yet compared; may only shrink)
│   └── BINDING_EXEMPTIONS.md  (the 77 "Proof: see method" answers)
├── template.html
└── index.html                 (auto-generated artifact)
```

Calculus and Graphs are drafted and held back for review; `sheets.json` is the source of truth for which pillars are live.

## Conventions

A new sheet cannot be merged without a verify script that passes and binds. See `CONTRIBUTING.md` for the pipeline.

- **Numbering:** two-digit, zero-padded (`sheet01`).
- **LaTeX:** include `\input{../../shared/preamble}`.
- **Answers:** wrap in `\ans{...}` for `latex_bridge` parsing.
- **Checks:** `return` the value you verified, so the harness compares it to the `.tex`.
- **Compilation:** run `pdflatex` from within `sheets/` or `answers/`.

## The Bounty (Hall of Fame)

If you find a mathematical error in a compiled answer key, open a GitHub Issue — that is the most valuable contribution to this repo, and it is worth being precise about what the bounty covers.

**A wrong answer is claimable.** Any question, including the 530 not yet compared against their PDFs. Those are exactly where a wrong answer is most likely to have survived, so they are fair game and interesting.

**Beating the pipeline is the harder claim.** If you can show a mathematically incorrect answer surviving a check that the gate reports as *bound* — one where the script does compare its result against the printed answer — that is a defect in the verification itself, not just in one sheet. Your name goes in the Hall of Fame below either way; say which kind you think you have.

*No bounties claimed yet.* One cosmetic issue has been reported and is open.

## Roadmap

The static PDF corpus is open source, and it is the whole of what this repo publishes.

Next, in order: clear `verify/BINDING_BASELINE.json` from 530 to zero, pillar by pillar, so every printed answer is compared against a computation; then reduce the 77 exemptions by rewriting "Proof: see method" answers as the identity or bound they actually establish, which is better for students as well as for the pipeline.
