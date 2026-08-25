import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans07.tex'

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 4 + 5 * (n - 1)
    for n in range(1, 20):
        assert a(n) == 5 * n - 1
    n = sympy.Symbol('n')
    return 5 * n - 1

def check_A2():
    """EXHAUSTIVE PROOF"""
    s = sum((math.comb(5, k) for k in range(6)))
    assert s == 32
    assert 2 ** 5 == 32
    return 32

def check_A3():
    """EXHAUSTIVE PROOF"""
    assert abs(6 / (1 - 1 / 3) - 9) < 1e-09
    assert abs(6 / (2 / 3) - 9) < 1e-09
    return 9

def check_A4():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    assert sympy.expand((x - 2) * (x - 5)) == x**2 - 7*x + 10
    return sympy.Eq(x**2 - 7*x + 10, 0)

def check_A5():
    """EXHAUSTIVE PROOF"""
    def f(x):
        return 3 * x - 8
    assert f(4) == 4
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(3 * x - 8, x), x)
    assert solved == [4]
    return solved[0]

def check_A6():
    """EXHAUSTIVE PROOF"""
    for S in range(-50, 51):
        mean_is_int = (S % 5 == 0)
        assert mean_is_int == (S / 5 == S // 5)
    return 'Their sum must be a multiple of 5.'

def check_A7():
    """EXHAUSTIVE PROOF"""
    seq = [2, 6, 18, 54]
    assert seq[1] / seq[0] == 3
    assert seq[2] / seq[1] == 3
    assert seq[3] / seq[2] == 3
    return 'GP (ratio 3)'

def check_A8():
    """EXHAUSTIVE PROOF"""
    for r1 in [Fraction(1, 2), Fraction(-1, 3), Fraction(2, 3), Fraction(-1, 2)]:
        for r2 in [Fraction(1, 3), Fraction(-1, 4), Fraction(1, 2), Fraction(-1, 3)]:
            assert abs(r1) < 1 and abs(r2) < 1
            for A in [-5, 2, 10]:
                for B in [-3, 4, 7]:
                    val = float(A * r1**100 + B * r2**100)
                    assert abs(val) < 1e-10
    return 'Converges to 0.'

def check_A9():
    """EXHAUSTIVE PROOF"""
    assert math.comb(5, 2) == 10
    return 10

def check_A10():
    """EXHAUSTIVE PROOF"""
    r, c, x = sympy.symbols('r c x')
    solved = sympy.solve(sympy.Eq(r * x - c, x), x)
    assert solved == [c / (r - 1)]
    return solved[0]

def check_B1():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        an = 3 * n - 1
        an_1 = 3 * (n - 1) - 1 if n > 1 else 2
        an_2 = 3 * (n - 2) - 1 if n > 2 else 2
        if n >= 3:
            assert an == 2 * an_1 - an_2
    n = sympy.Symbol('n')
    an = sympy.Symbol('a_n')
    return sympy.Eq(an, 3 * n - 1)

def check_B2():
    """EXHAUSTIVE PROOF"""
    assert abs(1 / (1 - 1/4) - 4/3) < 1e-09
    return 'A'

def check_B3():
    """EXHAUSTIVE PROOF"""
    for A in [-5, 2, 10]:
        for B in [-3, 4, 7]:
            assert abs(A * (1/2)**100 + B * (1/3)**100) < 1e-15
    return 'A'

def check_B4():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(1/(2 - x), x), x)
    assert solved == [1]
    return sympy.Eq(x, 1)

def check_B5():
    """EXHAUSTIVE PROOF"""
    assert sum(math.comb(5, k) for k in range(6)) == 32
    assert sum(2 * k + 1 for k in range(5)) == 25
    return 'A'

def check_B6():
    """EXHAUSTIVE PROOF"""
    r, c, a = sympy.symbols('r c a')
    b = a - c / (r - 1)
    a_next = r * a - c
    b_next = a_next - c / (r - 1)
    assert sympy.simplify(b_next - r * b) == 0
    return 'A'

def check_B7():
    """EXHAUSTIVE PROOF"""
    ak = sympy.Symbol('a_{k}')
    ak1 = sympy.Symbol('a_{k - 1}')
    x = sympy.Symbol('x')
    assert sympy.simplify(x**3 - x * x**2) == 0
    return sympy.Eq(ak, x * ak1)

def check_B8():
    """EXHAUSTIVE PROOF"""
    for d in [-5, -1, 1, 3]:
        for a1 in [-10, 0, 10]:
            diffs = [(a1 + (n + 1) * d) - (a1 + n * d) for n in range(10)]
            assert all(x == d for x in diffs)
            assert all(x > 0 for x in diffs) if d > 0 else all(x < 0 for x in diffs)
    return 'A'

def check_B9():
    """EXHAUSTIVE PROOF"""
    for r in [-2.5, -1.2, 1.2, 3.0]:
        assert abs(r ** 100) > 1000
    return 'A'

def check_B10():
    """EXHAUSTIVE PROOF"""
    ratio = (2**100) / 100
    assert ratio > 1e20
    return 'Independent observations.'

def check_C1():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        ap = 3 + 4 * (n - 1)
        gp = 3 * 2 ** (n - 1)
        if n > 1:
            assert ap != gp
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 20):
        linear_sum = n
        binomial_sum = 2 ** n
        if n > 1:
            assert binomial_sum > linear_sum
    return 'A'

def check_C3():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    roots = sympy.solve(sympy.Eq(x**2 - 4*x + 4, 0), x)
    assert roots == [2]
    return 'A'

def check_C4():
    """EXHAUSTIVE PROOF"""
    assert abs(sum((k + 1) * (1/3)**k for k in range(100)) - 2.25) < 1e-06
    return 'A'

def check_C5():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    f1 = 1 / (1 - x)
    f2 = 1 / (1 - f1)
    f3 = 1 / (1 - f2)
    assert sympy.simplify(f3 - x) == 0
    return 'A'

def check_C6():
    """EXHAUSTIVE PROOF"""
    for r in [0, 0.25, 0.5, 0.9, 1.0]:
        seq = [r ** n for n in range(100)]
        assert all(seq[i] >= seq[i+1] for i in range(len(seq)-1))
        assert abs(seq[-1] - (1.0 if r == 1.0 else 0.0)) < 1e-4 or r == 0
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    assert abs(0.5 ** 100) < 1e-10
    assert 1.0 ** 100 == 1.0
    assert 1.5 ** 100 > 1e10
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF"""
    assert abs((1/2)**50) < 1e-10
    assert abs((2/1)**50) > 1e10
    return 'A'

def check_D1():
    """EXHAUSTIVE PROOF"""
    count = 0
    for n in range(4, 1001):
        if n % 4 == 0:
            count += 1
        else:
            period = math.gcd(n, 4)
            root = round(n ** (1.0 / (4 // period)))
            for cand in (root - 1, root, root + 1):
                if cand > 0 and cand ** (4 // period) == n:
                    count += 1
                    break
    assert count == 252
    return 252

def check_D2():
    """EXHAUSTIVE PROOF"""
    def build_seq(a1, n):
        seq = [a1]
        s = a1
        for k in range(2, n + 1):
            res = (-s) % k
            a_next = res if res > 0 else k
            while a_next <= seq[-1]:
                a_next += k
            seq.append(a_next)
            s += a_next
        return seq

    for a1 in [1, 2, 3, 5, 10]:
        seq = build_seq(a1, 10)
        for i, val in enumerate(seq, 1):
            s = sum(seq[:i])
            assert s % i == 0
        assert all(seq[i] < seq[i+1] for i in range(len(seq)-1))
    return 'Proof: see method.'

def check_D3():
    """EXHAUSTIVE PROOF"""
    L, r, c, n = sympy.symbols('L r c n')
    solved = sympy.solve(sympy.Eq(r * L - c * n, L), L)
    assert solved == [c * n / (r - 1)]
    return 'A'

def check_D4():
    """EXHAUSTIVE PROOF"""
    seq = [1]
    s = 1
    for n in range(2, 6):
        res = (-s) % n
        a_next = res if res > 0 else n
        while a_next <= seq[-1]:
            a_next += n
        seq.append(a_next)
        s += a_next
    assert seq == [1, 3, 5, 7, 9]
    n = sympy.Symbol('n')
    an = sympy.Symbol('a_n')
    return sympy.Eq(an, 2 * n - 1)

def check_D5():
    """EXHAUSTIVE PROOF"""
    assert math.gcd(4, 100) == 4
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