# Original User Request

## Initial Request — 2026-07-11T19:55:59+01:00

You are the Algebra sub-orchestrator.
Your working directory is /home/cereal-dev/Documents/speed-maths/.agents/sub_orch_algebra.
Your objective is to generate exhaustive Python verification scripts for the remaining 6 Algebra worksheet answer keys (Algebra 02-07) in the repository:
- `algebra/verify/sheet02_verify.py`
- `algebra/verify/sheet03_verify.py`
- `algebra/verify/sheet04_verify.py`
- `algebra/verify/sheet05_verify.py`
- `algebra/verify/sheet06_verify.py`
- `algebra/verify/sheet07_verify.py`
Each script must match the exact conventions established in the existing `sheet01_verify.py` scripts and satisfy:
- R1: Independent Verification (genuine check route, not duplicating the method).
- R2: Exact Arithmetic Only (strictly standard library modules: math, itertools, fractions.Fraction. No sympy or other third-party libraries).
- R3: Strict Structure (boilerplate from sheet01_verify.py, -O guard, CHECKS dict, check_A1...check_D5 functions).
- R4: Error Correction Protocol (if a mathematical error is found in the source .tex file, directly edit the .tex file to fix it, then ensure the script passes).

Since you are a sub-orchestrator, you must:
1. Decompose your work into milestones (e.g. Sheets 02-04, Sheets 05-07) or individual sheet tasks.
2. Run the iteration loop per sheet or milestone:
   - Spawn Explorers (or do exploration) to understand the questions and formulate checks. (Wait, the first explorer already extracted all question/method details into `/home/cereal-dev/Documents/speed-maths/.agents/explorer_m1/analysis.md`! You can read that file for details of the questions!).
   - Spawn Workers to implement the verification scripts.
   - Spawn Reviewers/Challengers to review and run checks on the scripts.
   - Spawn Forensic Auditor to perform integrity forensics.
3. Validate your work by running `tools/validate_verify_scripts.py` on the generated scripts.
4. When done, write your `handoff.md` and notify the parent orchestrator (conversation ID: 48cb6d3e-9d66-481b-8fdf-b3dcd4d8c274).

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
