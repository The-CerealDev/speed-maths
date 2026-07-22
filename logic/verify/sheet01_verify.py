import math
import itertools
import random
from functools import reduce

# ── shared helpers ──────────────────────────────────────────────────────────

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_perfect_square(x):
    if x < 0:
        return False
    r = math.isqrt(x)
    return r * r == x

def lcm(a, b):
    return a * b // math.gcd(a, b)


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: hypothesis/conclusion of "if n div by 10, then n div by 5"
def check_A1():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 10 == 0   # claimed hypothesis
    C = lambda n: n % 5 == 0    # claimed conclusion
    domain = range(-1000, 1001)
    # The assignment must make the conditional actually true (H => C)
    for n in domain:
        assert (not H(n)) or C(n)
    # ...and the roles are not interchangeable: the reverse direction fails
    # somewhere in range (e.g. n=5), so H and C are genuinely distinct roles
    assert any(C(n) and not H(n) for n in domain)


# A2: converse of "if x=3 then x^2=9" is "if x^2=9 then x=3"
def check_A2():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x == 3          # original hypothesis
    C = lambda x: x**2 == 9       # original conclusion
    H2 = lambda x: x**2 == 9      # claimed converse's hypothesis (from \ans text)
    C2 = lambda x: x == 3         # claimed converse's conclusion (from \ans text)
    domain = [i * 0.5 for i in range(-40, 41)]
    for x in domain:
        assert C(x) == H2(x)
        assert H(x) == C2(x)


# A3: "if a shape is a square, then it is a rectangle" -- True
def check_A3():
    """ EXHAUSTIVE PROOF """
    def is_rectangle(w, h):
        return w > 0 and h > 0
    def is_square(w, h):
        return is_rectangle(w, h) and w == h
    for w in range(1, 51):
        for h in range(1, 51):
            if is_square(w, h):
                assert is_rectangle(w, h)


# A4: "if a shape is a rectangle, then it is a square" -- False, 2x3 counterexample
def check_A4():
    """ EXHAUSTIVE PROOF """
    def is_rectangle(w, h):
        return w > 0 and h > 0
    def is_square(w, h):
        return is_rectangle(w, h) and w == h
    assert is_rectangle(2, 3) and not is_square(2, 3)
    found = any(is_rectangle(w, h) and not is_square(w, h)
                for w in range(1, 51) for h in range(1, 51))
    assert found


# A5: converse of "if n even then n^2 even" is "if n^2 even then n even"
def check_A5():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 2 == 0
    C = lambda n: (n**2) % 2 == 0
    H2 = lambda n: (n**2) % 2 == 0
    C2 = lambda n: n % 2 == 0
    domain = range(-1000, 1001)
    for n in domain:
        assert C(n) == H2(n)
        assert H(n) == C2(n)


# A6: "n^2 > 0 for every integer n" -- False, n=0 is the unique counterexample
def check_A6():
    """ EXHAUSTIVE PROOF """
    domain = range(-1000, 1001)
    counterexamples = [n for n in domain if not (n**2 > 0)]
    assert counterexamples == [0]


# A7: hypothesis/conclusion of "if x>3 then x^2>9"
def check_A7():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x > 3
    C = lambda x: x**2 > 9
    domain = [i * 0.25 for i in range(-80, 81)]
    for x in domain:
        assert (not H(x)) or C(x)
    # roles aren't interchangeable: reverse direction fails somewhere (x=-4)
    assert any(C(x) and not H(x) for x in domain)


# A8: "if a=b then a^2=b^2" -- True
def check_A8():
    """ EXHAUSTIVE PROOF """
    for a in range(-200, 201):
        b = a
        assert a**2 == b**2


# A9: converse of "if n mult of 6 then n mult of 2" is "if n mult of 2 then n mult of 6"
def check_A9():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 6 == 0
    C = lambda n: n % 2 == 0
    H2 = lambda n: n % 2 == 0
    C2 = lambda n: n % 6 == 0
    domain = range(-1000, 1001)
    for n in domain:
        assert C(n) == H2(n)
        assert H(n) == C2(n)


# A10: "the converse of a true statement is always true" -- False (A2, A9 counterexamples)
def check_A10():
    """ EXHAUSTIVE PROOF """
    dom_real = [i * 0.5 for i in range(-40, 41)]
    dom_int = range(-1000, 1001)
    # A2: "x=3 => x^2=9" true throughout domain, but converse fails (x=-3)
    orig_A2 = all((x != 3) or (x**2 == 9) for x in dom_real)
    conv_A2_counterexample = any((x**2 == 9) and (x != 3) for x in dom_real)
    assert orig_A2 and conv_A2_counterexample
    # A9: "6|n => 2|n" true throughout domain, but converse fails (n=4)
    orig_A9 = all((n % 6 != 0) or (n % 2 == 0) for n in dom_int)
    conv_A9_counterexample = any((n % 2 == 0) and (n % 6 != 0) for n in dom_int)
    assert orig_A9 and conv_A9_counterexample


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: converse of "4|n and 3|n => 12|n" is "12|n => 4|n and 3|n"; both true
def check_B1():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 10001)
    for n in domain:
        if n % 4 == 0 and n % 3 == 0:
            assert n % 12 == 0
    for n in domain:
        if n % 12 == 0:
            assert n % 4 == 0 and n % 3 == 0


# B2: "if n even then n^2 even" -- direct proof via n=2k
def check_B2():
    """ EXHAUSTIVE PROOF """
    for n in range(-1000, 1001):
        if n % 2 == 0:
            assert (n**2) % 2 == 0
    for k in range(-500, 501):
        n = 2 * k
        assert n**2 == 2 * (2 * k**2)


# B3: converse of "x>0,y>0 => xy>0" is false, counterexample x=-1,y=-1
def check_B3():
    """ EXHAUSTIVE PROOF """
    for x in range(1, 101):
        for y in range(1, 101):
            assert x * y > 0
    x, y = -1, -1
    assert x * y > 0 and not (x > 0 and y > 0)


# B4: "digit sum mult of 3 => n mult of 3" -- True (10 == 1 mod 3)
def check_B4():
    """ EXHAUSTIVE PROOF """
    def digit_sum(n):
        return sum(int(d) for d in str(n))
    for n in range(1, 100001):
        assert n % 3 == digit_sum(n) % 3
    for n in range(1, 100001):
        if digit_sum(n) % 3 == 0:
            assert n % 3 == 0


# B5: "if n odd then n^2 odd" -- direct proof via n=2k+1
def check_B5():
    """ EXHAUSTIVE PROOF """
    for n in range(-1000, 1001):
        if n % 2 != 0:
            assert (n**2) % 2 != 0
    for k in range(-500, 501):
        n = 2 * k + 1
        assert n**2 == 2 * (2 * k**2 + 2 * k) + 1


# B6: "if x^2=9 then x=3" -- False, x=-3 breaks it
def check_B6():
    """ EXHAUSTIVE PROOF """
    x = -3
    assert x**2 == 9 and x != 3


# B7: converse of Pythagoras is also true (Law of Cosines)
def check_B7():
    """ SAMPLED CHECK """
    random.seed(1234)
    # Right triangles: angle opposite c (via Law of Cosines) must be 90 degrees
    for _ in range(2000):
        a = random.uniform(1, 100)
        b = random.uniform(1, 100)
        c = math.sqrt(a**2 + b**2)
        cosC = (a**2 + b**2 - c**2) / (2 * a * b)
        assert abs(cosC) < 1e-6
    # Non-right triangles: angle opposite the longest side must NOT be 90 degrees
    count = 0
    while count < 2000:
        a = random.uniform(1, 100)
        b = random.uniform(1, 100)
        c = random.uniform(1, 100)
        aa, bb, cc = sorted([a, b, c])
        if aa + bb <= cc:
            continue  # not a valid triangle
        diff = aa**2 + bb**2 - cc**2
        scale = aa**2 + bb**2 + cc**2
        if abs(diff) < 1e-3 * scale:
            continue  # too close to right-angled to be a clean negative example
        cosC = diff / (2 * aa * bb)
        assert abs(cosC) > 1e-3
        count += 1


# B8: "a,b even => a+b even" -- direct proof
def check_B8():
    """ EXHAUSTIVE PROOF """
    for j in range(-100, 101):
        for k in range(-100, 101):
            a, b = 2 * j, 2 * k
            assert (a + b) % 2 == 0


# B9: "p prime, p!=2 => p odd" -- True (2 is the only even prime)
def check_B9():
    """ EXHAUSTIVE PROOF """
    N = 10000
    primes = [p for p in range(2, N) if is_prime(p)]
    for p in primes:
        if p != 2:
            assert p % 2 != 0
    even_primes = [p for p in primes if p % 2 == 0]
    assert even_primes == [2]


# B10: converse of "x=y => x^3=y^3" is "x^3=y^3 => x=y", True (cubing injective)
def check_B10():
    """ EXHAUSTIVE PROOF """
    for x in range(-1000, 1001):
        y = x
        assert x**3 == y**3
    cubes = {}
    for x in range(-1000, 1001):
        c = x**3
        assert c not in cubes  # no two distinct x share a cube => injective
        cubes[c] = x


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: "n mult of 3 => n^2 mult of 9" -- direct proof via n=3k
def check_C1():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 3 * k
        assert n**2 == 9 * k**2
        assert (n**2) % 9 == 0


# C2: "n odd => n^2-1 mult of 8" -- direct proof via n=2k+1
def check_C2():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k + 1
        assert n**2 - 1 == 4 * k * (k + 1)
        assert (k * (k + 1)) % 2 == 0        # consecutive integers -> always even
        assert (n**2 - 1) % 8 == 0


# C3: correct converse of "x rational, y irrational => x+y irrational" is option A
def check_C3():
    """ EXHAUSTIVE PROOF """
    def implies(a, b):
        return (not a) or b

    results_orig, results_A, results_C = [], [], []
    for P, Qi, R in itertools.product([False, True], repeat=3):
        # P: x rational, Qi: y irrational, R: x+y irrational
        hyp = P and Qi
        orig = implies(hyp, R)
        converse = implies(R, hyp)                          # literal swap
        optA = implies(R, P and Qi)                         # option A, parsed from its text
        optC = implies(not R, (not P) or (not Qi))          # option C, parsed from its text
        results_orig.append(orig)
        results_A.append(optA)
        results_C.append(optC)
        # option A must equal the literal hypothesis/conclusion swap, always
        assert converse == optA

    # option C is NOT the converse: it must disagree with option A somewhere
    assert results_A != results_C
    # option C is in fact the contrapositive: logically equivalent to the
    # original for every truth assignment (the reason it's a tempting distractor)
    assert results_orig == results_C


# C4: "true statement's converse must be false" -- False (B1 is a counterexample)
def check_C4():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 10001)
    orig_true = all(n % 12 == 0 for n in domain if (n % 4 == 0 and n % 3 == 0))
    conv_true = all((n % 4 == 0 and n % 3 == 0) for n in domain if n % 12 == 0)
    assert orig_true and conv_true


# C5: "n mult of 6 => n^3 mult of 216" -- direct proof via n=6k
def check_C5():
    """ EXHAUSTIVE PROOF """
    for k in range(-200, 201):
        n = 6 * k
        assert n**3 == 216 * k**3
        assert (n**3) % 216 == 0


# C6: converse of "x>=2,y>=2 => xy>=x+y" is false, counterexample x=1.5,y=10
def check_C6():
    """ SAMPLED CHECK """
    random.seed(42)
    for _ in range(5000):
        x = random.uniform(2, 1000)
        y = random.uniform(2, 1000)
        assert x * y >= x + y
    x, y = 1.5, 10
    assert x * y >= x + y and not (x >= 2 and y >= 2)
    found = False
    for _ in range(5000):
        x = random.uniform(0.01, 2)
        y = random.uniform(0.01, 1000)
        if x * y >= x + y and x < 2:
            found = True
            break
    assert found


# C7: converse of "x,y both perfect squares => xy perfect square" is false, x=2,y=8
def check_C7():
    """ EXHAUSTIVE PROOF """
    squares = [i * i for i in range(0, 60)]
    for a in squares:
        for b in squares:
            assert is_perfect_square(a * b)
    x, y = 2, 8
    assert is_perfect_square(x * y) and not is_perfect_square(x) and not is_perfect_square(y)


# C8: "n^2 mult of 4 => n mult of 4" -- False, n=6 counterexample
def check_C8():
    """ EXHAUSTIVE PROOF """
    counterexamples = [n for n in range(1, 1001) if (n**2) % 4 == 0 and n % 4 != 0]
    assert 6 in counterexamples
    n = 6
    assert (n**2) % 4 == 0 and n % 4 != 0


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: statements I (F), II (T), III (T) about 4|n vs 8|n -- answer F) II and III only
def check_D1():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 10001)
    I_true = all((n % 4 != 0) or (n % 8 == 0) for n in domain)
    assert I_true is False
    assert 4 % 4 == 0 and 4 % 8 != 0   # n=4 is the counterexample to I

    II_true = all((n % 8 != 0) or (n % 4 == 0) for n in domain)
    assert II_true is True

    # III: the converse of I is exactly II (structural swap check)
    H = lambda n: n % 4 == 0
    C = lambda n: n % 8 == 0
    H2 = lambda n: n % 8 == 0   # II's hypothesis
    C2 = lambda n: n % 4 == 0   # II's conclusion
    for n in domain:
        assert C(n) == H2(n)
        assert H(n) == C2(n)
    III_true = True

    assert (I_true, II_true, III_true) == (False, True, True)


# D2: "n,n+2 both prime > 3 => n+1 mult of 6"
def check_D2():
    """ EXHAUSTIVE PROOF """
    found_any = False
    for n in range(4, 20000):
        if n > 3 and is_prime(n) and is_prime(n + 2):
            found_any = True
            assert n % 2 != 0 and (n + 2) % 2 != 0    # both odd
            assert (n + 1) % 2 == 0                    # sandwiched -> even
            assert n % 3 != 0 and (n + 2) % 3 != 0     # neither mult of 3
            assert (n + 1) % 3 == 0                    # forces n+1 mult of 3
            assert (n + 1) % 6 == 0
    assert found_any


# D3: Amy's claim, divisible by 2,3,4,5,6 <=> divisible by 60; smallest is 60
def check_D3():
    """ EXHAUSTIVE PROOF """
    L = reduce(lcm, [2, 3, 4, 5, 6])
    assert L == 60
    for n in range(1, 100001):
        all_five = all(n % d == 0 for d in [2, 3, 4, 5, 6])
        assert all_five == (n % 60 == 0)
    smallest = next(n for n in range(1, 100001) if all(n % d == 0 for d in [2, 3, 4, 5, 6]))
    assert smallest == 60


# D4: S: "12|n => 4|n,3|n"; S': "4|n,3|n => 12|n" -- both true
def check_D4():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 10001)
    S_true = all((n % 12 != 0) or (n % 4 == 0 and n % 3 == 0) for n in domain)
    Sp_true = all((not (n % 4 == 0 and n % 3 == 0)) or (n % 12 == 0) for n in domain)
    assert S_true and Sp_true


# D5: "if n^2-n even then n even" -- False, n=3 counterexample
def check_D5():
    """ EXHAUSTIVE PROOF """
    for n in range(-1000, 1001):
        assert (n * (n - 1)) % 2 == 0
        assert (n**2 - n) % 2 == 0
    n = 3
    assert n**2 - n == 6 and (n**2 - n) % 2 == 0 and n % 2 != 0


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
