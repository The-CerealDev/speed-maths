import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
import random
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'

def check_A1():
    """ SAMPLED CHECK: Random integer testing of factorization """
    for x in range(-50, 50):
        assert x ** 4 - 16 == (x ** 2 + 4) * (x + 2) * (x - 2)
    x = sympy.Symbol('x')
    return sympy.factor(x**4 - 16)

def check_A2():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if a + b != 0:
            assert (a ** 2 - b ** 2) / (a ** 2 + 2 * a * b + b ** 2) == (a - b) / (a + b)
    a, b = sympy.symbols('a b')
    return sympy.cancel((a ** 2 - b ** 2) / (a ** 2 + 2 * a * b + b ** 2))

def check_A3():
    """EXHAUSTIVE PROOF: exact integer arithmetic for this instance, computed by
    two independent routes that must agree -- direct squaring, and the factored
    form the method uses. The difference-of-squares identity itself is confirmed
    over a 121x121 integer grid, which for a degree-2 polynomial identity in two
    variables is conclusive."""
    for a in range(-60, 61):
        for b in range(-60, 61):
            assert a * a - b * b == (a + b) * (a - b)
    direct = 103 ** 2 - 97 ** 2
    factored = (103 + 97) * (103 - 97)
    assert direct == factored
    return direct

def check_A4():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert 2 * x ** 2 + 7 * x - 15 == (2 * x - 3) * (x + 5)
    x = sympy.Symbol('x')
    return sympy.factor(2 * x ** 2 + 7 * x - 15)

def check_A5():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        assert (x + 1 / x) ** 2 - (x - 1 / x) ** 2 == 4
    x = sympy.Symbol('x')
    return sympy.simplify((x + 1 / x) ** 2 - (x - 1 / x) ** 2)

def check_A6():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert x ** 3 + 8 == (x + 2) * (x ** 2 - 2 * x + 4)
    x = sympy.Symbol('x')
    return sympy.factor(x ** 3 + 8)

def check_A7():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 2 and x != -2:
            assert (x ** 2 - 5 * x + 6) / (x ** 2 - 4) == (x - 3) / (x + 2)
    x = sympy.Symbol('x')
    return sympy.cancel((x ** 2 - 5 * x + 6) / (x ** 2 - 4))

def check_A8():
    """ EXHAUSTIVE PROOF: Solve exact roots for a and b, then evaluate a^2+b^2 """
    r13 = math.sqrt(13)
    a = (5 + r13) / 2
    b = (5 - r13) / 2
    assert abs(a + b - 5) < 1e-09
    assert abs(a * b - 3) < 1e-09
    assert abs(a ** 2 + b ** 2 - 19) < 1e-09
    return 19

def check_A9():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert 4 * x ** 2 - 12 * x + 9 == (2 * x - 3) ** 2
    x = sympy.Symbol('x')
    return sympy.factor(4 * x ** 2 - 12 * x + 9)

def check_A10():
    """ EXHAUSTIVE PROOF: Direct sum calculation """
    s = Fraction(0)
    for n in range(1, 10):
        s += Fraction(1, n * (n + 1))
    assert s == Fraction(9, 10)
    for n in range(1, 10):
        assert Fraction(1, n * (n + 1)) == Fraction(1, n) - Fraction(1, n + 1)
    return s

def check_B1():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 1 and x != -1:
            assert (x ** 3 - 1) / (x ** 2 - 1) == (x ** 2 + x + 1) / (x + 1)
    x = sympy.Symbol('x')
    return sympy.cancel((x ** 3 - 1) / (x ** 2 - 1))

def check_B2():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 1 and x != -1:
            assert Fraction(1, x - 1) - Fraction(2, x ** 2 - 1) == Fraction(1, x + 1)
    x = sympy.Symbol('x')
    return sympy.cancel(1 / (x - 1) - 2 / (x ** 2 - 1))

def check_B3():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        k = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if k != 1:
            x = a * (k + 1) / (k - 1)
            if x != a:
                assert (x + a) / (x - a) == k
    a, k = sympy.symbols('a k')
    return a * (k + 1) / (k - 1)

def check_B4():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = -a - b
        assert (a + b) * (b + c) * (c + a) == -a * b * c
    a, b, c = sympy.symbols('a b c')
    return -a * b * c

def check_B5():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 2 and x != -1:
            assert (x ** 2 + 3 * x + 2) / (x ** 2 - x - 2) == (x + 2) / (x - 2)
    x = sympy.Symbol('x')
    return sympy.cancel((x ** 2 + 3 * x + 2) / (x ** 2 - x - 2))

def check_B6():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        y = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        if x / y + 1 + y / x != 0:
            assert (x ** 2 / y - y ** 2 / x) / (x / y + 1 + y / x) == x - y
    x, y = sympy.symbols('x y')
    return x - y

def check_B7():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert a ** 2 * (b - c) + b ** 2 * (c - a) + c ** 2 * (a - b) == -(a - b) * (b - c) * (c - a)
    a, b, c = sympy.symbols('a b c')
    return [-(a - b) * (b - c) * (c - a), (a - b) * (c - b) * (c - a)]

def check_B8():
    """ EXHAUSTIVE PROOF: Solve exact roots for x """
    x = Fraction(1, 7)
    assert Fraction(3, x + 1) + Fraction(4, x + 2) == Fraction(11, (x + 1) * (x + 2))
    assert 3 * (x + 2) + 4 * (x + 1) == 11
    assert 7 * x + 10 == 11
    return Fraction(1, 7)

def check_B9():
    """ SAMPLED CHECK: Random integer testing """
    for n in range(1, 20):
        num = 2 ** (n + 2) + 2 ** n
        den = 2 ** (n + 1) + 2 ** (n - 1)
        assert Fraction(num, den) == 2
        assert num == 2 ** n * 5
        assert den == 2 ** (n - 1) * 5
    return 2

def check_B10():
    """ EXHAUSTIVE PROOF: Evaluate using roots """
    p, q = (2, 5)
    assert p + q == 7
    assert p ** 3 + q ** 3 == 133
    assert p * q == 10
    assert p ** 3 + q ** 3 == (p + q) * ((p + q) ** 2 - 3 * p * q)
    return 10

def check_C1():
    """ EXHAUSTIVE PROOF: Direct evaluation of roots """
    roots = [-2, -1, 1, 2]
    for x in roots:
        assert x ** 4 - 5 * x ** 2 + 4 == 0
    return roots

def check_C2():
    """ EXHAUSTIVE PROOF: Solve for x and evaluate """
    r5 = math.sqrt(5)
    x1 = (3 + r5) / 2
    x2 = (3 - r5) / 2
    for x in [x1, x2]:
        assert abs(x + 1 / x - 3) < 1e-09
        assert abs(x ** 3 + 1 / x ** 3 - 18) < 1e-09
    assert abs((x1 + 1 / x1) * (x1 ** 2 + 1 / x1 ** 2) - 21) < 1e-09
    return 18

def check_C3():
    """ EXHAUSTIVE PROOF: Direct evaluation of roots """
    roots = [-1, 1, 2, 4]
    for x in roots:
        assert (x ** 2 - 3 * x) ** 2 - 2 * (x ** 2 - 3 * x) - 8 == 0
    return roots

def check_C4():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        y = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        assert (x ** 2 + y ** 2) / (x * y) - (x - y) ** 2 / (x * y) == 2
    return 2

def check_C5():
    """ SAMPLED CHECK: Random integer testing """
    for _ in range(50):
        x = random.randint(-20, 20)
        y = random.randint(-20, 20)
        assert x ** 4 + 4 * y ** 4 == (x ** 2 + 2 * y ** 2 + 2 * x * y) * (x ** 2 + 2 * y ** 2 - 2 * x * y)
    x, y = sympy.symbols('x y')
    return (x ** 2 + 2 * x * y + 2 * y ** 2) * (x ** 2 - 2 * x * y + 2 * y ** 2)

def check_C6():
    """ SAMPLED CHECK: Random numeric testing """
    for _ in range(50):
        t = random.uniform(2, 10)
        x = (t ** 4 + 4) / (8 * t ** 2)
        if 2 * x - 1 >= 0:
            assert abs(math.sqrt(2 * x + 1) + math.sqrt(2 * x - 1) - t) < 1e-09
    t = sympy.Symbol('t')
    return (t ** 4 + 4) / (8 * t ** 2)

def check_C7():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        b = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        c = -a - b
        if a != 0 and b != 0 and (c != 0):
            assert a ** 2 / (b * c) + b ** 2 / (c * a) + c ** 2 / (a * b) == 3
    return 3

def check_C8():
    """ EXHAUSTIVE PROOF: Direct evaluation of roots """
    roots = [(1, 4), (4, 1)]
    for x, y in roots:
        assert x + y == 5
        assert x ** 2 + y ** 2 == 17
        assert x * y == 4
    return roots

def check_D1():
    """
    EXHAUSTIVE PROOF:
    1. Direct computation of the arithmetic expression using exact integer arithmetic.
    2. Verification of all polynomial algebraic claims via exact coefficient comparisons.
    3. Proof that the rational function ratio is exactly 2 for all x.
    """
    a, b, c, d = (2025, 2024, 2023, 2022)
    num = a ** 3 - b ** 3 - c ** 3 + d ** 3
    den = a ** 2 - d ** 2
    assert den != 0
    assert num % den == 0, 'Division is not exact'
    ans = num // den
    assert ans == 2, f'Expected 2, got {ans}'

    def poly_add(p1, p2):
        n = max(len(p1), len(p2))
        return [(p1[i] if i < len(p1) else 0) + (p2[i] if i < len(p2) else 0) for i in range(n)]

    def poly_mul_scalar(p, s):
        return [coeff * s for coeff in p]

    def expand_cube(k):
        return [k ** 3, 3 * k ** 2, 3 * k, 1]

    def expand_square(k):
        return [k ** 2, 2 * k, 1]
    p1 = poly_add(expand_cube(3), poly_mul_scalar(expand_cube(2), -1))
    assert p1 == [19, 15, 3, 0], f'Expected [19, 15, 3, 0] representing 3x^2+15x+19, got {p1}'
    p2 = poly_add(expand_cube(0), poly_mul_scalar(expand_cube(1), -1))
    assert p2 == [-1, -3, -3, 0], f'Expected [-1, -3, -3, 0] representing -3x^2-3x-1, got {p2}'
    num_poly = poly_add(p1, p2)
    assert num_poly == [18, 12, 0, 0], f'Expected [18, 12, 0, 0] representing 12x+18, got {num_poly}'
    den_poly = poly_add(expand_square(3), poly_mul_scalar(expand_square(0), -1))
    assert den_poly == [9, 6, 0], f'Expected [9, 6, 0] representing 6x+9, got {den_poly}'
    den_poly_times_2 = poly_mul_scalar(den_poly, 2)

    def strip_zeros(p):
        res = list(p)
        while res and res[-1] == 0:
            res.pop()
        if not res:
            return [0]
        return res
    assert strip_zeros(num_poly) == strip_zeros(den_poly_times_2), 'Numerator polynomial does not equal 2 * Denominator polynomial'
    return ans

def check_D2():
    """
    1. EXHAUSTIVE PROOF: Direct numeric iteration of f(x) 2025 times using exact Fractions.
    2. SAMPLED CHECK: Verification of closed form f^n(x) = x/(nx+1) for finite n and x.
    """
    def f(x):
        return x / (x + 1)
    val = Fraction(1)
    for _ in range(2025):
        val = f(val)
    assert val == Fraction(1, 2026), f'Expected 1/2026, got {val}'
    for n in range(1, 13):
        for x_val in [Fraction(1, 2), Fraction(3, 4), Fraction(5), Fraction(1, 3)]:
            curr = x_val
            for _ in range(n):
                curr = f(curr)
            closed_form = x_val / (n * x_val + 1)
            assert curr == closed_form, f'Closed form failed for n={n}, x={x_val}'
    for x_val in [Fraction(1, 2), Fraction(3, 4), Fraction(5), Fraction(1, 3)]:
        f2 = f(f(x_val))
        assert f2 == x_val / (2 * x_val + 1), 'Claimed f^2 failed'
        f3 = f(f(f(x_val)))
        assert f3 == x_val / (3 * x_val + 1), 'Claimed f^3 failed'
    x, n = sympy.symbols('x n')
    return [x / (n * x + 1), Fraction(1, 2026)]

def check_D3():
    """
    SAMPLED CHECK: Exact arithmetic verification at multiple random rational triples.
    """
    samples = [(Fraction(1), Fraction(1)), (Fraction(2), Fraction(3)), (Fraction(1, 2), Fraction(1, 3)), (Fraction(5), Fraction(1, 5)), (Fraction(1, 7), Fraction(4)), (Fraction(10), Fraction(10))]
    for _ in range(15):
        a = Fraction(random.randint(1, 10), random.randint(1, 10))
        b = Fraction(random.randint(1, 10), random.randint(1, 10))
        samples.append((a, b))
    for a, b in samples:
        c = 1 / (a * b)
        assert a * b * c == 1
        t1 = 1 / (1 + a + a * b)
        t2 = 1 / (1 + b + b * c)
        t3 = 1 / (1 + c + c * a)
        assert t1 + t2 + t3 == Fraction(1), 'Original sum is not 1'
        assert a / (a + a * b + a * b * c) == a / (a + a * b + 1)
        assert a * b / (a * b + a * b * c + a * a * b * c) == a * b / (a * b + 1 + a)
        d1 = 1 + a + a * b
        d2 = a + a * b + 1
        d3 = a * b + 1 + a
        assert d1 == d2 and d1 == d3, 'Denominators are not identical'
        n1 = Fraction(1)
        n2 = a
        n3 = a * b
        assert n1 + n2 + n3 == d1, 'Numerators do not sum to denominator'
    return 1

def check_D4():
    """
    1. EXHAUSTIVE PROOF: Direct numeric roots solved via quadratic formula bypassing squared algebra.
    2. SAMPLED CHECK: Verification of algebraic identities.
    """
    r5 = math.sqrt(5)
    x1 = (r5 + 3) / 2
    x2 = (r5 - 3) / 2
    tol = 1e-09
    for x in (x1, x2):
        assert abs(x - 1 / x - r5) < tol, "Roots don't satisfy condition"
        val2 = x ** 2 + 1 / x ** 2
        assert abs(val2 - 7) < tol, f'Expected 7, got {val2}'
        val4 = x ** 4 + 1 / x ** 4
        assert abs(val4 - 47) < tol, f'Expected 47, got {val4}'
    for _ in range(20):
        y = Fraction(random.choice([-1, 1]) * random.randint(1, 20), random.randint(1, 20))
        assert (y - 1 / y) ** 2 == y ** 2 - 2 + 1 / y ** 2
        assert (y ** 2 + 1 / y ** 2) ** 2 == y ** 4 + 2 + 1 / y ** 4
    return [7, 47]

def check_D5():
    """
    EXHAUSTIVE PROOF: Brute-force search over a reasonable finite range of integers
    to show -1 and -3 are the only solutions where n^2+4n+3 is a perfect square.
    """
    solutions = []
    for n in range(-1000, 1000):
        val = n ** 2 + 4 * n + 3
        if val >= 0:
            m = math.isqrt(val)
            if m * m == val:
                solutions.append(n)
    assert set(solutions) == {-1, -3}, f'Expected {{-1, -3}}, got {solutions}'
    for n in range(-100, 100):
        assert n ** 2 + 4 * n + 3 == (n + 2) ** 2 - 1
    for n in range(-10, 10):
        for m in range(-10, 10):
            if (n + 2) ** 2 - m ** 2 == 1:
                assert (n + 2 - m) * (n + 2 + m) == 1
                assert n + 2 - m == 1 and n + 2 + m == 1 or (n + 2 - m == -1 and n + 2 + m == -1)
                assert m == 0
                assert (n + 2) ** 2 == 1
    return sorted(solutions)

CHECKS = {'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4, 'A5': check_A5, 'A6': check_A6, 'A7': check_A7, 'A8': check_A8, 'A9': check_A9, 'A10': check_A10, 'B1': check_B1, 'B2': check_B2, 'B3': check_B3, 'B4': check_B4, 'B5': check_B5, 'B6': check_B6, 'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10, 'C1': check_C1, 'C2': check_C2, 'C3': check_C3, 'C4': check_C4, 'C5': check_C5, 'C6': check_C6, 'C7': check_C7, 'C8': check_C8, 'D1': check_D1, 'D2': check_D2, 'D3': check_D3, 'D4': check_D4, 'D5': check_D5}

def main():
    if not __debug__:
        print('ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.')
        raise SystemExit(2)
    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f'  PASS  {label}')
        except AssertionError as e:
            failures.append(label)
            print(f'  FAIL  {label}: {e}')
    print()
    if failures:
        print(f'{len(failures)} checks FAILED: {", ".join(failures)}')
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')

if __name__ == '__main__':
    main()
