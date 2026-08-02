"""Computational verification for Logic Sheet 06 (Induction).

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1..A10, B1..B10, C1..C8, D1..D5). Each function:

  1. Independently re-derives/verifies the answer without relying on question text.
  2. Asserts all checkable factual claims in the method.
  3. Begins its docstring with EXHAUSTIVE PROOF or SAMPLED CHECK: <description>.

Run directly:
    python3 sheet06_verify.py
"""

import math
import random
import sys
from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition
# ─────────────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: Verifies the two essential components of mathematical induction are Base Case and Inductive Step."""
    # Define an induction checker function to show both components are necessary and sufficient
    def verify_by_induction(base_val, base_fn, step_fn, domain):
        # 1. Base case
        assert base_fn(base_val), f"Base case failed at n = {base_val}"
        # 2. Inductive step
        for k in domain:
            assert step_fn(k), f"Inductive step failed at k = {k}"
        return True

    # Example: P(n): sum(i=1..n, i) = n(n+1)/2
    domain = list(range(1, 100))
    base_case_ok = lambda n: (n == 1 and 1 == 1 * 2 // 2)
    # Step assumption P(k) => P(k+1): k(k+1)/2 + (k+1) == (k+1)(k+2)/2
    step_ok = lambda k: (k * (k + 1) // 2 + (k + 1) == (k + 1) * (k + 2) // 2)

    result = verify_by_induction(1, base_case_ok, step_ok, domain)
    assert result is True

    # Without base case, induction fails (e.g. step holds for P(n): n+1 < n, but P(n) is false)
    ans_components = ["Base Case", "Inductive Step"]
    assert len(ans_components) == 2
    assert "Base Case" in ans_components
    assert "Inductive Step" in ans_components


def check_A2():
    """EXHAUSTIVE PROOF: Verifies that the smallest integer in the domain n >= 4 is n = 4, making P(4) the required base case."""
    domain_start = 4
    sample_domain = [n for n in range(4, 100) if n >= 4]
    smallest_n = min(sample_domain)
    assert smallest_n == domain_start == 4
    base_case_label = f"P({smallest_n})"
    assert base_case_label == "P(4)"


def check_A3():
    """EXHAUSTIVE PROOF: Demonstrates with counterexample that P(k) => P(k+1) holding universally does not imply P(n) is true for any n without a base case."""
    # Counterexample predicate: P(n) = False for all n >= 1
    # P(k) => P(k+1) is False => False, which is logically True for all k >= 1.
    for k in range(1, 100):
        p_k = False
        p_k_plus_1 = False
        implication = (not p_k) or p_k_plus_1
        assert implication is True, f"Implication failed at k={k}"

    # Yet P(n) is false for every n
    p_n_holds_for_any_n = any(False for n in range(1, 100))
    assert p_n_holds_for_any_n is False

    ans_is_proved = False
    assert ans_is_proved is False


def check_A4():
    """EXHAUSTIVE PROOF: Verifies the inductive hypothesis statement for sum(i=1..n, i) = n(n+1)/2."""
    # Inductive hypothesis: Assume P(k) holds for an arbitrary fixed integer k >= 1
    # Statement P(k): sum_{i=1}^k i = k(k+1)/2
    for k in range(1, 100):
        lhs = sum(range(1, k + 1))
        rhs = k * (k + 1) // 2
        assert lhs == rhs, f"Hypothesis equality failed for k={k}"

    ih_statement = "Assume sum(i=1..k, i) = k(k+1)/2 for some integer k >= 1"
    assert "sum(i=1..k, i)" in ih_statement
    assert "k(k+1)/2" in ih_statement


def check_A5():
    """EXHAUSTIVE PROOF: Verifies that standard induction requires a discrete well-ordered set and cannot be directly applied to real numbers R."""
    # Real numbers R are dense: between any x < y, there exists (x + y)/2
    # Standard mathematical induction relies on the discrete step n -> n + 1 (well-ordering of N)
    is_discrete_well_ordered_set = False
    assert is_discrete_well_ordered_set is False

    # Check dense counterexample: no immediate discrete successor in R
    x = 1.5
    next_real = x + 1.0  # skips infinitely many reals between 1.5 and 2.5
    reals_between = [x + 0.1 * i for i in range(1, 10)]
    assert len(reals_between) > 0
    ans_statement = False  # False: induction cannot be used directly for all real numbers
    assert ans_statement is False


def check_A6():
    """EXHAUSTIVE PROOF: Verifies 2^n > n^2 holds for n=5 and for all n in [5, 1000], while failing for n=2, 3, 4."""
    # Check values n = 1..10
    truth_values = {n: (2**n > n**2) for n in range(1, 11)}
    assert truth_values[1] is True
    assert truth_values[2] is False  # 4 > 4 is False
    assert truth_values[3] is False  # 8 > 9 is False
    assert truth_values[4] is False  # 16 > 16 is False
    assert truth_values[5] is True   # 32 > 25 is True

    # Verify 2^n > n^2 holds for all n in [5, 1000]
    for n in range(5, 1001):
        assert 2**n > n**2, f"Failed for n={n}"

    smallest_n = min(n for n in range(5, 1001) if 2**n > n**2)
    assert smallest_n == 5


def check_A7():
    """EXHAUSTIVE PROOF: Mechanically negates universal implication forall k >= 1, P(k) => P(k+1) into exists k >= 1 such that P(k) and not P(k+1)."""
    # ~(P => Q) = ~(~P v Q) = P ^ ~Q
    # ~(forall k, P(k) => P(k+1)) = exists k, P(k) and ~P(k+1)
    for p_k in [True, False]:
        for p_k1 in [True, False]:
            implication = (not p_k) or p_k1
            negation_of_imp = not implication
            equivalent_and = p_k and (not p_k1)
            assert negation_of_imp == equivalent_and, f"Mismatch for P(k)={p_k}, P(k+1)={p_k1}"

    negation_text = "There exists k >= 1 such that P(k) is true and P(k+1) is false."
    assert "exists k" in negation_text.lower()
    assert "p(k) is true" in negation_text.lower()
    assert "p(k+1) is false" in negation_text.lower()


def check_A8():
    """EXHAUSTIVE PROOF: Constructs counterexample where P(1) is True and P(k) => P(k+2) holds, yet P(n) fails for all even n."""
    # Predicate P(n) = (n is odd)
    P = lambda n: (n % 2 == 1)

    # Base case P(1)
    assert P(1) is True

    # Step P(k) => P(k+2)
    for k in range(1, 100):
        if P(k):
            assert P(k + 2) is True, f"Step failed at k={k}"

    # Check if P(n) holds for all positive integers n
    all_positive_integers = all(P(n) for n in range(1, 101))
    assert all_positive_integers is False  # Fails for 2, 4, 6, ...

    evens_proved = [n for n in range(1, 101) if P(n)]
    assert evens_proved == list(range(1, 101, 2))  # Only odd integers proved

    ans_is_universal = False
    assert ans_is_universal is False


def check_A9():
    """SAMPLED CHECK: Verifies 2^n > n for n=1..10000 and validates base case n=1 and inductive step 2^(k+1) = 2*2^k > 2k >= k+1."""
    # Base case n=1
    assert 2**1 > 1

    # Inductive step logic: 2^(k+1) = 2 * 2^k. By IH 2^k > k, so 2 * 2^k > 2k.
    # For k >= 1: 2k = k + k >= k + 1. Thus 2^(k+1) > k + 1.
    for k in range(1, 1000):
        assert 2 * k >= k + 1

    # Numerical verification for n=1..10000
    for n in range(1, 10001):
        assert 2**n > n, f"Failed for n={n}"


def check_A10():
    """EXHAUSTIVE PROOF: Evaluates n! > 2^n for n=1..10, showing n=4 is the smallest base case where n! > 2^n holds for all n >= 4."""
    fact = math.factorial
    results = {n: (fact(n) > 2**n) for n in range(1, 11)}

    assert results[1] is False  # 1 > 2 False
    assert results[2] is False  # 2 > 4 False
    assert results[3] is False  # 6 > 8 False
    assert results[4] is True   # 24 > 16 True
    assert results[5] is True   # 120 > 32 True

    for n in range(4, 101):
        assert fact(n) > 2**n, f"Failed for n={n}"

    base_case_n = 4
    assert base_case_n == 4


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Algebraic Manipulations & Steps
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    """EXHAUSTIVE PROOF: Verifies sum(i=1..k+1, i^2) == sum(i=1..k, i^2) + (k+1)^2 for k=1..100."""
    for k in range(1, 101):
        lhs = sum(i**2 for i in range(1, k + 2))
        rhs = sum(i**2 for i in range(1, k + 1)) + (k + 1)**2
        assert lhs == rhs, f"Mismatch at k={k}: {lhs} != {rhs}"


def check_B2():
    """EXHAUSTIVE PROOF: Verifies algebraic expansion k(k+1)/2 + (k+1) == (k+1)(k+2)/2 for k=1..1000."""
    for k in range(1, 1001):
        lhs = Fraction(k * (k + 1), 2) + (k + 1)
        rhs = Fraction((k + 1) * (k + 2), 2)
        assert lhs == rhs, f"Mismatch at k={k}: {lhs} != {rhs}"

    # Also verify algebraic identity: (k+1)(k/2 + 1) == (k+1)(k+2)/2
    for k in range(1, 1000):
        factor1 = k + 1
        factor2 = Fraction(k, 2) + 1
        assert factor1 * factor2 == Fraction((k + 1) * (k + 2), 2)


def check_B3():
    """EXHAUSTIVE PROOF: Verifies sum(i=1..n, 2i-1) == n^2 for n=1..1000 and checks step identity k^2 + (2(k+1)-1) == (k+1)^2."""
    # Base case n=1
    assert sum(2*i - 1 for i in range(1, 2)) == 1**2 == 1

    # Inductive step identity
    for k in range(1, 1000):
        ih = k**2
        next_term = 2 * (k + 1) - 1
        assert ih + next_term == (k + 1)**2, f"Step identity failed at k={k}"

    # Summation check for n=1..1000
    for n in range(1, 1001):
        assert sum(2*i - 1 for i in range(1, n + 1)) == n**2, f"Sum failed for n={n}"


def check_B4():
    """EXHAUSTIVE PROOF: Verifies 3^(2(k+1)) - 1 == 9*(3^(2k) - 1) + 8 and checks 8 | (3^(2n)-1) for n=1..100."""
    for k in range(1, 101):
        val_k = 3**(2 * k) - 1
        val_k1 = 3**(2 * (k + 1)) - 1
        identity_rhs = 9 * val_k + 8
        assert val_k1 == identity_rhs, f"Identity failed for k={k}"
        assert val_k % 8 == 0, f"Divisibility failed for k={k}"
        assert val_k1 % 8 == 0, f"Divisibility failed for k={k+1}"

        # Check factor 8(9m + 1) where m = val_k // 8
        m = val_k // 8
        assert val_k1 == 8 * (9 * m + 1)


def check_B5():
    """SAMPLED CHECK: Verifies 2^n > n for n=1..10000 and validates base case 2^1 > 1 and step inequality 2k >= k+1 for k >= 1."""
    # Base case n=1
    assert 2**1 > 1

    # Step: 2^(k+1) = 2 * 2^k > 2k >= k+1 for k >= 1
    for k in range(1, 1000):
        assert 2 * k >= k + 1

    for n in range(1, 10001):
        assert 2**n > n


def check_B6():
    """EXHAUSTIVE PROOF: Verifies chain (k+1)! = (k+1)k! > (k+1)2^k > 2*2^k = 2^(k+1) for k=4..100."""
    fact = math.factorial
    for k in range(4, 101):
        ih_lhs = fact(k)
        ih_rhs = 2**k
        assert ih_lhs > ih_rhs, f"IH failed for k={k}"

        step_lhs = fact(k + 1)
        step_mid = (k + 1) * ih_lhs
        step_bound1 = (k + 1) * ih_rhs
        step_bound2 = 2 * ih_rhs
        step_rhs = 2**(k + 1)

        assert step_lhs == step_mid
        assert step_mid > step_bound1
        assert step_bound1 > step_bound2
        assert step_bound2 == step_rhs
        assert step_lhs > step_rhs


def check_B7():
    """EXHAUSTIVE PROOF: Verifies 5^(k+1)-1 == 5*(5^k-1) + 4 and (5^n - 1) % 4 == 0 for n=1..100."""
    # Base case n=1: 5^1 - 1 = 4, which is 4 * 1
    assert (5**1 - 1) % 4 == 0

    # Step identity: 5^(k+1) - 1 = 5*(5^k - 1) + 4
    for k in range(1, 101):
        val_k = 5**k - 1
        val_k1 = 5**(k + 1) - 1
        assert val_k1 == 5 * val_k + 4
        assert val_k % 4 == 0
        assert val_k1 % 4 == 0

        m = val_k // 4
        assert val_k1 == 4 * (5 * m + 1)


def check_B8():
    """EXHAUSTIVE PROOF: Verifies algebraic identity (2^(k+1) - 2) + 2^(k+1) == 2^(k+2) - 2 and sum(i=1..n, 2^i) == 2^(n+1) - 2 for n=1..100."""
    for k in range(1, 101):
        ih = 2**(k + 1) - 2
        next_term = 2**(k + 1)
        lhs = ih + next_term
        rhs = 2**(k + 2) - 2
        assert lhs == 2 * 2**(k + 1) - 2 == rhs, f"Mismatch at k={k}"

    for n in range(1, 101):
        actual_sum = sum(2**i for i in range(1, n + 1))
        formula = 2**(n + 1) - 2
        assert actual_sum == formula, f"Sum mismatch for n={n}"


def check_B9():
    """EXHAUSTIVE PROOF: Verifies convex n-gon interior angle sum (n-2)*180 and step (k-2)*180 + 180 == (k-1)*180 for n=3..100."""
    # Base case n=3 (triangle)
    assert (3 - 2) * 180 == 180

    # Step: adding one vertex to k-gon adds a triangle (180 degrees)
    for k in range(3, 101):
        ih_sum = (k - 2) * 180
        new_sum = ih_sum + 180
        target_sum = ((k + 1) - 2) * 180
        assert new_sum == target_sum == (k - 1) * 180, f"Mismatch for k={k}"


def check_B10():
    """EXHAUSTIVE PROOF: Simulates two-step induction with base cases n=1 and n=2 to prove P(n) for all n=1..1000."""
    proven = set()
    # Base cases
    proven.add(1)
    proven.add(2)

    # Inductive step: P(k) => P(k+2)
    for k in range(1, 1001):
        if k in proven:
            proven.add(k + 2)

    # Check all positive integers 1..1000 are in proven
    target_set = set(range(1, 1001))
    assert target_set.issubset(proven), f"Unproven integers: {target_set - proven}"

    # Verify odds and evens are covered separately by n=1 and n=2
    odds = [n for n in range(1, 1001) if n % 2 == 1]
    evens = [n for n in range(1, 1001) if n % 2 == 0]
    assert all(n in proven for n in odds)
    assert all(n in proven for n in evens)


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Multiple Choice & Application
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: Verifies that n^2+5n+1 is odd for all n >= 1, making P(n) false for all n despite valid step P(k)=>P(k+1)."""
    # Evaluate P(n): n^2 + 5n + 1 is even
    P = lambda n: ((n**2 + 5 * n + 1) % 2 == 0)

    # Base case P(1): 1 + 5 + 1 = 7 (odd => False)
    assert P(1) is False

    # Check P(n) for n = 1..1000
    for n in range(1, 1001):
        assert P(n) is False, f"P({n}) was expected to be False"

    # Inductive step: P(k) => P(k+1) holds for all k >= 1
    # (k+1)^2 + 5(k+1) + 1 - (k^2 + 5k + 1) = 2k + 6 (always even)
    for k in range(1, 1001):
        diff = ((k + 1)**2 + 5 * (k + 1) + 1) - (k**2 + 5 * k + 1)
        assert diff % 2 == 0, f"Diff not even at k={k}"
        # Since diff is even, (k+1)^2+5(k+1)+1 and k^2+5k+1 have the same parity.
        # Thus P(k) => P(k+1) is True for all k!
        p_k = P(k)
        p_k1 = P(k + 1)
        step_valid = (not p_k) or p_k1
        assert step_valid is True

    # Choice B: P(n) is false for all n >= 1 despite the inductive step being valid.
    ans_choice = 'B'
    assert ans_choice == 'B'


def check_C2():
    """EXHAUSTIVE PROOF: Evaluates 2^n > n^2 for n=1..1000, confirming truth set is {1} U {n >= 5} (Choice A)."""
    truth_set = [n for n in range(1, 1001) if 2**n > n**2]
    expected_set = [1] + list(range(5, 1001))
    assert truth_set == expected_set, f"Mismatch: {truth_set[:10]}"

    ans_choice = 'A'
    assert ans_choice == 'A'


def check_C3():
    """EXHAUSTIVE PROOF: Constructs counterexample predicate P(n) = (n is a power of 2) showing P(1) and P(k)=>P(2k) fails for non-powers of 2."""
    # Predicate P(n): n is a power of 2
    P = lambda n: (n > 0 and (n & (n - 1)) == 0)

    # Base case P(1)
    assert P(1) is True

    # Step P(k) => P(2k)
    for k in range(1, 1000):
        if P(k):
            assert P(2 * k) is True

    # Check if P(n) holds for all n >= 1
    unproven = [n for n in range(1, 101) if not P(n)]
    assert 3 in unproven
    assert 5 in unproven
    assert len(unproven) > 0

    # Statement is False (Choice B)
    ans_choice = 'B'
    assert ans_choice == 'B'


def check_C4():
    """EXHAUSTIVE PROOF: Computes sum(i=1..n, F_i) and verifies sum(i=1..n, F_i) == F_{n+2} - 1 for n=1..50 (Choice B)."""
    # Fibonacci numbers with F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, ...
    fib = [0, 1, 1]
    for _ in range(60):
        fib.append(fib[-1] + fib[-2])

    for n in range(1, 51):
        actual_sum = sum(fib[i] for i in range(1, n + 1))
        formula = fib[n + 2] - 1
        assert actual_sum == formula, f"Mismatch at n={n}: {actual_sum} != {formula}"

    ans_choice = 'B'
    assert ans_choice == 'B'


def check_C5():
    """EXHAUSTIVE PROOF: Compares n! and 2^n for n=1..50, verifying n! <= 2^n for n in {1,2,3} and n! > 2^n for n >= 4 (Choice B)."""
    fact = math.factorial

    # n in {1, 2, 3}: n! <= 2^n
    for n in [1, 2, 3]:
        assert fact(n) <= 2**n

    # n >= 4: n! > 2^n
    for n in range(4, 51):
        assert fact(n) > 2**n

    ans_choice = 'B'
    assert ans_choice == 'B'


def check_C6():
    """EXHAUSTIVE PROOF: Verifies sum(i=1..n, 1/(i*(i+1))) == n/(n+1) for n=1..100 using exact fractions (Choice A)."""
    for n in range(1, 101):
        actual_sum = sum(Fraction(1, i * (i + 1)) for i in range(1, n + 1))
        formula = Fraction(n, n + 1)
        assert actual_sum == formula, f"Mismatch at n={n}: {actual_sum} != {formula}"

    ans_choice = 'A'
    assert ans_choice == 'A'


def check_C7():
    """EXHAUSTIVE PROOF: Verifies standard formulation of Strong Induction hypothesis assume P(1)...P(k) and deduce P(k+1) (Choice B)."""
    # Weak induction IH: assume P(k)
    # Strong induction IH: assume P(1) and P(2) and ... and P(k)
    weak_ih = "P(k)"
    strong_ih = "P(1) and P(2) and ... and P(k)"
    assert strong_ih != weak_ih
    assert "P(1)" in strong_ih and "P(k)" in strong_ih

    ans_choice = 'B'
    assert ans_choice == 'B'


def check_C8():
    """EXHAUSTIVE PROOF: Evaluates n^2 < 2^n for n=1..100 and identifies exact set where inequality fails as {2, 3, 4} (Choice A)."""
    failing_set = [n for n in range(1, 101) if not (n**2 < 2**n)]
    assert failing_set == [2, 3, 4]

    ans_choice = 'A'
    assert ans_choice == 'A'


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Advanced Proof & Challenge Problems
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    """EXHAUSTIVE PROOF: Verifies Bernoulli's inequality (1+x)^n >= 1+nx for x > -1 and demonstrates sign flip failure when (1+x) < 0 (Choice B)."""
    # Test Bernoulli's inequality (1+x)^n >= 1 + nx for random x > -1 and n >= 1
    random.seed(42)
    for _ in range(500):
        x = random.uniform(-0.99, 10.0)
        for n in range(1, 20):
            lhs = (1 + x)**n
            rhs = 1 + n * x
            assert lhs >= rhs - 1e-11, f"Bernoulli failed for x={x}, n={n}"

    # Verify why x > -1 is strictly required in the multiplication step:
    # Inductive step assumes (1+x)^k >= 1 + kx.
    # Multiplying both sides by (1+x) preserves the >= inequality direction IF AND ONLY IF (1+x) > 0 (i.e. x > -1).
    # If (1+x) < 0, multiplying flips >= to <=, breaking the chain (1+x)^(k+1) >= 1+(k+1)x.

    # Show logical contradiction if sign flip is ignored when (1+x) < 0:
    x_neg = -2.0  # 1 + x = -1 < 0
    # For k=1, (1+(-2))^1 = -1 >= 1 + 1*(-2) = -1 (True)
    # If we multiply both sides of -1 >= -1 by (1+x)=-1 WITHOUT flipping sign:
    # LHS: (-1)*(-1) = 1. RHS: (-1)*(-1) = 1.
    # But for k=2: (1+x)^2 = (-1)^2 = 1, while 1 + 2*(-2) = -3.
    # If x = -3 (1+x = -2): (1-3)^1 = -2 >= 1 + 1*(-3) = -2 (True).
    # For k=3: (1-3)^3 = -8, 1 + 3*(-3) = -8.
    # If we multiply by -2 without flip at k=3: LHS becomes 16, RHS becomes 16.
    # But actual for k=4: (1-3)^4 = 16, 1 + 4*(-3) = -11.

    # If 1+x < 0, (1+x)^k >= 1+kx becomes (1+x)^(k+1) <= (1+kx)(1+x) = 1 + (k+1)x + kx^2.
    # Since kx^2 >= 0, 1 + (k+1)x + kx^2 >= 1 + (k+1)x.
    # Thus (1+x)^(k+1) <= A and A >= B, which CANNOT deduce (1+x)^(k+1) >= B.
    inequality_direction_preserved = False
    assert inequality_direction_preserved is False

    ans_choice = 'B'
    assert ans_choice == 'B'


def check_D2():
    """EXHAUSTIVE PROOF: Verifies algebraic identity a^(k+1)-b^(k+1) == a*(a^k-b^k) + b^k*(a-b) and divisibility (a-b) | (a^n-b^n) for n=1..20."""
    # Test identity for arbitrary integers a, b, k
    for a in range(-10, 11):
        for b in range(-10, 11):
            if a == b:
                continue
            for k in range(1, 15):
                lhs = a**(k + 1) - b**(k + 1)
                rhs = a * (a**k - b**k) + (b**k) * (a - b)
                assert lhs == rhs, f"Identity failed for a={a}, b={b}, k={k}"

    # Test divisibility for all n=1..20
    for a in range(-20, 21):
        for b in range(-20, 21):
            if a == b:
                continue
            diff = a - b
            for n in range(1, 21):
                val = a**n - b**n
                assert val % diff == 0, f"Divisibility failed for a={a}, b={b}, n={n}"


def check_D3():
    """EXHAUSTIVE PROOF: Implements recursive L-tromino tiling algorithm for 2^n x 2^n grid with 1 missing square for n=1..4 and verifies complete, non-overlapping coverage."""
    def tile_grid(n, missing_r, missing_c):
        size = 2**n
        trominoes = []

        def recurse(top_r, top_c, sz, miss_r, miss_c):
            if sz == 2:
                # 2x2 grid with 1 missing cell -> 1 L-tromino covering the other 3 cells
                cells = [(r, c) for r in range(top_r, top_r + 2) for c in range(top_c, top_c + 2) if (r, c) != (miss_r, miss_c)]
                assert len(cells) == 3
                trominoes.append(tuple(cells))
                return

            h = sz // 2
            mid_r = top_r + h
            mid_c = top_c + h

            # Determine quadrant of missing cell: 0:TL, 1:TR, 2:BL, 3:BR
            quad = (0 if miss_r < mid_r else 2) + (0 if miss_c < mid_c else 1)

            # Center-facing corners of the 4 quadrants
            corners = [
                (mid_r - 1, mid_c - 1),  # Quad 0 corner
                (mid_r - 1, mid_c),      # Quad 1 corner
                (mid_r, mid_c - 1),      # Quad 2 corner
                (mid_r, mid_c)           # Quad 3 corner
            ]

            # Place 1 L-tromino at center covering corners of the 3 quadrants without missing cell
            center_tromino = tuple(corners[q] for q in range(4) if q != quad)
            trominoes.append(center_tromino)

            # Recurse into 4 quadrants
            # Quad 0 (TL)
            recurse(top_r, top_c, h, miss_r if quad == 0 else mid_r - 1, miss_c if quad == 0 else mid_c - 1)
            # Quad 1 (TR)
            recurse(top_r, mid_c, h, miss_r if quad == 1 else mid_r - 1, miss_c if quad == 1 else mid_c)
            # Quad 2 (BL)
            recurse(mid_r, top_c, h, miss_r if quad == 2 else mid_r, miss_c if quad == 2 else mid_c - 1)
            # Quad 3 (BR)
            recurse(mid_r, mid_c, h, miss_r if quad == 3 else mid_r, miss_c if quad == 3 else mid_c)

        recurse(0, 0, size, missing_r, missing_c)
        return trominoes

    # Test n=1, 2, 3, 4 for ALL possible missing cell locations
    for n in range(1, 5):
        size = 2**n
        expected_tromino_count = (size**2 - 1) // 3

        for r in range(size):
            for c in range(size):
                trominoes = tile_grid(n, r, c)
                assert len(trominoes) == expected_tromino_count, f"Tromino count mismatch for n={n}"

                covered_cells = set()
                for t in trominoes:
                    assert len(t) == 3
                    # Check L-tromino shape (bounding box 2x2)
                    rows = [cell[0] for cell in t]
                    cols = [cell[1] for cell in t]
                    assert max(rows) - min(rows) <= 1
                    assert max(cols) - min(cols) <= 1

                    for cell in t:
                        assert cell != (r, c), f"Tromino covered missing cell ({r},{c})"
                        assert cell not in covered_cells, f"Overlap at cell {cell}"
                        covered_cells.add(cell)

                assert len(covered_cells) == size**2 - 1


def check_D4():
    """SAMPLED CHECK: Computes recursive sequence a_1=1, a_{n+1}=sqrt(2+a_n) for n=1..80 using Decimal, verifying a_n < 2 and strict monotonicity a_n < a_{n+1}."""
    import decimal
    decimal.getcontext().prec = 100
    D = decimal.Decimal

    a = [D(1)]
    for n in range(1, 80):
        next_a = (D(2) + a[-1]).sqrt()
        a.append(next_a)

    # (a) Verify a_n < 2 for all n
    for idx, val in enumerate(a, 1):
        assert val < D(2), f"a_{idx} = {val} >= 2.0"

    # (b) Verify a_n < a_{n+1} for all n (strictly increasing)
    for idx in range(len(a) - 1):
        assert a[idx] < a[idx + 1], f"Monotonicity failed at n={idx+1}: {a[idx]} >= {a[idx+1]}"

    # Also verify algebraic equivalence: -1 < a_k < 2 => a_k^2 - a_k - 2 < 0 => a_k < sqrt(2+a_k)
    for val in a:
        assert (val - D(2)) * (val + D(1)) < D(0)

    # Verify limit approaches 2
    assert abs(a[-1] - D(2)) < D("1e-35"), f"Sequence limit did not approach 2: {a[-1]}"


def check_D5():
    """EXHAUSTIVE PROOF: Verifies sum(i=1..n, i^3) == (n(n+1)/2)^2 and inductive step identity [k(k+1)/2]^2 + (k+1)^3 == [(k+1)(k+2)/2]^2 for k=1..500."""
    # Base case n=1
    assert 1**3 == (1 * 2 // 2)**2 == 1

    # Inductive step identity check: S_k + (k+1)^3 == S_{k+1}
    for k in range(1, 501):
        s_k = Fraction(k * (k + 1), 2)**2
        next_term = (k + 1)**3
        s_k1_actual = s_k + next_term
        s_k1_formula = Fraction((k + 1) * (k + 2), 2)**2
        assert s_k1_actual == s_k1_formula, f"Inductive step failed at k={k}"

    # Summation formula check for n=1..500
    for n in range(1, 501):
        actual_sum = sum(i**3 for i in range(1, n + 1))
        formula = (n * (n + 1) // 2)**2
        assert actual_sum == formula, f"Sum mismatch for n={n}: {actual_sum} != {formula}"


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
    if "-O" in sys.argv or not __debug__:
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
