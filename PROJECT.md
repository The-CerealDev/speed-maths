# Project: Speed Maths Verification Scripts Generation

## Architecture
This project involves adding exhaustive computational verification scripts for 12 math worksheet answer keys (Algebra 02-07, Combinatorics 02-07).
The verification scripts are located in:
- `algebra/verify/sheetNN_verify.py`
- `combinatorics/verify/sheetNN_verify.py`

Each verification script acts as a test runner for its corresponding LaTeX answer key:
- `algebra/answers/ansNN.tex`
- `combinatorics/answers/ansNN.tex`

If any mathematical errors are found in the LaTeX answer keys during the generation/running of the verification scripts, we MUST directly modify the `.tex` files under `answers/` (and recompile the PDF using pdflatex if needed) to ensure the sheet answers and methods match the truth.

## Code Layout
- `algebra/answers/ans01.tex` ... `ans07.tex` — LaTeX answer keys
- `algebra/verify/sheet01_verify.py` ... `sheet07_verify.py` — Python verification scripts
- `combinatorics/answers/ans01.tex` ... `ans07.tex` — LaTeX answer keys
- `combinatorics/verify/sheet01_verify.py` ... `sheet07_verify.py` — Python verification scripts
- `combinatorics/verify/run_all.py` — Run all combinatorics verify scripts
- `tools/validate_verify_scripts.py` — Test validator for structure compliance (E2E Test Track)

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | Exploration & Global Planning | Retrieve and catalog all questions, initialize project files | none | DONE |
| M2 | E2E Testing Track | Design and implement `tools/validate_verify_scripts.py` | none | DONE |
| M3 | Algebra sheets 02-04 | Generate & verify sheet02, sheet03, sheet04 scripts | M1, M2 | IN_PROGRESS (Conv: 466bff0e-c0ed-4bb0-9733-b579a67fac58) |
| M4 | Algebra sheets 05-07 | Generate & verify sheet05, sheet06, sheet07 scripts | M3 | IN_PROGRESS (Conv: 466bff0e-c0ed-4bb0-9733-b579a67fac58) |
| M5 | Combinatorics sheets 02-04 | Generate & verify sheet02, sheet03, sheet04 scripts | M1, M2 | IN_PROGRESS (Conv: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) |
| M6 | Combinatorics sheets 05-07 | Generate & verify sheet05, sheet06, sheet07 scripts (updating 07) | M5 | IN_PROGRESS (Conv: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) |
| M7 | E2E Validation & Hardening | Final run of all scripts, E2E validator, and coverage checks | M4, M6 | PLANNED |

## Interface Contracts
### LaTeX ↔ Python Verification
- A verification script named `sheetNN_verify.py` is paired with `ansNN.tex`.
- For every question in section `<S>` number `<N>` in `ansNN.tex`, there must exist a function `check_<S><N>()` in `sheetNN_verify.py` (e.g. `check_A1`, `check_D5`).
- The script must throw `AssertionError` if the answer or any checkable method claim in `ansNN.tex` is mathematically incorrect.
- The script must execute without flags (`python3 sheetNN_verify.py`) and exit with `0` on success.
- If run with `-O` flag, the script must print an error and exit with code `2`.
