## 2026-07-11T18:54:55Z
You are a developer worker.
Your working directory is /home/cereal-dev/Documents/speed-maths/.agents/worker_validate.
Your objective is to:
1. Write a Python script at `/home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py` that validates all worksheet verification scripts (`sheetNN_verify.py` in `algebra/verify/` and `combinatorics/verify/`).
2. The validator script must perform the following checks for each verification script:
   - Run the script (without `-O` flag) and verify it exits with code 0.
   - Run the script with `-O` flag (`python3 -O ...`) and verify it exits with code 2.
   - Read and parse the script content to ensure:
     - It has the `-O` optimization guard (`if not __debug__:` check inside `main()`).
     - It contains a `CHECKS` dictionary mapped to the corresponding check functions.
     - It defines check functions for all 33 standard worksheet question labels: A1 to A10, B1 to B10, C1 to C8, D1 to D5.
     - Each check function has a docstring that explicitly contains either the string "EXHAUSTIVE PROOF" or "SAMPLED CHECK" (case-insensitive).
3. The script must output clear success or failure messages for each check, and exit with code 0 if all scripts pass, or a non-zero exit code if any script fails.
4. Run python3 /home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py to test it (or write unit tests) and ensure it works. It should find and run whatever verification scripts currently exist (which at this point are `algebra/verify/sheet01_verify.py`, `combinatorics/verify/sheet01_verify.py`, and `combinatorics/verify/sheet07_verify.py` which might fail some checks if it is not fully complete - report this!).
5. When done, write your `handoff.md` in your working directory and notify the parent orchestrator (conversation ID: 48cb6d3e-9d66-481b-8fdf-b3dcd4d8c274).

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
