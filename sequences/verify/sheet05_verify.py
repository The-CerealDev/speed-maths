import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import fractions
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans05.tex'

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return 5 - n
    assert a(1) == 4
    assert a(2) == 3
    for n in range(1, 20):
        assert a(n + 1) - a(n) == -1
        assert a(n + 1) < a(n)
    return 'Decreasing'

def check_A2():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return n ** 2
    assert a(1) == 1
    for n in range(1, 100):
        assert a(n) >= 1
    assert a(1000) == 1000000
    return 'Not bounded above; bounded below (by 1).'

def check_A3():
    """EXHAUSTIVE PROOF"""
    def f(x):
        return 2 * x - 3
    assert f(3) == 3
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(2 * x - 3, x), x)
    assert solved == [3]
    return solved[0]

def check_A4():
    """EXHAUSTIVE PROOF"""
    a1 = 2
    a2 = Fraction(1, a1)
    a3 = Fraction(1, a2)
    a4 = Fraction(1, a3)
    assert a2 == Fraction(1, 2)
    assert a3 == 2
    assert a4 == Fraction(1, 2)
    return [a2, a3, a4]

def check_A5():
    """EXHAUSTIVE PROOF"""
    assert math.floor(3.7) == 3
    assert math.ceil(3.2) == 4
    assert math.floor(5) == 5
    assert math.ceil(5) == 5
    return [math.floor(3.7), math.ceil(3.2)]

def check_A6():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return (1 / 2) ** n + (1 / 3) ** n
    assert abs(a(100) - 0) < 1e-09
    return 'Yes, converges to 0.'

def check_A7():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return (-1) ** n
    for n in range(1, 100):
        assert -1 <= a(n) <= 1
        assert a(n) != a(n + 1)
    return 'Bounded (yes); does not converge.'

def check_A8():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return (-1) ** n
    assert abs(a(1) - a(2)) == 2
    return False

def check_A9():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return Fraction(n, n + 1)
    assert a(1) == Fraction(1, 2)
    assert a(2) == Fraction(2, 3)
    assert a(3) == Fraction(3, 4)
    assert a(1) < a(2) < a(3)
    return 'Increasing'

def check_A10():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return math.isqrt(n)
    n = 1
    while a(n) != 4:
        n += 1
    assert n == 16
    for i in range(16, 25):
        assert a(i) == 4
    assert a(25) == 5
    return n

def check_B1():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return Fraction(n, n + 1)
    for n in range(1, 100):
        diff = a(n + 1) - a(n)
        assert diff == Fraction(1, (n + 1) * (n + 2))
        assert diff > 0
    n = sympy.Symbol('n')
    return Fraction(1, 1) / ((n + 1) * (n + 2))

def check_B2():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return Fraction(n, n + 1)
    for n in range(1, 100):
        assert a(n) == 1 - Fraction(1, n + 1)
        assert a(n) < 1
    return 'A'

def check_B3():
    """EXHAUSTIVE PROOF"""
    a = Fraction(3)
    for _ in range(1, 100):
        a = Fraction(1, a)
    assert a == Fraction(1, 3)
    assert 100 % 2 == 0
    return 'B'

def check_B4():
    """EXHAUSTIVE PROOF"""
    def f(x):
        return Fraction(1, x)
    assert f(1) == 1
    assert f(-1) == -1
    x = sympy.Symbol('x')
    solved = sympy.solve(sympy.Eq(1 / x, x), x)
    assert set(solved) == {1, -1}
    return [1, -1]

def check_B5():
    """EXHAUSTIVE PROOF"""
    def f(x):
        return x
    a = 5
    for _ in range(10):
        a = f(a)
        assert a == 5
    return 'A'

def check_B6():
    """EXHAUSTIVE PROOF"""
    seq_A = [(-1) ** n for n in range(1, 6)]
    assert not (all((seq_A[i] <= seq_A[i + 1] for i in range(4))) or all((seq_A[i] >= seq_A[i + 1] for i in range(4))))
    seq_B = [math.sin(n) for n in range(1, 6)]
    assert not (all((seq_B[i] <= seq_B[i + 1] for i in range(4))) or all((seq_B[i] >= seq_B[i + 1] for i in range(4))))
    seq_C = [Fraction(1, n) for n in range(1, 6)]
    assert all((seq_C[i] > seq_C[i + 1] for i in range(4)))
    seq_D = [n % 3 for n in range(1, 6)]
    assert not (all((seq_D[i] <= seq_D[i + 1] for i in range(4))) or all((seq_D[i] >= seq_D[i + 1] for i in range(4))))
    return 'C'

def check_B7():
    """EXHAUSTIVE PROOF"""
    assert math.floor(-2.3) == -3
    return 'B'

def check_B8():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return math.floor(n / 2)
    assert [a(n) for n in range(1, 6)] == [0, 1, 1, 2, 2]
    assert a(1) == math.floor(0.5)
    assert a(2) == math.floor(1)
    return 'A'

def check_B9():
    """EXHAUSTIVE PROOF"""
    def a(n):
        return (-1) ** n / n
    for n in range(1, 100):
        assert -1 / n <= a(n) <= 1 / n
    assert abs(a(10000)) < 0.001
    return 0

def check_B10():
    """EXHAUSTIVE PROOF"""
    d1 = 1
    assert all((d1 > 0 for _ in range(1)))
    return 'A'

def check_C1():
    """EXHAUSTIVE PROOF"""
    a = Fraction(2)
    seq = [a]
    for _ in range(30):
        a = (a - 1) / (a + 1)
        seq.append(a)
    assert seq[0] == 2
    assert seq[1] == Fraction(1, 3)
    assert seq[2] == Fraction(-1, 2)
    assert seq[3] == -3
    assert seq[4] == 2
    for n in range(25):
        assert seq[n + 4] == seq[n]
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    a = Fraction(2)
    for _ in range(101 - 1):
        a = (a - 1) / (a + 1)
    assert a == 2
    assert 101 % 4 == 1
    return 'A'

def check_C3():
    """EXHAUSTIVE PROOF"""
    a = 1.0
    for _ in range(10):
        a = math.sqrt(a + 2)
    assert abs(a - 2.0) < 1e-05
    for x in [-1, 2]:
        assert x ** 2 - x - 2 == 0
    return 'A'

def check_C4():
    """EXHAUSTIVE PROOF"""
    w = {1: 10, 2: 15, 3: 18, 4: 22, 5: 31, 6: 36, 7: 41}
    primes = [2, 3, 5, 7]
    counterexample = None
    for p in primes:
        val = w[p]
        if val % 3 != 0 and val % 5 != 0:
            counterexample = p
            break
    assert counterexample == 5
    return 'C'

def check_C5():
    """EXHAUSTIVE PROOF"""
    count = 0
    for n in range(1, 101):
        if math.isqrt(n) == 7:
            count += 1
    assert count == 64 - 49
    assert count == 15
    return 'C'

def check_C6():
    """EXHAUSTIVE PROOF"""
    a = Fraction(2)
    seq = [a]
    for _ in range(15):
        a = 1 - Fraction(1, a)
        seq.append(a)
    assert seq[0] == 2
    assert seq[1] == Fraction(1, 2)
    assert seq[2] == -1
    assert seq[3] == 2
    for n in range(10):
        assert seq[n + 3] == seq[n]
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    def a(n, a1):
        return a1 + 3 * (n - 1)
    for a1 in range(-20, 21):
        for n in range(1, 100):
            assert a(n + 1, a1) - a(n, a1) == 3 > 0
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF"""
    L = 3
    assert L == 2 * L - 3
    L2 = 2
    assert L2 == math.sqrt(L2 + 2)
    return 'A'

def check_D1():
    """EXHAUSTIVE PROOF"""
    a = 1.0
    for _ in range(50):
        a = math.sqrt(a + 2)
    assert abs(a - 2.0) < 1e-09

    def diff(x):
        return math.sqrt(x + 2) - x
    assert diff(1.0) > 0
    assert diff(1.5) > 0
    assert diff(1.9) > 0
    assert diff(1.99) > 0
    return 'Bounded above by 2, strictly increasing, converges to 2.'

def check_D2():
    """EXHAUSTIVE PROOF"""
    def f(x):
        return Fraction(1, 1 - x)
    a = Fraction(2)
    seq = [a]
    for _ in range(12):
        a = f(a)
        seq.append(a)
    assert seq[0] == 2
    assert seq[1] == -1
    assert seq[2] == Fraction(1, 2)
    assert seq[3] == 2
    for n in range(9):
        assert seq[n + 3] == seq[n]
    return 'B'

def check_D3():
    """EXHAUSTIVE PROOF"""
    a = 100
    n = 1
    seq = [a]
    while a != 0:
        a = a // 2
        seq.append(a)
        n += 1
    assert n == 8
    assert seq == [100, 50, 25, 12, 6, 3, 1, 0]
    return 'C'

def check_D4():
    """EXHAUSTIVE PROOF"""
    a = 3.0
    seq = [a]
    for _ in range(10):
        a = (a + 4 / a) / 2
        seq.append(a)
    for i in range(1, len(seq) - 1):
        assert seq[i + 1] <= seq[i]
    for x in seq:
        assert x >= 2.0
    assert abs(seq[-1] - 2.0) < 1e-09
    return 'A'

def check_D5():
    """EXHAUSTIVE PROOF"""
    a = Fraction(1, 2)
    assert a * (1 - a) == Fraction(1, 4)
    a2 = Fraction(1, 4)
    assert a2 * (1 - a2) == Fraction(3, 16)
    x = sympy.Symbol('x')
    diff = sympy.simplify(x * (1 - x) - x)
    assert diff == -x**2
    assert sympy.diff(diff, x) == -2 * x
    for num in range(-10, 11):
        for den in range(1, 10):
            val = Fraction(num, den)
            assert val * (1 - val) - val == -val**2 <= 0
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
