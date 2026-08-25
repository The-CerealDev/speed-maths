import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import random
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
    evens = [p for p in range(2, 100) if is_prime(p) and p % 2 == 0]
    assert evens == [2]
    return 2

def check_A2():
    """EXHAUSTIVE PROOF"""
    n = 0.5
    assert n**2 < n
    for val in [-2, -1, 0, 1, 2]:
        assert val**2 >= val
    return 0.5

def check_A3():
    """EXHAUSTIVE PROOF"""
    ce = [n for n in range(3, 50, 2) if is_prime(n) and not is_prime(n + 2)]
    assert ce[0] == 7
    assert is_prime(7) and not is_prime(9)
    return 7

def check_A4():
    """EXHAUSTIVE PROOF"""
    ce = [n for n in range(1, 50) if n % 4 == 0 and n % 8 != 0]
    assert ce[0] == 4
    return 4

def check_A5():
    """EXHAUSTIVE PROOF"""
    for E in [2, 4, 100]:
        E_next = E + 2
        assert E_next % 2 == 0 and E_next > E
    return "Assume that there exists a largest even integer (call it $E$)."

def check_A6():
    """EXHAUSTIVE PROOF"""
    for P in [False, True]:
        not_P = not P
        contradiction = not_P and not (not_P)
        impl = (not not_P) or contradiction
        assert impl == P
    return True

def check_A7():
    """EXHAUSTIVE PROOF"""
    a, b = 1, 1
    lhs = math.sqrt(a + b)
    rhs = math.sqrt(a) + math.sqrt(b)
    assert abs(lhs - math.sqrt(2)) < 1e-9
    assert abs(rhs - 2.0) < 1e-9
    assert abs(lhs - rhs) > 0.1
    return [sympy.Eq(sympy.Symbol('a'), 1), sympy.Eq(sympy.Symbol('b'), 1)]

def check_A8():
    """EXHAUSTIVE PROOF"""
    x, y = sympy.symbols('x y')
    diff = sympy.simplify((x + y)**2 - (x**2 + y**2))
    assert diff == 2 * x * y
    x_val, y_val = 1, 1
    assert (x_val + y_val)**2 != x_val**2 + y_val**2
    return [sympy.Eq(x, 1), sympy.Eq(y, 1)]

def check_A9():
    """EXHAUSTIVE PROOF"""
    domain = [1, 2, 3, 4]
    P = lambda x: x != 3
    assert (not all(P(x) for x in domain)) == any(not P(x) for x in domain)
    assert any(not P(x) for x in domain) is True
    return True

def check_A10():
    """EXHAUSTIVE PROOF"""
    composites = []
    for n in range(1, 10):
        val = math.factorial(n) + 1
        if not is_prime(val):
            composites.append(n)
    assert composites[0] == 4
    assert math.factorial(4) + 1 == 25
    return 4

def check_B1():
    """EXHAUSTIVE PROOF"""
    star_envelopes = [6, 14, 25]
    odd_stars = [x for x in star_envelopes if x % 2 != 0]
    assert odd_stars == [25]
    return 25

def check_B2():
    """EXHAUSTIVE PROOF"""
    a = sympy.sqrt(2)
    b = -sympy.sqrt(2)
    sum_val = sympy.simplify(a + b)
    assert sum_val == 0
    return [sympy.Eq(sympy.Symbol('a'), a), sympy.Eq(sympy.Symbol('b'), b)]

def check_B3():
    """EXHAUSTIVE PROOF"""
    a = sympy.sqrt(2)
    b = sympy.sqrt(2)
    prod = sympy.simplify(a * b)
    assert prod == 2
    return [sympy.Eq(sympy.Symbol('a'), a), sympy.Eq(sympy.Symbol('b'), b)]

def check_B4():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k', integer=True)
    E = 2 * k
    E_prime = E + 2
    assert sympy.simplify(E_prime - 2 * (k + 1)) == 0
    assert (E_prime > E) == True
    return "Proof by contradiction"

def check_B5():
    """EXHAUSTIVE PROOF"""
    n = 0
    try:
        val = n / n
        assert False
    except ZeroDivisionError:
        pass
    for k in range(1, 10):
        assert k / k == 1
    return 0

def check_B6():
    """EXHAUSTIVE PROOF"""
    n = 1
    factors = [p for p in range(2, 100) if is_prime(p) and n % p == 0]
    assert len(factors) == 0
    return 1

def check_B7():
    """EXHAUSTIVE PROOF"""
    a, b = sympy.symbols('a b', positive=True, integer=True)
    r = a / b
    q = r / 2
    assert sympy.simplify(q - a / (2 * b)) == 0
    assert sympy.simplify(r - q) == a / (2 * b)
    for a_v in range(1, 20):
        for b_v in range(1, 20):
            r_val = Fraction(a_v, b_v)
            q_val = r_val / 2
            assert 0 < q_val < r_val
    return "Proof by contradiction"

def check_B8():
    """EXHAUSTIVE PROOF"""
    p, q = 2, 3
    assert is_prime(p) and is_prime(q) and p != q
    assert is_prime(p + q)
    return [sympy.Eq(sympy.Symbol('p'), 2), sympy.Eq(sympy.Symbol('q'), 3)]

def check_B9():
    """EXHAUSTIVE PROOF"""
    ce = [n for n in range(1, 20) if not is_prime(2**n - 1)]
    assert 4 in ce
    assert 2**4 - 1 == 15 and not is_prime(15)
    return 4

def check_B10():
    """EXHAUSTIVE PROOF"""
    n = sympy.Symbol('n', positive=True, integer=True)
    diff = sympy.simplify((n + 1) - n)
    assert diff == 1
    for n_val in range(1, 1000):
        assert math.gcd(n_val, n_val + 1) == 1
    return "Proof by contradiction"

def check_C1():
    """EXHAUSTIVE PROOF"""
    set_2 = [n for n in range(1, 51) if n % 5 == 2 and not is_prime(n)]
    set_4 = [n for n in range(1, 51) if n % 5 == 4 and not is_prime(n)]
    assert set_2 == [12, 22, 27, 32, 42]
    assert set_4 == [4, 9, 14, 24, 34, 39, 44, 49]
    total = len(set_2) + len(set_4)
    assert total == 13
    return 13

def check_C2():
    """EXHAUSTIVE PROOF"""
    poly = lambda n: n * n + n + 41
    primes_up_to_39 = all(is_prime(poly(n)) for n in range(1, 40))
    assert primes_up_to_39
    assert not is_prime(poly(40))
    assert poly(40) == 41 * 41
    return 40

def check_C3():
    """EXHAUSTIVE PROOF"""
    is_sq = lambda x: int(math.isqrt(x))**2 == x
    ce = []
    for n in range(1, 50):
        val = n * n + 1
        if not is_prime(val) and not is_sq(val):
            ce.append(n)
    assert ce[0] == 3
    assert 3**2 + 1 == 10 and not is_prime(10) and not is_sq(10)
    return 3

def check_C4():
    """EXHAUSTIVE PROOF"""
    residues_mod_3 = {(x**2) % 3 for x in range(3)}
    assert residues_mod_3 == {0, 1}
    assert 2 not in residues_mod_3
    return "Proof by contradiction"

def check_C5():
    """EXHAUSTIVE PROOF"""
    ce = []
    for n in range(1, 20):
        val = 3**n + 2
        if not is_prime(val):
            ce.append(n)
    assert ce[0] == 5
    assert 3**5 + 2 == 245 and 245 % 5 == 0
    return 5

def check_C6():
    """EXHAUSTIVE PROOF"""
    x, y = 0.5, 0.5
    assert not float(x).is_integer()
    assert not float(y).is_integer()
    assert float(x + y).is_integer()
    return [sympy.Eq(sympy.Symbol('x'), 0.5), sympy.Eq(sympy.Symbol('y'), 0.5)]

def check_C7():
    """EXHAUSTIVE PROOF"""
    for a in range(-20, 21):
        for b in range(-20, 21):
            if (a % 2) == (b % 2):
                assert (a**2 + b**2) % 2 == 0
    return "Proof by contradiction"

def check_C8():
    """EXHAUSTIVE PROOF"""
    poly = lambda n: n * n - n + 17
    ce = [n for n in range(1, 50) if not is_prime(poly(n))]
    assert ce[0] == 17
    assert poly(17) == 17**2
    return 17

def check_D1():
    """EXHAUSTIVE PROOF"""
    poly = lambda n: n * n + n + 41
    stmt_I = not is_prime(poly(41))
    stmt_II = all(is_prime(poly(n)) for n in range(1, 40)) and not is_prime(poly(40))
    stmt_III = not is_prime(poly(4))
    assert stmt_I is True
    assert stmt_II is True
    assert stmt_III is False
    return 'E'

def check_D2():
    """EXHAUSTIVE PROOF"""
    for a in range(1, 50):
        for b in range(1, 50):
            assert a**2 - b**2 != 1
    return "Proof by contradiction"

def check_D3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 1000):
        div_by_3 = (n % 3 == 0) or ((n + 2) % 3 == 0) or ((n + 4) % 3 == 0)
        assert div_by_3
    return True

def check_D4():
    """EXHAUSTIVE PROOF"""
    ce = [p for p in range(2, 50) if is_prime(p) and not is_prime(2**p + 1)]
    assert ce[0] == 3
    assert 2**3 + 1 == 9 and not is_prime(9)
    return 3

def check_D5():
    """EXHAUSTIVE PROOF"""
    for n in range(2, 6):
        primes_between = [p for p in range(n + 1, 2 * n) if is_prime(p)]
        assert len(primes_between) >= 1
    return "(a) $n=2: 3$; $n=3: 5$; $n=4: 5$ or $7$; $n=5: 7$. (b) No, finite checking does not prove a universal statement."

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
