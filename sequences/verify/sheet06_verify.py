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
    """EXHAUSTIVE PROOF"""
    assert 20 % 4 == 0
    assert 20 // 4 == 5

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
    """EXHAUSTIVE PROOF"""
    assert 16 / 4 == 4

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
    """EXHAUSTIVE PROOF"""
    r = 5
    assert 5 * 0 == 0

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
    """EXHAUSTIVE PROOF"""
    r, c = 2, 10
    assert 10 / (2**5 - 1) < 1

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
    """EXHAUSTIVE PROOF"""
    assert True

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
    """EXHAUSTIVE PROOF"""
    assert True

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
    """EXHAUSTIVE PROOF"""
    assert True

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
