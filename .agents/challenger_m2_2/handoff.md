# Handoff Report — Challenger 2 Verification of Combinatorics Sheets 02-04

## 1. Observation

- **Verified scripts**:
  - `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet02_verify.py`
  - `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet03_verify.py`
  - `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet04_verify.py`
- **Verification execution**:
  - Command: `python3 run_all.py` inside `/home/cereal-dev/Documents/speed-maths/combinatorics/verify`
  - Result: All target scripts pass when unmodified.
    ```
    ── sheet02_verify.py ─────────────────────────────────
      PASS  A1
      ...
      PASS  D5
    All 33 checks passed.
    
    ── sheet03_verify.py ─────────────────────────────────
      PASS  A1
      ...
      PASS  D5
    All 33 checks passed.
    
    ── sheet04_verify.py ─────────────────────────────────
      PASS  A1
      ...
      PASS  D5
    All 33 checks passed.
    ```
- **Structure conformity**:
  - target scripts pass structural validations by `tools/validate_verify_scripts.py`.
- **Mutated Script Executions**:
  - **Sheet 02**: Changed `ans_val == 21` to `ans_val == 22` in `check_A1` of `sheet02_verify.py`. Running `python3 sheet02_verify.py` outputted:
    `FAIL  A1: Expected 22, got 21` and exited with status 1.
  - **Sheet 03**: Changed `ans_val == 120` to `ans_val == 121` in `check_A1` of `sheet03_verify.py`. Running `python3 sheet03_verify.py` failed with `FAIL  A1:` and exited with status 1.
  - **Sheet 04**: Changed `ans_val == 10` to `ans_val == 11` in `check_A1` of `sheet04_verify.py`. Running `python3 sheet04_verify.py` failed with `FAIL  A1:` and exited with status 1.
- **LaTeX Answer key Mutation**:
  - Changed `\ans{$21$}` to `\ans{$22$}` in `combinatorics/answers/ans02.tex`. Running `python3 sheet02_verify.py` passed with code 0 (no assertion error raised).
- **Arithmetic checks**:
  - No occurrences of floating-point division `/` were found in the verify scripts. Integer division `//` is used exclusively.
  - Rational approximation (e.g., in `sheet04_verify.py` question C3) utilizes `fractions.Fraction`.

## 2. Logic Chain

1. **Assertion Sensitivity**: Since modifying expected values inside the verification scripts (`sheet02_verify.py`, `sheet03_verify.py`, `sheet04_verify.py`) causes immediate failures (AssertionError) and exits with non-zero status (Observation 4), the checks are indeed active and not dummy or facade checks.
2. **Coupling Gap**: Since modifying the answer in `ans02.tex` did not cause `sheet02_verify.py` to fail (Observation 5), there is no direct runtime coupling between the LaTeX answer keys and the verification scripts.
3. **Exact Arithmetic**: Since all calculations and asserts are performed using integer operations (`//`, `math.comb`, `math.factorial`) or exact fractions (`fractions.Fraction`) (Observation 6), the arithmetic is exact and does not suffer from floating-point approximation error.

## 3. Caveats

- We assumed that any other sheet verify scripts (e.g., sheet01, sheet05-07) are out of scope. Note that `tools/validate_verify_scripts.py` failed on `algebra/verify/sheet05_verify.py` (missing import `itertools`) and `combinatorics/verify/sheet07_verify.py` (lacking docstrings/missing functions), but this does not affect the target scripts for sheets 02-04.

## 4. Conclusion

The verification scripts for Combinatorics Sheets 02, 03, and 04 are **PASS** (correct, non-dummy, and mathematically exact).
*Recommendation*: Address Challenge 1 (decoupling of verify scripts and LaTeX) by introducing a parser check that ensures LaTeX answer macro values match the verify scripts' expected answers.

## 5. Verification Method

To independently verify the verdict:
1. Run `python3 combinatorics/verify/run_all.py` to confirm all target scripts run and pass.
2. Mutate any target verification script (e.g., `/home/cereal-dev/Documents/speed-maths/combinatorics/verify/sheet02_verify.py`) expected value and run it again. Observe that it fails.
3. Check the code of the target verification scripts to verify they only use `//` and `Fraction`.
