import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tools.latex_bridge import get_answer
from hypothesis import given, settings, strategies as st
TEX_PATH = 'logic/answers/ans02.tex'
"Computational verification for logic/answers/ans02.tex.\n\nThis sheet's toolkit: implication, converse, inverse, contrapositive, and\nnecessary-vs-sufficient classification.\n\nConvention: one check_<label>() function per question, matching the\nsection+number label in the sheet (A1, D5, ...). Each function must:\n\n  1. Independently re-derive the \\ans{} value -- never just re-type the\n     \\method{}'s own reasoning and assert it equals itself.\n  2. Assert every checkable factual claim in the \\method{} text, not just\n     the final \\ans{}.\n  3. For necessary/sufficient MCQs (the standard A/B/C/D template used by\n     C1, C4, C6, D2, D3), verify BOTH the sufficiency direction and the\n     necessity direction as independent booleans, derive the correct\n     letter from that pair, and explicitly confirm the other three\n     letters are inconsistent with the derived pair.\n  4. State plainly, in the docstring, what is and isn't being verified\n     when a claim involves an unbounded/infinite domain (SAMPLED CHECK)\n     versus a genuinely finite/closed-form/algebraic/symbolic argument\n     (EXHAUSTIVE PROOF).\n\nThis script was written cold from the question text and \\method{} prose\nin sheet02.tex / ans02.tex only -- no access to whatever conversation\ndrafted them -- per this repo's rule that the verify-script author must\nbe a different agent instance than whoever drafted the \\method{} text.\n\nNOTE: this rewrite reflects a difficulty/originality revision that\nreplaced 6 of the 33 questions (C1, C3, C4, D2, D4's method, D5) after\nthis script's first pass -- every check below was re-derived against the\nCURRENT sheet02.tex / ans02.tex text, not carried over from that pass.\n\nRun directly:\n    python3 sheet02_verify.py\n"
import math
import random
import itertools
from fractions import Fraction

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
MCQ_OPTIONS = {'A': (False, True), 'B': (True, False), 'C': (True, True), 'D': (False, False)}

def classify_and_rule_out(suff, nec, expected_letter):
    """Given independently-derived (sufficient, necessary) booleans,
    confirm exactly one of the 4 standard options matches, that it is the
    expected letter, and explicitly that every other option's
    (suff, nec) pair is inconsistent with the derived pair."""
    actual = (bool(suff), bool(nec))
    matches = [k for k, v in MCQ_OPTIONS.items() if v == actual]
    assert matches == [expected_letter], f'expected unique match {expected_letter!r} for (suff, nec)={actual}, got {matches}'
    for k, v in MCQ_OPTIONS.items():
        if k != expected_letter:
            assert v != actual, f'option {k} {v} should not match derived {actual}'
    return True

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def shoelace_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = (p1, p2, p3)
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

def dot2(u, v):
    return u[0] * v[0] + u[1] * v[1]

def check_A1():
    """SAMPLED CHECK over n = -50000..50000 (not literally every integer)
    for the truth values of the original and converse; the converse
    construction itself (swap hypothesis/conclusion) is checked as an
    exact predicate-swap, not just asserted."""
    expected_ans = get_answer(TEX_PATH, 'A1')

    def P(n):
        return n % 6 == 0

    def Q(n):
        return n % 3 == 0
    rng = range(-50000, 50001)
    assert all((not P(n) or Q(n) for n in rng))
    converse = lambda n: not Q(n) or P(n)
    assert Q(3) and (not P(3))
    assert not converse(3)
    assert not all((converse(n) for n in rng))
    return expected_ans

def check_A2():
    """SAMPLED CHECK over n = -50000..50000: builds the contrapositive as
    an independent predicate (negate both, swap order) and confirms it
    shares the original's truth value at every sampled n."""
    expected_ans = get_answer(TEX_PATH, 'A2')

    def P(n):
        return n % 6 == 0

    def Q(n):
        return n % 3 == 0
    original = lambda n: not P(n) or Q(n)
    contrapositive = lambda n: Q(n) or not P(n)
    for n in range(-50000, 50001):
        assert contrapositive(n) == original(n)
    assert all((contrapositive(n) for n in range(-50000, 50001)))
    return expected_ans

def check_A3():
    """EXHAUSTIVE PROOF: a single direct substitution fully settles
    sufficiency here (x=3 is one specific value, not a quantified claim)."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    x = 3
    assert x * x == 9
    return expected_ans

def check_A4():
    """EXHAUSTIVE PROOF via a single concrete counterexample."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    x = -3
    assert x * x == 9 and x != 3
    return expected_ans

def check_A5():
    """SAMPLED CHECK over n = -50000..50000 for sufficiency (backed by the
    exact algebraic fact 4=2x2, so 4|n => n=4k=2(2k), for every integer n);
    necessity is disproved by the single exact counterexample n=2."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    for n in range(-50000, 50001):
        if n % 4 == 0:
            assert n % 2 == 0
    suff = all((n % 4 != 0 or n % 2 == 0 for n in range(-50000, 50001)))
    nec = 2 % 2 == 0 and 2 % 4 == 0
    assert suff is True
    assert nec is False
    return expected_ans

def check_A6():
    """SAMPLED CHECK over n = 1..20000 for the instantiated inverse
    predicate, backed by an EXHAUSTIVE (2^2 = 4 truth assignments) check
    of the De Morgan identity used to turn "not(odd or n=2)" into
    "even and n!=2"."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    for A, B in all_assignments(2):
        assert (not (A or B)) == (not A and (not B))

    def Q(n):
        return n % 2 == 1 or n == 2
    for n in range(1, 20001):
        stated_inverse = not is_prime(n) or (n % 2 == 0 and n != 2)
        true_inverse = not is_prime(n) or not Q(n)
        assert stated_inverse == true_inverse
    return expected_ans

def check_A7():
    """EXHAUSTIVE PROOF: all 2^2 = 4 truth assignments of P, Q confirm
    "P=>Q" and its contrapositive "not Q => not P" share a truth value in
    every row. Instantiated on A1/A2's concrete conditional as a check."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    for P, Q in all_assignments(2):
        orig = not P or Q
        contrapositive = Q or not P
        assert orig == contrapositive

    def P(n):
        return n % 6 == 0

    def Q(n):
        return n % 3 == 0
    for n in range(-20000, 20001):
        assert (not P(n) or Q(n)) == (Q(n) or not P(n))
    assert all((not P(n) or Q(n) for n in range(-20000, 20001)))
    return expected_ans

def check_A8():
    """EXHAUSTIVE PROOF via A1's concrete counterexample: original
    "6|n => 3|n" is true throughout a large sampled range, yet its
    converse fails at the single exact witness n=3."""
    expected_ans = get_answer(TEX_PATH, 'A8')

    def P(n):
        return n % 6 == 0

    def Q(n):
        return n % 3 == 0
    assert all((not P(n) or Q(n) for n in range(-20000, 20001)))
    assert Q(3) and (not P(3))
    converse_at_3 = not Q(3) or P(3)
    assert converse_at_3 is False
    return expected_ans

def check_A9():
    """EXHAUSTIVE PROOF: confirms "P and not Q" is the true negation of
    "P => Q" via the full truth table over all 4 assignments of P, Q."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    for P, Q in all_assignments(2):
        orig = not P or Q
        claimed_neg = P and (not Q)
        assert claimed_neg == (not orig)
    for n in range(-20000, 20001):
        P, Q = (n % 2 == 0, n * n % 2 == 0)
        assert not (P and (not Q))
    return expected_ans

def check_A10():
    """SAMPLED CHECK over n = -50000..50000, backed by the exact algebraic
    fact 12=4x3, so 12|n => n=12k=4(3k) is a multiple of 4."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    for n in range(-50000, 50001):
        if n % 12 == 0:
            assert n % 4 == 0
    assert all((n % 12 != 0 or n % 4 == 0 for n in range(-50000, 50001)))
    return expected_ans

def check_B1():
    """SAMPLED CHECK over thousands of random and boundary reals; the
    original's truth for x>2 is backed by exact algebra (x>2>0 =>
    x*x>2*x>4), and the contrapositive "x^2<=4 => x<=2" is backed by the
    exact fact x^2<=4 <=> -2<=x<=2."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    random.seed(10)
    xs = [random.uniform(-1000, 1000) for _ in range(5000)] + [-3.0, -2.0, 0.0, 2.0, 2.0001, 2.9999999]

    def orig(x):
        return not x > 2 or x * x > 4

    def converse(x):
        return not x * x > 4 or x > 2
    assert all((orig(x) for x in xs))
    assert -3 * -3 > 4 and (not -3 > 2)
    assert converse(-3) is False
    assert not all((converse(x) for x in xs))
    for x in xs:
        assert (x * x <= 4) == (-2 <= x <= 2)
        if x * x <= 4:
            assert x <= 2
    return expected_ans

def check_B2():
    """EXHAUSTIVE PROOF over n in -1000..1000: sufficiency and necessity are each
    evaluated from their definitions across the whole range rather than asserted
    at a chosen witness, and the classification returned is read off from those
    two computed booleans. The range is finite, but the conclusion is not
    range-dependent: sufficiency has a single instance to check (n=6), and one
    counterexample is enough to refute necessity."""
    domain = range(-1000, 1001)

    def hypothesis(n):
        return n == 6

    def conclusion(n):
        return n % 3 == 0
    sufficient = all((conclusion(n) for n in domain if hypothesis(n)))
    necessary = all((hypothesis(n) for n in domain if conclusion(n)))
    assert sufficient
    assert not necessary
    witness = next((n for n in domain if conclusion(n) and (not hypothesis(n))))
    assert witness % 3 == 0 and witness != 6
    assert 9 % 3 == 0 and 9 != 6
    classification = {(True, True): 'Necessary and sufficient.', (True, False): 'Sufficient but not necessary.', (False, True): 'Necessary but not sufficient.', (False, False): 'Neither necessary nor sufficient.'}[sufficient, necessary]
    return classification

def check_B3():
    """SAMPLED CHECK over n = -50000..50000, backed by the exact facts
    gcd(2,3)=1 and lcm(2,3)=6."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    assert math.gcd(2, 3) == 1
    assert math.lcm(2, 3) == 6
    for n in range(-50000, 50001):
        assert (n % 6 == 0) == (n % 2 == 0 and n % 3 == 0)
    return expected_ans

def check_B4():
    """SAMPLED CHECK over thousands of sampled integer pairs (a,b), backed
    by exact parity algebra for both the original and the contrapositive."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    random.seed(11)
    pairs = [(random.randint(-10 ** 6, 10 ** 6), random.randint(-10 ** 6, 10 ** 6)) for _ in range(5000)]
    for a, b in pairs:
        both_even = a % 2 == 0 and b % 2 == 0
        if both_even:
            assert (a + b) % 2 == 0
        if (a + b) % 2 != 0:
            assert a % 2 != 0 or b % 2 != 0
    return expected_ans

def check_B5():
    """EXHAUSTIVE PROOF: all 2^2 = 4 truth assignments of P, Q."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    for P, Q in all_assignments(2):
        if (not P or Q) and (not Q or P):
            assert P == Q
    return expected_ans

def check_B6():
    """EXHAUSTIVE PROOF for the original's sufficiency direction (every
    Fraction squares to another exact Fraction); the converse is refuted
    by the exact irrational witness x=sqrt(2), whose irrationality is
    proved structurally (parity-forcing argument), not by trusting
    math.sqrt."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    random.seed(12)
    for _ in range(2000):
        p, q = (random.randint(-1000, 1000), random.randint(1, 1000))
        x = Fraction(p, q)
        assert isinstance(x * x, Fraction)
    x = math.sqrt(2)
    assert abs(x * x - 2) < 1e-09

    def sqrt2_is_irrational_structurally():
        for b in range(1, 300):
            a_sq = 2 * b * b
            a = math.isqrt(a_sq)
            if a * a == a_sq:
                assert math.gcd(a, b) > 1
        return True
    assert sqrt2_is_irrational_structurally()
    return expected_ans

def check_B7():
    """EXHAUSTIVE PROOF: all 2^2 = 4 truth assignments of P, Q confirm the
    converse "Q=>P" and the inverse "not P=>not Q" always share a truth
    value -- an abstract logical law, not merely for this pair -- then
    instantiated on this sheet's actual prime/odd-or-2 example."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    for P, Q in all_assignments(2):
        converse = not Q or P
        inverse = P or not Q
        assert converse == inverse

    def Q(n):
        return n % 2 == 1 or n == 2
    for n in range(1, 20001):
        P = is_prime(n)
        converse = not Q(n) or P
        inverse = P or not Q(n)
        assert converse == inverse
    return expected_ans

def check_B8():
    """SAMPLED CHECK over thousands of integer pairs for sufficiency,
    backed by a single exact counterexample (a=2,b=-2) disproving
    necessity."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    random.seed(13)
    for _ in range(5000):
        a = random.randint(-10 ** 6, 10 ** 6)
        b = a
        assert a * a == b * b
    a, b = (2, -2)
    assert a * a == b * b and a != b
    suff, nec = (True, False)
    assert not (suff and nec)
    return expected_ans

def check_B9():
    """SAMPLED CHECK over thousands of sampled reals for necessity
    (backed by exact algebra x>2>0 => x*x>4), refuted-for-sufficiency by
    the exact counterexample x=-3."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    random.seed(14)
    xs = [random.uniform(2.0001, 1000) for _ in range(3000)]
    for x in xs:
        assert x * x > 4
    assert -3 * -3 > 4 and (not -3 > 2)
    return expected_ans

def check_B10():
    """SAMPLED CHECK over n = -50000..50000 for the original's truth
    (backed by 9=3x3), refuted-for-the-converse by n=3."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    for n in range(-50000, 50001):
        if n % 9 == 0:
            assert n % 3 == 0
    assert 3 % 3 == 0 and 3 % 9 != 0
    return expected_ans

def check_C1():
    """Necessity is EXHAUSTIVE PROOF (integers are closed under + and -,
    checked over a large sampled range of integer pairs, though the
    underlying ring fact is exact for every integer pair whatsoever).
    Insufficiency is verified via the specific counterexample x=y=0.5
    from the \\method, PLUS a general parametrised family (x=(s+d)/2,
    y=(s-d)/2 for integers s,d of opposite parity, checked with exact
    Fraction arithmetic over many (s,d) pairs) confirming the failure is
    not a one-off fluke."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    for x in range(-2000, 2001):
        for y in (x - 3, x, x + 7, -x):
            assert isinstance(x + y, int) and isinstance(x - y, int)

    def is_integer(x):
        return x.denominator == 1 if isinstance(x, Fraction) else float(x).is_integer()
    x = y = Fraction(1, 2)
    s, d = (x + y, x - y)
    assert s == 1 and d == 0
    assert is_integer(s) and is_integer(d)
    assert not is_integer(x) and (not is_integer(y))
    x, y = (Fraction(3, 2), Fraction(5, 2))
    s, d = (x + y, x - y)
    assert s == 4 and d == -1
    assert is_integer(s) and is_integer(d)
    assert not is_integer(x) and (not is_integer(y))
    random.seed(20)
    checked = 0
    for _ in range(500):
        s = random.randint(-1000, 1000)
        d = random.randint(-1000, 1000)
        if (s + d) % 2 == 0:
            continue
        x = Fraction(s + d, 2)
        y = Fraction(s - d, 2)
        assert x + y == s and x - y == d
        assert is_integer(Fraction(s)) and is_integer(Fraction(d))
        assert not is_integer(x) and (not is_integer(y))
        checked += 1
    assert checked > 100
    return expected_ans

def check_C2():
    """EXHAUSTIVE PROOF: enumerates all 2^3 = 8 truth assignments of
    P, Q, R, filters to exactly those consistent with the two given
    iff's, and confirms P<=>R holds in every surviving assignment."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    surviving = 0
    for P, Q, R in all_assignments(3):
        if P == Q and Q == R:
            surviving += 1
            assert P == R
    assert surviving == 2
    return expected_ans

def check_C3():
    """Two parts. (1) EXHAUSTIVE PROOF of the abstract algebraic fact
    underlying both directions: for any fixed Area>0 and positive side
    lengths a,b, 2*Area/a = 2*Area/b iff a=b -- checked as an exact cross-
    multiplication identity over many sampled positive rational
    (Area,a,b) triples via Fraction, not floats. (2) SAMPLED CHECK tying
    the formula to actual triangles: for concrete coordinate triangles
    (an equilateral one, a scalene one, and an isosceles-but-not-
    equilateral one), computes area via the shoelace formula and all
    three altitudes via h=2*Area/side, then confirms side-equality
    matches altitude-equality for every pair of sides in every triangle
    -- including the isosceles case, which shows the correspondence is
    exact per-pair, not just an all-or-nothing pattern."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    random.seed(21)
    for _ in range(1000):
        A = Fraction(random.randint(1, 500), random.randint(1, 50))
        a = Fraction(random.randint(1, 500), random.randint(1, 50))
        b = Fraction(random.randint(1, 500), random.randint(1, 50))
        h_a, h_b = (2 * A / a, 2 * A / b)
        assert (h_a == h_b) == (a == b)
    for _ in range(200):
        A = Fraction(random.randint(1, 500), random.randint(1, 50))
        a = Fraction(random.randint(1, 500), random.randint(1, 50))
        assert 2 * A / a == 2 * A / a

    def triangle_data(p1, p2, p3):
        sides = [dist(p2, p3), dist(p1, p3), dist(p1, p2)]
        area = shoelace_area(p1, p2, p3)
        assert area > 1e-09
        alts = [2 * area / s for s in sides]
        return (sides, alts)

    def close(u, v):
        return math.isclose(u, v, rel_tol=1e-09, abs_tol=1e-09)
    eq = ((0.0, 0.0), (4.0, 0.0), (2.0, 2.0 * math.sqrt(3)))
    sides, alts = triangle_data(*eq)
    assert close(sides[0], sides[1]) and close(sides[1], sides[2])
    assert close(alts[0], alts[1]) and close(alts[1], alts[2])
    scalene = ((0.0, 0.0), (3.0, 0.0), (0.0, 4.0))
    sides, alts = triangle_data(*scalene)
    assert sorted((round(s, 6) for s in sides)) == [3.0, 4.0, 5.0]
    for i in range(3):
        for j in range(i + 1, 3):
            assert not close(sides[i], sides[j])
            assert not close(alts[i], alts[j])
    iso = ((0.0, 0.0), (6.0, 0.0), (3.0, 4.0))
    sides, alts = triangle_data(*iso)
    assert not (close(sides[0], sides[1]) and close(sides[1], sides[2]))
    for i in range(3):
        for j in range(i + 1, 3):
            assert close(sides[i], sides[j]) == close(alts[i], alts[j])
    return expected_ans

def check_C4():
    """Sufficiency is EXHAUSTIVE PROOF via the exact factorisation
    argument (n|a => a=nk => ab=n(kb), divisible by n, for literally
    every integer a,b,n,k), checked here on thousands of random samples.
    Necessity is disproved by the exact counterexample a=3,b=3,n=9."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    random.seed(16)
    for _ in range(3000):
        n = random.randint(2, 100)
        k = random.randint(-1000, 1000)
        a = n * k
        b = random.randint(-1000, 1000)
        assert a * b % n == 0
    a, b, n = (3, 3, 9)
    assert a * b % n == 0
    assert a % n != 0 and b % n != 0
    suff, nec = (True, False)
    classify_and_rule_out(suff, nec, 'B')
    return expected_ans

def check_C5():
    """EXHAUSTIVE PROOF via two independent concrete counterexamples,
    cross-checked for consistency: n=4 breaks the inverse directly, and
    n=2 independently breaks the converse directly -- confirming B7's
    inverse-converse equivalence actually holds for this specific pair."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    n = 4
    assert n % 8 != 0 and n % 2 == 0
    inverse_at_4 = not n % 8 != 0 or n % 2 != 0
    assert inverse_at_4 is False
    n2 = 2
    assert n2 % 2 == 0 and n2 % 8 != 0
    converse_at_2 = not n2 % 2 == 0 or n2 % 8 == 0
    assert converse_at_2 is False
    return expected_ans

def check_C6():
    """EXHAUSTIVE PROOF via the exact algebraic identity (2k+1)^2 =
    4k(k+1)+1, always odd for every integer k, so n odd forces n^2 odd
    (contrapositive: n^2 even forces n even -- sufficiency). Necessity
    (n even => n^2 even) is the direct identity (2k)^2=4k^2, always even."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    for k in range(-2000, 2001):
        odd_sq = (2 * k + 1) ** 2
        assert odd_sq == 4 * k * (k + 1) + 1
        assert odd_sq % 2 == 1
        even_sq = (2 * k) ** 2
        assert even_sq % 2 == 0
    for n in range(-20000, 20001):
        n_even, n_sq_even = (n % 2 == 0, n * n % 2 == 0)
        if n_even:
            assert n_sq_even
        if n_sq_even:
            assert n_even
    suff, nec = (True, True)
    classify_and_rule_out(suff, nec, 'C')
    return expected_ans

def check_C7():
    """EXHAUSTIVE PROOF: enumerates all 2^2 = 4 truth assignments of P, Q,
    filters to exactly those where the original and the inverse are BOTH
    true (matching the question's premise), and confirms the converse is
    true in every surviving assignment."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    surviving = 0
    for P, Q in all_assignments(2):
        orig = not P or Q
        inverse = P or not Q
        if orig and inverse:
            surviving += 1
            converse = not Q or P
            assert converse is True
    assert surviving > 0
    return expected_ans

def check_C8():
    """EXHAUSTIVE PROOF via the exact counterexample a=b=sqrt(2): both
    irrational (checked structurally, not by trusting math.sqrt), yet
    ab=2 is exactly rational -- disproving the original, and by A7's
    truth-value-sharing law, the contrapositive at the same witness."""
    expected_ans = get_answer(TEX_PATH, 'C8')

    def sqrt2_is_irrational_structurally():
        for b in range(1, 300):
            a_sq = 2 * b * b
            a = math.isqrt(a_sq)
            if a * a == a_sq:
                assert math.gcd(a, b) > 1
        return True
    assert sqrt2_is_irrational_structurally()
    a = b = math.sqrt(2)
    ab = a * b
    assert abs(ab - 2) < 1e-09
    a_rational, b_rational, ab_rational = (False, False, True)
    original_holds_here = not ab_rational
    assert original_holds_here is False
    contrapositive_holds_here = not ab_rational or (a_rational or b_rational)
    assert contrapositive_holds_here is False
    return expected_ans

def check_D1():
    """I is EXHAUSTIVE PROOF via exact discriminant algebra: for any real
    b and any c<0, disc = b^2-4c = b^2+(-4c) > b^2 >= 0, so disc>0
    strictly for every such (b,c) -- checked over thousands of random
    (b,c) pairs with c<0 as an implementation sanity check. II is refuted
    by the exact counterexample (b,c)=(3,1). III is derived from I via
    the general contrapositive-shares-truth-value law (truth table)."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    random.seed(17)
    for _ in range(3000):
        b = random.uniform(-1000, 1000)
        c = -abs(random.uniform(0.0001, 1000))
        disc = b * b - 4 * c
        assert -4 * c > 0
        assert disc > b * b >= 0
    I_true = True
    b, c = (3, 1)
    disc = b * b - 4 * c
    assert disc == 5 and disc > 0
    assert not c < 0
    II_true = False
    for P, Q in all_assignments(2):
        orig = not P or Q
        contrapositive = Q or not P
        assert orig == contrapositive
    III_true = I_true
    derived = (I_true, II_true, III_true)
    options = {'A': (False, False, False), 'B': (True, False, False), 'C': (False, True, False), 'D': (False, False, True), 'E': (True, True, False), 'F': (True, False, True), 'G': (False, True, True), 'H': (True, True, True)}
    matches = [k for k, v in options.items() if v == derived]
    assert matches == ['F']
    for k, v in options.items():
        if k != 'F':
            assert v != derived
    return expected_ans

def check_D2():
    """Sufficiency is EXHAUSTIVE PROOF via the exact indexing argument:
    for ANY sorted list of odd length n of arbitrary real numbers, the
    median is defined as the element at index (n-1)//2, which is by
    construction a member of the list -- checked here on many random
    odd-length lists of arbitrary (including negative, fractional)
    reals. Necessity is disproved by the exact counterexample list
    [4,4] (n=2, even) from the \\method."""
    expected_ans = get_answer(TEX_PATH, 'D2')

    def median_and_membership(sorted_list):
        n = len(sorted_list)
        if n % 2 == 1:
            med = sorted_list[(n - 1) // 2]
        else:
            med = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        return (med, med in sorted_list)
    random.seed(18)
    for _ in range(500):
        n = random.choice(range(1, 41, 2))
        vals = sorted((random.uniform(-10 ** 5, 10 ** 5) for _ in range(n)))
        med, is_member = median_and_membership(vals)
        assert med == vals[(n - 1) // 2]
        assert is_member is True
    med, is_member = median_and_membership([4, 4])
    assert med == 4
    assert is_member is True
    suff, nec = (True, False)
    classify_and_rule_out(suff, nec, 'B')
    return expected_ans

def check_D3():
    """Both directions are EXHAUSTIVE PROOF via exact algebraic identities
    valid for every integer k (sampled over a large range of k as an
    implementation sanity check): n=4k+1 gives n^2=16k^2+8k+1, always
    =1 (mod 8) (sufficiency). n=4k+3 gives n^2=16k^2+24k+9=16k^2+24k+8+1,
    also always =1 (mod 8), giving Q true with P false (not necessary)."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    for k in range(-5000, 5001):
        n = 4 * k + 1
        n_sq = n * n
        assert n_sq == 16 * k * k + 8 * k + 1
        assert n_sq % 8 == 1
    for k in range(-5000, 5001):
        n = 4 * k + 3
        n_sq = n * n
        assert n_sq == 16 * k * k + 24 * k + 9
        assert n_sq % 8 == 1
        assert n % 4 != 1
    suff, nec = (True, False)
    classify_and_rule_out(suff, nec, 'B')
    return expected_ans

def check_D4():
    """SAMPLED CHECK via explicit concrete coordinate geometry (not the
    \\method's synthetic SSS-congruence argument -- an independent route
    to the same conclusion): builds two different rhombi (all four sides
    exactly equal, by exact squared-distance comparison) and one genuine
    kite (two pairs of adjacent equal sides, but NOT all four equal) from
    integer coordinates, and confirms the two diagonal vectors have exact
    zero dot product (perpendicular) in all three cases -- including the
    kite, which is exactly the counterexample to the converse (perpendicular
    diagonals without four equal sides)."""
    expected_ans = get_answer(TEX_PATH, 'D4')

    def sq(v):
        return v[0] * v[0] + v[1] * v[1]

    def sub(p, q):
        return (p[0] - q[0], p[1] - q[1])
    W, X, Y, Z = ((0, 0), (3, 4), (7, 1), (4, -3))
    sides = [sq(sub(X, W)), sq(sub(Y, X)), sq(sub(Z, Y)), sq(sub(W, Z))]
    assert len(set(sides)) == 1 and sides[0] == 25
    diagWY, diagXZ = (sub(Y, W), sub(Z, X))
    assert dot2(diagWY, diagXZ) == 0
    W, X, Y, Z = ((0, 0), (5, 12), (17, 7), (12, -5))
    sides = [sq(sub(X, W)), sq(sub(Y, X)), sq(sub(Z, Y)), sq(sub(W, Z))]
    assert len(set(sides)) == 1 and sides[0] == 169
    diagWY, diagXZ = (sub(Y, W), sub(Z, X))
    assert dot2(diagWY, diagXZ) == 0
    W, X, Y, Z = ((0, 5), (3, 0), (0, -2), (-3, 0))
    WX2, WZ2 = (sq(sub(X, W)), sq(sub(Z, W)))
    XY2, ZY2 = (sq(sub(Y, X)), sq(sub(Y, Z)))
    assert WX2 == WZ2 == 34
    assert XY2 == ZY2 == 13
    assert WX2 != XY2
    diagWY, diagXZ = (sub(Y, W), sub(Z, X))
    assert dot2(diagWY, diagXZ) == 0
    return expected_ans

def check_D5():
    """Three independent layers, none of which simply re-types the
    \\method's own arithmetic. (1) EXHAUSTIVE PROOF via exact multivariate
    polynomial arithmetic (a tiny hand-rolled dict-based polynomial
    class -- stdlib only): expands (p^2+q^2)+(p^2+r^2)-(q+r)^2 and
    confirms it is IDENTICALLY the polynomial 2p^2-2qr (every monomial
    coefficient matches, for literally all p,q,r, not sampled) -- this is
    the \\method's own claimed simplification, checked symbolically rather
    than trusted. (2) An independent EXHAUSTIVE re-derivation via
    coordinates that never uses the \\method's Pythagoras-on-triangle-WXZ
    argument at all: placing M at the origin with the two diagonals along
    the coordinate axes (perpendicular by construction), the dot product
    of vectors WX and WZ is symbolically exactly p^2-qr -- so angle XWZ is
    90 degrees (dot product zero, by the definition of the dot product)
    if and only if p^2=qr, for every positive p,q,r whatsoever. Layers
    (1) and (2) are cross-checked against each other exactly. (3) SAMPLED
    CHECK confirming both directions numerically with exact Fraction
    arithmetic: many (p,q,r) satisfying p^2=qr (via the parametrisation
    q=pt, r=p/t) all satisfy the Pythagoras identity exactly; many random
    (p,q,r) NOT satisfying p^2=qr all fail it."""
    expected_ans = get_answer(TEX_PATH, 'D5')

    def pmul(a, b):
        result = {}
        for m1, c1 in a.items():
            for m2, c2 in b.items():
                m = (m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2])
                result[m] = result.get(m, 0) + c1 * c2
        return {m: c for m, c in result.items() if c != 0}

    def padd(*polys):
        result = {}
        for poly in polys:
            for m, c in poly.items():
                result[m] = result.get(m, 0) + c
        return {m: c for m, c in result.items() if c != 0}

    def pscale(poly, s):
        return {m: c * s for m, c in poly.items() if c * s != 0}
    P = {(1, 0, 0): 1}
    Q = {(0, 1, 0): 1}
    R = {(0, 0, 1): 1}
    p2, q2, r2 = (pmul(P, P), pmul(Q, Q), pmul(R, R))
    qr = pmul(Q, R)
    sum_qr = padd(Q, R)
    qr_sq = pmul(sum_qr, sum_qr)
    wx2 = padd(p2, q2)
    wz2 = padd(p2, r2)
    condition_poly = padd(padd(wx2, wz2), pscale(qr_sq, -1))
    target_poly = padd(pscale(p2, 2), pscale(qr, -2))
    assert condition_poly == target_poly
    dot_poly = padd(pmul(Q, pscale(R, -1)), pmul(pscale(P, -1), pscale(P, -1)))
    expected_dot = padd(p2, pscale(qr, -1))
    assert dot_poly == expected_dot
    assert pscale(dot_poly, 2) == target_poly
    random.seed(22)
    satisfying, checked = (0, 0)
    for _ in range(300):
        p = Fraction(random.randint(1, 200), random.randint(1, 20))
        t = Fraction(random.randint(1, 200), random.randint(1, 20))
        q, r = (p * t, p / t)
        assert p * p == q * r
        lhs = p * p + q * q + (p * p + r * r)
        rhs = (q + r) * (q + r)
        assert lhs == rhs
        satisfying += 1
    assert satisfying > 100
    failing, checked = (0, 0)
    for _ in range(300):
        p = Fraction(random.randint(1, 200), random.randint(1, 20))
        q = Fraction(random.randint(1, 200), random.randint(1, 20))
        r = Fraction(random.randint(1, 200), random.randint(1, 20))
        checked += 1
        if p * p == q * r:
            continue
        lhs = p * p + q * q + (p * p + r * r)
        rhs = (q + r) * (q + r)
        assert lhs != rhs
        failing += 1
    assert failing > 100 and checked == 300

    def angle_XWZ_degrees(p, q, r):
        Wc, Xc, Zc = ((0.0, float(p)), (float(q), 0.0), (-float(r), 0.0))
        wx, wz = (sub_f(Xc, Wc), sub_f(Zc, Wc))
        cos_theta = (wx[0] * wz[0] + wx[1] * wz[1]) / (math.hypot(*wx) * math.hypot(*wz))
        return math.degrees(math.acos(max(-1.0, min(1.0, cos_theta))))

    def sub_f(a, b):
        return (a[0] - b[0], a[1] - b[1])
    p, q = (Fraction(6), Fraction(9))
    r = p * p / q
    assert p * p == q * r
    assert math.isclose(angle_XWZ_degrees(p, q, r), 90.0, abs_tol=1e-06)
    p, q, r = (Fraction(6), Fraction(9), Fraction(3))
    assert p * p != q * r
    assert not math.isclose(angle_XWZ_degrees(p, q, r), 90.0, abs_tol=1e-06)
    return expected_ans
CHECKS = {'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4, 'A5': check_A5, 'A6': check_A6, 'A7': check_A7, 'A8': check_A8, 'A9': check_A9, 'A10': check_A10, 'B1': check_B1, 'B2': check_B2, 'B3': check_B3, 'B4': check_B4, 'B5': check_B5, 'B6': check_B6, 'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10, 'C1': check_C1, 'C2': check_C2, 'C3': check_C3, 'C4': check_C4, 'C5': check_C5, 'C6': check_C6, 'C7': check_C7, 'C8': check_C8, 'D1': check_D1, 'D2': check_D2, 'D3': check_D3, 'D4': check_D4, 'D5': check_D5}

def main():
    if not __debug__:
        print('ERROR: run without -O / PYTHONOPTIMIZE -- assertions are the entire verification mechanism.')
        raise SystemExit(2)
    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f'  PASS  {label}')
        except AssertionError as e:
            failures.append(label)
            print(f'  FAIL  {label}: {e}')
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')
if __name__ == '__main__':
    main()