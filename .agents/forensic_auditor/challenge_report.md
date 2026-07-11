## Challenge Summary

**Overall risk assessment**: MEDIUM (due to facade check in `sheet05_verify.py`)

## Challenges

### [High] Challenge 1: Facade verification logic in `sheet05_verify.py` check_B7

- **Assumption challenged**: Asserting `p**2 - 2*q == (-p)**2 - 2*q` checks the correctness of the roots transformation.
- **Attack scenario**: If the LaTeX file contained an incorrect formula, e.g., $x^2 - (p^2 - 3q)x + q^2 = 0$, the verification script would still pass because the assertion is a mathematical tautology ($p^2 = p^2$) and does not verify the formula.
- **Blast radius**: Undetected errors in answer sheets if incorrect formulas are introduced.
- **Mitigation**: Rewrite `check_B7` to randomly sample roots $r, s$ as Fractions, define $p = -(r+s)$, $q = r \cdot s$, and assert that the sum of squared roots $r^2+s^2$ is indeed equal to $p^2 - 2q$, and the product $r^2 \cdot s^2$ is equal to $q^2$:
  ```python
  r = Fraction(random.randint(-10, 10), random.randint(1, 10))
  s = Fraction(random.randint(-10, 10), random.randint(1, 10))
  p = -(r + s)
  q = r * s
  assert r**2 + s**2 == p**2 - 2*q
  assert r**2 * s**2 == q**2
  ```

### [Low] Challenge 2: Incomplete edge-case check for linear constraint in `sheet05_verify.py` check_C4

- **Assumption challenged**: Verifying $D > 0$ for $-1 < k < 4$ is sufficient to show two distinct real roots.
- **Attack scenario**: At $k = 0$, the discriminant $D = 16 > 0$, but the equation $kx^2-4x+k-3=0$ becomes $-4x-3=0$, which is linear and has only one real root, not two distinct roots. The check does not explicitly test or assert that $k \neq 0$ is excluded.
- **Blast radius**: Missing edge case verification in constraints.
- **Mitigation**: Add an assertion that $k \neq 0$ for any valid quadratic.

### [Low] Challenge 3: Float comparison tolerance limits

- **Assumption challenged**: Absolute tolerance of `1e-9` is sufficient for nested square root evaluations on all python versions and platforms.
- **Attack scenario**: Different versions of Python math libraries could cause calculations of surd expressions to have errors slightly larger than `1e-9`, leading to false positive test failures.
- **Blast radius**: Local test execution passes, but CI/CD or another user's machine fails on validation.
- **Mitigation**: Use `math.isclose(val1, val2, rel_tol=1e-9, abs_tol=1e-9)` for robust float comparison.

## Stress Test Results

- Checked:
  - `python3 -O algebra/verify/sheet04_verify.py` exits with code 2 (PASS)
  - `python3 algebra/verify/sheet04_verify.py` exits with code 0 (PASS)
  - `python3 -O algebra/verify/sheet05_verify.py` exits with code 2 (PASS)
  - `python3 algebra/verify/sheet05_verify.py` exits with code 0 (PASS)

## Unchallenged Areas

- TeX syntax parser — The TeX files are assumed to be syntactically correct and compiled successfully, as our focus was solely on the verification scripts' mathematical validity and integrity.
