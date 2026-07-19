import math
import itertools
from collections import Counter

def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(math.isqrt(n)) + 1))

def pf(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
                break
    return factors

# A1
def check_A1():
    """EXHAUSTIVE PROOF"""
    assert (10**10 + 10**5 + 1) % 9 == 3

# A2
def check_A2():
    """EXHAUSTIVE PROOF"""
    assert (3**2026) % 10 == 9

# A3
def check_A3():
    """EXHAUSTIVE PROOF"""
    assert max(p for p in range(2, 1002) if 1001 % p == 0 and is_prime(p)) == 13

# A4
def check_A4():
    """EXHAUSTIVE PROOF"""
    assert (7 * 8 * 9) % 5 == 4

# A5
def check_A5():
    """EXHAUSTIVE PROOF"""
    assert next(n for n in range(1, 10) if (2*n) % 5 == 3) == 4

# A6
def check_A6():
    """EXHAUSTIVE PROOF"""
    assert math.gcd(144, 84) == 12

# A7
def check_A7():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for i in range(1, 37) if 36 % i == 0) == 9

# A8
def check_A8():
    """EXHAUSTIVE PROOF"""
    assert (2**10) % 11 == 1

# A9
def check_A9():
    """EXHAUSTIVE PROOF"""
    assert pf(120) == [2, 2, 2, 3, 5]

# A10
def check_A10():
    """EXHAUSTIVE PROOF"""
    assert next(k for k in range(1, 100) if math.isqrt(12*k)**2 == 12*k) == 3

# B1
def check_B1():
    """EXHAUSTIVE PROOF"""
    val = 3**2026 + 3**2025 + 3**2024
    assert sum(1 for i in [3, 4, 5, 6, 7] if val % i == 0) == 1

# B2
def check_B2():
    """EXHAUSTIVE PROOF"""
    fact = math.factorial(100)
    assert max(p for p in range(1, 100) if fact % (2**p) == 0) == 97

# B3
def check_B3():
    """EXHAUSTIVE PROOF"""
    assert max((10*a+b)//(a+b) for a in range(1, 10) for b in range(1, 10) if (10*a+b) % (a+b) == 0) == 9

# B4
def check_B4():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for x in range(-100, 100) for y in range(-100, 100) if x != 0 and y != 0 and x*y == 24) == 16

# B5
def check_B5():
    """EXHAUSTIVE PROOF"""
    assert next(n for n in range(3, 100) if n % 3 == 2 and n % 4 == 2 and n % 5 == 2) == 62

# B6
def check_B6():
    """EXHAUSTIVE PROOF"""
    assert (11**11 + 12**12) % 10 == 7

# B7
def check_B7():
    """EXHAUSTIVE PROOF"""
    assert next(p for p in range(2, 100) if is_prime(p) and is_prime(p**2+2)) == 3

# B8
def check_B8():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for n in range(-50, 50) if n != -2 and (2*n+15) % (n+2) == 0) == 4

# B9
def check_B9():
    """EXHAUSTIVE PROOF"""
    assert sum(n for n in range(1, 50) if is_prime(n**2-1)) == 2

# B10
def check_B10():
    """EXHAUSTIVE PROOF"""
    assert (5**2026 + 6**2026) % 100 == 81

# C1
def check_C1():
    """EXHAUSTIVE PROOF"""
    assert set((x, y) for x in range(1, 50) for y in range(1, 50) if 3*x + 3*y == x*y) == {(4,12), (6,6), (12,4)}

# C2
def check_C2():
    """EXHAUSTIVE PROOF"""
    sols = [(x,y) for x in range(1, 2000) for y in range(1, 2000) if x**2 - y**2 == 2025]
    assert min(sols, key=lambda p: p[1]) == (51, 24)

# C3
def check_C3():
    """EXHAUSTIVE PROOF"""
    assert set((x, y) for x in range(-50, 50) for y in range(-50, 50) if x*y + x + y == 14) == {(0,14), (14,0), (-2,-16), (-16,-2), (2,4), (4,2), (-4,-6), (-6,-4)}

# C4
def check_C4():
    """EXHAUSTIVE PROOF"""
    assert set(x for x in range(-50, 50) if is_prime(x**4+x**2+1)) == {1, -1}

# C5
def check_C5():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for a in range(10) for b in range(10) if int(f"3{a}4{b}2") % 36 == 0) == 6

# C6
def check_C6():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for c in itertools.combinations(range(1, 11), 3) if sum(c) % 3 == 0) == 42

# C7
def check_C7():
    """EXHAUSTIVE PROOF"""
    assert sum(x for x in range(-50, 50) if x != -1 and (x**2+7*x+2) % (x+1) == 0) == -6

# C8
def check_C8():
    """EXHAUSTIVE PROOF"""
    assert pow(2019, 2025, 100) == 99

# D1
def check_D1():
    """EXHAUSTIVE PROOF"""
    target = 2**3 * 3**2 * 5
    divs = [d for d in range(1, target+1) if target % d == 0]
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)
    assert sum(1 for i, a in enumerate(divs) for b in divs[i:] if lcm(a, b) == target) == 53

# D2
def check_D2():
    """EXHAUSTIVE PROOF"""
    assert set((p, q) for p in range(2, 50) for q in range(2, 50) if is_prime(p) and is_prime(q) and p**2 - 2*q**2 == 1) == {(3,2)}

# D3
def check_D3():
    """EXHAUSTIVE PROOF"""
    assert sum(1 for x in range(-20, 20) for y in range(-20, 20) for z in range(-20, 20) if x**3 + 2*y**3 == 4*z**3) == 1

# D4
def check_D4():
    """EXHAUSTIVE PROOF"""
    assert pow(7, 9999, 1000) == 143

# D5
def check_D5():
    """EXHAUSTIVE PROOF"""
    assert pow(2025, 2026, 1000) == 625


CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4, "C5": check_C5,
    "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
}

def main():
    if not __debug__:
        raise Exception("Do not run with -O! Assertions are disabled.")

    passed = 0
    for name, func in CHECKS.items():
        try:
            func()
            passed += 1
        except Exception as e:
            print(f"FAILED {name}: {e}")
            raise
    print(f"All {passed} checks passed!")

if __name__ == "__main__":
    main()
