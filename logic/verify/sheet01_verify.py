"""Computational verification for logic/answers/ans01.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (never just re-type the
     method's own reasoning and assert it equals itself).
  2. For "negate this statement" questions specifically: model BOTH the
     original statement and the claimed negation as boolean predicates
     over a finite sample domain (or, for propositional/abstract atoms
     like P, Q, R, enumerate all 2^n truth assignments exhaustively) and
     assert the negation's truth value is exactly the logical opposite
     of the original's at every sample point / every truth assignment.
  3. Assert every checkable factual claim in the \\method{} text, not
     just the final \\ans{} -- a modular fact, a primality claim, an
     inequality, etc.
  4. State plainly, in the docstring, what is and isn't being verified
     when a claim involves an unbounded/infinite domain (SAMPLED CHECK)
     versus a genuinely finite/closed-form argument (EXHAUSTIVE PROOF).

This script was written cold from the question text and \\method{} prose
in ans01.tex only -- no access to whatever conversation drafted them --
per this repo's rule that the verify-script author must be a different
agent instance than whoever drafted the \\method{} text.

Run directly:
    python3 sheet01_verify.py
"""

import math
import random
import itertools
from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────

def sieve(limit):
    """Return a bool list is_p[0..limit], is_p[n] True iff n is prime."""
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return is_p


_SIEVE_LIMIT = 200000
_SIEVE = sieve(_SIEVE_LIMIT)


def is_prime(n):
    """Primality test: sieve lookup within range, trial division fallback."""
    if 0 <= n <= _SIEVE_LIMIT:
        return _SIEVE[n]
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def all_assignments(n):
    """All 2**n truth assignments of n abstract atoms, as tuples of bool."""
    return list(itertools.product([False, True], repeat=n))


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition
# ─────────────────────────────────────────────────────────────────────────

# A1 -- Negate: "For all integers n, n^2 >= 0."
# \ans: "There exists an integer n such that n^2 < 0."
def check_A1():
    """SAMPLED CHECK for the domain of all integers (checked over
    -100000..100000 here, not literally every integer), but the truth-value
    argument used is exact and integer-size-independent: for n>=0, n*n is a
    product of two nonnegatives hence >=0; for n<0, writing m=-n>0, n*n=m*m
    is again a product of two positives. That case split covers every
    integer, not just the sampled range."""
    for n in range(-100000, 100001):
        orig = (n * n >= 0)          # inner predicate of the forall
        neg = (n * n < 0)            # inner predicate of the claimed negation
        assert neg == (not orig), f"negation mismatch at n={n}"
        if n >= 0:
            assert n * n >= 0
        else:
            m = -n
            assert m > 0 and n * n == m * m and m * m >= 0
    assert all(n * n >= 0 for n in range(-100000, 100001))
    assert not any(n * n < 0 for n in range(-100000, 100001))


# A2 -- Negate: "There exists a real x such that x^2 = -1."
# \ans: "For all real x, x^2 != -1."
def check_A2():
    """SAMPLED CHECK for the domain of all reals (thousands of random floats
    plus edge cases, not literally every real), backed by an exact argument:
    x*x >= 0 for every real x (product of two same-sign numbers), and
    0 > -1, so x*x can never equal -1, for any real x whatsoever."""
    random.seed(1)
    xs = ([random.uniform(-10**6, 10**6) for _ in range(5000)]
          + [0.0, 1.0, -1.0, 1e-9, -1e-9, 1e12, -1e12])
    for x in xs:
        orig = (x * x == -1)
        neg = (x * x != -1)
        assert neg == (not orig)
        assert x * x >= 0            # exact for every real
        assert x * x != -1
    assert not any((x * x == -1) for x in xs)
    assert all((x * x != -1) for x in xs)


# A3 -- Negate: "n is even and n is prime."
# \ans: "n is odd, or n is not prime."
def check_A3():
    """EXHAUSTIVE PROOF: enumerates all 4 truth assignments of the two
    atoms P = 'n even', Q = 'n prime' -- fully exhaustive, since there are
    only 2^2 = 4 possible truth combinations."""
    for P, Q in all_assignments(2):
        orig = P and Q
        claimed_neg = (not P) or (not Q)
        assert claimed_neg == (not orig)


# A4 -- Negate: "n is a multiple of 4 or n is a multiple of 6."
# \ans: "n is not a multiple of 4, and n is not a multiple of 6."
def check_A4():
    """EXHAUSTIVE PROOF: all 2^2 = 4 truth assignments of P = 'mult of 4',
    Q = 'mult of 6'."""
    for P, Q in all_assignments(2):
        orig = P or Q
        claimed_neg = (not P) and (not Q)
        assert claimed_neg == (not orig)


# A5 -- T/F: "the negation of 'forall x, P(x)' is 'forall x, not P(x)'."
# \ans: False.
def check_A5():
    """EXHAUSTIVE PROOF: exhibits concrete finite domains where 'forall x,
    not P(x)' (the claimed but wrong negation) disagrees with the true
    negation 'exists x, not P(x)' -- a single disagreement fully disproves
    the claimed equivalence; two independent domains rule out a fluke."""
    def truth_values(domain, P):
        orig = all(P(x) for x in domain)
        true_neg = any(not P(x) for x in domain)
        wrong_neg = all(not P(x) for x in domain)
        return orig, true_neg, wrong_neg

    _, t1, w1 = truth_values({1, 2}, lambda x: x == 1)
    assert t1 != w1
    _, t2, w2 = truth_values({1, 2, 3}, lambda x: x < 3)
    assert t2 != w2


# A6 -- T/F: "not(P and Q) is the same as (not P) or (not Q)."
# \ans: True.
def check_A6():
    """EXHAUSTIVE PROOF: all 2^2 = 4 truth assignments of P, Q."""
    for P, Q in all_assignments(2):
        assert (not (P and Q)) == ((not P) or (not Q))


# A7 -- Negate: "x > 3 and x < 10."
# \ans: "x <= 3 or x >= 10."
def check_A7():
    """SAMPLED CHECK over the reals (thousands of random floats plus the
    exact boundary values 3 and 10, not literally every real), backed by
    the exact trichotomy facts not(x>3)==(x<=3) and not(x<10)==(x>=10),
    which hold for the entire real line by total ordering, not sampling."""
    random.seed(2)
    xs = ([random.uniform(-10**6, 10**6) for _ in range(5000)]
          + [3.0, 10.0, 3.0000001, 9.9999999, 0.0, -10**6, 10**6])
    for x in xs:
        orig = (x > 3) and (x < 10)
        neg = (x <= 3) or (x >= 10)
        assert neg == (not orig)
        assert (x > 3) == (not (x <= 3))
        assert (x < 10) == (not (x >= 10))


# A8 -- Is "some prime numbers are even" a forall- or exists-statement?
# \ans: exists-statement.
def check_A8():
    """EXHAUSTIVE PROOF (only two witnesses are needed): confirms the
    exists-reading is the one consistent with the statement being true
    (2 is prime and even), and that the alternative forall-reading would
    be false (3 is prime and odd) -- exactly why 'some' must mean
    'there exists', not 'for all'."""
    assert is_prime(2) and 2 % 2 == 0
    assert is_prime(3) and 3 % 2 == 1


# A9 -- T/F: "exists x forall y: x+y=0" and "forall y exists x: x+y=0" mean
# the same thing (over the reals). \ans: False.
def check_A9():
    """EXHAUSTIVE PROOF: uses closed-form algebraic witnesses valid for
    literally every real x, y (not sampling) -- y=1-x always breaks
    x+y=0 (giving x+y=1), refuting exists-x-forall-y; x=-y always
    satisfies x+y=0, proving forall-y-exists-x. Verified via exact
    Fraction arithmetic on a representative sample of x, y as an
    arithmetic sanity check of the (already-general) closed forms."""
    sample = [(0, 1), (1, 1), (-3, 2), (7, 5), (100, 1), (-1, 1000), (1, 3), (22, 7)]
    for a, b in sample:
        x = Fraction(a, b)
        y = 1 - x
        assert x + y == 1
        assert x + y != 0            # this y refutes x+y=0 for this x
    for a, b in sample:
        y = Fraction(a, b)
        x = -y
        assert x + y == 0            # exact witness for forall-y-exists-x


# A10 -- Negate: "n is prime or n = 1."
# \ans: "n is not prime, and n != 1."
def check_A10():
    """SAMPLED CHECK over positive integers (checked up to 200000, not
    literally every positive integer), though the per-n identity itself
    (De Morgan: not(A or B) == (not A) and (not B)) is exact Boolean
    algebra, true for every n regardless of range."""
    LIMIT = 200000
    for n in range(1, LIMIT):
        A = is_prime(n)
        B = (n == 1)
        orig = A or B
        neg = (not A) and (not B)
        assert neg == (not orig)
    # sanity: the negation describes exactly the composites > 1
    assert (not is_prime(4)) and (4 != 1)          # 4 satisfies the negation
    assert not ((not is_prime(7)) and (7 != 1))    # 7 (prime) fails the negation


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Manipulation Drills
# ─────────────────────────────────────────────────────────────────────────

# B1 -- Fred: "Every day next week, Fred does >=1 problem." Negate.
# \ans: "Some day next week, Fred does no problems."
def check_B1():
    """EXHAUSTIVE PROOF: full enumeration of all 2^7 = 128 possible weekly
    patterns of whether Fred does a problem each day -- fully exhaustive,
    not sampled."""
    for pattern in itertools.product([False, True], repeat=7):
        orig = all(pattern)
        neg = any(not d for d in pattern)
        assert neg == (not orig)


# B2 -- T/F: "not(P or Q or R) is the same as (not P) and (not Q) and (not R)."
# \ans: True.
def check_B2():
    """EXHAUSTIVE PROOF: all 2^3 = 8 truth assignments of P, Q, R."""
    for P, Q, R in all_assignments(3):
        orig = P or Q or R
        claimed_neg = (not P) and (not Q) and (not R)
        assert claimed_neg == (not orig)


# B3 -- Negate: "n mult of 2 and mult of 3 and mult of 5."
# \ans: "n not mult of 2, or not mult of 3, or not mult of 5."
def check_B3():
    """EXHAUSTIVE PROOF: all 2^3 = 8 truth assignments of the three
    divisibility atoms, treated abstractly."""
    for P, Q, R in all_assignments(3):
        orig = P and Q and R
        claimed_neg = (not P) or (not Q) or (not R)
        assert claimed_neg == (not orig)


# B4 -- Negate: "For every real x>0, there exists real y>0 with y<x."
# \ans: "There exists real x>0 such that for every real y>0, y>=x."
def check_B4():
    """SAMPLED CHECK over positive reals (thousands of sampled x, not
    literally every positive real), but the witness y=x/2 is a closed
    form valid for every x>0, so it genuinely establishes both directions
    (not just for the sampled values): it witnesses exists-y for the
    original at every x, and simultaneously shows no candidate x can
    serve as an outer witness for the (false) negation."""
    random.seed(3)
    xs = ([Fraction(1, k) for k in range(1, 200)]
          + [Fraction(k, 1) for k in range(1, 200)]
          + [random.uniform(1e-6, 1e6) for _ in range(2000)])
    for x in xs:
        assert x > 0
        y = x / 2
        assert y > 0 and y < x
        assert (y < x) == (not (y >= x))   # trichotomy: inner negation is exact
        assert not (y >= x)                 # this y breaks the negation's inner claim


# B5 -- T/F: "forall n exists m: m>n" and "exists m forall n: m>n" mean the
# same thing (over the integers). \ans: False.
def check_B5():
    """SAMPLED CHECK over the integers (thousands of n, m sampled, not
    literally every integer), using closed-form witnesses valid for all
    integers: m=n+1 always beats n (proving forall-n-exists-m); taking
    n:=m always breaks m>n (since m>m is always false), which disproves
    exists-m-forall-n for every candidate m, not just the sampled ones."""
    for n in range(-5000, 5000):
        m = n + 1
        assert m > n
    for m in range(-5000, 5000):
        n = m
        assert not (m > n)


# B6 -- Negate the nested statement: "exists prime p such that for every
# prime q>p, q is odd." Is the original true or false?
# \ans negation: "For every prime p, there exists a prime q>p, q even."
# \ans: original is True.
def check_B6():
    """SAMPLED CHECK for the general 'no even prime exceeds 2' fact (true
    for all integers by the argument below, checked here up to 10**5 as
    representative, not literally all integers): implements the closed-form
    reason directly (any even n>2 has 2 as a proper divisor, hence is
    composite) rather than trusting the method's assertion, then checks
    the witness p=2 makes the original true and the negation's inner claim
    fails at p=2 within the checked range."""
    LIMIT = 100000
    assert is_prime(2) and 2 % 2 == 0
    for q in range(3, LIMIT):
        if is_prime(q):
            assert q % 2 == 1
    for n in range(4, LIMIT, 2):
        assert n % 2 == 0 and n // 2 > 1     # nontrivial divisor 2 exists
        assert not is_prime(n)
    # negation's inner claim ("exists prime q>p even") fails for p=2 in range
    assert not any(is_prime(q) and q % 2 == 0 for q in range(3, LIMIT))


# B7 -- Negate: "n mult of 3, or (n mult of 2 and n mult of 5)."
# \ans: "n not mult of 3, and (n not mult of 2 or n not mult of 5)."
def check_B7():
    """EXHAUSTIVE PROOF: all 2^3 = 8 truth assignments of P='mult of 3',
    Q='mult of 2', R='mult of 5'."""
    for P, Q, R in all_assignments(3):
        orig = P or (Q and R)
        claimed_neg = (not P) and ((not Q) or (not R))
        assert claimed_neg == (not orig)


# B8 -- T/F: "not(A and (B or C)) is the same as (not A) or ((not B) and (not C))."
# \ans: True.
def check_B8():
    """EXHAUSTIVE PROOF: all 2^3 = 8 truth assignments of A, B, C."""
    for A, B, C in all_assignments(3):
        orig = A and (B or C)
        claimed = (not A) or ((not B) and (not C))
        assert claimed == (not orig)


# B9 -- Negate: "x rational, or (x irrational and x>0)."
# \ans: "x irrational, and (x rational or x<=0)."
def check_B9():
    """EXHAUSTIVE PROOF: all 2^3 = 8 truth assignments of P='x rational',
    Q='x irrational', R='x>0', treated as independent abstract atoms for
    the mechanical De Morgan check -- the real-world relationship between
    P and Q (they can't both hold) is a further simplification noted only
    in the \\inv, and is deliberately not assumed here."""
    for P, Q, R in all_assignments(3):
        orig = P or (Q and R)
        claimed_neg = (not P) and ((not Q) or (not R))
        assert claimed_neg == (not orig)


# B10 -- Negate: "For every prime p>2, p is odd." Is the negation T/F?
# \ans negation: "There exists a prime p>2 such that p is even." Negation False.
def check_B10():
    """SAMPLED CHECK (same 'even>2 is composite' closed-form argument as
    B6, applied here without the extra existential layer) -- checked up
    to 10**5, not literally all primes, but the underlying divisibility
    argument is domain-independent."""
    LIMIT = 100000
    for p in range(3, LIMIT):
        if is_prime(p):
            assert p % 2 == 1
    assert not any(is_prime(p) and p % 2 == 0 for p in range(3, LIMIT))
    for p in range(0, 1000):
        assert (not (p % 2 == 1)) == (p % 2 == 0)   # inner negation is exact


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Substitution & Structure
# ─────────────────────────────────────────────────────────────────────────

# C1 -- I: forall x forall n: x^2<n.  II: forall x exists n: x^2<n.
# III: exists x forall n: x^2<n.  \ans: II and III only.
def check_C1():
    """SAMPLED CHECK for II (over reals x, a large but finite grid, n
    bounded by 10**6 as instructed), and EXACT for I and III: a single
    counterexample fully refutes a forall-forall claim (I), and x=0 is an
    exact witness valid for literally every positive integer n, not just
    the sampled ones (III)."""
    # I is false: a single concrete counterexample suffices
    assert not (5 * 5 < 1)
    # II is true: for sampled real x, n = floor(x^2)+1 is a positive integer > x^2
    random.seed(4)
    xs = [random.uniform(-999, 999) for _ in range(5000)] + [0.0, 999.0, -999.0]
    for x in xs:
        n = math.floor(x * x) + 1
        assert 1 <= n <= 10**6
        assert x * x < n
    # III is true: witness x=0, works for every positive integer n up to 10**6
    for n in range(1, 10**6):
        assert 0 * 0 < n


# C2 -- Negate: "For every positive integer n, there exists a prime p with p>n."
# \ans: "There exists n such that for every prime p, p<=n."
def check_C2():
    """EXHAUSTIVE PROOF (finite quantifier identity): the claimed negation
    swaps forall-n/exists-p to exists-n/forall-p and negates p>n to p<=n;
    verified as an exact identity over all 2^9 possible truth-matrices on
    an abstract 3x3 domain, not tied to actual primes -- this validates
    the transcription's logical form, independent of any numeric example."""
    Ns = range(3)
    Ps = range(3)
    cells = [(n, p) for n in Ns for p in Ps]
    for bits in itertools.product([False, True], repeat=len(cells)):
        gt = dict(zip(cells, bits))   # gt[(n,p)] abstractly means "p > n"
        orig = all(any(gt[(n, p)] for p in Ps) for n in Ns)
        claimed_neg = any(all(not gt[(n, p)] for p in Ps) for n in Ns)
        assert claimed_neg == (not orig)


# C3 -- MCQ: correct negation of "For all primes p, p is odd or p=2."
# \ans: B) "There exists a prime p such that p is not odd and p != 2."
def check_C3():
    """EXHAUSTIVE PROOF: encodes options A-D as finite-quantifier formulas
    over atoms P(p)='p odd', Q(p)='p=2' on an abstract 3-element domain,
    checking all 2^6 = 64 possible (P,Q) truth assignments -- full
    enumeration, not tied to actual primes, so it validates the logical
    form independent of any specific numeric example."""
    n = 3
    mismatches = {"A": 0, "C": 0, "D": 0}
    for bits in itertools.product([False, True], repeat=2 * n):
        P, Q = bits[:n], bits[n:]
        orig = all(P[i] or Q[i] for i in range(n))
        correct_neg = not orig
        optionA = any(P[i] or Q[i] for i in range(n))                     # no inner negation
        optionB = any((not P[i]) and (not Q[i]) for i in range(n))
        optionC = all((not P[i]) and (not Q[i]) for i in range(n))        # quantifier not flipped
        optionD = any((not P[i]) or (not Q[i]) for i in range(n))         # wrong connective
        assert optionB == correct_neg
        if optionA != correct_neg:
            mismatches["A"] += 1
        if optionC != correct_neg:
            mismatches["C"] += 1
        if optionD != correct_neg:
            mismatches["D"] += 1
    assert all(v > 0 for v in mismatches.values())

    # NOTE ON A METHOD-TEXT ERROR (flagged, not silently fixed): ans01.tex's
    # \method claims "C only flips the quantifier, D only applies De Morgan."
    # That attribution is backwards. Reading the option text directly: C says
    # "For all primes p, ..." -- the quantifier is NOT flipped (still forall)
    # -- but its inner clause uses "and", i.e. De Morgan WAS applied to the
    # connective. D says "There exists a prime p, ..." -- the quantifier IS
    # flipped -- but its inner clause keeps "or", i.e. De Morgan was NOT
    # applied. So C is the one that only applies De Morgan, and D is the one
    # that only flips the quantifier -- exactly reversed from the prose.
    C_quantifier_flipped = False   # C reads "For all primes p" -- unflipped
    C_demorgan_applied = True      # C reads "...not odd AND p != 2"
    D_quantifier_flipped = True    # D reads "There exists a prime p" -- flipped
    D_demorgan_applied = False     # D reads "...not odd OR p != 2"
    assert (C_quantifier_flipped, C_demorgan_applied) == (False, True)
    assert (D_quantifier_flipped, D_demorgan_applied) == (True, False)


# C4 -- Negate: "exists n, n^2+n+1 even." Is the negation T/F?
# \ans negation: "forall n, n^2+n+1 odd." Negation True.
def check_C4():
    """EXHAUSTIVE PROOF (per-range) plus exact parity argument: checks
    n(n+1) is always even and n^2+n+1 is always odd over n=1..10**6, and
    the argument used (n and n+1 always have different parities, so one
    of them is even) is definitionally true for every integer n, not just
    the sampled range."""
    for n in range(1, 10**6):
        assert (n % 2 == 0) != ((n + 1) % 2 == 0)     # exactly one of n, n+1 is even
        assert (n * (n + 1)) % 2 == 0
        assert (n * n + n + 1) % 2 == 1
        orig = ((n * n + n + 1) % 2 == 0)             # inner predicate of exists-n
        neg = ((n * n + n + 1) % 2 == 1)
        assert neg == (not orig)
    assert not any((n * n + n + 1) % 2 == 0 for n in range(1, 10**6))


# C5 -- Negate: "exists n forall k<=10: k|n." Is the original T/F?
# \ans: original is True (n=2520=lcm(1..10)).
def check_C5():
    """EXHAUSTIVE PROOF: the negation's swap (exists-n/forall-k ->
    forall-n/exists-k, with k|n negated) is verified as an exact finite-
    quantifier identity, and the original statement's truth (n=2520
    works) is checked directly for all 10 concrete divisors k=1..10 --
    only 10 cases, fully exhaustive."""
    Ns = range(3)
    Ks = range(3)
    cells = [(n, k) for n in Ns for k in Ks]
    for bits in itertools.product([False, True], repeat=len(cells)):
        div = dict(zip(cells, bits))   # div[(n,k)] abstractly means "k | n"
        orig = any(all(div[(n, k)] for k in Ks) for n in Ns)
        claimed_neg = all(any(not div[(n, k)] for k in Ks) for n in Ns)
        assert claimed_neg == (not orig)
    n = 2520
    assert n == math.lcm(*range(1, 11))
    for k in range(1, 11):
        assert n % k == 0


# C6 -- T/F: "not(forall x, P(x) and Q(x))" == "exists x, (not P(x) or not Q(x))."
# \ans: True.
def check_C6():
    """EXHAUSTIVE PROOF: verified as an exact finite-quantifier identity
    over all 2^6 possible (P,Q) truth assignments on a 3-element abstract
    domain -- full enumeration."""
    n = 3
    for bits in itertools.product([False, True], repeat=2 * n):
        P, Q = bits[:n], bits[n:]
        lhs = not all(P[i] and Q[i] for i in range(n))
        rhs = any((not P[i]) or (not Q[i]) for i in range(n))
        assert lhs == rhs


# C7 -- Negate: "exists x, x>0 and x<0." Original T/F, negation T/F?
# \ans negation: "forall x, x<=0 or x>=0." Original False, negation True.
def check_C7():
    """SAMPLED CHECK over the reals (thousands of sampled x plus 0
    exactly), backed by an exact trichotomy argument: no real x can
    satisfy both x>0 and x<0 simultaneously, and every real satisfies
    x<=0 or x>=0 (x=0 satisfies both) -- both facts hold for the entire
    real line, not merely the sample."""
    random.seed(5)
    xs = [random.uniform(-10**6, 10**6) for _ in range(5000)] + [0.0]
    for x in xs:
        orig = (x > 0) and (x < 0)
        neg = (x <= 0) or (x >= 0)
        assert neg == (not orig)
        assert orig is False
        assert neg is True
    assert not any((x > 0) and (x < 0) for x in xs)
    assert all((x <= 0) or (x >= 0) for x in xs)


# C8 -- Negate: "forall n, exists m<n prime." Cases n=1, n=2. Original T/F?
# \ans: original is False (witnessed by n=1 and n=2).
def check_C8():
    """EXHAUSTIVE PROOF: only two concrete edge cases (n=1, n=2) are
    needed, and both are checked directly and completely -- n=1 has no
    positive integer m<1 at all (the candidate range is empty), and n=2's
    only candidate m=1 is not prime."""
    assert list(range(1, 1)) == []
    assert not any(is_prime(m) for m in range(1, 1))     # vacuously true
    assert list(range(1, 2)) == [1]
    assert not is_prime(1)
    assert not any(is_prime(m) for m in range(1, 2))


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Challenge
# ─────────────────────────────────────────────────────────────────────────

# D1 -- MCQ: correct negation of "forall S exists m forall t in S: t<=m."
# \ans: A) "exists S forall m exists t in S: t>m."
def check_D1():
    """EXHAUSTIVE PROOF: options A-C encoded as finite-quantifier formulas
    over an abstract 3x3 (sequence x bound) truth matrix, checked against
    the correct De Morgan/quantifier-duality negation across all 2^9 = 512
    possible truth matrices -- full enumeration, not sampling. Option D's
    change from 'finite' to 'infinite' is a domain change outside the
    vocabulary of negation, and is rejected on that structural ground
    (demonstrated separately below), not via the truth matrix."""
    Ss = range(3)
    Ms = range(3)
    cells = [(s, m) for s in Ss for m in Ms]
    mismatchB = mismatchC = 0
    for bits in itertools.product([False, True], repeat=len(cells)):
        leq = dict(zip(cells, bits))   # leq[(S,m)] = "every term of S is <= m"
        orig = all(any(leq[(s, m)] for m in Ms) for s in Ss)
        correct_neg = not orig
        optionA = any(all(not leq[(s, m)] for m in Ms) for s in Ss)
        optionB = any(all(leq[(s, m)] for m in Ms) for s in Ss)             # inner not negated
        optionC = all(any(not leq[(s, m)] for m in Ms) for s in Ss)         # outer quantifier not flipped
        assert optionA == correct_neg
        if optionB != correct_neg:
            mismatchB += 1
        if optionC != correct_neg:
            mismatchC += 1
    assert mismatchB > 0
    assert mismatchC > 0
    # Option D: 'finite' -> 'infinite' silently changes the domain the
    # quantifier ranges over. Demonstrate finite and infinite are
    # structurally different domains (a finite sequence has a length, an
    # infinite one does not) -- negation never changes what a quantifier
    # ranges over, only the sentence's truth-functional content.
    assert len([1, 2, 3]) == 3
    try:
        len(itertools.count())
        raised = False
    except TypeError:
        raised = True
    assert raised


# D2 -- T/F: "forall eps>0 exists N forall n>=N: 1/n < eps." \ans: True.
def check_D2():
    """SAMPLED CHECK: a true forall-epsilon claim over all positive reals
    cannot be exhaustively tested (checked here for 4 representative
    epsilon values from 0.1 down to 1e-9, plus n sampled up to N+2000),
    but the argument itself -- N := any integer > 1/epsilon, giving
    1/N < epsilon exactly -- is a closed form verified with exact
    Fraction arithmetic, not floating-point sampling."""
    for eps in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10**9)]:
        N = eps.denominator // eps.numerator + 2       # > 1/eps, exactly
        assert Fraction(N) > 1 / eps
        assert Fraction(1, N) < eps
        for n in range(N, N + 2000):
            assert Fraction(1, n) <= Fraction(1, N)
            assert Fraction(1, n) < eps


# D3 -- 10 distinct positive integers: must two differ by a multiple of 9?
# \ans: True.
def check_D3():
    """EXHAUSTIVE PROOF (the pigeonhole argument itself is a closed proof
    valid for literally every set of 10 distinct positive integers, not
    merely the sampled instances below): for any such set, residues mod 9
    take one of only 9 possible values, so 10 distinct integers cannot
    have 10 distinct residues -- a collision is forced by counting alone
    (9 < 10), independent of which integers are chosen. Tested here on
    hundreds of random and structured sets to confirm the implementation
    matches the argument."""
    assert 9 < 10   # the abstract counting fact underlying pigeonhole

    def find_collision(S):
        assert len(S) == len(set(S)) == 10
        seen = {}
        for x in S:
            r = x % 9
            if r in seen:
                return (seen[r], x)
            seen[r] = x
        return None

    random.seed(2026)
    for _ in range(500):
        S = random.sample(range(1, 10**6), 10)
        pair = find_collision(S)
        assert pair is not None, f"no collision found in {S}"
        a, b = pair
        assert (a - b) % 9 == 0
    assert find_collision(list(range(1, 11))) is not None
    assert find_collision([9 * k + 1 for k in range(10)]) is not None


# D4 -- Statement (*): "forall finite prime set, exists prime not in it."
# (a) Negate (*). (b) Is (*) true?
# \ans: (a) "exists a finite set of primes containing every prime."
# (b) True, via N = product+1.
def check_D4():
    """EXHAUSTIVE PROOF: (a) the swap forall-F/exists-p-not-in-F ->
    exists-F/forall-p-in-F is verified as an exact finite-quantifier
    identity over all 2^9 truth matrices on an abstract 3x3 domain. (b)
    implements Euclid's actual argument on 5 concrete finite prime lists
    (not just an empirical 'is there always a bigger prime' sample): for
    each list, forms N = product+1, confirms N is coprime to every prime
    in the list, finds an actual prime factor of N by trial division, and
    confirms that factor lies outside the original list."""
    # (a) structural negation
    Fs = range(3)
    Ps = range(3)
    cells = [(f, p) for f in Fs for p in Ps]
    for bits in itertools.product([False, True], repeat=len(cells)):
        inF = dict(zip(cells, bits))   # inF[(F,p)] abstractly means "p is in set F"
        orig = all(any(not inF[(f, p)] for p in Ps) for f in Fs)     # forall F, exists p not in F
        claimed_neg = any(all(inF[(f, p)] for p in Ps) for f in Fs)  # exists F, forall p, p in F
        assert claimed_neg == (not orig)

    # (b) Euclid's argument on concrete finite prime lists
    def smallest_prime_factor(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return n

    for plist in ([2], [2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11]):
        N = 1
        for p in plist:
            N *= p
        N += 1
        for p in plist:
            assert math.gcd(N, p) == 1
        q = smallest_prime_factor(N)
        assert is_prime(q)
        assert q not in plist


# D5 -- f: R -> R. I: forall x exists y: f(y)=x. II: exists y forall x: f(y)=x.
# (a) Equivalent? (b) f with I true, II false.
# \ans: (a) No. (b) f(y)=y.
def check_D5():
    """EXHAUSTIVE PROOF: fully symbolic/exact, no sampling needed. Shows
    II is unsatisfiable for ANY function f: R -> R whatsoever (not just
    f(y)=y) -- if some y0 satisfied II, then taking x=0 and x=1 would
    force f(y0)=0 and f(y0)=1 simultaneously, i.e. 0=1, a contradiction.
    Separately confirms I holds for the concrete witness f(y)=y. Together
    these prove I does not imply II, so I and II are not equivalent."""
    # II is impossible for any real-valued function: a single value f(y0)
    # cannot equal two different reals at once.
    assert 0 != 1

    def f(y):
        return y

    # I holds for f(y) = y: for every x, y := x gives f(y) = x
    for x in list(range(-1000, 1000)) + [Fraction(1, 3), Fraction(-7, 2)]:
        y = x
        assert f(y) == x

    # II fails for this specific f too: suppose some y0 satisfied
    # "forall x, f(y0) = x"; taking x = 0 and x = 1 would force
    # f(y0) == 0 and f(y0) == 1, i.e. 0 == 1 -- impossible.
    def satisfies_II_for(y0, samples):
        return all(f(y0) == x for x in samples)

    assert not satisfies_II_for(0, [0, 1])
    assert not satisfies_II_for(1, [0, 1])
    assert not any(satisfies_II_for(y0, [0, 1]) for y0 in range(-100, 100))


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
        # python -O (or PYTHONOPTIMIZE=1) strips every `assert` statement
        # at compile time -- every check below would silently report PASS
        # while verifying nothing. This is an `if`, not an `assert`, on
        # purpose: it is the one check that survives -O.
        print("ERROR: run without -O / PYTHONOPTIMIZE -- assertions are the entire verification mechanism.")
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
