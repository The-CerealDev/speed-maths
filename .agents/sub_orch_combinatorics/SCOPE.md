# Scope: Combinatorics Worksheet Verification

## Architecture
- All verification scripts reside in `combinatorics/verify/`.
- The target answer key files are in `combinatorics/answers/ans01.tex` through `ans07.tex`.
- Each script `sheetNN_verify.py` imports standard libraries (`math`, `itertools`, `fractions`, etc.) and implements:
  - `-O` optimization guard checking `__debug__` and exiting with code 2.
  - A module-level `CHECKS` dictionary mapping labels like `"A1"`, `"D5"` to their check functions.
  - A `main()` function executing all mapped checks in order and reporting results.
  - One function `check_<label>()` per question.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Fix Sheet 01 & Prep | Fix sheet01_verify.py docstring, prepare template, set up test run | None | DONE |
| 2 | Sheets 02-04 | Implement combinatorics/verify/sheet02_verify.py, sheet03_verify.py, sheet04_verify.py | M1 | PLANNED |
| 3 | Sheets 05-07 | Implement combinatorics/verify/sheet05_verify.py, sheet06_verify.py, and update sheet07_verify.py | M2 | PLANNED |
| 4 | Validation & Polish | Run tools/validate_verify_scripts.py and fix any remaining errors | M3 | PLANNED |

## Interface Contracts
- Valid strength tags in check function docstrings: `"EXHAUSTIVE PROOF"` or `"SAMPLED CHECK"`.
- Strictly standard library modules. No third-party modules.
- Strict structure matching the template: -O guard, CHECKS dictionary, check_A1...check_D5 functions.
