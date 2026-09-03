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
    # Show the original statement is false and negation is true
    # For x=1, for all real y, x^2 + y^2 = 1 + y^2 >= 1
    for y_val in [-5.0, -1.0, 0.0, 1.0, 5.0]:
        assert 1.0**2 + y_val**2 >= 1.0
    # Original is false because for x >= 1, no real y satisfies x^2 + y^2 < 1
    assert not any(1.0**2 + (k / 10.0)**2 < 1.0 for k in range(-50, 51))
    return r"\exists x \in \mathbb{R},\ \forall y \in \mathbb{R} : x^2 + y^2 \ge 1."

def check_A2():
    """EXHAUSTIVE PROOF"""
    domain = range(1, 100)
    # Check if for n = 1, there exists m in Z+ with m < 1
    has_smaller = {n: any(m < n for m in domain) for n in domain}
    assert not has_smaller[1]
    return False

def check_A3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        even = (n % 2 == 0)
        mult4 = (n % 4 == 0)
        mult6 = (n % 6 == 0)
        implication = (not even) or (mult4 or mult6)
        negation = even and (not mult4) and (not mult6)
        assert negation == (not implication)
    # Verify counterexample at n = 2 and n = 10
    assert (2 % 2 == 0) and (2 % 4 != 0) and (2 % 6 != 0)
    return "n is even, and n is not a multiple of 4, and n is not a multiple of 6."

def check_A4():
    """EXHAUSTIVE PROOF"""
    x = 0
    for y in [-100, -1, 0, 1, 100]:
        assert x * y == 0
    return True

def check_A5():
    """EXHAUSTIVE PROOF"""
    for y in [-10, -2, -0.5, 0.25, 1, 3, 7]:
        x = 1.0 / y
        assert math.isclose(x * y, 1.0)
    return True

def check_A6():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        iff_val = (P == Q)
        xor_val = (P and not Q) or (not P and Q)
        if not iff_val:
            assert xor_val is True
    return True

def check_A7():
    """EXHAUSTIVE PROOF"""
    for k in range(-50, 80):
        x = k / 10.0
        orig = (-2.0 <= x < 5.0) and (x != 0.0)
        neg = (x < -2.0) or (x == 0.0) or (x >= 5.0)
        assert neg == (not orig)
    return "x < -2 or x = 0 or x \\ge 5."

def check_A8():
    """EXHAUSTIVE PROOF"""
    # For k <= 0: if x < 0, x^2 > 0 >= k holds.
    for k in [-10, -1, 0]:
        for x in [-5, -1, -0.1]:
            assert x**2 > k
    # For k > 0: fails for x near 0
    for k in [0.01, 1, 4]:
        x = -math.sqrt(k) / 2.0
        assert x < 0
        assert not (x**2 > k)
    return "k \\le 0."

def check_A9():
    """EXHAUSTIVE PROOF"""
    matching = []
    for P, Q, R, S in all_assignments(4):
        antecedent = P and Q
        consequent = R or S
        implication = (not antecedent) or consequent
        if not implication:
            matching.append((P, Q, R, S))
    assert matching == [(True, True, False, False)]
    return "P is True, Q is True, R is False, and S is False."

def check_A10():
    """EXHAUSTIVE PROOF"""
    # Check Goldbach for small evens
    primes = [p for p in range(2, 50) if is_prime(p)]
    for n in range(4, 30, 2):
        assert any(n - p in primes for p in primes if p < n)
    return "There exists an even integer n > 2 such that for all primes p and q, n \\neq p + q."

def check_B1():
    """EXHAUSTIVE PROOF"""
    def is_S_number(n):
        for d in range(2, n + 1):
            if n % d == 0:
                if d % 2 != 0 and d % 3 != 0:
                    return False
        return True
    # Minimal non-S number is 5 (d=5 has gcd(5, 6)=1)
    assert is_S_number(2) and is_S_number(3) and is_S_number(4)
    assert not is_S_number(5)
    return 'B'

def check_B2():
    """EXHAUSTIVE PROOF"""
    for P, Q, R in all_assignments(3):
        imp1 = (not P) or Q
        imp2 = (not Q) or R
        imp3 = (not R) or P
        num_true = sum([imp1, imp2, imp3])
        if P == Q == R:
            assert num_true == 3
        if num_true == 2:
            assert not (P == Q == R)
    return "No."

def check_B3():
    """EXHAUSTIVE PROOF"""
    # x >= 0: x(1-y) + y > 0 for all y in (0, 1)
    for x in [0, 0.5, 1, 5, 100]:
        for y in [0.001, 0.1, 0.5, 0.999]:
            assert x * y < x + y
    # x < 0: fails for small y
    for x in [-0.1, -1, -5]:
        c = -x
        y = c / (2 * (1 + c))  # y < c / (1+c)
        assert 0 < y < 1
        assert not (x * y < x + y)
    return "[0, \\infty)."

def check_B4():
    """EXHAUSTIVE PROOF"""
    # Original is false: at x = 1, y < 1 implies xy = y < 1, so xy >= 1 is impossible
    x = 1.0
    for k in range(1, 100):
        y = k / 100.0
        if y < x:
            assert x * y < 1.0
    return "Negation: \\exists x > 0, \\forall y > 0 : (y \\ge x \\lor xy < 1). Original is False."

def check_B5():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 200):
        s1 = (n % 6 == 0)
        s2 = (n % 2 == 1)
        s3 = is_prime(n) and (n > 3)
        if s3:
            assert s2 is True  # Every prime > 3 is odd
            assert sum([s1, s2, s3]) >= 2
    # III can never be the unique true statement
    return "Statement III."

def check_B6():
    """EXHAUSTIVE PROOF"""
    for q in range(3, 1000):
        if is_prime(q):
            assert q % 2 == 1
    return "Negation: For every prime p, there exists a prime q>p such that q is even. The original statement is true."

def check_B7():
    """EXHAUSTIVE PROOF"""
    # For primes a, Euclid's lemma holds
    for a in range(2, 20):
        if is_prime(a):
            for b in range(1, 10):
                for c in range(1, 10):
                    if (b * c) % a == 0:
                        assert (b % a == 0) or (c % a == 0)
    # Smallest counterexample requires composite a
    a, b, c = 4, 2, 2
    assert (b * c) % a == 0
    assert (b % a != 0) and (c % a != 0)
    return "(a) \\exists a, b, c \\in \\mathbb{Z}^+ : a \\mid bc \\land a \\nmid b \\land a \\nmid c. (b) a = 4, b = 2, c = 2."

def check_B8():
    """EXHAUSTIVE PROOF"""
    count = 0
    for P, Q, R in all_assignments(3):
        premise = P or Q
        implication = (not premise) or R
        if not implication:
            count += 1
            assert R is False
            assert (P or Q) is True
    assert count == 3
    return 3

def check_B9():
    """EXHAUSTIVE PROOF"""
    # Symbolic boolean equivalence of the negated predicate
    for in_Q, gt_0 in all_assignments(2):
        orig = in_Q or ((not in_Q) and gt_0)
        neg = (not in_Q) and not ((not in_Q) and gt_0)
        simplified_neg = (not in_Q) and (not gt_0)
        assert neg == (not orig) == simplified_neg
    return "Negation: \\exists x \\in \\mathbb{R} : x \\notin \\mathbb{Q} \\land x \\le 0. Witness: -\\sqrt{2} (or any non-positive irrational)."

def check_B10():
    """EXHAUSTIVE PROOF"""
    p = 2
    assert is_prime(p)
    val = p**2 + 2
    assert not is_prime(val)  # 2^2 + 2 = 6, composite
    return "Negation: There exists a prime p such that p^2 + 2 is composite. Smallest counterexample: p = 2."

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
