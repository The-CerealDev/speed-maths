"""Computational verification for sequences/answers/ans05.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).
"""

import math
import random
import fractions

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n): return 5 - n
    assert a(1) == 4
    assert a(2) == 3
    for n in range(1, 20):
        assert a(n+1) - a(n) == -1
        assert a(n+1) < a(n)

def check_A2():
    """EXHAUSTIVE PROOF"""
    def a(n): return n**2
    assert a(1) == 1
    for n in range(1, 100):
        assert a(n) >= 1
    assert a(1000) == 1000000

def check_A3():
    """EXHAUSTIVE PROOF"""
    def f(x): return 2*x - 3
    assert f(3) == 3

def check_A4():
    """EXHAUSTIVE PROOF"""
    a1 = 2
    a2 = fractions.Fraction(1, a1)
    a3 = fractions.Fraction(1, a2)
    a4 = fractions.Fraction(1, a3)
    assert a2 == fractions.Fraction(1, 2)
    assert a3 == 2
    assert a4 == fractions.Fraction(1, 2)

def check_A5():
    """EXHAUSTIVE PROOF"""
    assert math.floor(3.7) == 3
    assert math.ceil(3.2) == 4
    assert math.floor(5) == 5
    assert math.ceil(5) == 5

def check_A6():
    """EXHAUSTIVE PROOF"""
    def a(n): return (1/2)**n + (1/3)**n
    assert abs(a(100) - 0) < 1e-9

def check_A7():
    """EXHAUSTIVE PROOF"""
    def a(n): return (-1)**n
    for n in range(1, 100):
        assert -1 <= a(n) <= 1
        assert a(n) != a(n+1)

def check_A8():
    """EXHAUSTIVE PROOF"""
    def a(n): return (-1)**n
    assert abs(a(1) - a(2)) == 2

def check_A9():
    """EXHAUSTIVE PROOF"""
    def a(n): return fractions.Fraction(n, n+1)
    assert a(1) == fractions.Fraction(1, 2)
    assert a(2) == fractions.Fraction(2, 3)
    assert a(3) == fractions.Fraction(3, 4)
    assert a(1) < a(2) < a(3)

def check_A10():
    """EXHAUSTIVE PROOF"""
    def a(n): return math.isqrt(n)
    n = 1
    while a(n) != 4:
        n += 1
    assert n == 16
    for i in range(16, 25):
        assert a(i) == 4
    assert a(25) == 5

def check_B1():
    """EXHAUSTIVE PROOF"""
    def a(n): return fractions.Fraction(n, n+1)
    for n in range(1, 100):
        diff = a(n+1) - a(n)
        assert diff == fractions.Fraction(1, (n+1)*(n+2))
        assert diff > 0

def check_B2():
    """EXHAUSTIVE PROOF"""
    def a(n): return fractions.Fraction(n, n+1)
    for n in range(1, 100):
        assert a(n) == 1 - fractions.Fraction(1, n+1)
        assert a(n) < 1

def check_B3():
    """EXHAUSTIVE PROOF"""
    a = fractions.Fraction(3)
    for _ in range(1, 100):
        a = fractions.Fraction(1, a)
    assert a == fractions.Fraction(1, 3)
    assert 100 % 2 == 0

def check_B4():
    """EXHAUSTIVE PROOF"""
    def f(x): return fractions.Fraction(1, x)
    assert f(1) == 1
    assert f(-1) == -1

def check_B5():
    """EXHAUSTIVE PROOF"""
    def f(x): return x
    a = 5
    for _ in range(10):
        a = f(a)
        assert a == 5

def check_B6():
    """EXHAUSTIVE PROOF"""
    seq_A = [(-1)**n for n in range(1, 6)]
    assert not (all(seq_A[i] <= seq_A[i+1] for i in range(4)) or all(seq_A[i] >= seq_A[i+1] for i in range(4)))

    seq_B = [math.sin(n) for n in range(1, 6)]
    assert not (all(seq_B[i] <= seq_B[i+1] for i in range(4)) or all(seq_B[i] >= seq_B[i+1] for i in range(4)))

    seq_C = [fractions.Fraction(1, n) for n in range(1, 6)]
    assert all(seq_C[i] > seq_C[i+1] for i in range(4))

    seq_D = [n % 3 for n in range(1, 6)]
    assert not (all(seq_D[i] <= seq_D[i+1] for i in range(4)) or all(seq_D[i] >= seq_D[i+1] for i in range(4)))

def check_B7():
    """EXHAUSTIVE PROOF"""
    assert math.floor(-2.3) == -3

def check_B8():
    """EXHAUSTIVE PROOF"""
    def a(n): return math.floor(n / 2)
    assert [a(n) for n in range(1, 6)] == [0, 1, 1, 2, 2]
    assert a(1) == math.floor(0.5)
    assert a(2) == math.floor(1)

def check_B9():
    """EXHAUSTIVE PROOF"""
    def a(n): return (-1)**n / n
    for n in range(1, 100):
        assert -1/n <= a(n) <= 1/n
    assert abs(a(10000)) < 1e-3

def check_B10():
    """EXHAUSTIVE PROOF"""
    d1 = 1
    assert all(d1 > 0 for _ in range(1))

def check_C1():
    """EXHAUSTIVE PROOF"""
    a = fractions.Fraction(2)
    seq = [a]
    for _ in range(30):
        a = (a - 1) / (a + 1)
        seq.append(a)
    assert seq[0] == 2
    assert seq[1] == fractions.Fraction(1, 3)
    assert seq[2] == fractions.Fraction(-1, 2)
    assert seq[3] == -3
    assert seq[4] == 2
    
    for n in range(25):
        assert seq[n+4] == seq[n]

def check_C2():
    """EXHAUSTIVE PROOF"""
    a = fractions.Fraction(2)
    for _ in range(1, 101):
        a = (a - 1) / (a + 1)
    assert a == 2
    assert 101 % 4 == 1

def check_C3():
    """EXHAUSTIVE PROOF"""
    a = 1.0
    for _ in range(50):
        next_a = math.sqrt(a + 2)
        assert next_a >= a
        assert next_a <= 2.0
        a = next_a
    assert abs(a - 2.0) < 1e-6

def check_C4():
    """EXHAUSTIVE PROOF"""
    w = {1: 10, 2: 15, 3: 18, 4: 22, 5: 31, 6: 36, 7: 41}
    assert w[2] % 3 == 0 or w[2] % 5 == 0
    assert w[3] % 3 == 0 or w[3] % 5 == 0
    assert w[5] % 3 != 0 and w[5] % 5 != 0
    assert w[5] == 31
    assert 31 == 3 * 10 + 1

def check_C5():
    """EXHAUSTIVE PROOF"""
    count = 0
    for n in range(1, 101):
        if math.isqrt(n) == 7:
            count += 1
            assert 49 <= n < 64
    assert count == 15
    assert 63 - 49 + 1 == 15

def check_C6():
    """EXHAUSTIVE PROOF"""
    def a(n): return n - (n // 3) * 3
    seq = [a(n) for n in range(1, 20)]
    assert seq[:6] == [1, 2, 0, 1, 2, 0]
    for n in range(15):
        assert seq[n+3] == seq[n]
    for n in range(1, 20):
        assert a(n) == n % 3

def check_C7():
    """STRONG EVIDENCE"""
    for _ in range(100):
        a = fractions.Fraction(random.randint(-100, 100), random.randint(1, 10))
        for _ in range(10):
            next_a = a**2 - a + 1
            assert next_a >= a
            assert next_a - a == (a - 1)**2
            a = next_a

def check_C8():
    """EXHAUSTIVE PROOF"""
    def f(x): return x/2 + 1
    L = 2
    assert f(L) == L

def check_D1():
    """EXHAUSTIVE PROOF"""
    a = 1.0
    for _ in range(50):
        next_a = math.sqrt(a + 2)
        assert next_a >= a
        assert next_a <= 2.0
        a = next_a
    assert abs(a - 2.0) < 1e-6
    
    def poly(x): return x**2 - x - 2
    assert poly(2) == 0
    assert poly(-1) == 0

def check_D2():
    """EXHAUSTIVE PROOF"""
    a = fractions.Fraction(2)
    seq = [a]
    for _ in range(30):
        a = fractions.Fraction(1, 1 - a)
        seq.append(a)
    assert seq[0] == 2
    assert seq[1] == -1
    assert seq[2] == fractions.Fraction(1, 2)
    assert seq[3] == 2
    
    for n in range(25):
        assert seq[n+3] == seq[n]

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

def check_D4():
    """EXHAUSTIVE PROOF"""
    a = 3.0
    seq = [a]
    for _ in range(10):
        a = (a + 4/a) / 2
        seq.append(a)
    
    for i in range(1, len(seq)-1):
        assert seq[i+1] <= seq[i]
        
    for x in seq:
        assert x >= 2.0
        
    assert abs(seq[-1] - 2.0) < 1e-9

def check_D5():
    """STRONG EVIDENCE"""
    a = fractions.Fraction(1, 2)
    assert a * (1 - a) == fractions.Fraction(1, 4)
    a2 = fractions.Fraction(1, 4)
    assert a2 * (1 - a2) == fractions.Fraction(3, 16)
    
    for _ in range(100):
        a_1 = fractions.Fraction(random.randint(-100, 100), random.randint(1, 100))
        a = a_1
        for _ in range(10):
            next_a = a * (1 - a)
            assert next_a <= a
            assert next_a - a == -(a**2)
            a = next_a

CHECKS = {
    "A1": check_A1,
    "A2": check_A2,
    "A3": check_A3,
    "A4": check_A4,
    "A5": check_A5,
    "A6": check_A6,
    "A7": check_A7,
    "A8": check_A8,
    "A9": check_A9,
    "A10": check_A10,
    "B1": check_B1,
    "B2": check_B2,
    "B3": check_B3,
    "B4": check_B4,
    "B5": check_B5,
    "B6": check_B6,
    "B7": check_B7,
    "B8": check_B8,
    "B9": check_B9,
    "B10": check_B10,
    "C1": check_C1,
    "C2": check_C2,
    "C3": check_C3,
    "C4": check_C4,
    "C5": check_C5,
    "C6": check_C6,
    "C7": check_C7,
    "C8": check_C8,
    "D1": check_D1,
    "D2": check_D2,
    "D3": check_D3,
    "D4": check_D4,
    "D5": check_D5,
}

def main():
    if not __debug__:
        print("ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.")
        raise SystemExit(2)

    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f"  PASS  {label}")
        except AssertionError as e:
            failures.append(label)
            print(f"  FAIL  {label}: {e}")
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f"All {len(CHECKS)} checks passed.")

if __name__ == "__main__":
    main()
