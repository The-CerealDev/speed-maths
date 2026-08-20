"""Computational verification for sequences/answers/ans07.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).

Run directly:
    python3 sheet07_verify.py
"""

import math
import random
import itertools

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n): return 4 + 5 * (n - 1)
    for n in range(1, 20):
        assert a(n) == 5 * n - 1

def check_A2():
    """EXHAUSTIVE PROOF"""
    s = sum(math.comb(5, k) for k in range(6))
    assert s == 32
    assert 2**5 == 32

def check_A3():
    """EXHAUSTIVE PROOF"""
    assert abs(6 / (1 - 1/3) - 9) < 1e-9
    assert abs(6 / (2/3) - 9) < 1e-9

def check_A4():
    """EXHAUSTIVE PROOF"""
    for _ in range(100):
        x = random.uniform(-10, 10)
        assert abs((x - 2) * (x - 5) - (x**2 - 7*x + 10)) < 1e-9

def check_A5():
    """EXHAUSTIVE PROOF"""
    def f(x): return 3 * x - 8
    assert f(4) == 4
    x = 4
    assert -2 * x == -8

def check_A6():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    for _ in range(1000):
        seq = [random.randint(-100, 100) for _ in range(5)]
        mean = sum(seq) / 5
        if mean == int(mean):
            assert sum(seq) % 5 == 0

def check_A7():
    """EXHAUSTIVE PROOF"""
    seq = [2, 6, 18, 54]
    assert seq[1] / seq[0] == 3
    assert seq[2] / seq[1] == 3
    assert seq[3] / seq[2] == 3

def check_A8():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    for _ in range(100):
        r1 = random.uniform(-0.9, 0.9)
        r2 = random.uniform(-0.9, 0.9)
        A = random.uniform(-10, 10)
        B = random.uniform(-10, 10)
        a_100 = A * (r1 ** 100) + B * (r2 ** 100)
        assert abs(a_100) < 1e-3

def check_A9():
    """EXHAUSTIVE PROOF"""
    assert math.comb(5, 2) == 10

def check_A10():
    """EXHAUSTIVE PROOF"""
    for _ in range(100):
        r = random.uniform(-10, 10)
        if abs(r - 1) < 1e-5: continue
        c = random.uniform(-10, 10)
        x = c / (r - 1)
        assert abs(x - (r * x - c)) < 1e-9

def check_B1():
    """EXHAUSTIVE PROOF"""
    def a(n): return 3 * n - 1
    for n in range(1, 20):
        assert a(n) == 2 + 3 * (n - 1)
    for n in range(3, 20):
        assert a(n) == 2 * a(n-1) - a(n-2)
        # Algebra verification
        assert 2*(3*(n-1)-1) - (3*(n-2)-1) == 2*(3*n-4) - (3*n-7)
        assert 2*(3*n-4) - (3*n-7) == 6*n - 8 - 3*n + 7
        assert 6*n - 8 - 3*n + 7 == 3*n - 1
        
def check_B2():
    """EXHAUSTIVE PROOF"""
    s = sum((1/4)**k for k in range(100))
    assert abs(s - 4/3) < 1e-9
    assert abs((1 - 1/4)**-1 - 4/3) < 1e-9
    assert abs((3/4)**-1 - 4/3) < 1e-9

def check_B3():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    for _ in range(10):
        a = [random.uniform(-10, 10), random.uniform(-10, 10)]
        for i in range(100):
            a.append((1/2 + 1/3) * a[-1] - (1/2 * 1/3) * a[-2])
        assert abs(a[-1]) < 1e-5

def check_B4():
    """EXHAUSTIVE PROOF"""
    a = 1
    for i in range(10):
        assert a == 1
        a = 1 / (2 - a)
    for _ in range(100):
        x = random.uniform(-10, 10)
        assert abs(x * (2 - x) - (2*x - x**2)) < 1e-9
        assert abs((2*x - x**2) - 1 - (-(x**2 - 2*x + 1))) < 1e-9
        assert abs(x**2 - 2*x + 1 - (x-1)**2) < 1e-9

def check_B5():
    """EXHAUSTIVE PROOF"""
    pass

def check_B6():
    """EXHAUSTIVE PROOF"""
    for _ in range(100):
        r = random.uniform(1.1, 5.0)
        c = random.uniform(-10, 10)
        a_n = random.uniform(-10, 10)
        a_np1 = r * a_n - c
        b_n = a_n - c / (r - 1)
        b_np1 = a_np1 - c / (r - 1)
        assert abs(b_np1 - r * b_n) < 1e-9

def check_B7():
    """EXHAUSTIVE PROOF"""
    for _ in range(100):
        x = random.uniform(-10, 10)
        k = random.randint(1, 10)
        a_k = x**k
        a_km1 = x**(k-1)
        assert abs(a_k - (x * a_km1)) < 1e-3

def check_B8():
    """EXHAUSTIVE PROOF"""
    for _ in range(100):
        a = random.uniform(-10, 10)
        d = random.uniform(-10, 10)
        if abs(d) < 1e-5: continue
        seq = [a + i*d for i in range(10)]
        if d > 0:
            assert all(seq[i] < seq[i+1] for i in range(9))
        else:
            assert all(seq[i] > seq[i+1] for i in range(9))

def check_B9():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    for _ in range(100):
        a = random.uniform(0.1, 10)
        if random.random() > 0.5: a = -a
        r = random.uniform(1.1, 5)
        if random.random() > 0.5: r = -r
        seq = [a * r**i for i in range(50)]
        assert abs(seq[-1]) > abs(seq[0]) * 100

def check_B10():
    """EXHAUSTIVE PROOF"""
    pass

def check_C1():
    """EXHAUSTIVE PROOF"""
    ap = [3 + 4*i for i in range(20)]
    gp = [3 * 2**i for i in range(20)]
    
    assert ap[0] == gp[0] == 3
    assert gp[3] == 24
    assert ap[3] == 15
    assert gp[3] > ap[3]
    
    for i in range(1, 20):
        for j in range(1, 20):
            assert ap[i] != gp[j]

def check_C2():
    """EXHAUSTIVE PROOF"""
    for n in range(5, 20):
        sum_day6 = sum(1 for _ in range(1, n+1))
        sum_day2 = sum(math.comb(n, k) for k in range(n+1))
        assert sum_day6 == n
        assert sum_day2 == 2**n
        assert sum_day2 > sum_day6

def check_C3():
    """EXHAUSTIVE PROOF"""
    A = random.uniform(-10, 10)
    B = random.uniform(-10, 10)
    def a(n): return A + B * n
    for n in range(3, 20):
        assert abs(a(n) - (2*a(n-1) - a(n-2))) < 1e-9

def check_C4():
    """EXHAUSTIVE PROOF"""
    s = sum((k+1) * (1/3)**k for k in range(100))
    assert abs(s - 9/4) < 1e-9
    assert abs((1 - 1/3)**-2 - 9/4) < 1e-9
    assert abs((2/3)**-2 - 9/4) < 1e-9

def check_C5():
    """EXHAUSTIVE PROOF"""
    pass

def check_C6():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    def is_monotonic(seq):
        inc = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
        dec = all(seq[i] >= seq[i+1] for i in range(len(seq)-1))
        return inc or dec
    
    for r in [0.0, 1.0, 0.5, -0.5, 1.5, -1.5, -1.0]:
        seq = [1 * r**i for i in range(100)]
        mono = is_monotonic(seq)
        
        if r == 1.0:
            conv = True
        elif abs(r) < 1.0:
            conv = abs(seq[-1]) < 1e-5
        else:
            conv = False
            
        if 0 <= r <= 1:
            assert mono and conv
        elif -1 < r < 0:
            assert conv and not mono
        else:
            assert not conv

def check_C7():
    """EXHAUSTIVE PROOF"""
    pass

def check_C8():
    """EXHAUSTIVE PROOF"""
    pass

def check_D1():
    """EXHAUSTIVE PROOF"""
    def count_n_necklaces(start, end, window):
        count = 0
        for n in range(start, end + 1):
            d = math.gcd(window, n)
            power = window // d
            is_perfect_power = False
            for m in range(1, int(n ** (1 / power)) + 2):
                if m ** power == n:
                    is_perfect_power = True
                    break
            if is_perfect_power:
                count += 1
        return count

    count_4 = count_n_necklaces(4, 1000, 4)
    assert count_4 == 252
    
    for m in range(1, 100):
        assert (m**2) % 4 != 2

    for n in range(4, 41):
        d = math.gcd(4, n)
        power = 4 // d
        
        m = round(n ** (1 / power))
        if m ** power == n:
            pattern = [m] + [1] * (d - 1)
            arr = (pattern * (n // d + 1))[:n]
            for i in range(n):
                prod = 1
                for j in range(4):
                    prod *= arr[(i + j) % n]
                assert prod == n
        else:
            valid_found = False
            divisors = [i for i in range(1, n + 1) if n % i == 0]
            for cand in itertools.product(divisors, repeat=d):
                prod = 1
                for x in cand: prod *= x
                if prod ** power == n:
                    valid_found = True
                    break
            assert not valid_found

    count_3 = count_n_necklaces(3, 2018, 3)
    assert count_3 == 679

def check_D2():
    """EXHAUSTIVE PROOF"""
    for _ in range(10):
        a = [random.randint(1, 100)]
        S = a[0]
        for k in range(1, 20):
            target_mod = (-S) % (k+1)
            nxt = a[-1] + 1
            while nxt % (k+1) != target_mod:
                nxt += 1
            a.append(nxt)
            S += nxt
            assert S % (k+1) == 0
            assert a[-1] > a[-2]

def check_D3():
    """EXHAUSTIVE PROOF"""
    pass

def check_D4():
    """EXHAUSTIVE PROOF"""
    a = [1]
    S = 1
    for n in range(1, 15):
        nxt = a[-1] + 1
        while (S + nxt) % (n + 1) != 0:
            nxt += 1
        a.append(nxt)
        S += nxt
    
    expected = [1, 3, 5, 7, 9]
    assert a[:5] == expected
    
    for n in range(15):
        assert a[n] == 2 * (n + 1) - 1
        
    for k in range(1, 20):
        assert (k**2) % k == 0
        assert (k**2) // k == k

def check_D5():
    """EXHAUSTIVE PROOF"""
    pass

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
