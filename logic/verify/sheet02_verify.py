"""Computational verification for logic/sheets/sheet02.tex + answers/ans02.tex.

Sheet 2's toolkit is necessary/sufficient conditions. Every question reduces
to: does condition => target hold (sufficient), does target => condition
hold (necessary), over a finite integer range or a dense finite grid of
rationals standing in for the reals. Abstract P/Q/R transitivity questions
are checked by exhaustively enumerating all consistent boolean models.

stdlib only. Run: python3 sheet02_verify.py
"""

import math
import itertools
from fractions import Fraction

# ── shared helpers ──────────────────────────────────────────────────────────

def implies(a, b):
    return (not a) or b

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def lcm(a, b):
    return a * b // math.gcd(a, b)

def num_divisors(n):
    cnt = 0
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            cnt += 1 if d * d == n else 2
    return cnt

def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_rectangle(w, h):
    return w > 0 and h > 0

def is_square(w, h):
    return is_rectangle(w, h) and w == h

def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b

def is_isosceles(a, b, c):
    return is_triangle(a, b, c) and (a == b or b == c or a == c)

def is_equilateral(a, b, c):
    return is_triangle(a, b, c) and a == b == c

def is_leap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    return y % 4 == 0

REAL_GRID = [Fraction(i, 10) for i in range(-3000, 3001)]        # -300.0 .. 300.0 step 0.1, exact
HALF_GRID = [Fraction(i, 2) for i in range(-400, 401)]            # -200.0 .. 200.0 step 0.5, exact


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: "n div by 4" sufficient for "n div by 2" -- Yes
def check_A1():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 4 == 0
    T = lambda n: n % 2 == 0
    domain = range(-2000, 2001)
    for n in domain:
        assert implies(H(n), T(n))
    assert any(H(n) for n in domain)      # not vacuous
    assert 4 == 2 * 2                     # method's stated identity


# A2: "n div by 4" necessary for "n div by 2" -- No, n=2 counterexample
def check_A2():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 4 == 0
    T = lambda n: n % 2 == 0
    domain = range(-2000, 2001)
    n = 2
    assert T(n) and not H(n)
    assert not all(implies(T(n2), H(n2)) for n2 in domain)


# A3: "x=3" sufficient for "x^2=9" -- Yes
def check_A3():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x == 3
    T = lambda x: x**2 == 9
    for x in HALF_GRID:
        assert implies(H(x), T(x))
    assert any(H(x) for x in HALF_GRID)


# A4: "x=3" necessary for "x^2=9" -- No, x=-3 counterexample
def check_A4():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x == 3
    T = lambda x: x**2 == 9
    x = Fraction(-3)
    assert T(x) and not H(x)
    assert not all(implies(T(x2), H(x2)) for x2 in HALF_GRID)


# A5: "rectangle" necessary for "square" -- True
def check_A5():
    """ EXHAUSTIVE PROOF """
    for w in range(1, 101):
        for h in range(1, 101):
            if is_square(w, h):
                assert is_rectangle(w, h)
    assert any(is_square(w, h) for w in range(1, 101) for h in range(1, 101))


# A6: "rectangle" sufficient for "square" -- False, 2x3 counterexample
def check_A6():
    """ EXHAUSTIVE PROOF """
    assert is_rectangle(2, 3) and not is_square(2, 3)
    found = any(is_rectangle(w, h) and not is_square(w, h)
                for w in range(1, 101) for h in range(1, 101))
    assert found


# A7: "n=6" sufficient for "n mult of 3" -- Yes
def check_A7():
    """ EXHAUSTIVE PROOF """
    n = 6
    assert n % 3 == 0
    assert n == 3 * 2


# A8: "n=6" necessary for "n mult of 3" -- No, n=9 counterexample
def check_A8():
    """ EXHAUSTIVE PROOF """
    n = 9
    assert n % 3 == 0 and n != 6
    domain = range(1, 1000)
    counterexamples = [m for m in domain if m % 3 == 0 and m != 6]
    assert 9 in counterexamples


# A9: "n even" necessary for "n div by 4" -- True
def check_A9():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 4 == 0   # "div by 4"
    T = lambda n: n % 2 == 0   # "even"
    domain = range(-2000, 2001)
    for n in domain:
        assert implies(H(n), T(n))
    assert 4 == 2 * 2
    assert any(H(n) for n in domain)


# A10: "n even" sufficient for "n div by 4" -- False, n=2 counterexample
def check_A10():
    """ EXHAUSTIVE PROOF """
    n = 2
    assert n % 2 == 0 and n % 4 != 0
    domain = range(-2000, 2001)
    assert not all(implies(m % 2 == 0, m % 4 == 0) for m in domain)


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: "x>5" as condition for "x>0" -- sufficient but not necessary
def check_B1():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x > 5
    T = lambda x: x > 0
    for x in REAL_GRID:
        assert implies(H(x), T(x))
    assert any(H(x) for x in REAL_GRID)
    x = Fraction(1)
    assert T(x) and not H(x)
    assert not all(implies(T(x2), H(x2)) for x2 in REAL_GRID)


# B2: "n div by 6" as condition for "2|n and 3|n" -- necessary and sufficient
def check_B2():
    """ EXHAUSTIVE PROOF """
    assert math.gcd(2, 3) == 1
    assert lcm(2, 3) == 6
    H = lambda n: n % 6 == 0
    T = lambda n: (n % 2 == 0) and (n % 3 == 0)
    domain = range(-10000, 10001)
    for n in domain:
        assert H(n) == T(n)


# B3: "ab=0" as condition for "a=0" -- necessary but not sufficient
def check_B3():
    """ EXHAUSTIVE PROOF """
    grid = [Fraction(i, 4) for i in range(-40, 41)]
    for a in grid:
        for b in grid:
            if a == 0:
                assert a * b == 0
    a, b = Fraction(1), Fraction(0)
    assert a * b == 0 and a != 0


# B4: "n^2 even" as condition for "n even" -- necessary and sufficient
def check_B4():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n**2 % 2 == 0
    T = lambda n: n % 2 == 0
    domain = range(-5000, 5001)
    for n in domain:
        assert H(n) == T(n)


# B5: "x is an integer" as condition for "x is rational" -- sufficient but not necessary
def check_B5():
    """ EXHAUSTIVE PROOF """
    def is_integer_frac(x):
        return x.denominator == 1
    grid = [Fraction(n) for n in range(-500, 501)]
    for x in grid:
        assert is_integer_frac(x)                          # sanity: genuinely integers
        assert x == Fraction(x.numerator, x.denominator)    # manifestly a ratio of integers
    half = Fraction(1, 2)
    assert not is_integer_frac(half)
    assert half.numerator == 1 and half.denominator == 2    # a rational, non-integer witness


# B6: "equilateral" as condition for "isosceles" -- sufficient but not necessary
def check_B6():
    """ EXHAUSTIVE PROOF """
    for s in range(1, 51):
        assert is_equilateral(s, s, s)
        assert is_isosceles(s, s, s)
    a, b, c = 3, 3, 5
    assert is_triangle(a, b, c)
    assert is_isosceles(a, b, c) and not is_equilateral(a, b, c)


# B7: P=>Q, Q=>R both true => P sufficient for R
def check_B7():
    """ EXHAUSTIVE PROOF """
    models = [(P, Q, R) for P, Q, R in itertools.product([False, True], repeat=3)
              if implies(P, Q) and implies(Q, R)]
    assert len(models) > 0
    for P, Q, R in models:
        assert implies(P, R)
    # without the two hypotheses, P=>R does not hold for every assignment
    assert any(P and not R for P, Q, R in itertools.product([False, True], repeat=3))


# B8: 9|n => 3|n => digitsum%3==0, so 9|n sufficient for digitsum%3==0
def check_B8():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)
    for n in domain:
        assert n % 3 == digit_sum(n) % 3                          # underlying digit-sum fact
    H = lambda n: n % 9 == 0
    T = lambda n: digit_sum(n) % 3 == 0
    for n in domain:
        assert implies(n % 9 == 0, n % 3 == 0)                    # first link
        assert implies(n % 3 == 0, T(n))                          # second link
        assert implies(H(n), T(n))                                # chained sufficiency
    assert any(H(n) for n in domain)


# B9: weakest of {8|n, 4|n, 2|n} (each sufficient for "n even") is 2|n
def check_B9():
    """ EXHAUSTIVE PROOF """
    a = lambda n: n % 8 == 0
    b = lambda n: n % 4 == 0
    c = lambda n: n % 2 == 0
    even = lambda n: n % 2 == 0
    domain = range(-5000, 5001)
    for n in domain:
        assert implies(a(n), even(n))
        assert implies(b(n), even(n))
        assert implies(c(n), even(n))
        assert implies(a(n), b(n))     # 8|n => 4|n
        assert implies(b(n), c(n))     # 4|n => 2|n
        assert c(n) == even(n)         # (c) coincides exactly with the target: nec & suff
    assert 8 == 4 * 2 and 4 == 2 * 2


# B10: strongest of {2|n, 4|n, 8|n} (each necessary for "24|n") is 8|n
def check_B10():
    """ EXHAUSTIVE PROOF """
    a = lambda n: n % 2 == 0
    b = lambda n: n % 4 == 0
    c = lambda n: n % 8 == 0
    target = lambda n: n % 24 == 0
    domain = range(-5000, 5001)
    for n in domain:
        assert implies(target(n), a(n))
        assert implies(target(n), b(n))
        assert implies(target(n), c(n))
        assert implies(c(n), b(n))     # 8|n => 4|n
        assert implies(b(n), a(n))     # 4|n => 2|n
    assert 24 == 8 * 3


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: "n div by 6" for "2|n and 3|n" -- C) necessary and sufficient
def check_C1():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 6 == 0
    T = lambda n: (n % 2 == 0) and (n % 3 == 0)
    domain = range(-10000, 10001)
    suff = all(implies(H(n), T(n)) for n in domain)
    nec = all(implies(T(n), H(n)) for n in domain)
    assert suff and nec
    optA = nec and not suff
    optB = suff and not nec
    optC = suff and nec
    optD = (not suff) and (not nec)
    assert (optA, optB, optC, optD) == (False, False, True, False)


# C2: "4|n" necessary and sufficient for "n even and n/2 even"
def check_C2():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 4 == 0
    T = lambda n: (n % 2 == 0) and ((n // 2) % 2 == 0)
    domain = range(-10000, 10001)
    for n in domain:
        assert H(n) == T(n)
    for k in range(-2000, 2001):
        n = 4 * k
        assert n % 2 == 0
        assert n // 2 == 2 * k
        assert (n // 2) % 2 == 0


# C3: "x^2<4" as condition for "x<2" -- sufficient but not necessary
def check_C3():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x**2 < 4
    T = lambda x: x < 2
    for x in REAL_GRID:
        assert H(x) == (Fraction(-2) < x < Fraction(2))    # method's intermediate equivalence
        assert implies(H(x), T(x))
    assert any(H(x) for x in REAL_GRID)
    x = Fraction(-5)
    assert T(x) and not H(x)
    assert not all(implies(T(x2), H(x2)) for x2 in REAL_GRID)


# C4: "n prime" as condition for "n has exactly two positive divisors" -- necessary and sufficient
def check_C4():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 20001):
        assert is_prime(n) == (num_divisors(n) == 2)


# C5: P suff for Q, Q suff for R => P suff for R (abstract, general proof)
def check_C5():
    """ EXHAUSTIVE PROOF """
    models = [(P, Q, R) for P, Q, R in itertools.product([False, True], repeat=3)
              if implies(P, Q) and implies(Q, R)]
    assert len(models) > 0
    for P, Q, R in models:
        assert implies(P, R)


# C6: "4|n" for "12|n" -- necessary: yes, sufficient: no
def check_C6():
    """ EXHAUSTIVE PROOF """
    domain = range(-10000, 10001)
    for n in domain:
        assert implies(n % 12 == 0, n % 4 == 0)
    n = 4
    assert n % 4 == 0 and n % 12 != 0


# C7: C = "n mult of 10" is necessary but not sufficient for "n mult of 100"
def check_C7():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)
    for n in domain:
        assert implies(n % 100 == 0, n % 10 == 0)
    n = 10
    assert n % 10 == 0 and n % 100 != 0
    assert 100 == 10 * 10


# C8: x iff y, y iff z => x iff z (abstract, general proof)
def check_C8():
    """ EXHAUSTIVE PROOF """
    models = [(x, y, z) for x, y, z in itertools.product([False, True], repeat=3)
              if (x == y) and (y == z)]
    assert len(models) > 0
    for x, y, z in models:
        assert x == z
        assert implies(x, z) and implies(z, x)


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: "x>0" as condition for "x^2>0" -- C) sufficient but not necessary
def check_D1():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x > 0
    T = lambda x: x**2 > 0
    for x in REAL_GRID:
        assert implies(H(x), T(x))
    x = Fraction(-1)
    assert T(x) and not H(x)
    assert not all(implies(T(x2), H(x2)) for x2 in REAL_GRID)


# D2: "x rational" as condition for "x^2 rational" -- sufficient but not necessary
def check_D2():
    """ SAMPLED CHECK """
    # Sufficient: rationals closed under multiplication -- exact identity check via Fraction
    for p in range(-30, 31):
        for q in range(1, 11):
            x = Fraction(p, q)
            assert x * x == Fraction(p * p, q * q)
    # Not necessary: sqrt(2) is irrational, yet its square (=2) is rational.
    # Bounded search (no exhaustive proof over all naturals is possible): for every
    # denominator q up to N, no integer p satisfies p^2 = 2q^2.
    N = 200000
    for qv in range(1, N):
        p = math.isqrt(2 * qv * qv)
        assert p * p != 2 * qv * qv
        assert (p + 1) * (p + 1) != 2 * qv * qv
    assert Fraction(2, 1).denominator == 1     # x^2 = 2 is manifestly rational
    # parity lemma underlying the classical descent proof: p^2 even iff p even
    for p in range(-2000, 2001):
        assert (p * p % 2 == 0) == (p % 2 == 0)


# D3: "Y div by 4" as condition for "Y is a leap year" -- necessary but not sufficient
def check_D3():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 20001)
    for y in domain:
        assert implies(is_leap(y), y % 4 == 0)
    y = 1900
    assert y % 4 == 0 and y % 100 == 0 and y % 400 != 0
    assert is_leap(y) is False
    assert not all(implies(y2 % 4 == 0, is_leap(y2)) for y2 in domain)


# D4: A=>B, B=>C, C=>A => A,B,C all logically equivalent
def check_D4():
    """ EXHAUSTIVE PROOF """
    models = [(A, B, C) for A, B, C in itertools.product([False, True], repeat=3)
              if implies(A, B) and implies(B, C) and implies(C, A)]
    assert len(models) > 0
    for A, B, C in models:
        assert A == B == C
        assert implies(A, C) and implies(C, A)
        assert implies(B, A) and implies(A, B)
        assert implies(C, B) and implies(B, C)


# D5: "9|n" as condition for "3|n" -- sufficient but not necessary (via S's false converse)
def check_D5():
    """ EXHAUSTIVE PROOF """
    domain = range(-10000, 10001)
    for n in domain:
        assert implies(n % 9 == 0, n % 3 == 0)                            # S itself
    n = 6
    assert n % 3 == 0 and n % 9 != 0                                      # breaks S's converse
    assert not all(implies(m % 3 == 0, m % 9 == 0) for m in domain)       # S's converse is false
    assert 9 == 3 * 3


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
            print(f"PASS {name}")
            passed += 1
        except Exception as e:
            print(f"FAILED {name}: {e}")
            raise
    print(f"All {passed} checks passed!")

if __name__ == "__main__":
    main()
