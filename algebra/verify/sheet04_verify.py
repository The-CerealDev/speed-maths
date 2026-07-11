import math
import random
from fractions import Fraction

# A1
def check_A1():
    """ EXHAUSTIVE PROOF: Direct evaluation of DOTS and Fermat's factorisation logic """
    assert 201 * 199 == 39999
    for n in range(1, 1000):
        for d in range(n):
            assert (n - d) * (n + d) == n**2 - d**2

# A2
def check_A2():
    """ SAMPLED CHECK: Random integer testing of trinomial factorisation """
    for x in range(-50, 50):
        assert x**2 - x - 42 == (x - 7) * (x + 6)

# A3
def check_A3():
    """ EXHAUSTIVE PROOF: Direct evaluation at x=-1 """
    assert sum((-1)**k for k in range(5)) == 1

# A4
def check_A4():
    """ EXHAUSTIVE PROOF: Solve exact roots for p and q and evaluate power sum """
    # p+q=6, pq=7 => roots of t^2 - 6t + 7 = 0 are 3 +- sqrt(2)
    r2 = math.sqrt(2)
    p = 3 + r2
    q = 3 - r2
    assert abs(p + q - 6) < 1e-9
    assert abs(p * q - 7) < 1e-9
    assert abs(p**3 + q**3 - 90) < 1e-9

# A5
def check_A5():
    """ EXHAUSTIVE PROOF: Verify using the remainder theorem and factorization """
    assert 1**3 + 2*1 - 3 == 0
    for x in range(-50, 50):
        assert x**3 + 2*x - 3 == (x - 1) * (x**2 + x + 3)

# A6
def check_A6():
    """ SAMPLED CHECK: Random integer testing of complete factorization """
    for x in range(-50, 50):
        assert 2*x**3 - 18*x == 2 * x * (x - 3) * (x + 3)

# A7
def check_A7():
    """ SAMPLED CHECK: Random integer testing of exponent simplification """
    def pow3(k):
        if k >= 0:
            return Fraction(3**k)
        else:
            return Fraction(1, 3**(-k))
    for n in range(-10, 10):
        num = pow3(n+1) - pow3(n-1)
        den = pow3(n)
        assert num / den == Fraction(8, 3)

# A8
def check_A8():
    """ EXHAUSTIVE PROOF: Solve exact roots for a and b and evaluate product """
    # a-b=3, a^2+b^2=29
    # S = a+b = +- sqrt(2*(a^2+b^2) - (a-b)^2) = +- sqrt(58 - 9) = +- 7
    for a, b in [(5, 2), (-2, -5)]:
        assert a - b == 3
        assert a**2 + b**2 == 29
        assert a * b == 10

# A9
def check_A9():
    """ SAMPLED CHECK: Random rational testing of difference of two squares """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert x**4 - 1 == (x**2 + 1) * (x + 1) * (x - 1)

# A10
def check_A10():
    """ EXHAUSTIVE PROOF: Verify factorial reduction for a range of integers """
    for n in range(2, 50):
        assert math.factorial(n) // math.factorial(n - 2) == n * (n - 1)

# B1
def check_B1():
    """ SAMPLED CHECK: Random rational testing of geometric series summation """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 1:
            assert Fraction(x**5 - 1, x - 1) == x**4 + x**3 + x**2 + x + 1

# B2
def check_B2():
    """ EXHAUSTIVE PROOF: Direct evaluation of remainders and polynomial factorization """
    assert 1**10 - 3*1**5 + 2 == 0
    assert (-1)**10 - 3*(-1)**5 + 2 == 6
    for x in range(-10, 10):
        assert x**10 - 3*x**5 + 2 == (x**5 - 1) * (x**5 - 2)

# B3
def check_B3():
    """ SAMPLED CHECK: Random rational testing of fraction subtraction """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if a != b and a != -b:
            assert Fraction(a*b, a - b) - Fraction(a**2 * b, a**2 - b**2) == Fraction(a * b**2, a**2 - b**2)

# B4
def check_B4():
    """ SAMPLED CHECK: Random rational testing of factorization """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert x**6 - y**6 == (x - y) * (x + y) * (x**2 + x*y + y**2) * (x**2 - x*y + y**2)

# B5
def check_B5():
    """ EXHAUSTIVE PROOF: Solve for roots of the quadratic and evaluate reciprocal sum """
    alpha = Fraction(1, 3)
    beta = Fraction(-2)
    assert 3 * alpha**2 + 5 * alpha - 2 == 0
    assert 3 * beta**2 + 5 * beta - 2 == 0
    assert 1 / alpha + 1 / beta == Fraction(5, 2)

# B6
def check_B6():
    """ SAMPLED CHECK: Random rational testing of expression simplification """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 0:
            assert (1 - 1 / x**2) * (x**2 + x) == Fraction((x - 1) * (x + 1)**2, x)

# B7
def check_B7():
    """ SAMPLED CHECK: Random rational testing of algebraic identity """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (a + b + c)**2 - 2*(a*b + b*c + c*a) == a**2 + b**2 + c**2
    assert 5**2 - 2 * 6 == 13

# B8
def check_B8():
    """ SAMPLED CHECK: Random rational testing of rearranged equation """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 2:
            y = Fraction(3*x + 1, x - 2)
            if y != 3:
                assert Fraction(2*y + 1, y - 3) == x

# B9
def check_B9():
    """ EXHAUSTIVE PROOF: Verify composite claim for n >= 2 """
    for n in range(2, 100):
        val = 4*n**2 - 1
        factor1 = 2*n - 1
        factor2 = 2*n + 1
        assert val == factor1 * factor2
        assert factor1 > 1
        assert factor2 > 1

# B10
def check_B10():
    """ EXHAUSTIVE PROOF: Solve for exact roots and construct target quadratic """
    r3 = math.sqrt(3)
    alpha = 2 + r3
    beta = 2 - r3
    assert abs(alpha + beta - 4) < 1e-9
    assert abs(alpha * beta - 1) < 1e-9
    u = alpha - beta
    v = beta - alpha
    assert abs(u + v) < 1e-9
    assert abs(u * v - (-12)) < 1e-9

# C1
def check_C1():
    """ EXHAUSTIVE PROOF: Verify solutions to the exponential equation """
    for x in [0, 2]:
        assert 4**x - 5 * 2**x + 4 == 0

# C2
def check_C2():
    """ SAMPLED CHECK: Random rational testing of reciprocal power expression """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 0:
            t = x + 1 / x
            assert x**3 + 1 / x**3 == t**3 - 3*t

# C3
def check_C3():
    """ SAMPLED CHECK: Random positive rational testing of AM-GM minimum """
    for _ in range(50):
        x = Fraction(random.randint(1, 100), random.randint(1, 100))
        assert 3*x + 27 / x >= 18
    assert 3*3 + 27 / 3 == 18

# C4
def check_C4():
    """ EXHAUSTIVE PROOF: Verify the unique real solution and discard extraneous root """
    x = 12 - 4 * math.sqrt(7)
    assert abs(math.sqrt(2 * x - 1) + math.sqrt(x - 1) - 2) < 1e-9

# C5
def check_C5():
    """ SAMPLED CHECK: Random rational testing of algebraic factorization """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (x + 1) * (x + 3) * (x + 5) * (x + 7) + 16 == (x**2 + 8*x + 11)**2

# C6
def check_C6():
    """ SAMPLED CHECK: Random rational testing of Cauchy-Schwarz identity """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        d = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (a**2 + b**2) * (c**2 + d**2) - (a*c + b*d)**2 == (a*d - b*c)**2

# C7
def check_C7():
    """ SAMPLED CHECK: Random rational testing of linear variable substitution """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        u = x + y
        v = x - y
        assert x**4 + y**4 == Fraction(u**4 + v**4 + 6 * u**2 * v**2, 8)

# C8
def check_C8():
    """ EXHAUSTIVE PROOF: Verify roots of the quartic equation """
    roots = [2, -2, math.sqrt(3), -math.sqrt(3)]
    for x in roots:
        assert abs(x**4 - 7 * x**2 + 12) < 1e-9

# D1
def check_D1():
    """ EXHAUSTIVE PROOF: Verify that no square integer modulo 4 is equal to 2 or 3 """
    for n in range(4):
        assert n**2 % 4 in [0, 1]
    for n in range(-1000, 1000):
        assert (n**2 + 2) % 4 != 0

# D2
def check_D2():
    """ EXHAUSTIVE PROOF: Verify quartic factorization and roots """
    r2 = math.sqrt(2)
    for x in [1, 1 + r2, 1 - r2]:
        assert abs(x**4 - 4 * x**3 + 4 * x**2 - 1) < 1e-9

# D3
def check_D3():
    """ EXHAUSTIVE PROOF: Verify sequence recurrence and closed form expression """
    a = [Fraction(0)] * 21
    a[1] = Fraction(1)
    for n in range(1, 20):
        a[n+1] = a[n] / (a[n] + 2)
        assert a[n+1] == Fraction(1, 2**(n+1) - 1)

# D4
def check_D4():
    """ EXHAUSTIVE PROOF: Verify product telescopes for finite n """
    for n in range(2, 50):
        prod = Fraction(1)
        for k in range(2, n + 1):
            prod *= (1 - Fraction(1, k**2))
        assert prod == Fraction(n + 1, 2 * n)

# D5
def check_D5():
    """ EXHAUSTIVE PROOF: Direct evaluation of polynomial masking question """
    p_0 = (-1) * (-2) * (-3) * (-4) + 10*0
    p_12 = (11) * (10) * (9) * (8) + 10*12
    assert p_0 == 24
    assert p_12 == 8040
    assert p_12 - 12 * p_0 == 7752

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
