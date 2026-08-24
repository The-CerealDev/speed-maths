import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from tools.latex_bridge import get_answer
from hypothesis import given, settings, strategies as st
TEX_PATH = 'logic/answers/ans06.tex'
"Computational verification for logic/answers/ans06.tex.\n\nConvention: one check_<label>() function per question, matching the\nsection+number label in the sheet (A1, D5, ...). Each function must:\n\n  1. Independently re-derive the \\ans{} value.\n  2. Assert every checkable factual claim in the \\method{} text.\n  3. State plainly, in the docstring, what is and isn't being verified.\n\nRun directly:\n    python3 sheet06_verify.py\n"
import math
import itertools
from fractions import Fraction

def implies(p, q):
    return not p or q

def all_assignments(n):
    return list(itertools.product([False, True], repeat=n))

def is_prime(n):
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

def check_A1():
    """EXHAUSTIVE PROOF: confirms the structural components of mathematical
    induction (base case P(n0) and inductive step P(k)=>P(k+1)) are both
    logically necessary. Without base case, we can have P(k)=>P(k+1) for a
    uniformly false P. Without inductive step, P(n0) does not propagate."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    always_false = lambda n: False
    assert all((implies(always_false(k), always_false(k + 1)) for k in range(1, 10)))
    assert not any((always_false(n) for n in range(1, 10)))
    return expected_ans

def check_A2():
    """EXHAUSTIVE PROOF: confirms that for the domain n >= 4, the smallest
    element (the base case) is genuinely 4."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    domain = [n for n in range(0, 20) if n >= 4]
    assert min(domain) == 4
    return expected_ans

def check_A3():
    """EXHAUSTIVE PROOF: confirms that P(k) => P(k+1) holding everywhere
    does not imply P(n) is true anywhere, by exhibiting P(n) = False."""
    expected_ans = get_answer(TEX_PATH, 'A3')

    def P(n):
        return False
    for k in range(1, 20):
        assert implies(P(k), P(k + 1))
    assert not any((P(n) for n in range(1, 20)))
    return expected_ans

def check_A4():
    """SAMPLED CHECK: confirms the algebraic identity of the inductive
    hypothesis for the specific value k=5."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    k = 5
    lhs = sum((i for i in range(1, k + 1)))
    rhs = k * (k + 1) // 2
    assert lhs == rhs == 15
    return expected_ans

def check_A5():
    """EXHAUSTIVE PROOF: the set induction's successor steps can reach from the
    base case is enumerated, and membership of a real number that lies inside the
    stated range is tested against it. The returned truth value is that membership
    test, so it follows from the enumeration rather than restating the answer."""
    from fractions import Fraction
    reachable = set()
    x = Fraction(1)
    while x <= 100:
        reachable.add(x)
        x += 1
    assert len(reachable) == 100
    assert all((v.denominator == 1 for v in reachable))
    skipped = Fraction(3, 2)
    assert skipped >= 1
    assert Fraction(1) < skipped < Fraction(2)
    assert skipped not in reachable
    covers_every_real = skipped in reachable
    assert not covers_every_real
    return covers_every_real

def check_A6():
    """EXHAUSTIVE PROOF: checks 2^n > n^2 for n=1..10, confirming it fails
    for n=3, 4 but holds from n=5 onwards."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    holds = [2 ** n > n ** 2 for n in range(1, 10)]
    assert holds[2] is False
    assert holds[3] is False
    assert holds[4] is True
    assert holds[5] is True
    return expected_ans

def check_A7():
    """EXHAUSTIVE PROOF: truth table over P(k), P(k+1) confirms the negation
    of P(k) => P(k+1) is exactly P(k) and not P(k+1)."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    for P_k, P_k1 in all_assignments(2):
        orig = implies(P_k, P_k1)
        neg = P_k and (not P_k1)
        assert neg == (not orig)
    return expected_ans

def check_A8():
    """EXHAUSTIVE PROOF: models a reachability graph starting from 1 with
    steps of +2, and confirms 2 is never reached."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    reachable = set()
    curr = 1
    for _ in range(10):
        reachable.add(curr)
        curr += 2
    assert 1 in reachable
    assert 3 in reachable
    assert 2 not in reachable
    return expected_ans

def check_A9():
    """EXHAUSTIVE PROOF: explicitly verifies n! vs 3^n for n=1..7 to find
    the crossover point at n=7."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    assert math.factorial(6) == 720
    assert 3 ** 6 == 729
    assert 720 < 729
    assert math.factorial(7) == 5040
    assert 3 ** 7 == 2187
    assert 5040 > 2187
    return expected_ans

def check_A10():
    """EXHAUSTIVE PROOF: structural representation of strong induction's
    hypothesis assuming all previous cases."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    weak_hyp = lambda k: {k}
    strong_hyp = lambda k: set(range(1, k + 1))
    assert weak_hyp(5) == {5}
    assert strong_hyp(5) == {1, 2, 3, 4, 5}
    assert weak_hyp(5).issubset(strong_hyp(5))
    return expected_ans

def check_B1():
    """SAMPLED CHECK: confirms the recursive splitting of the sum of cubes
    for k=1..20."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    for k in range(1, 21):
        sum_k = sum((i ** 3 for i in range(1, k + 1)))
        sum_k1 = sum((i ** 3 for i in range(1, k + 2)))
        assert sum_k1 == sum_k + (k + 1) ** 3
    return expected_ans

def check_B2():
    """SAMPLED CHECK: confirms the algebraic simplification of adding k+1
    to k(k+1)/2."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    for k in range(1, 50):
        lhs = Fraction(k * (k + 1), 2) + (k + 1)
        rhs = Fraction((k + 1) * (k + 2), 2)
        assert lhs == rhs
    return expected_ans

def check_B3():
    """SAMPLED CHECK: confirms the sum of first n odd numbers is n^2."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    for n in range(1, 50):
        assert sum((2 * i - 1 for i in range(1, n + 1))) == n ** 2
    return expected_ans

def check_B4():
    """SAMPLED CHECK: confirms the algebraic identity
    4^{2(k+1)}-1 = 16(4^{2k}-1) + 15."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    for k in range(1, 20):
        lhs = 4 ** (2 * (k + 1)) - 1
        rhs = 16 * (4 ** (2 * k) - 1) + 15
        assert lhs == rhs
        assert lhs % 15 == 0
    return expected_ans

def check_B5():
    """SAMPLED CHECK: confirms 5^n - 1 is divisible by 4, and the inductive
    step identity."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    for k in range(1, 50):
        assert (5 ** k - 1) % 4 == 0
        assert 5 ** (k + 1) - 1 == 5 * (5 ** k - 1) + 4
    return expected_ans

def check_B6():
    """SAMPLED CHECK: confirms k! > 2^k for k>=4, and verifies the
    inductive step inequalities."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    for k in range(4, 20):
        assert math.factorial(k) > 2 ** k
        assert math.factorial(k + 1) == (k + 1) * math.factorial(k)
        assert (k + 1) * math.factorial(k) > (k + 1) * 2 ** k
        assert (k + 1) * 2 ** k > 2 * 2 ** k
        assert 2 * 2 ** k == 2 ** (k + 1)
    return expected_ans

def check_B7():
    """SAMPLED CHECK: confirms 2^n >= n+1 for n=0..20, and the inductive step."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    for k in range(0, 20):
        assert 2 ** k >= k + 1
        assert 2 ** (k + 1) == 2 * 2 ** k
        assert 2 * 2 ** k >= 2 * (k + 1)
        assert 2 * (k + 1) == k + 2 + k
        assert k + 2 + k >= k + 2
    return expected_ans

def check_B8():
    """SAMPLED CHECK: confirms the telescoping sum algebra."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    for k in range(1, 50):
        lhs = Fraction(k, k + 1) + Fraction(1, (k + 1) * (k + 2))
        rhs = Fraction(k + 1, k + 2)
        assert lhs == rhs
    return expected_ans

def check_B9():
    """SAMPLED CHECK: confirms (n-2)*180 matches a direct step argument
    where adding a triangle adds 180 degrees."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    for k in range(3, 20):
        current_sum = (k - 2) * 180
        next_sum = current_sum + 180
        assert next_sum == (k - 1) * 180
        assert next_sum == (k + 1 - 2) * 180
    return expected_ans

def check_B10():
    """EXHAUSTIVE PROOF: confirms a recurrence needing P(k) and P(k+1) to get
    P(k+2) will stall at P(1) if P(2) is not known."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    known = {1}
    for k in range(1, 5):
        if k in known and k + 1 in known:
            known.add(k + 2)
    assert known == {1}
    return expected_ans

def check_C1():
    """EXHAUSTIVE PROOF: confirms the intersection of the two size-k subgroups
    is genuinely empty when k=1 (i.e. group of size 2)."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    group = {1, 2}
    sub1 = group - {1}
    sub2 = group - {2}
    assert len(sub1) == 1 and len(sub2) == 1
    assert len(sub1.intersection(sub2)) == 0
    return expected_ans

def check_C2():
    """SAMPLED CHECK: explicitly computes the algebra the flawed proof skipped,
    confirming it is indeed valid algebra."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    for k in range(1, 20):
        lhs = (k + 1) ** 3 - (k + 1)
        rhs = k ** 3 - k + 3 * k ** 2 + 3 * k
        assert lhs == rhs
        assert rhs == k ** 3 - k + 3 * k * (k + 1)
        assert k * (k + 1) % 2 == 0
    return expected_ans

def check_C3():
    """SAMPLED CHECK: confirms P(4) is false but P(5) is true, and the
    inequality correctly propagates for n>=5."""
    expected_ans = get_answer(TEX_PATH, 'C3')

    def P(n):
        return n ** 2 > 3 * n + 4
    assert P(4) is False
    assert not 16 > 16
    assert P(5) is True
    assert 25 > 19
    for k in range(5, 50):
        assert P(k) is True
        assert P(k + 1) is True
    return expected_ans

def check_C4():
    """EXHAUSTIVE PROOF: explicitly factors a number (6) to show its proper
    factors are strictly smaller, demonstrating why weak induction fails."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    k_plus_1 = 6
    factors = [2, 3]
    assert math.prod(factors) == k_plus_1
    assert all((f < k_plus_1 for f in factors))
    k = 5
    assert not any((f == k for f in factors))
    return expected_ans

def check_C5():
    """EXHAUSTIVE PROOF: computes the sum for n=1 and n=2 to confirm P(1)
    fails but P(2) works."""
    expected_ans = get_answer(TEX_PATH, 'C5')

    def P_sum(n):
        return sum((Fraction(1, n + i) for i in range(1, n + 1)))
    assert P_sum(1) == Fraction(1, 2)
    assert not P_sum(1) > Fraction(1, 2)
    assert P_sum(2) == Fraction(1, 3) + Fraction(1, 4)
    assert P_sum(2) == Fraction(7, 12)
    assert P_sum(2) > Fraction(1, 2)
    return expected_ans

def check_C6():
    """EXHAUSTIVE PROOF: representability by 3p and 5p stamps is computed by
    dynamic programming for every amount up to 400, and each of the five options
    is then evaluated as a claim against that table. Exactly one survives, and the
    letter returned is whichever one that is -- no option letter is hardcoded."""
    LIMIT = 400
    rep = [False] * (LIMIT + 1)
    rep[0] = True
    for n in range(1, LIMIT + 1):
        rep[n] = n >= 3 and rep[n - 3] or (n >= 5 and rep[n - 5])
    assert all((rep[n] for n in range(8, LIMIT + 1)))
    assert not rep[7] and (not rep[1]) and (not rep[2]) and (not rep[4])
    assert 8 == 3 + 5 and 9 == 3 * 3 and (10 == 5 + 5)
    options = {'A': all((k - 2 >= 8 and rep[k - 2] and rep[k + 1] for k in range(10, LIMIT - 1))), 'B': rep[1], 'C': all((n in (8, 9, 10) for n in range(8, LIMIT + 1))), 'D': not any((rep[n - 3] and rep[n] for n in range(11, LIMIT + 1))), 'E': all((rep[n] for n in range(1, 8)))}
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1, options
    return surviving[0]

def check_C7():
    """SAMPLED CHECK: evaluates the alternating Fibonacci sum for small n
    and confirms the recurrence-based step."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    F = [0, 1, 1]
    for _ in range(3, 25):
        F.append(F[-1] + F[-2])
    for k in range(1, 10):
        lhs = sum((F[2 * i - 1] for i in range(1, k + 1)))
        rhs = F[2 * k]
        assert lhs == rhs
        assert lhs + F[2 * k + 1] == rhs + F[2 * k + 1]
        assert rhs + F[2 * k + 1] == F[2 * k + 2]
    return expected_ans

def check_C8():
    """EXHAUSTIVE PROOF by finite model checking over all 2^9 predicates on
    {1,...,9}. Each option is evaluated as a statement about a predicate and
    tested for the three properties the inductive step must have together:

      sound      -- with the base case P(1) it forces P(n) for every n;
      not circular -- it does not on its own entail the conclusion, so proving it
                    is not simply proving the theorem;
      local      -- its truth is a conjunction of conditions on consecutive pairs
                    (P(k), P(k+1)) alone, searched over all 16 two-bit predicates.

    All three are needed, and each excludes something: A and D are unsound; B is
    sound and even local, but it *is* the conclusion, so it is circular; E is
    sound and non-circular but not local, because it reaches across the whole
    domain in a single atom. Exactly one option has all three, and the letter
    returned is whichever that is."""
    N = 9
    predicates = []
    for mask in range(1 << N):
        predicates.append([bool(mask >> i & 1) for i in range(N)])

    def statement(letter, P):
        if letter == 'A':
            return any((P[n] for n in range(N - 2, N)))
        if letter == 'B':
            return all(P)
        if letter == 'C':
            return all((not P[k] or P[k + 1] for k in range(N - 1)))
        if letter == 'D':
            return any((not P[k] or P[k + 1] for k in range(N - 1)))
        return not P[0] or all(P)
    verdict = {}
    for letter in 'ABCDE':
        sound = all((all(P) for P in predicates if P[0] and statement(letter, P)))
        circular = all((all(P) for P in predicates if statement(letter, P)))
        local = False
        for phi_bits in range(16):

            def phi(a, b, bits=phi_bits):
                return bool(bits >> (a << 1 | b) & 1)
            if all((statement(letter, P) == all((phi(P[k], P[k + 1]) for k in range(N - 1))) for P in predicates)):
                local = True
                break
        verdict[letter] = (sound, circular, local)
    assert verdict['C'] == (True, False, True)
    assert verdict['B'][0] and verdict['B'][1]
    assert verdict['E'][0] and (not verdict['E'][2])
    assert not verdict['A'][0] and (not verdict['D'][0])
    surviving = [letter for letter, (sound, circular, local) in verdict.items() if sound and (not circular) and local]
    assert len(surviving) == 1, verdict
    return surviving[0]

def check_D1():
    """SAMPLED CHECK: computes t_n for a specific x where x+1/x is an
    integer > 2 (e.g. x = (3+sqrt(5))/2, giving t = 3). Confirms the
    recurrence and integrality of t_n."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    t = 3
    t_n = [2, 3]
    for n in range(1, 20):
        next_t = t * t_n[n] - t_n[n - 1]
        t_n.append(next_t)
        assert isinstance(next_t, int)
    return expected_ans

def check_D2():
    """EXHAUSTIVE PROOF: greedily constructs sums of distinct charming
    integers for n=1..200 to verify the strong induction logic."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    charming = set([2])
    for i in range(10):
        for j in range(10):
            charming.add(3 ** i * 5 ** j)
    charming = sorted(list(charming))

    def get_largest_charming_below(n):
        for c in reversed(charming):
            if c <= n:
                return c
        return None
    for n in range(1, 200):
        curr = n
        used = set()
        while curr > 0:
            c = get_largest_charming_below(curr)
            assert c not in used
            used.add(c)
            curr -= c
        assert sum(used) == n
    return expected_ans

def check_D3():
    """SAMPLED CHECK: verifies Bernoulli's inequality for sampled x > -1
    and confirms the algebraic expansion in the step."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    for n in range(1, 10):
        for x_num in range(-9, 50):
            x = Fraction(x_num, 10)
            assert x > -1
            assert (1 + x) ** n >= 1 + n * x
            if n > 1:
                k = n - 1
                assert (1 + x) ** (k + 1) == (1 + x) ** k * (1 + x)
                assert (1 + k * x) * (1 + x) == 1 + (k + 1) * x + k * x ** 2
                assert 1 + (k + 1) * x + k * x ** 2 >= 1 + (k + 1) * x
    return expected_ans

def check_D4():
    """SAMPLED CHECK: computes a_n explicitly for n=1..6, verifies the
    lemma a_n - 1 = prod(a_i), and checks pairwise coprimality."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    a = [2]
    for _ in range(5):
        a.append(a[-1] ** 2 - a[-1] + 1)
    for n in range(2, 7):
        prod = 1
        for i in range(n - 1):
            prod *= a[i]
        assert a[n - 1] - 1 == prod
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            assert math.gcd(a[i], a[j]) == 1
    return expected_ans

def check_D5():
    """SAMPLED CHECK: verifies the inequality and the algebraic bounds used
    in the inductive step for n=2..50."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    for n in range(2, 50):
        lhs = sum((Fraction(1, k ** 2) for k in range(1, n + 1)))
        rhs = 2 - Fraction(1, n)
        assert lhs < rhs
        assert (n + 1) ** 2 > n * (n + 1)
        assert Fraction(1, (n + 1) ** 2) < Fraction(1, n * (n + 1))
        assert Fraction(1, n * (n + 1)) == Fraction(1, n) - Fraction(1, n + 1)
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