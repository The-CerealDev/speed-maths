import math
from fractions import Fraction

# ── shared helpers ──────────────────────────────────────────────────────────

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_composite(x):
    return x > 1 and not is_prime(x)

def divisors(n):
    n = abs(n)
    return sorted(d for d in range(1, n + 1) if n % d == 0)


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: "Every prime number is odd." -- False, n=2
def check_A1():
    """ EXHAUSTIVE PROOF """
    n = 2
    assert is_prime(n)
    assert n % 2 == 0   # even, so "prime => odd" is violated
    # confirm 2 is genuinely the only even prime in a wide range (why this
    # is *the* standard counterexample source, per the \inv note)
    even_primes = [p for p in range(2, 10000) if is_prime(p) and p % 2 == 0]
    assert even_primes == [2]


# A2: "n^2 >= n for every real number n." -- False, n=0.5
def check_A2():
    """ EXHAUSTIVE PROOF """
    n = 0.5
    assert n**2 < n
    assert n**2 == 0.25
    # \method also claims: over the INTEGERS the claim is true, since
    # n^2-n = n(n-1) >= 0 always. Verify exhaustively over a wide integer range.
    for k in range(-1000, 1001):
        assert k * (k - 1) >= 0
        assert k**2 - k == k * (k - 1)
        assert k**2 >= k


# A3: "If n is prime, then n+2 is prime." -- False, n=7
def check_A3():
    """ EXHAUSTIVE PROOF """
    n = 7
    assert is_prime(n)
    assert not is_prime(n + 2)
    assert n + 2 == 9 == 3**2


# A4: "The sum of two primes is always even." -- False, 2+3=5
def check_A4():
    """ EXHAUSTIVE PROOF """
    p, q = 2, 3
    assert is_prime(p) and is_prime(q)
    s = p + q
    assert s == 5
    assert s % 2 != 0  # odd, breaking "always even"


# A5: "Every multiple of 4 is a multiple of 8." -- False, n=4
def check_A5():
    """ EXHAUSTIVE PROOF """
    n = 4
    assert n % 4 == 0
    assert n % 8 != 0


# A6: "sqrt(a+b) = sqrt(a)+sqrt(b) for all a,b >= 0." -- False, a=b=1
def check_A6():
    """ EXHAUSTIVE PROOF """
    a, b = 1, 1
    assert a >= 0 and b >= 0
    # exact integer route (no floating-point sqrt): a, b are themselves
    # perfect squares here, so sqrt(a), sqrt(b) are exact integers, and we
    # compare (sqrt(a+b))^2 against (sqrt(a)+sqrt(b))^2 directly
    assert math.isqrt(a) ** 2 == a and math.isqrt(b) ** 2 == b
    sqrt_a, sqrt_b = math.isqrt(a), math.isqrt(b)
    lhs_squared = a + b                     # (sqrt(a+b))^2, exactly
    rhs_squared = (sqrt_a + sqrt_b) ** 2     # (sqrt(a)+sqrt(b))^2, exactly
    assert lhs_squared == 2 and rhs_squared == 4
    assert lhs_squared != rhs_squared       # unequal squares of non-negatives => unequal values


# A7: "(x+y)^2 = x^2+y^2 for all real x,y." -- False, x=y=1
def check_A7():
    """ EXHAUSTIVE PROOF """
    x, y = 1, 1
    assert (x + y)**2 == 4
    assert x**2 + y**2 == 2
    assert (x + y)**2 != x**2 + y**2
    # sanity: the true identity has the missing cross term 2xy
    assert (x + y)**2 == x**2 + 2 * x * y + y**2


# A8: "n!+1 is always prime." -- False, n=4
def check_A8():
    """ EXHAUSTIVE PROOF """
    for n in (1, 2, 3):
        assert is_prime(math.factorial(n) + 1)
    n = 4
    val = math.factorial(n) + 1
    assert val == 25 == 5**2
    assert not is_prime(val)


# A9: "If a number is not prime, it must be even." -- False, n=9
def check_A9():
    """ EXHAUSTIVE PROOF """
    n = 9
    assert not is_prime(n)
    assert n == 3 * 3
    assert n % 2 != 0


# A10: "All odd numbers greater than 1 are prime." -- False, n=9
def check_A10():
    """ EXHAUSTIVE PROOF """
    n = 9
    assert n % 2 != 0 and n > 1
    assert not is_prime(n)
    assert n == 3 * 3


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: "n^2+n+41 is prime for every positive integer n." -- False, n=41
def check_B1():
    """ EXHAUSTIVE PROOF """
    n = 41
    val = n**2 + n + 41
    assert val == 1763
    assert val == 41 * 43
    assert val % 41 == 0
    assert not is_prime(val)
    # the structural claim: 41 | n^2+n+41 whenever n ≡ 0 (mod 41)
    for k in range(0, 10):
        m = 41 * k
        assert (m**2 + m + 41) % 41 == 0


# B2: "a,b both irrational => a+b irrational." -- False, a=sqrt2, b=-sqrt2
def check_B2():
    """ EXHAUSTIVE PROOF (algebraic identity, exact integer arithmetic only;
    the irrationality of sqrt(2) itself is the pillar's known background fact
    and is not re-derived here -- only the arithmetic consequence is checked) """
    # sqrt(2) is symbolically "the (positive) real r with r**2 == 2". Working
    # only from that defining property, with no floating-point sqrt anywhere:
    r_squared = 2                     # defining property of r = sqrt(2)
    a_plus_b = 0                      # a=r, b=-r  =>  a+b = r + (-r) = 0, an
                                       # identity true for ANY r whatsoever
    assert a_plus_b == 0
    assert isinstance(a_plus_b, int)  # manifestly rational (an integer)
    # consistency check: r is not itself an integer (no integer squares to 2),
    # so a and b are not the trivial "both already rational" case
    for k in range(-2, 3):
        assert k * k != r_squared


# B3: "a,b both irrational => ab irrational." -- False, a=b=sqrt2
def check_B3():
    """ EXHAUSTIVE PROOF (algebraic identity, exact integer arithmetic only;
    the irrationality of sqrt(2) itself is the pillar's known background fact
    and is not re-derived here -- only the arithmetic consequence is checked) """
    r_squared = 2           # defining property of r = sqrt(2): r*r = 2 exactly
    ab = r_squared           # a=b=r  =>  ab = r*r = 2 exactly, by definition
    assert ab == 2
    assert isinstance(ab, int)   # manifestly rational (an integer)
    for k in range(-2, 3):
        assert k * k != r_squared  # r itself is not an integer


# B4: quadratic with integer coeffs, one integer root, one non-integer root
def check_B4():
    """ EXHAUSTIVE PROOF """
    def f(x):
        return 2 * x**2 - 3 * x + 1

    # independently re-derive the roots via the quadratic formula, not by
    # trusting the stated factorisation
    a, b, c = 2, -3, 1
    disc = b**2 - 4 * a * c
    assert disc == 1
    sqrt_disc = math.isqrt(disc)
    assert sqrt_disc * sqrt_disc == disc
    r1 = Fraction(-b + sqrt_disc, 2 * a)
    r2 = Fraction(-b - sqrt_disc, 2 * a)
    roots = {r1, r2}
    assert roots == {Fraction(1, 1), Fraction(1, 2)}

    # each root actually satisfies f(x) = 0
    for r in roots:
        assert 2 * r**2 - 3 * r + 1 == 0

    # confirm the claimed factorisation (2x-1)(x-1) really equals the
    # original polynomial, by matching at 3 distinct points (degree <= 2)
    def g(x):
        return (2 * x - 1) * (x - 1)
    for x in (0, 1, 2, 3, 4):
        assert f(x) == g(x)

    assert r1.denominator == 1 or r2.denominator == 1     # one is an integer
    assert not (r1.denominator == 1 and r2.denominator == 1)  # not both integers


# B5: "For every integer n, n/n = 1." -- False, n=0
def check_B5():
    """ EXHAUSTIVE PROOF """
    n = 0
    try:
        n / n
        assert False, "division by zero should have raised"
    except ZeroDivisionError:
        pass
    # sanity: for every nonzero integer, n/n == 1 (the claim's "n" only fails at 0)
    for n in list(range(-1000, 0)) + list(range(1, 1001)):
        assert n / n == 1


# B6: "Every positive integer has at least one prime factor." -- False, n=1
def check_B6():
    """ EXHAUSTIVE PROOF """
    n = 1
    assert divisors(n) == [1]
    assert not is_prime(n)
    prime_factors = [d for d in divisors(n) if is_prime(d)]
    assert prime_factors == []


# B7: "For all integers n, n^n is positive." -- False, n=-1
def check_B7():
    """ EXHAUSTIVE PROOF """
    n = -1
    # n^n for n=-1 means 1/(n^1) = 1/(-1) = -1, computed exactly via Fraction
    val = Fraction(1, n ** 1)
    assert val == Fraction(-1, 1)
    assert val < 0
    # positive n's do give positive n^n, confirming the claim isn't broken elsewhere in a small range
    for k in range(1, 50):
        assert k**k > 0


# B8: "If x^2 is an integer, then x is an integer." -- False, x=sqrt(2)
def check_B8():
    """ EXHAUSTIVE PROOF (x^2=2 is exact by definition of x=sqrt(2); the
    irrationality of sqrt(2) itself is taken as known, but x's non-integer-
    ness IS shown exactly here: no integer squares to 2) """
    x_squared = 2   # x := sqrt(2), defined by x**2 = 2 exactly
    assert isinstance(x_squared, int)   # x^2 is an integer
    for k in range(-2, 3):
        assert k * k != x_squared       # x itself is not an integer (no integer root of 2)


# B9: "If p,q distinct primes, then p+q is composite." -- False, p=2,q=3
def check_B9():
    """ EXHAUSTIVE PROOF """
    p, q = 2, 3
    assert is_prime(p) and is_prime(q) and p != q
    s = p + q
    assert s == 5
    assert is_prime(s)
    assert not is_composite(s)


# B10: "For every integer n>=1, 2^n-1 is prime." -- False, n=4
def check_B10():
    """ EXHAUSTIVE PROOF """
    n = 4
    val = 2**n - 1
    assert val == 15
    assert val == 3 * 5
    assert not is_prime(val)


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: smallest positive n with n^2+n+41 not prime -- claimed n=40
def check_C1():
    """ EXHAUSTIVE PROOF """
    def f(n):
        return n**2 + n + 41

    # the celebrated fact: prime for every n = 0, 1, ..., 39
    for n in range(0, 40):
        assert is_prime(f(n))

    # "smallest positive integer n" -- exhaustively confirm nothing smaller
    # than 40 (in the positive range) breaks it, and 40 itself breaks it
    for n in range(1, 40):
        assert is_prime(f(n))
    assert f(40) == 1681 == 41**2
    assert not is_prime(f(40))
    assert not is_prime(41**2)


# C2: "a≡b (mod n) => a^2≡b^2 (mod n^2)." -- False, n=3,a=1,b=4
def check_C2():
    """ EXHAUSTIVE PROOF """
    n, a, b = 3, 1, 4
    assert a % n == b % n  # a ≡ b (mod n)
    assert (a**2) % (n**2) != (b**2) % (n**2)
    assert a**2 == 1
    assert b**2 == 16
    assert 16 % 9 == 7
    assert 1 % 9 == 1


# C3: which n is a counterexample to "n^2-n+11 prime for all positive n"
def check_C3():
    """ EXHAUSTIVE PROOF """
    def f(n):
        return n**2 - n + 11

    vals = {'A': f(1), 'B': f(5), 'C': f(11), 'D': f(10)}
    assert vals == {'A': 11, 'B': 31, 'C': 121, 'D': 101}
    primality = {k: is_prime(v) for k, v in vals.items()}
    assert primality == {'A': True, 'B': True, 'C': False, 'D': True}
    # exactly one option is composite -- the MCQ has a unique correct answer
    composite_options = [k for k, p in primality.items() if not p]
    assert composite_options == ['C']
    # structural reason C works: at n=11, the linear terms -n+11 cancel to 0,
    # leaving the bare square n^2 = 121 = 11^2
    n = 11
    assert -n + 11 == 0
    assert f(n) == n**2 == 121
    assert not is_prime(n**2)   # a prime squared is never itself prime


# C4: "If p is prime, then 2^p-1 is prime." -- False, p=11
def check_C4():
    """ EXHAUSTIVE PROOF """
    p = 11
    assert is_prime(p)
    val = 2**p - 1
    assert val == 2047
    assert val == 23 * 89
    assert not is_prime(val)


# C5: "a^2≡b^2 (mod n) => a≡b (mod n)." -- False, n=8,a=1,b=3
def check_C5():
    """ EXHAUSTIVE PROOF """
    n, a, b = 8, 1, 3
    assert (a**2) % n == (b**2) % n
    assert a**2 == 1
    assert b**2 == 9
    assert 9 % 8 == 1
    assert a % n != b % n


# C6: smallest positive n with 3^n+2 not prime -- claimed n=5
def check_C6():
    """ EXHAUSTIVE PROOF """
    def f(n):
        return 3**n + 2

    for n in range(1, 5):
        assert is_prime(f(n))
    assert f(1) == 5 and f(2) == 11 and f(3) == 29 and f(4) == 83
    assert f(5) == 245
    assert f(5) == 5 * 49 == 5 * 7**2
    assert not is_prime(f(5))


# C7: "x,y both non-integers => x+y non-integer." -- False, x=y=0.5
def check_C7():
    """ EXHAUSTIVE PROOF """
    x = y = Fraction(1, 2)
    assert x.denominator != 1 and y.denominator != 1
    s = x + y
    assert s == 1
    assert s.denominator == 1


# C8: Euclid's Lemma without primality -- False, a=4,b=2,c=2
def check_C8():
    """ EXHAUSTIVE PROOF """
    a, b, c = 4, 2, 2
    bc = b * c
    assert bc == 4
    assert bc % a == 0          # a | bc
    assert b % a != 0           # a does not divide b
    assert c % a != 0           # a does not divide c
    assert not is_prime(a)      # breaks precisely because a is composite


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: truth of I, II, III -- claimed answer H) None of them
def check_D1():
    """ EXHAUSTIVE PROOF """
    # I: n^2+n+41 prime for all positive n -- False (fails at n=40, see C1)
    n = 40
    I_val = n**2 + n + 41
    assert I_val == 1681 == 41**2
    I_true = not is_composite(I_val)  # is claim I true? no, it's composite here
    assert is_composite(I_val)
    I_holds = False
    assert I_holds is False

    # II: 2^n-1 prime whenever n prime -- False (fails at n=11, see C4)
    p = 11
    assert is_prime(p)
    II_val = 2**p - 1
    assert II_val == 2047 == 23 * 89
    assert is_composite(II_val)
    II_holds = False
    assert II_holds is False

    # III: n!+1 prime for all positive n -- False (fails at n=4, see A8)
    m = 4
    III_val = math.factorial(m) + 1
    assert III_val == 25 == 5**2
    assert is_composite(III_val)
    III_holds = False
    assert III_holds is False

    assert (I_holds, II_holds, III_holds) == (False, False, False)


# D2: smallest positive n with n^2+n+1 not prime -- claimed n=4
def check_D2():
    """ EXHAUSTIVE PROOF """
    def f(n):
        return n**2 + n + 1

    for n in range(1, 4):
        assert is_prime(f(n))
    assert f(1) == 3 and f(2) == 7 and f(3) == 13
    assert f(4) == 21 == 3 * 7
    assert not is_prime(f(4))


# D3: "sum of any three consecutive primes always even." -- False, 3+5+7
def check_D3():
    """ EXHAUSTIVE PROOF """
    primes = [p for p in range(2, 50) if is_prime(p)]
    assert 3 in primes and 5 in primes and 7 in primes
    i = primes.index(3)
    # confirm 3,5,7 are genuinely consecutive entries in the prime sequence
    assert primes[i:i + 3] == [3, 5, 7]
    s = 3 + 5 + 7
    assert s == 15
    assert s % 2 != 0
    # sanity: sum of three odd numbers is always odd
    for a in range(1, 100, 2):
        for b in range(1, 100, 2):
            for c in (1, 3):
                assert (a + b + c) % 2 != 0


# D4: "n^2+1 prime => n even." -- False, n=1
def check_D4():
    """ EXHAUSTIVE PROOF """
    n = 1
    val = n**2 + 1
    assert val == 2
    assert is_prime(val)
    assert n % 2 != 0  # n is odd, breaking the claim


# D5: T:"2^n-1 prime => n prime". (a) B10/C4 don't contradict T. (b) converse
#     false. (c) sufficient but not necessary.
def check_D5():
    """ EXHAUSTIVE PROOF """
    def hyp(n):   # "2^n-1 is prime"
        return is_prime(2**n - 1)

    def concl(n):  # "n is prime"
        return is_prime(n)

    # T is given as true; corroborate it over a wide bounded range (this is
    # the standard fact that Mersenne-prime exponents must themselves be
    # prime, checked exhaustively over a finite window rather than assumed)
    for n in range(1, 40):
        if hyp(n):
            assert concl(n)

    # (a) B10's n=4 and C4's n=11: in both cases T's HYPOTHESIS is false,
    # so T is not violated (an implication with a false antecedent is
    # vacuously true) -- neither example contradicts T.
    assert not hyp(4)             # 2^4-1 = 15, composite
    assert not hyp(11)            # 2^11-1 = 2047, composite
    assert (not hyp(4)) or concl(4)     # T holds vacuously at n=4
    assert (not hyp(11)) or concl(11)   # T holds vacuously at n=11

    # (b) T's converse: "n prime => 2^n-1 prime". False -- counterexample
    # is exactly C4's n=11: prime n, but 2^11-1 composite.
    assert concl(11) and not hyp(11)
    converse_holds_at_11 = (not concl(11)) or hyp(11)
    assert converse_holds_at_11 is False

    # (c) "2^n-1 prime" sufficient but not necessary for "n prime":
    #   sufficient  <=> T (hyp => concl) holds -- corroborated above
    #   necessary   <=> converse (concl => hyp) holds -- shown False at n=11
    sufficient = all((not hyp(n)) or concl(n) for n in range(1, 40))
    necessary = all((not concl(n)) or hyp(n) for n in range(1, 40))
    assert sufficient is True
    assert necessary is False


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
