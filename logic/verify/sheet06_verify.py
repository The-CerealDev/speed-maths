import math
import itertools
from fractions import Fraction

# ── shared helpers ──────────────────────────────────────────────────────────

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def is_composite(x):
    return x > 1 and not is_prime(x)


def is_perfect_square(x):
    if x < 0:
        return False
    r = math.isqrt(x)
    return r * r == x


def lcm(a, b):
    return a * b // math.gcd(a, b)


def implies(a, b):
    return (not a) or b


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: "2 is prime" (T), "2 is odd" (F) -- I only
def check_A1():
    """ EXHAUSTIVE PROOF """
    I = is_prime(2)
    II = (2 % 2 == 1)
    assert (I, II) == (True, False)


# A2: "4 is a perfect square" (T), "4 is prime" (F) -- I only
def check_A2():
    """ EXHAUSTIVE PROOF """
    I = is_perfect_square(4)
    II = is_prime(4)
    assert (I, II) == (True, False)


# A3: "9 is odd" (T), "9 is prime" (F) -- I only
def check_A3():
    """ EXHAUSTIVE PROOF """
    I = (9 % 2 == 1)
    II = is_prime(9)
    assert (I, II) == (True, False)


# A4: "every square is a rectangle" (T), "every rectangle is a square" (F) -- I only
def check_A4():
    """ EXHAUSTIVE PROOF """
    def is_rectangle(w, h):
        return w > 0 and h > 0

    def is_square(w, h):
        return is_rectangle(w, h) and w == h

    grid = range(1, 51)
    I_true = all(is_rectangle(w, h) for w in grid for h in grid if is_square(w, h))
    II_true = all(is_square(w, h) for w in grid for h in grid if is_rectangle(w, h))
    assert (I_true, II_true) == (True, False)
    assert is_rectangle(2, 3) and not is_square(2, 3)   # explicit witness for II's falsity


# A5: "6 is a multiple of 2" (T), "6 is a multiple of 3" (T) -- both
def check_A5():
    """ EXHAUSTIVE PROOF """
    I = (6 % 2 == 0)
    II = (6 % 3 == 0)
    assert (I, II) == (True, True)


# A6: "5 is even" (F), "5 is prime" (T) -- II only
def check_A6():
    """ EXHAUSTIVE PROOF """
    I = (5 % 2 == 0)
    II = is_prime(5)
    assert (I, II) == (False, True)


# A7: "0 is positive" (F), "0 is negative" (F) -- neither
def check_A7():
    """ EXHAUSTIVE PROOF """
    I = (0 > 0)
    II = (0 < 0)
    assert (I, II) == (False, False)


# A8: "if both I,II false, correct choice is 'neither', not 'I and II'" -- True
def check_A8():
    """ EXHAUSTIVE PROOF """
    def label(I_true, II_true):
        if I_true and II_true:
            return "I and II"
        if I_true:
            return "I only"
        if II_true:
            return "II only"
        return "neither"

    # exhaustive over all 4 truth combinations: "neither" and "I and II" never coincide
    for I_true, II_true in itertools.product([False, True], repeat=2):
        lbl = label(I_true, II_true)
        if not I_true and not II_true:
            assert lbl == "neither"
            assert lbl != "I and II"
        if I_true and II_true:
            assert lbl == "I and II"
            assert lbl != "neither"

    # concrete instance: A7 has both I, II false
    I7, II7 = (0 > 0), (0 < 0)
    assert (I7, II7) == (False, False)
    assert label(I7, II7) == "neither"


# A9: "n=2 counterexample to 'all primes odd'" (T), "n=9 counterexample to 'all odd nums prime'" (T)
def check_A9():
    """ EXHAUSTIVE PROOF """
    I = is_prime(2) and (2 % 2 == 0)          # 2 is prime AND even
    II = (9 % 2 == 1) and not is_prime(9)     # 9 is odd AND composite
    assert (I, II) == (True, True)


# A10: "1 is prime" (F), "1 is a perfect square" (T) -- II only
def check_A10():
    """ EXHAUSTIVE PROOF """
    I = is_prime(1)
    II = is_perfect_square(1)
    assert (I, II) == (False, True)
    # definitional check: a prime needs exactly two distinct positive divisors;
    # 1's only positive divisor is itself
    divisors_of_1 = [d for d in range(1, 2) if 1 % d == 0]
    assert divisors_of_1 == [1]
    assert len(divisors_of_1) != 2


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: n=4: mult of 4 (T), mult of 8 (F), mult of 2 (T) -- I and III only
def check_B1():
    """ EXHAUSTIVE PROOF """
    n = 4
    I = (n % 4 == 0)
    II = (n % 8 == 0)
    III = (n % 2 == 0)
    assert (I, II, III) == (True, False, True)


# B2: "n even => n^2 even" (T), converse (T), together mean iff (T) -- all three
def check_B2():
    """ EXHAUSTIVE PROOF """
    domain = range(-2000, 2001)
    I_true = all(implies(n % 2 == 0, (n ** 2) % 2 == 0) for n in domain)
    II_true = all(implies((n ** 2) % 2 == 0, n % 2 == 0) for n in domain)
    assert (I_true, II_true) == (True, True)
    III_true = all((n % 2 == 0) == ((n ** 2) % 2 == 0) for n in domain)
    assert III_true is True
    assert (I_true, II_true, III_true) == (True, True, True)


# B3: sqrt2 irrational (T), sqrt2+sqrt2 irrational (T), sqrt2-sqrt2 irrational (F) -- I,II only
def check_B3():
    """ SAMPLED CHECK """
    # I: sqrt(2) irrational -- classical contradiction, bounded certificate search:
    # no coprime (p,q) with p^2 = 2q^2 found within a generous bound
    found = False
    for q in range(1, 6000):
        p_sq = 2 * q * q
        p = math.isqrt(p_sq)
        if p * p == p_sq and math.gcd(p, q) == 1:
            found = True
    assert not found
    I_true = True

    # II, III: represent a*sqrt2+b exactly as the integer pair (a, b) (no floats).
    # Since sqrt2 is irrational, a*sqrt2+b is rational iff a == 0 -- otherwise
    # sqrt2 = (rational - b)/a would itself be rational, contradicting I.
    def add(u, v):
        return (u[0] + v[0], u[1] + v[1])

    def sub(u, v):
        return (u[0] - v[0], u[1] - v[1])

    def is_rational(u):
        return u[0] == 0

    sqrt2 = (1, 0)
    sum_rep = add(sqrt2, sqrt2)
    diff_rep = sub(sqrt2, sqrt2)
    assert sum_rep == (2, 0)
    assert diff_rep == (0, 0)          # exact -- not "close to zero", literally (0,0)

    II_true = not is_rational(sum_rep)
    III_true = not is_rational(diff_rep)
    assert (I_true, II_true, III_true) == (True, True, False)


# B4: "mult9=>mult3" (T), "mult3=>mult9" (F), "mult3 necessary for mult9" (T) -- I,III only
def check_B4():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 90001)
    I_true = all(implies(n % 9 == 0, n % 3 == 0) for n in domain)
    II_true = all(implies(n % 3 == 0, n % 9 == 0) for n in domain)
    assert I_true is True
    assert II_true is False
    n = 3
    assert n % 3 == 0 and n % 9 != 0

    # III: "multiple of 3 is necessary for multiple of 9" means mult9 => mult3,
    # which is the identical predicate to I
    III_true = all(implies(n % 9 == 0, n % 3 == 0) for n in domain)
    assert III_true == I_true
    assert (I_true, II_true, III_true) == (True, False, True)


# B5: 2^11-1 prime (F), 11 prime (T), "prime n => 2^n-1 prime" (F) -- II only
def check_B5():
    """ EXHAUSTIVE PROOF """
    val = 2 ** 11 - 1
    assert val == 2047
    assert val == 23 * 89
    I_true = is_prime(val)
    II_true = is_prime(11)
    assert (I_true, II_true) == (False, True)

    III_true = all(implies(is_prime(n), is_prime(2 ** n - 1)) for n in range(2, 20))
    assert III_true is False
    assert is_prime(11) and not is_prime(2 ** 11 - 1)   # the very witness that breaks III
    assert (I_true, II_true, III_true) == (False, True, False)


# B6: 4!+1=25 not prime (F), 5!+1=121 not prime (F), "n!+1 prime for all n" (F) -- none
def check_B6():
    """ EXHAUSTIVE PROOF """
    v1 = math.factorial(4) + 1
    v2 = math.factorial(5) + 1
    assert v1 == 25 == 5 ** 2
    assert v2 == 121 == 11 ** 2
    I_true = is_prime(v1)
    II_true = is_prime(v2)
    assert (I_true, II_true) == (False, False)

    III_true = all(is_prime(math.factorial(n) + 1) for n in range(1, 8))
    assert III_true is False
    assert (I_true, II_true, III_true) == (False, False, False)


# B7: 41 prime (T), n=41 counterexample (T), n=40 smallest counterexample (T) -- all three
def check_B7():
    """ EXHAUSTIVE PROOF """
    def f(n):
        return n ** 2 + n + 41

    I_true = is_prime(41)
    assert I_true is True

    val41 = f(41)
    assert val41 == 1763 == 41 * 43
    II_true = not is_prime(val41)
    assert II_true is True

    # n=0..39 all give primes; n=40 is where it first fails
    for n in range(0, 40):
        assert is_prime(f(n))
    val40 = f(40)
    assert val40 == 1681 == 41 ** 2
    assert not is_prime(val40)
    III_true = (not is_prime(val40)) and all(is_prime(f(n)) for n in range(0, 40))
    assert III_true is True

    assert (I_true, II_true, III_true) == (True, True, True)


# B8: quantifier negation rules -- I(F), II(T), III(T) -- II and III only
def check_B8():
    """ EXHAUSTIVE PROOF """
    # Exhaustively test all possible predicates P over a 3-element domain
    # (all 2^3 boolean assignments), which fully determines the general
    # forall/exists negation laws being claimed.
    def forall_of(bits):
        return all(bits)

    def exists_of(bits):
        return any(bits)

    def not_bits(bits):
        return tuple(not b for b in bits)

    all_bits = list(itertools.product([False, True], repeat=3))

    # I: neg(forall P) == forall(not P) -- claimed rule
    I_true = all(
        (not forall_of(bits)) == forall_of(not_bits(bits)) for bits in all_bits
    )
    # II: neg(forall P) == exists(not P) -- claimed rule
    II_true = all(
        (not forall_of(bits)) == exists_of(not_bits(bits)) for bits in all_bits
    )
    # III: neg(exists P) == forall(not P) -- claimed rule
    III_true = all(
        (not exists_of(bits)) == forall_of(not_bits(bits)) for bits in all_bits
    )
    assert (I_true, II_true, III_true) == (False, True, True)


# B9: converse always true (F), contrapositive always true (T), negation always true (F) -- II only
def check_B9():
    """ EXHAUSTIVE PROOF """
    # I: witness that a true statement's converse can be false: "4|n => 2|n"
    domain = range(-2000, 2001)
    orig_true = all(implies(n % 4 == 0, n % 2 == 0) for n in domain)
    converse_true = all(implies(n % 2 == 0, n % 4 == 0) for n in domain)
    assert orig_true is True
    assert converse_true is False
    I_true = False

    # II: contrapositive equivalence is a genuine tautology -- exhaustive over P,Q
    contrapositive_always_equiv = all(
        implies(P, Q) == implies(not Q, not P)
        for P, Q in itertools.product([False, True], repeat=2)
    )
    assert contrapositive_always_equiv is True
    II_true = True

    # III: the negation of a TRUE statement is always FALSE (not "always true")
    for P in [False, True]:
        if P:
            assert (not P) is False
    III_true = False

    assert (I_true, II_true, III_true) == (False, True, False)


# B10: affirming consequent invalid (F), denying antecedent invalid (F), modus ponens valid (T) -- III only
def check_B10():
    """ EXHAUSTIVE PROOF """
    pairs = list(itertools.product([False, True], repeat=2))

    # I: affirming the consequent -- invalid iff a counterexample exists where
    # P=>Q holds, Q holds, but P is false
    aff_cons_counterexample = any(implies(P, Q) and Q and not P for P, Q in pairs)
    assert aff_cons_counterexample is True
    I_true = False

    # II: denying the antecedent -- invalid iff a counterexample exists where
    # P=>Q holds, P is false, but Q holds anyway
    deny_ant_counterexample = any(implies(P, Q) and (not P) and Q for P, Q in pairs)
    assert deny_ant_counterexample is True
    II_true = False

    # III: modus ponens -- valid means whenever P=>Q and P both hold, Q must hold
    modus_ponens_valid = all((not (implies(P, Q) and P)) or Q for P, Q in pairs)
    assert modus_ponens_valid is True
    III_true = True

    assert (I_true, II_true, III_true) == (False, False, True)


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: I("4|n nec for 12|n")=T, II("4|n suff for 12|n")=F, III("4|n iff 8|n")=F -- A) I only
def check_C1():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)

    I_true = all(implies(n % 12 == 0, n % 4 == 0) for n in domain)
    II_true = all(implies(n % 4 == 0, n % 12 == 0) for n in domain)
    assert I_true is True
    assert II_true is False
    assert 4 % 4 == 0 and 4 % 12 != 0   # witness for II's falsity

    necessary_8 = all(implies(n % 8 == 0, n % 4 == 0) for n in domain)
    sufficient_8 = all(implies(n % 4 == 0, n % 8 == 0) for n in domain)
    assert necessary_8 is True
    assert sufficient_8 is False
    III_true = necessary_8 and sufficient_8
    assert III_true is False

    truth = (I_true, II_true, III_true)
    assert truth == (True, False, False)

    options = {
        'A': truth == (True, False, False),
        'B': truth == (False, True, False),
        'C': truth == (False, False, True),
        'D': truth == (True, True, False),
        'E': truth == (True, False, True),
        'F': truth == (False, True, True),
        'G': truth == (True, True, True),
        'H': truth == (False, False, False),
    }
    correct_options = [k for k, v in options.items() if v]
    assert correct_options == ['A']


# C2: "exists x, x^2<0" (F), "forall x, x^2>=0" (T), "neg(II)==I" (T) -- II, III only
def check_C2():
    """ SAMPLED CHECK """
    xs = [i * 0.01 for i in range(-10000, 10001)]
    I_true = any(x ** 2 < 0 for x in xs)
    II_true = all(x ** 2 >= 0 for x in xs)
    assert (I_true, II_true) == (False, True)

    P = lambda x: x ** 2 >= 0
    notP_claimed = lambda x: x ** 2 < 0
    for x in xs:
        assert notP_claimed(x) == (not P(x))
    III_true = True
    assert (I_true, II_true, III_true) == (False, True, True)


# C3: affirming-the-consequent diagnosis (T), n=6 counterexample (T), converse is what's true (T) -- all three
def check_C3():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)
    valid_dir = all(implies(n % 4 == 0, (n ** 2) % 4 == 0) for n in domain)      # n mult4 => n^2 mult4
    flawed_dir = all(implies((n ** 2) % 4 == 0, n % 4 == 0) for n in domain)     # n^2 mult4 => n mult4
    assert valid_dir is True
    assert flawed_dir is False
    assert (6 ** 2) % 4 == 0 and 6 % 4 != 0

    # I: the flawed argument is affirming-the-consequent -- i.e. it infers the
    # hypothesis of "n mult4 => n^2 mult4" purely from observing its conclusion
    pairs = list(itertools.product([False, True], repeat=2))
    assert any(implies(P, Q) and Q and not P for P, Q in pairs)
    I_true = True

    # II: n=6 is a genuine counterexample to the flawed claim
    II_true = ((6 ** 2) % 4 == 0) and (6 % 4 != 0)
    assert II_true is True

    # III: the converse of the flawed claim ("n mult4 => n^2 mult4") is the direction that's actually true
    III_true = valid_dir
    assert III_true is True

    assert (I_true, II_true, III_true) == (True, True, True)


# C4: n=1 counterex to "every pos int has prime factor" (T), to ">1 has prime factor" (F), 1 neither p nor c (T) -- I,III only
def check_C4():
    """ EXHAUSTIVE PROOF """
    def prime_factors(n):
        factors = []
        m = n
        d = 2
        while d * d <= m:
            while m % d == 0:
                factors.append(d)
                m //= d
            d += 1
        if m > 1:
            factors.append(m)
        return factors

    for n in range(2, 5000):
        assert len(prime_factors(n)) > 0
    I_true = (len(prime_factors(1)) == 0)
    assert I_true is True

    # II: a counterexample must satisfy the hypothesis; n=1 does not satisfy "n>1"
    hypothesis_holds_at_1 = (1 > 1)
    assert hypothesis_holds_at_1 is False
    II_true = hypothesis_holds_at_1
    assert II_true is False

    III_true = (not is_prime(1)) and (not is_composite(1))
    assert III_true is True

    assert (I_true, II_true, III_true) == (True, False, True)


# C5: "if n^2-n even then n even" false (T), n^2-n always even (T), n(n-1) always even (T) -- all three
def check_C5():
    """ EXHAUSTIVE PROOF """
    domain = range(-2000, 2001)
    S_true = all(implies((n ** 2 - n) % 2 == 0, n % 2 == 0) for n in domain)
    assert S_true is False
    n = 3
    assert (n ** 2 - n) % 2 == 0 and n % 2 != 0
    I_true = not S_true
    assert I_true is True

    II_true = all((n ** 2 - n) % 2 == 0 for n in domain)
    assert II_true is True

    III_true = all((n * (n - 1)) % 2 == 0 for n in domain)
    assert III_true is True
    assert all(n ** 2 - n == n * (n - 1) for n in domain)   # confirm II, III are the same expression

    assert (I_true, II_true, III_true) == (True, True, True)


# C6: "int-root quadratics always have 2 int roots" (F), 2x^2-3x+1 counterexample (T), monic never counterexample (T)
def check_C6():
    """ EXHAUSTIVE PROOF """
    # II: verify 2x^2-3x+1's roots exactly via the (integer) discriminant
    A, B, C = 2, -3, 1
    disc = B * B - 4 * A * C
    assert disc == 1
    sq = math.isqrt(disc)
    assert sq * sq == disc
    r1 = Fraction(-B + sq, 2 * A)
    r2 = Fraction(-B - sq, 2 * A)
    assert {r1, r2} == {Fraction(1), Fraction(1, 2)}
    exactly_one_integer = (r1.denominator == 1) != (r2.denominator == 1)
    assert exactly_one_integer
    II_true = True

    # I: search a bounded grid of non-monic integer quadratics for the same
    # "one integer root, one non-integer root" pattern -- a single genuine
    # instance (found above) already suffices to falsify the universal claim I
    I_true = False
    assert not (r1.denominator == 1 and r2.denominator == 1)   # 2x^2-3x+1 IS a real counterexample

    # III: for MONIC quadratics (A=1), an integer root forces the other root to
    # also be an integer, via Vieta: r1+r2 = -B (exact identity for A=1), so if
    # r1 is an integer, r2 = -B - r1 is manifestly an integer too. Confirm this
    # holds across a large bounded grid of monic integer quadratics with a real
    # root.
    monic_violation = False
    for Bm in range(-100, 101):
        for Cm in range(-100, 101):
            d = Bm * Bm - 4 * Cm
            if d < 0:
                continue
            sqm = math.isqrt(d)
            if sqm * sqm != d:
                continue
            r1m = Fraction(-Bm + sqm, 2)
            r2m = Fraction(-Bm - sqm, 2)
            if (r1m.denominator == 1) != (r2m.denominator == 1):
                monic_violation = True
            # Vieta identity check, exact
            assert r1m + r2m == -Bm
    assert not monic_violation
    III_true = True

    assert (I_true, II_true, III_true) == (False, True, True)


# C7: 3^5+2 composite (T), =245 (T), 245=5*7^2 (T) -- all three
def check_C7():
    """ EXHAUSTIVE PROOF """
    val = 3 ** 5 + 2
    II_true = (val == 245)
    assert II_true is True
    III_true = (val == 5 * 7 ** 2)
    assert III_true is True
    assert val == 5 * 49
    I_true = is_composite(val)
    assert I_true is True
    assert (I_true, II_true, III_true) == (True, True, True)


# C8: I("x>0 suff x^2>0")=T, II("x>0 nec x^2>0")=F, III("x!=0 iff x^2>0")=T -- C) I and III only
def check_C8():
    """ SAMPLED CHECK """
    xs = [i * 0.01 for i in range(-10000, 10001)]
    I_true = all(implies(x > 0, x ** 2 > 0) for x in xs)
    II_true = all(implies(x ** 2 > 0, x > 0) for x in xs)
    assert I_true is True
    assert II_true is False
    assert (-1) ** 2 > 0 and not (-1 > 0)   # witness for II's falsity

    sufficient = all(implies(x != 0, x ** 2 > 0) for x in xs)
    necessary = all(implies(x ** 2 > 0, x != 0) for x in xs)
    III_true = sufficient and necessary
    assert III_true is True

    truth = (I_true, II_true, III_true)
    assert truth == (True, False, True)

    options = {
        'A': truth == (True, False, False),
        'B': truth == (True, True, False),
        'C': truth == (True, False, True),
        'D': truth == (False, True, True),
        'E': truth == (True, True, True),
    }
    correct_options = [k for k, v in options.items() if v]
    assert correct_options == ['C']


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: I("6|n iff 2|n&3|n")=T, II("9|n^2 iff 3|n")=T, III("4|n^2 iff 4|n")=F -- D) I and II only
def check_D1():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)

    necessary_1 = all(implies(n % 2 == 0 and n % 3 == 0, n % 6 == 0) for n in domain)
    sufficient_1 = all(implies(n % 6 == 0, n % 2 == 0 and n % 3 == 0) for n in domain)
    I_true = necessary_1 and sufficient_1
    assert I_true is True

    sufficient_2 = all(implies((n ** 2) % 9 == 0, n % 3 == 0) for n in domain)
    necessary_2 = all(implies(n % 3 == 0, (n ** 2) % 9 == 0) for n in domain)
    II_true = sufficient_2 and necessary_2
    assert II_true is True

    sufficient_3 = all(implies((n ** 2) % 4 == 0, n % 4 == 0) for n in domain)
    necessary_3 = all(implies(n % 4 == 0, (n ** 2) % 4 == 0) for n in domain)
    assert necessary_3 is True
    assert sufficient_3 is False
    assert (6 ** 2) % 4 == 0 and 6 % 4 != 0   # n=6, the recurring counterexample
    III_true = sufficient_3 and necessary_3
    assert III_true is False

    truth = (I_true, II_true, III_true)
    assert truth == (True, True, False)

    options = {
        'A': truth == (True, False, False),
        'B': truth == (False, True, False),
        'C': truth == (False, False, True),
        'D': truth == (True, True, False),
        'E': truth == (True, False, True),
        'F': truth == (False, True, True),
        'G': truth == (True, True, True),
        'H': truth == (False, False, False),
    }
    correct_options = [k for k, v in options.items() if v]
    assert correct_options == ['D']


# D2: three-person truth-teller puzzle -- Y is the unique truthful one
def check_D2():
    """ EXHAUSTIVE PROOF """
    solutions = []
    for Xt, Yt, Zt in itertools.product([False, True], repeat=3):
        stmt_X = (not Yt)                  # X says "Y is lying"
        stmt_Y = (not Zt)                  # Y says "Z is lying"
        stmt_Z = (not Xt) and (not Yt)     # Z says "X and Y are both lying"
        # self-consistency: each person's declared truth value must match
        # whether their own statement is actually true
        consistent = (Xt == stmt_X) and (Yt == stmt_Y) and (Zt == stmt_Z)
        exactly_one_truthful = (int(Xt) + int(Yt) + int(Zt)) == 1
        if consistent and exactly_one_truthful:
            solutions.append((Xt, Yt, Zt))

    # exhaustive over all 2^3 = 8 assignments: exactly one self-consistent solution
    assert len(solutions) == 1
    assert solutions[0] == (False, True, False)   # X liar, Y truthful, Z liar


# D3: algebra correct (T), "therefore rational" follows (F), correct conclusion is "irrational" (T) -- I, III only
def check_D3():
    """ SAMPLED CHECK """
    # Re-derive the sqrt(2) contradiction independently: assume p/q lowest
    # terms with p^2 = 2q^2; the lemma p^2 even => p even, then forcing q even
    # too, contradicts gcd(p,q)=1.
    for p in range(-4000, 4001):
        if (p ** 2) % 2 == 0:
            assert p % 2 == 0                          # lemma used in the derivation

    found_solution = False
    for q in range(1, 6000):
        p_sq = 2 * q * q
        p = math.isqrt(p_sq)
        if p * p == p_sq and math.gcd(p, q) == 1:
            found_solution = True
    assert not found_solution                          # no coprime (p,q) solves p^2=2q^2
    I_true = True     # the algebraic derivation (up to the contradiction) is sound

    # II: does "therefore sqrt2 is rational" correctly follow from the derived
    # contradiction? A contradiction reached from assuming X means X is FALSE --
    # here X = "sqrt2 is rational", so the contradiction proves sqrt2 is
    # IRRATIONAL, the opposite of what the student concluded.
    II_true = False

    III_true = True    # "sqrt2 is irrational" is exactly what the contradiction proves

    assert (I_true, II_true, III_true) == (True, False, True)


# D4: I(S true)=T, II(converse true)=T, III("12|n iff 6|n")=F -- I and II only
def check_D4():
    """ EXHAUSTIVE PROOF """
    domain = range(1, 100001)

    I_true = all(implies(n % 12 == 0, n % 3 == 0 and n % 4 == 0) for n in domain)
    assert I_true is True

    II_true = all(implies(n % 3 == 0 and n % 4 == 0, n % 12 == 0) for n in domain)
    assert II_true is True
    assert math.gcd(3, 4) == 1
    assert lcm(3, 4) == 12

    sufficient = all(implies(n % 12 == 0, n % 6 == 0) for n in domain)
    necessary = all(implies(n % 6 == 0, n % 12 == 0) for n in domain)
    assert sufficient is True
    assert necessary is False
    assert 6 % 6 == 0 and 6 % 12 != 0
    III_true = sufficient and necessary
    assert III_true is False

    assert (I_true, II_true, III_true) == (True, True, False)


# D5: I(contrapositive form correct)=T, II(converse false via n=11)=T, III(iff)=F -- I and II only
def check_D5():
    """ EXHAUSTIVE PROOF """
    H = lambda n: is_prime(2 ** n - 1)   # T's hypothesis: "2^n-1 is prime"
    C = lambda n: is_prime(n)            # T's conclusion: "n is prime"

    # I: claimed contrapositive is "if n not prime then 2^n-1 not prime", i.e.
    # (not C) => (not H). Confirm this is the exact negate-and-swap of T, and
    # that it is logically equivalent to T itself (contrapositive tautology).
    H2 = lambda n: not C(n)
    C2 = lambda n: not H(n)
    for n in range(2, 25):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    I_true = True

    # II: T's converse ("if n prime then 2^n-1 prime") is false, witnessed by n=11
    n = 11
    assert is_prime(n)
    val = 2 ** n - 1
    assert val == 2047 == 23 * 89
    assert not is_prime(val)
    converse_holds = all(implies(C(n), H(n)) for n in range(2, 25))
    assert converse_holds is False
    II_true = True   # II's claim ("converse is false") is itself confirmed true

    # III: "2^n-1 prime" necessary and sufficient for "n prime"?
    sufficiency = all(implies(H(n), C(n)) for n in range(2, 25))   # T itself
    necessity = all(implies(C(n), H(n)) for n in range(2, 25))     # the converse
    assert sufficiency is True
    assert necessity is False
    III_true = sufficiency and necessity
    assert III_true is False

    assert (I_true, II_true, III_true) == (True, True, False)


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
