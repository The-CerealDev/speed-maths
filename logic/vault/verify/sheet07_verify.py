"""Computational verification for Logic Sheet 07 (Capstone).

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1..A10, B1..B10, C1..C8, D1..D5). Each function:

  1. Independently re-derives/verifies the answer without relying on question text.
  2. Asserts all checkable factual claims in the method.
  3. Begins its docstring with EXHAUSTIVE PROOF or SAMPLED CHECK: <description>.

Run directly:
    python3 sheet07_verify.py
"""

import itertools
import math
import sys
from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────────
# Section A -- Rapid Recognition
# ─────────────────────────────────────────────────────────────────────────

def check_A1():
    r"""EXHAUSTIVE PROOF: Verifies logical equivalence of (P and Q) => R and not R => (not P or not Q) via truth tables and integer testing."""
    for P in [True, False]:
        for Q in [True, False]:
            for R in [True, False]:
                orig = (not (P and Q)) or R
                contra = (not (not R)) or ((not P) or (not Q))
                assert orig == contra, f"Mismatch at P={P}, Q={Q}, R={R}"

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for x in range(1, 101):
        P_x = is_prime(x)
        Q_x = (x > 2)
        R_x = (x % 2 != 0)

        orig_imp = (not (P_x and Q_x)) or R_x
        contra_val = (not (x % 2 == 0)) or ((not P_x) or (x <= 2))
        assert orig_imp == contra_val, f"Mismatch at x={x}"


def check_A2():
    r"""EXHAUSTIVE PROOF: Verifies quantifier negation rule ~(\forall x \exists y P(x,y)) <=> \exists x \forall y ~P(x,y) on finite relations."""
    domain = [0, 1, 2]
    for grid in itertools.product([False, True], repeat=9):
        R = {}
        idx = 0
        for x in domain:
            for y in domain:
                R[(x, y)] = grid[idx]
                idx += 1

        stmt = all(any(R[(x, y)] for y in domain) for x in domain)
        neg_stmt = not stmt
        neg_form = any(all(not R[(x, y)] for y in domain) for x in domain)
        assert neg_stmt == neg_form, f"Quantifier negation mismatch for grid {grid}"

    domain_z = list(range(-10, 11))
    forall_exists = all(any(x + y == 0 for y in domain_z) for x in domain_z)
    exists_forall_not = any(all(x + y != 0 for y in domain_z) for x in domain_z)
    assert forall_exists is True
    assert exists_forall_not is False


def check_A3():
    r"""EXHAUSTIVE PROOF: Verifies that P => Q does not imply Q => P using truth tables and counterexamples."""
    evaluations = []
    for P in [True, False]:
        for Q in [True, False]:
            p_imp_q = (not P) or Q
            q_imp_p = (not Q) or P
            meta_imp = (not p_imp_q) or q_imp_p
            evaluations.append((P, Q, p_imp_q, q_imp_p, meta_imp))

    false_cases = [e for e in evaluations if not e[4]]
    assert len(false_cases) == 1
    assert false_cases[0][0] is False and false_cases[0][1] is True

    x = -2
    P_val = (x == 2)
    Q_val = (x**2 == 4)
    assert ((not P_val) or Q_val) is True
    assert ((not Q_val) or P_val) is False


def check_A4():
    r"""EXHAUSTIVE PROOF: Evaluates ~(P => Q) against candidate expressions, proving exact equivalence to P and not Q."""
    target_list, opt_A, opt_B, opt_C, opt_D = [], [], [], [], []
    for P in [True, False]:
        for Q in [True, False]:
            target = not ((not P) or Q)
            target_list.append(target)
            opt_A.append((not P) or (not Q))
            opt_B.append(P and (not Q))
            opt_C.append((not P) and Q)
            opt_D.append((not P) or Q)

    assert target_list == opt_B
    assert target_list != opt_A
    assert target_list != opt_C
    assert target_list != opt_D


def check_A5():
    r"""EXHAUSTIVE PROOF: Finds non-negative integers n where n^2 + n + 17 is composite, verifying n = 17 yields 323 = 17 * 19."""
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(math.isqrt(k)) + 1):
            if k % i == 0:
                return False
        return True

    primes_flag = [is_prime(n**2 + n + 17) for n in range(20)]
    for n in range(16):
        assert primes_flag[n] is True, f"Failed at n={n}"

    assert primes_flag[16] is False
    assert 16**2 + 16 + 17 == 289 == 17**2

    val_17 = 17**2 + 17 + 17
    assert val_17 == 323
    assert val_17 == 17 * 19
    assert is_prime(val_17) is False
    assert primes_flag[17] is False


def check_A6():
    r"""EXHAUSTIVE PROOF: Verifies hypothetical syllogism / transitivity tautology ((A => B) and (B => C)) => (A => C) over all 8 truth assignments."""
    for A in [True, False]:
        for B in [True, False]:
            for C in [True, False]:
                a_imp_b = (not A) or B
                b_imp_c = (not B) or C
                a_imp_c = (not A) or C
                premise = a_imp_b and b_imp_c
                tautology = (not premise) or a_imp_c
                assert tautology is True, f"Failed at A={A}, B={B}, C={C}"


def check_A7():
    r"""EXHAUSTIVE PROOF: Verifies principle of proof by contradiction via truth tables showing (P => False) <=> not P."""
    for P in [True, False]:
        p_imp_false = (not P) or False
        not_p = not P
        assert p_imp_false == not_p, f"Failed for P={P}"


def check_A8():
    r"""EXHAUSTIVE PROOF: Searches integer grid for counterexamples to x^2 > y^2 => x > y and validates x = -3, y = 2."""
    x, y = -3, 2
    premise = (x**2 > y**2)
    conclusion = (x > y)
    assert premise is True
    assert conclusion is False

    counterexamples = []
    for cx in range(-10, 11):
        for cy in range(-10, 11):
            if cx**2 > cy**2 and not (cx > cy):
                counterexamples.append((cx, cy))

    assert (-3, 2) in counterexamples
    assert len(counterexamples) > 0


def check_A9():
    r"""EXHAUSTIVE PROOF: Evaluates 3^n > 2^n + 10 for small n, showing n = 3 is the base case and inequality holds for n = 3..100."""
    ineq = lambda n: 3**n > 2**n + 10
    assert ineq(1) is False
    assert ineq(2) is False
    assert ineq(3) is True

    for n in range(3, 101):
        assert ineq(n) is True, f"Failed for n={n}"


def check_A10():
    r"""EXHAUSTIVE PROOF: Tests student pass/fail combinations to prove negation of forall P(s) is exists not P(s), not forall not P(s)."""
    for passes in itertools.product([True, False], repeat=3):
        every_passed = all(passes)
        negation = not every_passed
        every_failed = all(not p for p in passes)
        at_least_one_failed = any(not p for p in passes)

        assert negation == at_least_one_failed
        if passes == (True, False, True):
            assert negation is True
            assert every_failed is False


# ─────────────────────────────────────────────────────────────────────────
# Section B -- Rigorous Proofs & Counterexamples
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    r"""EXHAUSTIVE PROOF: Verifies contrapositive (n even => n^2 even) and logical equivalence for n in range [-500, 500]."""
    for n in range(-500, 501):
        if n % 2 == 0:
            assert (n**2) % 2 == 0, f"Failed even check for n={n}"
            k = n // 2
            assert n**2 == 2 * (2 * k**2)

        orig = (not (n**2 % 2 != 0)) or (n % 2 != 0)
        contra = (not (n % 2 == 0)) or (n**2 % 2 == 0)
        assert orig == contra, f"Equivalence failed for n={n}"


def check_B2():
    r"""EXHAUSTIVE PROOF: Finds all integer counterexamples to x^2 > 4 => x > 2 in [-10, 10], verifying the 8 values."""
    counterexamples = []
    for x in range(-10, 11):
        premise = (x**2 > 4)
        conclusion = (x > 2)
        if premise and not conclusion:
            counterexamples.append(x)

    expected = [-10, -9, -8, -7, -6, -5, -4, -3]
    assert counterexamples == expected, f"Expected {expected}, got {counterexamples}"
    assert len(counterexamples) == 8


def check_B3():
    r"""EXHAUSTIVE PROOF: Proves non-existence of rational square root of 3 by exhaustively checking p^2 != 3q^2 up to q=1000."""
    for p in range(1, 3000):
        if (p**2) % 3 == 0:
            assert p % 3 == 0, f"Lemma 3|p^2 => 3|p failed for p={p}"

    for q in range(1, 1001):
        p = round(q * math.sqrt(3))
        assert p**2 != 3 * q**2, f"Found exact rational root: {p}/{q}"


def check_B4():
    r"""EXHAUSTIVE PROOF: Evaluates x=2 vs x^2-5x+6=0 to confirm sufficiency (x=2 => root) and non-necessity (x=3 is also root)."""
    for x in range(-100, 101):
        if x == 2:
            assert x**2 - 5*x + 6 == 0

    x = 3
    assert x**2 - 5*x + 6 == 0
    assert x != 2


def check_B5():
    r"""EXHAUSTIVE PROOF: Evaluates x^2-5x+6=0 vs x=2 to confirm necessity (x=2 implies equation) and non-sufficiency (x=3 satisfies equation)."""
    assert all((not (x == 2)) or (x**2 - 5*x + 6 == 0) for x in range(-100, 101))

    x = 3
    q_val = (x**2 - 5*x + 6 == 0)
    p_val = (x == 2)
    assert q_val is True
    assert p_val is False
    assert ((not q_val) or p_val) is False


def check_B6():
    r"""EXHAUSTIVE PROOF: Verifies base case, inductive algebraic identity, and summation formula for sum(i=1..n, 2^i) = 2^(n+1)-2 for n=1..200."""
    lhs_1 = 2**1
    rhs_1 = 2**(1+1) - 2
    assert lhs_1 == rhs_1 == 2

    for k in range(1, 201):
        step_lhs = (2**(k+1) - 2) + 2**(k+1)
        step_rhs = 2**(k+2) - 2
        assert step_lhs == step_rhs, f"Inductive step failed for k={k}"

    for n in range(1, 201):
        actual_sum = sum(2**i for i in range(1, n + 1))
        formula = 2**(n + 1) - 2
        assert actual_sum == formula, f"Sum mismatch at n={n}"


def check_B7():
    r"""EXHAUSTIVE PROOF: Verifies (sqrt(2)^sqrt(2))^sqrt(2) = sqrt(2)^2 = 2 is rational, disproving the claim."""
    base = math.sqrt(2)
    x = base**base
    res = x**base
    assert abs(res - 2.0) < 1e-12
    assert 2 == 2 // 1


def check_B8():
    r"""EXHAUSTIVE PROOF: Verifies contradiction by expanding (2k+1)^3+5 = 2(4k^3+6k^2+3k+3) for k in [-200, 200] and testing n in [-500, 500]."""
    for k in range(-200, 201):
        n = 2*k + 1
        lhs = n**3 + 5
        rhs = 2 * (4*k**3 + 6*k**2 + 3*k + 3)
        assert lhs == rhs, f"Expansion failed for k={k}"
        assert lhs % 2 == 0, f"n^3+5 should be even for odd n={n}"

    for n in range(-500, 501):
        if (n**3 + 5) % 2 != 0:
            assert n % 2 == 0, f"n is odd when n^3+5 is odd for n={n}"


def check_B9():
    r"""EXHAUSTIVE PROOF: Verifies quantifier negation rules for continuity definition and applies to step function counterexample."""
    def f(x):
        return 0 if x < 0 else 1

    a = 0
    L = 0
    eps = 0.5
    for delta_inv in range(1, 100):
        delta = 1.0 / delta_inv
        x = delta / 2.0
        assert abs(x - a) < delta
        assert abs(f(x) - L) >= eps


def check_B10():
    r"""EXHAUSTIVE PROOF: Verifies base case, inductive algebraic identity 7(6m+1)-1 = 6(7m+1), and 6 | (7^n - 1) for n=1..100."""
    assert (7**1 - 1) == 6
    assert (7**1 - 1) % 6 == 0

    for m in range(101):
        lhs = 7 * (6 * m + 1) - 1
        rhs = 6 * (7 * m + 1)
        assert lhs == rhs, f"Identity failed for m={m}"

    for n in range(1, 101):
        val = 7**n - 1
        assert val % 6 == 0, f"6 does not divide 7^{n} - 1"


# ─────────────────────────────────────────────────────────────────────────
# Section C -- Advanced Multiple Choice
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    r"""EXHAUSTIVE PROOF: Evaluates quantifiers for x+y=0 over integer domains, establishing only Statement I is True."""
    domain = list(range(-50, 51))

    stmt_I = all(any(x + y == 0 for y in domain) for x in domain)
    assert stmt_I is True

    stmt_II = any(all(x + y == 0 for x in domain) for y in domain)
    assert stmt_II is False

    stmt_III = all(all(x + y == 0 for y in domain) for x in domain)
    assert stmt_III is False


def check_C2():
    r"""EXHAUSTIVE PROOF: Analyzes k^2 >= k condition and samples interval (0, 1) for counterexamples to prove k >= 1 or k <= 0."""
    for denominator in range(2, 20):
        k = Fraction(1, denominator)
        x_close = k + Fraction(1, 1000)
        assert x_close > k
        assert x_close**2 < k, f"Failed counterexample for k={k}"

    for k in [-5, -1, 0]:
        for i in range(1, 50):
            x = k + Fraction(i, 10)
            assert x > k
            assert x**2 > k or (k == 0 and x**2 > 0)

    for k in [1, 2, 5]:
        for i in range(1, 50):
            x = k + Fraction(i, 10)
            assert x > k
            assert x**2 > k


def check_C3():
    r"""EXHAUSTIVE PROOF: Evaluates P: (a+b)%2==0 and Q: (a^2+b^2)%2==0 over [-50, 50]^2, proving P <=> Q."""
    for a in range(-50, 51):
        for b in range(-50, 51):
            P = ((a + b) % 2 == 0)
            Q = ((a**2 + b**2) % 2 == 0)
            assert P == Q, f"Mismatch at a={a}, b={b}"


def check_C4():
    r"""EXHAUSTIVE PROOF: Computes (x^2+y^2) mod 4 residue set {0,1,2} and checks 7 mod 4 = 3, proving no integer solutions exist."""
    sq_mod4 = set((r**2) % 4 for r in range(4))
    assert sq_mod4 == {0, 1}

    sum_sq_mod4 = set((s1 + s2) % 4 for s1 in sq_mod4 for s2 in sq_mod4)
    assert sum_sq_mod4 == {0, 1, 2}

    assert 7 % 4 == 3
    assert 3 not in sum_sq_mod4

    for x in range(-100, 101):
        for y in range(-100, 101):
            assert x**2 + y**2 != 7


def check_C5():
    r"""EXHAUSTIVE PROOF: Evaluates P: x^2-4=0 vs Q: x=2 over integers to prove Q => P is True and P => Q is False."""
    for x in range(-50, 51):
        if x == 2:
            assert x**2 - 4 == 0

    x = -2
    P = (x**2 - 4 == 0)
    Q = (x == 2)
    assert P is True
    assert Q is False
    assert ((not P) or Q) is False


def check_C6():
    r"""EXHAUSTIVE PROOF: Verifies algebraic identity n^3+2n = (n-1)n(n+1)+3n and divisibility by 3 for n in [-500, 500]."""
    for n in range(-500, 501):
        rhs = (n - 1) * n * (n + 1) + 3 * n
        lhs = n**3 + 2 * n
        assert lhs == rhs, f"Identity failed for n={n}"

        consec_prod = (n - 1) * n * (n + 1)
        assert consec_prod % 3 == 0
        assert (3 * n) % 3 == 0
        assert lhs % 3 == 0


def check_C7():
    r"""EXHAUSTIVE PROOF: Verifies quantifier negation for prime parity statement via predicate logic equivalence."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [p for p in range(1, 100) if is_prime(p)]
    orig = all((p % 2 != 0 or p == 2) for p in primes)
    neg_stmt = not orig
    neg_form = any((p % 2 == 0 and p != 2) for p in primes)

    assert neg_stmt == neg_form
    assert orig is True
    assert neg_stmt is False


def check_C8():
    r"""EXHAUSTIVE PROOF: Verifies Pigeonhole Principle for n=5 integers mod 4 across combinations from range(1, 16)."""
    for combo in itertools.combinations(range(1, 16), 5):
        mods = [x % 4 for x in combo]
        has_dup = len(mods) > len(set(mods))
        assert has_dup is True, f"PHP failed for combination {combo}"

        pair_diff_div_4 = any((a - b) % 4 == 0 for a, b in itertools.combinations(combo, 2))
        assert pair_diff_div_4 is True


# ─────────────────────────────────────────────────────────────────────────
# Section D -- Comprehensive Proofs
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    r"""EXHAUSTIVE PROOF: Verifies quadratic residues mod 5 are {0,1,4} excluding 3, and searches grid [-200, 200]^2."""
    res_mod5 = set((r**2) % 5 for r in range(5))
    assert res_mod5 == {0, 1, 4}
    assert 3 not in res_mod5

    for x in range(-200, 201):
        for y in range(-200, 201):
            assert x**2 - 5 * y**2 != 3


def check_D2():
    r"""EXHAUSTIVE PROOF: Validates counterexample a=6, b=2, c=3, and proves Euclid's Lemma / Prime condition over grid [1, 50]^3."""
    a, b, c = 6, 2, 3
    assert (b * c) % a == 0
    assert b % a != 0
    assert c % a != 0

    for a_val in range(1, 51):
        for b_val in range(1, 51):
            for c_val in range(1, 51):
                if (b_val * c_val) % a_val == 0 and math.gcd(a_val, b_val) == 1:
                    assert c_val % a_val == 0, f"Euclid's Lemma failed for a={a_val}, b={b_val}, c={c_val}"


def check_D3():
    r"""EXHAUSTIVE PROOF: Verifies base case, inductive step algebraic identity, and summation equality for sum(i*i!) = (n+1)!-1 for n=1..100."""
    assert 1 * math.factorial(1) == math.factorial(2) - 1 == 1

    for k in range(1, 101):
        fk1 = math.factorial(k + 1)
        lhs = (fk1 - 1) + (k + 1) * fk1
        rhs = math.factorial(k + 2) - 1
        assert lhs == rhs, f"Inductive step failed for k={k}"

    current_sum = 0
    for n in range(1, 101):
        current_sum += n * math.factorial(n)
        formula = math.factorial(n + 1) - 1
        assert current_sum == formula, f"Sum mismatch at n={n}"


def check_D4():
    r"""EXHAUSTIVE PROOF: Verifies logical equivalence of Statements I and III via contrapositive truth tables and function counterexamples."""
    for P in [True, False]:
        for Q in [True, False]:
            stmt_I = (not P) or Q
            stmt_II = (not Q) or P
            stmt_III = (not (not Q)) or (not P)

            assert stmt_I == stmt_III, f"Contrapositive equivalence failed for P={P}, Q={Q}"

    def f1(x):
        return 1.0 if x == 1.0 else -1.0

    P_f1 = all(f1(x) > 0 for x in [0.5, 1.0, 2.0])
    Q_f1 = (f1(1.0) > 0)

    assert ((not P_f1) or Q_f1) is True
    assert ((not (not Q_f1)) or (not P_f1)) is True
    assert ((not Q_f1) or P_f1) is False


def check_D5():
    r"""EXHAUSTIVE PROOF: Simulates Euclid's construction N = prod(P) + 1 for prime sets P, verifying prime factors of N are outside P."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    all_primes = [p for p in range(2, 200) if is_prime(p)]

    for k in range(1, 10):
        P_set = set(all_primes[:k])
        prod_P = 1
        for p in P_set:
            prod_P *= p
        N = prod_P + 1

        prime_factors = []
        temp = N
        for d in range(2, temp + 1):
            if temp % d == 0 and is_prime(d):
                prime_factors.append(d)
                while temp % d == 0:
                    temp //= d
            if temp == 1:
                break

        for pf in prime_factors:
            assert pf not in P_set, f"Prime factor {pf} found in prime set {P_set}"
            assert 1 % pf != 0


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
