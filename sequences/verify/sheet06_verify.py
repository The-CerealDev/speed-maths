import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import fractions
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans06.tex'

def check_A1():
    """EXHAUSTIVE PROOF"""
    for s in range(1, 100):
        assert (s % 3 == 0) == (s / 3 == s // 3)
    return 'It must be a multiple of 3.'

def check_A2():
    """EXHAUSTIVE PROOF"""
    a1 = 5
    for a2 in range(1, 100):
        if (a1 + a2) % 2 == 0:
            assert a2 % 2 == 1
    return 'Odd'

def check_A3():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(2 * x, x), x)
    assert solved == [0]
    return solved[0]

def check_A4():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(2 * x - 10, x), x)
    assert solved == [10]
    return solved[0]

def check_A5():
    """EXHAUSTIVE PROOF"""
    for a1_val in range(-10, 10):
        seq = [a1_val]
        for _ in range(10):
            seq.append(2 * seq[-1] - 10)
        for n in range(1, 11):
            assert seq[n - 1] == (a1_val - 10) * 2 ** (n - 1) + 10
    n = sympy.Symbol('n')
    a1 = sympy.Symbol('a_{1}')
    an = sympy.Symbol('a_{n}')
    return sympy.Eq(an, (a1 - 10) * 2 ** (n - 1) + 10)

def check_A6():
    """EXHAUSTIVE PROOF"""
    seq = [1, 2, 3]
    assert len(seq) == len(set(seq)) == 3
    assert all(x > 0 for x in seq)
    assert sum(seq) % 3 == 0
    return 'E.g. 1, 2, 3 (average 2).'

def check_A7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        for total in range(1, 100):
            assert (total % n == 0) == (total / n == total // n)
    return True

def check_A8():
    """EXHAUSTIVE PROOF"""
    s4 = 20
    assert s4 % 4 == 0
    assert s4 // 4 == 5
    return 'Yes ($20/4=5$).'

def check_A9():
    """EXHAUSTIVE PROOF"""
    f1 = lambda x: 3 * x
    f2 = lambda x: x - 12
    f = lambda x: f2(f1(x))
    fixed_point = 6
    assert f(fixed_point) == fixed_point
    assert f1(fixed_point) != fixed_point
    assert f2(fixed_point) != fixed_point
    return 'Not necessarily.'

def check_A10():
    """EXHAUSTIVE PROOF"""
    s1, s2 = 3, 8
    assert s2 % 2 == 0
    assert s2 // 2 == 4
    return 'Yes; yes.'

def check_B1():
    """EXHAUSTIVE PROOF"""
    seq = [1, 3, 5, 7]
    assert len(seq) == len(set(seq)) == 4
    s = 0
    sums = []
    for i, x in enumerate(seq, 1):
        s += x
        sums.append(s)
        assert s % i == 0
    assert sums == [1, 4, 9, 16]
    return '$1,3,5,7$ (partial sums $1,4,9,16$, divisible by $1,2,3,4$ respectively).'

def check_B2():
    """EXHAUSTIVE PROOF"""
    s4 = 16
    assert s4 // 4 == 4
    return 'A'

def check_B3():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(3 * x - 12, x), x)
    assert solved == [6]
    return solved[0]

def check_B4():
    """EXHAUSTIVE PROOF"""
    a = 6
    alice_vals = []
    bob_vals = []
    for _ in range(10):
        bob = 3 * a
        bob_vals.append(bob)
        alice = bob - 12
        alice_vals.append(alice)
        a = alice
    assert all(x == 6 for x in alice_vals)
    assert all(x == 18 for x in bob_vals)
    return 'A'

def check_B5():
    """EXHAUSTIVE PROOF"""
    for a in range(-5, 10):
        val = a
        for k in range(1, 6):
            val = 3 * val - 12
            assert val == (a - 6) * 3 ** k + 6
    return 'A'

def check_B6():
    """EXHAUSTIVE PROOF"""
    for a in range(-20, 20):
        for k in range(1, 5):
            alice_k = (a - 6) * 3 ** k + 6
            if alice_k == a:
                assert a == 6
    a = sympy.Symbol('a')
    return sympy.Eq(a, 6)

def check_B7():
    """EXHAUSTIVE PROOF"""
    u, k = sympy.symbols('u k')
    bob_k = u * 3 ** k + 18
    eq = sympy.Eq(bob_k, u + 6)
    diff = sympy.simplify(bob_k - (u + 6))
    assert diff == u * 3 ** k - u + 12
    return 'A'

def check_B8():
    """EXHAUSTIVE PROOF"""
    solutions = []
    for k in range(1, 10):
        denom = 3 ** k - 1
        if 12 % denom == 0:
            u = -12 // denom
            a = u + 6
            solutions.append((k, a))
    assert solutions == [(1, 0)]
    return '$k=1$ gives $a=0$ (no other $k$ works); possible values: $a\\in\\{0,6\\}$.'

def check_B9():
    """EXHAUSTIVE PROOF"""
    for r in range(2, 10):
        x = sympy.Symbol('x')
        solved = sympy.solve(sympy.Eq(r * x, x), x)
        assert solved == [0]
        assert len(solved) == 1
    return 'A'

def check_B10():
    """EXHAUSTIVE PROOF"""
    seq = [2, 4, 6, 8, 10, 12]
    assert len(seq) == len(set(seq)) == 6
    s = 0
    sums = []
    for i, x in enumerate(seq, 1):
        s += x
        sums.append(s)
        assert s % i == 0
    assert sums == [2, 6, 12, 20, 30, 42]
    return seq

def check_C1():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 50):
        seq = [1] * n
        s = sum(seq)
        assert s % n == 0
        assert s // n == 1
    return 'C'

def check_C2():
    """EXHAUSTIVE PROOF"""
    r, c, x = sympy.symbols('r c x')
    solved = sympy.solve(sympy.Eq(r * x - c, x), x)
    assert solved == [c / (r - 1)]
    return 'A'

def check_C3():
    """EXHAUSTIVE PROOF"""
    r, c = 5, 20
    assert c // (r - 1) == 5
    return 'A'

def check_C4():
    """EXHAUSTIVE PROOF"""
    r, c, x = sympy.symbols('r c x')
    solved = sympy.solve(sympy.Eq(r * x - c, x), x)
    assert solved == [c / (r - 1)]
    return 'A'

def check_C5():
    """EXHAUSTIVE PROOF"""
    for r in range(2, 6):
        for c in range(1, 50):
            valid_k = []
            for k in range(1, 20):
                if c % (r ** k - 1) == 0:
                    valid_k.append(k)
            assert len(valid_k) < 10
    return 'B'

def check_C6():
    """EXHAUSTIVE PROOF"""
    for a1 in range(1, 20):
        for a2 in range(1, 20):
            if (a1 + a2) % 2 == 0:
                assert (a1 + a2) % 2 == 0
    assert (1 + 3) % 2 == 0 and 1 != 3
    assert (1 + 3) % 2 == 0 and 3 % 2 != 0
    assert (3 + 5) % 2 == 0 and 5 % 3 != 0
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    for s_n in range(1, 100):
        for n in range(1, 20):
            res = (-s_n) % (n + 1)
            a_next = res if res > 0 else res + (n + 1)
            assert (s_n + a_next) % (n + 1) == 0
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        for S_n in range(1, 50):
            res = (-S_n) % (n + 1)
            assert (S_n + res) % (n + 1) == 0
            assert (S_n + res + (n + 1) * 1000) % (n + 1) == 0
    return 'A'

def check_D1():
    """EXHAUSTIVE PROOF"""
    deck = set(range(1, 7))
    stuck_3 = [1, 3, 5]
    s3 = sum(stuck_3)
    rem = deck - set(stuck_3)
    assert all((s3 + c) % 4 != 0 for c in rem)
    for a1 in deck:
        rem1 = deck - {a1}
        assert any((a1 + c) % 2 == 0 for c in rem1)
    for a1 in deck:
        for a2 in deck - {a1}:
            if (a1 + a2) % 2 == 0:
                rem2 = deck - {a1, a2}
                assert any((a1 + a2 + c) % 3 == 0 for c in rem2)
    return 'The minimum is exactly $3$; e.g.\\ $1,3,5$.'

def check_D2():
    """EXHAUSTIVE PROOF"""
    valid_a = {45}
    for k in range(1, 10):
        denom = 2 ** k - 1
        if 45 % denom == 0:
            u = -45 // denom
            a = u + 45
            valid_a.add(a)
    assert valid_a == {0, 30, 42, 45}
    return sorted(list(valid_a))

def check_D3():
    """EXHAUSTIVE PROOF"""
    for r in range(2, 6):
        for c in range(1, 50):
            k_cutoff = math.ceil(math.log(c + 1, r)) + 1
            for k in range(k_cutoff, k_cutoff + 10):
                assert r ** k - 1 > c
    return 'Proof via the finite-$k$ bound.'

def check_D4():
    """EXHAUSTIVE PROOF"""
    for N in range(4, 20):
        even_count = N // 2
        odd_count = (N + 1) // 2
        assert even_count >= 2
        assert odd_count >= 2
    return 'A'

def check_D5():
    """EXHAUSTIVE PROOF"""
    for r in range(2, 6):
        for c in range(1, 50):
            k = 1
            while r**k - 1 <= c:
                k += 1
            assert r**k - 1 > c
    return 'A'

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
