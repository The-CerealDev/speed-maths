import math
import itertools

# A1
def check_A1():
    """ EXHAUSTIVE PROOF """
    assert 7 * 11 * 13 == 1001

# A2
def check_A2():
    """ EXHAUSTIVE PROOF """
    assert (10**5) % 11 == 10

# A3
def check_A3():
    """ EXHAUSTIVE PROOF """
    assert str(7**100)[-1] == '1'

# A4
def check_A4():
    """ EXHAUSTIVE PROOF """
    for k in range(1, 100):
        if math.isqrt(12 * k)**2 == 12 * k:
            assert k == 3
            return
    assert False

# A5
def check_A5():
    """ EXHAUSTIVE PROOF """
    assert math.gcd(84, 120) == 12

# A6
def check_A6():
    """ EXHAUSTIVE PROOF """
    for p in range(31, 100):
        if all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1)):
            assert p == 31
            return

# A7
def check_A7():
    """ EXHAUSTIVE PROOF """
    assert (3**10) % 8 == 1

# A8
def check_A8():
    """ EXHAUSTIVE PROOF """
    n = 210
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    assert sum(factors) == 17

# A9
def check_A9():
    """ EXHAUSTIVE PROOF """
    for d in range(10):
        if int(f"53{d}2") % 9 == 0:
            assert d == 8
            return
    assert False

# A10
def check_A10():
    """ EXHAUSTIVE PROOF """
    n = 27**5
    k = 0
    while n % (3**(k+1)) == 0:
        k += 1
    assert k == 15

# B1
def check_B1():
    """ EXHAUSTIVE PROOF """
    count = sum(1 for i in range(1, 145) if 144 % i == 0)
    assert count == 15

# B2
def check_B2():
    """ EXHAUSTIVE PROOF """
    for x in range(2, 1000):
        if x % 3 == 1 and x % 4 == 1 and x % 5 == 1:
            assert x == 61
            return
    assert False

# B3
def check_B3():
    """ EXHAUSTIVE PROOF """
    for x in range(1, 100):
        if (5 * x) % 7 == 1:
            assert x == 3
            return
    assert False

# B4
def check_B4():
    """ EXHAUSTIVE PROOF """
    count = 0
    n = math.factorial(100)
    while n % 5 == 0:
        count += 1
        n //= 5
    assert count == 24

# B5
def check_B5():
    """ EXHAUSTIVE PROOF """
    assert str(51**2)[-2:] == '01'

# B6
def check_B6():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 100):
        if math.factorial(n) % 100 == 0:
            assert n == 10
            return
    assert False

# B7
def check_B7():
    """ EXHAUSTIVE PROOF """
    min_sum = float('inf')
    for a in range(1, 200):
        for b in range(1, 200):
            if a != b and math.gcd(a, b) == 12 and (a * b) // math.gcd(a, b) == 144:
                min_sum = min(min_sum, a + b)
    assert min_sum == 84

# B8
def check_B8():
    """ EXHAUSTIVE PROOF """
    num = 2**10 * 5**8
    assert sum(int(d) for d in str(num)) == 4

# B9
def check_B9():
    """ EXHAUSTIVE PROOF """
    assert (2**20 + 3**20) % 5 == 2

# B10
def check_B10():
    """ EXHAUSTIVE PROOF """
    n = math.factorial(125)
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    assert count == 31

# C1
def check_C1():
    """ EXHAUSTIVE PROOF """
    primes = set()
    for i in range(2, 200):
        if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
            primes.add(i)
    for n in range(1, 100):
        val = n**2 - 4*n - 5
        if val in primes:
            assert n == 6
            return
    assert False

# C2
def check_C2():
    """ EXHAUSTIVE PROOF """
    count = 0
    for x in range(-100, 100):
        if x != 1 and (x**2 + 11) % (x - 1) == 0:
            count += 1
    assert count == 12

# C3
def check_C3():
    """ EXHAUSTIVE PROOF """
    total = 0
    for n in range(1, 100):
        val = n**2 + 8*n
        if math.isqrt(val)**2 == val:
            total += n
    assert total == 1

# C4
def check_C4():
    """ EXHAUSTIVE PROOF """
    count = 0
    primes = {2, 3, 5, 7}
    for i in range(100, 1000):
        prod = int(str(i)[0]) * int(str(i)[1]) * int(str(i)[2])
        if prod in primes:
            count += 1
    assert count == 12

# C5
def check_C5():
    """ EXHAUSTIVE PROOF """
    count = sum(1 for x in range(1, 101) if (x**2) % 5 == 4)
    assert count == 40

# C6
def check_C6():
    """ EXHAUSTIVE PROOF """
    count = 0
    for x in range(1, 100):
        y = 100 - x
        if math.gcd(x, y) == 5:
            count += 1
    assert count == 8

# C7
def check_C7():
    """ EXHAUSTIVE PROOF """
    max_n = 0
    for n in range(1, 1000):
        if (n**3 + 100) % (n + 10) == 0:
            max_n = n
    assert max_n == 890

# C8
def check_C8():
    """ EXHAUSTIVE PROOF """
    total = sum(x for x in range(1, 20) if (x**2) % 11 == 5)
    assert total == 44

# D1
def check_D1():
    """ EXHAUSTIVE PROOF """
    total = sum(int("".join(perm)) for perm in itertools.permutations('1234'))
    assert total == 66660

# D2
def check_D2():
    """ EXHAUSTIVE PROOF """
    count = 0
    for b in range(1, 2024):
        a2 = 2024 + b**2
        if math.isqrt(a2)**2 == a2:
            count += 1
    assert count == 4

# D3
def check_D3():
    """ EXHAUSTIVE PROOF """
    n = math.factorial(2025)
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    assert count % 100 == 5

# D4
def check_D4():
    """ EXHAUSTIVE PROOF """
    count = sum(1 for x in range(1, 101) for y in range(1, 101) if (x**2 + y**2) % 5 == 0)
    assert count == 3600

# D5
def check_D5():
    """ EXHAUSTIVE PROOF """
    max_gcd = 0
    for n in range(1, 1000):
        max_gcd = max(max_gcd, math.gcd(n**2 + 3, n + 2))
    assert max_gcd == 7

if __name__ == "__main__":
    for k, v in dict(globals()).items():
        if k.startswith("check_") and callable(v):
            v()
            print(f"{k} passed")
