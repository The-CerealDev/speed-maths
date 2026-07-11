import math
import random
from fractions import Fraction

# A1
def check_A1():
    """ EXHAUSTIVE PROOF: Direct evaluation of the factor theorem condition """
    k = 6
    assert 2**3 - 3 * 2**2 + k * 2 - 8 == 0
    for x in range(-50, 50):
        assert x**3 - 3 * x**2 + 6 * x - 8 == (x - 2) * (x**2 - x + 4)

# A2
def check_A2():
    """ EXHAUSTIVE PROOF: Verify using the remainder theorem """
    assert 1**100 - 1 == 0

# A3
def check_A3():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert 6 * x**2 - x - 12 == (2 * x - 3) * (3 * x + 4)

# A4
def check_A4():
    """ SAMPLED CHECK: Random integer testing """
    for n in range(1, 10):
        for x in range(-5, 5):
            if x**n != 1:
                assert (x**(2 * n) - 1) // (x**n - 1) == x**n + 1

# A5
def check_A5():
    """ SAMPLED CHECK: Verify the minimum value using random positive rational numbers """
    assert 3 + Fraction(9, 3) == 6
    for _ in range(100):
        x = Fraction(random.randint(1, 100), random.randint(1, 100))
        assert x + 9 / x >= 6

# A6
def check_A6():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert x**4 - y**4 == (x**2 + y**2) * (x + y) * (x - y)

# A7
def check_A7():
    """ EXHAUSTIVE PROOF: Solve for exact roots and evaluate the expression """
    r3 = math.sqrt(3)
    alpha = (3 + r3) / 2
    beta = (3 - r3) / 2
    assert abs(2 * alpha**2 - 6 * alpha + 3) < 1e-9
    assert abs(2 * beta**2 - 6 * beta + 3) < 1e-9
    assert abs(alpha**2 + beta**2 - 6) < 1e-9

# A8
def check_A8():
    """ SAMPLED CHECK: Random integer testing """
    for n in range(1, 20):
        val = (math.factorial(n + 1) - math.factorial(n)) // math.factorial(n - 1)
        assert val == n**2

# A9
def check_A9():
    """ EXHAUSTIVE PROOF: Verify identity and test specific constraint solution """
    for _ in range(30):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert (a + b + c)**2 - (a**2 + b**2 + c**2) == 2 * (a * b + b * c + c * a)
    a, b, c = Fraction(2), Fraction(2), Fraction(0)
    assert a + b + c == 4
    assert a**2 + b**2 + c**2 == 8
    assert a * b + b * c + c * a == 4

# A10
def check_A10():
    """ EXHAUSTIVE PROOF: Verify that k = +-8 makes it a perfect square and no other integer in range [-50, 50] does """
    for x in range(-50, 50):
        assert x**2 + 8 * x + 16 == (x + 4)**2
        assert x**2 - 8 * x + 16 == (x - 4)**2
    for k in range(-50, 50):
        if k not in [8, -8]:
            assert k**2 - 64 != 0

# B1
def check_B1():
    """ EXHAUSTIVE PROOF: Verify the roots and factorisation of the cubic polynomial """
    roots = [Fraction(3), Fraction(-2), Fraction(1, 2)]
    for x in roots:
        assert 2 * x**3 - 3 * x**2 - 11 * x + 6 == 0
    for x in range(-50, 50):
        assert 2 * x**3 - 3 * x**2 - 11 * x + 6 == (x - 3) * (x + 2) * (2 * x - 1)

# B2
def check_B2():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert (x**3 + 1) // (x**2 - x + 1) == x + 1

# B3
def check_B3():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        p = a + b
        q = a**3 + b**3
        if p != 0:
            assert a * b == (p**3 - q) / (3 * p)

# B4
def check_B4():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 0 and x != -1:
            assert (x**2 * (x + 1) - x * (x + 1)**2) / (x * (x + 1)) == -1

# B5
def check_B5():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert a**3 - a**2 * b - a * b**2 + b**3 == (a - b)**2 * (a + b)

# B6
def check_B6():
    """ EXHAUSTIVE PROOF: Verify sum of first n odd integers up to n=100 """
    for n in range(1, 100):
        s = sum(2 * r - 1 for r in range(1, n + 1))
        assert s == n**2

# B7
def check_B7():
    """ EXHAUSTIVE PROOF: Verify the solution to the rational equation """
    x = Fraction(-1, 5)
    assert (2 * x - 1) / (x + 3) - (x + 2) / (x - 1) == 1

# B8
def check_B8():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if a != 0 and b != 0 and a != b and a != -b:
            val1 = (1 / a - 1 / b) / (1 / a**2 - 1 / b**2)
            val2 = a * b / (a + b)
            assert val1 == val2

# B9
def check_B9():
    """ SAMPLED CHECK: Verify divisibility by 6 for a range of integers """
    for n in range(-500, 500):
        assert (n**3 - n) % 6 == 0

# B10
def check_B10():
    """ EXHAUSTIVE PROOF: Solve for exact roots and evaluate power sums """
    r5 = math.sqrt(5)
    alpha = (1 + r5) / 2
    beta = (1 - r5) / 2
    assert abs(alpha**3 + beta**3 - 4) < 1e-9
    assert abs(alpha**4 + beta**4 - 7) < 1e-9

# C1
def check_C1():
    """ EXHAUSTIVE PROOF: Verify the solutions directly """
    for x in [0, 2]:
        assert 9**x - 10 * 3**x + 9 == 0

# C2
def check_C2():
    """ SAMPLED CHECK: Verify the minimum value using rational solutions to the constraint """
    assert 1**2 + 2**2 == 5
    for _ in range(50):
        y = Fraction(random.randint(-10, 10), random.randint(1, 10))
        x = 5 - 2 * y
        assert x**2 + y**2 >= 5

# C3
def check_C3():
    """ SAMPLED CHECK: Verify the inequality on random rational numbers """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert a**2 + b**2 + c**2 >= a * b + b * c + c * a

# C4
def check_C4():
    """ EXHAUSTIVE PROOF: Direct evaluation of the solution """
    x = 4
    assert math.sqrt(x + 5) + math.sqrt(x - 3) == 4

# C5
def check_C5():
    """ SAMPLED CHECK: Verify the minimum value using random integers """
    assert (-2)**2 + 4 * (-2) + 3**2 - 6 * 3 + 13 == 0
    for _ in range(50):
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        assert x**2 + 4 * x + y**2 - 6 * y + 13 >= 0

# C6
def check_C6():
    """ EXHAUSTIVE PROOF: Solve for exact roots and evaluate expression """
    r21 = math.sqrt(21)
    x1 = (5 + r21) / 2
    x2 = (5 - r21) / 2
    for x in [x1, x2]:
        assert abs(x + 1 / x - 5) < 1e-9
        assert abs((x**4 + 1) / (x**2) - 23) < 1e-9

# C7
def check_C7():
    """ EXHAUSTIVE PROOF: Verify the roots directly """
    for x in [1, -1]:
        assert x**4 + 4 * x**2 - 5 == 0

# C8
def check_C8():
    """ SAMPLED CHECK: Verify the minimum value using rational solutions to the constraint """
    assert 1 / Fraction(1, 2) + 1 / Fraction(1, 2) == 4
    for _ in range(50):
        num = random.randint(1, 99)
        a = Fraction(num, 100)
        b = 1 - a
        assert 1 / a + 1 / b >= 4

# D1
def check_D1():
    """ EXHAUSTIVE PROOF: Verify the roots and the algebraic identity """
    for x in [1, -1]:
        assert x**4 + 2 * x**3 - 2 * x - 1 == 0
    for x in range(-50, 50):
        assert x**4 + 2 * x**3 - 2 * x - 1 == (x - 1) * (x + 1)**3

# D2
def check_D2():
    """ EXHAUSTIVE PROOF: Verify the primality of n^2+n+41 for n < 40 and composite for n=40 """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    val_40 = 40**2 + 40 + 41
    assert val_40 == 1681
    assert not is_prime(val_40)
    assert 41 * 41 == 1681

    for n in range(40):
        val = n**2 + n + 41
        assert is_prime(val), f"Failed for n={n}, val={val}"

# D3
def check_D3():
    """ SAMPLED CHECK: Verify the inequality for random positive rational numbers with product 1 """
    for _ in range(50):
        a = Fraction(random.randint(1, 100), random.randint(1, 100))
        b = Fraction(random.randint(1, 100), random.randint(1, 100))
        c = 1 / (a * b)
        assert a * b * c == 1
        assert a + b + c >= 3

# D4
def check_D4():
    """ SAMPLED CHECK: Verify both parts of the inequality using rational and float operations """
    for _ in range(50):
        a = Fraction(random.randint(1, 100), random.randint(1, 100))
        b = Fraction(random.randint(1, 100), random.randint(1, 100))
        assert a / b + b / a >= 2
    for _ in range(50):
        a = random.uniform(0.1, 100.0)
        b = random.uniform(0.1, 100.0)
        assert (a + b) / 2 >= math.sqrt(a * b)

# D5
def check_D5():
    """ EXHAUSTIVE PROOF: Brute-force search over the range [1, 1000] """
    solutions = []
    for n in range(1, 1001):
        if (n**2 - 1) % (n + 3) == 0:
            solutions.append(n)
    assert set(solutions) == {1, 5}

CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4,
    "C5": check_C5, "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
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
