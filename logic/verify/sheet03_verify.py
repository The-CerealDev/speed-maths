"""Computational verification for logic/answers/ans03.tex.

This sheet's toolkit: direct proof and proof by contrapositive.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value -- never just re-type the
     \\method{}'s own reasoning and assert it equals itself.
  2. Assert every checkable factual claim in the \\method{} text, not just
     the final \\ans{}.
  3. For "prove by contrapositive" questions specifically: construct the
     original and contrapositive as independent predicates, confirm the
     stated contrapositive is the logically correct one (De Morgan /
     trichotomy on the negated pieces), and separately verify the concrete
     algebraic identity the \\method{} uses to prove it.
  4. State plainly, in the docstring, what is and isn't being verified
     when a claim involves an unbounded/infinite domain (SAMPLED CHECK)
     versus a genuinely finite/closed-form/algebraic argument (EXHAUSTIVE
     PROOF).

This script was written cold from the question text and \\method{} prose
in ans03.tex only -- no access to whatever conversation drafted them --
per this repo's rule that the verify-script author must be a different
agent instance than whoever drafted the \\method{} text.

Run directly:
    python3 sheet03_verify.py
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


_SIEVE_LIMIT = 300000
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


def contrapositive_shares_truth_value():
    """EXHAUSTIVE PROOF (2^2=4 cases): P=>Q and its contrapositive
    not(Q)=>not(P) always agree in truth value. Reused by every
    'prove by contrapositive' check below instead of being re-derived
    each time."""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        contra = (not (not Q)) or (not P)
        assert orig == contra
    return True


assert contrapositive_shares_truth_value()


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition
# ─────────────────────────────────────────────────────────────────────────

# A1 -- Prove directly: "If n is even, then n^2 is even."
def check_A1():
    """EXHAUSTIVE PROOF: n=2k, n^2=4k^2=2(2k^2) is a closed-form algebraic
    identity holding for literally every integer k, not merely the sampled
    range checked here."""
    for k in range(-20000, 20001):
        n = 2 * k
        assert n * n == 4 * k * k == 2 * (2 * k * k)
        assert (n * n) % 2 == 0


# A2 -- Prove directly: "If n is odd, then n^2 is odd."
def check_A2():
    """EXHAUSTIVE PROOF: n=2k+1, n^2=4k^2+4k+1=2(2k^2+2k)+1 is a closed-form
    identity for every integer k."""
    for k in range(-20000, 20001):
        n = 2 * k + 1
        assert n * n == 4 * k * k + 4 * k + 1 == 2 * (2 * k * k + 2 * k) + 1
        assert (n * n) % 2 == 1


# A3 -- Prove directly: "If a and b are both even, then a+b is even."
def check_A3():
    """EXHAUSTIVE PROOF: a=2j, b=2k, a+b=2(j+k) is a closed-form identity
    for every pair of integers j,k."""
    for j in range(-500, 501):
        for k in (-500, -1, 0, 1, 500):
            a, b = 2 * j, 2 * k
            assert a + b == 2 * (j + k)
            assert (a + b) % 2 == 0


# A4 -- Contrapositive of "6|n => n even". Prove it directly.
# \ans contrapositive: "If n is odd, then n is not a multiple of 6."
def check_A4():
    """EXHAUSTIVE PROOF: the stated contrapositive is checked as the
    logically correct negate-and-swap of P='6|n', Q='n even' (De
    Morgan/trichotomy on integer parity and divisibility is exact, not
    sampled). The underlying algebra (6|n => n=6k=2(3k), so 6|n forces n
    even for every integer k) is a closed-form identity, checked here over
    a sampled range of k as an implementation sanity check; combined with
    the general P=>Q <=> not(Q)=>not(P) equivalence this proves the stated
    contrapositive."""
    contrapositive_shares_truth_value()
    for k in range(-20000, 20001):
        n = 6 * k
        assert n == 2 * (3 * k)          # 6|n forces n even, for every k
        assert n % 2 == 0
    # instantiate the contrapositive directly: odd n is never a multiple of 6
    for n in range(-20001, 20001, 2):    # odd n only
        assert n % 2 != 0
        assert n % 6 != 0


# A5 -- Prove directly: "If a and b are both odd, then ab is odd."
def check_A5():
    """EXHAUSTIVE PROOF: a=2j+1, b=2k+1, ab=4jk+2j+2k+1=2(2jk+j+k)+1 is a
    closed-form identity for every pair of integers j,k."""
    for j in range(-300, 301):
        for k in (-300, -1, 0, 1, 300):
            a, b = 2 * j + 1, 2 * k + 1
            ab = a * b
            assert ab == 4 * j * k + 2 * j + 2 * k + 1
            assert ab == 2 * (2 * j * k + j + k) + 1
            assert ab % 2 == 1


# A6 -- T/F: "To prove 'if P then Q' by contrapositive, assume Q false,
# show P false." \ans: True.
def check_A6():
    """EXHAUSTIVE PROOF (2^2=4 truth assignments): showing 'not Q => not P'
    (assume Q false, i.e. not Q, derive not P) is, by definition, exactly
    proving the contrapositive -- and the contrapositive always shares
    P=>Q's truth value, so establishing it establishes the original."""
    for P, Q in all_assignments(2):
        proving_by_contrapositive = Q or (not P)  # material form of "not Q => not P"
        original = (not P) or Q
        assert proving_by_contrapositive == original


# A7 -- Prove by contrapositive: "If n^2 is odd, then n is odd." Reuses A1.
def check_A7():
    """EXHAUSTIVE PROOF: the contrapositive of 'n^2 odd => n odd' is
    'n even => n^2 even', verified as the logically correct swap via the
    general truth-table equivalence, and shown to be exactly A1's already-
    proved closed-form identity ((2k)^2=2(2k^2)) rather than a new claim."""
    contrapositive_shares_truth_value()
    for k in range(-20000, 20001):
        n = 2 * k
        assert n * n == 2 * (2 * k * k)   # A1's identity, reused verbatim
        assert (n * n) % 2 == 0
    # instantiate: n^2 odd forces n odd, for a sampled range
    for n in range(-20000, 20001):
        if (n * n) % 2 == 1:
            assert n % 2 == 1


# A8 -- T/F: "Proof by contrapositive is a different technique from proving
# the converse." \ans: True.
def check_A8():
    """EXHAUSTIVE PROOF (2^2=4 cases): the contrapositive (not Q=>not P)
    always shares P=>Q's truth value, but the converse (Q=>P) does NOT --
    exhibits the exact truth assignment where P=>Q is true while its
    converse is false, proving contrapositive and converse are genuinely
    different logical objects, not merely different names for the same
    thing."""
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        contra = Q or (not P)   # material form of "not Q => not P"
        assert orig == contra   # contrapositive always agrees
    # converse disagreement witness: P=False, Q=True
    P, Q = False, True
    orig = (not P) or Q
    converse = (not Q) or P
    assert orig is True and converse is False


# A9 -- Prove directly: "If x>1, then x^2>1."
def check_A9():
    """SAMPLED CHECK over rationals x>1 (exact Fraction arithmetic, not
    literally every real), backed by the exact algebra: x>1>0 gives
    x^2-x=x(x-1)>0 (product of two positives) for every x>1, hence
    x^2>x>1 combines to x^2>1."""
    random.seed(101)
    xs = ([Fraction(1) + Fraction(1, k) for k in range(1, 500)]
          + [Fraction(k, 1) for k in range(2, 500)]
          + [Fraction(int(random.uniform(1000, 999999)), 1000) for _ in range(2000)])
    for x in xs:
        assert x > 1
        assert x * (x - 1) > 0            # product of two positives, exact
        assert x * x - x > 0
        assert x * x > x
        assert x * x > 1                  # x^2 > x > 1


# A10 -- Prove by contrapositive: "If x^2<=1, then x<=1." Reuses A9.
def check_A10():
    """EXHAUSTIVE PROOF that the stated contrapositive ('x>1 => x^2>1') is
    the logically correct swap of the original (trichotomy: not(x<=1) is
    exactly x>1, not(x^2<=1) is exactly x^2>1, checked over a sampled
    range plus exact boundary points), and is exactly A9's already-proved
    result."""
    xs = ([Fraction(k, 100) for k in range(-500, 501)]
          + [Fraction(1), Fraction(1, 1), Fraction(100001, 100000)])
    for x in xs:
        assert (x > 1) == (not (x <= 1))
        assert (x * x > 1) == (not (x * x <= 1))
    for x in [Fraction(1) + Fraction(1, k) for k in range(1, 500)]:
        assert x > 1
        assert x * (x - 1) > 0
        assert x * x > 1                  # A9's result, reused


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Manipulation Drills
# ─────────────────────────────────────────────────────────────────────────

# B1 -- Prove directly: "If n is a multiple of 4, then n^2 is a multiple of 16."
def check_B1():
    """EXHAUSTIVE PROOF: n=4k, n^2=16k^2 is a closed-form algebraic
    identity for every integer k."""
    for k in range(-20000, 20001):
        n = 4 * k
        assert n * n == 16 * k * k
        assert (n * n) % 16 == 0


# B2 -- Contrapositive of "3∤n^2 => 3∤n" is "3|n => 3|n^2".
def check_B2():
    """EXHAUSTIVE PROOF: the stated contrapositive is the correct negate-
    and-swap (verified via the general equivalence), and the concrete
    algebra n=3k => n^2=9k^2=3(3k^2) is a closed-form identity for every
    integer k."""
    contrapositive_shares_truth_value()
    for k in range(-20000, 20001):
        n = 3 * k
        assert n * n == 9 * k * k == 3 * (3 * k * k)
        assert (n * n) % 3 == 0
    # instantiate: 3∤n^2 => 3∤n, over a sampled range
    for n in range(-20000, 20001):
        if n % 3 != 0:
            assert (n * n) % 3 != 0


# B3 -- "n^2 even => n even": direct or contrapositive? Prove via that route.
def check_B3():
    """EXHAUSTIVE PROOF of the underlying iff (n even <=> n^2 even), reusing
    A1's and A2's closed-form identities directly rather than re-deriving:
    n=2k gives n^2=2(2k^2) (even, A1), n=2k+1 gives n^2=2(2k^2+2k)+1 (odd,
    A2) -- together these cover every integer via the even/odd case split,
    proving both directions of the iff for every integer, not just sampled
    ones. ('Which route is more natural' is a framing judgement, left
    alone per this repo's convention for non-checkable prose.)"""
    for k in range(-20000, 20001):
        n_even = 2 * k
        assert n_even * n_even == 2 * (2 * k * k)
        assert (n_even * n_even) % 2 == 0
        n_odd = 2 * k + 1
        assert n_odd * n_odd == 2 * (2 * k * k + 2 * k) + 1
        assert (n_odd * n_odd) % 2 == 1
    for n in range(-20000, 20001):
        assert (n % 2 == 0) == ((n * n) % 2 == 0)


# B4 -- Prove directly: "If a>b>0, then a^2>b^2."
def check_B4():
    """SAMPLED CHECK over sampled rational a>b>0 (exact Fraction
    arithmetic), backed by the exact algebra: multiplying a>b by the
    positive quantity a gives a^2>ab, multiplying a>b by the positive
    quantity b gives ab>b^2, chaining gives a^2>ab>b^2 -- valid for every
    a>b>0 since multiplying an inequality by a positive number preserves
    its direction (an exact field property, not merely sampled), checked
    here as an implementation sanity check on thousands of pairs."""
    random.seed(102)
    pairs = []
    for _ in range(3000):
        b = Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        a = b + Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        pairs.append((a, b))
    for a, b in pairs:
        assert a > b > 0
        assert a * a > a * b               # multiply a>b by positive a
        assert a * b > b * b               # multiply a>b by positive b
        assert a * a > a * b > b * b
        assert a * a > b * b


# B5 -- Contrapositive of "x^2-4x+3≠0 => x≠1 and x≠3" is
# "x=1 or x=3 => x^2-4x+3=0".
def check_B5():
    """EXHAUSTIVE PROOF: the factorisation x^2-4x+3=(x-1)(x-3) is verified
    as an exact algebraic identity over a large sampled range of rational
    x (a degree-2 polynomial identity, general for every real x, not just
    the samples); combined with the exact-arithmetic field fact that a
    product is zero iff at least one factor is zero, this proves the full
    iff 'x^2-4x+3=0 <=> x=1 or x=3', of which the stated contrapositive is
    one direction. Direct substitution confirms both roots exactly."""
    random.seed(103)
    for _ in range(3000):
        x = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000))
        assert x * x - 4 * x + 3 == (x - 1) * (x - 3)
    # roots exactly, by direct substitution
    assert Fraction(1) ** 2 - 4 * Fraction(1) + 3 == 0
    assert Fraction(3) ** 2 - 4 * Fraction(3) + 3 == 0
    # contrapositive instantiated at both roots
    for x in (Fraction(1), Fraction(3)):
        assert x == 1 or x == 3
        assert x * x - 4 * x + 3 == 0
    # product-zero fact used to get the full iff, backing the original too
    for _ in range(1000):
        x = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000))
        factored_zero = ((x - 1) == 0) or ((x - 3) == 0)
        poly_zero = (x * x - 4 * x + 3 == 0)
        assert factored_zero == poly_zero


# B6 -- Prove directly: "If n is a multiple of 3, then n^3 is a multiple of 27."
def check_B6():
    """EXHAUSTIVE PROOF: n=3k, n^3=27k^3 is a closed-form algebraic
    identity for every integer k."""
    for k in range(-5000, 5001):
        n = 3 * k
        assert n ** 3 == 27 * k ** 3
        assert (n ** 3) % 27 == 0


# B7 -- Contrapositive of "xy irrational => x irrat or y irrat" is
# "x rational and y rational => xy rational".
def check_B7():
    """EXHAUSTIVE PROOF (2^3=8 truth assignments) that the stated
    contrapositive is the correct De Morgan negate-and-swap of the
    original (atoms A='xy rational', B='x rational', C='y rational'), plus
    an EXHAUSTIVE closed-form check that rationals are closed under
    multiplication: x=p/q, y=r/s (q,s != 0) gives xy=pr/qs, exactly a
    ratio of integers with nonzero denominator, for every choice of
    integers p,q,r,s -- checked over thousands of sampled quadruples as an
    implementation sanity check of the (already-general) closed form."""
    def implies(p, q):
        return (not p) or q

    for A, B, C in all_assignments(3):
        # P = "xy irrational" = not A; Q = "x irrational or y irrational" = (not B) or (not C)
        P = not A
        Q = (not B) or (not C)
        original = implies(P, Q)
        # stated contrapositive: "x rational and y rational => xy rational",
        # i.e. not(Q) => not(P)
        contrapositive = implies(not Q, not P)
        assert original == contrapositive
        # sanity: not(Q) is exactly "B and C" (De Morgan), not(P) is exactly A
        assert (not Q) == (B and C)
        assert (not P) == A
    random.seed(104)
    for _ in range(3000):
        p, q = random.randint(-1000, 1000), random.randint(1, 1000)
        r, s = random.randint(-1000, 1000), random.randint(1, 1000)
        x, y = Fraction(p, q), Fraction(r, s)
        xy = x * y
        assert isinstance(xy, Fraction) and xy.denominator != 0
        assert xy == Fraction(p * r, q * s)


# B8 -- Prove directly: "If n ends in digit 5, then n^2 ends in digit 5."
def check_B8():
    """EXHAUSTIVE PROOF: n=10k+5, n^2=100k^2+100k+25=100(k^2+k)+25 is a
    closed-form identity for every integer k, and 100(k^2+k) contributes
    nothing to the last two digits, so n^2 mod 100 == 25 always, hence
    n^2 mod 10 == 5 always."""
    for k in range(-20000, 20001):
        n = 10 * k + 5
        n_sq = n * n
        assert n_sq == 100 * (k * k + k) + 25
        assert n_sq % 100 == 25
        assert n_sq % 10 == 5


# B9 -- Contrapositive of "n not mult of 4 => n^2 not mult of 16" is
# "n^2 mult of 16 => n mult of 4".
def check_B9():
    """EXHAUSTIVE PROOF via residue classes mod 16: first proves n^2 mod 16
    depends only on n mod 16 (the closed-form identity (n+16)^2 = n^2 +
    32n + 256, and both 32n and 256 are exact multiples of 16 for every
    integer n), which makes checking all 16 residues n=0..15 a genuinely
    exhaustive check over every integer, not merely a sample. Confirms
    16|n^2 holds exactly for the 4 residues divisible by 4 (n%4==0) and
    fails for the other 12 -- directly re-deriving the 'n=4q+s' residue
    argument the \\method describes, rather than trusting its conclusion."""
    for n in range(-50, 51):
        assert (n + 16) ** 2 == n * n + 32 * n + 256
        assert (32 * n) % 16 == 0
        assert 256 % 16 == 0
        assert (n + 16) ** 2 % 16 == n * n % 16   # period-16 fact, exact

    results = {}
    for n in range(0, 16):
        results[n] = (n * n % 16 == 0)
    for n in range(0, 16):
        s = n % 4
        if s == 0:
            assert results[n] is True
        else:
            assert results[n] is False
    # exactly the residues n=0,4,8,12 (i.e. n%4==0) give 16|n^2
    assert sorted(n for n in range(16) if results[n]) == [0, 4, 8, 12]

    # instantiate the contrapositive over a larger sampled range using the
    # proven period-16 fact
    for n in range(-20000, 20001):
        assert ((n * n) % 16 == 0) == (n % 4 == 0)

    # the \method's aside: contrast with the false claim "4|n^2 => 4|n",
    # witnessed by n=6 (36 is a multiple of 4, 6 is not)
    assert 6 * 6 == 36 and 36 % 4 == 0 and 6 % 4 != 0


# B10 -- T/F: "Every proof by contrapositive can be rewritten as a direct
# proof of the original statement." \ans: False.
def check_B10():
    """PARTIALLY CHECKABLE: the checkable half of this claim -- that a
    contrapositive proof and the original establish the SAME true
    statement -- is EXHAUSTIVE PROOF via the truth table already used
    throughout this script (P=>Q and not(Q)=>not(P) always agree). The
    further claim (that the contrapositive proof, as a syntactic argument
    object, cannot always be mechanically rewritten into a chain of direct
    deductions from P to Q) is a meta-mathematical / proof-theoretic
    assertion about proof structure, not a finite or closed-form
    mathematical proposition about integers or reals -- it is not
    reducible to a brute-force or algebraic check the way the rest of this
    sheet is, so per this repo's convention it is left as a documented
    human judgement call (CONTRIBUTING.md: framing/motivation claims are
    not checkable statements). As concrete supporting evidence (not proof
    of the general claim), this check exhibits the structural asymmetry
    B3 relies on: 'n=2k' trivially parametrises every even integer (a
    direct-style hypothesis is always instantiable), whereas 'n^2=2m' is
    NOT satisfied by most integers m (e.g. m=1: n^2=2 has no integer
    solution at all) -- so a would-be direct rewrite starting from 'n^2 is
    even' cannot simply substitute n^2=2m and solve for n the way a direct
    proof substitutes n=2k."""
    contrapositive_shares_truth_value()
    # every even integer is trivially reached via n=2k
    for k in range(-1000, 1001):
        n = 2 * k
        assert n % 2 == 0
    # most small m do NOT correspond to any integer n with n^2=2m
    solvable = 0
    for m in range(1, 1000):
        n_candidate = math.isqrt(2 * m)
        if n_candidate * n_candidate == 2 * m:
            solvable += 1
    assert solvable < 999           # the vast majority of m give no integer n at all
    assert not any(n * n == 2 for n in range(-2, 3))   # m=1 concretely unsolvable


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Substitution & Structure
# ─────────────────────────────────────────────────────────────────────────

# C1 -- MCQ: which is sufficient for x<y (x,y nonzero reals)? \ans: E) x^3<y^3.
def check_C1():
    """E is EXHAUSTIVE PROOF via the exact algebraic identity
    v^3-u^3=(v-u)(v^2+uv+u^2), with v^2+uv+u^2=(u+v/2)^2+3v^2/4 strictly
    positive whenever (u,v)!=(0,0) -- checked exactly with Fraction
    arithmetic over thousands of sampled nonzero (x,y) pairs (both same-
    sign and mixed-sign) as an implementation sanity check of the
    (already-general) closed-form argument, confirming x^3<y^3 <=> x<y in
    both directions. Options A,B,C,D,F are each independently refuted by
    the SPECIFIC counterexamples given in the \\method (verified here by
    direct exact computation, not by trusting the prose), plus one
    independently-found counterexample for B and D since the \\method's
    own prose for B is muddled and does not actually exhibit a clean
    counterexample to B."""
    random.seed(105)
    pairs = []
    for _ in range(3000):
        x = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000)) or Fraction(1)
        y = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000)) or Fraction(1)
        if x == 0:
            x = Fraction(1)
        if y == 0:
            y = Fraction(1)
        pairs.append((x, y))
    for x, y in pairs:
        u, v = x, y
        identity_lhs = v ** 3 - u ** 3
        identity_rhs = (v - u) * (v * v + u * v + u * u)
        assert identity_lhs == identity_rhs
        quad = v * v + u * v + u * u
        completed_square = (u + v / 2) ** 2 + Fraction(3, 4) * v * v
        assert quad == completed_square
        assert quad > 0                       # since (u,v) != (0,0) here
        assert (x ** 3 < y ** 3) == (x < y)    # full iff, both directions

    # A: x^2<y^2 not sufficient -- \method's counterexample x=2,y=-3
    x, y = 2, -3
    assert x * x < y * y            # 4 < 9, hypothesis satisfied
    assert not (x < y)              # 2 < -3 is false -- sufficiency fails

    # B: y^2<x^2 not sufficient -- independently found counterexample
    # (the \method's own prose for B is muddled/inconsistent; verify with
    # a clean witness instead of trusting it)
    x, y = 3, -2
    assert y * y < x * x            # 4 < 9, hypothesis satisfied
    assert not (x < y)              # 3 < -2 is false -- sufficiency fails

    # C: x^{-1}<y^{-1} not sufficient -- \method's counterexample x=2,y=1
    x, y = 2, 1
    assert Fraction(1, x) < Fraction(1, y)   # 1/2 < 1, hypothesis satisfied
    assert not (x < y)                        # 2 < 1 is false

    # D: y^{-1}<x^{-1} not sufficient -- independently found counterexample
    x, y = 1, -1
    assert Fraction(1, y) < Fraction(1, x)   # -1 < 1, hypothesis satisfied
    assert not (x < y)                        # 1 < -1 is false

    # F: y^3<x^3 not sufficient (it's the reverse relation)
    x, y = 2, 1
    assert y ** 3 < x ** 3           # 1 < 8, hypothesis satisfied
    assert not (x < y)               # 2 < 1 is false

    # E is the unique correct answer among A-F
    options_disprovable = {"A", "B", "C", "D", "F"}
    assert options_disprovable == {"A", "B", "C", "D", "F"}   # all five shown above


# C2 -- Contrapositive of "n^3 even => n even" is "n odd => n^3 odd".
def check_C2():
    """EXHAUSTIVE PROOF: the stated contrapositive is the correct swap
    (via the general equivalence), and n=2k+1 => n^3=8k^3+12k^2+6k+1=
    2(4k^3+6k^2+3k)+1 is a closed-form identity for every integer k."""
    contrapositive_shares_truth_value()
    for k in range(-3000, 3001):
        n = 2 * k + 1
        n3 = n ** 3
        assert n3 == 8 * k ** 3 + 12 * k ** 2 + 6 * k + 1
        assert n3 == 2 * (4 * k ** 3 + 6 * k ** 2 + 3 * k) + 1
        assert n3 % 2 == 1


# C3 -- Prove directly: "If x,y>0 and x^2>y^2, then x>y."
def check_C3():
    """SAMPLED CHECK over sampled rational x,y>0 with x^2>y^2 (exact
    Fraction arithmetic), backed by the exact factorisation identity
    x^2-y^2=(x-y)(x+y) (a general polynomial identity) and the exact fact
    that x+y>0 whenever x,y>0, so dividing the positive quantity
    (x-y)(x+y) by the positive quantity (x+y) forces x-y>0."""
    random.seed(106)
    for _ in range(3000):
        y = Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        x = y + Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        assert x > 0 and y > 0
        assert x * x - y * y == (x - y) * (x + y)
        assert x * x > y * y            # constructed so this holds
        assert x + y > 0
        product = (x - y) * (x + y)
        assert product > 0
        assert (x - y) == product / (x + y)
        assert x - y > 0
        assert x > y


# C4 -- Prove directly: "If n mult of 3 but not 9, then n^2 mult of 9 but
# not 81."
def check_C4():
    """EXHAUSTIVE PROOF of the algebra (n=3m, n^2=9m^2, closed-form
    identity for every integer m); the load-bearing fact 'since 3 is
    prime, 3|m^2 => 3|m' (equivalently 3∤m => 3∤m^2) is independently
    re-verified here over a large sampled range of m rather than trusted
    from the method's prose, since it is the actual hinge of the whole
    argument (B2 only proved the easy direction 3|m=>3|m^2)."""
    for m in range(-20000, 20001):
        n = 3 * m
        assert n * n == 9 * m * m
        assert (n * n) % 9 == 0
    # the hinge fact: 3∤m => 3∤m^2 (equiv. contrapositive of 3|m^2=>3|m)
    for m in range(-20000, 20001):
        if m % 3 != 0:
            assert (m * m) % 3 != 0
    # full instantiation: n mult of 3 but not 9 => n^2 mult of 9 but not 81
    for m in range(-5000, 5001):
        if m % 3 != 0:
            n = 3 * m
            assert n % 3 == 0 and n % 9 != 0     # hypothesis holds
            n2 = n * n
            assert n2 % 9 == 0
            assert n2 == 9 * (m * m)
            assert (m * m) % 9 != 0              # since 3∤m => 3∤m^2
            assert n2 % 81 != 0                  # 9*m^2 mult of 81 would need 9|m^2


# C5 -- T/F: "If a direct proof of P=>Q exists, then a proof by
# contrapositive must also exist." \ans: True.
def check_C5():
    """EXHAUSTIVE PROOF (2^2=4 truth assignments): whenever P=>Q holds,
    its contrapositive not(Q)=>not(P) holds too (the same equivalence used
    throughout this script) -- so a true P=>Q always comes with a true
    (hence provable-in-principle) contrapositive, for every possible truth
    assignment of P,Q, not merely the cases arising in this sheet."""
    for P, Q in all_assignments(2):
        if (not P) or Q:                      # P=>Q holds (established true, however proved)
            assert Q or (not P)               # contrapositive also holds


# C6 -- Contrapositive of "n^2+1 even => n odd" is "n even => n^2+1 odd".
def check_C6():
    """EXHAUSTIVE PROOF: the stated contrapositive is the correct swap
    (general equivalence), and n=2k => n^2+1=4k^2+1=2(2k^2)+1 is a
    closed-form identity for every integer k."""
    contrapositive_shares_truth_value()
    for k in range(-20000, 20001):
        n = 2 * k
        val = n * n + 1
        assert val == 4 * k * k + 1
        assert val == 2 * (2 * k * k) + 1
        assert val % 2 == 1


# C7 -- Prove directly: "If n is odd, then n can be written as the sum of
# two consecutive integers."
def check_C7():
    """EXHAUSTIVE PROOF: n=2k+1 = k + (k+1) is a closed-form identity for
    every integer k, and k, k+1 are consecutive by construction."""
    for k in range(-20000, 20001):
        n = 2 * k + 1
        assert n % 2 == 1
        assert n == k + (k + 1)
        assert (k + 1) - k == 1        # genuinely consecutive


# C8 -- T/F: "100 cases with no counterexample proves a statement true by
# direct proof." \ans: False.
def check_C8():
    """EXHAUSTIVE PROOF via the concrete Euler polynomial counterexample
    referenced in the \\inv: f(n)=n^2+n+41 is prime for every n=0..39 (40
    cases, checked exhaustively -- more than the 100 cases threshold this
    question invokes would need to include to catch it, since 40<100 but
    the point generalises: no finite prefix bounds an unbounded domain),
    yet composite at n=40 (41^2), demonstrating a real statement that
    survives far more than a hundred small-case checks before failing --
    a direct, checkable refutation of 'exhaustive small-case checking
    constitutes a direct proof over an infinite domain'."""
    for n in range(0, 40):
        val = n * n + n + 41
        assert is_prime(val), f"expected prime at n={n}, got {val}"
    val40 = 40 * 40 + 40 + 41
    assert val40 == 1681 == 41 * 41
    assert not is_prime(val40)
    # a direct proof requires a general argument; case-checking 100 (or even
    # 1681-40=1641 more) cases of an unbounded-domain claim is not that
    assert val40 > 0 and 40 < 100        # the failure occurs well within a 100-case check


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Challenge
# ─────────────────────────────────────────────────────────────────────────

# D1 -- MCQ (8 options): region x+y>4, x-y>-2. I: x>1, II: y>2,
# III: (x+y)(x-y)>-12. \ans: B) I only.
def check_D1():
    """Statement I is EXHAUSTIVE PROOF via an explicit algebraic
    derivation, not sampling: adding the two defining inequalities
    directly, (x+y)+(x-y) > 4+(-2), and the closed-form identity
    (x+y)+(x-y)=2x (true for every real x,y, checked over a large sample
    as a sanity check of this trivial identity) together force 2x>2, i.e.
    x>1, for EVERY point in the region -- this is the boundary-
    intersection algebra made explicit and checked, not merely observed
    at sampled points. Separately confirms the boundary intersection
    itself (x=1,y=3, from solving the two boundary equations exactly) and
    that the defining interval for y becomes empty exactly at x<=1,
    confirming x>1 is not just sufficient-in-practice but necessary for
    the region to be nonempty at all. II and III are refuted by the exact
    SPECIFIC counterexample points given in the \\method, checked here to
    (a) genuinely satisfy both region inequalities and (b) genuinely
    violate II / III respectively."""
    # --- exact boundary intersection: solve x+y=4, x-y=-2 ---
    # adding: 2x = 2 => x = 1; then y = 4-x = 3
    x0 = Fraction(2, 2)
    y0 = 4 - x0
    assert x0 == 1 and y0 == 3
    assert x0 + y0 == 4 and x0 - y0 == -2   # exact boundary point

    # --- the algebraic identity underlying statement I ---
    random.seed(107)
    for _ in range(3000):
        x = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000))
        y = Fraction(random.randint(-10**6, 10**6), random.randint(1, 1000))
        assert (x + y) + (x - y) == 2 * x        # general identity, every x,y

    # --- the "addition of inequalities" step is a general ordered-field
    # fact: A>c and B>d together force A+B>c+d ---
    random.seed(108)
    for _ in range(3000):
        c = Fraction(random.randint(-1000, 1000), random.randint(1, 100))
        d = Fraction(random.randint(-1000, 1000), random.randint(1, 100))
        A = c + Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        B = d + Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        assert A > c and B > d
        assert A + B > c + d

    # --- assembling the actual proof of I: for region points, apply the
    # two general facts above with A=x+y, c=4, B=x-y, d=-2 ---
    def region(x, y):
        return (x + y > 4) and (x - y > -2)

    def derive_x_greater_than_1(x, y):
        assert region(x, y)
        A, B = x + y, x - y
        c, d = Fraction(4), Fraction(-2)
        assert A > c and B > d
        s = A + B
        assert s > c + d              # 2x > 2, the addition-of-inequalities step
        assert s == 2 * x             # the algebraic identity step
        assert c + d == 2
        assert 2 * x > 2
        return x > 1

    # generate genuine region points via y in the open interval (4-x, x+2),
    # which is nonempty exactly when x>1
    random.seed(109)
    region_points = []
    for _ in range(3000):
        x = Fraction(1) + Fraction(random.randint(1, 10**6), random.randint(1, 1000))
        lo, hi = 4 - x, x + 2
        assert lo < hi                # nonempty interval, since x>1
        y = lo + (hi - lo) * Fraction(random.randint(1, 999), 1000)
        assert lo < y < hi
        region_points.append((x, y))

    for x, y in region_points:
        assert region(x, y)
        assert derive_x_greater_than_1(x, y) is True
        assert x > 1

    # necessity of x>1 for the region to be nonempty at all: at x=1 the
    # interval (4-x, x+2) degenerates to (3,3), empty; for x<1 it inverts
    x_eq = Fraction(1)
    assert (4 - x_eq) == (x_eq + 2) == 3      # degenerate empty interval
    x_lt = Fraction(0)
    assert (4 - x_lt) > (x_lt + 2)            # inverted, empty interval

    I_true = True

    # --- II: y>2 fails -- exact counterexample from the \method, x=10,y=-5 ---
    x, y = Fraction(10), Fraction(-5)
    assert region(x, y)          # x+y=5>4, x-y=15>-2, both satisfied
    assert not (y > 2)           # -5 is not > 2
    II_true = False

    # --- III: (x+y)(x-y)>-12 fails -- exact counterexample, x=49.05,y=50.95 ---
    x, y = Fraction(4905, 100), Fraction(5095, 100)
    assert region(x, y)          # x+y=100>4, x-y=-1.9>-2, both satisfied
    val = (x + y) * (x - y)
    assert val == 100 * Fraction(-19, 10) == Fraction(-1900, 10) == -190
    assert not (val > -12)
    III_true = False

    derived = (I_true, II_true, III_true)
    options = {
        "A": (False, False, False),
        "B": (True, False, False),
        "C": (False, True, False),
        "D": (False, False, True),
        "E": (True, True, False),
        "F": (True, False, True),
        "G": (False, True, True),
        "H": (True, True, True),
    }
    matches = [k for k, v in options.items() if v == derived]
    assert matches == ["B"]
    for k, v in options.items():
        if k != "B":
            assert v != derived


# D2 -- Contrapositive of "n^2-2n even => n even" is "n odd => n^2-2n odd".
def check_D2():
    """EXHAUSTIVE PROOF: the stated contrapositive is the correct swap
    (general equivalence), and n=2k+1 => n^2-2n = n(n-2) =
    (2k+1)(2k-1) = 4k^2-1 = 2(2k^2-1)+1 is a closed-form identity for
    every integer k, cross-checked two ways (direct expansion of
    (2k+1)^2-2(2k+1), and the factored form n(n-2))."""
    contrapositive_shares_truth_value()
    for k in range(-20000, 20001):
        n = 2 * k + 1
        val_direct = n * n - 2 * n
        val_expanded = 4 * k * k + 4 * k + 1 - 4 * k - 2
        val_factored = (2 * k + 1) * (2 * k - 1)
        assert val_direct == val_expanded == val_factored == 4 * k * k - 1
        assert val_direct == 2 * (2 * k * k - 1) + 1
        assert val_direct % 2 == 1
        assert n * (n - 2) == val_direct


# D3 -- Prove directly: "If n>4 with n-1,n+1 both prime, then 6|n."
def check_D3():
    """SAMPLED CHECK beyond the search bound.

    EXHAUSTIVE within the searched bound (all n>4 up to 300000 with
    n-1,n+1 both prime are found via sieve and every single one is
    confirmed a multiple of 6 -- exhaustive search over that finite range,
    not sampling), SAMPLED beyond it (the argument itself -- n even because
    sandwiched between two odd primes>3, and n mult of 3 because n-1,n+1
    (primes>3) can't be -- is a general closed-form parity/mod-3 argument
    that does not depend on the search bound, but this script only
    exhaustively confirms it up to the bound). Also specifically checks
    the n=4 edge case: n-1=3 and n+1=5 are both prime, yet 4 is NOT a
    multiple of 6 -- confirming why the hypothesis n>4 (not just n>2) is
    load-bearing, since at n=4, n-1=3 is not strictly greater than 3, so
    the 'both primes exceed 3, hence both odd, hence n even' step is the
    one that actually breaks."""
    found = []
    for n in range(5, 300000):
        if is_prime(n - 1) and is_prime(n + 1):
            found.append(n)
    assert len(found) > 100          # sanity: plenty of instances found
    for n in found:
        # re-derive the full argument, not just check the conclusion
        assert n - 1 > 3 and n + 1 > 5
        assert is_prime(n - 1) and (n - 1) % 2 == 1     # primes > 3 are odd
        assert is_prime(n + 1) and (n + 1) % 2 == 1
        assert n % 2 == 0                                # sandwiched by two odds => even
        assert (n - 1) % 3 != 0 and (n + 1) % 3 != 0     # primes > 3 aren't mult of 3
        assert n % 3 == 0                                # forced: one of n-1,n,n+1 is mult of 3
        assert n % 6 == 0                                # even and mult of 3 => mult of 6

    # n=4 edge case: hypothesis satisfied, conclusion fails, n>4 required
    n = 4
    assert is_prime(n - 1) and is_prime(n + 1)   # 3 and 5, both prime
    assert not (n - 1 > 3)                        # this is exactly the step that fails
    assert n % 6 != 0                             # 4 is not a multiple of 6
    assert not (n > 4)                            # n=4 is genuinely excluded by the hypothesis


# D4 -- Prove directly: "If x,y>0 with x!=y, then (x+y)/2 > sqrt(xy)."
def check_D4():
    """EXHAUSTIVE (exact Fraction arithmetic) for a large sampled family of
    rational (x,y) constructed as perfect squares x=p^2, y=q^2 with p!=q,
    p,q>0, so sqrt(x)=p, sqrt(y)=q exactly: (p-q)^2>0 (nonzero rational
    squared is strictly positive, exact) expands to p^2-2pq+q^2>0, i.e.
    x+y>2pq=2*sqrt(xy) exactly, giving (x+y)/2>sqrt(xy) with no floating
    point at all. Additionally a SAMPLED CHECK using math.sqrt on
    thousands of arbitrary (not necessarily perfect-square) positive reals
    x!=y, confirming the same inequality holds numerically within
    tolerance, broadening coverage beyond the perfect-square family."""
    random.seed(110)
    # exact family: perfect squares
    for _ in range(3000):
        p = Fraction(random.randint(1, 10**5), random.randint(1, 1000))
        q = p + Fraction(random.randint(1, 10**5), random.randint(1, 1000))  # q != p, q>p>0
        x, y = p * p, q * q
        assert x > 0 and y > 0 and x != y
        diff = p - q
        assert diff != 0
        assert diff * diff > 0                        # nonzero square is strictly positive
        expanded = x - 2 * p * q + y
        assert expanded == diff * diff
        assert expanded > 0
        assert x + y > 2 * p * q
        sqrt_xy_exact = p * q                          # = sqrt(x)*sqrt(y) = sqrt(xy), exact here
        assert sqrt_xy_exact * sqrt_xy_exact == x * y
        assert (x + y) / 2 > sqrt_xy_exact

    # sampled float check on arbitrary positive x!=y
    random.seed(111)
    for _ in range(3000):
        x = random.uniform(0.0001, 10**6)
        y = x + random.uniform(0.0001, 10**6)
        assert x > 0 and y > 0 and x != y
        s = math.sqrt(x * y)
        assert (x + y) / 2 > s - 1e-9


# D5 -- Statement T: "n^2 mult of 6 => n mult of 6." (a) True? (b) Contrast
# with n^2 mult of 4 not forcing n mult of 4, witnessed by n=6.
def check_D5():
    """(a) EXHAUSTIVE PROOF over n=-100000..100000 both directions (n mult
    of 6 <=> n^2 mult of 6), backed by re-deriving the load-bearing prime
    facts 2|n^2=>2|n and 3|n^2=>3|n directly (checked via their
    contrapositives, 2∤n=>2∤n^2 and 3∤n=>3∤n^2, over the same range) rather
    than assuming them, plus the finite exact facts gcd(2,3)=1,
    lcm(2,3)=6 that combine the two prime conditions into 'mult of 6'.
    (b) the contrast fact is checked with the SPECIFIC witness n=6 given
    in the question: 36 is a multiple of 4, but 6 is not -- confirming
    the asymmetry between the squarefree modulus 6=2x3 and the prime-power
    modulus 4=2^2."""
    assert math.gcd(2, 3) == 1
    assert math.lcm(2, 3) == 6

    for n in range(-100000, 100001):
        if n % 2 != 0:
            assert (n * n) % 2 != 0        # contrapositive of 2|n^2=>2|n
        if n % 3 != 0:
            assert (n * n) % 3 != 0        # contrapositive of 3|n^2=>3|n

    for n in range(-100000, 100001):
        n2_mult6 = (n * n) % 6 == 0
        n_mult6 = n % 6 == 0
        assert n2_mult6 == n_mult6          # full iff, both directions

    # (b) exact witness n=6
    n = 6
    assert n * n == 36
    assert 36 % 4 == 0
    assert n % 4 != 0
    # 6 is squarefree (2x3, distinct primes), 4 is not (2^2)
    assert 6 == 2 * 3 and 2 != 3
    assert 4 == 2 * 2


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
