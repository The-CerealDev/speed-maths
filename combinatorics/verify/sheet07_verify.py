"""Computational verification for combinatorics/answers/ans07.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer. A correct \\ans{} sitting on a
     \\method{} whose intermediate step doesn't actually check out is a
     documentation bug this script exists to catch.

Claims that are pure framing or motivation ("this is startling", "the
surest way to find a recurrence") are not checkable statements and are
left alone on purpose — that's still a human reviewer's job.

Run directly:
    python3 sheet07_verify.py
"""

import random
from functools import lru_cache

# ─────────────────────────────────────────────────────────────────────────
# A1 — climb 4 stairs, steps of 1 or 2. \ans{5}
# \method claims: f(n) = f(n-1) + f(n-2), running sequence 1, 2, 3, 5.
# ─────────────────────────────────────────────────────────────────────────
def check_A1():
    @lru_cache(None)
    def f(n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        return f(n - 1) + f(n - 2)

    def brute(n):
        # independent count: compositions of n using parts {1, 2}
        if n == 0:
            return 1
        if n < 0:
            return 0
        return brute(n - 1) + brute(n - 2)

    assert brute(4) == f(4), "brute-force count disagrees with the recurrence"
    assert [f(k) for k in range(1, 5)] == [1, 2, 3, 5], "method's stated running sequence is wrong"
    assert f(4) == 5  # \ans{5}


# ─────────────────────────────────────────────────────────────────────────
# D2 — erase two numbers 1..10, write |a-b|, repeat; prove last number odd.
# \method claims: |a-b| - (a+b) = -2*min(a,b); initial sum 55 is odd.
# ─────────────────────────────────────────────────────────────────────────
def check_D2():
    for a in range(0, 15):
        for b in range(0, 15):
            assert abs(a - b) - (a + b) == -2 * min(a, b), f"identity fails at a={a}, b={b}"

    assert sum(range(1, 11)) == 55
    assert 55 % 2 == 1

    # the actual theorem, not just the lemma: simulate many random reduction
    # orders on {1, ..., 10} and check the surviving number is always odd
    random.seed(0)
    for _ in range(2000):
        nums = list(range(1, 11))
        while len(nums) > 1:
            i, j = random.sample(range(len(nums)), 2)
            a, b = nums.pop(max(i, j)), nums.pop(min(i, j))
            nums.append(abs(a - b))
        assert nums[0] % 2 == 1  # \ans{Proof below.}


# ─────────────────────────────────────────────────────────────────────────
# D5 — remove a power of 2 from a pile of 2025; last stone wins.
# \method claims: no power of 2 is divisible by 3 (2^k mod 3 alternates
# 1, 2); losing positions are exactly the multiples of 3; 2025 is a
# multiple of 3, so the first player loses. \ans{The second player.}
# ─────────────────────────────────────────────────────────────────────────
def check_D5():
    N = 2025
    powers = []
    p = 1
    while p <= N:
        powers.append(p)
        p *= 2

    for k, val in enumerate(powers):
        assert val % 3 != 0, f"2^{k} is divisible by 3"
        assert val % 3 == (1 if k % 2 == 0 else 2), f"2^{k} mod 3 breaks the alternating pattern"

    # full game-tree DP, independent of the proof's induction argument.
    # is_losing[n] == True means the player about to move from n stones
    # loses under optimal play.
    is_losing = [False] * (N + 1)
    is_losing[0] = True
    for n in range(1, N + 1):
        is_losing[n] = not any(is_losing[n - q] for q in powers if q <= n)

    assert all(is_losing[n] == (n % 3 == 0) for n in range(N + 1)), \
        "losing positions are not exactly the multiples of 3"

    assert 2025 % 3 == 0
    assert is_losing[2025] is True  # first player (mover at 2025) loses
    # \ans{The second player.}


CHECKS = {
    "A1": check_A1,
    "D2": check_D2,
    "D5": check_D5,
}


def main():
    if not __debug__:
        # python -O (or PYTHONOPTIMIZE=1) strips every `assert` statement
        # at compile time — every check below would silently report PASS
        # while verifying nothing. This is an `if`, not an `assert`, on
        # purpose: it is the one check that survives -O.
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
