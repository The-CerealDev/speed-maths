import math
import random
from fractions import Fraction

# Section A
def check_A1():
    for x in range(-50, 50):
        assert x**5 - x == x*(x - 1)*(x + 1)*(x**2 + 1)

def check_A2():
    for _ in range(50):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        assert (a+b+c)**2 - (a**2+b**2+c**2) == 2*(a*b + b*c + c*a)
    assert 2 * 4 == 8

def check_A3():
    assert 7**2 - 5**2 + 3**2 - 1**2 == 32

def check_A4():
    r13 = math.sqrt(13)
    p = 4 + r13
    q = 4 - r13
    val = (p - 1/p) * (q - 1/q)
    assert abs(val - (-16)) < 1e-9

def check_A5():
    for n in range(1, 20):
        assert math.factorial(2*n) // math.factorial(2*n - 1) - math.factorial(n) // math.factorial(n - 1) == n

def check_A6():
    for x in range(-50, 50):
        assert 27*x**3 - 8 == (3*x - 2)*(9*x**2 + 6*x + 4)

def check_A7():
    for _ in range(50):
        x = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        t = x - Fraction(1, x)
        assert t**2 + 4 == (x + Fraction(1, x))**2

def check_A8():
    assert math.log2(8) + math.log2(4) - math.log2(32) == 0

def check_A9():
    def f(x): return 2*x + 1
    def g(x): return x**2 - 1
    for x in range(-50, 50):
        assert f(g(x)) - g(f(x)) == -2*x**2 - 4*x - 1

def check_A10():
    for _ in range(50):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        if a != b and a != c:
            assert Fraction(a**2 - b**2, a - b) - Fraction(a**2 - c**2, a - c) == b - c

# Section B
def check_B1():
    for n in range(2, 20):
        prod = Fraction(1)
        for k in range(2, n + 1):
            prod *= (1 - Fraction(1, k))
        assert prod == Fraction(1, n)
    prod = Fraction(1)
    for k in range(2, 101):
        prod *= (1 - Fraction(1, k))
    assert prod == Fraction(1, 100)

def check_B2():
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x**2 - x - 2 != 0 and x**2 + 6*x + 5 != 0 and x + 1 != 0:
            val = (Fraction(x**2 + 3*x - 10, x**2 - x - 2)) * (Fraction(x**2 + x - 2, x**2 + 6*x + 5))
            ans = Fraction((x + 2)*(x - 1), (x + 1)**2)
            assert val == ans

def check_B3():
    a, b, c = 1, -1, 2
    assert a + b + c == 2
    assert a**2 + b**2 + c**2 == 6
    assert a*b*c == -2
    assert a**3 + b**3 + c**3 == 8

def check_B4():
    for x in range(-50, 50):
        assert x**4 + 4 == (x**2 + 2*x + 2)*(x**2 - 2*x + 2)

def check_B5():
    def f(x): return Fraction(2*x + 1, x - 1)
    def f_inv(x): return Fraction(x + 1, x - 2)
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(1, 10))
        if x != 1 and x != 2 and f(x) != 2:
            assert f_inv(f(x)) == x
            assert f(f_inv(x)) == x

def check_B6():
    for n in range(-20, 20):
        prod = (n - 1) * n * (n + 1) * (n + 2)
        assert prod == (n**2 + n - 1)**2 - 1

def check_B7():
    for _ in range(50):
        x = Fraction(random.randint(-10, 10), random.randint(2, 10))
        if x**8 != 1 and x != 1 and x != -1:
            val = Fraction(1, 1 + x) + Fraction(1, 1 - x) + Fraction(2, 1 + x**2) + Fraction(4, 1 + x**4)
            assert val == Fraction(8, 1 - x**8)

def check_B8():
    a, b, c = 1, 2, -3
    assert a + b + c == 0
    p = -7
    q = 6
    assert a**3 + b**3 + c**3 == -18
    assert -3*q == -18

def check_B9():
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = -a - b
        assert (a**2 + b**2 + c**2)**2 == 2*(a**4 + b**4 + c**4)

def check_B10():
    for x in [Fraction(7, 2), Fraction(-5, 2)]:
        assert Fraction(x + 1, x - 2) + Fraction(x - 2, x + 1) == Fraction(10, 3)

# Section C
def check_C1():
    for _ in range(50):
        x = random.uniform(0.1, 10.0)
        y = random.uniform(0.1, 10.0)
        assert x/3 + 2*y/3 >= (x**(1/3)) * (y**(2/3)) - 1e-9

def check_C2():
    for x, y in [(Fraction(3, 2), Fraction(-1, 2)), (Fraction(-1, 2), Fraction(3, 2))]:
        assert x + y == 1
        assert x**4 + y**4 == Fraction(41, 8)

def check_C3():
    for _ in range(50):
        a = random.uniform(0.1, 10.0)
        b = random.uniform(0.1, 10.0)
        v1 = math.sqrt((a**2 + b**2)/2)
        v2 = (a + b)/2
        v3 = math.sqrt(a * b)
        v4 = 2 * a * b / (a + b)
        assert v1 >= v2 - 1e-9
        assert v2 >= v3 - 1e-9
        assert v3 >= v4 - 1e-9

def check_C4():
    for x in [1, 0]:
        assert 27**x + 27**(1-x) == 28

def check_C5():
    for _ in range(50):
        a = random.uniform(0.01, 0.98)
        b = random.uniform(0.01, 0.99 - a)
        c = 1 - a - b
        if a > 0 and b > 0 and c > 0:
            assert 1/a + 1/b + 1/c >= 9 - 1e-9

def check_C6():
    assert sum(k**3 for k in range(3, 11)) == 3016

def check_C7():
    for _ in range(50):
        x = random.uniform(-10.0, 10.0)
        assert abs(abs(x**2 - 4) - abs(x - 2) * abs(x + 2)) < 1e-9

def check_C8():
    x = Fraction(8, 3)
    y = Fraction(4, 3)
    assert x + y == 4
    assert x**2 * y == Fraction(256, 27)
    for _ in range(50):
        xt = random.uniform(0.1, 3.9)
        yt = 4 - xt
        assert xt**2 * yt <= 256/27 + 1e-9

# Section D
def check_D1():
    a = 8
    b = 2
    k = 4
    assert a**2 + b**2 == k*(a*b + 1)

def check_D2():
    for c in [-2, -1, 1, 2]:
        def p(x): return c * x * (x - 1) * (x + 1)
        for x in range(-10, 10):
            assert (x - 1) * p(x + 1) == (x + 2) * p(x)

def check_D3():
    a, b, c = Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)
    val = a/(1 - a) + b/(1 - b) + c/(1 - c)
    assert val == Fraction(3, 2)
    for _ in range(50):
        at = random.uniform(0.01, 0.98)
        bt = random.uniform(0.01, 0.99 - at)
        ct = 1 - at - bt
        if at > 0 and bt > 0 and ct > 0:
            assert at/(1 - at) + bt/(1 - bt) + ct/(1 - ct) >= 1.5 - 1e-9

def check_D4():
    prod = Fraction(1)
    for n in range(2, 100):
        prod *= Fraction(n**3 - 1, n**3 + 1)
    N = 99
    assert prod == Fraction(2*(N**2 + N + 1), 3*N*(N + 1))
    assert abs(float(prod) - 2/3) < 0.02

def check_D5():
    for n in range(-10, 10):
        assert n**3 + (-n)**3 == (n + -n)**2
    for x, y in [(1,0), (0,1), (1,2), (2,1), (2,2)]:
        assert x**3 + y**3 == (x + y)**2
    for x in range(-50, 50):
        for y in range(-50, 50):
            if x**3 + y**3 == (x + y)**2:
                assert (x == -y) or ((x, y) in [(1,0), (0,1), (1,2), (2,1), (2,2)])

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
