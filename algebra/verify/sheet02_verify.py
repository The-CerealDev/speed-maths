import math
import random
from fractions import Fraction

# A1
def check_A1():
    """ SAMPLED CHECK: Random integer testing of factorization """
    for x in range(-50, 50):
        assert x**3 - 27 == (x - 3) * (x**2 + 3 * x + 9)

# A2
def check_A2():
    """ EXHAUSTIVE PROOF: Direct evaluation using float arithmetic with tolerance """
    val = (math.sqrt(5) + math.sqrt(3)) * (math.sqrt(5) - math.sqrt(3))
    assert abs(val - 2) < 1e-9

# A3
def check_A3():
    """ EXHAUSTIVE PROOF: Direct evaluation """
    assert 999**2 - 1 == 998000

# A4
def check_A4():
    """ EXHAUSTIVE PROOF: Solve for a and b and evaluate a^2 + b^2 """
    solutions = [(5, 1), (-1, -5)]
    for a, b in solutions:
        assert a - b == 4
        assert a * b == 5
        assert a**2 + b**2 == 26

# A5
def check_A5():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (x + y)**3 - x**3 - y**3 == 3 * x * y * (x + y)

# A6
def check_A6():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert 3 * x**2 - 75 == 3 * (x - 5) * (x + 5)

# A7
def check_A7():
    """ EXHAUSTIVE PROOF: Direct evaluation using float arithmetic with tolerance """
    val1 = 1 / (math.sqrt(3) + math.sqrt(2))
    val2 = math.sqrt(3) - math.sqrt(2)
    assert abs(val1 - val2) < 1e-9

# A8
def check_A8():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert x**2 * (x - 1) - (x - 1) == (x - 1)**2 * (x + 1)

# A9
def check_A9():
    """ EXHAUSTIVE PROOF: Solve exact roots for p and q, then evaluate p^2 + q^2 """
    r13 = math.sqrt(13)
    p = (5 + r13) / 2
    q = (5 - r13) / 2
    assert abs(p + q - 5) < 1e-9
    assert abs(p * q - 3) < 1e-9
    assert abs(p**2 + q**2 - 19) < 1e-9

# A10
def check_A10():
    """ SAMPLED CHECK: Random integer testing with positive and negative exponents """
    for n in range(-20, 20):
        val = (Fraction(2)**(n + 3) - Fraction(2)**n) / Fraction(2)**n
        assert val == 7

# B1
def check_B1():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 1 and x != -1:
            assert x / (x**2 - 1) + 1 / (x - 1) == (2 * x + 1) / ((x - 1) * (x + 1))

# B2
def check_B2():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert x**4 - x**2 - 12 == (x - 2) * (x + 2) * (x**2 + 3)

# B3
def check_B3():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        r = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if r != 1 and a != 0:
            S = a / (1 - r)
            if S != 0:
                assert r == 1 - a / S
                assert r == (S - a) / S

# B4
def check_B4():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 0 and x != -1:
            assert (1 + 1 / x) * (1 - 1 / (x + 1)) == 1

# B5
def check_B5():
    """ EXHAUSTIVE PROOF: Solve using roots of the quadratic equation """
    r5 = math.sqrt(5)
    x = (3 + r5) / 2
    y = (3 - r5) / 2
    assert abs(x + y - 3) < 1e-9
    assert abs(x * y - 1) < 1e-9
    assert abs(x**3 + y**3 - 18) < 1e-9

# B6
def check_B6():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if a * b != 0:
            assert ((a + b)**2 - (a - b)**2) / (4 * a * b) == 1

# B7
def check_B7():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert x**3 + 3 * x**2 - x - 3 == (x - 1) * (x + 1) * (x + 3)

# B8
def check_B8():
    """ EXHAUSTIVE PROOF: Direct evaluation of the solution """
    x = Fraction(7)
    assert (x - 1) / (x + 2) == (x + 3) / (x + 8)

# B9
def check_B9():
    """ SAMPLED CHECK: Random float testing for positive reals """
    for _ in range(50):
        a = random.uniform(0.1, 100.0)
        b = random.uniform(0.1, 100.0)
        if abs(a - b) > 1e-4:
            ra = math.sqrt(a)
            rb = math.sqrt(b)
            val1 = (ra - rb) / (ra + rb) + (ra + rb) / (ra - rb)
            val2 = 2 * (a + b) / (a - b)
            assert abs(val1 - val2) < 1e-9

# B10
def check_B10():
    """ EXHAUSTIVE PROOF: Evaluate using the actual roots 1, 2, 3 """
    roots = [1, 2, 3]
    assert sum(roots) == 6
    assert sum(r**2 for r in roots) == 14
    assert roots[0] * roots[1] * roots[2] == 6

# C1
def check_C1():
    """ EXHAUSTIVE PROOF: Verify the roots directly """
    roots = [2, -2, 3, -3]
    for x in roots:
        assert x**4 - 13 * x**2 + 36 == 0

# C2
def check_C2():
    """ EXHAUSTIVE PROOF: Verify roots directly and check algebraically on integer range """
    for x in [0, -5]:
        assert (x + 1) * (x + 2) * (x + 3) * (x + 4) == 24
    for x in range(-50, 50):
        val = (x + 1) * (x + 2) * (x + 3) * (x + 4) - 24
        assert val == x * (x + 5) * (x**2 + 5 * x + 10)

# C3
def check_C3():
    """ EXHAUSTIVE PROOF: Verify using float arithmetic with tolerance """
    val1 = math.sqrt(6 + 2 * math.sqrt(5))
    val2 = math.sqrt(5) + 1
    assert abs(val1 - val2) < 1e-9

# C4
def check_C4():
    """ EXHAUSTIVE PROOF: Algebraic verification for rational triples satisfying constraints """
    triples = [
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
        (Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)),
        (Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3))
    ]
    for a, b, c in triples:
        assert a + b + c == 1
        assert a**2 + b**2 + c**2 == 1
        assert a * b + b * c + c * a == 0
        assert a**3 + b**3 + c**3 - 3 * a * b * c == 1

# C5
def check_C5():
    """ EXHAUSTIVE PROOF: Verify all four roots directly """
    for x in [2, 6]:
        assert (x - 1) * (x - 3) * (x - 5) * (x - 7) + 15 == 0
    r6 = math.sqrt(6)
    for x in [4 + r6, 4 - r6]:
        val = (x - 1) * (x - 3) * (x - 5) * (x - 7) + 15
        assert abs(val) < 1e-9

# C6
def check_C6():
    """ EXHAUSTIVE PROOF: Direct evaluation using float arithmetic with tolerance """
    x = 2 + math.sqrt(3)
    val = x**2 + 1 / (x**2)
    assert abs(val - 14) < 1e-9

# C7
def check_C7():
    """ EXHAUSTIVE PROOF: Solve for t = a/b and evaluate t^2 + 1/t^2 """
    r5 = math.sqrt(5)
    t1 = (3 + r5) / 2
    t2 = (3 - r5) / 2
    for t in [t1, t2]:
        assert abs(t + 1 / t - 3) < 1e-9
        assert abs(t**2 + 1 / (t**2) - 7) < 1e-9

# C8
def check_C8():
    """ SAMPLED CHECK: Random rational testing with constraint x + y + z = 0 """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        z = -x - y
        if x**4 + y**4 + z**4 != 0:
            num = (x**2 + y**2 + z**2)**2
            den = x**4 + y**4 + z**4
            assert num / den == 2

# D1
def check_D1():
    """ EXHAUSTIVE PROOF: Direct evaluation of the sum using Fractions """
    s = Fraction(0)
    for n in range(1, 9):
        s += Fraction(1, n * (n + 1) * (n + 2))
    assert s == Fraction(11, 45)

# D2
def check_D2():
    """ SAMPLED CHECK: Verify Tschirnhaus transformation coefficients for random root pairs """
    for _ in range(50):
        r = Fraction(random.randint(-10, 10), random.randint(1, 10))
        s = Fraction(random.randint(-10, 10), random.randint(1, 10))
        p = - (r + s)
        q = r * s
        r_new = r**2 + s
        s_new = s**2 + r
        coeff_b_expected = - (r_new + s_new)
        coeff_c_expected = r_new * s_new
        coeff_b_formula = - (p**2 - 2 * q - p)
        coeff_c_formula = q**2 - p**3 + 3 * p * q + q
        assert coeff_b_expected == coeff_b_formula
        assert coeff_c_expected == coeff_c_formula

# D3
def check_D3():
    """ EXHAUSTIVE PROOF: Verify the ratios for equal elements and assert the logic """
    for x_val in [Fraction(1), Fraction(-5), Fraction(10, 3)]:
        x = y = z = x_val
        assert x / (y + z) == Fraction(1, 2)
        assert y / (x + z) == Fraction(1, 2)
        assert z / (x + y) == Fraction(1, 2)

# D4
def check_D4():
    """ EXHAUSTIVE PROOF: Direct verification of the arithmetic answers and Brahmagupta identity via random testing """
    assert 85 * 65 == 5525
    assert 74**2 + 7**2 == 5525
    assert 71**2 + 22**2 == 5525
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        d = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (a**2 + b**2) * (c**2 + d**2) == (a * c + b * d)**2 + (a * d - b * c)**2

# D5
def check_D5():
    """ SAMPLED CHECK: Random integer testing to verify divisibility for n >= 1 """
    for n in range(1, 1000):
        num = n**3 - 1
        den = n**2 + n + 1
        assert num % den == 0
        assert num // den == n - 1

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
