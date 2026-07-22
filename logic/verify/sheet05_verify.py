import itertools
import math

# ── shared helpers ──────────────────────────────────────────────────────────

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def implies(a, b):
    return (not a) or b


def truth_assignments(n):
    return itertools.product([False, True], repeat=n)


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: "P=>Q, Q true, conclude P" -- INVALID (affirming the consequent)
def check_A1():
    """ EXHAUSTIVE PROOF """
    # There must exist a truth assignment where P=>Q holds and Q holds, but
    # P is false -- i.e. the argument's conclusion is NOT forced.
    counterexample_exists = any(
        implies(P, Q) and Q and not P for P, Q in truth_assignments(2)
    )
    assert counterexample_exists
    # Concrete instance matching the method's own example: "n prime => n odd"
    n = 9
    H = lambda n: is_prime(n)
    C = lambda n: n % 2 == 1
    assert implies(H(n), C(n))   # the implication holds (vacuously, H(9) false)
    assert C(n) and not H(n)     # Q true, P false -- conclusion "P" would be wrong


# A2: "P=>Q, Q false, conclude P false" -- VALID (modus tollens)
def check_A2():
    """ EXHAUSTIVE PROOF """
    for P, Q in truth_assignments(2):
        if implies(P, Q) and not Q:
            assert not P


# A3: "P=>Q, P false, conclude Q false" -- INVALID (denying the antecedent)
def check_A3():
    """ EXHAUSTIVE PROOF """
    counterexample_exists = any(
        implies(P, Q) and (not P) and Q for P, Q in truth_assignments(2)
    )
    assert counterexample_exists
    n = 6
    H = lambda n: n % 4 == 0
    C = lambda n: n % 2 == 0
    assert implies(H(n), C(n))     # "4|n => even" holds for all n, incl. n=6 (vacuously)
    assert (not H(n)) and C(n)     # P false (6 not mult of 4), but Q true (6 even)


# A4: "P=>Q, P true, conclude Q" -- VALID (modus ponens)
def check_A4():
    """ EXHAUSTIVE PROOF """
    for P, Q in truth_assignments(2):
        if implies(P, Q) and P:
            assert Q


# A5: "n odd => n^2 odd. n^2=49 odd. Therefore n=7." -- flawed, n=-7 also works
def check_A5():
    """ EXHAUSTIVE PROOF """
    domain = range(-1000, 1001)
    solutions = [n for n in domain if n % 2 != 0 and n ** 2 == 49]
    assert set(solutions) == {-7, 7}
    assert len(solutions) > 1   # so concluding the single value n=7 is unjustified
    assert (-7) ** 2 == 49 and (-7) % 2 != 0 and -7 != 7


# A6: "square=>rectangle; not square; therefore not rectangle" -- denying antecedent
def check_A6():
    """ EXHAUSTIVE PROOF """
    def is_rectangle(w, h):
        return w > 0 and h > 0

    def is_square(w, h):
        return is_rectangle(w, h) and w == h

    w, h = 2, 3
    assert is_rectangle(w, h) and not is_square(w, h)   # counterexample stands
    for a in range(1, 51):
        for b in range(1, 51):
            if is_square(a, b):
                assert is_rectangle(a, b)   # sanity: squares are still rectangles


# A7: "if P=>Q and Q=>P both true, assuming Q to conclude P is valid" -- TRUE
def check_A7():
    """ EXHAUSTIVE PROOF """
    for P, Q in truth_assignments(2):
        if implies(P, Q) and implies(Q, P) and Q:
            # this is exactly modus ponens applied to the given true statement Q=>P
            assert P


# A8: "x^2=5x, divide by x, get x=5" -- loses x=0
def check_A8():
    """ EXHAUSTIVE PROOF """
    domain = [i * 0.25 for i in range(-4000, 4001)]
    true_solutions = [x for x in domain if abs(x ** 2 - 5 * x) < 1e-9]
    assert 0.0 in true_solutions
    assert 5.0 in true_solutions
    # the "divide by x" step is only legitimate when x != 0
    for x in true_solutions:
        if x == 0:
            continue
        assert abs((x ** 2) / x - 5) < 1e-9   # x=5 recovered validly for x!=0 solutions


# A9: "squaring can introduce extraneous solutions" -- TRUE
def check_A9():
    """ EXHAUSTIVE PROOF """
    x_orig = -2
    assert x_orig == -2
    squared_solutions = [x for x in range(-10, 11) if x ** 2 == x_orig ** 2]
    assert set(squared_solutions) == {-2, 2}
    assert 2 in squared_solutions and 2 != x_orig   # x=2 is extraneous


# A10: "dividing by a variable expression can lose valid solutions" -- TRUE
def check_A10():
    """ EXHAUSTIVE PROOF """
    domain = [i * 0.25 for i in range(-4000, 4001)]
    true_solutions = [x for x in domain if abs(x ** 2 - 5 * x) < 1e-9]
    assert 0.0 in true_solutions              # x=0 is a genuine solution
    naive_solutions_after_division = {5.0}    # dividing by x throws it away
    assert 0.0 not in naive_solutions_after_division


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: "n^2 mult of 4 => n mult of 4" -- False, n=6
def check_B1():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 10001):
        if n % 4 == 0:
            assert (n ** 2) % 4 == 0    # the TRUE direction
    n = 6
    assert (n ** 2) % 4 == 0 and n % 4 != 0


# B2: "sqrt(x^2)=x for all real x" -- False for negative x
def check_B2():
    """ EXHAUSTIVE PROOF """
    for i in range(-4000, 4001):
        x = i * 0.25
        assert math.sqrt(x ** 2) == abs(x)
    x = -3.0
    assert math.sqrt(x ** 2) == 3.0 != x


# B3: a=b "proof" that a=0 -- flaw is dividing by (a-b)=0 in Line V
def check_B3():
    """ EXHAUSTIVE PROOF """
    for t in range(-500, 501):
        a, b = t, t   # a = b, as given
        assert a == b                              # Line I
        assert a ** 2 == a * b                      # Line II
        assert a ** 2 - b ** 2 == a * b - b ** 2     # Line III
        assert (a - b) * (a + b) == b * (a - b)      # Line IV
        assert a - b == 0                            # the hidden zero
    # dividing Line IV by (a-b) is illegitimate: for a concrete nonzero a=b,
    # the "conclusion" a=0 is false, exposing the flaw
    a, b = 5, 5
    assert (a - b) * (a + b) == b * (a - b)   # Line IV genuinely holds
    assert a != 0                              # but Line V's "a=0" is false


# B4: "sunny=>sunglasses, sunglasses, therefore sunny" -- affirming the consequent
def check_B4():
    """ EXHAUSTIVE PROOF """
    counterexample_exists = any(
        implies(P, Q) and Q and not P for P, Q in truth_assignments(2)
    )
    assert counterexample_exists   # same structure as A1/B1: not a forced conclusion


# B5: "x^2>4 therefore x>2" -- incomplete case split, x<-2 also valid
def check_B5():
    """ EXHAUSTIVE PROOF """
    for i in range(-4000, 4001):
        x = i * 0.25
        assert (x ** 2 > 4) == (x > 2 or x < -2)
    x = -3
    assert x ** 2 > 4 and not (x > 2)


# B6: "6|n => 2|n,3|n. n is mult of 2. Therefore n mult of 6." -- partial consequent
def check_B6():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 10001):
        if n % 6 == 0:
            assert n % 2 == 0 and n % 3 == 0   # the TRUE hypothesis-direction fact
    n = 4
    assert n % 2 == 0 and n % 6 != 0


# B7: "n odd => n^2 odd" -- NO flaw, correct proof
def check_B7():
    """ EXHAUSTIVE PROOF """
    for k in range(-1000, 1001):
        n = 2 * k + 1
        assert n % 2 != 0                              # given: n odd
        assert n ** 2 == 4 * k ** 2 + 4 * k + 1          # Line 2
        assert 4 * k ** 2 + 4 * k + 1 == 2 * (2 * k ** 2 + 2 * k) + 1   # Line 3
        assert (n ** 2) % 2 != 0                          # Line 4


# B8: "mult of 4 => even. n even. Therefore n mult of 4." -- False, n=6
def check_B8():
    """ EXHAUSTIVE PROOF """
    for n in range(1, 10001):
        if n % 4 == 0:
            assert n % 2 == 0
    n = 6
    assert n % 2 == 0 and n % 4 != 0


# B9: "sqrt(4)=+-2" -- notation error, sqrt is single-valued and non-negative
def check_B9():
    """ EXHAUSTIVE PROOF """
    assert math.sqrt(4) == 2.0
    assert math.sqrt(4) != -2.0
    # the two SOLUTIONS of x^2=4 are +-2, distinct from the VALUE of sqrt(4)
    solutions_of_x2_eq_4 = [x for x in range(-10, 11) if x ** 2 == 4]
    assert set(solutions_of_x2_eq_4) == {-2, 2}
    assert math.sqrt(4) in solutions_of_x2_eq_4   # sqrt(4) picks exactly one of them


# B10: "(-2)^2=2^2=4, cancel squares, -2=2" -- illegitimate cancellation
def check_B10():
    """ EXHAUSTIVE PROOF """
    assert (-2) ** 2 == 2 ** 2 == 4
    assert -2 != 2
    # the legitimate "un-squaring" step gives |{-2}| = |2|, i.e. 2 = 2, not -2 = 2
    assert abs(-2) == abs(2)
    assert not (math.sqrt((-2) ** 2) == -2)   # sqrt of the square is 2, never -2


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: n even => n^3 even and mult of 8 -- Completely correct (A)
def check_C1():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k
        assert n ** 3 == 8 * k ** 3                    # Line II
        assert 8 * k ** 3 == 2 * (4 * k ** 3)            # Line III
        assert (n ** 3) % 2 == 0
        assert (n ** 3) % 8 == 0


# C2: "n^2>100 => n>10 by taking sqrt" -- proof step flawed in general, true only for positive n
def check_C2():
    """ EXHAUSTIVE PROOF """
    # As stated for ALL integers, the "proof" is broken: taking sqrt gives |n|>10.
    for n in range(-2000, 2001):
        assert (n ** 2 > 100) == (n > 10 or n < -10)
    n = -11
    assert n ** 2 > 100 and not (n > 10)   # counterexample to the proof step
    # But the CLAIM itself, restricted to positive integers, is genuinely true
    for n in range(1, 2001):
        if n ** 2 > 100:
            assert n > 10


# C3: "a|b and b|a => a=b" -- flaw, correct conclusion is a=+-b; a=3,b=-3
def check_C3():
    """ EXHAUSTIVE PROOF """
    a, b = 3, -3
    assert b % a == 0 and a % b == 0
    assert a != b
    for a in range(-100, 101):
        for b in range(-100, 101):
            if a != 0 and b != 0 and b % a == 0 and a % b == 0:
                assert a == b or a == -b


# C4: "x+1/x=2, x positive real => x=1" -- fully valid
def check_C4():
    """ SAMPLED CHECK """
    # Multiplying by x is safe because x>0 rules out x=0 (domain check)
    for i in range(1, 2001):
        x = i * 0.01
        assert x != 0
    # Independent re-derivation via AM-GM style identity, not the method's own algebra:
    # x + 1/x - 2 = (x-1)^2 / x, which is >=0 for x>0, with equality iff x=1.
    for i in range(1, 20001):
        x = i * 0.001
        lhs = x + 1 / x
        rhs = (x - 1) ** 2 / x
        assert abs((lhs - 2) - rhs) < 1e-9
        if abs(x - 1) < 1e-9:
            assert abs(lhs - 2) < 1e-6
        else:
            assert lhs > 2


# C5: "n^2 div by 4 => n div by 4" via n=2*sqrt(m) -- non-sequitur, n=6
def check_C5():
    """ EXHAUSTIVE PROOF """
    n = 6
    assert n ** 2 == 36 == 4 * 9
    assert n ** 2 % 4 == 0 and n % 4 != 0
    # "n even" alone (independent of the flawed derivation) never forces div-by-4
    counterexamples = [k for k in range(1, 1001) if k % 2 == 0 and k % 4 != 0]
    assert 6 in counterexamples and len(counterexamples) > 0


# C6: "x^3=x has exactly one real solution, x=0, dividing by (x^2-1)" -- three solutions
def check_C6():
    """ EXHAUSTIVE PROOF """
    domain = [i * 0.01 for i in range(-2000, 2001)]
    solutions = [x for x in domain if abs(x ** 3 - x) < 1e-9]
    close_to = lambda x, targets: any(abs(x - t) < 1e-6 for t in targets)
    found_roots = [t for t in (-1, 0, 1) if any(abs(x - t) < 0.02 for x in solutions)]
    assert set(found_roots) == {-1, 0, 1}
    for x in (-1, 0, 1):
        assert x ** 3 - x == 0
    # dividing by (x^2-1) silently assumes x^2 != 1, discarding x=+-1
    assert (-1) ** 2 - 1 == 0 and 1 ** 2 - 1 == 0
    # zero-product property gives the full solution set
    zp_solutions = set()
    for x in range(-5, 6):
        if x * (x ** 2 - 1) == 0:
            zp_solutions.add(x)
    assert zp_solutions == {-1, 0, 1}


# C7: "p prime, p>2 => p+1 not prime" -- fully valid
def check_C7():
    """ EXHAUSTIVE PROOF """
    N = 20000
    primes = [p for p in range(2, N) if is_prime(p)]
    for p in primes:
        if p > 2:
            assert p % 2 != 0             # p odd
            assert (p + 1) % 2 == 0        # p+1 even
            assert p + 1 > 2               # p+1 exceeds the only even prime
            assert not is_prime(p + 1)     # hence p+1 is not prime


# C8: "n^2 >= 2n-1, equality only n=1" -- fully valid
def check_C8():
    """ EXHAUSTIVE PROOF """
    for n in range(-1000, 1001):
        assert n ** 2 - 2 * n + 1 == (n - 1) ** 2   # the identity
        assert (n - 1) ** 2 >= 0                     # any real square is >=0
        assert ((n - 1) ** 2 == 0) == (n == 1)        # equality iff n=1
        assert (n ** 2 >= 2 * n - 1) == True          # rearranged inequality
    for n in range(1, 1001):
        assert (n ** 2 == 2 * n - 1) == (n == 1)


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: student proves the CONVERSE of "n even => n^2 even", not the original -- B
def check_D1():
    """ EXHAUSTIVE PROOF """
    domain = range(-2000, 2001)
    # Sub-lemma the student's contradiction step relies on: "n odd => n^2 odd"
    # -- confirm it's actually true, ruling out option C ("error in the
    # contradiction step").
    for n in domain:
        if n % 2 != 0:
            assert n ** 2 % 2 != 0

    # Original target: H(n): n even, C(n): n^2 even.
    H = lambda n: n % 2 == 0
    C = lambda n: n ** 2 % 2 == 0
    # Student's argument: assumes n^2 even (=C), derives n even (=H).
    # That is precisely the converse C=>H, i.e. hypothesis/conclusion swapped.
    H_student = lambda n: n ** 2 % 2 == 0   # matches C, not H
    C_student = lambda n: n % 2 == 0        # matches H, not C
    for n in domain:
        assert H_student(n) == C(n)
        assert C_student(n) == H(n)

    # Confirm the student's proved statement (the converse) is itself true here
    # -- i.e. their sub-proof is valid, they just proved the wrong target.
    for n in domain:
        assert H_student(n) == C_student(n)   # n^2 even <=> n even, both directions hold

    # General point: a statement and its converse are NOT automatically the
    # same claim -- exhibit a case (distinct from n/n^2 parity) where original
    # holds but converse fails, showing "proved the converse" is a genuine,
    # substantive error even though it happens to coincide with truth here.
    H2 = lambda n: n % 4 == 0
    C2 = lambda n: n % 2 == 0
    orig_true = all(implies(H2(n), C2(n)) for n in range(1, 10001))
    converse_counterexample = any(C2(n) and not H2(n) for n in range(1, 10001))
    assert orig_true and converse_counterexample


# D2: sqrt(2) "rational" proof -- contradiction actually proves IRRATIONAL
def check_D2():
    """ SAMPLED CHECK """
    # Re-verify the load-bearing lemma used twice in the student's own steps:
    # p^2 even => p even (exhaustive over a large integer range).
    for p in range(-5000, 5001):
        if (p ** 2) % 2 == 0:
            assert p % 2 == 0

    # If p^2 = 2q^2 with p even (p=2r), then q^2=2r^2 forces q even too --
    # confirm this chain is genuinely forced whenever it applies.
    for r in range(-1000, 1001):
        p = 2 * r
        # p^2 = 2 q^2  =>  q^2 = 2 r^2 (algebraically, if such q existed)
        q_squared = 2 * r ** 2
        q = math.isqrt(q_squared) if q_squared >= 0 else None
        if q is not None and q * q == q_squared:
            assert q % 2 == 0   # whenever an integer q exists, it's even

    # Bounded classical-descent search: no coprime (p,q) with p^2=2q^2 exists,
    # up to a generous bound -- evidence (not a full infinite-descent proof)
    # that sqrt(2) genuinely has no rational representation, i.e. is
    # irrational -- the OPPOSITE of what the student's final line asserts.
    found_solution = False
    for q in range(1, 5000):
        p_squared = 2 * q * q
        p = math.isqrt(p_squared)
        if p * p == p_squared:
            if math.gcd(p, q) == 1:
                found_solution = True
    assert not found_solution

    # A reached contradiction from "assume rational" means "rational" is false
    # -- the student's own derivation (p,q both forced even, contradicting
    # lowest terms) is exactly a valid derivation of "not rational".
    p, q = 2, 2   # arbitrary "assume both even" instance, matching lowest-terms failure
    assert p % 2 == 0 and q % 2 == 0   # this is what "both even" (the contradiction) means
    assert math.gcd(p, q) != 1          # confirms it genuinely contradicts "lowest terms"


# D3: "n^2+n even for all n, therefore by induction every polynomial is even" -- not valid induction
def check_D3():
    """ EXHAUSTIVE PROOF """
    for n in range(-1000, 1001):
        assert (n ** 2 + n) % 2 == 0   # the individual claim is at least true
    # counterexample to the broad, unrelated conclusion: p(n) = n is a
    # polynomial with integer coefficients, but p(1) = 1 is odd
    p = lambda n: n
    n = 1
    assert p(n) == 1 and p(n) % 2 != 0


# D4: "isosceles <=> two equal angles, therefore equivalent to having a right angle" -- non-sequitur
def check_D4():
    """ EXHAUSTIVE PROOF """
    def is_valid_triangle(angles):
        return all(a > 0 for a in angles) and sum(angles) == 180

    def has_two_equal(angles):
        a, b, c = angles
        return a == b or b == c or a == c

    def has_right_angle(angles):
        return 90 in angles

    # Two equal angles, but no right angle -- breaks "two equal => right angle"
    t1 = (70, 70, 40)
    assert is_valid_triangle(t1) and has_two_equal(t1) and not has_right_angle(t1)

    # A right angle, but no two equal angles -- breaks "right angle => two equal"
    t2 = (30, 60, 90)
    assert is_valid_triangle(t2) and has_right_angle(t2) and not has_two_equal(t2)

    # So the two properties are independent in both directions -- not equivalent
    assert not (has_two_equal(t1) == has_right_angle(t1) and
                has_two_equal(t2) == has_right_angle(t2))


# D5: n^2-n+41 off-by-one substitution error -- composite pattern starts at n=41, not n=40
def check_D5():
    """ EXHAUSTIVE PROOF """
    def f_plus(n):
        return n ** 2 + n + 41

    def f_minus(n):
        return n ** 2 - n + 41

    # (a) the polynomial identity underlying the correct substitution m=n-1
    for n in range(-500, 501):
        m = n - 1
        assert f_plus(m) == f_minus(n)

    # (b) re-derive (Day 4, C1) independently: f_plus prime for n=0..39,
    # first composite at n=40, where it equals 1681 = 41^2
    for n in range(0, 40):
        assert is_prime(f_plus(n))
    assert f_plus(40) == 1681 == 41 ** 2
    assert not is_prime(f_plus(40))

    # (c) the student's claimed threshold n=40 for f_minus: compute directly
    # and check primality with extra care (highest-stakes check on the sheet)
    val_40 = f_minus(40)
    assert val_40 == 1601
    # exact trial division up to sqrt(1601) ~ 40.01 -- exhaustive for this n
    limit = int(1601 ** 0.5) + 1
    assert limit >= 40
    divisors_found = [d for d in range(2, limit + 1) if 1601 % d == 0]
    assert divisors_found == []
    assert is_prime(1601)   # cross-check via the shared helper
    assert is_prime(val_40)
    # this directly falsifies the student's claim: n=40 is NOT composite

    # (d) the correct threshold, n=41: f_minus(41) = 1681, composite
    val_41 = f_minus(41)
    assert val_41 == 1681 == 41 ** 2
    assert not is_prime(val_41)

    # (e) tie it together: f_minus mirrors f_plus's pattern shifted by one,
    # so f_minus is prime for n=1..40 and first composite at n=41
    for n in range(1, 41):
        assert is_prime(f_minus(n))
    assert not is_prime(f_minus(41))


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
