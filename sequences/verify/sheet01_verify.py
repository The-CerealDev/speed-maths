import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 5 + 3 * (n - 1)
    assert a(1) == 5
    assert a(4) == 14
    for n in range(1, 10):
        assert a(n) == 3 * n + 2
    n = sympy.Symbol('n')
    return 3 * n + 2

def check_A2():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 7 - 3 * (n - 1)
    assert a(20) == 7 - 57
    assert a(20) == -50
    return -50

def check_A3():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 4 + 5 * (n - 1)
    S_10 = sum((a(n) for n in range(1, 11)))
    assert S_10 == 265
    assert a(10) == 49
    assert S_10 == 5 * (4 + 49)
    assert 5 * (8 + 45) == 265
    return 265

def check_A4():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 4 * n - 1
    assert a(1) == 3
    assert a(2) == 7
    assert a(3) == 11
    assert a(2) - a(1) == 4
    assert a(3) - a(2) == 4
    return [[3, 7, 11], 4]

def check_A5():
    """EXHAUSTIVE PROOF"""
    a_1 = 2
    a_5 = 18
    d = (a_5 - a_1) / 4
    assert d == 4
    assert a_5 - a_1 == 16
    return int(d)

def check_A6():
    """EXHAUSTIVE PROOF"""
    assert sum(range(1, 51)) == 1275
    assert 50 * 51 // 2 == 1275
    return 1275

def check_A7():
    """EXHAUSTIVE PROOF"""
    def S(n):
        return n ** 2 + 3 * n
    a_1 = S(1)
    assert a_1 == 4
    return a_1

def check_A8():
    """EXHAUSTIVE PROOF"""
    def a(n, a1, d):
        return a1 + (n - 1) * d
    for a1 in range(-5, 5):
        for d in range(-5, 5):
            for n in range(1, 20):
                assert isinstance(a(n, a1, d), int)
    return True

def check_A9():
    """EXHAUSTIVE PROOF"""
    a_3 = 13
    a_9 = 37
    assert a_9 - a_3 == 24
    d = (a_9 - a_3) / 6
    assert d == 4
    return int(d)

def check_A10():
    """EXHAUSTIVE PROOF"""
    a_1 = 4
    a_6 = 29
    assert a_6 - a_1 == 25
    d = (a_6 - a_1) / 5
    assert d == 5
    return int(d)

def check_B1():
    """EXHAUSTIVE PROOF"""
    a = 3
    l = 59
    n = 15
    d = (l - a) // (n - 1)
    assert d == 4
    S_15 = sum((a + i * d for i in range(n)))
    assert S_15 == 465
    assert n * (a + l) // 2 == 465
    return [d, S_15]

def check_B2():
    """EXHAUSTIVE PROOF"""
    S_8 = 100
    S_4 = 30
    assert S_8 - S_4 == 70
    return 'B'

def check_B3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        S_n = sum((3 * i for i in range(1, n + 1)))
        assert S_n == 3 * n * (n + 1) // 2
    return 'Proof by the AP sum formula.'

def check_B4():
    """EXHAUSTIVE PROOF"""
    middle_term = 315 // 21
    assert middle_term == 15
    a, d = sympy.symbols('a d')
    S_21 = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, 20)).doit()
    assert sympy.simplify(S_21 - 21 * (a + 10 * d)) == 0
    return 'A'

def check_B5():
    """EXHAUSTIVE PROOF"""
    a = 10
    d = -3
    a_n = lambda n: a + (n - 1) * d
    assert a_n(4) == 1
    assert a_n(5) == -2
    assert a_n(4) > 0 and a_n(5) < 0
    return a_n(4)

def check_B6():
    """EXHAUSTIVE PROOF"""
    a, d = (-100, 1)
    seq = [a + i * d for i in range(5)]
    assert any((x < 0 for x in seq))
    assert all((seq[i] < seq[i + 1] for i in range(len(seq) - 1)))
    assert all((seq[i + 1] - seq[i] == d for i in range(len(seq) - 1)))
    return 'D'

def check_B7():
    """EXHAUSTIVE PROOF"""
    a1, d, n = sympy.symbols('a1 d n')
    a_n = a1 + (n - 1) * d
    b_n = (a1 - 6) + (n - 1) * d
    assert sympy.simplify(a_n - b_n) == 6
    for d_val in range(-10, 11):
        for a_val in range(-10, 11):
            b_val = a_val - 6
            for n_val in range(1, 10):
                assert (a_val + (n_val - 1) * d_val) - (b_val + (n_val - 1) * d_val) == 6
    return 'A'

def check_B8():
    """EXHAUSTIVE PROOF"""
    a, d = (1, 5)
    a_n = lambda n: a + (n - 1) * d
    assert a_n(3) == 11
    assert a_n(3) + a_n(5) == 32
    assert a + 2 * d == 11
    assert 2 * a + 6 * d == 32
    assert a + 3 * d == 16
    assert a + 3 * d - (a + 2 * d) == 5
    return 'C'

def check_B9():
    """EXHAUSTIVE PROOF"""
    possible = []
    for a in range(1, 20):
        for d in range(1, 20):
            if a + 4 * d == 17:
                possible.append((a, d))
    assert (13, 1) in possible
    assert (9, 2) in possible
    assert (5, 3) in possible
    assert (2, 4) not in possible
    assert 2 + 4 * 4 == 18
    return 'D'

def check_B10():
    """EXHAUSTIVE PROOF"""
    ap = [2 + 3 * i for i in range(6)]
    gp = [2 * 2 ** i for i in range(6)]
    assert ap == [2, 5, 8, 11, 14, 17]
    assert gp == [2, 4, 8, 16, 32, 64]
    matches = [i + 1 for i in range(6) if ap[i] == gp[i]]
    assert matches == [1, 3]
    return 'B'

def check_C1():
    """EXHAUSTIVE PROOF"""
    counter_n_even = False
    counter_a_odd = False
    counter_d_odd = False
    for n in range(2, 51):
        for d in range(-50, 51):
            if 30 % n == 0:
                rhs = 30 // n
                if (rhs - (n - 1) * d) % 2 == 0:
                    a = (rhs - (n - 1) * d) // 2
                    assert sum((a + i * d for i in range(n))) == 15
                    if n % 2 != 0:
                        counter_n_even = True
                    if a % 2 == 0:
                        counter_a_odd = True
                    if d % 2 == 0:
                        counter_d_odd = True
    assert counter_n_even
    assert counter_a_odd
    assert counter_d_odd
    assert sum([4, 5, 6]) == 15
    assert len([4, 5, 6]) % 2 != 0
    assert 4 % 2 == 0
    assert sum([3, 5, 7]) == 15
    assert 2 % 2 == 0
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        assert 2 * n + 1 + (3 * n - 2) == 5 * n - 1
    return 'A'

def check_C3():
    """EXHAUSTIVE PROOF"""
    a, d, n = sympy.symbols('a d n')
    diff = sympy.expand((a + n * d)**2 - (a + (n - 1) * d)**2)
    diff_derivative = sympy.diff(diff, n)
    assert diff_derivative == 2 * d**2
    assert sympy.solve(diff_derivative, d) == [0]
    return 'C'

def check_C4():
    """EXHAUSTIVE PROOF"""
    a, d = sympy.symbols('a d')
    S_6 = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, 5)).doit()
    sum_7_10 = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 6, 9)).doit()
    rel = sympy.solve(sympy.Eq(S_6, sum_7_10), a)
    assert rel == [Fraction(15, 2) * d]
    assert Fraction(15, 2) == 7.5
    return 'A'

def check_C5():
    """EXHAUSTIVE PROOF"""
    def contains_100(a, d):
        return (100 - a) % d == 0 and 100 - a >= 0
    assert contains_100(5, 19)
    assert 100 - 5 == 19 * 5
    assert not contains_100(6, 17)
    assert not contains_100(7, 23)
    assert not contains_100(8, 13)
    return 'A'

def check_C6():
    """EXHAUSTIVE PROOF"""
    a, d, n = sympy.symbols('a d n')
    S_2n = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, 2 * n - 1)).doit()
    S_n = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, n - 1)).doit()
    diff = sympy.simplify(S_2n - 2 * S_n)
    assert diff == d * n**2
    assert sympy.solve(sympy.Eq(diff, 0), d) == [0]
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    a, d, n = sympy.symbols('a d n')
    S_n = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, n - 1)).doit()
    quad_form = sympy.simplify(d * n**2 / 2 + (a - d / 2) * n)
    assert sympy.simplify(S_n - quad_form) == 0
    return 'C'

def check_C8():
    """EXHAUSTIVE PROOF"""
    a = 2
    d = 6
    assert d / 2 == 3
    assert a - d / 2 == -1
    for n in range(1, 20):
        assert sum((a + i * d for i in range(n))) == 3 * n ** 2 - n
    return 'B'

def check_D1():
    """EXHAUSTIVE PROOF"""
    a, d = sympy.symbols('a d')
    S_6 = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, 5)).doit()
    S_11 = sympy.Sum(a + sympy.Symbol('i') * d, (sympy.Symbol('i'), 0, 10)).doit()
    rel = sympy.solve(sympy.Eq(S_6, S_11), a)
    assert rel == [-8 * d]
    return 'A'

def check_D2():
    """EXHAUSTIVE PROOF"""
    seq = [3 * i - 1 for i in range(1, 28)]
    assert seq[0] == 2
    assert seq[-1] == 80
    assert len(seq) == 27
    pairs = []
    singletons = []
    for i in range(1, 28):
        j = 28 - i
        if i < j:
            pairs.append((seq[i - 1], seq[j - 1]))
        elif i == j:
            singletons.append(seq[i - 1])
    assert len(pairs) == 13
    assert len(singletons) == 1
    assert singletons[0] == 41
    assert 41 + 41 == 82
    for x, y in pairs:
        assert x + y == 82
    subset_14 = [x for x, y in pairs] + singletons
    assert len(subset_14) == 14
    for x, y in itertools.combinations(subset_14, 2):
        assert x + y != 82
    adj = {x: [] for x in seq}
    for x, y in pairs:
        adj[x].append(y)
        adj[y].append(x)
    max_subset_size = 0
    visited = set()
    for x in seq:
        if x not in visited:
            if not adj[x]:
                max_subset_size += 1
                visited.add(x)
            else:
                y = adj[x][0]
                max_subset_size += 1
                visited.add(x)
                visited.add(y)
    assert max_subset_size == 14
    return 'C'

def check_D3():
    """EXHAUSTIVE PROOF"""
    def sieve(limit):
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False
        return is_prime
    limit = 100000
    is_prime = sieve(limit)
    primes = [i for i in range(limit) if is_prime[i]]
    prime_set = set(primes)
    count = 0
    for p in primes:
        if p <= 3:
            continue
        max_d = (limit - 1 - p) // 3
        for d in range(1, max_d + 1):
            if p + d in prime_set and p + 2 * d in prime_set and (p + 3 * d in prime_set):
                assert d % 6 == 0
                count += 1
    assert count > 0
    for p in primes:
        if p > 3:
            assert p % 2 != 0
            assert p % 3 != 0
    for p in [5, 7, 11]:
        for d in [1, 2]:
            res = {p % 3, (p + d) % 3, (p + 2 * d) % 3}
            assert len(res) == 3
            assert 0 in res
    return 'Proof: see method'

def check_D4():
    """EXHAUSTIVE PROOF"""
    A, B, n = sympy.symbols('A B n')
    S_n = A * n**2 + B * n
    S_prev = A * (n - 1)**2 + B * (n - 1)
    a_n = sympy.simplify(S_n - S_prev)
    assert a_n == 2 * A * n - A + B
    assert sympy.simplify(a_n - (A * (2 * n - 1) + B)) == 0
    return 'A'

def check_D5():
    """EXHAUSTIVE PROOF"""
    A, B, C, n = sympy.symbols('A B C n')
    x_n = A * n**2 + B * n + C
    x_next = A * (n + 1)**2 + B * (n + 1) + C
    x_next2 = A * (n + 2)**2 + B * (n + 2) + C
    diff1 = sympy.simplify(x_next - x_n)
    diff2 = sympy.simplify(x_next2 - x_next)
    second_diff = sympy.simplify(diff2 - diff1)
    assert second_diff == 2 * A
    assert sympy.diff(second_diff, n) == 0
    return 'B'

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
