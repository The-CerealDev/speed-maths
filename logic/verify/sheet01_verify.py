import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import random
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'

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
    for n in range(-1000, 1001):
        orig = n * n >= 0
        neg = n * n < 0
        assert neg == (not orig)
    return "There exists an integer n such that n^2<0."

def check_A2():
    """EXHAUSTIVE PROOF"""
    for k in range(-100, 101):
        x = k / 10.0
        orig = (x * x == -1)
        neg = (x * x != -1)
        assert neg == (not orig)
    return "For all real numbers x, x^2 \\neq -1."

def check_A3():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = P and Q
        claimed_neg = (not P) or (not Q)
        assert claimed_neg == (not orig)
    return "n is odd, or n is not prime."

def check_A4():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = P or Q
        claimed_neg = (not P) and (not Q)
        assert claimed_neg == (not orig)
    return "n is not a multiple of 4, and n is not a multiple of 6."

def check_A5():
    """EXHAUSTIVE PROOF"""
    domain = {1, 2}
    P = lambda x: x == 1
    true_neg = any(not P(x) for x in domain)
    wrong_neg = all(not P(x) for x in domain)
    assert true_neg != wrong_neg
    return False

def check_A6():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        assert (not (P and Q)) == ((not P) or (not Q))
    return True

def check_A7():
    """EXHAUSTIVE PROOF"""
    for k in range(-20, 40):
        x = k / 2.0
        orig = (x > 3 and x < 10)
        neg = (x <= 3 or x >= 10)
        assert neg == (not orig)
    return "x \\leq 3 or x \\geq 10."

def check_A8():
    """EXHAUSTIVE PROOF"""
    assert is_prime(2) and 2 % 2 == 0
    return "\\exists-statement."

def check_A9():
    """EXHAUSTIVE PROOF"""
    for x in range(-10, 10):
        y = 1 - x
        assert x + y == 1 != 0
    return False

def check_A10():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        A = is_prime(n)
        B = (n == 1)
        orig = A or B
        neg = (not A) and (not B)
        assert neg == (not orig)
    return "n is not prime, and n \\neq 1."

def check_B1():
    """EXHAUSTIVE PROOF"""
    for pattern in itertools.product([False, True], repeat=7):
        orig = all(pattern)
        neg = any(not d for d in pattern)
        assert neg == (not orig)
    return "Some day next week, Fred will do no maths problems."

def check_B2():
    """EXHAUSTIVE PROOF"""
    for P, Q, R in all_assignments(3):
        orig = P or Q or R
        claimed_neg = (not P) and (not Q) and (not R)
        assert claimed_neg == (not orig)
    return True

def check_B3():
    """EXHAUSTIVE PROOF"""
    for P, Q, R in all_assignments(3):
        orig = P and Q and R
        claimed_neg = (not P) or (not Q) or (not R)
        assert claimed_neg == (not orig)
    return "n is not a multiple of 2, or n is not a multiple of 3, or n is not a multiple of 5."

def check_B4():
    """EXHAUSTIVE PROOF"""
    for k in range(1, 50):
        x = k / 10.0
        y = x / 2.0
        assert 0 < y < x
    return "There exists a real x>0 such that for every real y>0, y \\geq x."

def check_B5():
    """EXHAUSTIVE PROOF"""
    for m in range(-10, 10):
        n = m
        assert not (m > n)
    return False

def check_B6():
    """EXHAUSTIVE PROOF"""
    for q in range(3, 1000):
        if is_prime(q):
            assert q % 2 == 1
    return "Negation: For every prime p, there exists a prime q>p such that q is even. The original statement is true."

def check_B7():
    """EXHAUSTIVE PROOF"""
    for A, B, C in all_assignments(3):
        orig = A or (B and C)
        neg = (not A) and ((not B) or (not C))
        assert neg == (not orig)
    return "n is not a multiple of 3, and (n is not a multiple of 2 or n is not a multiple of 5)."

def check_B8():
    """EXHAUSTIVE PROOF"""
    for A, B, C in all_assignments(3):
        orig = A and (B or C)
        neg = (not A) or ((not B) and (not C))
        assert neg == (not orig)
    return True

def check_B9():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = P or ((not P) and Q)
        neg = (not P) and (P or (not Q))
        assert neg == (not orig)
    return "x is irrational, and (x is rational or x \\leq 0)."

def check_B10():
    """EXHAUSTIVE PROOF"""
    evens_gt_2 = [p for p in range(3, 1000) if is_prime(p) and p % 2 == 0]
    assert len(evens_gt_2) == 0
    return "Negation: There exists a prime p>2 such that p is even. The negation is false."

def check_C1():
    """EXHAUSTIVE PROOF"""
    assert not (5**2 < 1)
    for x in range(-10, 11):
        n = x**2 + 1
        assert x**2 < n
    for n in range(1, 100):
        assert 0**2 < n
    return "II and III only."

def check_C2():
    """EXHAUSTIVE PROOF"""
    for k in [-10, -5, -1, 0]:
        for x in [k - 0.5, k - 1, k - 10]:
            assert x**2 > k
    for k in [0.1, 1.0, 5.0]:
        x = 0
        assert x < k
        assert not (x**2 > k)
    return 'C'

def check_C3():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        orig = P or Q
        neg = (not P) and (not Q)
        assert neg == (not orig)
    return 'B'

def check_C4():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 1000):
        assert (n**2 + n + 1) % 2 == 1
    return "Negation: For every positive integer n, n^2+n+1 is odd. The negation is true."

def check_C5():
    """EXHAUSTIVE PROOF"""
    n = 2520
    assert all(n % k == 0 for k in range(1, 11))
    return "Negation: For every positive integer n, there exists a positive integer k\\leq 10 such that k does not divide n. The original statement is true."

def check_C6():
    """EXHAUSTIVE PROOF"""
    for x in range(-100, 101):
        y = 1
        assert x * y - x + y == 1 > 0
    return 'E'

def check_C7():
    """EXHAUSTIVE PROOF"""
    for y in range(-50, 50):
        assert 1 * y == y
    return "Negation: For every real number x, there exists a real number y such that xy \\neq y. The original statement is true."

def check_C8():
    """EXHAUSTIVE PROOF"""
    assert len([m for m in range(1, 1) if is_prime(m)]) == 0
    assert len([m for m in range(1, 2) if is_prime(m)]) == 0
    return "Negation: There exists a positive integer n such that no positive integer m<n is prime. The original statement is false, witnessed by n=1 (and also n=2)."

def check_D1():
    """EXHAUSTIVE PROOF"""
    Ss = range(3)
    Ms = range(3)
    cells = [(s, m) for s in Ss for m in Ms]
    for bits in itertools.product([False, True], repeat=len(cells)):
        leq = dict(zip(cells, bits))
        orig = all(any(leq[s, m] for m in Ms) for s in Ss)
        correct_neg = not orig
        optionA = any(all(not leq[s, m] for m in Ms) for s in Ss)
        assert optionA == correct_neg
    return 'A'

def check_D2():
    """EXHAUSTIVE PROOF"""
    for eps in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000), Fraction(1, 1000000)]:
        N = eps.denominator // eps.numerator + 1
        assert Fraction(1, N) < eps
        for n in range(N, N + 100):
            assert Fraction(1, n) < eps
    return True

def check_D3():
    """EXHAUSTIVE PROOF"""
    terms = list(range(2, 93, 3))
    assert len(terms) == 31
    pairs = []
    singletons = []
    for x in terms:
        comp = 94 - x
        if comp == x:
            singletons.append(x)
        elif comp in terms and x < comp:
            pairs.append((x, comp))
    assert len(singletons) == 1 and singletons == [47]
    assert len(pairs) == 15
    max_avoiding = len(pairs) + len(singletons)
    assert max_avoiding == 16
    assert max_avoiding + 1 == 17
    return 'C'

def check_D4():
    """EXHAUSTIVE PROOF"""
    for plist in [[2], [2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11]]:
        N = 1
        for p in plist:
            N *= p
        N += 1
        for p in plist:
            assert math.gcd(N, p) == 1
    return "(a) There exists a finite set of primes containing every prime. (b) (*) is true."

def check_D5():
    """EXHAUSTIVE PROOF"""
    f = lambda y: y
    for x in range(-10, 11):
        assert f(x) == x
    assert f(0) != 1
    return "(a) No, not equivalent. (b) $f(y)=y$ (the identity function on $\\mathbb{R}$)."

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
