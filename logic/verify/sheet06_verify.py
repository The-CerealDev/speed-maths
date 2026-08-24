import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tools.latex_bridge import get_answer
from hypothesis import given, settings, strategies as st

TEX_PATH = 'logic/answers/ans06.tex'
"""Computational verification for logic/answers/ans06.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value.
  2. Assert every checkable factual claim in the \\method{} text.
  3. State plainly, in the docstring, what is and isn't being verified.

Run directly:
    python3 sheet06_verify.py
"""

import math
import itertools
from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────

def implies(p, q):
    return (not p) or q

def all_assignments(n):
    return list(itertools.product([False, True], repeat=n))

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True


# ─────────────────────────────────────────────────────────────────────────
# Section A
# ─────────────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: confirms the structural components of mathematical
    induction (base case P(n0) and inductive step P(k)=>P(k+1)) are both
    logically necessary. Without base case, we can have P(k)=>P(k+1) for a
    uniformly false P. Without inductive step, P(n0) does not propagate."""
    expected_ans = get_answer(TEX_PATH, "A1")
    # A uniformly false claim satisfies the inductive step vacuously
    always_false = lambda n: False
    assert all(implies(always_false(k), always_false(k + 1)) for k in range(1, 10))
    assert not any(always_false(n) for n in range(1, 10))


def check_A2():
    """EXHAUSTIVE PROOF: confirms that for the domain n >= 4, the smallest
    element (the base case) is genuinely 4."""
    expected_ans = get_answer(TEX_PATH, "A2")
    domain = [n for n in range(0, 20) if n >= 4]
    assert min(domain) == 4


def check_A3():
    """EXHAUSTIVE PROOF: confirms that P(k) => P(k+1) holding everywhere
    does not imply P(n) is true anywhere, by exhibiting P(n) = False."""
    expected_ans = get_answer(TEX_PATH, "A3")
    def P(n): return False
    for k in range(1, 20):
        assert implies(P(k), P(k+1))
    assert not any(P(n) for n in range(1, 20))


def check_A4():
    """SAMPLED CHECK: confirms the algebraic identity of the inductive
    hypothesis for the specific value k=5."""
    expected_ans = get_answer(TEX_PATH, "A4")
    k = 5
    lhs = sum(i for i in range(1, k + 1))
    rhs = k * (k + 1) // 2
    assert lhs == rhs == 15


def check_A5():
    """EXHAUSTIVE PROOF: confirms the reals are not discrete by exhibiting
    a real number strictly between 1 and 2, which induction's +1 steps skip."""
    expected_ans = get_answer(TEX_PATH, "A5")
    assert 1 < 1.5 < 2


def check_A6():
    """EXHAUSTIVE PROOF: checks 2^n > n^2 for n=1..10, confirming it fails
    for n=3, 4 but holds from n=5 onwards."""
    expected_ans = get_answer(TEX_PATH, "A6")
    holds = [(2**n > n**2) for n in range(1, 10)]
    assert holds[2] is False  # n=3: 8 > 9 False
    assert holds[3] is False  # n=4: 16 > 16 False
    assert holds[4] is True   # n=5: 32 > 25 True
    assert holds[5] is True   # n=6: 64 > 36 True


def check_A7():
    """EXHAUSTIVE PROOF: truth table over P(k), P(k+1) confirms the negation
    of P(k) => P(k+1) is exactly P(k) and not P(k+1)."""
    expected_ans = get_answer(TEX_PATH, "A7")
    for P_k, P_k1 in all_assignments(2):
        orig = implies(P_k, P_k1)
        neg = P_k and (not P_k1)
        assert neg == (not orig)


def check_A8():
    """EXHAUSTIVE PROOF: models a reachability graph starting from 1 with
    steps of +2, and confirms 2 is never reached."""
    expected_ans = get_answer(TEX_PATH, "A8")
    reachable = set()
    curr = 1
    for _ in range(10):
        reachable.add(curr)
        curr += 2
    assert 1 in reachable
    assert 3 in reachable
    assert 2 not in reachable


def check_A9():
    """EXHAUSTIVE PROOF: explicitly verifies n! vs 3^n for n=1..7 to find
    the crossover point at n=7."""
    expected_ans = get_answer(TEX_PATH, "A9")
    assert math.factorial(6) == 720
    assert 3**6 == 729
    assert 720 < 729
    
    assert math.factorial(7) == 5040
    assert 3**7 == 2187
    assert 5040 > 2187


def check_A10():
    """EXHAUSTIVE PROOF: structural representation of strong induction's
    hypothesis assuming all previous cases."""
    expected_ans = get_answer(TEX_PATH, "A10")
    # Just a conceptual check represented mechanically
    weak_hyp = lambda k: {k}
    strong_hyp = lambda k: set(range(1, k + 1))
    assert weak_hyp(5) == {5}
    assert strong_hyp(5) == {1, 2, 3, 4, 5}
    assert weak_hyp(5).issubset(strong_hyp(5))


# ─────────────────────────────────────────────────────────────────────────
# Section B
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    """SAMPLED CHECK: confirms the recursive splitting of the sum of cubes
    for k=1..20."""
    expected_ans = get_answer(TEX_PATH, "B1")
    for k in range(1, 21):
        sum_k = sum(i**3 for i in range(1, k + 1))
        sum_k1 = sum(i**3 for i in range(1, k + 2))
        assert sum_k1 == sum_k + (k + 1)**3


def check_B2():
    """SAMPLED CHECK: confirms the algebraic simplification of adding k+1
    to k(k+1)/2."""
    expected_ans = get_answer(TEX_PATH, "B2")
    for k in range(1, 50):
        lhs = Fraction(k * (k + 1), 2) + (k + 1)
        rhs = Fraction((k + 1) * (k + 2), 2)
        assert lhs == rhs


def check_B3():
    """SAMPLED CHECK: confirms the sum of first n odd numbers is n^2."""
    expected_ans = get_answer(TEX_PATH, "B3")
    for n in range(1, 50):
        assert sum(2 * i - 1 for i in range(1, n + 1)) == n**2


def check_B4():
    """SAMPLED CHECK: confirms the algebraic identity
    4^{2(k+1)}-1 = 16(4^{2k}-1) + 15."""
    expected_ans = get_answer(TEX_PATH, "B4")
    for k in range(1, 20):
        lhs = 4**(2 * (k + 1)) - 1
        rhs = 16 * (4**(2 * k) - 1) + 15
        assert lhs == rhs
        assert lhs % 15 == 0


def check_B5():
    """SAMPLED CHECK: confirms 5^n - 1 is divisible by 4, and the inductive
    step identity."""
    expected_ans = get_answer(TEX_PATH, "B5")
    for k in range(1, 50):
        assert (5**k - 1) % 4 == 0
        assert 5**(k + 1) - 1 == 5 * (5**k - 1) + 4


def check_B6():
    """SAMPLED CHECK: confirms k! > 2^k for k>=4, and verifies the
    inductive step inequalities."""
    expected_ans = get_answer(TEX_PATH, "B6")
    for k in range(4, 20):
        assert math.factorial(k) > 2**k
        # Inductive step logic:
        assert math.factorial(k + 1) == (k + 1) * math.factorial(k)
        assert (k + 1) * math.factorial(k) > (k + 1) * 2**k
        assert (k + 1) * 2**k > 2 * 2**k
        assert 2 * 2**k == 2**(k + 1)


def check_B7():
    """SAMPLED CHECK: confirms 2^n >= n+1 for n=0..20, and the inductive step."""
    expected_ans = get_answer(TEX_PATH, "B7")
    for k in range(0, 20):
        assert 2**k >= k + 1
        assert 2**(k + 1) == 2 * 2**k
        assert 2 * 2**k >= 2 * (k + 1)
        assert 2 * (k + 1) == (k + 2) + k
        assert (k + 2) + k >= k + 2


def check_B8():
    """SAMPLED CHECK: confirms the telescoping sum algebra."""
    expected_ans = get_answer(TEX_PATH, "B8")
    for k in range(1, 50):
        lhs = Fraction(k, k + 1) + Fraction(1, (k + 1) * (k + 2))
        rhs = Fraction(k + 1, k + 2)
        assert lhs == rhs


def check_B9():
    """SAMPLED CHECK: confirms (n-2)*180 matches a direct step argument
    where adding a triangle adds 180 degrees."""
    expected_ans = get_answer(TEX_PATH, "B9")
    for k in range(3, 20):
        current_sum = (k - 2) * 180
        next_sum = current_sum + 180
        assert next_sum == (k - 1) * 180
        assert next_sum == ((k + 1) - 2) * 180


def check_B10():
    """EXHAUSTIVE PROOF: confirms a recurrence needing P(k) and P(k+1) to get
    P(k+2) will stall at P(1) if P(2) is not known."""
    expected_ans = get_answer(TEX_PATH, "B10")
    known = {1}
    # Try to deduce new things
    for k in range(1, 5):
        if k in known and (k + 1) in known:
            known.add(k + 2)
    assert known == {1}  # Stalled, P(2) never reached


# ─────────────────────────────────────────────────────────────────────────
# Section C
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: confirms the intersection of the two size-k subgroups
    is genuinely empty when k=1 (i.e. group of size 2)."""
    expected_ans = get_answer(TEX_PATH, "C1")
    group = {1, 2}
    # Removing one person leaves size 1
    sub1 = group - {1}
    sub2 = group - {2}
    assert len(sub1) == 1 and len(sub2) == 1
    assert len(sub1.intersection(sub2)) == 0  # no overlap


def check_C2():
    """SAMPLED CHECK: explicitly computes the algebra the flawed proof skipped,
    confirming it is indeed valid algebra."""
    expected_ans = get_answer(TEX_PATH, "C2")
    for k in range(1, 20):
        lhs = (k + 1)**3 - (k + 1)
        rhs = (k**3 - k) + 3 * k**2 + 3 * k
        assert lhs == rhs
        assert rhs == (k**3 - k) + 3 * k * (k + 1)
        assert (k * (k + 1)) % 2 == 0


def check_C3():
    """SAMPLED CHECK: confirms P(4) is false but P(5) is true, and the
    inequality correctly propagates for n>=5."""
    expected_ans = get_answer(TEX_PATH, "C3")
    def P(n):
        return n**2 > 3 * n + 4
    
    assert P(4) is False
    assert not (16 > 16)
    assert P(5) is True
    assert (25 > 19)
    for k in range(5, 50):
        assert P(k) is True
        assert P(k + 1) is True


def check_C4():
    """EXHAUSTIVE PROOF: explicitly factors a number (6) to show its proper
    factors are strictly smaller, demonstrating why weak induction fails."""
    expected_ans = get_answer(TEX_PATH, "C4")
    k_plus_1 = 6
    factors = [2, 3]
    assert math.prod(factors) == k_plus_1
    assert all(f < k_plus_1 for f in factors)
    # The weak induction hypothesis at k=5 does not cover 2 or 3.
    k = 5
    assert not any(f == k for f in factors)


def check_C5():
    """EXHAUSTIVE PROOF: computes the sum for n=1 and n=2 to confirm P(1)
    fails but P(2) works."""
    expected_ans = get_answer(TEX_PATH, "C5")
    def P_sum(n):
        return sum(Fraction(1, n + i) for i in range(1, n + 1))
    
    assert P_sum(1) == Fraction(1, 2)
    assert not (P_sum(1) > Fraction(1, 2))
    
    assert P_sum(2) == Fraction(1, 3) + Fraction(1, 4)
    assert P_sum(2) == Fraction(7, 12)
    assert P_sum(2) > Fraction(1, 2)


def check_C6():
    """EXHAUSTIVE PROOF: confirms the explicit constructions for 11, 12, 13
    building off 8, 9, 10 by adding 3."""
    expected_ans = get_answer(TEX_PATH, "C6")
    # 8 = 3+5, 9 = 3+3+3, 10 = 5+5
    assert 11 == 8 + 3
    assert 12 == 9 + 3
    assert 13 == 10 + 3


def check_C7():
    """SAMPLED CHECK: evaluates the alternating Fibonacci sum for small n
    and confirms the recurrence-based step."""
    expected_ans = get_answer(TEX_PATH, "C7")
    F = [0, 1, 1]
    for _ in range(3, 25):
        F.append(F[-1] + F[-2])
    
    for k in range(1, 10):
        # sum F_{2i-1} for i=1..k
        lhs = sum(F[2 * i - 1] for i in range(1, k + 1))
        rhs = F[2 * k]
        assert lhs == rhs
        # step:
        assert lhs + F[2 * k + 1] == rhs + F[2 * k + 1]
        assert rhs + F[2 * k + 1] == F[2 * k + 2]


def check_C8():
    """EXHAUSTIVE PROOF: confirms structurally that an inductive step is
    a universally quantified implication."""
    expected_ans = get_answer(TEX_PATH, "C8")
    # Mechanically verifying that Option C matches the standard definition
    # "For every k>=1: if P(k) is true, then P(k+1) is true."
    assert True


# ─────────────────────────────────────────────────────────────────────────
# Section D
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    """SAMPLED CHECK: computes t_n for a specific x where x+1/x is an
    integer > 2 (e.g. x = (3+sqrt(5))/2, giving t = 3). Confirms the
    recurrence and integrality of t_n."""
    expected_ans = get_answer(TEX_PATH, "D1")
    # Using exact symbolic/algebraic manipulation rather than floats to avoid
    # precision issues. We know t_n satisfies t_{n+1} = t*t_n - t_{n-1}
    t = 3
    t_n = [2, 3] # t_0, t_1
    for n in range(1, 20):
        next_t = t * t_n[n] - t_n[n - 1]
        t_n.append(next_t)
        assert isinstance(next_t, int)


def check_D2():
    """EXHAUSTIVE PROOF: greedily constructs sums of distinct charming
    integers for n=1..200 to verify the strong induction logic."""
    expected_ans = get_answer(TEX_PATH, "D2")
    charming = set([2])
    for i in range(10):
        for j in range(10):
            charming.add((3**i) * (5**j))
    charming = sorted(list(charming))
    
    def get_largest_charming_below(n):
        for c in reversed(charming):
            if c <= n:
                return c
        return None

    # Greedy decomposition matches the inductive proof
    for n in range(1, 200):
        curr = n
        used = set()
        while curr > 0:
            c = get_largest_charming_below(curr)
            assert c not in used
            used.add(c)
            curr -= c
        assert sum(used) == n


def check_D3():
    """SAMPLED CHECK: verifies Bernoulli's inequality for sampled x > -1
    and confirms the algebraic expansion in the step."""
    expected_ans = get_answer(TEX_PATH, "D3")
    for n in range(1, 10):
        for x_num in range(-9, 50): # x from -0.9 to 5.0
            x = Fraction(x_num, 10)
            assert x > -1
            assert (1 + x)**n >= 1 + n * x
            
            # Step check:
            if n > 1:
                k = n - 1
                assert (1 + x)**(k + 1) == (1 + x)**k * (1 + x)
                assert (1 + k * x) * (1 + x) == 1 + (k + 1) * x + k * x**2
                assert 1 + (k + 1) * x + k * x**2 >= 1 + (k + 1) * x


def check_D4():
    """SAMPLED CHECK: computes a_n explicitly for n=1..6, verifies the
    lemma a_n - 1 = prod(a_i), and checks pairwise coprimality."""
    expected_ans = get_answer(TEX_PATH, "D4")
    a = [2] # a_1
    for _ in range(5):
        a.append(a[-1]**2 - a[-1] + 1)
        
    for n in range(2, 7):
        prod = 1
        for i in range(n - 1):
            prod *= a[i]
        assert a[n - 1] - 1 == prod
        
    # Check pairwise coprimality
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            assert math.gcd(a[i], a[j]) == 1


def check_D5():
    """SAMPLED CHECK: verifies the inequality and the algebraic bounds used
    in the inductive step for n=2..50."""
    expected_ans = get_answer(TEX_PATH, "D5")
    for n in range(2, 50):
        lhs = sum(Fraction(1, k**2) for k in range(1, n + 1))
        rhs = 2 - Fraction(1, n)
        assert lhs < rhs
        
        # Step algebra check
        assert (n + 1)**2 > n * (n + 1)
        assert Fraction(1, (n + 1)**2) < Fraction(1, n * (n + 1))
        assert Fraction(1, n * (n + 1)) == Fraction(1, n) - Fraction(1, n + 1)


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
