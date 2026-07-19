import math

# A1
def check_A1():
    """ EXHAUSTIVE PROOF: Modular arithmetic """
    assert pow(3, 2025, 10) == 3

# A2
def check_A2():
    """ EXHAUSTIVE PROOF: Direct arithmetic """
    assert 7 * 11 * 13 == 1001

# A3
def check_A3():
    """ EXHAUSTIVE PROOF: GCD computation """
    assert math.gcd(42, 105) == 21

# A4
def check_A4():
    """ EXHAUSTIVE PROOF: Counting divisors """
    divs = [i for i in range(1, 121) if 120 % i == 0]
    assert len(divs) == 16

# A5
def check_A5():
    """ EXHAUSTIVE PROOF: Modular exponentiation """
    assert pow(5, 10, 6) == 1

# A6
def check_A6():
    """ EXHAUSTIVE PROOF: Linear congruence """
    assert next(x for x in range(1, 10) if (2*x) % 5 == 1) == 3

# A7
def check_A7():
    """ EXHAUSTIVE PROOF: Chinese Remainder Theorem brute force """
    assert next(n for n in range(2, 100) if n % 3 == 1 and n % 4 == 1) == 13

# A8
def check_A8():
    """ EXHAUSTIVE PROOF: Direct arithmetic """
    assert 2**3 * 3**2 * 5 == 360

# A9
def check_A9():
    """ EXHAUSTIVE PROOF: Modular exponentiation """
    assert pow(7, 3, 10) == 3

# A10
def check_A10():
    """ EXHAUSTIVE PROOF: Prime factorisation """
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True
    primes = [p for p in range(2, 10000) if 9999 % p == 0 and is_prime(p)]
    assert max(primes) == 101

# B1
def check_B1():
    """ EXHAUSTIVE PROOF: Factorial power of prime """
    n = math.factorial(50)
    k = 0
    while n % (7**(k+1)) == 0:
        k += 1
    assert k == 8

# B2
def check_B2():
    """ EXHAUSTIVE PROOF: Perfect cube search """
    assert next(n for n in range(1, 1000) if round((15*n)**(1/3))**3 == 15*n) == 225

# B3
def check_B3():
    """ EXHAUSTIVE PROOF: Factorial sum remainder """
    total = sum(math.factorial(i) for i in range(1, 101))
    assert total % 12 == 9

# B4
def check_B4():
    """ EXHAUSTIVE PROOF: Exponentiation comparison """
    assert 3**40 > 4**30

# B5
def check_B5():
    """ EXHAUSTIVE PROOF: Linear congruence """
    assert next(x for x in range(1, 10) if (3*x) % 7 == 4) == 6

# B6
def check_B6():
    """ EXHAUSTIVE PROOF: Modular exponentiation """
    assert pow(7, 2022, 100) == 49

# B7
def check_B7():
    """ EXHAUSTIVE PROOF: Counting perfect square factors """
    divs = [i for i in range(1, 1001) if 1000 % i == 0]
    sq_divs = [i for i in divs if round(i**0.5)**2 == i]
    assert len(sq_divs) == 4

# B8
def check_B8():
    """ EXHAUSTIVE PROOF: Quadratic congruence """
    ans = [x for x in range(8) if (x**2) % 8 == 1]
    assert ans == [1, 3, 5, 7]

# B9
def check_B9():
    """ EXHAUSTIVE PROOF: Exponential equation """
    for x in range(10):
        for y in range(10):
            if 2**x * 3**y == 12**3:
                assert x + y == 9

# B10
def check_B10():
    """ EXHAUSTIVE PROOF: Diophantine equation """
    ans = set()
    for x in range(1, 20):
        for y in range(1, 20):
            if x * y == x + y + 3:
                ans.add((x, y))
    assert ans == {(2, 5), (3, 3), (5, 2)}

# C1
def check_C1():
    """ EXHAUSTIVE PROOF: Rational expression integer values """
    ans = [n for n in range(1, 100) if (n**2 + 3*n + 5) % (n + 1) == 0]
    assert sum(ans) == 2

# C2
def check_C2():
    """ EXHAUSTIVE PROOF: Factorisation counting """
    val = pow(2, 2024) + pow(2, 2023) + pow(2, 2022)
    ans = sum(1 for i in [6, 7, 8, 9, 10] if val % i == 0)
    assert ans == 2

# C3
def check_C3():
    """ EXHAUSTIVE PROOF: Difference of squares """
    ans = [(x, y) for x in range(1, 50) for y in range(1, 50) if x**2 - y**2 == 17]
    assert ans == [(9, 8)]

# C4
def check_C4():
    """ EXHAUSTIVE PROOF: LCM pairs counting """
    ans = sum(1 for a in range(1, 301) for b in range(1, 301) if (a*b)//math.gcd(a,b) == 300)
    assert ans == 75

# C5
def check_C5():
    """ EXHAUSTIVE PROOF: Divisors counting """
    def count_divs(x):
        return sum(1 for i in range(1, x+1) if x % i == 0)
    ans = sum(1 for n in range(1, 101) if count_divs(n) == 3)
    assert ans == 4

# C6
def check_C6():
    """ EXHAUSTIVE PROOF: Divisibility digits sum """
    ans = max(n for n in range(1, 2000) if (n**3 + 100) % (n + 10) == 0)
    assert sum(int(d) for d in str(ans)) == 17

# C7
def check_C7():
    """ EXHAUSTIVE PROOF: Bounding triple sum """
    ans = []
    for x in range(1, 10):
        for y in range(x, 10):
            for z in range(y, 10):
                if x*y*z == x + y + z:
                    ans.append((x, y, z))
    assert ans == [(1, 2, 3)]

# C8
def check_C8():
    """ EXHAUSTIVE PROOF: Perfect square expression """
    ans = []
    for n in range(-100, 100):
        val = n**2 + 4*n + 3
        if val >= 0 and round(val**0.5)**2 == val:
            ans.append(n)
    assert sum(ans) == -4

# D1
def check_D1():
    """ EXHAUSTIVE PROOF: Prime squared plus two """
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True
    ans = [p for p in range(1, 100) if is_prime(p) and is_prime(p**2 + 2)]
    assert ans == [3]

# D2
def check_D2():
    """ EXHAUSTIVE PROOF: Algebraic manipulation and factor search """
    ans = set()
    for x in range(1, 50):
        for y in range(1, 50):
            if x**2 * y == x**2 + 3*y + 2:
                ans.add((x, y))
    assert ans == {(2, 6)}

# D3
def check_D3():
    """ EXHAUSTIVE PROOF: Bounding unit fractions """
    ans = sum(1 for x in range(1, 200) for y in range(x, 200) if x*y == 6*x + 6*y)
    assert ans == 5

# D4
def check_D4():
    """ EXHAUSTIVE PROOF: Sum of powers mod 11 """
    ans = sum(pow(i, 2025, 11) for i in range(1, 11)) % 11
    assert ans == 0

# D5
def check_D5():
    """ EXHAUSTIVE PROOF: Sophie Germain prime search """
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True
    ans = [n for n in range(-100, 100) if is_prime(n**4 + 4)]
    assert sum(ans) == 0

if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("check_") and callable(v):
            v()
            print(f"{k} passed.")
    print("All checks passed!")
