"""Computational verification for combinatorics/answers/ans04.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer.

Run directly:
    python3 sheet04_verify.py
"""

import itertools
import math
from fractions import Fraction

# Helper functions for polynomial operations
def poly_mul(p1, p2):
    res = [0] * (len(p1) + len(p2) - 1)
    for i, c1 in enumerate(p1):
        for j, c2 in enumerate(p2):
            res[i + j] += c1 * c2
    return res

def poly_pow(p, power):
    res = [1]
    for _ in range(power):
        res = poly_mul(res, p)
    return res

# Helper for multivariate polynomial multiplication (variables: a, b, c)
def mv_poly_mul(p1, p2):
    res = {}
    for k1, c1 in p1.items():
        for k2, c2 in p2.items():
            new_k = tuple(x + y for x, y in zip(k1, k2))
            res[new_k] = res.get(new_k, 0) + c1 * c2
    return res

# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: coefficient of x^2 in (1+x)^5 using polynomial multiplication."""
    p = poly_pow([1, 1], 5)
    ans_val = p[2]
    assert ans_val == 10
    assert math.comb(5, 2) == 10

def check_A2():
    """EXHAUSTIVE PROOF: coefficient of x in (x+2)^3. Check sum of coefficients is 27 at x=1."""
    p = poly_pow([2, 1], 3)
    ans_val = p[1]
    assert ans_val == 12
    assert math.comb(3, 1) * 2**2 == 12
    assert sum(p) == 27

def check_A3():
    """EXHAUSTIVE PROOF: Row 5 of Pascal's triangle."""
    ans_val = [math.comb(5, k) for k in range(6)]
    assert ans_val == [1, 5, 10, 10, 5, 1]

def check_A4():
    """EXHAUSTIVE PROOF: Coefficient of x^3 y^2 in (x+y)^5 using multivariate expansion."""
    # base is x+y: represented as (exponent_x, exponent_y)
    base = {(1, 0): 1, (0, 1): 1}
    res = {(0, 0): 1}
    for _ in range(5):
        # We can implement a 2D polynomial multiplication
        new_res = {}
        for k1, c1 in res.items():
            for k2, c2 in base.items():
                new_k = (k1[0]+k2[0], k1[1]+k2[1])
                new_res[new_k] = new_res.get(new_k, 0) + c1 * c2
        res = new_res
    ans_val = res[(3, 2)]
    assert ans_val == 10
    assert math.comb(5, 2) == 10

def check_A5():
    """EXHAUSTIVE PROOF: Sum of all coefficients of (1+x)^7."""
    p = poly_pow([1, 1], 7)
    ans_val = sum(p)
    assert ans_val == 128
    assert 2**7 == 128

def check_A6():
    """EXHAUSTIVE PROOF: Constant term of (x + 1/x)^4 is the x^4 term of (x^2+1)^4."""
    p = poly_pow([1, 0, 1], 4)
    ans_val = p[4]
    assert ans_val == 6
    assert math.comb(4, 2) == 6

def check_A7():
    """EXHAUSTIVE PROOF: Pascal's rule check C(9,4) + C(9,5) == C(100,5) is not true but C(9,4)+C(9,5)==C(10,5)."""
    assert math.comb(9, 4) + math.comb(9, 5) == math.comb(10, 5) == 252

def check_A8():
    """EXHAUSTIVE PROOF: Alternating sum of row 6."""
    ans_val = sum((-1)**k * math.comb(6, k) for k in range(7))
    assert ans_val == 0

def check_A9():
    """EXHAUSTIVE PROOF: Coefficient of x^2 in (1-x)^10 is not negative."""
    p = poly_pow([1, -1], 10)
    ans_val = p[2]
    assert ans_val == 45
    assert ans_val > 0

def check_A10():
    """EXHAUSTIVE PROOF: Largest coefficient in (1+x)^4."""
    p = poly_pow([1, 1], 4)
    ans_val = max(p)
    assert ans_val == 6
    assert math.comb(4, 2) == 6

# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Coefficient of x^3 in (2+3x)^5."""
    p = poly_pow([2, 3], 5)
    ans_val = p[3]
    assert ans_val == 1080
    assert math.comb(5, 3) * (2**2) * (3**3) == 1080
    assert sum(p) == 3125

def check_B2():
    """EXHAUSTIVE PROOF: Coefficient of x^5 in (1+2x)^4 (1+x)^3."""
    p1 = poly_pow([1, 2], 4)
    p2 = poly_pow([1, 1], 3)
    p = poly_mul(p1, p2)
    ans_val = p[5]
    assert ans_val == 168

def check_B3():
    """EXHAUSTIVE PROOF: Constant term of (2x + 1/x^2)^6 is coefficient of x^12 in (2x^3+1)^6."""
    p = poly_pow([1, 0, 0, 2], 6)
    ans_val = p[12]
    assert ans_val == 240
    assert math.comb(6, 2) * (2**4) == 240

def check_B4():
    """EXHAUSTIVE PROOF: Solve C(n,2) == 66 in range 2..50."""
    solutions = [n for n in range(2, 51) if math.comb(n, 2) == 66]
    assert len(solutions) == 1
    assert solutions[0] == 12
    assert 12 * 11 // 2 == 66

def check_B5():
    """EXHAUSTIVE PROOF: Coefficient of x^6 in (x^2 + 1/x)^6 is coefficient of x^12 in (x^3+1)^6."""
    p = poly_pow([1, 0, 0, 1], 6)
    ans_val = p[12]
    assert ans_val == 15
    assert math.comb(6, 2) == 15

def check_B6():
    """EXHAUSTIVE PROOF: Coefficient of x^2 in (1+2x)^4 (1-x)^2."""
    p1 = poly_pow([1, 2], 4)
    p2 = poly_pow([1, -1], 2)
    p = poly_mul(p1, p2)
    ans_val = p[2]
    assert ans_val == 9

def check_B7():
    """EXHAUSTIVE PROOF: Evaluate 11^3 and 9^3."""
    assert 11**3 == 1331
    assert 9**3 == 729
    # Binomial expansion checks
    assert sum(math.comb(3, k) * 10**(3-k) for k in range(4)) == 1331
    assert sum(math.comb(3, k) * 10**(3-k) * (-1)**k for k in range(4)) == 729

def check_B8():
    """EXHAUSTIVE PROOF: solve for k where C(6,3) * k^3 == 160."""
    solutions = [k for k in range(-10, 11) if math.comb(6, 3) * k**3 == 160]
    assert len(solutions) == 1
    assert solutions[0] == 2

def check_B9():
    """EXHAUSTIVE PROOF: solve C(n,2) == C(n,3) in range 3..50."""
    solutions = [n for n in range(3, 51) if math.comb(n, 2) == math.comb(n, 3)]
    assert len(solutions) == 1
    assert solutions[0] == 5

def check_B10():
    """EXHAUSTIVE PROOF: Coefficient of a^2 b^2 c in (a+b+c)^5."""
    base = {(1, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1}
    res = {(0, 0, 0): 1}
    for _ in range(5):
        res = mv_poly_mul(res, base)
    ans_val = res[(2, 2, 1)]
    assert ans_val == 30
    assert math.factorial(5) // (math.factorial(2) * math.factorial(2) * math.factorial(1)) == 30

# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Sum of even-index coefficients in row 10."""
    ans_val = sum(math.comb(10, k) for k in range(0, 11, 2))
    assert ans_val == 512
    assert 2**9 == 512

def check_C2():
    """EXHAUSTIVE PROOF: Greatest coefficient in (1+x)^8."""
    p = poly_pow([1, 1], 8)
    ans_val = max(p)
    assert ans_val == 70
    assert math.comb(8, 4) == 70

def check_C3():
    """EXHAUSTIVE PROOF: Estimate 1.01^10 from three terms using fractions."""
    ans_val = Fraction(1) + Fraction(10, 100) + Fraction(45, 10000)
    assert ans_val == Fraction(11045, 10000)

def check_C4():
    """EXHAUSTIVE PROOF: solve for n where C(n,5)*3^5 == 3 * C(n,4)*3^4 in range 5..50."""
    solutions = [n for n in range(5, 51) if math.comb(n, 5) * 3**5 == 3 * math.comb(n, 4) * 3**4]
    assert len(solutions) == 1
    assert solutions[0] == 9

def check_C5():
    """EXHAUSTIVE PROOF: Coefficient of x^4 in (1+x)^5 (1-2x)^3."""
    p1 = poly_pow([1, 1], 5)
    p2 = poly_pow([1, -2], 3)
    p = poly_mul(p1, p2)
    ans_val = p[4]
    assert ans_val == 25

def check_C6():
    """EXHAUSTIVE PROOF: evaluate sum(k * C(5,k) for k=0..5)."""
    ans_val = sum(k * math.comb(5, k) for k in range(6))
    assert ans_val == 80
    assert 5 * 2**4 == 80

def check_C7():
    """EXHAUSTIVE PROOF: evaluate sum(C(6,k) * 2^k for k=0..6)."""
    ans_val = sum(math.comb(6, k) * 2**k for k in range(7))
    assert ans_val == 729
    assert 3**6 == 729

def check_C8():
    """EXHAUSTIVE PROOF: check row 7 is generated from row 6."""
    row_6 = [math.comb(6, k) for k in range(7)]
    row_7 = [1] + [row_6[i] + row_6[i+1] for i in range(6)] + [1]
    assert row_7 == [1, 7, 21, 35, 35, 21, 7, 1]

# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """SAMPLED CHECK: verify C(2n, n) is even for n = 1..50."""
    for n in range(1, 51):
        assert math.comb(2 * n, n) % 2 == 0

def check_D2():
    """EXHAUSTIVE PROOF: sum(C(10, k)^2) == C(20, 10)."""
    lhs = sum(math.comb(10, k)**2 for k in range(11))
    rhs = math.comb(20, 10)
    assert lhs == rhs == 184756

def check_D3():
    """EXHAUSTIVE PROOF: check that only k=0,4,8,12 yield odd C(12, k)."""
    odd_k = [k for k in range(13) if math.comb(12, k) % 2 == 1]
    assert odd_k == [0, 4, 8, 12]

def check_D4():
    """EXHAUSTIVE PROOF: check sum(C(m, 2) for m=2..9) == C(10, 3)."""
    lhs = sum(math.comb(m, 2) for m in range(2, 10))
    rhs = math.comb(10, 3)
    assert lhs == rhs == 120

def check_D5():
    """SAMPLED CHECK: check p | C(p, k) for all primes p < 50 and 0 < k < p."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for p in primes:
        for k in range(1, p):
            assert math.comb(p, k) % p == 0

# ═══════════════════════════════════════════════════════════════════════
# Execution setup
# ═══════════════════════════════════════════════════════════════════════

CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4,
    "C5": check_C5, "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
}

def main():
    if not __debug__:
        print("ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.")
        raise SystemExit(2)

    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f"  PASS  {label}")
        except AssertionError as e:
            failures.append(label)
            print(f"  FAIL  {label}: {e}")
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f"All {len(CHECKS)} checks passed.")

if __name__ == "__main__":
    main()
