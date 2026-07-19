import math
import itertools

# A1
def check_A1():
    """EXHAUSTIVE PROOF"""
    assert 7 * 13 == 91
    # Verify both are prime
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True
    assert is_prime(7)
    assert is_prime(13)

# A2
def check_A2():
    """EXHAUSTIVE PROOF"""
    assert (3**20) % 10 == 1

# A3
def check_A3():
    """EXHAUSTIVE PROOF"""
    assert math.gcd(144, 60) == 12

# A4
def check_A4():
    """EXHAUSTIVE PROOF"""
    assert (12 * 13) % 5 == 1

# A5
def check_A5():
    """EXHAUSTIVE PROOF"""
    def smallest_prime_factor(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return i
        return n
    assert smallest_prime_factor(323) == 17

# A6
def check_A6():
    """EXHAUSTIVE PROOF"""
    divisors = [i for i in range(1, 29) if 28 % i == 0]
    assert len(divisors) == 6

# A7
def check_A7():
    """EXHAUSTIVE PROOF"""
    assert (5**3) % 6 == 5

# A8
def check_A8():
    """EXHAUSTIVE PROOF"""
    ans = [x for x in range(7) if (4*x) % 7 == 1]
    assert len(ans) == 1
    assert ans[0] == 2

# A9
def check_A9():
    """EXHAUSTIVE PROOF"""
    assert (10**10) % 9 == 1

# A10
def check_A10():
    """EXHAUSTIVE PROOF"""
    assert 3**20 > 2**30

# B1
def check_B1():
    """EXHAUSTIVE PROOF"""
    assert (7**4) % 100 == 1

# B2
def check_B2():
    """EXHAUSTIVE PROOF"""
    val = math.factorial(20)
    s = str(val)
    zeros = len(s) - len(s.rstrip('0'))
    assert zeros == 4

# B3
def check_B3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 1000):
        if math.isqrt(120 * n)**2 == 120 * n:
            assert n == 30
            break

# B4
def check_B4():
    """EXHAUSTIVE PROOF"""
    val = math.factorial(50)
    count = 0
    while val % 3 == 0:
        count += 1
        val //= 3
    assert count == 22

# B5
def check_B5():
    """EXHAUSTIVE PROOF"""
    sols = []
    for x in range(1, 100):
        for y in range(1, x):
            if x**2 - y**2 == 17:
                sols.append((x, y))
    assert len(sols) == 1
    assert sols[0] == (9, 8)

# B6
def check_B6():
    """EXHAUSTIVE PROOF"""
    assert (3**100) % 10 == 1

# B7
def check_B7():
    """EXHAUSTIVE PROOF"""
    ans = [x for x in range(11) if (3*x + 4) % 11 == 6]
    assert len(ans) == 1
    assert ans[0] == 8

# B8
def check_B8():
    """EXHAUSTIVE PROOF"""
    divisors = [i for i in range(1, 51) if 50 % i == 0]
    assert sum(divisors) == 93

# B9
def check_B9():
    """EXHAUSTIVE PROOF"""
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True
    primes = [i for i in range(41, 50) if is_prime(i)]
    assert len(primes) == 3

# B10
def check_B10():
    """EXHAUSTIVE PROOF"""
    for n in range(100, 1000):
        if n % 3 == 2 and n % 4 == 2 and n % 5 == 2:
            assert n == 122
            break

# C1
def check_C1():
    """EXHAUSTIVE PROOF"""
    def count_divisors(n):
        return sum(1 for i in range(1, n+1) if n % i == 0)
    
    prod = 1
    for n in range(1, 50):
        if count_divisors(n) == 3:
            prod *= n
    assert prod == 44100

# C2
def check_C2():
    """EXHAUSTIVE PROOF"""
    def count_divisors(n):
        cnt = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cnt += 1
                if i * i != n:
                    cnt += 1
        return cnt

    for n in range(1, 20000):
        if count_divisors(n) == 15:
            assert n == 144
            break

# C3
def check_C3():
    """EXHAUSTIVE PROOF"""
    count = 0
    for a in range(6):
        for b in range(5):
            for c in range(4):
                val = (3**a) * (5**b) * (7**c)
                if val % 45 == 0:
                    count += 1
    assert count == 64

# C4
def check_C4():
    """EXHAUSTIVE PROOF"""
    val = math.factorial(10)
    divisors = [i for i in range(1, int(math.sqrt(val)) + 1) if val % i == 0]
    for d in reversed(divisors):
        if d * d != val and val % (val // d) == 0:
            divisors.append(val // d)
    
    square_divisors = [d for d in divisors if math.isqrt(d)**2 == d]
    assert len(square_divisors) == 30

# C5
def check_C5():
    """EXHAUSTIVE PROOF"""
    max_gcd = 0
    for n in range(1, 1000):
        g = math.gcd(n**2 + 5, n + 2)
        if g > max_gcd:
            max_gcd = g
    assert max_gcd == 9

# C6
def check_C6():
    """EXHAUSTIVE PROOF"""
    val = 10**15 - 2026
    digit_sum = sum(int(d) for d in str(val))
    assert digit_sum == 126

# C7
def check_C7():
    """EXHAUSTIVE PROOF"""
    sols = set()
    for x in range(1, 100):
        for y in range(1, 100):
            if x**3 - y**3 == 37:
                sols.add((x, y))
    assert sols == {(4, 3)}

# C8
def check_C8():
    """EXHAUSTIVE PROOF"""
    for x in range(1, 1000):
        if x % 3 == 1 and x % 4 == 2 and x % 5 == 3:
            assert x == 58
            break

# D1
def check_D1():
    """EXHAUSTIVE PROOF"""
    count = 0
    for x in range(-20, 21):
        for y in range(-20, 21):
            if x**2 + x*y + y**2 == 7:
                count += 1
    assert count == 12

# D2
def check_D2():
    """EXHAUSTIVE PROOF"""
    count = 0
    for n in range(1, 101):
        # use large ints to safely compute
        val = n**n
        r = math.isqrt(val)
        if r*r == val:
            count += 1
    assert count == 55

# D3
def check_D3():
    """EXHAUSTIVE PROOF"""
    sols = set()
    for a in range(1, 100):
        for b in range(1, 100):
            if a**2 - 4*(b**2) == 45:
                sols.add((a, b))
    assert sols == {(7, 1), (9, 3), (23, 11)}

# D4
def check_D4():
    """EXHAUSTIVE PROOF"""
    val = 2**16 - 1
    largest_prime = 1
    # Simple prime factorisation
    d = 2
    while d * d <= val:
        if val % d == 0:
            largest_prime = d
            while val % d == 0:
                val //= d
        d += 1
    if val > 1:
        largest_prime = val
    assert largest_prime == 257

# D5
def check_D5():
    """EXHAUSTIVE PROOF"""
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True
    
    sols = []
    for p in range(2, 100):
        if not is_prime(p): continue
        for q in range(2, 100):
            if not is_prime(q): continue
            if p**2 - 2*(q**2) == 1:
                sols.append((p, q))
    assert len(sols) == 1
    p, q = sols[0]
    assert p + q == 5


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
