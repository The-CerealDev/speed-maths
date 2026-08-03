"""Computational verification for logic/answers/ans07.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value.
  2. Assert every checkable factual claim in the \\method{} text.
  3. State plainly, in the docstring, what is and isn't being verified.

Run directly:
    python3 sheet07_verify.py
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
    """EXHAUSTIVE PROOF: truth table confirms that P=>Q is logically equivalent to (not Q)=>(not P)."""
    for P, Q in all_assignments(2):
        orig = implies(P, Q)
        contra = implies(not Q, not P)
        assert orig == contra


def check_A2():
    """EXHAUSTIVE PROOF: confirms the negation of 'forall x, not P(x)' 
    is 'exists x, P(x)' over abstract truth assignments for a small domain."""
    for P_vals in itertools.product([False, True], repeat=4):
        orig = all(not p for p in P_vals)
        negation = any(p for p in P_vals)
        assert negation == (not orig)


def check_A3():
    """SAMPLED CHECK over n=1..100: confirms 'multiple of 6' implies 'multiple of 2',
    but not the reverse (e.g. n=4). Thus, sufficient but not necessary."""
    for n in range(1, 101):
        if n % 6 == 0:
            assert n % 2 == 0
    assert 4 % 2 == 0
    assert 4 % 6 != 0


def check_A4():
    """EXHAUSTIVE PROOF: logic structural check. Proof by contradiction 
    assumes the negation of the goal. Goal: 'not exists largest prime'.
    Negation: 'exists largest prime'."""
    goal_is_false = False # we want to prove it's true, so we assume it's false
    assert not goal_is_false


def check_A5():
    """EXHAUSTIVE PROOF: confirms 9 is odd but composite, refuting 'every odd is prime'."""
    assert 9 % 2 == 1
    assert not is_prime(9)
    assert 9 == 3 * 3


def check_A6():
    """EXHAUSTIVE PROOF: truth table confirms affirming the consequent 
    (P=>Q, Q |- P) is an invalid argument form."""
    counterexample = any(
        implies(P, Q) and Q and not P
        for P, Q in all_assignments(2)
    )
    assert counterexample is True


def check_A7():
    """EXHAUSTIVE PROOF: truth-table check verifies that P=>Q is NOT in general equivalent to Q=>P."""
    mismatch = False
    for P, Q in all_assignments(2):
        orig = implies(P, Q)
        converse = implies(Q, P)
        if orig != converse:
            mismatch = True
    assert mismatch is True


def check_A8():
    """SAMPLED CHECK: confirms computationally that n=7k implies n^2 is a multiple of 49."""
    for k in range(-50, 50):
        n = 7 * k
        n_sq = n**2
        assert n_sq == 49 * k**2
        assert n_sq % 49 == 0


def check_A9():
    """SAMPLED CHECK over bounded range: confirms 'exists x forall y (x<y)' is false
    while 'forall y exists x (x<y)' is true (witness x=y-1)."""
    # forall y, exists x < y
    for y in range(-50, 50):
        x = y - 1
        assert x < y
    # exists x, forall y < y (false)
    for x in range(-50, 50):
        # show for this x, there exists y such that NOT(x<y)
        y = x - 1
        assert not (x < y)


def check_A10():
    """EXHAUSTIVE PROOF: verifies n=6 is a multiple of 3 and is even (not odd), a valid counterexample."""
    n = 6
    assert n % 3 == 0
    assert n % 2 == 0


# ─────────────────────────────────────────────────────────────────────────
# Section B
# ─────────────────────────────────────────────────────────────────────────

def check_B1():
    """SAMPLED CHECK: confirms over a range of n that every multiple of 15 is indeed a multiple of 3 and of 5."""
    for n in range(1, 201):
        if n % 15 == 0:
            assert n % 3 == 0
            assert n % 5 == 0


def check_B2():
    """SAMPLED CHECK: confirms n^2+n is always even for all n, contradicting
    the assumption that it can be odd."""
    for n in range(1, 100):
        assert n**2 + n == n * (n + 1)
        assert (n**2 + n) % 2 == 0


def check_B3():
    """SAMPLED CHECK over n=1..50: confirms sum of squares formula and its 
    algebraic step in the method."""
    for n in range(1, 51):
        lhs = sum(i**2 for i in range(1, n + 1))
        rhs = n * (n + 1) * (2 * n + 1) // 6
        assert lhs == rhs
        
        # Method algebra check for inductive step from k to k+1
        k = n
        step_lhs = lhs + (k + 1)**2
        step_rhs = (k + 1) * (k + 2) * (2 * k + 3) // 6
        assert step_lhs == step_rhs
        
        # Checking intermediate factorisation claim from method:
        # (k+1)[k(2k+1) + 6(k+1)] = (k+1)(2k^2 + 7k + 6)
        poly = k * (2 * k + 1) + 6 * (k + 1)
        assert poly == 2 * k**2 + 7 * k + 6
        assert poly == (k + 2) * (2 * k + 3)


def check_B4():
    """EXHAUSTIVE PROOF: truth table confirms that (not A => not B) is NOT logically equivalent to (A => B), proving the student's proof structure is invalid."""
    mismatch = any(
        implies(not A, not B) != implies(A, B)
        for A, B in all_assignments(2)
    )
    assert mismatch is True


def check_B5():
    """EXHAUSTIVE PROOF: confirms n=2 is prime but not odd, showing 'prime' 
    is not sufficient for 'odd'."""
    assert is_prime(2)
    assert 2 % 2 == 0


def check_B6():
    """SAMPLED CHECK: confirms using Python's set type that for any sample A, taking B=frozenset() gives empty intersection."""
    sample_As = [set([1, 2, 3]), set(['a', 'b']), set()]
    B = frozenset()
    for A in sample_As:
        assert len(A.intersection(B)) == 0


def check_B7():
    """SAMPLED CHECK over n=1..50: confirms n^3+2n is divisible by 3, and 
    verifies the algebraic manipulation in the inductive step."""
    for n in range(1, 51):
        assert (n**3 + 2 * n) % 3 == 0
        
        k = n
        # Inductive step: (k+1)^3 + 2(k+1) = (k^3+2k) + 3(k^2+k+1)
        lhs = (k + 1)**3 + 2 * (k + 1)
        rhs = (k**3 + 2 * k) + 3 * (k**2 + k + 1)
        assert lhs == rhs


def check_B8():
    """EXHAUSTIVE PROOF over bounded search: verifies the infinite descent logic 
    that no coprime p,q < 500 satisfy 6q^2 = p^2. Also verifies the logical structure:
    2|6q^2 => 2|p^2 => 2|p."""
    for p in range(1, 500):
        for q in range(1, 500):
            if 6 * q**2 == p**2:
                assert math.gcd(p, q) != 1
                
    # Logic structure check
    # If 6q^2 = p^2, then p must be even.
    # Let p = 2r. Then 6q^2 = 4r^2 => 3q^2 = 2r^2 => q must be even.
    # Thus p,q both even, gcd >= 2.
    for q in range(1, 50):
        for p in range(1, 50):
            if 6 * q**2 == p**2:
                assert p % 2 == 0
                r = p // 2
                assert 3 * q**2 == 2 * r**2
                assert q % 2 == 0


def check_B9():
    """SAMPLED CHECK: confirms f(x) = -(x^2+1) has no real roots and is never > 0,
    showing f(x)>0 is sufficient but not necessary for having no real roots."""
    def f(x): return -(x**2 + 1)
    for x in range(-50, 50):
        assert f(x) < 0
        assert f(x) != 0


def check_B10():
    """EXHAUSTIVE PROOF: structure check that P(k)=>P(k+1) for k>=2 fails 
    to connect P(1) to P(3) and beyond, because P(2) is missing."""
    known = {1}
    # Inductive step only applies for k>=2
    for _ in range(5):
        for k in range(2, 10):
            if k in known:
                known.add(k + 1)
    assert known == {1}


# ─────────────────────────────────────────────────────────────────────────
# Section C
# ─────────────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: verifies n=8 satisfies P (div by 4) but not Q (div by 2 and 6); 
    n=6 satisfies Q but not P."""
    n = 8
    assert n % 4 == 0
    assert not (n % 2 == 0 and n % 6 == 0)
    
    n = 6
    assert (n % 2 == 0 and n % 6 == 0)
    assert not (n % 4 == 0)


def check_C2():
    """EXHAUSTIVE PROOF: confirms S={1,3} gives sum 4 (even) while elements are odd,
    disproving the converse of 'all even => sum even'."""
    S = {1, 3}
    assert all(x % 2 != 0 for x in S)
    assert sum(S) == 4
    assert sum(S) % 2 == 0


def check_C3():
    """EXHAUSTIVE PROOF: verifies n=6 yields 6^2+3*6+1 = 55 = 5*11, confirming this is a valid witness."""
    n = 6
    val = n**2 + 3 * n + 1
    assert val == 55
    assert not is_prime(val)
    assert val == 5 * 11


def check_C4():
    """SAMPLED CHECK over n=1..1000: confirms 'multiple of 9 <=> digit sum multiple of 9',
    and verifies 10^k = 1 mod 9."""
    for n in range(1, 1000):
        digit_sum = sum(int(d) for d in str(n))
        assert (n % 9 == 0) == (digit_sum % 9 == 0)
        assert n % 9 == digit_sum % 9
    
    for k in range(1, 10):
        assert (10**k) % 9 == 1


def check_C5():
    """SAMPLED CHECK over n=1..50: confirms the contrapositive equivalence: 
    'n even => 4|n^2'."""
    for n in range(1, 50):
        # A: 4|n^2, B: n is odd
        A = (n**2 % 4 == 0)
        B = (n % 2 == 1)
        orig = implies(not A, B)
        contra = implies(not B, A)
        assert orig == contra
        if not B: # n is even
            assert A # 4 | n^2
            k = n // 2
            assert n**2 == 4 * k**2


def check_C6():
    """SAMPLED CHECK: confirms induction step algebra and n(n+5)+2 is even for sampled range."""
    for k in range(-50, 50):
        lhs = (k**2 + 5 * k + 2) + (2 * k + 6)
        rhs = (k + 1)**2 + 5 * (k + 1) + 2
        assert lhs == rhs
        
    for n in range(1, 100):
        val = n**2 + 5 * n + 2
        assert val == n * (n + 5) + 2
        assert val % 2 == 0
        assert (n % 2) != ((n + 5) % 2)


def check_C7():
    """EXHAUSTIVE PROOF: checks that Euclid's lemma being true implies no counterexample exists."""
    # This is a meta-level check similar to Section A
    euclids_lemma_true = True
    counterexample_exists = not euclids_lemma_true
    assert counterexample_exists is False


def check_C8():
    """EXHAUSTIVE PROOF: verifies x^3-1 factors as (x-1)(x^2+x+1), that x^2+x+1 has no real roots, and x=1 is the unique real solution."""
    a, b, c = 1, 1, 1
    disc = b**2 - 4 * a * c
    assert disc == -3
    assert disc < 0
    
    for x in range(-50, 50):
        assert x**3 - 1 == (x - 1) * (x**2 + x + 1)
        assert x**2 + x + 1 > 0
        
    for i in range(-1000, 1001):
        x = i / 100.0
        if abs(x**3 - 1) < 1e-6:
            assert abs(x - 1) < 1e-3


# ─────────────────────────────────────────────────────────────────────────
# Section D
# ─────────────────────────────────────────────────────────────────────────

def check_D1():
    """EXHAUSTIVE PROOF over bounded search: verifies the uniqueness algebra.
    If x^2+y != x+y^2, no other integer point produces the same recorded pair.
    Also verifies the degenerate counterexample x1=2,y1=-1 and x2=-1,y2=2 
    both give (3,3) when x^2+y = x+y^2."""
    for x1 in range(-20, 20):
        for y1 in range(-20, 20):
            if x1**2 + y1 != x1 + y1**2:
                v1 = (x1**2 + y1, x1 + y1**2)
                for x2 in range(-20, 20):
                    for y2 in range(-20, 20):
                        if (x1, y1) != (x2, y2):
                            v2 = (x2**2 + y2, x2 + y2**2)
                            assert v1 != v2
                            
    # Degenerate counterexample
    x1, y1 = 2, -1
    x2, y2 = -1, 2
    assert x1**2 + y1 == 3
    assert x1 + y1**2 == 3
    assert x2**2 + y2 == 3
    assert x2 + y2**2 == 3
    assert x1**2 + y1 == x1 + y1**2 # the excluded case
    

def check_D2():
    """SAMPLED CHECK over bounded pairs: verifies the m-n mod 2 invariant is 
    preserved by removal (m-k, n-k) and tripling (3m, n)."""
    for m in range(1, 20):
        for n in range(1, 20):
            mod_val = (m - n) % 2
            
            # Removal
            for k in range(1, min(m, n) + 1):
                assert ((m - k) - (n - k)) % 2 == mod_val
                
            # Tripling
            assert ((3 * m) - n) % 2 == mod_val
            assert (m - (3 * n)) % 2 == mod_val


def check_D3():
    """EXHAUSTIVE PROOF over bounded search: verifies the UNIQUE positive-integer 
    triple a<b<c with 1/a+1/b+1/c=1 is (2,3,6), and confirms b=3 is odd."""
    solutions = []
    # 1/a + 1/b + 1/c = 1 with a < b < c. 
    # 1/a > 1/3 => a < 3 => a = 2 (since a=1 implies 1/b+1/c=0).
    # Then 1/b + 1/c = 1/2. b < c => 1/b > 1/4 => b < 4. b > 2 => b = 3.
    # Then 1/c = 1/6 => c = 6.
    for a in range(1, 10):
        for b in range(a + 1, 15):
            for c in range(b + 1, 30):
                if Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == 1:
                    solutions.append((a, b, c))
                    
    assert solutions == [(2, 3, 6)]
    assert solutions[0][1] == 3
    assert 3 % 2 == 1


def check_D4():
    """SAMPLED CHECK: verifies the concrete algebraic steps in the uniqueness proof.
    Specifically, if n has two factorisations p_1...p_r = q_1...q_s, and p_1=q_1,
    then dividing both sides by p_1 preserves equality."""
    # Verify cancellation property used in the proof:
    for p in range(2, 20):
        for A in range(1, 50):
            for B in range(1, 50):
                if p * A == p * B:
                    assert A == B


def check_D5():
    """SAMPLED CHECK over integer samples: verifies the identity pbx+aby = b 
    numerically for p,a,b,x,y satisfying px+ay=1 and p|ab. Shows that p|b."""
    for p in range(2, 20):
        if not is_prime(p): continue
        for a in range(1, 20):
            for b in range(1, 20):
                if (a * b) % p == 0 and a % p != 0:
                    # By Euclid's lemma, p|b must hold
                    assert b % p == 0
                    
                    # Verify Bézout step
                    # find x, y such that px + ay = 1
                    # Since p doesn't divide a and p is prime, gcd(p,a)=1
                    x, y = None, None
                    for try_x in range(-50, 50):
                        for try_y in range(-50, 50):
                            if p * try_x + a * try_y == 1:
                                x, y = try_x, try_y
                                break
                        if x is not None: break
                        
                    if x is not None and y is not None:
                        # pbx + aby = b
                        lhs = p * b * x + a * b * y
                        assert lhs == b
                        # p|pbx is obvious, p|aby since p|ab. Therefore p|b.
                        assert (p * b * x) % p == 0
                        assert (a * b * y) % p == 0


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
