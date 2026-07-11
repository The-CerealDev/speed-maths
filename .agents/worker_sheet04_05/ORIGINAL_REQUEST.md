## 2026-07-11T18:59:14Z

You are a worker subagent.
Your task is to implement the Python verification scripts for Algebra Sheet 04 and Sheet 05:
1. `algebra/verify/sheet04_verify.py`
2. `algebra/verify/sheet05_verify.py`

You must follow these rules:
- R1: Independent Verification (genuine check route, not duplicating the method).
- R2: Exact Arithmetic Only (strictly standard library modules: math, itertools, fractions.Fraction. No sympy or other third-party libraries).
- R3: Strict Structure (boilerplate from sheet01_verify.py, -O guard, CHECKS dict, check_A1...check_D5 functions, matching the exact format of sheet01_verify.py).
- R4: Error Correction Protocol (if a mathematical error is found in the source .tex file, directly edit the .tex file to fix it, then ensure the script passes).

You can read details about the questions and answers from:
- `/home/cereal-dev/Documents/speed-maths/.agents/explorer_m1/analysis.md`
- `/home/cereal-dev/Documents/speed-maths/algebra/answers/ans04.tex`
- `/home/cereal-dev/Documents/speed-maths/algebra/answers/ans05.tex`
- `/home/cereal-dev/Documents/speed-maths/algebra/verify/sheet01_verify.py` (for the boilerplate/structure reference)

After implementing the scripts, run the validation tool `python3 tools/validate_verify_scripts.py` to ensure they pass the structure and execution checks. If there are any errors in the latex source files, edit them directly to correct them, and update the verification scripts accordingly.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

When finished, write a report detailing your work and send it back to the parent.
