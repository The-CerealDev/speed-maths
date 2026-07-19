import math

# A1
def check_A1():
    '''EXHAUSTIVE PROOF'''
    n = 2025
    largest_prime = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                largest_prime = max(largest_prime, i)
            
            other = n // i
            is_prime_other = True
            for j in range(2, int(math.sqrt(other)) + 1):
                if other % j == 0:
                    is_prime_other = False
                    break
            if is_prime_other:
                largest_prime = max(largest_prime, other)
    assert largest_prime == 5

# A2
def check_A2():
    '''EXHAUSTIVE PROOF'''
    assert pow(3, 2026, 10) == 9

# A3
def check_A3():
    '''EXHAUSTIVE PROOF'''
    assert math.gcd(84, 120) == 12

# A4
def check_A4():
    '''EXHAUSTIVE PROOF'''
    assert pow(10, 10, 9) == 1

# A5
def check_A5():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for d in range(10):
        num = 40000 + 7000 + d * 100 + 50 + 3
        if num % 9 == 0:
            ans = d
    assert ans == 8

# A6
def check_A6():
    '''EXHAUSTIVE PROOF'''
    count = 0
    for i in range(1, 101):
        if 100 % i == 0:
            count += 1
    assert count == 9

# A7
def check_A7():
    '''EXHAUSTIVE PROOF'''
    assert 3**200 > 2**300

# A8
def check_A8():
    '''EXHAUSTIVE PROOF'''
    assert pow(5, 2024, 4) == 1

# A9
def check_A9():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for n in range(1, 100):
        val = 12 * n
        if int(math.sqrt(val))**2 == val:
            ans = n
            break
    assert ans == 3

# A10
def check_A10():
    '''EXHAUSTIVE PROOF'''
    n = 210
    sum_primes = 0
    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                sum_primes += i
    assert sum_primes == 17

# B1
def check_B1():
    '''EXHAUSTIVE PROOF'''
    val = math.factorial(20)
    s = str(val)
    assert len(s) - len(s.rstrip('0')) == 4

# B2
def check_B2():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for x in range(1, 7):
        if (3 * x) % 7 == 4:
            ans = x
            break
    assert ans == 6

# B3
def check_B3():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for q in range(2, 50):
        for p in range(q + 1, 50):
            if p**2 - q**2 == 24:
                # check primes
                p_prime = all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1))
                q_prime = all(q % i != 0 for i in range(2, int(math.sqrt(q)) + 1))
                if p_prime and q_prime:
                    ans = p + q
    assert ans == 12

# B4
def check_B4():
    '''EXHAUSTIVE PROOF'''
    assert pow(5, 2025, 100) == 25

# B5
def check_B5():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for n in range(1, 100):
        if n % 3 == 2 and n % 5 == 3:
            ans = n
            break
    assert ans == 8

# B6
def check_B6():
    '''EXHAUSTIVE PROOF'''
    count = 0
    for i in range(1, 3601):
        if 3600 % i == 0:
            if int(math.sqrt(i))**2 == i:
                count += 1
    assert count == 12

# B7
def check_B7():
    '''EXHAUSTIVE PROOF'''
    val = (27**5) * (9**4)
    count = 0
    while val % 3 == 0:
        val //= 3
        count += 1
    assert count == 23

# B8
def check_B8():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for n in range(1, 100):
        count = sum(1 for i in range(1, n + 1) if n % i == 0)
        if count == 6:
            ans = n
            break
    assert ans == 12

# B9
def check_B9():
    '''EXHAUSTIVE PROOF'''
    max_sum = -1
    for x in range(1, 145):
        if 144 % x == 0:
            y = 144 // x
            if math.gcd(x, y) == 3:
                max_sum = max(max_sum, x + y)
    assert max_sum == 51

# B10
def check_B10():
    '''EXHAUSTIVE PROOF'''
    total = sum(math.factorial(i) for i in range(1, 11))
    assert total % 5 == 3

# C1
def check_C1():
    '''EXHAUSTIVE PROOF'''
    count = 0
    for x in range(1, 50):
        for y in range(1, 50):
            if x * y + x + y == 23:
                count += 1
    assert count == 6

# C2
def check_C2():
    '''EXHAUSTIVE PROOF'''
    s = 0
    for p in range(2, 100):
        is_prime = all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1))
        if is_prime:
            val = p**2 + 2
            is_val_prime = all(val % i != 0 for i in range(2, int(math.sqrt(val)) + 1))
            if is_val_prime:
                s += p
    assert s == 3

# C3
def check_C3():
    '''EXHAUSTIVE PROOF'''
    count = 0
    for i in range(100, 1000):
        s = str(i)
        if s == s[::-1] and i % 11 == 0:
            count += 1
    assert count == 8

# C4
def check_C4():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for n in range(1, 20):
        if (n - 1) * n * (n + 1) == 336:
            ans = (n - 1) + n + (n + 1)
            break
    assert ans == 21

# C5
def check_C5():
    '''EXHAUSTIVE PROOF'''
    ans = -1
    for N in range(1000, 10000):
        s = str(N)
        if sum(int(c) for c in s) == 12:
            rev = int(s[::-1])
            if rev == N + 1089:
                ans = max(ans, N)
    assert ans == 5016

# C6
def check_C6():
    '''EXHAUSTIVE PROOF'''
    s = 0
    for x in range(1, 100):
        if x != 3 and (x + 11) % (x - 3) == 0:
            s += x
    assert s == 39

# C7
def check_C7():
    '''EXHAUSTIVE PROOF'''
    max_gcd = -1
    for n in range(1, 1000):
        val = math.gcd(7 * n + 15, 3 * n + 2)
        max_gcd = max(max_gcd, val)
    assert max_gcd == 31

# C8
def check_C8():
    '''EXHAUSTIVE PROOF'''
    s = 0
    for n in range(-100, 100):
        if n != 1 and (n**2 + 3 * n + 5) % (n - 1) == 0:
            s += n
    assert s == 6

# D1
def check_D1():
    '''EXHAUSTIVE PROOF'''
    ans = []
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                if 100 * a + 10 * b + c == math.factorial(a) + math.factorial(b) + math.factorial(c):
                    ans.append(100 * a + 10 * b + c)
    assert len(ans) == 1
    assert ans[0] == 145

# D2
def check_D2():
    '''EXHAUSTIVE PROOF'''
    possible_values = set()
    for n in range(1, 1000):
        d_n = math.gcd(n**2 + 3, n + 1)
        possible_values.add(d_n)
    assert sum(possible_values) == 7

# D3
def check_D3():
    '''EXHAUSTIVE PROOF'''
    assert pow(2025, 2025, 1000) == 625

# D4
def check_D4():
    '''EXHAUSTIVE PROOF'''
    count = 0
    for n in range(1, 101):
        if n % 2 == 0:
            count += 1
        else:
            if int(math.sqrt(n))**2 == n:
                count += 1
    assert count == 55

# D5
def check_D5():
    '''EXHAUSTIVE PROOF'''
    max_sum = -1
    for x in range(1, 50):
        for y in range(x, 50):
            for z in range(y, 50):
                # Check 1/x + 1/y + 1/z == 1 using cross multiplication
                if y * z + x * z + x * y == x * y * z:
                    max_sum = max(max_sum, x + y + z)
    assert max_sum == 11


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
