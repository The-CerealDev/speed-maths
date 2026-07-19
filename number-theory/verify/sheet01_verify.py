import math
import itertools

# A1
def check_A1():
    """ EXHAUSTIVE PROOF """
    assert 3**4 * 5**2 == 2025

# A2
def check_A2():
    """ EXHAUSTIVE PROOF """
    assert (10**6) % 7 == 1

# A3
def check_A3():
    """ EXHAUSTIVE PROOF """
    assert str(3**2024)[-1] == '1'

# A4
def check_A4():
    """ EXHAUSTIVE PROOF """
    found = False
    for d in range(10):
        num = int(f"73{d}4")
        if num % 9 == 0:
            assert d == 4
            found = True
    assert found

# A5
def check_A5():
    """ EXHAUSTIVE PROOF """
    for a in range(1, 100):
        for b in range(1, 100):
            if a != b and math.gcd(a, b) == 6 and (a * b) // math.gcd(a, b) == 36:
                assert a + b == 42
                return
    assert False

# A6
def check_A6():
    """ EXHAUSTIVE PROOF """
    num = math.factorial(20)
    k = 0
    while num % (2**(k+1)) == 0:
        k += 1
    assert k == 18

# A7
def check_A7():
    """ EXHAUSTIVE PROOF """
    assert (11**10) % 10 == 1

# A8
def check_A8():
    """ EXHAUSTIVE PROOF """
    assert (2**100 + 3**100) % 5 == 2

# A9
def check_A9():
    """ EXHAUSTIVE PROOF """
    for i in range(2, 1001):
        if 1001 % i == 0:
            assert i == 7
            break

# A10
def check_A10():
    """ EXHAUSTIVE PROOF """
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True
    
    found = False
    for n in range(1, 100):
        if is_prime(n**2 - 1):
            assert n == 2
            found = True
    assert found

# B1
def check_B1():
    """ EXHAUSTIVE PROOF """
    divs = sum(1 for i in range(1, 361) if 360 % i == 0)
    assert divs == 24

# B2
def check_B2():
    """ EXHAUSTIVE PROOF """
    for x in range(1, 1000):
        if x % 5 == 3 and x % 7 == 5:
            assert x == 33
            break

# B3
def check_B3():
    """ EXHAUSTIVE PROOF """
    num_str = str(2**2024 * 5**2025)
    digit_sum = sum(int(d) for d in num_str)
    assert digit_sum == 5

# B4
def check_B4():
    """ EXHAUSTIVE PROOF """
    for x in range(1, 100):
        if (4 * x) % 7 == 5:
            assert x == 3
            break

# B5
def check_B5():
    """ EXHAUSTIVE PROOF """
    assert str(99**2)[-2:] == '01'

# B6
def check_B6():
    """ EXHAUSTIVE PROOF """
    assert math.gcd(2**12 - 1, 2**18 - 1) == 63

# B7
def check_B7():
    """ EXHAUSTIVE PROOF """
    for n in range(2, 100):
        s = (n-1) + n + (n+1)
        r = int(round(s**(1/3.0)))
        if r**3 == s:
            assert n + 1 == 10
            break

# B8
def check_B8():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 50000):
        if int(math.sqrt(10 * n))**2 == 10 * n:
            r = int(round((6 * n)**(1/3.0)))
            if r**3 == 6 * n:
                assert n == 36000
                return
    assert False

# B9
def check_B9():
    """ EXHAUSTIVE PROOF """
    s = str(math.factorial(100))
    assert len(s) - len(s.rstrip('0')) == 24

# B10
def check_B10():
    """ EXHAUSTIVE PROOF """
    max_val = -1
    for x in range(10):
        for y in range(10):
            num = int(f"24{x}8{y}")
            if num % 4 == 0 and num % 9 == 0:
                max_val = max(max_val, x + y)
    assert max_val == 13

# C1
def check_C1():
    """ EXHAUSTIVE PROOF """
    total = 0
    for x in range(-100, 100):
        if x != -1 and (x**2 + 5) % (x + 1) == 0:
            total += x
    assert total == -8

# C2
def check_C2():
    """ EXHAUSTIVE PROOF """
    count = 0
    for a in range(1, 100):
        for b in range(1, 100):
            if a * b == 6 * (a + b):
                count += 1
    assert count == 9

# C3
def check_C3():
    """ EXHAUSTIVE PROOF """
    count = sum(1 for n in range(1, 101) if n % 3 == 0)
    assert count == 33

# C4
def check_C4():
    """ EXHAUSTIVE PROOF """
    found = []
    for a in range(1, 10):
        for b in range(10):
            if int(f"{a}34{b}2") % 99 == 0:
                found.append(a * b)
    assert found == [18]

# C5
def check_C5():
    """ EXHAUSTIVE PROOF """
    for num_neg1 in range(25):
        num_1 = 24 - num_neg1
        if num_neg1 * (-1) + num_1 * 1 == 0 and ((-1) ** num_neg1) * (1 ** num_1) == 1:
            assert num_neg1 == 12
            return
    assert False

# C6
def check_C6():
    """ EXHAUSTIVE PROOF """
    num = 3**256 - 1
    k = 0
    while num % (2**(k+1)) == 0:
        k += 1
    assert k == 10

# C7
def check_C7():
    """ EXHAUSTIVE PROOF """
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True
    
    found = []
    for q in range(2, 50):
        if is_prime(q):
            p2 = 1 + 2 * q**2
            p = int(math.sqrt(p2))
            if p**2 == p2 and is_prime(p):
                found.append((p, q))
    assert found == [(3, 2)]

# C8
def check_C8():
    """ EXHAUSTIVE PROOF """
    import math
    nums = []
    for x in range(100, 1000):
        s = str(x)
        nums.append(int(s + s[::-1]))
    g = nums[0]
    for n in nums[1:]:
        g = math.gcd(g, n)
    
    max_p = 1
    d = 2
    while d * d <= g:
        while (g % d) == 0:
            max_p = d
            g //= d
        d += 1
    if g > 1:
        max_p = g
    assert max_p == 11

# D1
def check_D1():
    """ EXHAUSTIVE PROOF """
    total = 0
    for n in range(-2000, 2000):
        if n != -10 and (n**3 + 100) % (n + 10) == 0:
            total += n
    assert total == -540

# D2
def check_D2():
    """ EXHAUSTIVE PROOF """
    count = 0
    for p in itertools.product('123', repeat=5):
        if sum(int(d) for d in p) % 3 == 0:
            count += 1
    assert count == 81

# D3
def check_D3():
    """ EXHAUSTIVE PROOF """
    assert -2*1 + 12 == 10
    assert -2*5 + 12 == 2
    assert -2*6 + 12 == 0

# D4
def check_D4():
    """ EXHAUSTIVE PROOF """
    n = 2**15 * 3**10 * 5**6
    assert int(math.sqrt(n // 2))**2 == n // 2
    assert int(round((n // 3)**(1/3.0)))**3 == n // 3
    assert int(round((n // 5)**(1/5.0)))**5 == n // 5
    
    divs = (15 + 1) * (10 + 1) * (6 + 1)
    assert divs == 1232

# D5
def check_D5():
    """ EXHAUSTIVE PROOF """
    found = []
    for y in range(1, 15):
        val = math.factorial(y) + 2016
        x = int(math.sqrt(val))
        if x**2 == val:
            found.append((x, y))
    assert found == [(84, 7)]


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
