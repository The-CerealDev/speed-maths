## 2026-07-11T19:56:27+01:00
Your objective is to fix `combinatorics/verify/sheet01_verify.py` so that check_A10's docstring includes a valid strength tag ('EXHAUSTIVE PROOF' or 'SAMPLED CHECK') to make it pass the validator script.

Scope boundaries:
- Do NOT modify any other files.
- Do NOT add external dependencies.

Input information:
- File path: `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet01_verify.py`
- Validator script: `/home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py`

Output requirements:
- Edit sheet01_verify.py to replace 'STRONG-BUT-FINITE' in check_A10's docstring with 'SAMPLED CHECK'.
- Run `python3 tools/validate_verify_scripts.py` to verify that the script passes.
- Write a handoff report in your working directory `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheet01` containing the diff and validation output.
- Send a message to the parent (conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0) with the path to your handoff report and status.

Completion criteria:
- `tools/validate_verify_scripts.py` passes for `sheet01_verify.py`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
