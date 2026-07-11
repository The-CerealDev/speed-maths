Your objective is to generate exhaustive Python verification scripts for Combinatorics worksheets 02, 03, and 04:
- `combinatorics/verify/sheet02_verify.py`
- `combinatorics/verify/sheet03_verify.py`
- `combinatorics/verify/sheet04_verify.py`

Scope boundaries:
- Do NOT add external dependencies (only standard library).
- Do NOT use sympy or other third-party libraries.
- Limit modifications to the generated scripts and the source `.tex` files in `combinatorics/answers/` if errors are found.

Input information:
- Stated answers and methods are extracted in `/home/cereal-dev/Documents/speed-maths/.agents/explorer_m1/analysis.md`.
- Source answer files: `combinatorics/answers/ans02.tex`, `ans03.tex`, `ans04.tex`.
- Template structure: `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet01_verify.py`.

Requirements:
- R1: Independent Verification (genuine check route: e.g. count permutations/combinations using itertools, Cartesian products, bijections, or simulate state transition/recursion, not just multiplying numbers).
- R2: Exact Arithmetic Only (strictly standard libraries: math, itertools, fractions.Fraction).
- R3: Strict Structure (exact boilerplate from sheet01_verify.py: -O optimization guard checking `__debug__` and exiting with code 2, CHECKS dictionary mapping labels "A1"..."D5" to their check functions, check_A1...check_D5 functions). Each function docstring must start with 'EXHAUSTIVE PROOF' or 'SAMPLED CHECK'.
- R4: Error Correction Protocol (if a mathematical error is found in the source .tex file, directly edit the .tex file to fix it, then ensure the script passes).

Completion criteria:
- All three scripts run and pass.
- `tools/validate_verify_scripts.py` passes for all three scripts.
- Write a handoff report in your working directory `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheets_02_04/handoff.md` detailing the implemented checks and any corrections made to the `.tex` files.
- Send a message to the parent (conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) with status.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
