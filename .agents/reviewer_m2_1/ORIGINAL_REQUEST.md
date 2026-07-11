## 2026-07-11T19:59:07Z

You are the first Reviewer. Your objective is to review the verification scripts generated for Combinatorics worksheets 02, 03, and 04:
- `combinatorics/verify/sheet02_verify.py`
- `combinatorics/verify/sheet03_verify.py`
- `combinatorics/verify/sheet04_verify.py`

Check the following:
- Conformance to speed-maths project requirements (R1: Independent Verification, R2: Exact Arithmetic, R3: Strict Structure, R4: Error Correction).
- Ensure all 33 questions are correctly mapped in the CHECKS dict and check functions.
- Verify that every check function's docstring starts with a valid strength tag (EXHAUSTIVE PROOF or SAMPLED CHECK).
- Check that the scripts execute successfully with code 0 and exit with code 2 under the -O flag.
- Run `tools/validate_verify_scripts.py` and verify these three scripts pass.

Write your review report in `/home/cereal-dev/Documents/speed-maths/.agents/reviewer_m2_1/review.md` and send a message back to the parent (conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) with your verdict (PASS/FAIL) and the report path.
