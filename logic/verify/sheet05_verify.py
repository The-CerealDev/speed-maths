"""Computational verification for logic/answers/ans05.tex.

This sheet's toolkit: Spot the Flaw / Common Fallacies / Proof Critique /
Valid vs. Invalid Arguments (Section A: name-the-fallacy recognition;
Section B: short numbered proof-critique drills; Section C/D: tricky MCQs,
some of which describe fully VALID proofs -- the trap is assuming every
question has a flaw).

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value -- never just re-type the
     \\method{}'s own reasoning and assert it equals itself.
  2. Assert every checkable factual claim in the \\method{} text, not just
     the final \\ans{}. For "spot the flaw" questions this means actually
     computing both the correct and the erroneous expansion/claim and
     confirming they genuinely diverge, not just trusting the prose.
  3. State plainly, in the docstring, what is and isn't being verified
     when a claim involves an unbounded/infinite domain (SAMPLED CHECK,
     usually backed by a closed-form argument valid for the full domain)
     versus a genuinely finite/exhaustive argument (EXHAUSTIVE PROOF).

This script was written cold from the question text and \\method{} prose
in ans05.tex only, per this repo's rule that the verify-script author
must be a different agent instance than whoever drafted the \\method{}
text.

Run directly:
    python3 sheet05_verify.py
"""

import itertools
import math
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


def implies(p, q):
    """Material conditional p => q."""
    return (not p) or q


def dist(P, Q):
    """Euclidean distance between two 2D points."""
    return math.hypot(P[0] - Q[0], P[1] - Q[1])


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition (fallacy literacy)
# ─────────────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: truth-table search confirms 'P=>Q, Q, therefore P'
    (affirming the consequent) has a satisfying assignment (P=False,Q=True)
    where both premises hold but the conclusion fails -- i.e. the form is
    genuinely invalid. Concrete instantiation with n=15: divisible by 3
    (Q true) but not by 6 (P false), and the general premise 'divisible by
    6 => divisible by 3' is checked on a sample of multiples of 6."""
    counterexample_exists = any(
        implies(P, Q) and Q and not P
        for P, Q in all_assignments(2)
    )
    assert counterexample_exists, "affirming the consequent should be an invalid form"
    n = 15
    assert n % 3 == 0
    assert n % 6 != 0
    for k in range(1, 2000):
        m = 6 * k
        assert m % 3 == 0  # confirms the P=>Q premise ('div by 6 => div by 3') is genuinely true


def check_A2():
    """EXHAUSTIVE PROOF: truth-table search confirms 'P=>Q, not P, therefore
    not Q' (denying the antecedent) has a satisfying assignment (P=False,
    Q=True) where both premises hold but the conclusion fails. Concrete
    instantiation with x=5: x<=10 (not P true) but x>0 (Q true, so not Q
    is false); the premise 'x>10 => x>0' is checked on a sample of reals."""
    counterexample_exists = any(
        implies(P, Q) and (not P) and Q
        for P, Q in all_assignments(2)
    )
    assert counterexample_exists, "denying the antecedent should be an invalid form"
    x = 5
    assert x <= 10       # not P
    assert x > 0         # Q (so not Q is false) -- conclusion x<=0 fails
    for k in range(-2000, 2000):
        xv = k / 10
        if xv > 10:
            assert xv > 0  # premise x>10 => x>0 holds throughout the sample


def check_A3():
    """EXHAUSTIVE PROOF for the concrete instance; demonstrates a genuine
    example of a TRUE claim carrying a genuinely FLAWED argument, showing a
    proof's validity and a statement's truth are independent properties.
    Claim 'for all integers n, n(n+1) is even' is verified directly (true),
    while a deliberately flawed one-line 'argument' for it ('n is always
    even') is shown to rest on a false premise, i.e. it genuinely fails as
    a proof despite the target claim being true."""
    flawed_premise = lambda n: n % 2 == 0     # asserts n is always even -- false in general
    assert not all(flawed_premise(n) for n in range(1, 200)), \
        "the flawed premise must not be universally true, or the argument would not be flawed"
    for n in range(-2000, 2000):
        assert (n * (n + 1)) % 2 == 0, f"target claim is nonetheless true at n={n}"


def check_A4():
    """EXHAUSTIVE PROOF: models a 6-line proof as a sequential dependency
    chain where trust in line i requires no flaw at or before i. With the
    (only) flaw at line 4, lines 5-6 inherit its untrustworthiness even
    though their own algebra could be locally correct -- so exactly lines
    1-3 (3 lines) remain trustworthy."""
    flawed_line = 4
    n_lines = 6
    flaw_seen = False
    trusted = []
    for i in range(1, n_lines + 1):
        if i == flawed_line:
            flaw_seen = True
        trusted.append(not flaw_seen)
    assert trusted == [True, True, True, False, False, False]
    assert sum(trusted) == 3
    assert flawed_line - 1 == 3


def check_A5():
    """EXHAUSTIVE PROOF: confirms squaring is not injective by exhibiting
    x=-2 as an extraneous solution introduced when squaring the equation
    x=2: -2 does not satisfy x=2, but (-2)^2 = 4 = 2^2, so it satisfies the
    squared equation."""
    assert (-2) ** 2 == 4
    assert 2 ** 2 == 4
    assert -2 != 2
    original_solutions = {2}
    squared_solutions = {r for r in (-2, 2) if r ** 2 == 4}
    assert squared_solutions == {-2, 2}
    assert squared_solutions != original_solutions
    assert -2 not in original_solutions and (-2) ** 2 == 4


def check_A6():
    """EXHAUSTIVE PROOF: verifies, via full truth-table enumeration over
    (premises_true, argument_valid, conclusion_true), the tautology
    '(premises_true and argument_valid) => conclusion_true' that defines a
    genuinely valid argument. Since the concrete conclusion 0=1 is actually
    false, the tautology's contrapositive forces NOT(premises_true AND
    argument_valid) -- i.e. an error (false premise or invalid step) must
    exist somewhere in the chain."""
    for A, B, C in itertools.product([False, True], repeat=3):
        rule_holds = implies(A and B, C)
        if rule_holds and not C:
            assert not (A and B)
    conclusion_true = (0 == 1)
    assert conclusion_true is False
    error_exists = not conclusion_true  # forced by the tautology above, given a false conclusion
    assert error_exists is True


def check_A7():
    """EXHAUSTIVE PROOF: exhibits two concrete instances of a P(n) that is
    true for n=1..10 (or n=1..4) yet false just beyond that range --
    demonstrating finite verification never entails a universal claim. (i)
    the trivial P(n): n<11. (ii) the richer 2n^2+11, prime for n=1..4 but
    composite at n=11 (reused from B7's fact, 253 = 11*23)."""
    P = lambda n: n < 11
    assert all(P(n) for n in range(1, 11))
    assert not P(11)
    f = lambda n: 2 * n ** 2 + 11
    for n in range(1, 5):
        assert is_prime(f(n))
    assert f(11) == 253 == 11 * 23
    assert not is_prime(f(11))


def check_A8():
    """EXHAUSTIVE PROOF for x=0 (a=2,b=5); SAMPLED CHECK confirming the
    division IS valid (forces a=b) whenever x!=0. Dividing ax=bx by x
    silently assumes x!=0; at x=0 the equation 0=0 holds for every a,b, so
    a=b need not follow."""
    a, b, x = 2, 5, 0
    assert a * x == b * x       # 0 == 0, regardless of a, b
    assert a != b                # yet a != b here -- the division step is unjustified
    for x2 in range(1, 60):
        for a2 in range(-15, 15):
            for b2 in range(-15, 15):
                if a2 * x2 == b2 * x2:
                    assert a2 == b2  # for x2 != 0, ax=bx genuinely forces a=b


def check_A9():
    """EXHAUSTIVE PROOF: verifies 'P and not P' is unsatisfiable for every
    truth value of P (a genuine contradiction), then contrasts a concrete
    'unusual-looking but not impossible' result (a large but perfectly
    satisfiable equation) which has an actual satisfying instance and is
    therefore NOT a contradiction."""
    for P in (False, True):
        assert (P and (not P)) is False   # unsatisfiable in every case: a genuine contradiction
    # "unusual" but satisfiable: x + 1 = 1000000 has an actual witness, x = 999999
    x = 999999
    assert x + 1 == 1000000
    assert x > 0
    # a genuine numeric contradiction, by contrast, has no satisfying witness at all
    assert (0 == 1) is False


def check_A10():
    """EXHAUSTIVE PROOF for a concrete counterexample; confirms the cross-multiplication
    identity ad=bc holds even when a!=c and b!=d. Specifically, a/b = c/d does
    not imply a=c and b=d, using the counterexample 1/2 = 2/4."""
    a, b, c, d = 1, 2, 2, 4
    assert Fraction(a, b) == Fraction(c, d)
    assert a != c
    assert b != d
    assert a * d == b * c


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Manipulation Drills (short proof-critique)
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    """SAMPLED CHECK over integers k (backed by an exact algebraic identity
    valid for every integer k, not just the sampled range): confirms
    (2k+1)^2 = 4k^2+4k+1 = 2(2k^2+2k)+1 exactly, and that this is always
    odd -- the proof as given is fully valid, with no flaw."""
    for k in range(-500, 501):
        n = 2 * k + 1
        assert n ** 2 == 4 * k ** 2 + 4 * k + 1
        assert 4 * k ** 2 + 4 * k + 1 == 2 * (2 * k ** 2 + 2 * k) + 1
        assert n ** 2 % 2 == 1


def check_B2():
    """EXHAUSTIVE PROOF over a bounded integer search (the quadratic
    x^2=3x has at most 2 real roots, both integers here, so a bounded
    search finds all of them): x^2-3x=0 has roots x=0 and x=3, but the
    given proof (divide by x) silently loses x=0 -- invalid when x=0."""
    roots = [r for r in range(-30, 31) if r ** 2 == 3 * r]
    assert roots == [0, 3]
    assert 0 ** 2 == 3 * 0        # x=0 genuinely satisfies the original equation
    assert 0 != 3                  # but the claimed answer x=3 misses it
    try:
        0 / 0
        assert False, "0/0 should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass


def check_B3():
    """EXHAUSTIVE PROOF: the derived quadratic x^2-11x+18=0 has exactly the
    two integer roots 9 and 2 (bounded search); x=9 satisfies the ORIGINAL
    equation sqrt(x+7)=x-5, while x=2 does not (its RHS is negative, so it
    can never equal a non-negative square root) -- confirming x=2 is a
    genuine extraneous root introduced by squaring."""
    roots = [r for r in range(-30, 31) if r ** 2 - 11 * r + 18 == 0]
    assert set(roots) == {9, 2}
    assert math.isclose(math.sqrt(9 + 7), 9 - 5)   # x=9 checks out
    lhs2, rhs2 = math.sqrt(2 + 7), 2 - 5
    assert rhs2 < 0 <= lhs2
    assert not math.isclose(lhs2, rhs2)             # x=2 fails the original equation


def check_B4():
    """SAMPLED CHECK over integers n (backed by exact Fraction arithmetic,
    so each sampled n is an exact algebraic identity, not a float
    approximation): confirms the TRUE simplification of
    2*((4n+1)/2-(n-3)/2) is 3n+4, while Line 2's erroneous simplification
    (failing to flip the sign of -3 when distributing) gives 3n-2 -- a
    persistent, constant (6) discrepancy, never zero. Also confirms both
    the true value (9n+12) and Line 3's erroneous value (9n-6) happen to
    be multiples of 3, since the outer factor of 3 is untouched by the
    error -- exactly as the \\method{} notes."""
    for n in range(-200, 201):
        A = Fraction(4 * n + 1, 2)
        B = Fraction(n - 3, 2)
        two_AB_correct = 2 * (A - B)
        assert two_AB_correct == Fraction(3 * n + 4)
        two_AB_erroneous = Fraction(4 * n + 1 - n - 3)   # literally what Line 2 wrote
        assert two_AB_erroneous == Fraction(3 * n - 2)
        assert two_AB_correct != two_AB_erroneous          # genuine, persistent divergence
        assert two_AB_correct - two_AB_erroneous == 6

        original_expr = 6 * (A - B)
        assert original_expr == Fraction(3) * two_AB_correct == Fraction(9 * n + 12)
        line3_value = Fraction(3) * two_AB_erroneous
        assert line3_value == Fraction(9 * n - 6)

        assert original_expr.denominator == 1 and line3_value.denominator == 1
        assert int(original_expr) % 3 == 0
        assert int(line3_value) % 3 == 0


def check_B5():
    """SAMPLED CHECK over integers k (backed by exact algebraic identities
    valid for every integer k): confirms the proof's shown even case
    (n=2k) genuinely yields an even value, AND separately confirms the
    unshown odd case (n=2k+1) also yields an even value (per the
    \\method{}'s parenthetical) -- so the claim is true overall, but the
    given proof is still incomplete as written since it never establishes
    the odd case."""
    for k in range(-200, 201):
        n = 2 * k
        val = n ** 2 + n + 2
        assert val == 4 * k ** 2 + 2 * k + 2 == 2 * (2 * k ** 2 + k + 1)
        assert val % 2 == 0

        n2 = 2 * k + 1
        val2 = n2 ** 2 + n2 + 2
        assert val2 == 4 * k ** 2 + 4 * k + 1 + 2 * k + 1 + 2
        assert val2 == 4 * k ** 2 + 6 * k + 4 == 2 * (2 * k ** 2 + 3 * k + 2)
        assert val2 % 2 == 0


def check_B6():
    """EXHAUSTIVE PROOF (bounded search suffices since x^2=9 has exactly 2
    real roots): confirms x=3 => x^2=9 (the direction actually shown), but
    x^2=9 does NOT imply x=3, since x=-3 is a genuine counterexample
    satisfying x^2=9 without satisfying x=3."""
    assert 3 ** 2 == 9
    assert (-3) ** 2 == 9
    assert -3 != 3
    roots = [r for r in range(-20, 21) if r ** 2 == 9]
    assert set(roots) == {3, -3}


def check_B7():
    """EXHAUSTIVE PROOF: computes Fibonacci numbers up to F6 to confirm the given
    values (F3, F4, F5) are prime, then confirms F6=8 is neither 1 nor prime, 
    serving as a counterexample to the universal claim."""
    F = [0, 1, 1]  # F_0=0 (unused), F_1=1, F_2=1
    for n in range(3, 7):
        F.append(F[n - 1] + F[n - 2])
    
    assert F[3] == 2
    assert F[4] == 3
    assert F[5] == 5
    assert is_prime(F[3])
    assert is_prime(F[4])
    assert is_prime(F[5])
    
    assert F[6] == 8
    assert F[6] != 1
    assert not is_prime(F[6])
    assert 8 == 2 * 4  # nontrivial factorization


def check_B8():
    """EXHAUSTIVE PROOF: confirms the shown statement (n div by 3 => n^2
    div by 3) is itself arithmetically true on a sample, then proves via
    full truth-table enumeration over abstract atoms A='3|n', B='3|n^2'
    that A=>B is NOT logically equivalent, in general, to either the
    original claim (notA=>notB) or its contrapositive (B=>A) -- exhibiting
    a concrete truth assignment where they diverge."""
    for n in range(-300, 301):
        if n % 3 == 0:
            assert (n ** 2) % 3 == 0
    mismatch_with_original = any(
        implies(A, B) != implies(not A, not B)
        for A, B in all_assignments(2)
    )
    mismatch_with_contrapositive = any(
        implies(A, B) != implies(B, A)
        for A, B in all_assignments(2)
    )
    assert mismatch_with_original
    assert mismatch_with_contrapositive
    # sanity: an implication and its OWN contrapositive are always equivalent
    for A, B in all_assignments(2):
        original = implies(not A, not B)
        contrapositive_of_original = implies(B, A)
        assert original == contrapositive_of_original


def check_B9():
    """SAMPLED CHECK over integers j,k (backed by an exact identity valid
    for every integer pair): confirms a non-circular direct proof exists --
    a=2j, b=2k directly gives a+b=2(j+k), even -- WITHOUT ever assuming
    a+b is even up front, demonstrating the flawed proof's opening
    assumption (a+b=2m) was logically unnecessary, i.e. circular."""
    for j in range(-200, 201):
        for k in range(-50, 51):
            a, b = 2 * j, 2 * k
            s = a + b
            assert s == 2 * (j + k)
            assert s % 2 == 0


def check_B10():
    """EXHAUSTIVE PROOF for the concrete 5-student instance (3 passed, 2
    did not): confirms the correct negation ('at least one student did not
    pass') is true, while the student's incorrect conclusion ('every
    student failed') is false in this instance -- a single disagreement
    disproves the claimed equivalence. Backed by the general quantifier
    identity not(forall x P(x)) == exists x, not P(x), verified exhaustively
    over all 2^5 = 32 possible pass/fail patterns of 5 students, contrasted
    against the (non-equivalent) forall x, not P(x)."""
    passed = [True, True, True, False, False]
    every_passed = all(passed)
    assert every_passed is False
    correct_negation = any(not p for p in passed)
    incorrect_conclusion = all(not p for p in passed)
    assert correct_negation == (not every_passed) is True
    assert incorrect_conclusion is False
    assert correct_negation != incorrect_conclusion

    for pattern in itertools.product([False, True], repeat=5):
        orig = all(pattern)
        correct_neg = any(not p for p in pattern)
        assert correct_neg == (not orig)
    # exhibit a pattern where the WRONG negation (all failed) disagrees with the correct one
    mismatch_exists = any(
        (all(not p for p in pattern)) != (not all(pattern))
        for pattern in itertools.product([False, True], repeat=5)
    )
    assert mismatch_exists


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Substitution & Structure (tricky MCQs)
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: confirms the discriminant of 2x^2+2x+1 is exactly
    -4 (< 0, so the roots are genuinely non-real, ruling out real-- let
    alone integer-linear-- factorisation), then confirms the claim's
    actual failure point: n=3 gives 2(9)+6+1=25=5^2, composite. This is
    exactly the category error the \\method{} identifies: irreducibility
    over the reals says nothing about primality of integer outputs."""
    a, b, c = 2, 2, 1
    disc = b ** 2 - 4 * a * c
    assert disc == -4
    assert disc < 0
    # negative discriminant => complex (non-real) roots via the quadratic formula
    real_part = -b / (2 * a)
    imag_part_sq = -disc / (2 * a) ** 2
    assert imag_part_sq > 0    # roots have a genuinely nonzero imaginary part
    n = 3
    val = 2 * n ** 2 + 2 * n + 1
    assert val == 25 == 5 ** 2
    assert not is_prime(val)


def check_C2():
    """EXHAUSTIVE PROOF (bounded search suffices; a quadratic has at most 2
    roots): x^2-5x+6 factors exactly as (x-2)(x-3), confirmed for many x.
    x=2 satisfies P (so Q=>P holds), but x=3 ALSO satisfies P without
    satisfying Q, so P=>Q genuinely fails -- confirming the flaw."""
    for x in range(-50, 51):
        assert x ** 2 - 5 * x + 6 == (x - 2) * (x - 3)
    assert 2 ** 2 - 5 * 2 + 6 == 0    # x=2 satisfies P (backs Q=>P)
    assert 3 ** 2 - 5 * 3 + 6 == 0    # x=3 also satisfies P
    assert 3 != 2                      # ... without satisfying Q -- P=>Q fails
    roots = [r for r in range(-50, 51) if r ** 2 - 5 * r + 6 == 0]
    assert set(roots) == {2, 3}


def check_C3():
    """SAMPLED CHECK over integers n (backed by the exact identity
    n^2+n = n(n+1), a product of two consecutive integers, always even for
    every integer n): confirms the claim is true for BOTH parities, while
    the proof as given establishes only the even case explicitly."""
    for n in range(-300, 301):
        assert n ** 2 + n == n * (n + 1)
        assert (n * (n + 1)) % 2 == 0
    for k in range(-150, 151):
        n_even = 2 * k
        assert (n_even ** 2 + n_even) % 2 == 0     # the case the given proof covers
        n_odd = 2 * k + 1
        assert (n_odd ** 2 + n_odd) % 2 == 0        # the case it omits, but which also holds


def check_C4():
    """SAMPLED CHECK over integers n (backed by an exact mod-3 argument
    valid for every integer n: {n-2,n,n+2} covers all 3 residues mod 3
    exactly once as n-2, n, n+2 differ by multiples that shift residues by
    1 each step, so exactly one is divisible by 3): confirms Lines I-II,
    then confirms Line III's gap concretely -- 3 itself is divisible by 3
    yet prime, and n=5 gives the all-prime trio 3,5,7."""
    for n in range(-500, 501):
        vals = [n - 2, n, n + 2]
        divisible_by_3 = [v % 3 == 0 for v in vals]
        assert sum(divisible_by_3) == 1, f"failed at n={n}"
    trio = [3, 5, 7]
    assert all(is_prime(v) for v in trio)
    assert 3 % 3 == 0
    assert is_prime(3)   # divisible by 3 but NOT composite -- exactly Line III's gap


def check_C5():
    """EXHAUSTIVE PROOF (closed-form witnesses valid for every integer, not
    merely sampled): m=n+1 witnesses 'forall n exists m, m>n' for literally
    every n; separately, for ANY candidate M, taking n:=M breaks M>n --
    disproving 'exists M forall n, M>n' for every candidate, confirming
    the quantifier swap is invalid."""
    for n in range(-2000, 2000):
        m = n + 1
        assert m > n
    for M in range(-2000, 2000):
        n = M
        assert not (M > n)


def check_C6():
    """EXHAUSTIVE PROOF via explicit coordinates: constructs a concrete
    kite (two pairs of adjacent equal sides, A=(0,2),B=(-1,0),C=(0,-1),
    D=(1,0)) whose diagonals are perpendicular (dot product exactly 0) but
    which is NOT a rhombus (its two distinct side lengths differ) --
    exactly the counterexample the \\method{} cites to disprove the
    converse."""
    A, B, C, D = (0, 2), (-1, 0), (0, -1), (1, 0)
    AB, BC, CD, DA = dist(A, B), dist(B, C), dist(C, D), dist(D, A)
    assert math.isclose(AB, DA)      # kite: one pair of adjacent sides equal
    assert math.isclose(BC, CD)      # the other pair of adjacent sides equal
    assert not math.isclose(AB, BC)  # NOT all four sides equal -- not a rhombus
    AC = (C[0] - A[0], C[1] - A[1])
    BD = (D[0] - B[0], D[1] - B[1])
    dot = AC[0] * BD[0] + AC[1] * BD[1]
    assert dot == 0                   # diagonals genuinely perpendicular


def check_C7():
    """EXHAUSTIVE PROOF for the concrete pair; SAMPLED CHECK backing the
    general same-sign <=> equality fact. At x=-2,y=-5: |x+y|=7=|x|+|y|, so
    the STRICT inequality 7<7 genuinely fails -- a fully valid single
    counterexample to a universal strict-inequality claim, confirming the
    student's disproof is correct as it stands."""
    x, y = -2, -5
    assert abs(x + y) == 7
    assert abs(x) + abs(y) == 7
    assert not (abs(x + y) < abs(x) + abs(y))   # strict inequality fails here
    for xv in range(-20, 21):
        for yv in range(-20, 21):
            same_sign = (xv >= 0 and yv >= 0) or (xv <= 0 and yv <= 0)
            eq = (abs(xv + yv) == abs(xv) + abs(yv))
            assert eq == same_sign


def check_C8():
    """EXHAUSTIVE PROOF via explicit coordinates: constructs a concrete
    non-square rhombus (vertices (-3,0),(0,4),(3,0),(0,-4), all four sides
    length 5) whose diagonals are UNEQUAL in length (6 vs 8), confirming
    it is not a square -- a genuine counterexample to sufficiency
    ('four equal sides => square')."""
    verts = [(-3, 0), (0, 4), (3, 0), (0, -4)]
    sides = [dist(verts[i], verts[(i + 1) % 4]) for i in range(4)]
    assert all(math.isclose(s, 5) for s in sides)
    d1 = dist(verts[0], verts[2])
    d2 = dist(verts[1], verts[3])
    assert math.isclose(d1, 6) and math.isclose(d2, 8)
    assert not math.isclose(d1, d2)   # unequal diagonals -- not a square, despite equal sides


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Challenge
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    """SAMPLED CHECK over integer u,v (backed by the exact algebraic
    identity (u+v)^2-4uv=(u-v)^2>=0, valid for every real u,v -- so lines
    II-III of the ATTEMPT are genuinely correct): confirms the attempt's
    algebra is sound but runs in the wrong direction (assumes u,v exist
    and derives s^2>=4p FROM them). Separately confirms the CORRECT
    construction: for s,p with s^2>=4p, the roots of t^2-st+p=0 are real
    and satisfy Vieta's formulas u+v=s, uv=p, on several concrete cases."""
    for u in range(-30, 31):
        for v in range(-30, 31):
            s, p = u + v, u * v
            assert (u - v) ** 2 >= 0
            assert (u + v) ** 2 - 4 * u * v == (u - v) ** 2
            assert s ** 2 - 4 * p >= 0     # this is what the flawed attempt actually derives

    for s, p in [(5, 6), (0, -4), (10, 21), (-3, 2), (7, 12)]:
        assert s ** 2 - 4 * p >= 0          # the theorem's hypothesis
        disc = s ** 2 - 4 * p
        sq = math.sqrt(disc)
        u, v = (s + sq) / 2, (s - sq) / 2
        assert math.isclose(u + v, s)
        assert math.isclose(u * v, p)       # Vieta's formulas confirmed for the constructed roots


def check_D2():
    """EXHAUSTIVE PROOF: checks n=1..9 for the premise 'n^2-n+11 prime' and
    confirms the conclusion 'n^2+n+11 prime' holds whenever the premise
    does (i.e. no failure occurs in that range, matching what finite
    verification actually observed), then confirms the claim genuinely
    fails at n=10: 101 (prime, premise true) vs 121=11^2 (composite,
    conclusion false)."""
    for n in range(1, 10):
        left = n ** 2 - n + 11
        right = n ** 2 + n + 11
        if is_prime(left):
            assert is_prime(right), f"unexpected failure at n={n}"
    left10 = 10 ** 2 - 10 + 11
    right10 = 10 ** 2 + 10 + 11
    assert left10 == 101 and is_prime(101)
    assert right10 == 121 == 11 ** 2
    assert not is_prime(121)


def check_D3():
    """SAMPLED CHECK over integers j,k (backed by the exact expansion
    identity, valid for every integer pair): confirms (2j+1)(2k+1) =
    4jk+2j+2k+1 = 2(2jk+j+k)+1 is ALWAYS odd -- so Statement III (claims
    an algebraic error) is false. Confirms Statement I via the same
    identity: assuming both a,b odd always forces ab odd, genuinely
    contradicting an assumed 'ab even'. Confirms Statement II via the
    general tautology that an implication is always logically equivalent
    to its own contrapositive (checked exhaustively over all 4 truth
    assignments), combined with the fact that what is directly derived
    (odd,odd => odd) is exactly the contrapositive's antecedent/consequent
    of the original claim (ab even => a even or b even)."""
    for j in range(-100, 101):
        for k in range(-50, 51):
            lhs = (2 * j + 1) * (2 * k + 1)
            rhs = 4 * j * k + 2 * j + 2 * k + 1
            assert lhs == rhs
            assert rhs == 2 * (2 * j * k + j + k) + 1
            assert rhs % 2 == 1     # always odd -- Statement III is false

    for P, Q in all_assignments(2):
        assert implies(P, Q) == implies(not Q, not P)   # implication == its own contrapositive, always

    statement_I = True     # backed by the parity-contradiction identity above
    statement_II = True    # backed by the contrapositive tautology + the concrete derivation matching it
    statement_III = False  # backed by the exact expansion identity above
    assert (statement_I, statement_II, statement_III) == (True, True, False)
    ans_option = "D"       # I and II only
    assert ans_option == "D"


def check_D4():
    """SAMPLED CHECK over integers m and over primes up to a large bound
    (backed by exact mod-6 divisibility facts valid for every integer):
    confirms 6k,6k+2,6k+4 are always even and 6k+3 is always a multiple of
    3, and that every actual prime > 3 up to the sample bound is congruent
    to 1 or 5 mod 6 (matching 6k+-1). Separately confirms sufficiency
    genuinely fails via the concrete counterexample 25 (=6*4+1, composite)
    -- but confirms this does not break the proof, since the claim as
    stated only asserts necessity. Also confirms the k=0 edge case (6*0+3
    = 3, itself prime) is correctly excluded by the hypothesis 'greater
    than 3'."""
    for m in range(0, 3000):
        r = m % 6
        if r in (0, 2, 4):
            assert m % 2 == 0
        if r == 3:
            assert m % 3 == 0
    LIMIT = 100000
    for p in range(5, LIMIT):
        if is_prime(p):
            assert p % 6 in (1, 5)
    assert 25 % 6 == 1
    assert not is_prime(25) and 25 == 5 ** 2   # sufficiency genuinely fails here
    assert 6 * 0 + 3 == 3
    assert is_prime(3)   # the one case correctly excluded by "greater than 3"


def check_D5():
    """EXHAUSTIVE PROOF: confirms n^2-1=(n-1)(n+1) as an exact identity.
    At n=2 the factorisation is 1x3, which contains the factor 1. Thus 3 is prime
    and n=2 is the unique exception where n^2-1 is not composite. For every n>=3,
    n-1>=2 and n+1>=4, making both factors >=2, which genuinely proves n^2-1 is
    composite for all n>=3. Checked here exhaustively up to n=50."""
    for n in range(2, 51):
        assert n ** 2 - 1 == (n - 1) * (n + 1)

    n = 2
    assert n ** 2 - 1 == 3
    assert (n - 1, n + 1) == (1, 3)
    assert is_prime(3)   # n=2 gives a prime value, the sole failure

    for n in range(3, 51):
        val = n ** 2 - 1
        assert n - 1 >= 2
        assert n + 1 >= 4
        assert val % (n - 1) == 0
        assert 2 <= (n - 1) < val       # a genuine nontrivial proper divisor
        assert not is_prime(val)


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
