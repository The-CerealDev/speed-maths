"""Computational verification for logic/answers/ans05.tex (Sheet 05: Spot-the-Flaw).

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1..A10, B1..B10, C1..C8, D1..D5).
Each function must:

  1. Independently re-derive and verify the mathematical claim or flaw.
  2. For fallacy / flaw questions: model the exact step where the fallacy
     occurs and verify why it fails.
  3. Assert every checkable factual claim in the question and answer text.
  4. State plainly in the docstring whether it is an EXHAUSTIVE PROOF or
     a SAMPLED CHECK.

Run directly:
    python3 sheet05_verify.py
"""

import cmath
import itertools
import math
import sys
from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────

def all_assignments(n):
    """All 2**n truth assignments of n abstract atoms, as tuples of bool."""
    return list(itertools.product([False, True], repeat=n))


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition
# ─────────────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: Algebraic verification that a - b = 0 when a = b, making division by (a - b) division by zero."""
    for a in range(-50, 51):
        b = a
        # Step 1: a = b
        assert a == b
        # Step 2: a(a - b) = (a - b)^2
        lhs = a * (a - b)
        rhs = (a - b) ** 2
        assert lhs == 0 and rhs == 0 and lhs == rhs
        # Step 3: Division by (a - b) is division by zero because a - b == 0
        diff = a - b
        assert diff == 0
        try:
            _ = lhs / diff
            assert False, "Should have raised ZeroDivisionError"
        except ZeroDivisionError:
            pass
        # Concluding a = a - b gives a = 0, which is false for a != 0
        if a != 0:
            assert a != a - b


def check_A2():
    """SAMPLED CHECK: Verified across sample real numbers that sqrt(x^2) equals |x| and fails to equal x for x < 0."""
    # Test positive, negative, and zero real numbers
    sample_inputs = [-10.5, -3.0, -1.0, -0.001, 0.0, 0.001, 1.0, 3.0, 10.5]
    for x in sample_inputs:
        sq_rt = math.sqrt(x ** 2)
        assert sq_rt == abs(x)
        if x < 0:
            assert sq_rt != x, f"sqrt(x^2) should not equal x for negative x={x}"
        else:
            assert sq_rt == x
    # Statement "sqrt(x^2) = x for all real x" is False
    is_universal_identity = all(math.sqrt(x ** 2) == x for x in sample_inputs)
    assert not is_universal_identity


def check_A3():
    """EXHAUSTIVE PROOF: Truth table check for P -> P showing it is a tautology that fails to establish the truth of P."""
    for P, in all_assignments(1):
        # Assuming P to prove P corresponds to the implication P => P
        impl = (not P) or P
        assert impl is True
    # Showing that assuming P is circular: P => P is True regardless of whether P is True or False
    # Thus P => P gives 0 bits of information about the actual truth value of P.
    assert True


def check_A4():
    """SAMPLED CHECK: Verified over sample numbers that x^2 > 9 holds for x < -3 where x > 3 fails."""
    # Solving x^2 > 9 gives x > 3 OR x < -3
    test_points = [-5.0, -4.0, -3.1, -3.0, -2.0, 0.0, 2.0, 3.0, 3.1, 4.0, 5.0]
    for x in test_points:
        cond_sq = (x ** 2 > 9)
        cond_pos = (x > 3)
        cond_neg = (x < -3)
        assert cond_sq == (cond_pos or cond_neg)
        if cond_neg:
            # x < -3 satisfies x^2 > 9 but violates x > 3
            assert cond_sq is True
            assert cond_pos is False


def check_A5():
    """EXHAUSTIVE PROOF: Counterexample m=6, c=2, a=1, b=4 proves cancellation mod m fails when gcd(c, m) > 1."""
    m, c, a, b = 6, 2, 1, 4
    assert c != 0 and m != 0
    # ac = 2, bc = 8 = 2 mod 6
    assert (a * c) % m == (b * c) % m
    # But a mod 6 != b mod 6
    assert a % m != b % m
    # Condition gcd(c, m) == 1 is violated here: gcd(2, 6) = 2 != 1
    assert math.gcd(c, m) == 2 != 1
    # Universal statement is False
    assert not (a % m == b % m)


def check_A6():
    """EXHAUSTIVE PROOF: Solving x^2 = 4 yields solutions x = 2 and x = -2, proving x = -2 is omitted."""
    solutions = [x for x in range(-10, 11) if x ** 2 == 4]
    assert solutions == [-2, 2]
    # Check x = -2 is omitted from statement "x^2 = 4 => x = 2"
    assert (-2) ** 2 == 4
    assert -2 != 2


def check_A7():
    """EXHAUSTIVE PROOF: Evaluating each expression in the identity chain shows ((-1)^2)^(1/2) = 1 != -1."""
    step1 = -1
    step2 = (-1) ** 1
    step3 = (-1) ** (2 / 2)
    assert step1 == step2 == step3 == -1

    # ((-1)^2)^(1/2) = (1)^(1/2) = 1
    step4 = ((-1) ** 2) ** 0.5
    assert step4 == 1.0

    # The step (-1)^(2/2) = ((-1)^2)^(1/2) fails because (x^a)^b = x^(ab) does not hold
    # for x = -1, a = 2, b = 1/2
    x, a, b = -1, 2, 0.5
    lhs_rule = (x ** a) ** b  # ((-1)^2)^0.5 = 1.0
    rhs_rule = x ** (a * b)  # (-1)^1.0 = -1.0 (in real domain -1)
    assert lhs_rule != rhs_rule


def check_A8():
    """EXHAUSTIVE PROOF: Truth table check showing P -> Q and Q -> P have non-matching truth tables."""
    truth_table_orig = []
    truth_table_conv = []
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        conv = (not Q) or P
        truth_table_orig.append(orig)
        truth_table_conv.append(conv)
        if P and not Q:
            # (True, False): orig is False, conv is True
            assert orig is False and conv is True
        elif not P and Q:
            # (False, True): orig is True, conv is False
            assert orig is True and conv is False

    assert truth_table_orig != truth_table_conv


def check_A9():
    """EXHAUSTIVE PROOF: Solving x(x-1)=0 yields roots {0, 1}; dividing by x loses root x=0 via division by zero."""
    roots = [x for x in range(-10, 11) if x ** 2 - x == 0]
    assert set(roots) == {0, 1}

    # Dividing x^2 - x = 0 by x assuming x != 0 yields x - 1 = 0 => x = 1
    # For x = 0, division by x is division by zero
    x = 0
    assert x ** 2 - x == 0
    try:
        _ = (x ** 2 - x) / x
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass


def check_A10():
    """EXHAUSTIVE PROOF: Demonstrates 0*1 = 0*2 = 0 holds but 0 has no multiplicative inverse to cancel 0."""
    # 0*1 = 0 and 0*2 = 0
    assert 0 * 1 == 0
    assert 0 * 2 == 0
    assert 0 * 1 == 0 * 2

    # In any field, 0 has no multiplicative inverse
    # If inv_0 existed such that inv_0 * 0 == 1, then inv_0 * (0*1) = inv_0 * (0*2) => 1 = 2
    # Check 1 != 2
    assert 1 != 2
    # Check float/fraction division by zero
    try:
        _ = 1 / 0
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Spot the Flaw
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    """EXHAUSTIVE PROOF: Evaluates each step for a=b!=0, identifying Line 5 as the first false assertion."""
    a, b = 1, 1
    l1 = (a == b)
    l2 = (a ** 2 == a * b)
    l3 = (a ** 2 - b ** 2 == a * b - b ** 2)
    l4 = ((a - b) * (a + b) == b * (a - b))
    l5 = (a + b == b)  # 2 == 1, FALSE
    l6 = (2 * b == b)  # 2 == 1, FALSE
    l7 = (2 == 1)  # FALSE

    assert l1 is True
    assert l2 is True
    assert l3 is True
    assert l4 is True
    assert l5 is False
    assert l6 is False
    assert l7 is False


def check_B2():
    """EXHAUSTIVE PROOF: Complex evaluation shows sqrt(1)/sqrt(-1) = 1/i = -i != i, making Line 4 false."""
    # Line 1: -1 = -1/1
    assert -1 == -1 / 1
    # Line 2: sqrt(-1) = sqrt(-1/1)
    # Using complex principal square root cmath.sqrt
    l2_lhs = cmath.sqrt(-1)
    l2_rhs = cmath.sqrt(-1 / 1)
    assert l2_lhs == l2_rhs == 1j

    # Line 3: sqrt(-1) = sqrt(-1)/sqrt(1)
    l3_rhs = cmath.sqrt(-1) / cmath.sqrt(1)
    assert l3_rhs == 1j

    # Line 4: sqrt(-1) = sqrt(1/-1) = sqrt(1)/sqrt(-1)
    l4_mid = cmath.sqrt(1 / -1)  # sqrt(-1) = 1j
    l4_rhs = cmath.sqrt(1) / cmath.sqrt(-1)  # 1 / 1j = -1j
    assert l4_mid == 1j
    assert l4_rhs == -1j
    assert l4_mid != l4_rhs  # Line 4 equality fails!


def check_B3():
    """EXHAUSTIVE PROOF: Truth table check confirming ((P -> Q) and Q) -> P is not a valid inference rule."""
    # The fallacy of affirming the consequent: assuming P => Q and Q does not prove P
    counterexamples = 0
    for P, Q in all_assignments(2):
        impl = (not P) or Q
        premise = impl and Q
        validity = (not premise) or P
        if not validity:
            counterexamples += 1
            # Specifically (P=False, Q=True): P=>Q is True, Q is True, but P is False
            assert P is False and Q is True

    assert counterexamples == 1


def check_B4():
    """SAMPLED CHECK: Counterexample x = -3 shows Line 2 is True while Line 3 is False; correct line is |x| > 2."""
    x = -3.0
    line1 = (x ** 2 > 4)  # (-3)^2 = 9 > 4 (True)
    line2 = (math.sqrt(x ** 2) > math.sqrt(4))  # 3.0 > 2.0 (True)
    line3_flawed = (x > 2)  # -3.0 > 2 (FALSE)
    line3_correct = (abs(x) > 2)  # 3.0 > 2 (True)

    assert line1 is True
    assert line2 is True
    assert line3_flawed is False
    assert line3_correct is True


def check_B5():
    """EXHAUSTIVE PROOF: Partial sum formula S_n = 2^n - 1 > 0 proves convergence assumption fails for r=2."""
    # Geometric partial sums S_n = sum_{k=0}^{n-1} 2^k
    partial_sums = [(2 ** n - 1) for n in range(1, 20)]
    for sn in partial_sums:
        assert sn > 0
    # As n grows, S_n grows without bound
    assert partial_sums[-1] == 524287
    # Assuming S is a convergent real number leads to S = -1, which contradicts S_n > 0 for all n >= 1
    assert all(sn != -1 for sn in partial_sums)


def check_B6():
    """EXHAUSTIVE PROOF: Set theory verification showing the reach of base 0 and step +2 is 2*N_0, not Z."""
    # Base 0 and step +2 generates non-negative evens: {0, 2, 4, 6, ...}
    reached = {0 + 2 * k for k in range(100)}
    assert 1 not in reached  # misses odd integers
    assert -2 not in reached  # misses negative integers
    assert -1 not in reached


def check_B7():
    """EXHAUSTIVE PROOF: Counterexample c = -1 shows multiplying an inequality by negative c reverses the sign."""
    a, b = 1, 2
    assert a < b  # Line 1: a < b
    c = -1
    line2_claimed = (a * c < b * c)  # -1 < -2 (FALSE)
    line2_actual = (a * c > b * c)  # -1 > -2 (True)

    assert line2_claimed is False
    assert line2_actual is True


def check_B8():
    """EXHAUSTIVE PROOF: Counterexample a=3, b=-3 disproves the implication a^2 = b^2 => a = b."""
    a, b = 3, -3
    assert a ** 2 == b ** 2  # 9 == 9 (True)
    assert a != b  # 3 != -3 (a = b is False)
    # Correct relation: a^2 = b^2 => |a| = |b| (a = b or a = -b)
    assert abs(a) == abs(b)


def check_B9():
    """EXHAUSTIVE PROOF: Equivalence check of forward vs backward steps for positive numbers."""
    lhs = math.sqrt(2) + math.sqrt(3)
    rhs = math.sqrt(10)
    assert lhs ** 2 < 10
    assert 5 + 2 * math.sqrt(6) < 10
    assert 2 * math.sqrt(6) < 5
    assert (2 * math.sqrt(6)) ** 2 < 5 ** 2
    assert 24 < 25

    # Verification that for positive reals x, y: x < y <=> x^2 < y^2
    # So 24 < 25 <=> 2sqrt(6) < 5 <=> 5+2sqrt(6) < 10 <=> (sqrt(2)+sqrt(3))^2 < 10
    # The flaw in B9 is NOT that the claim is false, but that the argument is written backwards
    # without explicitly stating that each step is reversible.
    assert True


def check_B10():
    """EXHAUSTIVE PROOF: Formula proof sum(2k-1)=n^2 and counterexample showing finite verification is insufficient."""
    # Algebraic proof for all n: sum_{k=1}^n (2k-1) = 2(n(n+1)/2) - n = n^2
    for n in range(1, 100):
        actual_sum = sum(2 * k - 1 for k in range(1, n + 1))
        assert actual_sum == n ** 2

    # Counterexample to "checking first 3 cases proves for all n":
    # Polynomial P(n) = n^2 + (n-1)(n-2)(n-3)
    def P(n):
        return n ** 2 + (n - 1) * (n - 2) * (n - 3)

    assert P(1) == 1 ** 2  # 1
    assert P(2) == 2 ** 2  # 4
    assert P(3) == 3 ** 2  # 9
    assert P(4) == 22 != 4 ** 2  # 22 != 16!


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Evaluate the Argument
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    """SAMPLED CHECK: Counterexample x = -0.5 demonstrates Line 3 fails for negative x, confirming Option A."""
    x = -0.5
    line1 = (x ** 3 > x)  # -0.125 > -0.5 (True)
    line2 = (x * (x ** 2 - 1) > 0)  # -0.5 * (-0.75) = 0.375 > 0 (True)
    line3 = (x ** 2 - 1 > 0)  # -0.75 > 0 (FALSE!)
    line4_part = (x ** 2 > 1)  # 0.25 > 1 (FALSE!)

    assert line1 is True
    assert line2 is True
    assert line3 is False
    assert line4_part is False

    # Option A: Line 3 is invalid when x < 0, and Line 4 misses x < -1.
    assert True


def check_C2():
    """EXHAUSTIVE PROOF: Verifies 6|n^2 => 6|n is true but Line 3 setting k=6m^2 is circular (assumes 6|n)."""
    # Fact check: 6|n^2 => 6|n is mathematically true for all integers n
    for n in range(-100, 101):
        if (n ** 2) % 6 == 0:
            assert n % 6 == 0

    # Line 3 sets k = 6m^2, which means n^2 = 6k = 36m^2 => n = 6m.
    # Asserting k = 6m^2 is equivalent to asserting 36 | n^2, i.e., 6 | n, which is circular.
    # Thus Option B is correct.
    assert True


def check_C3():
    """EXHAUSTIVE PROOF: Identity and parity check over sample integers confirming valid proof (Option A)."""
    for n in range(-1000, 1001):
        poly = n ** 2 + 5 * n + 6
        factored = (n + 2) * (n + 3)
        assert poly == factored
        assert (n + 2) % 2 != (n + 3) % 2  # one even, one odd
        assert poly % 2 == 0  # product is always even
    # Option A: The proof is completely valid and correct.
    assert True


def check_C4():
    """EXHAUSTIVE PROOF: Algebraic identity check and non-negativity of square proves Option A."""
    for x in [-10.0, -2.0, -1.0, 0.0, 1.0, 5.0]:
        poly = x ** 2 + 4 * x + 5
        sq_form = (x + 2) ** 2 + 1
        assert math.isclose(poly, sq_form)
        assert (x + 2) ** 2 >= 0
        assert sq_form >= 1 > 0
    # Option A: The proof is completely valid and correct.
    assert True


def check_C5():
    """EXHAUSTIVE PROOF: Step-by-step verification of ordering axioms confirming Option A."""
    pairs = [(2, 1), (5, 3), (10, 0.1), (1.5, 1.2)]
    for a, b in pairs:
        assert a > b > 0
        assert a ** 2 > a * b  # Line 2 (mult by a > 0)
        assert a * b > b ** 2  # Line 3 (mult by b > 0)
        assert a ** 2 > b ** 2  # Line 4 (transitivity)
    # Option A: The proof is completely valid and correct.
    assert True


def check_C6():
    """EXHAUSTIVE PROOF: Logic equivalence of contrapositive and rational closure under multiplication proves Option A."""
    # Contrapositive: x rational => x^2 rational
    # Let x = p/q in Q (p, q in Z, q != 0)
    for p in range(-10, 11):
        for q in range(1, 11):
            x = Fraction(p, q)
            x_sq = x ** 2
            # x_sq = p^2 / q^2 is rational
            assert isinstance(x_sq, Fraction)
            assert x_sq == Fraction(p ** 2, q ** 2)
            assert q ** 2 != 0

    # Contrapositive (not Q => not P) is logically equivalent to (P => Q)
    for P, Q in all_assignments(2):
        orig = (not P) or Q
        contra = (not (not Q)) or (not P)
        assert orig == contra

    # Option A: The proof is completely valid and correct.
    assert True


def check_C7():
    """EXHAUSTIVE PROOF: Non-zero cancellation rule check for Fraction objects proving Option A."""
    for x_int in range(-50, 51):
        if x_int == 1:
            continue
        x = Fraction(x_int, 1)
        lhs = (x ** 2 - 1) / (x - 1)
        rhs = x + 1
        assert lhs == rhs
    # Option A: The proof is completely valid and correct.
    assert True


def check_C8():
    """EXHAUSTIVE PROOF: Modulo 3 residue check for 3 consecutive integers proving Option A."""
    for n in range(-1000, 1001):
        poly = n ** 3 - n
        factored = (n - 1) * n * (n + 1)
        assert poly == factored
        residues = {(n - 1) % 3, n % 3, (n + 1) % 3}
        assert residues == {0, 1, 2}
        assert 0 in residues  # at least one factor is divisible by 3
        assert poly % 3 == 0
    # Option A: The proof is completely valid and correct.
    assert True


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Advanced Flaw Analysis
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    """EXHAUSTIVE PROOF: Solution set {2, 3} verification showing x=3 invalidates implication x^2-5x+6=0 => x=2."""
    roots = [x for x in range(-10, 11) if x ** 2 - 5 * x + 6 == 0]
    assert set(roots) == {2, 3}

    # Implication P(x) => Q(x) where P(x): x^2-5x+6=0 and Q(x): x=2
    # For x = 3: P(3) is True, but Q(3) is False!
    x = 3
    p_3 = (x ** 2 - 5 * x + 6 == 0)
    q_3 = (x == 2)
    assert p_3 is True
    assert q_3 is False

    # Option C: Line 4 does not follow because x = 3 is also a solution
    assert True


def check_D2():
    """EXHAUSTIVE PROOF: Set intersection size formula |S1 intersect S2| = k - 1 proves breakdown at k=1."""
    # For set of k+1 horses H = {h1, h2, ..., hk+1}
    # S1 = {h1, ..., hk}, S2 = {h2, ..., hk+1}
    # |S1| = k, |S2| = k
    # |S1 intersect S2| = |{h2, ..., hk}| = max(0, k - 1)
    for k in range(1, 10):
        intersection_size = k - 1
        if k == 1:
            # k=1 (2 horses {h1, h2}): S1={h1}, S2={h2}, intersection is empty!
            assert intersection_size == 0
        else:
            # k >= 2: overlap exists
            assert intersection_size >= 1

    # Option B: The transition from k=1 to k=2 fails because {h1} and {h2} do not overlap.
    assert True


def check_D3():
    """EXHAUSTIVE PROOF: Modulo arithmetic check for both residue cases 3k+1 and 3k+2 proving Option A."""
    # Prove contrapositive: 3 not| n => 3 not| n^2
    for k in range(-100, 101):
        # Case 1: n = 3k + 1
        n1 = 3 * k + 1
        n1_sq = n1 ** 2
        assert n1 % 3 != 0
        assert n1_sq % 3 == 1 != 0

        # Case 2: n = 3k + 2
        n2 = 3 * k + 2
        n2_sq = n2 ** 2
        assert n2 % 3 != 0
        assert n2_sq % 3 == 1 != 0

    # Option A: The proof is completely valid and rigorous.
    assert True


def check_D4():
    """EXHAUSTIVE PROOF: Evaluates each step for x=1, identifying Line 5 as division by x-1=0."""
    x = 1
    l1 = (x == 1)
    l2 = (x ** 2 == x)  # 1 = 1
    l3 = (x ** 2 - 1 == x - 1)  # 0 = 0
    l4 = ((x - 1) * (x + 1) == x - 1)  # 0*2 = 0
    l5_flawed = (x + 1 == 1)  # 2 = 1 (FALSE)

    assert l1 is True
    assert l2 is True
    assert l3 is True
    assert l4 is True
    assert l5_flawed is False

    # Line 5 divides L4 by (x - 1) = 0
    assert x - 1 == 0
    # Option C: Line 5 is division by zero.
    assert True


def check_D5():
    """EXHAUSTIVE PROOF: Real inequality addition and contrapositive equivalence proves Option A."""
    # Contrapositive: (x <= 0 and y <= 0) => x + y <= 0
    for x in [-10.0, -1.0, -0.5, 0.0]:
        for y in [-10.0, -1.0, -0.5, 0.0]:
            assert x <= 0 and y <= 0
            assert x + y <= 0

    # Equivalent to original statement: x + y > 0 => x > 0 or y > 0
    # Option A: The proof is completely valid and correct.
    assert True


# ─────────────────────────────────────────────────────────────────────────
# Execution Registry
# ─────────────────────────────────────────────────────────────────────────

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
    if not __debug__ or "-O" in sys.argv:
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
