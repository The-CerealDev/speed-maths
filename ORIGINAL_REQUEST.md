# Original User Request

## Initial Request — 2026-07-11T18:51:37Z

Generate exhaustive Python verification scripts for the remaining 12 math worksheet answer keys (Algebra 02-07, Combinatorics 02-07) in the repository, matching the exact conventions established in the existing `sheet01_verify.py` scripts.

Working directory: `/home/cereal-dev/Documents/speed-maths/`
Integrity mode: development

## Requirements

### R1. Independent Mathematical Verification
Every `check_()` function must compute the answer through a genuinely different route than the `\method{}` block (e.g., full brute-force enumeration, exact numerical evaluation of roots) rather than just re-typing the method's algebraic steps.

### R2. Exact Arithmetic Only
Use strictly standard library modules (`math`, `itertools`, `fractions.Fraction`). Avoid floating-point errors entirely by using exact Fraction arithmetic where necessary. No `sympy` or third-party libraries.

### R3. Strict Execution Structure
Each script must exactly mirror the boilerplate from `sheet01_verify.py`, including the `-O` flag guard in `main()`, the dictionary of `CHECKS`, and the exact naming convention (`check_A1`, etc.) corresponding to the LaTeX file.

### R4. Error Correction Protocol
If the agent discovers a mathematical error in the source `.tex` answer sheet during verification, the agent MUST directly edit the `.tex` file to fix the mathematical error (updating both `\ans` and `\method` if necessary), and then ensure the verification script passes against the newly corrected math.

## Acceptance Criteria

### Execution & Correctness
- [ ] Running `python3 <sheet_name>_verify.py` completes successfully with exit code 0 for all 12 generated files.
- [ ] No `ZeroDivisionError`, `MemoryError`, or floating-point precision assertions fail.
- [ ] Every question in the `.tex` answer sheet has a corresponding check function.
- [ ] The script accurately throws an `AssertionError` if an answer in the `.tex` file is mathematically incorrect.
