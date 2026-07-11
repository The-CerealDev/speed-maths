## 2026-07-11T19:59:07Z
You are the first Challenger. Your objective is to empirically verify the correctness of the verification scripts generated for Combinatorics worksheets 02, 03, and 04:
- `combinatorics/verify/sheet02_verify.py`
- `combinatorics/verify/sheet03_verify.py`
- `combinatorics/verify/sheet04_verify.py`

Verify that:
- The checks are NOT dummy/facade checks. If you temporarily change the expected answer in the script or in the tex file and run the script, does it raise an AssertionError? Make sure to restore the file after testing.
- The arithmetic is exact and doesn't rely on floating-point approximations where exact results are expected.

Write your challenge report in `/home/cereal-dev/Documents/speed-maths/.agents/challenger_m2_1/challenge.md` and send a message back to the parent (conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) with your verdict (PASS/FAIL) and the report path.
