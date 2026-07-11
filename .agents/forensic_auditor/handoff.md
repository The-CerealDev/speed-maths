# Handoff Report: Forensic Audit of sheet04_verify.py and sheet05_verify.py

## 1. Observation
- Verified scripts paths:
  - `algebra/verify/sheet04_verify.py`
  - `algebra/verify/sheet05_verify.py`
- Executed commands and outputs:
  - `python3 algebra/verify/sheet04_verify.py` returned exit code 0 and printed:
    ```
    All 33 checks passed.
    ```
  - `python3 algebra/verify/sheet05_verify.py` returned exit code 0 and printed:
    ```
    All 33 checks passed.
    ```
  - `python3 tools/validate_verify_scripts.py` output:
    ```
    Validating algebra/verify/sheet04_verify.py...
      RESULT: PASS
    Validating algebra/verify/sheet05_verify.py...
      RESULT: PASS
    ```
- Inspected the source code of both files.
- In `algebra/verify/sheet05_verify.py`, the function `check_B7()` (lines 138-149) contains the following code:
  ```python
  def check_B7():
      """ SAMPLED CHECK: Random rational testing of root squared quadratic coefficients """
      for _ in range(50):
          p = Fraction(random.randint(-10, 10), random.randint(1, 10))
          q = Fraction(random.randint(-10, 10), random.randint(1, 10))
          # roots r, s of x^2 + px + q = 0 satisfy r+s = -p, r*s = q
          # roots r^2, s^2 satisfy sum r^2+s^2 = (r+s)^2 - 2rs = p^2 - 2q
          # product r^2*s^2 = q^2
          # Target quadratic is x^2 - (p^2 - 2q)x + q^2 = 0
          # Let's verify coefficients.
          assert p**2 - 2*q == (-p)**2 - 2*q
  ```
  Note that the final assertion is `assert p**2 - 2*q == (-p)**2 - 2*q`.

## 2. Logic Chain
- Step 1: Running the scripts dynamically confirms that both scripts compile and run successfully (Observation section).
- Step 2: Running `tools/validate_verify_scripts.py` confirms that both scripts meet structural standards (Observation section).
- Step 3: Detailed static code review of `sheet05_verify.py`'s `check_B7()` reveals that the assertion is `p**2 - 2*q == (-p)**2 - 2*q` (Observation section).
- Step 4: Mathematically, $(-p)^2 = p^2$, so the assertion is always true regardless of $p$ and $q$, and does not test any relation between roots of the quadratic and the target formula. Thus, it is a facade check.
- Conclusion: Because `sheet05_verify.py` contains a facade check, it fails the integrity audit and constitutes an INTEGRITY VIOLATION under development mode rules.

## 3. Caveats
- Checked only the algebra files `sheet04_verify.py` and `sheet05_verify.py` as requested. Other verification scripts (like combinatorics files or other algebra sheets) are outside the scope of this audit.

## 4. Conclusion
- Verdict is **INTEGRITY VIOLATION**. A facade check was found in `algebra/verify/sheet05_verify.py` function `check_B7`.
- Recommended remediation: Rewrite `check_B7()` in `algebra/verify/sheet05_verify.py` as follows:
  ```python
  def check_B7():
      """ SAMPLED CHECK: Random rational testing of root squared quadratic coefficients """
      for _ in range(50):
          r = Fraction(random.randint(-10, 10), random.randint(1, 10))
          s = Fraction(random.randint(-10, 10), random.randint(1, 10))
          p = -(r + s)
          q = r * s
          assert r**2 + s**2 == p**2 - 2*q
          assert r**2 * s**2 == q**2
  ```

## 5. Verification Method
- To independently verify, run:
  ```bash
  python3 algebra/verify/sheet04_verify.py
  python3 algebra/verify/sheet05_verify.py
  ```
- Inspect the file contents of:
  - `/home/cereal-dev/Documents/speed-maths/algebra/verify/sheet05_verify.py` at line 149 to see the assertion `assert p**2 - 2*q == (-p)**2 - 2*q`.
- Invalidation condition: Any changes to the assertion that make it verify the actual relationship of roots and coefficients.
