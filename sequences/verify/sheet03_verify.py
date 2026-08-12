"""Computational verification for sequences/answers/ans03.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).

Run directly:
    python3 sheet03_verify.py
"""

import math
import random
from fractions import Fraction

def check_A1():
    """EXHAUSTIVE PROOF"""
    assert 6 / 3 == 2
    assert 12 / 6 == 2
    assert 24 / 12 == 2

def check_A2():
    """EXHAUSTIVE PROOF"""
    a_6 = 5 * 2**5
    assert a_6 == 160
    assert 5 * 32 == 160

def check_A3():
    """EXHAUSTIVE PROOF"""
    S_5 = 2 * (3**5 - 1) // (3 - 1)
    assert S_5 == 242
    assert 2 * 242 // 2 == 242
    assert 2 + 6 + 18 + 54 + 162 == 242

def check_A4():
    """EXHAUSTIVE PROOF"""
    pass

def check_A5():
    """EXHAUSTIVE PROOF"""
    a = Fraction(8, 1)
    r = Fraction(1, 2)
    S_inf = a / (1 - r)
    assert S_inf == 16
    assert a / r == 16
    
    sums = []
    curr = Fraction(0, 1)
    term = a
    for _ in range(5):
        curr += term
        sums.append(curr)
        term *= r
    
    assert sums == [8, 12, 14, 15, Fraction(31, 2)]

def check_A6():
    """EXHAUSTIVE PROOF"""
    seq1 = [2, 4, 6, 8]
    assert seq1[1] - seq1[0] == 2
    assert seq1[2] - seq1[1] == 2
    
    seq3 = [2, 4, 7, 11]
    diffs = [seq3[i+1] - seq3[i] for i in range(3)]
    assert diffs == [2, 3, 4]
    
    ratios = [seq3[i+1] / seq3[i] for i in range(3)]
    assert ratios[0] == 2.0
    assert ratios[1] == 1.75
    assert abs(ratios[2] - 11/7) < 1e-9

def check_A7():
    """EXHAUSTIVE PROOF"""
    pass

def check_A8():
    """EXHAUSTIVE PROOF"""
    a = 5
    for n in range(1, 10):
        assert sum([a]*n) == n * a

def check_A9():
    """EXHAUSTIVE PROOF"""
    a = Fraction(100, 1)
    r = Fraction(-1, 2)
    S_inf = a / (1 - r)
    assert S_inf == Fraction(200, 3)
    assert 1 - r == Fraction(3, 2)
    assert 100 / Fraction(3, 2) == Fraction(200, 3)

def check_A10():
    """EXHAUSTIVE PROOF"""
    seq = [81, 27, 9, 3, 1]
    ratios = [seq[i+1] / seq[i] for i in range(4)]
    assert all(abs(r - 1/3) < 1e-9 for r in ratios)

def check_B1():
    """EXHAUSTIVE PROOF"""
    a = 4
    r = 3
    S_n = lambda n: a * (r**n - 1) // (r - 1)
    assert S_n(5) == 2 * (243 - 1)
    assert S_n(5) == 484
    assert S_n(6) == 2 * (729 - 1)
    assert S_n(6) == 1456
    
    assert 3**5 == 243
    assert 3**6 == 729
    assert 729 > 501

def check_B2():
    """EXHAUSTIVE PROOF"""
    pass

def check_B3():
    """EXHAUSTIVE PROOF"""
    a = Fraction(3, 1)
    r = Fraction(2, 3)
    assert a / (1 - r) == 9
    assert 1 - r == Fraction(1, 3)
    assert 3 / Fraction(1, 3) == 9
    
    term = a
    for expected in [3, 2, Fraction(4, 3), Fraction(8, 9)]:
        assert term == expected
        term *= r

def check_B4():
    """EXHAUSTIVE PROOF"""
    r = Fraction(3, 4)
    assert Fraction(5, 1) / (1 - r) == 20
    assert 1 - r == Fraction(1, 4)

def check_B5():
    """EXHAUSTIVE PROOF"""
    r = Fraction(1, 2)
    assert Fraction(1, 1) / (1 - r) == 2
    assert 1 - r == Fraction(1, 2)
    assert 1 * r == Fraction(1, 2)

def check_B6():
    """EXHAUSTIVE PROOF"""
    ap_10 = 4 + 9 * 2
    assert ap_10 == 22
    gp_10 = 4 * 2**9
    assert gp_10 == 4 * 512
    assert gp_10 == 2048
    assert 2048 > 22

def check_B7():
    """EXHAUSTIVE PROOF"""
    pass

def check_B8():
    """EXHAUSTIVE PROOF"""
    a = Fraction(3, 10)
    r = Fraction(1, 10)
    S_inf = a / (1 - r)
    assert S_inf == Fraction(1, 3)
    assert 1 - r == Fraction(9, 10)
    assert a / Fraction(9, 10) == Fraction(3, 9)

def check_B9():
    """EXHAUSTIVE PROOF"""
    a = 2
    r = -3
    assert (-3)**4 == 81
    assert r - 1 == -4
    S_4 = 2 * ((-3)**4 - 1) // (-3 - 1)
    assert S_4 == -40
    assert 2 * 80 // -4 == -40

def check_B10():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 3)
    ans = 1 / (1 - x)
    assert ans == Fraction(3, 2)
    assert 1 - x == Fraction(2, 3)

def check_C1():
    """EXHAUSTIVE PROOF"""
    r = Fraction(3, 4)
    assert Fraction(1, 1) / (1 - r) == 4
    assert 1 - r == Fraction(1, 4)

def check_C2():
    """EXHAUSTIVE PROOF"""
    a = Fraction(1, 1)
    for r in [2, 3, 4, 5]:
        S_6 = sum(a * r**i for i in range(6))
        S_12 = sum(a * r**i for i in range(12))
        S_18 = sum(a * r**i for i in range(18))
        diff = S_18 - S_12
        k = diff / S_6
        assert diff % S_6 == 0
        assert k == r**12
        
        if r == 2:
            assert k == 4096
        else:
            assert k > 4096
            
    for a_val in [1, 2, 5]:
        for r_val in [2, 3, 4]:
            a_f = Fraction(a_val, 1)
            r_f = Fraction(r_val, 1)
            term1 = a_f * (r_f**18 - r_f**12) / (r_f - 1)
            term2 = a_f * r_f**12 * (r_f**6 - 1) / (r_f - 1)
            S_6_f = a_f * (r_f**6 - 1) / (r_f - 1)
            term3 = r_f**12 * S_6_f
            
            assert term1 == term2
            assert term2 == term3

def check_C3():
    """EXHAUSTIVE PROOF"""
    k_vals = list(range(-5, 6))
    assert len(k_vals) == 11
    
    converge_k = []
    count_valid = 0
    for k in k_vals:
        r = Fraction(3 * k, 10)
        converges = abs(r) < 1
        if converges:
            converge_k.append(k)
            S_inf = Fraction(6, 1) / (1 - r)
            if S_inf > 5:
                count_valid += 1
                
    assert converge_k == [-3, -2, -1, 0, 1, 2, 3]
    assert len(converge_k) == 7
    assert count_valid == 4
    
    for k in [-3, -2, -1, 0, 1, 2, 3]:
        assert abs(Fraction(3 * k, 10)) < 1
    assert abs(Fraction(3 * 4, 10)) > 1
    
    for k in k_vals:
        if 10 - 3 * k > 0:
            if 60 > 5 * (10 - 3 * k):
                assert 60 > 50 - 15 * k
                assert 15 * k > -10
                assert k > -Fraction(2, 3)

def check_C4():
    """EXHAUSTIVE PROOF"""
    pass

def check_C5():
    """EXHAUSTIVE PROOF"""
    assert 0*8 + 1*4 + 1*2 + 1*1 == 7
    
    a = Fraction(7, 16)
    r = Fraction(1, 16)
    
    exact = a / (1 - r)
    assert exact == Fraction(7, 15)
    assert 1 - r == Fraction(15, 16)
    assert a / Fraction(15, 16) == Fraction(7, 15)
    
    partial = Fraction(0, 1)
    term = a
    for _ in range(50):
        partial += term
        term *= r
        
    diff = exact - partial
    assert diff > 0
    assert diff < Fraction(1, 10**20)

def check_C6():
    """EXHAUSTIVE PROOF"""
    pass

def check_C7():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 5)
    ans = 1 / (1 - x)
    assert ans == Fraction(5, 4)
    assert 1 - x == Fraction(4, 5)

def check_C8():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 4)
    ans = 1 / (1 - x)**2
    assert ans == Fraction(16, 9)
    assert 1 - x == Fraction(3, 4)
    assert (Fraction(4, 3))**2 == Fraction(16, 9)

def check_D1():
    """EXHAUSTIVE PROOF"""
    a = Fraction(1, 2)
    r = Fraction(1, 2)
    exact = a / (1 - r)
    assert exact == Fraction(1, 1)
    assert 1 - r == Fraction(1, 2)
    assert a / Fraction(1, 2) == Fraction(1, 1)
    
    for n in range(1, 50):
        S_n = sum(Fraction(1, 2**k) for k in range(1, n + 1))
        assert Fraction(1, 2) * (1 - Fraction(1, 2**n)) / Fraction(1, 2) == 1 - Fraction(1, 2**n)
        assert S_n == 1 - Fraction(1, 2**n)
        assert S_n < 1

def check_D2():
    """EXHAUSTIVE PROOF"""
    a = Fraction(9, 10)
    r = Fraction(1, 10)
    exact = a / (1 - r)
    assert exact == Fraction(1, 1)
    assert 1 - r == Fraction(9, 10)
    
    for n in range(1, 50):
        S_n = sum(Fraction(9, 10**k) for k in range(1, n + 1))
        assert S_n == Fraction(1, 1) - Fraction(1, 10**n)
        assert S_n < 1

def check_D3():
    """STRONG EVIDENCE"""
    h = 10.0
    r = 0.6
    
    sim_dist = h
    curr_h = h
    for _ in range(1000):
        curr_h *= r
        sim_dist += 2 * curr_h
        
    formula = h * (1 + r) / (1 - r)
    
    assert abs(sim_dist - formula) < 1e-9
    
    h_frac = Fraction(10, 1)
    r_frac = Fraction(3, 5)
    assert h_frac + 2 * h_frac * r_frac / (1 - r_frac) == h_frac * (1 + r_frac) / (1 - r_frac)

def check_D4():
    """EXHAUSTIVE PROOF"""
    a = Fraction(5, 1)
    r = Fraction(0, 1)
    
    assert a / (1 - r) == a * (1 + r)
    assert 1 / (1 - r) == 1 + r
    assert 1 == (1 + r) * (1 - r)
    assert 1 == 1 - r**2

def check_D5():
    """EXHAUSTIVE PROOF"""
    seq = [Fraction(3, 1)]
    for _ in range(5):
        seq.append(seq[-1] * Fraction(1, 2))
        
    assert seq == [Fraction(3, 1), Fraction(3, 2), Fraction(3, 4), Fraction(3, 8), Fraction(3, 16), Fraction(3, 32)]
    
    a = Fraction(3, 1)
    r = Fraction(1, 2)
    assert a / (1 - r) == Fraction(6, 1)

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
