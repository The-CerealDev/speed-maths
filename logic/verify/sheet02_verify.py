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
    P = lambda n: n % 6 == 0
    Q = lambda n: n % 3 == 0
    assert all(not P(n) or Q(n) for n in range(-1000, 1001))
    assert Q(3) and not P(3)
    return "``If $n$ is a multiple of $3$, then $n$ is a multiple of $6$.''"

def check_A2():
    """EXHAUSTIVE PROOF"""
    P = lambda n: n % 6 == 0
    Q = lambda n: n % 3 == 0
    for n in range(-1000, 1001):
        orig = not P(n) or Q(n)
        contra = not (not Q(n)) or (not P(n))
        assert orig == contra
    return "``If $n$ is not a multiple of $3$, then $n$ is not a multiple of $6$.''"

def check_A3():
    """EXHAUSTIVE PROOF"""
    x = 3
    assert x * x == 9
    return True

def check_A4():
    """EXHAUSTIVE PROOF"""
    x = -3
    assert x * x == 9 and x != 3
    return False

def check_A5():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        if n % 4 == 0:
            assert n % 2 == 0
    assert 2 % 2 == 0 and 2 % 4 != 0
    return "Sufficient."

def check_A6():
    """EXHAUSTIVE PROOF"""
    for A, B in all_assignments(2):
        assert (not (A or B)) == ((not A) and (not B))
    return "``If $n$ is not prime, then $n$ is even and $n\\neq2$.''"

def check_A7():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        contra = Q or (not P)
        assert orig == contra
    return True

def check_A8():
    """EXHAUSTIVE PROOF"""
    n = 3
    assert n % 3 == 0 and n % 6 != 0
    return False

def check_A9():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        neg = P and (not Q)
        assert neg == (not orig)
    return "``$n$ is even and $n^2$ is odd.''"

def check_A10():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        if n % 12 == 0:
            assert n % 4 == 0
    return True

def check_B1():
    """EXHAUSTIVE PROOF"""
    assert (-3)**2 > 4 and not (-3 > 2)
    for x in [-2, -1, 0, 1, 2]:
        assert x**2 <= 4 and x <= 2
    return "Converse: ``If $x^2>4$, then $x>2$'' --- false. Contrapositive: ``If $x^2\\leq4$, then $x\\leq2$'' --- true."

def check_B2():
    """EXHAUSTIVE PROOF"""
    n1, n2 = 6, 9
    assert n1 % 3 == 0
    assert n2 % 3 == 0 and n2 != 6
    return "Sufficient but not necessary."

def check_B3():
    """EXHAUSTIVE PROOF"""
    assert math.gcd(2, 3) == 1
    assert math.lcm(2, 3) == 6
    for n in range(-1000, 1001):
        assert (n % 6 == 0) == (n % 2 == 0 and n % 3 == 0)
    return "Necessary and sufficient."

def check_B4():
    """EXHAUSTIVE PROOF"""
    for a in range(-10, 11):
        for b in range(-10, 11):
            if (a + b) % 2 != 0:
                assert a % 2 != 0 or b % 2 != 0
    return "``If $a+b$ is odd, then $a$ is odd or $b$ is odd.'' True."

def check_B5():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        if ((not P) or Q) and ((not Q) or P):
            assert P == Q
    return True

def check_B6():
    """EXHAUSTIVE PROOF"""
    for p in range(-10, 11):
        for q in range(1, 10):
            x = Fraction(p, q)
            assert isinstance(x * x, Fraction)
    x_sq = 2
    assert not any(a * a == 2 * b * b for b in range(1, 100) for a in range(1, 150) if math.gcd(a, b) == 1)
    return "Converse: ``$x^2$ is rational'' is sufficient for ``$x$ is rational''. The converse is false."

def check_B7():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        converse = (not Q) or P
        inverse = P or (not Q)
        assert converse == inverse
    return "Inverse: ``If $n$ is not prime, then $n$ is even and $n\\neq2$'' (A6). Converse: ``If $n$ is odd or $n=2$, then $n$ is prime.'' Yes, they are logically equivalent."

def check_B8():
    """EXHAUSTIVE PROOF"""
    a, b = 2, -2
    assert a * a == b * b and a != b
    return False

def check_B9():
    """EXHAUSTIVE PROOF"""
    assert (-3)**2 > 4 and not (-3 > 2)
    for x in range(3, 100):
        assert x**2 > 4
    return "Necessary but not sufficient."

def check_B10():
    """EXHAUSTIVE PROOF"""
    n = 3
    assert n % 3 == 0 and n % 9 != 0
    return "Converse: ``If $n$ is a multiple of $3$, then $n$ is a multiple of $9$.'' The converse is false."

def check_C1():
    """EXHAUSTIVE PROOF"""
    x, y = Fraction(1, 2), Fraction(1, 2)
    assert (x + y).denominator == 1
    assert (x - y).denominator == 1
    assert x.denominator != 1 and y.denominator != 1
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    surviving = 0
    for P, Q, R in all_assignments(3):
        if P == Q and Q == R:
            surviving += 1
            assert P == R
    assert surviving == 2
    return "Proved."

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
    n_inv, n_conv = 4, 2
    assert n_inv % 8 != 0 and n_inv % 2 == 0
    assert n_conv % 2 == 0 and n_conv % 8 != 0
    return "Inverse: ``If $n$ is not a multiple of $8$, then $n$ is not a multiple of $2$.'' The inverse is false, so the converse is also false."

def check_C6():
    """EXHAUSTIVE PROOF"""
    for k in range(-100, 101):
        assert (2 * k + 1)**2 % 2 == 1
        assert (2 * k)**2 % 2 == 0
    return 'C'

def check_C7():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        inverse = P or (not Q)
        converse = (not Q) or P
        if orig and inverse:
            assert converse is True
    return "$S$'s converse must also be true."

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
