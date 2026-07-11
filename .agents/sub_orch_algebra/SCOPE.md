# Scope: Algebra Verification Scripts

## Architecture
Each sheet verification script `algebra/verify/sheetNN_verify.py` is written in Python, using only standard library modules (like `math`, `itertools`, `fractions.Fraction`). It contains:
- `check_A1` through `check_D5` functions.
- A module-level `CHECKS` dictionary mapping label to function.
- A `main()` runner that verifies that assertions are enabled (re-checking that it isn't run with `-O`/`PYTHONOPTIMIZE`).
- Each check function has a docstring specifying either `"SAMPLED CHECK"` or `"EXHAUSTIVE PROOF"`.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| 1 | Sheets 02 & 03 | Implement and validate `algebra/verify/sheet02_verify.py` and `algebra/verify/sheet03_verify.py` | None | DONE |
| 2 | Sheets 04 & 05 | Implement and validate `algebra/verify/sheet04_verify.py` and `algebra/verify/sheet05_verify.py` | M1 | IN_PROGRESS |
| 3 | Sheets 06 & 07 | Implement and validate `algebra/verify/sheet06_verify.py` and `algebra/verify/sheet07_verify.py` | M2 | PLANNED |

## Interface Contracts
- The verification scripts must run successfully when invoked as `python3 algebra/verify/sheetNN_verify.py` (exit code 0).
- The verification scripts must fail with exit code 2 when invoked as `python3 -O algebra/verify/sheetNN_verify.py`.
- No third-party packages (like `sympy`) can be imported or used.
- Error Correction Protocol (R4): If any mathematical error is found in the LaTeX answer key (`algebra/answers/ansNN.tex`), the file must be edited directly to correct the error, and the verification script must verify the corrected math.
