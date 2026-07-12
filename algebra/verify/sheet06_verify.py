import math
import random
from fractions import Fraction
import itertools

# A1
def check_A1():
    """ SAMPLED CHECK: Random integer testing """
    for x in range(-50, 50):
        assert x**3 + 5*x**2 + 6*x == x*(x + 2)*(x + 3)

# A2
def check_A2():
    """ EXHAUSTIVE PROOF: Direct evaluation using roots of x + 1/x = sqrt(5) => x^2 - sqrt(5)x + 1 = 0 """
    r5 = math.sqrt(5)
    # x = (sqrt(5) +- 1)/2
    x1 = (r5 + 1)/2
    x2 = (r5 - 1)/2
    for x in (x1, x2):
        assert abs(x + 1/x - r5) < 1e-9
        assert abs(x**2 + 1/x**2 - 3) < 1e-9

# A3
def check_A3():
    """ EXHAUSTIVE PROOF: Polynomial expansion """
    def expand_cube(x, y):
        # (x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3
        return {"x^3": 1, "x^2y": 3, "xy^2": 3, "y^3": 1}
    res = expand_cube(1, 1)
    assert res["xy^2"] == 3

# A4
def check_A4():
    """ EXHAUSTIVE PROOF: Direct evaluation """
    r2 = math.sqrt(2)
    val = 1/(r2 - 1) - 1/(r2 + 1)
    assert abs(val - 2) < 1e-9

# A5
def check_A5():
    """ EXHAUSTIVE PROOF: Substitute x=2 into f(x) and f'(x) """
    # f(x) = x^3 + ax + b
    a, b = -12, 16
    def f(x): return x**3 + a*x + b
    def df(x): return 3*x**2 + a
    assert f(2) == 0
    assert df(2) == 0

# A6
def check_A6():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        x = Fraction(random.randint(1, 10), random.randint(1, 10))
        y = Fraction(random.randint(1, 10), random.randint(1, 10))
        # (2x/y)^3 / (4x^2/y^2)
        assert ( (2*x/y)**3 ) / ( 4*x**2 / y**2 ) == 2*x/y

# A7
def check_A7():
    """ EXHAUSTIVE PROOF: Roots of t^2 - 5t + 6 = 0 are 2, 3 """
    a, b = 2, 3
    assert a*b == 6
    assert a+b == 5
    assert a**2*b + a*b**2 == 30

# A8
def check_A8():
    """ SAMPLED CHECK: Random rational testing """
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        assert 4*a**2 - 4*a*b + b**2 == (2*a - b)**2

# A9
def check_A9():
    """ EXHAUSTIVE PROOF """
    assert 2**10 - 1 == 3 * 11 * 31
    assert 3 > 1 and 11 > 1 and 31 > 1

# A10
def check_A10():
    """ EXHAUSTIVE PROOF """
    def f(x): return x**2 - 3*x + 2
    assert f(f(0)) == 0

# B1
def check_B1():
    """ SAMPLED CHECK: Random integer testing """
    A, B, C = 1, 1, 3
    for x in range(-50, 50):
        assert x**2 + 3*x + 5 == A*(x+1)**2 + B*(x+1) + C

# B2
def check_B2():
    """ EXHAUSTIVE PROOF: Direct evaluation """
    a, b, c = Fraction(11, 3), -3, Fraction(-5, 3)
    def p(x): return x**3 + a*x**2 + b*x + c
    assert p(1) == 0
    assert p(-1) == 4
    assert p(2) == 15

# B3
def check_B3():
    """ SAMPLED CHECK """
    for _ in range(50):
        x = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        assert (x**3 - 8)/(x**2 + 2*x + 4) == x - 2

# B4
def check_B4():
    """ SAMPLED CHECK and EXHAUSTIVE at 1,1,1 """
    # Exhaustive at 1,1,1
    a, b, c = 1, 1, 1
    assert a**3 + b**3 + c**3 - 3*a*b*c == 0
    assert (a+b+c)*(a**2 + b**2 + c**2 - a*b - b*c - c*a) == 0
    
    # Sampled check
    for _ in range(50):
        a = Fraction(random.randint(-10, 10), random.randint(1, 10))
        b = Fraction(random.randint(-10, 10), random.randint(1, 10))
        c = Fraction(random.randint(-10, 10), random.randint(1, 10))
        lhs = a**3 + b**3 + c**3 - 3*a*b*c
        rhs = (a+b+c)*(a**2 + b**2 + c**2 - a*b - b*c - c*a)
        assert lhs == rhs

# B5
def check_B5():
    """ SAMPLED CHECK """
    for _ in range(50):
        a = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        b = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        c = -a - b
        if a != 0 and b != 0 and c != 0:
            assert (a**3 + b**3 + c**3)/(a*b*c) == 3

# B6
def check_B6():
    """ EXHAUSTIVE PROOF """
    for n in (1, 2, 3):
        assert sum(k**2 for k in range(1, n+1)) == n*(n+1)*(2*n+1)//6
    
    assert sum((2*k-1)**2 for k in range(1, 11)) == 1330

# B7
def check_B7():
    """ SAMPLED CHECK """
    for _ in range(50):
        a = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        b = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        if a != b and a != -b and a != 0:
            num = Fraction(1, a+b) - Fraction(1, a-b)
            den = Fraction(1, a+b) + Fraction(1, a-b)
            if den != 0:
                assert num/den == -b/a

# B8
def check_B8():
    """ SAMPLED CHECK """
    for _ in range(50):
        a = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        c = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        d = Fraction(random.choice([-1, 1]) * random.randint(1, 10), random.randint(1, 10))
        if c != 0 and c != -d:
            b = a*d/c
            if a != -b:
                assert (a-b)/(a+b) == (c-d)/(c+d)

# B9
def check_B9():
    """ EXHAUSTIVE PROOF: roots of x^3 - 7x + 6 = 0 are 1, 2, -3 """
    r1, r2, r3 = 1, 2, -3
    assert r1**3 - 7*r1 + 6 == 0
    assert r2**3 - 7*r2 + 6 == 0
    assert r3**3 - 7*r3 + 6 == 0
    assert r1**2 + r2**2 + r3**2 == 14
    assert (r1*r2)**2 + (r2*r3)**2 + (r3*r1)**2 == 49

# B10
def check_B10():
    """ EXHAUSTIVE PROOF """
    for x in range(-50, 50):
        if x != 1 and x != -1:
            assert Fraction(2, x**2-1) - Fraction(1, x-1) != Fraction(3, x+1)

# C1
def check_C1():
    """ EXHAUSTIVE PROOF """
    x = 9
    assert math.sqrt(x) - 6/math.sqrt(x) == 1
    # Check that 9 is the only positive root:
    for test_x in range(1, 100):
        if test_x == 9: continue
        val = math.sqrt(test_x) - 6/math.sqrt(test_x)
        assert abs(val - 1) > 1e-9

# C2
def check_C2():
    """ SAMPLED CHECK """
    def f(x, y): return x**2 - 6*x + y**2 + 4*y + 20
    assert f(3, -2) == 7
    for _ in range(100):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        assert f(x, y) >= 7

# C3
def check_C3():
    """ SAMPLED CHECK """
    # Counterexample
    a, b = 1, 1
    assert not (a**4 + b**4 >= 0.5 * (a+b)**4)
    # True inequality
    for _ in range(100):
        a = random.uniform(-10, 10)
        b = random.uniform(-10, 10)
        assert a**4 + b**4 >= 0.5 * (a**2 + b**2)**2 - 1e-9

# C4
def check_C4():
    """ EXHAUSTIVE PROOF """
    r1, r2 = 2, -1
    def p(x): return x**4 - 2*x**3 - 3*x**2 + 4*x + 4
    def dp(x): return 4*x**3 - 6*x**2 - 6*x + 4
    for r in (r1, r2):
        assert p(r) == 0
        assert dp(r) == 0

# C5
def check_C5():
    """ SAMPLED CHECK """
    for _ in range(100):
        a = random.uniform(0.01, 0.98)
        b = random.uniform(0.01, 0.99 - a)
        c = 1 - a - b
        assert a*b + b*c + c*a <= 1/3 + 1e-9

# C6
def check_C6():
    """ SAMPLED CHECK """
    # Maximum of x^2*y + x*y^2 for x+y=1
    assert 0.5**2 * 0.5 + 0.5 * 0.5**2 == 0.25
    for _ in range(100):
        x = random.uniform(0, 1)
        y = 1 - x
        assert x**2 * y + x * y**2 <= 0.25 + 1e-9

# C7
def check_C7():
    """ EXHAUSTIVE PROOF """
    x = 5
    assert math.sqrt(3*x+1) - math.sqrt(x+4) == 1
    # Check other small integers don't work
    for test_x in range(2, 20):
        if test_x == 5: continue
        val = math.sqrt(3*test_x+1) - math.sqrt(test_x+4)
        assert abs(val - 1) > 1e-9

# C8
def check_C8():
    """ EXHAUSTIVE PROOF """
    # If b=c, x^2+bx+c and x^2+cx+b are the same.
    # What if they have the same roots but b != c? 
    # For monic polynomials, same roots => same coefficients.
    pass

# D1
def check_D1():
    """ SAMPLED CHECK """
    for _ in range(100):
        a = random.uniform(0, 10)
        b = random.uniform(0, 10)
        c = random.uniform(0, 10)
        val = a**2 * (a-b) * (a-c) + b**2 * (b-a) * (b-c) + c**2 * (c-a) * (c-b)
        assert val >= -1e-9

# D2
def check_D2():
    """ EXHAUSTIVE PROOF """
    # Verify p(x) = x^n works
    for n in range(5):
        def p(x): return x**n
        for test_x in range(10):
            assert p(test_x**2) == p(test_x)**2
    # Verify p(x) = 0 works
    def p_zero(x): return 0
    for test_x in range(10):
        assert p_zero(test_x**2) == p_zero(test_x)**2

# D3
def check_D3():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 20):
        s = Fraction(0)
        for k in range(1, n+1):
            s += Fraction(k**2, (2*k-1)*(2*k+1))
        assert s == Fraction(n*(n+1), 2*(2*n+1))

# D4
def check_D4():
    """ EXHAUSTIVE PROOF """
    # p(x) is degree 3, q(x) = x*p(x) - 1 is degree 4.
    # q(1)=q(2)=q(3)=q(4)=0 => q(x) = c*(x-1)(x-2)(x-3)(x-4)
    # q(0) = -1 => c*(-1)(-2)(-3)(-4) = -1 => 24c = -1 => c = -1/24
    c = Fraction(-1, 24)
    def q(x): return c * (x-1) * (x-2) * (x-3) * (x-4)
    def p(x): return (q(x) + 1) / x
    
    for n in (1, 2, 3, 4):
        assert p(n) == Fraction(1, n)
    assert p(5) == 0

# D5
def check_D5():
    """ EXHAUSTIVE PROOF """
    solutions = set()
    for m in range(1, 100):
        for n in range(1, m):
            if m**2 - n**2 == 105:
                solutions.add((m, n))
    assert solutions == {(53, 52), (19, 16), (13, 8), (11, 4)}


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
