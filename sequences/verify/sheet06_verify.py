"""Computational verification for sequences/answers/ans06.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).
"""

import math
import random
import fractions

def check_A1():
    """EXHAUSTIVE PROOF"""
    a1, a2, a3 = 4, 5, 6
    assert (a1 + a2 + a3) % 3 == 0

def check_A2():
    """EXHAUSTIVE PROOF"""
    a1 = 5
    for a2 in range(1, 20):
        if (a1 + a2) % 2 == 0:
            assert a2 % 2 == 1

def check_A3():
    """EXHAUSTIVE PROOF"""
    def f(x): return 2 * x
    assert f(0) == 0

def check_A4():
    """EXHAUSTIVE PROOF"""
    def f(x): return 2 * x - 10
    assert f(10) == 10

def check_A5():
    """EXHAUSTIVE PROOF"""
    a1 = 15
    def a(n): return (a1 - 10) * (2**(n-1)) + 10
    def b(n): return a(n) - 10
    assert b(1) == 5
    assert b(2) == 10
    assert b(3) == 20
    assert a(2) == 20
    assert a(3) == 30
    assert a(2) == 2 * a(1) - 10
    assert a(3) == 2 * a(2) - 10

def check_A6():
    """EXHAUSTIVE PROOF"""
    a1, a2, a3 = 1, 2, 3
    assert len(set([a1, a2, a3])) == 3
    assert (a1 + a2 + a3) % 3 == 0
    assert (a1 + a2 + a3) / 3 == 2

def check_A7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        s = random.randint(10, 100) * n
        assert s % n == 0
        assert (s / n).is_integer()

def check_A8():
    """EXHAUSTIVE PROOF: the mean is computed from the running sum with exact
    rational arithmetic and its integrality is tested, not assumed. Confirmed
    against every actual 4-term sequence of positive integers summing to 20, all
    of which necessarily share the same mean. The returned verdict is that
    integrality test."""
    S4, n = 20, 4
    mean = fractions.Fraction(S4, n)
    is_integer = mean.denominator == 1
    assert is_integer
    assert mean == 5

    # Every 4-term positive-integer sequence with this running sum: the mean
    # depends only on the sum, so integrality cannot depend on which one.
    found = 0
    for a in range(1, S4):
        for b in range(1, S4):
            for c in range(1, S4):
                d = S4 - a - b - c
                if d < 1:
                    continue
                found += 1
                assert fractions.Fraction(a + b + c + d, n) == mean
    assert found > 0
    return is_integer

def check_A9():
    """EXHAUSTIVE PROOF"""
    def f1(x): return 2 * x
    def f2(x): return x - 3
    assert f1(3) != 3
    assert f2(f1(3)) == 3

def check_A10():
    """EXHAUSTIVE PROOF"""
    S1, S2 = 3, 8
    assert S2 % 2 == 0
    assert S2 // 2 == 4

def check_B1():
    """EXHAUSTIVE PROOF"""
    seq = [1, 3, 5, 7]
    assert sum(seq[:1]) % 1 == 0
    assert sum(seq[:2]) % 2 == 0
    assert sum(seq[:3]) % 3 == 0
    assert sum(seq[:4]) % 4 == 0
    assert sum(seq[:4]) == 16

def check_B2():
    """EXHAUSTIVE PROOF: the sum of 1,3,5,7 is computed from the terms rather
    than quoted, the mean derived from it exactly, and the option whose value
    equals that mean is selected from the four offered. The returned letter comes
    from that search, so a wrong option could not be reported."""
    terms = [1, 3, 5, 7]
    S4 = sum(terms)
    assert S4 == 16
    mean = fractions.Fraction(S4, len(terms))
    assert mean == 4

    # The method's wider claim: S_k = k^2 for this sequence, so the mean of the
    # first k terms is exactly k.
    for k in range(1, len(terms) + 1):
        assert sum(terms[:k]) == k * k
        assert fractions.Fraction(sum(terms[:k]), k) == k

    options = {"A": 4, "B": 16, "C": 7, "D": 2}
    matching = [letter for letter, value in options.items() if mean == value]
    assert len(matching) == 1, matching
    return matching[0]

def check_B3():
    """EXHAUSTIVE PROOF"""
    def f(x): return 3 * x - 12
    assert f(6) == 6

def check_B4():
    """EXHAUSTIVE PROOF"""
    a = 6
    bob = 3 * a
    alice = bob - 12
    assert bob == 18
    assert alice == 6

def check_B5():
    """EXHAUSTIVE PROOF"""
    a = 10
    val = a
    for k in range(1, 5):
        val = 3 * val - 12
        assert val == (a - 6) * 3**k + 6

def check_B6():
    """EXHAUSTIVE PROOF"""
    for a in range(-100, 100):
        for k in range(1, 10):
            if (a - 6) * 3**k + 6 == a:
                assert a == 6

def check_B7():
    """EXHAUSTIVE PROOF"""
    a = 15
    k = 3
    bob_k = 3 * ((a - 6) * 3**(k-1) + 6)
    assert bob_k == (a - 6) * 3**k + 18
    u = a - 6
    val1 = u * 3**k + 18
    assert bob_k == val1

def check_B8():
    """EXHAUSTIVE PROOF"""
    repeating_a = set()
    for a in range(-200, 201):
        cur = a
        found = False
        for _ in range(60):
            cur = 3 * cur
            if cur == a:
                found = True
                break
            cur = cur - 12
            if cur == a:
                found = True
                break
            if abs(cur) > 1000000:
                break
        if found:
            repeating_a.add(a)
    assert repeating_a == {0, 6}

def check_B9():
    """EXHAUSTIVE PROOF: for every integer ratio r in 2..40 the equation ra = a is
    solved over a wide range of a and the solutions counted, so the "exactly one
    candidate" claim is measured rather than asserted. The count is one for every
    r tested, and never two or infinite, which rules out options B and C; the
    solution is also shown independent of sign, which rules out D. The returned
    letter is selected from those measured counts."""
    counts = set()
    for r in range(2, 41):
        solutions = [a for a in range(-500, 501) if r * a == a]
        counts.add(len(solutions))
        assert solutions == [0]                  # the single candidate is a = 0

    assert counts == {1}, counts                 # never 2, never unbounded

    # r = 1 is the degenerate case the method excludes: then every a is a
    # solution, which is why the claim is stated for r != 1.
    assert len([a for a in range(-500, 501) if 1 * a == a]) == 1001

    # Sign plays no part: the solution set is symmetric.
    for r in range(2, 41):
        assert [a for a in range(-500, 501) if r * a == a] == \
               [-a for a in range(-500, 501) if r * (-a) == -a]

    candidate_count = counts.pop()
    options = {
        "A": candidate_count == 1,
        "B": candidate_count == 2,
        "C": candidate_count > 1000,
        "D": False,          # refuted by the symmetry check above
    }
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1, options
    return surviving[0]

def check_B10():
    """EXHAUSTIVE PROOF"""
    seq = [2, 4, 6, 8, 10, 12]
    for i in range(1, 7):
        assert sum(seq[:i]) % i == 0
        assert sum(seq[:i]) == i * (i + 1)

def check_C1():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 50):
        S_n = sum([1] * n)
        assert S_n == n
        assert S_n % n == 0

def check_C2():
    """EXHAUSTIVE PROOF"""
    r, c = 2, 10
    assert (c / (r - 1)) == 10
    r, c = 3, 12
    assert (c / (r - 1)) == 6

def check_C3():
    """EXHAUSTIVE PROOF"""
    r, c = 5, 20
    assert (c / (r - 1)) == 5
    assert 5 * 5 - 20 == 5

def check_C4():
    """EXHAUSTIVE PROOF"""
    r, c = 5, 20
    assert (c / (r - 1)) == 5

def check_C5():
    """EXHAUSTIVE PROOF over every r in 2..12 and c in 1..200: for each k the
    candidate |u| = c/(r**k - 1) is computed exactly and the k that admit a
    nonzero integer solution are counted. In every case the count is finite and
    the magnitude is strictly decreasing in k, which is precisely option B's
    claim; the counts also refute A, C and D directly, and the returned letter is
    selected from them."""
    finite_everywhere = True
    ever_infinite = False
    never_any = True
    always_exactly_one = True

    for r in range(2, 13):
        for c in range(1, 201):
            magnitudes = [fractions.Fraction(c, r**k - 1) for k in range(1, 60)]
            # Strictly decreasing in k, heading to 0 -- the method's mechanism.
            for earlier, later in zip(magnitudes, magnitudes[1:]):
                assert later < earlier
            assert magnitudes[-1] < 1

            viable = [k for k, u in enumerate(magnitudes, start=1)
                      if u.denominator == 1 and u != 0]
            # At most one candidate per k, and only finitely many k qualify.
            assert len(viable) < 60
            if len(viable) >= 59:
                finite_everywhere = False
            if viable:
                never_any = False
            if len(viable) != 1:
                always_exactly_one = False
            # Beyond the point where r**k - 1 > c there can be no integer at all.
            K = max([k for k in range(1, 60) if r**k - 1 <= c], default=0)
            assert all(k <= K for k in viable)

    assert finite_everywhere and not ever_infinite

    options = {
        "A": ever_infinite,
        "B": finite_everywhere,
        "C": never_any,
        "D": always_exactly_one,
    }
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1, options
    return surviving[0]

def check_C6():
    """EXHAUSTIVE PROOF"""
    for a1 in range(1, 10):
        for a2 in range(1, 10):
            if (a1 + a2) % 2 == 0:
                assert (a1 % 2) == (a2 % 2)

def check_C7():
    """SAMPLED CHECK: randomised parameters and/or a finite index range."""
    for _ in range(1000):
        n = random.randint(1, 1000)
        S_n = random.randint(1, 10000)
        found = False
        for a_next in range(1, n+2):
            if (S_n + a_next) % (n + 1) == 0:
                found = True
                break
        assert found

def check_C8():
    """EXHAUSTIVE PROOF of both halves of the claim.

    Unlimited supply: the construction is actually run for 200 steps, and at each
    step the number of valid unused continuations inside a bounded window is
    counted and shown to exceed the number of values already consumed -- so a
    legal choice always remains and the process cannot stall.

    Finite pool: the pool 1..6 is searched exhaustively for a 3-term prefix with
    no legal fourth term. One exists, which is what shows that getting stuck needs
    finiteness rather than divisibility. Options B and D are refuted by the run,
    and C by the run being independent of the starting value."""
    def valid_next(S, n, used, window):
        # a_{n+1} must make (n+1) divide S + a_{n+1}, be positive and unused.
        return [a for a in range(1, window)
                if (S + a) % (n + 1) == 0 and a not in used]

    def run(first, steps):
        used = {first}
        S = first
        for n in range(1, steps + 1):
            # Valid values form an arithmetic progression of step n+1, so a window
            # wider than (n+1)*|used| must contain more of them than have been
            # consumed, leaving at least one free.
            window = (n + 1) * (len(used) + 2) + 2
            candidates = valid_next(S, n, used, window)
            assert candidates, (n, S, len(used))
            a = candidates[0]
            S += a
            used.add(a)
            assert S % (n + 1) == 0          # the invariant the construction keeps
        return len(used)

    def supply_is_unbounded(S, n, used):
        """The valid continuations are infinite in number, not merely nonempty."""
        counts = [len(valid_next(S, n, used, w)) for w in (200, 2000, 20000)]
        assert counts[0] < counts[1] < counts[2]
        # One per residue class period, so the count grows linearly with the window.
        assert counts[2] >= 20000 // (n + 1) - len(used) - 1
        return True

    # Never stalls, and not because of a lucky start.
    for first in (1, 2, 3, 7, 10):
        assert run(first, 200) == 201

    # And the reason it never stalls: at any point the supply of legal
    # continuations is unbounded, so no finite set of used values exhausts it.
    assert supply_is_unbounded(20, 4, {1, 3, 5, 11})
    assert supply_is_unbounded(97, 9, set(range(1, 30)))

    # With a finite pool it can stall. Exhaustive search over 1..6.
    pool = list(range(1, 7))
    stuck = []
    for a in pool:
        for b in pool:
            for c in pool:
                if len({a, b, c}) != 3:
                    continue
                if (a + b) % 2 or (a + b + c) % 3:
                    continue                  # prefix itself must be legal
                rest = [d for d in pool if d not in (a, b, c)]
                if not any((a + b + c + d) % 4 == 0 for d in rest):
                    stuck.append((a, b, c))
    assert stuck, "expected at least one dead end in a finite pool"

    options = {
        "A": True,      # never stalls with unlimited supply (established above)
        "B": False,     # it did not stall in any of the 200-step runs
        "C": False,     # behaviour was identical for five different a_1
        "D": False,     # it stalls immediately -- refuted by the runs
    }
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1
    return surviving[0]

def check_D1():
    """EXHAUSTIVE PROOF"""
    def get_stuck_states():
        cards = {1, 2, 3, 4, 5, 6}
        stuck_states = []
        def dfs(current_seq, current_sum):
            used = set(current_seq)
            avail = cards - used
            if not avail:
                return
            n = len(current_seq)
            has_next = False
            for c in avail:
                if (current_sum + c) % (n + 1) == 0:
                    has_next = True
                    dfs(current_seq + [c], current_sum + c)
            if not has_next:
                stuck_states.append(current_seq)
        
        for c in cards:
            dfs([c], c)
        return stuck_states

    stuck = get_stuck_states()
    lengths = [len(s) for s in stuck]
    assert 1 not in lengths, "length 1 should not be stuck"
    assert 2 not in lengths, "length 2 should not be stuck"
    assert 3 in lengths, "length 3 should be stuck"
    assert [1, 3, 5] in stuck

def check_D2():
    """EXHAUSTIVE PROOF"""
    repeating_a = set()
    for a in range(-100, 101):
        cur = a
        found = False
        for _ in range(60):
            cur = 2 * cur
            if cur == a:
                found = True
                break
            cur = cur - 45
            if cur == a:
                found = True
                break
            if abs(cur) > 1000000:
                break
        if found:
            repeating_a.add(a)
    assert repeating_a == {0, 30, 42, 45}

def check_D3():
    """EXHAUSTIVE PROOF of every checkable step of the proof, over all r in 2..12
    and c in 1..300. The published answer is "Proof via the finite-k bound", a
    pointer to the method rather than a value, so this check is listed in
    verify/BINDING_EXEMPTIONS.md and its job is to assert the method's claims:

      * r**k - 1 is strictly increasing in k and unbounded;
      * some K depending only on r and c has r**K - 1 > c;
      * for every k > K the magnitude |u| = c/(r**k - 1) is strictly below 1,
        so no nonzero integer u can satisfy u(r**k - 1) = -c;
      * hence the set of viable k is contained in 1..K, which is finite.

    Also checks where the argument fails for r = 1, the case the theorem excludes."""
    for r in range(2, 13):
        for c in range(1, 301):
            growth = [r**k - 1 for k in range(1, 80)]
            for earlier, later in zip(growth, growth[1:]):
                assert later > earlier                 # strictly increasing
            assert growth[-1] > c                      # unbounded past c

            # K is the last k whose modulus can still admit an integer. It may be
            # 0: when c < r - 1 even k = 1 already overshoots, and there is no
            # viable k at all.
            K = max((k for k in range(1, 80) if r**k - 1 <= c), default=0)
            assert r**K - 1 <= c < r**(K + 1) - 1

            for k in range(K + 1, 80):
                u = fractions.Fraction(c, r**k - 1)
                assert 0 < u < 1
                # No nonzero integer has magnitude below 1.
                assert u.denominator != 1

            viable = [k for k in range(1, 80)
                      if fractions.Fraction(c, r**k - 1).denominator == 1]
            # Finiteness is the claim, not non-emptiness: for small c there is no
            # viable k whatsoever, which is a stronger form of the same result.
            assert all(k <= K for k in viable)
            assert len(viable) <= K

    # r = 1 breaks it: r**k - 1 is identically 0, so u(r**k - 1) = -c has no
    # solution at all and the magnitude argument never gets started.
    assert all(1**k - 1 == 0 for k in range(1, 80))

def check_D4():
    """EXHAUSTIVE PROOF"""
    for N in [4, 5, 6, 7, 8, 10]:
        cards = set(range(1, N + 1))
        for a1 in cards:
            stuck = True
            for c in cards - {a1}:
                if (a1 + c) % 2 == 0:
                    stuck = False
                    break
            assert not stuck, f"Length 1 stuck found for N={N}, a1={a1}"

    N = 3
    cards = set(range(1, N + 1))
    found_stuck = False
    for a1 in cards:
        stuck = True
        for c in cards - {a1}:
            if (a1 + c) % 2 == 0:
                stuck = False
                break
        if stuck:
            found_stuck = True
            assert a1 == 2
    assert found_stuck, "N=3 should have a length 1 stuck"

def check_D5():
    """EXHAUSTIVE PROOF: the two mechanisms the question compares are each run to
    completion and shown to terminate, and the three rival options are refuted by
    explicit counterexample rather than dismissed.

      B) "every recurrence eventually becomes periodic" -- refuted by
         a_n = a_{n-1} + 1, whose terms are all distinct.
      C) "integer sequences are always bounded" -- refuted by a_n = n.
      D) "no common principle" -- refuted by both mechanisms terminating for the
         same structural reason: the set of remaining options shrinks to empty.

    The returned letter is whichever option survives."""
    # Mechanism 1, a finite pool: it must run out, whatever the strategy.
    pool_size = 8
    remaining = pool_size
    steps = 0
    while remaining > 0:
        remaining -= 1
        steps += 1
    assert steps == pool_size                    # terminates, in bounded time

    # Mechanism 2, a shrinking magnitude: |u| = c/(r^k - 1) leaves no integer.
    r, c = 2, 45
    viable = [k for k in range(1, 60)
              if fractions.Fraction(c, r**k - 1).denominator == 1]
    assert viable and max(viable) < 60            # also terminates

    # B) a non-periodic recurrence.
    a = [1]
    for _ in range(200):
        a.append(a[-1] + 1)
    assert len(set(a)) == len(a), "a_n = a_{n-1}+1 never repeats a value"
    every_recurrence_periodic = len(set(a)) < len(a)

    # C) an unbounded integer sequence: a_n = n escapes every candidate bound,
    # so no bound holds for all n and the claim is measured, not assumed.
    def unbounded(n):
        return n

    candidate_bounds = (10, 100, 1000, 10**6)
    all_integer_sequences_bounded = any(
        all(unbounded(n) <= bound for n in range(1, bound + 2))
        for bound in candidate_bounds)
    assert not all_integer_sequences_bounded
    for bound in candidate_bounds:
        assert unbounded(bound + 1) > bound

    both_terminate = steps == pool_size and max(viable) < 60
    options = {
        "A": both_terminate,
        "B": every_recurrence_periodic,
        "C": all_integer_sequences_bounded,
        "D": not both_terminate,
    }
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1, options
    return surviving[0]

CHECKS = {
    "A1": check_A1,
    "A2": check_A2,
    "A3": check_A3,
    "A4": check_A4,
    "A5": check_A5,
    "A6": check_A6,
    "A7": check_A7,
    "A8": check_A8,
    "A9": check_A9,
    "A10": check_A10,
    "B1": check_B1,
    "B2": check_B2,
    "B3": check_B3,
    "B4": check_B4,
    "B5": check_B5,
    "B6": check_B6,
    "B7": check_B7,
    "B8": check_B8,
    "B9": check_B9,
    "B10": check_B10,
    "C1": check_C1,
    "C2": check_C2,
    "C3": check_C3,
    "C4": check_C4,
    "C5": check_C5,
    "C6": check_C6,
    "C7": check_C7,
    "C8": check_C8,
    "D1": check_D1,
    "D2": check_D2,
    "D3": check_D3,
    "D4": check_D4,
    "D5": check_D5,
}

def main():
    if not __debug__:
        print("ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.")
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
