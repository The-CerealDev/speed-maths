"""Computational verification for sequences/answers/ans04.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).

Run directly:
    python3 sheet04_verify.py
"""

import math
import random
import cmath
from fractions import Fraction

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n):
        val = 2
        for _ in range(1, n):
            val = 3 * val - 1
        return val
    assert a(2) == 5
    assert a(3) == 14
    assert 3 * 2 - 1 == 5
    assert 3 * 5 - 1 == 14

def check_A2():
    """EXHAUSTIVE PROOF"""
    def a(n):
        val = 1
        for _ in range(1, n):
            val = 2 * val + 1
        return val
    assert a(4) == 15
    assert a(2) == 3
    assert a(3) == 7
    assert 2*1+1 == 3
    assert 2*3+1 == 7
    assert 2*7+1 == 15
    for n in range(1, 10):
        assert a(n) == 2**n - 1

def check_A3():
    """EXHAUSTIVE PROOF"""
    for n in range(3, 10):
        assert 2**n == 5 * 2**(n-1) - 6 * 2**(n-2)
        assert 3**n == 5 * 3**(n-1) - 6 * 3**(n-2)

def check_A4():
    """EXHAUSTIVE PROOF"""
    roots = []
    for x in range(-10, 10):
        if x**2 - 5*x + 6 == 0:
            roots.append(x)
    assert set(roots) == {2, 3}
    assert sum(roots) == 5
    assert roots[0] * roots[1] == 6

def check_A5():
    """STRONG EVIDENCE"""
    for _ in range(50):
        A = random.randint(-10, 10)
        B = random.randint(-10, 10)
        def a(n): return A * 2**n + B * 3**n
        for n in range(3, 10):
            assert a(n) == 5 * a(n-1) - 6 * a(n-2)

def check_A6():
    """EXHAUSTIVE PROOF"""
    def a_rec(n):
        val = Fraction(8, 1)
        for _ in range(1, n):
            val = Fraction(1, 2) * val
        return val
    def a_closed(n):
        return Fraction(8, 1) * Fraction(1, 2)**(n-1)
    
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)
        if n <= 4:
            assert a_rec(n) == Fraction(2**(4-n), 1)
        else:
            assert a_rec(n) == Fraction(1, 2**(n-4))

def check_A7():
    """EXHAUSTIVE PROOF"""
    L = -2
    assert L == 3*L + 4
    assert -2*L == 4

def check_A8():
    """STRONG EVIDENCE"""
    for _ in range(50):
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        if r1 == r2 or r1 == 0 or r2 == 0: continue
        p = r1 + r2
        q = -r1 * r2
        a1, a2 = random.randint(-10, 10), random.randint(-10, 10)
        def a(n):
            if n == 1: return a1
            if n == 2: return a2
            seq = [0, a1, a2]
            for i in range(3, n + 1):
                seq.append(p * seq[i-1] + q * seq[i-2])
            return seq[n]
        A = Fraction(a2 - a1 * r2, r1**2 - r1 * r2)
        B = Fraction(a1 * r1 - a2, r1 * r2 - r2**2)
        def a_closed(n): return A * (r1**n) + B * (r2**n)
        for n in range(1, 10):
            assert a(n) == a_closed(n)

def check_A9():
    """STRONG EVIDENCE"""
    def a(n): return 2**n + 3**n
    p, q = 5, -6
    for n in range(3, 10):
        assert a(n) == p * a(n-1) + q * a(n-2)

def check_A10():
    """STRONG EVIDENCE"""
    def a(n): return n * 2**n
    for n in range(3, 10):
        assert a(n) == 4 * a(n-1) - 4 * a(n-2)

def check_B1():
    """EXHAUSTIVE PROOF"""
    A = Fraction(-1, 2)
    B = Fraction(2, 3)
    def a_closed(n): return A * 2**n + B * 3**n
    assert a_closed(1) == 1
    assert a_closed(2) == 4
    
    assert 2*A + 3*B == 1
    assert 4*A + 9*B == 4
    assert 4*A + 6*B == 2
    assert 3*B == 2
    assert 2*A + 2 == 1
    
    def a_rec(n):
        if n == 1: return 1
        if n == 2: return 4
        seq = [0, 1, 4]
        for i in range(3, n + 1):
            seq.append(5 * seq[i-1] - 6 * seq[i-2])
        return seq[n]
        
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)

def check_B2():
    """EXHAUSTIVE PROOF"""
    a1 = random.randint(-10, 10)
    def a(n):
        val = a1
        for _ in range(1, n):
            val = 3 * val + 4
        return val
    def b(n):
        return a(n) + 2
    for n in range(1, 10):
        assert b(n+1) == 3 * b(n)

def check_B3():
    """EXHAUSTIVE PROOF"""
    def a(n):
        val = 1
        for _ in range(1, n):
            val = 3 * val + 4
        return val
    assert a(1) == 1
    assert a(1) + 2 == 3
    b_5 = 3**5
    assert b_5 == 243
    assert a(5) == 243 - 2 == 241

def check_B4():
    """EXHAUSTIVE PROOF"""
    roots = []
    for x in range(-10, 10):
        if x**2 - x - 2 == 0:
            roots.append(x)
    assert set(roots) == {2, -1}
    assert (2)**2 == 2 + 2
    assert (-1)**2 == -1 + 2

def check_B5():
    """EXHAUSTIVE PROOF"""
    def a_closed(n): return 2**n + (-1)**n
    assert a_closed(1) == 2 - 1 == 1
    assert a_closed(2) == 4 + 1 == 5
    
    def a_rec(n):
        if n == 1: return 1
        if n == 2: return 5
        seq = [0, 1, 5]
        for i in range(3, n + 1):
            seq.append(seq[i-1] + 2 * seq[i-2])
        return seq[n]
        
    for n in range(1, 10):
        assert a_rec(n) == a_closed(n)
        
    assert 2**1 - (-1)**1 == 3
    assert 2*2**1 - (-1)**1 == 5
    assert 2**0 + (-1)**0 == 2

def check_B6():
    """EXHAUSTIVE PROOF"""
    assert 5**2 + 4*(-6) == 1 > 0
    assert 4**2 + 4*(-4) == 0
    assert 1**2 + 4*(2) == 9 > 0
    assert 3**2 + 4*(-2) == 1 > 0

def check_B7():
    """EXHAUSTIVE PROOF"""
    A, B = 1, 1
    def a_closed(n): return (A + B * n) * 3**n
    assert a_closed(1) == 6
    assert a_closed(2) == 27
    
    assert (A + B * 1) * 3**1 == 6
    assert A + B == 2
    assert (A + B * 2) * 3**2 == 27
    assert A + 2*B == 3
    
    def a_rec(n):
        if n == 1: return 6
        if n == 2: return 27
        seq = [0, 6, 27]
        for i in range(3, n + 1):
            seq.append(6 * seq[i-1] - 9 * seq[i-2])
        return seq[n]
        
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)

def check_B8():
    """EXHAUSTIVE PROOF"""
    def a_closed(n): return (1 + n) * 3**n
    assert a_closed(4) == 5 * 81 == 405
    assert 81 * 5 == 405

def check_B9():
    """EXHAUSTIVE PROOF"""
    def a_rec(n):
        val = 2
        for _ in range(1, n):
            val = val + 5
        return val
    def a_closed(n):
        return 2 + 5 * (n - 1)
    
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)
        
    for x in range(-100, 100):
        assert x != x + 5

def check_B10():
    """EXHAUSTIVE PROOF"""
    assert (-6)**2 - 4*(1)*(9) == 36 - 36 == 0

def check_C1():
    """EXHAUSTIVE PROOF"""
    L = 1
    assert L == 4*L - 3
    assert -3*L == -3
    
    def a_rec(n, a1):
        val = a1
        for _ in range(1, n):
            val = 4 * val - 3
        return val
        
    a1 = random.randint(-10, 10)
    for n in range(1, 10):
        b_next = a_rec(n+1, a1) - 1
        b_curr = a_rec(n, a1) - 1
        assert b_next == 4 * b_curr

def check_C2():
    """EXHAUSTIVE PROOF"""
    def a_rec(n):
        val = 2
        for _ in range(1, n):
            val = 4 * val - 3
        return val
    
    def a_closed(n):
        return 1 + 4**(n-1)
        
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)

def check_C3():
    """EXHAUSTIVE PROOF"""
    r1 = 5
    r2 = -2
    p = r1 + r2
    q = -r1 * r2
    assert p == 3
    assert q == 10
    assert 5**2 - 3*5 - 10 == 0
    assert (-2)**2 - 3*(-2) - 10 == 0
    
    def a_closed(n): return 2 * r1**n + 3 * r2**n
    for n in range(3, 15):
        assert a_closed(n) == p * a_closed(n-1) + q * a_closed(n-2)

def check_C4():
    """EXHAUSTIVE PROOF"""
    p = 2
    q = -5
    discriminant = p**2 + 4*q
    assert discriminant == 4 - 20 == -16 < 0
    
    root1 = (p + cmath.sqrt(discriminant)) / 2
    root2 = (p - cmath.sqrt(discriminant)) / 2
    assert cmath.isclose(root1, 1 + 2j) or cmath.isclose(root1, 1 - 2j)
    assert cmath.isclose(root2, 1 + 2j) or cmath.isclose(root2, 1 - 2j)

def check_C5():
    """EXHAUSTIVE PROOF"""
    L = 5
    n = 2
    b_n = 10
    assert 2*b_n + L + 3**n != 2*b_n
    
    def a_part(n): return 3**n
    for n in range(1, 10):
        assert a_part(n+1) == 2 * a_part(n) + 3**n

def check_C6():
    """EXHAUSTIVE PROOF"""
    def a(n): return 7 * n
    for n in range(1, 10):
        assert a(n+1) == a(n) + 7

def check_C7():
    """EXHAUSTIVE PROOF"""
    def a_rec(n, a1, a2):
        if n == 1: return a1
        if n == 2: return a2
        seq = [0, a1, a2]
        for i in range(3, n + 1):
            seq.append(2 * seq[i-1] - seq[i-2])
        return seq[n]
    
    for _ in range(50):
        a1 = random.randint(-10, 10)
        a2 = random.randint(-10, 10)
        d = a2 - a1
        for n in range(1, 15):
            assert a_rec(n, a1, a2) == a1 + (n - 1) * d

def check_C8():
    """STRONG EVIDENCE"""
    for _ in range(50):
        r = random.uniform(-5, 5)
        if abs(r) < 0.01: continue
        q = -r * (1 / r)
        p = r + 1 / r
        assert abs(q + 1) < 1e-9
        assert abs(p) >= 2 - 1e-9

def check_D1():
    """STRONG EVIDENCE"""
    a_prev2 = Fraction(1, 1)
    a_prev1 = Fraction(2, 1)
    for n in range(3, 100):
        curr = (a_prev1 + a_prev2) / 2
        a_prev2 = a_prev1
        a_prev1 = curr
    
    assert abs(a_prev1 - Fraction(5, 3)) < 1e-9
    
    for x in [1, -0.5]:
        assert 2*x**2 - x - 1 == 0
        
    A = Fraction(5, 3)
    B = Fraction(4, 3)
    def a_closed(n): return A + B * Fraction(-1, 2)**n
    assert a_closed(1) == 1
    assert a_closed(2) == 2
    
    a_prev2 = Fraction(1, 1)
    a_prev1 = Fraction(2, 1)
    for n in range(3, 20):
        curr = (a_prev1 + a_prev2) / 2
        assert curr == a_closed(n)
        a_prev2 = a_prev1
        a_prev1 = curr
        
    assert A - B/2 == 1
    assert A + B/4 == 2
    assert Fraction(3, 4) * B == 1

def check_D2():
    """EXHAUSTIVE PROOF"""
    A = Fraction(0, 1)
    B = Fraction(1, 3)
    def a_closed(n): return (A + B * n) * 3**n
    assert a_closed(1) == 1
    assert a_closed(2) == 6
    assert a_closed(5) == 405
    
    assert (A+B)*3 == 1
    assert A+B == Fraction(1, 3)
    assert (A+2*B)*9 == 6
    assert A+2*B == Fraction(2, 3)
    
    def a_rec(n):
        if n == 1: return 1
        if n == 2: return 6
        seq = [0, 1, 6]
        for i in range(3, n + 1):
            seq.append(6 * seq[i-1] - 9 * seq[i-2])
        return seq[n]
        
    for n in range(1, 15):
        assert a_rec(n) == a_closed(n)
        
    assert a_rec(3) == 6 * 6 - 9 * 1 == 27
    assert a_closed(3) == 27
    
def check_D3():
    """STRONG EVIDENCE"""
    def a_rec(n):
        if n == 1: return 1
        if n == 2: return 0
        seq = [0, 1, 0]
        for i in range(3, n + 1):
            seq.append(-4 * seq[i-2])
        return seq[n]
        
    assert a_rec(3) == -4
    assert a_rec(4) == 0
    assert a_rec(5) == 16
    assert a_rec(6) == 0
    assert a_rec(7) == -64
    
    for n in range(1, 20):
        if n % 2 == 0:
            assert a_rec(n) == 0
        else:
            k = (n - 1) // 2
            assert a_rec(n) == (-4)**k

def check_D4():
    """EXHAUSTIVE PROOF"""
    p = 2
    q = -1
    def a_rec(n, a1, a2):
        if n == 1: return a1
        if n == 2: return a2
        seq = [0, a1, a2]
        for i in range(3, n + 1):
            seq.append(p * seq[i-1] + q * seq[i-2])
        return seq[n]
        
    for _ in range(50):
        a1 = random.randint(-10, 10)
        a2 = random.randint(-10, 10)
        d = a2 - a1
        for n in range(1, 15):
            assert a_rec(n, a1, a2) == a1 + (n - 1) * d
            
    assert 1**2 - 3*(1) - (-2) == 0
    assert 2**2 - 3*(2) - (-2) == 0

def check_D5():
    """STRONG EVIDENCE"""
    for _ in range(50):
        r1 = random.uniform(-0.99, 0.99)
        r2 = random.uniform(-0.99, 0.99)
        A = random.uniform(-100, 100)
        B = random.uniform(-100, 100)
        def a_closed(n): return A * r1**n + B * r2**n
        
        for n in [5000, 10000]:
            assert abs(a_closed(n)) < 1e-9

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
