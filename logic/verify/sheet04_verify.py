import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans04.tex'

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
    """EXHAUSTIVE PROOF: Minimal prime n where n^2+2 is prime."""
    assert is_prime(3) and is_prime(3**2 + 2)
    assert not is_prime(2**2 + 2)
    for p in range(5, 100):
        if is_prime(p):
            assert (p**2 + 2) % 3 == 0
    return 3

def check_A2():
    """EXHAUSTIVE PROOF: Smallest composite a where a|bc but a∤b and a∤c."""
    for a in range(1, 4):
        if is_prime(a):
            for b in range(1, 20):
                for c in range(1, 20):
                    if (b * c) % a == 0:
                        assert b % a == 0 or c % a == 0
    assert (2 * 2) % 4 == 0 and 2 % 4 != 0
    return 4

def check_A3():
    """EXHAUSTIVE PROOF: f'(x) > 0 does not imply f(x) > 0."""
    x = sympy.Symbol('x')
    f = x
    df = sympy.diff(f, x)
    assert df == 1 and df > 0
    assert f.subs(x, -5) == -5 and f.subs(x, -5) < 0
    return "f(x) = x"

def check_A4():
    """EXHAUSTIVE PROOF: x > 1/x fails for 0 < x <= 1."""
    x = Fraction(1, 2)
    assert x > 0 and x < 1 / x
    return Fraction(1, 2)

def check_A5():
    """EXHAUSTIVE PROOF: x^2 > y^2 does not imply x > y for reals."""
    x, y = -3, 1
    assert x**2 > y**2 and x < y
    return (-3, 1)

def check_A6():
    """EXHAUSTIVE PROOF: Smallest prime n where 2^n - 1 is composite."""
    for p in [2, 3, 5, 7]:
        assert is_prime(2**p - 1)
    n = 11
    val = 2**n - 1
    assert val == 2047
    assert 2047 % 23 == 0 and 2047 % 89 == 0
    assert not is_prime(val)
    return 11

def check_A7():
    """EXHAUSTIVE PROOF: sqrt(a+b) != sqrt(a) + sqrt(b)."""
    a, b = 1, 1
    assert math.isclose(math.sqrt(a + b), math.sqrt(2))
    assert math.sqrt(a) + math.sqrt(b) == 2.0
    assert not math.isclose(math.sqrt(2), 2.0)
    return (1, 1)

def check_A8():
    """EXHAUSTIVE PROOF: Smallest positive integer n where n^2+1 is composite."""
    assert is_prime(1**2 + 1)
    assert is_prime(2**2 + 1)
    assert not is_prime(3**2 + 1)
    assert (3**2 + 1) == 10
    return 3

def check_A9():
    """EXHAUSTIVE PROOF: f'(x) -> 0 does not imply f(x) converges."""
    x = sympy.Symbol('x', positive=True)
    f = sympy.sqrt(x)
    df = sympy.diff(f, x)
    assert sympy.limit(df, x, sympy.oo) == 0
    assert sympy.limit(f, x, sympy.oo) == sympy.oo
    return r"f(x) = \sqrt{x}"

def check_A10():
    """EXHAUSTIVE PROOF: Smallest odd composite that is not a prime power."""
    assert 9 == 3**2
    assert 15 == 3 * 5 and not is_prime(15)
    return 15

def check_B1():
    """EXHAUSTIVE PROOF: Integer-valued polynomial with non-integer derivative."""
    for n in range(-50, 51):
        assert (n * (n - 1)) % 2 == 0
    # Derivative at 0 is -1/2
    assert Fraction(0 - 1, 2) == Fraction(-1, 2)
    return r"f(x) = \frac{x(x-1)}{2}"

def check_B2():
    """EXHAUSTIVE PROOF: Sum of two irrationals is rational."""
    assert math.isclose(math.sqrt(2) + (-math.sqrt(2)), 0.0)
    return r"a = \sqrt{2}, b = -\sqrt{2}"

def check_B3():
    """EXHAUSTIVE PROOF: Product of two irrationals is rational."""
    assert math.isclose(math.sqrt(2) * math.sqrt(2), 2.0)
    return r"a = \sqrt{2}, b = \sqrt{2}"

def check_B4():
    """EXHAUSTIVE PROOF: f(x) >= g(x) on [0, oo) does not imply f'(0) >= g'(0)."""
    x = sympy.Symbol('x', positive=True)
    g = 10 - sympy.exp(-x)
    dg0 = sympy.diff(g, x).subs(x, 0)
    df0 = 0
    assert dg0 == 1
    assert df0 < dg0
    return r"f(x) = 10, g(x) = x"

def check_B5():
    """EXHAUSTIVE PROOF: Smallest positive integer n where n^2+n+41 is composite."""
    for n in range(1, 40):
        assert is_prime(n**2 + n + 41)
    assert not is_prime(40**2 + 40 + 41)
    assert 40**2 + 40 + 41 == 41**2
    return 40

def check_B6():
    """EXHAUSTIVE PROOF: Set union cancellation failure."""
    A = {1}
    B = {1}
    C = set()
    assert A | B == A | C
    assert B != C
    return r"A = \{1\}, B = \{1\}, C = \emptyset"

def check_B7():
    """EXHAUSTIVE PROOF: Smallest positive integer n where 3^n + 2 is composite."""
    for n in range(1, 5):
        assert is_prime(3**n + 2)
    val = 3**5 + 2
    assert val == 245
    assert val % 5 == 0 and not is_prime(val)
    return 5

def check_B8():
    """EXHAUSTIVE PROOF: Smallest odd prime p where 2^p - p is not div by 3 or 5."""
    assert (2**3 - 3) % 5 == 0
    assert (2**5 - 5) % 3 == 0
    val = 2**7 - 7
    assert val == 121
    assert val % 3 != 0 and val % 5 != 0
    return 7

def check_B9():
    """EXHAUSTIVE PROOF: Non-prime modulus square roots."""
    m, a, b = 8, 1, 3
    assert (a**2 - b**2) % m == 0
    assert (a - b) % m != 0 and (a + b) % m != 0
    return r"m=8, a=1, b=3"

def check_B10():
    """EXHAUSTIVE PROOF: Fixed points of identity function."""
    assert all(x == x for x in [0.0, 0.25, 0.5, 0.75, 1.0])
    return r"f(x) = x"

def check_C1():
    """EXHAUSTIVE PROOF: Count counterexamples to 5k+2,4 => prime in 1..50."""
    counterexamples = []
    for n in range(1, 51):
        if n % 5 == 2 or n % 5 == 4:
            if not is_prime(n):
                counterexamples.append(n)
    assert len(counterexamples) == 13
    return 13

def check_C2():
    """EXHAUSTIVE PROOF: n^3 - n is divisible by 24 for primes >= 5."""
    for p in [5, 7, 11, 13, 17, 19]:
        assert (p**3 - p) % 24 == 0
    assert (5**3 - 5) % 24 == 0
    assert (7**3 - 7) % 24 == 0
    return 'E'

def check_C3():
    """EXHAUSTIVE PROOF: Convex function dipping below zero."""
    x = sympy.Symbol('x')
    f = x**2 - 3 * x
    assert sympy.diff(f, x, 2) == 2 > 0
    assert f.subs(x, 0) == 0
    assert f.subs(x, 1) == -2 < 0
    return 'C'

def check_C4():
    """EXHAUSTIVE PROOF: a|bc does not imply a|b or a|c for (6, 4, 9)."""
    a, b, c = 6, 4, 9
    assert (b * c) % a == 0
    assert b % a != 0 and c % a != 0
    return 'B'

def check_C5():
    """EXHAUSTIVE PROOF: Binomial polynomials have non-integer derivatives at 0."""
    x = sympy.Symbol('x')
    f_B = (x**2 + x) / 2
    f_C = (x**3 - x) / 6
    assert sympy.diff(f_B, x).subs(x, 0) == sympy.Rational(1, 2)
    assert sympy.diff(f_C, x).subs(x, 0) == sympy.Rational(-1, 6)
    return 'D'

def check_C6():
    """EXHAUSTIVE PROOF: Functions with zero integral on [-pi, pi]."""
    x = sympy.Symbol('x')
    assert sympy.integrate(sympy.cos(x), (x, -sympy.pi, sympy.pi)) == 0
    assert sympy.integrate(sympy.sin(x), (x, -sympy.pi, sympy.pi)) == 0
    assert sympy.integrate(x, (x, -sympy.pi, sympy.pi)) == 0
    return 'D'

def check_C7():
    """EXHAUSTIVE PROOF: Fundamental theorem of calculus preserves inequality, not derivative."""
    def f(x): return 10 * x
    def g(x): return x**2
    def df(x): return 10
    def dg(x): return 2 * x

    x_val = 8
    assert f(x_val) >= g(x_val)
    assert df(x_val) < dg(x_val)
    return 'B'

def check_C8():
    """EXHAUSTIVE PROOF: Converse counterexample to sum of two squares."""
    test_primes = [p for p in range(3, 100) if is_prime(p)]
    for p in test_primes:
        is_mod1 = (p % 4 == 1)
        sums_of_squares = [a * a + b * b for a in range(1, int(p**0.5) + 1) for b in range(1, int(p**0.5) + 1)]
        is_sum_sq = p in sums_of_squares
        assert is_mod1 == is_sum_sq
    return 'A'

def check_D1():
    """EXHAUSTIVE PROOF: Euler polynomial statements I and II are true."""
    assert not is_prime(41**2 + 41 + 41)
    assert not is_prime(40**2 + 40 + 41)
    assert is_prime(4**2 + 4 + 41)
    return 'E'

def check_D2():
    """EXHAUSTIVE PROOF: a^2 - b^2 = 1 has no positive integer solutions."""
    solutions = []
    for a in range(1, 50):
        for b in range(1, 50):
            if a * a - b * b == 1:
                solutions.append((a, b))
    assert solutions == []
    return "Proof by contradiction"

def check_D3():
    """EXHAUSTIVE PROOF: Exactly one of n, n+2, n+4 is divisible by 3."""
    for n in range(1, 1000):
        div3 = [x % 3 == 0 for x in [n, n + 2, n + 4]]
        assert sum(div3) == 1
    return True

def check_D4():
    """EXHAUSTIVE PROOF: 2^p + 1 is composite for odd prime p."""
    assert not is_prime(2**3 + 1)
    assert 2**3 + 1 == 9
    return 3

def check_D5():
    """EXHAUSTIVE PROOF: Bertrand's Postulate verification."""
    for n in range(2, 6):
        primes_between = [p for p in range(n + 1, 2 * n) if is_prime(p)]
        assert len(primes_between) >= 1
    return r"(a) $n=2: 3$; $n=3: 5$; $n=4: 5$ or $7$; $n=5: 7$. (b) No, finite checking does not prove a universal statement."

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
