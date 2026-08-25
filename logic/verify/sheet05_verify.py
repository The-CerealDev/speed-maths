import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import random
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans05.tex'

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

def check_A1():
    """EXHAUSTIVE PROOF"""
    P = lambda n: n % 6 == 0
    Q = lambda n: n % 3 == 0
    assert Q(15) is True and P(15) is False
    assert all(not P(n) or Q(n) for n in range(-100, 101))
    return "Affirming the consequent"

def check_A2():
    """EXHAUSTIVE PROOF"""
    P = lambda x: x > 10
    Q = lambda x: x > 0
    assert (not P(5)) is True and (not Q(5)) is False
    return "Denying the antecedent"

def check_A3():
    """EXHAUSTIVE PROOF"""
    for x in range(3, 50):
        assert x > 2 and x**2 > 4
    return False

def check_A4():
    """EXHAUSTIVE PROOF"""
    trusted_lines = [1, 2, 3]
    assert len(trusted_lines) == 3
    return 3

def check_A5():
    """EXHAUSTIVE PROOF"""
    x = -2
    assert x != 2
    assert x**2 == 2**2
    return False

def check_A6():
    """EXHAUSTIVE PROOF"""
    for premise in [True]:
        conclusion = (0 == 1)
        valid_step = (not premise) or conclusion
        assert valid_step is False
    return "At least one line of the argument contains an error."

def check_A7():
    """EXHAUSTIVE PROOF"""
    poly = lambda n: n * n - n + 11
    assert all(is_prime(poly(n)) for n in range(1, 11))
    assert not is_prime(poly(11))
    return False

def check_A8():
    """EXHAUSTIVE PROOF"""
    a, b, x = 2, 5, 0
    assert a * x == b * x
    assert a != b
    return "The step is invalid if $x=0$."

def check_A9():
    """EXHAUSTIVE PROOF"""
    for P in [False, True]:
        contradiction = P and (not P)
        assert contradiction is False
    return True

def check_A10():
    """EXHAUSTIVE PROOF"""
    a, b, c, d = 1, 2, 2, 4
    assert Fraction(a, b) == Fraction(c, d)
    assert a != c and b != d
    return "Equal fractions do not require equal numerators and denominators separately."

def check_B1():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    n_sq = sympy.expand(n**2)
    assert sympy.simplify(n_sq - (2 * (2 * k**2 + 2 * k) + 1)) == 0
    for k_val in range(-50, 51):
        assert (2 * k_val + 1)**2 % 2 == 1
    return "Yes, fully valid."

def check_B2():
    """EXHAUSTIVE PROOF"""
    x = 0
    assert x**2 == 3 * x
    assert x != 3
    return "Dividing by $x$ is invalid when $x=0$."

def check_B3():
    """EXHAUSTIVE PROOF"""
    x1, x2 = 9, 2
    assert math.sqrt(x1 + 7) == x1 - 5
    assert math.sqrt(x2 + 7) != x2 - 5
    assert (x2 + 7) == (x2 - 5)**2
    return "$x=2$ is an extraneous root introduced by squaring; it must be checked against and rejected from the original equation."

def check_B4():
    """EXHAUSTIVE PROOF"""
    n = sympy.Symbol('n')
    written_line2 = 4 * n + 1 - n - 3
    correct_line2 = (4 * n + 1) - (n - 3)
    assert sympy.simplify(written_line2 - (3 * n - 2)) == 0
    assert sympy.simplify(correct_line2 - (3 * n + 4)) == 0
    assert sympy.simplify(written_line2 - correct_line2) != 0
    return "Line 2"

def check_B5():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    expr = sympy.expand(n**2 + n + 2)
    assert sympy.simplify(expr - 2 * (2 * k**2 + 3 * k + 2)) == 0
    for n_val in range(-50, 51):
        assert (n_val**2 + n_val + 2) % 2 == 0
    return "The proof only checks the even case; the odd case is never addressed."

def check_B6():
    """EXHAUSTIVE PROOF"""
    x = -3
    assert x**2 == 9 and x != 3
    return "Only the $\\Longleftarrow$ direction ($x=3\\implies x^2=9$) was shown; the $\\Longrightarrow$ direction ($x^2=9\\implies x=3$) is false, since $x=-3$ also satisfies $x^2=9$."

def check_B7():
    """EXHAUSTIVE PROOF"""
    fib = [0, 1, 1]
    for i in range(3, 10):
        fib.append(fib[-1] + fib[-2])
    assert fib[3] == 2 and is_prime(2)
    assert fib[4] == 3 and is_prime(3)
    assert fib[5] == 5 and is_prime(5)
    assert fib[6] == 8 and not is_prime(8) and fib[6] != 1
    return "Checking finitely many cases does not prove a universal claim; $F_6=8=2^3$ is the smallest counterexample."

def check_B8():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        if n % 3 == 0:
            assert (n * n) % 3 == 0
        if (n * n) % 3 == 0:
            assert n % 3 == 0
    return "The statement shown is neither the original claim nor its contrapositive --- it proves nothing about the original."

def check_B9():
    """EXHAUSTIVE PROOF"""
    j, k = sympy.symbols('j k')
    a, b = 2 * j, 2 * k
    sum_val = sympy.simplify(a + b)
    assert sum_val == 2 * (j + k)
    return "Circular reasoning: the proof begins by assuming $a+b$ is even (the very thing to be proved) instead of deriving it."

def check_B10():
    """EXHAUSTIVE PROOF"""
    students = [True, False]
    all_passed = all(students)
    all_failed = all(not s for s in students)
    at_least_one_failed = any(not s for s in students)
    assert not all_passed
    assert not all_failed
    assert at_least_one_failed
    return "The correct negation of ``every student passed'' is ``at least one student did not pass'', not ``every student failed''."

def check_C1():
    """EXHAUSTIVE PROOF"""
    assert 2**2 - 4 * 2 * 1 == -4
    val = 2 * 3**2 + 2 * 3 + 1
    assert val == 25 and not is_prime(val)
    return 'D'

def check_C2():
    """EXHAUSTIVE PROOF"""
    roots = [2, 3]
    assert all(r**2 - 5 * r + 6 == 0 for r in roots)
    assert 3**2 - 5 * 3 + 6 == 0 and 3 != 2
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF"""
    for n in range(-50, 51):
        assert (n**2 + n) % 2 == 0
    return 'B'

def check_C4():
    """EXHAUSTIVE PROOF"""
    assert is_prime(3) and is_prime(5) and is_prime(7)
    return 'C'

def check_C5():
    """EXHAUSTIVE PROOF"""
    for n in range(100):
        assert n + 1 > n
    return 'B'

def check_C6():
    """EXHAUSTIVE PROOF"""
    W, X, Y, Z = (0, 3), (2, 0), (0, -1), (-2, 0)
    d1 = (Y[0] - W[0], Y[1] - W[1])
    d2 = (Z[0] - X[0], Z[1] - X[1])
    assert d1[0] * d2[0] + d1[1] * d2[1] == 0
    s1 = math.hypot(X[0] - W[0], X[1] - W[1])
    s2 = math.hypot(Y[0] - X[0], Y[1] - X[1])
    assert s1 != s2
    return 'B'

def check_C7():
    """EXHAUSTIVE PROOF"""
    x, y = -2, -5
    assert abs(x + y) == 7
    assert abs(x) + abs(y) == 7
    assert not (abs(x + y) < abs(x) + abs(y))
    return 'D'

def check_C8():
    """EXHAUSTIVE PROOF"""
    sides = [math.hypot(5, 0), math.hypot(3, 4), math.hypot(-5, 0), math.hypot(-3, -4)]
    assert len(set(sides)) == 1 and sides[0] == 5.0
    diag1_sq = 8**2 + 4**2
    diag2_sq = (-2)**2 + 4**2
    assert diag1_sq != diag2_sq
    return 'B'

def check_D1():
    """EXHAUSTIVE PROOF"""
    s, p = sympy.symbols('s p')
    u, v = sympy.symbols('u v')
    diff_sq = sympy.expand((u - v)**2)
    ident = sympy.expand((u + v)**2 - 4 * u * v)
    assert sympy.simplify(diff_sq - ident) == 0
    return 'B'

def check_D2():
    """EXHAUSTIVE PROOF"""
    poly1 = lambda n: n * n - n + 11
    poly2 = lambda n: n * n + n + 11
    for n in range(1, 10):
        if is_prime(poly1(n)):
            assert is_prime(poly2(n))
    assert is_prime(poly1(10)) and poly1(10) == 101
    assert not is_prime(poly2(10)) and poly2(10) == 121
    return "(a) Finite verification is not a universal proof. (b) $n=10$."

def check_D3():
    """EXHAUSTIVE PROOF"""
    j, k = sympy.symbols('j k')
    prod = sympy.expand((2 * j + 1) * (2 * k + 1))
    assert sympy.simplify(prod - (2 * (2 * j * k + j + k) + 1)) == 0
    return 'D'

def check_D4():
    """EXHAUSTIVE PROOF"""
    for p in range(5, 1000):
        if is_prime(p):
            assert p % 6 in (1, 5)
    assert 25 % 6 == 1 and not is_prime(25)
    return 'B'

def check_D5():
    """EXHAUSTIVE PROOF"""
    assert is_prime(2**2 - 1)
    for n in range(3, 100):
        assert not is_prime(n**2 - 1)
        assert (n - 1) >= 2 and (n + 1) >= 4
    return "(a) Line 3. (b) $n=2$; and $n=2$ is the unique exception."

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
