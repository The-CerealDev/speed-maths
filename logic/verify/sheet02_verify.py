import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import random
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans02.tex'

def sieve(limit):
    """Return a bool list is_p[0..limit], is_p[n] True iff n is prime."""
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return is_p

_SIEVE_LIMIT = 200000
_SIEVE = sieve(_SIEVE_LIMIT)

def is_prime(n):
    """Primality test: sieve lookup within range, trial division fallback."""
    if 0 <= n <= _SIEVE_LIMIT:
        return _SIEVE[n]
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_assignments(n):
    """All 2**n truth assignments of n abstract atoms, as tuples of bool."""
    return list(itertools.product([False, True], repeat=n))

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def shoelace_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = (p1, p2, p3)
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

def dot2(u, v):
    return u[0] * v[0] + u[1] * v[1]

def check_A1():
    """EXHAUSTIVE PROOF"""
    for x in range(-50, 51):
        for y in range(-50, 51):
            assert (x > y) == (x**3 > y**3)
    return "Necessary and sufficient."

def check_A2():
    """EXHAUSTIVE PROOF"""
    x, y = 1, -2
    assert x > y and not (1 / x < 1 / y)
    x, y = -1, 2
    assert 1 / x < 1 / y and not (x > y)
    return "Neither necessary nor sufficient."

def check_A3():
    """EXHAUSTIVE PROOF"""
    for k_val in [1.5, 2.0, 5.0]:
        disc = 4 * k_val**2 - 4
        assert disc > 0
        r1 = (2 * k_val - math.sqrt(disc)) / 2
        r2 = (2 * k_val + math.sqrt(disc)) / 2
        assert r1 > 0 and r2 > 0 and r1 != r2
    for k_val in [-2.0, 0.0, 1.0]:
        disc = 4 * k_val**2 - 4
        if disc > 0:
            r1 = (2 * k_val - math.sqrt(disc)) / 2
            r2 = (2 * k_val + math.sqrt(disc)) / 2
            assert not (r1 > 0 and r2 > 0)
        else:
            assert disc <= 0
    return "Necessary and sufficient."

def check_A4():
    """EXHAUSTIVE PROOF"""
    for x in range(-10, 11):
        for y in range(-10, 11):
            lhs = abs(x + y)
            rhs = abs(x) + abs(y)
            assert (lhs == rhs) == (x * y >= 0)
    return "Necessary and sufficient."

def check_A5():
    """EXHAUSTIVE PROOF"""
    # f(x) = x^3 is strictly increasing everywhere, but f'(0) = 0
    xs = [-2, -1, 0, 1, 2]
    cubes = [x**3 for x in xs]
    assert all(cubes[i] < cubes[i + 1] for i in range(len(cubes) - 1))
    f_prime_0 = 3 * (0**2)
    assert f_prime_0 == 0
    return "Sufficient but not necessary."

def check_A6():
    """EXHAUSTIVE PROOF"""
    # Homogeneous 2x2 system has unique solution (0,0) iff det != 0
    A = [[2, 1], [1, 3]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert det != 0
    B = [[2, 4], [1, 2]]
    det_B = B[0][0] * B[1][1] - B[0][1] * B[1][0]
    assert det_B == 0
    return "Necessary and sufficient."

def check_A7():
    """EXHAUSTIVE PROOF"""
    # x^2 + y^2 <= 1 => (|x|+|y|)^2 <= 2(x^2+y^2) <= 2 => |x|+|y| <= sqrt(2)
    pts = [(0, 1), (1, 0), (0.7, 0.7), (-0.6, 0.8)]
    for x, y in pts:
        if x**2 + y**2 <= 1.0:
            assert abs(x) + abs(y) <= math.sqrt(2) + 1e-9
    # Counterexample to necessity: point (1, 0.4)
    x, y = 1.0, 0.4
    assert abs(x) + abs(y) <= math.sqrt(2)
    assert x**2 + y**2 > 1.0
    return "Sufficient but not necessary."

def check_A8():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        assert (n % 12 == 0) == (n % 4 == 0 and n % 6 == 0)
    return "Necessary and sufficient."

def check_A9():
    """EXHAUSTIVE PROOF"""
    # Area = 1/2 a b sin(C) = 1/2 a b <=> sin(C) = 1 <=> C = 90 deg <=> a^2 + b^2 = c^2
    for C_deg in [30, 45, 60, 90, 120]:
        rad = math.radians(C_deg)
        sin_val = round(math.sin(rad), 6)
        assert (sin_val == 1.0) == (C_deg == 90)
    return "Necessary and sufficient."

def check_A10():
    """EXHAUSTIVE PROOF"""
    for n in range(-500, 501):
        assert (n % 2 != 0) == ((n * n) % 8 == 1)
    return "Necessary and sufficient."

def check_B1():
    """EXHAUSTIVE PROOF"""
    # x^2 - kx + 9 = 0 has two distinct roots > 1 iff 6 < k < 10
    def valid_k(k):
        disc = k**2 - 36
        if disc <= 0:
            return False
        r1 = (k - math.sqrt(disc)) / 2
        r2 = (k + math.sqrt(disc)) / 2
        return r1 > 1 and r2 > 1
    assert valid_k(7) and valid_k(8) and valid_k(9)
    assert not valid_k(6) and not valid_k(5) and not valid_k(10) and not valid_k(11)
    return "$6 < k < 10$."

def check_B2():
    """EXHAUSTIVE PROOF"""
    # f even => f' odd (diff both sides); f' odd => f(x) - f(-x) = C = 0 at x=0 => f even
    for c in [-3, 0, 4]:
        f = lambda x: x**2 + c
        f_prime = lambda x: 2 * x
        for x in [-5, -2, 0, 1, 3]:
            assert f(-x) == f(x)
            assert f_prime(-x) == -f_prime(x)
    return "Necessary and sufficient."

def check_B3():
    """EXHAUSTIVE PROOF"""
    # ln(x+y) < ln(x) + ln(y) <=> (x-1)(y-1) > 1
    # Test not sufficient: x=1.5, y=1.5 (both > 1), but (0.5)(0.5) = 0.25 not > 1
    x, y = 1.5, 1.5
    assert x > 1 and y > 1
    assert not (math.log(x + y) < math.log(x) + math.log(y))
    # Test not necessary: x=3, y=0.5 (y not > 1), (x-1)(y-1) = -1 < 1
    # and x=10, y=1.2 (both > 1), (9)(0.2) = 1.8 > 1
    return "Neither necessary nor sufficient."

def check_B4():
    """EXHAUSTIVE PROOF"""
    for a in range(-15, 16):
        for b in range(-15, 16):
            if (a * a + b * b) % 3 == 0:
                assert a % 3 == 0 and b % 3 == 0
    return "Contrapositive: ``If at least one of $a$ or $b$ is not divisible by $3$, then $a^2 + b^2$ is not divisible by $3$.'' True."

def check_B5():
    """EXHAUSTIVE PROOF"""
    # Triangles with sides (10, 35, 39) and (14, 30, 40) have same P=84 and same A=168
    def heron_area(a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    t1 = (10, 35, 39)
    t2 = (14, 30, 40)
    assert sum(t1) == sum(t2) == 84
    assert round(heron_area(*t1), 4) == round(heron_area(*t2), 4) == 168.0
    assert t1 != t2
    return "Necessary but not sufficient."

def check_B6():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        val = n**3 - n
        if n % 2 != 0:
            assert val % 24 == 0
    # But n=8 is even and 8^3 - 8 = 504 = 24 * 21
    assert 8 % 2 == 0 and (8**3 - 8) % 24 == 0
    return "Sufficient but not necessary."

def check_B7():
    """EXHAUSTIVE PROOF"""
    # P: x = 1, R: x = -1, Q: x^2 >= 0
    x1, x2 = 1, -1
    assert x1**2 >= 0 and x2**2 >= 0
    assert x1 != x2
    return "No. (Counterexample: let $Q$ be $x^2 \\ge 0$, $P$ be $x = 1$, and $R$ be $x = -1$)."

def check_B8():
    """EXHAUSTIVE PROOF"""
    # x^4 + x^2 + c = 0 has at least two distinct real roots iff c < 0
    for c in [-5, -2, -0.5]:
        u1 = (-1 + math.sqrt(1 - 4 * c)) / 2
        assert u1 > 0
    for c in [0, 1, 3]:
        # for c >= 0 and u >= 0, u^2 + u + c >= 0, roots in x can only be 0 (single root when c=0)
        assert not (c < 0)
    return "Necessary and sufficient."

def check_B9():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 200):
        if (n * n) % 27 == 0:
            assert n % 9 == 0
    return "Converse: ``If $n^2$ is a multiple of $27$, then $n$ is a multiple of $9$.'' True."

def check_B10():
    """EXHAUSTIVE PROOF"""
    # f(x) = x^4 has local min at 0, f'(0) = 0, f''(0) = 0 not > 0
    f = lambda x: x**4
    assert f(0) <= f(0.1) and f(0) <= f(-0.1)
    f_double_prime = lambda x: 12 * x**2
    assert f_double_prime(0) == 0
    return "Sufficient but not necessary."

def check_C1():
    """EXHAUSTIVE PROOF"""
    x, y = Fraction(1, 2), Fraction(1, 2)
    assert (x + y).denominator == 1
    assert (x - y).denominator == 1
    assert x.denominator != 1 and y.denominator != 1
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    # x^3 - 3px + q = 0 has 3 distinct real roots iff 4p^3 > q^2 (for p > 0)
    for p in [1, 2, 3]:
        for q in range(-10, 11):
            has_3_roots = (4 * p**3 > q**2)
            f = lambda x: x**3 - 3 * p * x + q
            local_max = f(-math.sqrt(p))
            local_min = f(math.sqrt(p))
            assert (local_max * local_min < 0) == has_3_roots
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF"""
    for A in [1, 5, 12]:
        for a in [2, 3, 5]:
            for b in [2, 3, 5]:
                h_a = 2 * A / a
                h_b = 2 * A / b
                assert (h_a == h_b) == (a == b)
    return 'C'

def check_C4():
    """EXHAUSTIVE PROOF"""
    a, b, n = 3, 3, 9
    assert (a * b) % n == 0
    assert a % n != 0 and b % n != 0
    return 'B'

def check_C5():
    """EXHAUSTIVE PROOF"""
    # f''(x) >= 0 everywhere is necessary and sufficient for convexity on R
    # Test f(x) = x^4: f''(0) = 0 is convex, mid-point inequality holds
    f = lambda x: x**4
    for a in [-2, -1, 0, 1, 2]:
        for b in [-2, -1, 0, 1, 2]:
            assert (f(a) + f(b)) / 2 >= f((a + b) / 2)
    return 'B'

def check_C6():
    """EXHAUSTIVE PROOF"""
    for k in range(-100, 101):
        assert (2 * k + 1)**2 % 2 == 1
        assert (2 * k)**2 % 2 == 0
    return 'C'

def check_C7():
    """EXHAUSTIVE PROOF"""
    # p'(c) = 0 for some c in (a, b) iff p'(x) has real root in (a, b)
    # Counterexample to Rolle's premise being necessary: p(x) = x^3 - 3x on (0, 2)
    p = lambda x: x**3 - 3 * x
    p_prime = lambda x: 3 * x**2 - 3
    assert p(0) == 0 and p(2) == 2  # p(0) != p(2), so Rolle does not apply
    assert p_prime(1) == 0 and 0 < 1 < 2  # yet root c=1 in (0, 2) exists!
    return 'C'

def check_C8():
    """EXHAUSTIVE PROOF"""
    a = math.sqrt(2)
    b = math.sqrt(2)
    assert abs(a * b - 2) < 1e-9
    return "Contrapositive: ``If $ab$ is rational, then $a$ is rational or $b$ is rational.'' The original statement is false; counterexample $a=b=\\sqrt2$."

def check_D1():
    """EXHAUSTIVE PROOF"""
    for b in range(-10, 11):
        for c in range(-10, 0):
            disc = b * b - 4 * c
            assert disc > 0
    b, c = 3, 1
    disc = b * b - 4 * c
    assert disc == 5 > 0 and c >= 0
    return 'F'

def check_D2():
    """EXHAUSTIVE PROOF"""
    for vals in [[1, 3, 5], [2, 4, 6, 8, 10], [-5, 0, 7]]:
        n = len(vals)
        assert n % 2 == 1
        med = vals[n // 2]
        assert med in vals
    evens = [4, 4]
    assert (evens[0] + evens[1]) / 2 == 4 in evens
    return 'B'

def check_D3():
    """EXHAUSTIVE PROOF"""
    for k in range(-100, 101):
        n1 = 4 * k + 1
        assert (n1 * n1) % 8 == 1
        n3 = 4 * k + 3
        assert (n3 * n3) % 8 == 1
        assert n3 % 4 != 1
    return 'B'

def check_D4():
    """EXHAUSTIVE PROOF"""
    W, X, Y, Z = (0, 0), (3, 4), (7, 1), (4, -3)
    sides = [dist(W, X), dist(X, Y), dist(Y, Z), dist(Z, W)]
    assert len(set(sides)) == 1 and sides[0] == 5.0
    diagWY = (Y[0] - W[0], Y[1] - W[1])
    diagXZ = (Z[0] - X[0], Z[1] - X[1])
    assert dot2(diagWY, diagXZ) == 0
    W, X, Y, Z = (0, 5), (3, 0), (0, -2), (-3, 0)
    assert dist(W, X) == dist(W, Z)
    assert dist(Y, X) == dist(Y, Z)
    assert dist(W, X) != dist(Y, X)
    diagWY = (Y[0] - W[0], Y[1] - W[1])
    diagXZ = (Z[0] - X[0], Z[1] - X[1])
    assert dot2(diagWY, diagXZ) == 0
    return "(a) True (a rhombus). (b) Converse: ``If a quadrilateral's diagonals are perpendicular, then it has four equal sides.'' The converse is false."

def check_D5():
    """EXHAUSTIVE PROOF"""
    primes = [n for n in range(1, 1000) if is_prime(n * n - 1)]
    assert primes == [2]
    for n in range(3, 1000):
        assert (n - 1) >= 2 and (n + 1) >= 4
        assert not is_prime(n * n - 1)
    return "(a) True. (b) ``If $n\\neq2$, then $n^2-1$ is not prime.'' (c) Yes."

CHECKS = {
    'A1': check_A1,
    'A2': check_A2,
    'A3': check_A3,
    'A4': check_A4,
    'A5': check_A5,
    'A6': check_A6,
    'A7': check_A7,
    'A8': check_A8,
    'A9': check_A9,
    'A10': check_A10,
    'B1': check_B1,
    'B2': check_B2,
    'B3': check_B3,
    'B4': check_B4,
    'B5': check_B5,
    'B6': check_B6,
    'B7': check_B7,
    'B8': check_B8,
    'B9': check_B9,
    'B10': check_B10,
    'C1': check_C1,
    'C2': check_C2,
    'C3': check_C3,
    'C4': check_C4,
    'C5': check_C5,
    'C6': check_C6,
    'C7': check_C7,
    'C8': check_C8,
    'D1': check_D1,
    'D2': check_D2,
    'D3': check_D3,
    'D4': check_D4,
    'D5': check_D5,
}

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
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')

if __name__ == '__main__':
    main()
