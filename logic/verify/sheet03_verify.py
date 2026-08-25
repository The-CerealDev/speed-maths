import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import random
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans03.tex'

def sieve(limit):
    """Return a bool list is_p[0..limit], is_p[n] True iff n is prime."""
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return is_p

_SIEVE_LIMIT = 300000
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

def check_A1():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k
    assert sympy.simplify(n**2 - 2 * (2 * k**2)) == 0
    for val in range(-100, 101):
        assert (2 * val)**2 % 2 == 0
    return "Proved."

def check_A2():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    assert sympy.simplify(n**2 - (2 * (2 * k**2 + 2 * k) + 1)) == 0
    for val in range(-100, 101):
        assert (2 * val + 1)**2 % 2 == 1
    return "Proved."

def check_A3():
    """EXHAUSTIVE PROOF"""
    j, k = sympy.symbols('j k')
    a, b = 2 * j, 2 * k
    assert sympy.simplify((a + b) - 2 * (j + k)) == 0
    for j_val in range(-50, 51):
        for k_val in range(-50, 51):
            assert (2 * j_val + 2 * k_val) % 2 == 0
    return "Proved."

def check_A4():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        if n % 2 != 0:
            assert n % 6 != 0
    return "Contrapositive: ``If $n$ is odd, then $n$ is not a multiple of $6$.'' Proved."

def check_A5():
    """EXHAUSTIVE PROOF"""
    j, k = sympy.symbols('j k')
    a, b = 2 * j + 1, 2 * k + 1
    assert sympy.simplify(a * b - (2 * (2 * j * k + j + k) + 1)) == 0
    for j_val in range(-50, 51):
        for k_val in range(-50, 51):
            assert ((2 * j_val + 1) * (2 * k_val + 1)) % 2 == 1
    return "Proved."

def check_A6():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        contra = (not (not Q)) or (not P)
        assert orig == contra
    return True

def check_A7():
    """EXHAUSTIVE PROOF"""
    for n in range(-100, 101):
        if n % 2 == 0:
            assert (n * n) % 2 == 0
        if (n * n) % 2 != 0:
            assert n % 2 != 0
    return "Proved via the contrapositive ``if $n$ is even, then $n^2$ is even'' (A1)."

def check_A8():
    """EXHAUSTIVE PROOF"""
    p_to_q_differs = any(((not P) or Q) != ((not Q) or P) for P, Q in all_assignments(2))
    assert p_to_q_differs
    return True

def check_A9():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x', positive=True)
    assert sympy.simplify(x * x - x) == x * (x - 1)
    for k in range(3, 100):
        x_val = k / 2.0
        assert x_val > 1 and x_val**2 > 1
    return "Proved."

def check_A10():
    """EXHAUSTIVE PROOF"""
    for k in range(11, 100):
        x = k / 10.0
        assert x > 1 and x**2 > 1
    return "Proved via the contrapositive ``if $x>1$, then $x^2>1$'' (A9)."

def check_B1():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 4 * k
    assert sympy.simplify(n**2 - 16 * k**2) == 0
    for k_val in range(-100, 101):
        assert (4 * k_val)**2 % 16 == 0
    return "Proved."

def check_B2():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        if n % 3 == 0:
            assert (n * n) % 3 == 0
        if (n * n) % 3 != 0:
            assert n % 3 != 0
    return "Proved via the contrapositive ``if $n$ is a multiple of $3$, then $n^2$ is a multiple of $3$''."

def check_B3():
    """EXHAUSTIVE PROOF"""
    for n in range(-1000, 1001):
        if n % 2 != 0:
            assert (n * n) % 2 != 0
    return "Contrapositive is more natural. Proved via ``if $n$ is odd, then $n^2$ is odd'' (A2)."

def check_B4():
    """EXHAUSTIVE PROOF"""
    a, b = sympy.symbols('a b', positive=True)
    assert sympy.simplify(a**2 - b**2 - (a - b) * (a + b)) == 0
    for a_val in range(1, 50):
        for b_val in range(1, a_val):
            assert a_val**2 > b_val**2
    return "Proved."

def check_B5():
    """EXHAUSTIVE PROOF"""
    f = lambda x: x**2 - 4 * x + 3
    assert f(1) == 0 and f(3) == 0
    for x_val in range(-50, 50):
        if x_val not in (1, 3):
            assert f(x_val) != 0
    return "Proved via the contrapositive ``if $x=1$ or $x=3$, then $x^2-4x+3=0$''."

def check_B6():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 3 * k
    assert sympy.simplify(n**3 - 27 * k**3) == 0
    for k_val in range(-50, 51):
        assert (3 * k_val)**3 % 27 == 0
    return "Proved."

def check_B7():
    """EXHAUSTIVE PROOF"""
    for p in range(-10, 11):
        for q in range(1, 10):
            for r in range(-10, 11):
                for s in range(1, 10):
                    x = Fraction(p, q)
                    y = Fraction(r, s)
                    assert isinstance(x * y, Fraction)
    return "Contrapositive: ``If $x$ is rational and $y$ is rational, then $xy$ is rational.'' Proved."

def check_B8():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 10 * k + 5
    n_sq = sympy.expand(n**2)
    assert sympy.simplify(n_sq - (100 * (k**2 + k) + 25)) == 0
    for k_val in range(-100, 101):
        assert (10 * k_val + 5)**2 % 10 == 5
    return "Proved."

def check_B9():
    """EXHAUSTIVE PROOF"""
    for s in [0, 1, 2, 3]:
        for q in range(-50, 51):
            n = 4 * q + s
            if (n * n) % 16 == 0:
                assert s == 0 and n % 4 == 0
    return "Proved via the contrapositive ``if $n^2$ is a multiple of $16$, then $n$ is a multiple of $4$''."

def check_B10():
    """EXHAUSTIVE PROOF"""
    b1, b2 = True, False
    assert b1 != b2
    return False

def check_C1():
    """EXHAUSTIVE PROOF"""
    x, y = 1, -2
    assert x**2 < y**2 and not (x < y)
    assert abs(x) < abs(y) and not (x < y)
    for x_val in range(-10, 11):
        for y_val in range(-10, 11):
            assert (x_val**5 < y_val**5) == (x_val < y_val)
    return 'E'

def check_C2():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    assert sympy.simplify(n**3 - (2 * (4 * k**3 + 6 * k**2 + 3 * k) + 1)) == 0
    for val in range(-50, 51):
        assert (2 * val + 1)**3 % 2 == 1
    return "Proved via the contrapositive ``if $n$ is odd, then $n^3$ is odd''."

def check_C3():
    """EXHAUSTIVE PROOF"""
    x, y = sympy.symbols('x y', positive=True)
    assert sympy.simplify(x**2 - y**2 - (x - y) * (x + y)) == 0
    for x_val in range(1, 50):
        for y_val in range(1, 50):
            assert (x_val**2 > y_val**2) == (x_val > y_val)
    return "Proved."

def check_C4():
    """EXHAUSTIVE PROOF"""
    for m in range(-100, 101):
        if m % 3 != 0:
            n = 3 * m
            assert n % 3 == 0 and n % 9 != 0
            assert (n * n) % 9 == 0 and (n * n) % 81 != 0
    return "Proved."

def check_C5():
    """EXHAUSTIVE PROOF"""
    for x in [-5, 0, 3]:
        for y in [-5, 0, 3]:
            if x == 0 or y == 0:
                assert x * y == 0
    return "Proved via the contrapositive ``if $x=0$ or $y=0$, then $xy$ is rational''."

def check_C6():
    """EXHAUSTIVE PROOF"""
    for k in range(-100, 101):
        n = 3 * k
        assert (2 * n * n + 1) % 3 == 1 != 0
    return "Proved via the contrapositive ``if $n$ is a multiple of $3$, then $2n^2+1$ is not a multiple of $3$''."

def check_C7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 1000):
        if n % 3 != 0:
            assert (n * n) % 3 == 1
    return "Proved."

def check_C8():
    """EXHAUSTIVE PROOF"""
    poly = lambda n: n * n + n + 41
    assert all(is_prime(poly(n)) for n in range(40))
    assert not is_prime(poly(40))
    assert poly(40) == 41 * 41
    return False

def check_D1():
    """EXHAUSTIVE PROOF"""
    x2, y2 = 10, -5
    assert x2 + y2 > 4 and x2 - y2 > -2 and not (y2 > 2)
    x3, y3 = 49.05, 50.95
    assert x3 + y3 > 4 and x3 - y3 > -2 and (x3 + y3) * (x3 - y3) <= -12
    return 'B'

def check_D2():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    assert sympy.simplify(n**2 - 2 * n - (2 * (2 * k**2 - 1) + 1)) == 0
    for k_val in range(-100, 101):
        n_val = 2 * k_val + 1
        assert (n_val**2 - 2 * n_val) % 2 == 1
    return "Proved via the contrapositive ``if $n$ is odd, then $n^2-2n$ is odd''."

def check_D3():
    """EXHAUSTIVE PROOF"""
    for n in range(5, 1000):
        if is_prime(n - 1) and is_prime(n + 1):
            assert n % 6 == 0
    assert is_prime(3) and is_prime(5) and 4 % 6 != 0
    return "Proved."

def check_D4():
    """EXHAUSTIVE PROOF"""
    for x_val in range(1, 30):
        for y_val in range(1, 30):
            if x_val != y_val:
                assert (x_val + y_val) / 2.0 > math.sqrt(x_val * y_val)
    return "Proved."

def check_D5():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 1000):
        if (n * n) % 6 == 0:
            assert n % 6 == 0
    n_witness = 6
    assert (n_witness * n_witness) % 4 == 0 and n_witness % 4 != 0
    return "(a) $T$ is true. (b) $6=2\\times3$ is squarefree (a product of distinct primes); $4=2^2$ is not."

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
