# Speed Maths

Computationally verified corpus for TMUA and Competition(SMC, BMO1) preparation.

## For Students (TMUA & Competition Prep)

If you are revising for university admissions tests, you know the two biggest problems: past papers run out fast, and textbook answer keys are constantly wrong. 

This repository contains over 1,000 original questions across 4 pillars (Algebra, Combinatorics, Logic, Number Theory). **Every single solution in this repository is mathematically proven.** You will never waste an hour doubting your sanity because a textbook printed `56` instead of `65`.

**How to use this:**
1. Navigate to the `sheets/` directory of any pillar.
2. Do one daily drill.
3. Check your work against the `answers/` directory. If the answer key says you are wrong, you are wrong. The answers have been proven by a computational compiler.

---

## Architecture (For Engineers & Contributors)

The solutions in this repository are verified by a strict CI pipeline operating under `verify/` within each pillar.

1. **AST Parsing (`tools/latex_bridge.py`)**: Strips `.tex` formatting, handles juxtaposition edge cases, and compiles expressions (e.g., `\ans{\frac{x(x+1)}{2}}`) into symbolic SymPy nodes.
2. **Property-Based Testing (`hypothesis`)**: Fuzz-tests abstract combinatorial recurrence relations and algebraic identities across randomized integer boundaries.
3. **Mutation Testing (`mutmut`)**: The CI suite mutates the Python checks across 900+ tests to guarantee no trivial tautologies or facade tests falsely pass the suite.

If a math error exists in the PDFs, it means SymPy was beaten.

## Layout

```text
Speed-Maths/
├── shared/
│   └── preamble.tex           (LaTeX styles and macros)
├── algebra/
│   ├── sheets/ & answers/     (100% verified)
│   └── verify/                (CI proofs)
├── combinatorics/
│   ├── sheets/ & answers/     (100% verified)
│   └── verify/                (CI proofs)
├── number-theory/
│   ├── sheets/ & answers/     (100% verified)
│   └── verify/                (CI proofs)
├── logic/
│   ├── sheets/ & answers/     (100% verified)
│   └── verify/                (CI proofs)
├── tools/
│   ├── latex_bridge.py        (LaTeX AST compiler)
│   ├── validate_verify_scripts.py 
│   └── build_website.py       
├── template.html              
└── index.html                 (Auto-generated artifact)
```

## Conventions

New pillars (Calculus, Sequences, Graphs) cannot be merged without a passing Python verification script. See `CONTRIBUTING.md` for verification guidelines using `tools.latex_bridge.get_answer()`.

- **Numbering:** Two-digit, zero-padded (`sheet01`).
- **LaTeX:** Include `\input{../../shared/preamble}`.
- **Answers:** Wrap in `\ans{...}` for `latex_bridge` parsing.
- **Compilation:** Execute `pdflatex` from within `sheets/` or `answers/`.

## The Bounty (Hall of Fame)

We are extremely confident in the CI pipeline. If you find a mathematical error in any of the compiled answer keys, open a GitHub Issue. If you can successfully prove that a mathematically incorrect answer bypassed the SymPy/Hypothesis verification scripts, your name will be permanently added to the Hall of Fame below.

*No bounties claimed yet.*

## Roadmap

The static PDF corpus is open source. 
Development is currently focused on the Variant Retriever: an error-based semantic search engine that encodes human cognitive errors into 384-dimensional continuous vector spaces to map mistakes to past paper distractors. It remains in closed beta.
