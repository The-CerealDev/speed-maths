# Handoff Report — validate_verify_scripts

## 1. Observation
- **Validator Script Path**: `/home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py`
- **Discovered Verification Scripts**:
  - `algebra/verify/sheet01_verify.py`
  - `combinatorics/verify/sheet01_verify.py`
  - `combinatorics/verify/sheet07_verify.py`
- **E2E Command Execution**:
  ```bash
  python3 /home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py
  ```
- **Verbatim Output**:
  ```
  Found 3 verification script(s) to validate.
  Validating algebra/verify/sheet01_verify.py...
    RESULT: PASS

  Validating combinatorics/verify/sheet01_verify.py...
    RESULT: FAIL
      * Check function docstring violations:
      *   - check_A10 docstring does not contain either 'EXHAUSTIVE PROOF' or 'SAMPLED CHECK'. Got: "STRONG-BUT-FINITE: this is an algebraic identity in n, so it cannot\nbe brute-forced over an infinite domain. Verified for n = 1..30 using\nmath.factorial computed directly (a route independent of the method's\nmanual cancellation) — strong evidence, not a full symbolic proof."

  Validating combinatorics/verify/sheet07_verify.py...
    RESULT: FAIL
      * Missing expected check function definitions: check_A2, check_A3, check_A4, check_A5, check_A6, check_A7, check_A8, check_A9, check_A10, check_B1, check_B2, check_B3, check_B4, check_B5, check_B6, check_B7, check_B8, check_B9, check_B10, check_C1, check_C2, check_C3, check_C4, check_C5, check_C6, check_C7, check_C8, check_D1, check_D3, check_D4
      * Check function docstring violations:
      *   - check_A1 is missing a docstring.
      *   - check_D2 is missing a docstring.
      *   - check_D5 is missing a docstring.

  Some verification scripts failed validation.
  ```
- **Exit Code**: Exited with code `1`.

## 2. Logic Chain
- **Script Location & Discovery**: The validator uses glob pattern matching to find files of form `sheet[0-9][0-9]_verify.py` under the `algebra/verify/` and `combinatorics/verify/` folders. This aligns with layout requirements.
- **Execution Checking**: Subprocess execution is performed with and without `-O` flags (running under `sys.executable`). If a run without `-O` returns anything other than `0` (or runs with `-O` return anything other than `2`), it is reported as a failure.
- **AST Parsing**:
  - The script's AST is built via `ast.parse`.
  - The `main()` function is checked to verify it contains the guard node `if not __debug__:` (represented in AST as a unary negation of name `__debug__`).
  - The module-level assignment to `CHECKS` is parsed as a dictionary mapping label strings to check function names.
  - The presence of the 33 standard worksheet question label functions (`check_A1` to `check_D5`) is verified.
  - Docstrings are inspected using `ast.get_docstring()` to ensure the presence of tags `"EXHAUSTIVE PROOF"` or `"SAMPLED CHECK"` (case-insensitive).
- **Outcome**: The E2E run successfully validated the compliant `algebra/verify/sheet01_verify.py` script, while correctly highlighting specific docstring omissions in `combinatorics/verify/sheet01_verify.py` and structural/docstring omissions in the incomplete `combinatorics/verify/sheet07_verify.py`.

## 3. Caveats
- No terminal linters (like pylint/flake8) were available on the user system. A py_compile check was run instead to verify syntactical correctness.
- The validator assumes the 33 standard question labels per sheet layout. If sheets have non-standard layouts or differing counts, the `get_expected_labels()` function inside the validator script would need adjustment.

## 4. Conclusion
- The validator script is complete, correct, and conforms to all project rules.
- Running it detects the specific non-conformances in the existing codebase as requested.

## 5. Verification Method
1. Run the validator:
   ```bash
   python3 /home/cereal-dev/Documents/speed-maths/tools/validate_verify_scripts.py
   ```
2. Inspect the output to ensure:
   - `algebra/verify/sheet01_verify.py` passes.
   - `combinatorics/verify/sheet01_verify.py` fails due to `check_A10` missing a valid docstring tag.
   - `combinatorics/verify/sheet07_verify.py` fails due to missing definitions (not fully complete) and missing docstrings.
   - The exit code of the validator script itself is non-zero (specifically `1`).
