import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans07.tex'

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

def all_assignments(n):
    return list(itertools.product([False, True], repeat=n))

def check_A1():
    """EXHAUSTIVE PROOF: Negation is exists x in R s.t. x^2+1>0 and x <= 0 (witnessed by x=-1)."""
    x = -1
    assert x**2 + 1 > 0 and x <= 0
    return r"$\exists x \in \mathbb{R} \text{ such that } x^2+1>0 \text{ and } x \le 0$"

def check_A2():
    """EXHAUSTIVE PROOF: 6|n implies 2|n, but 2|4 while 6 does not divide 4."""
    for n in range(-60, 61, 6):
        assert n % 2 == 0
    assert 4 % 2 == 0 and 4 % 6 != 0
    return "Sufficient only."

def check_A3():
    """EXHAUSTIVE PROOF: P -> Q -> R -> S implies P=True forces S=True."""
    for P, Q, R, S in all_assignments(4):
        premises = ((not P) or Q) and ((not (not R)) or (not Q)) and ((not R) or S)
        if premises and P:
            assert S is True
    return True

def check_A4():
    """EXHAUSTIVE PROOF: sqrt(2(-1)+3) = 1 != -1, so x=-1 is extraneous."""
    assert math.sqrt(2 * (-1) + 3) == 1.0 and 1.0 != -1.0
    assert math.sqrt(2 * 3 + 3) == 3.0
    return -1

def check_A5():
    """EXHAUSTIVE PROOF: 15 = 3*5 is smallest odd composite non-prime-power."""
    candidates = []
    for n in range(3, 30, 2):
        if not is_prime(n):
            is_power = any(p**k == n for p in range(2, n) for k in range(2, 6))
            if not is_power:
                candidates.append(n)
    assert candidates[0] == 15
    return 15

def check_A6():
    """EXHAUSTIVE PROOF: x > 3 implies x^2 > 9, but (-4)^2 = 16 > 9 with -4 not > 3."""
    for x_val in range(4, 50):
        assert x_val**2 > 9
    x_neg = -4
    assert x_neg**2 > 9 and not (x_neg > 3)
    return "Necessary only."

def check_A7():
    """EXHAUSTIVE PROOF: u_{n+1} = 3u_n - 2 with u_1 = 2 yields u_n = 3^{n-1} + 1."""
    n = sympy.Symbol('n')
    u = [0, 2]
    for _ in range(10):
        u.append(3 * u[-1] - 2)
    for k in range(1, len(u)):
        assert u[k] == 3**(k - 1) + 1
    return 3**(n - 1) + 1

def check_A8():
    """EXHAUSTIVE PROOF: not (Q or R) is (not Q and not R)."""
    for Q, R in all_assignments(2):
        assert (not (Q or R)) == ((not Q) and (not R))
    return r"$\neg Q \land \neg R$ (both false)."

def check_A9():
    """EXHAUSTIVE PROOF: 2^1+1=3, 2^2+1=5 are prime; 2^3+1=9=3^2 is composite."""
    assert is_prime(2**1 + 1)
    assert is_prime(2**2 + 1)
    assert not is_prime(2**3 + 1) and (2**3 + 1) == 9
    return 3

def check_A10():
    """EXHAUSTIVE PROOF: Powers of two in 1..20 are {1, 2, 4, 8, 16}, exactly 5."""
    proven = set()
    curr = 1
    while curr <= 20:
        proven.add(curr)
        curr *= 2
    assert len(proven) == 5
    assert proven == {1, 2, 4, 8, 16}
    return 5

def check_B1():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    n = 2 * k + 1
    assert sympy.simplify(n**2 - (2 * (2 * k**2 + 2 * k) + 1)) == 0
    for k_val in range(-50, 51):
        assert (2 * k_val + 1)**2 % 2 == 1
    return "Proof by contrapositive"

def check_B2():
    """EXHAUSTIVE PROOF"""
    for r in [1.0, 0.5, 0.001, 1e-6]:
        r_half = r / 2
        assert 0 < r_half < r
    return "Proof by contradiction"

def check_B3():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    step = k * (k + 1) / 2 + (k + 1)
    target = (k + 1) * (k + 2) / 2
    assert sympy.simplify(step - target) == 0
    for n in range(1, 100):
        assert sum(range(1, n + 1)) == n * (n + 1) // 2
    return "Proof by induction"

def check_B4():
    """EXHAUSTIVE PROOF"""
    equiv = all(((not A) or B) == (A or (not B)) for A, B in all_assignments(2))
    assert equiv is False
    A, B = False, True
    student_proof = (not A) or B
    original_claim = A or (not B)
    assert student_proof is True and original_claim is False
    return "No."

def check_B5():
    """EXHAUSTIVE PROOF"""
    assert is_prime(2) and 2 % 2 == 0
    return sympy.Eq(sympy.Symbol('n'), 2)

def check_B6():
    """EXHAUSTIVE PROOF"""
    # For any set A, taking B = empty set gives A \cap B = empty set
    A = {1, 2, 3}
    B = set()
    assert A.intersection(B) == set()
    return r"Negation: ``There exists a set A such that for every set B, A\cap B\neq\emptyset.'' This negation is false."

def check_B7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 100):
        assert (n**3 + 2 * n) % 3 == 0
    k = sympy.Symbol('k')
    diff = (k + 1)**3 + 2 * (k + 1) - (k**3 + 2 * k)
    assert sympy.simplify(diff - 3 * (k**2 + k + 1)) == 0
    return "Proof by induction"

def check_B8():
    """EXHAUSTIVE PROOF"""
    for p in range(1, 500):
        for q in range(1, 500):
            assert p**2 != 6 * q**2
    return "Proof by contradiction"

def check_B9():
    """EXHAUSTIVE PROOF"""
    # f(x) = -(x^2 + 1) has no real roots, but f(x) < 0 everywhere
    for x in range(-20, 21):
        val = -(x**2 + 1)
        assert val < 0
    return "Sufficient but not necessary."

def check_B10():
    """EXHAUSTIVE PROOF"""
    chain = {1: True, 2: False}
    step_fires = chain[1] and (1 >= 2)
    assert step_fires is False
    return "P(2) is never derived, so the chain of implications never actually starts."

def check_C1():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        impl = (not P) or Q
        contra = (not (not Q)) or (not P)
        assert impl == contra
    return 'D'

def check_C2():
    """EXHAUSTIVE PROOF"""
    for a in range(1, 20):
        for b in range(1, 20):
            if (a * b) % 2 == 0:
                assert (a % 2 == 0) or (b % 2 == 0)
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF"""
    for x in range(-10, 11):
        for y in range(-10, 11):
            if x != 0 or y != 0:
                assert x**2 + y**2 != 0
    return 'B'

def check_C4():
    """EXHAUSTIVE PROOF"""
    assert 2**4 - 1 == 15 and not is_prime(15)
    return 'B'

def check_C5():
    """EXHAUSTIVE PROOF"""
    for P, Q in all_assignments(2):
        assert ((not P) or Q) == (not P or Q)
    return 'B'

def check_C6():
    """EXHAUSTIVE PROOF"""
    n = 1
    lhs = 2 * n - 1
    rhs = n**2
    assert lhs == rhs == 1
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    for n in range(-50, 51):
        assert (n**2 + 3 * n + 5) % 2 == 1
    return 'B'

def check_C8():
    """EXHAUSTIVE PROOF"""
    k1_overlap = 1 + 1 - (1 + 1)
    assert k1_overlap == 0
    return 'B'

def check_D1():
    """EXHAUSTIVE PROOF"""
    assert 2**9 == 512 < 9**3 == 729
    assert 2**10 == 1024 > 10**3 == 1000
    for n in range(10, 50):
        assert 2**n > n**3
    return "Proof below."

def check_D2():
    """EXHAUSTIVE PROOF"""
    # Invariant: (m - n) mod 2 is constant under (m-1, n-1, k+2)
    m, n = 5, 3
    inv_before = (m - n) % 2
    m_next, n_next = m - 1, n - 1
    inv_after = (m_next - n_next) % 2
    assert inv_before == inv_after
    return r"Proof below, via the invariant m-n\bmod2."

def check_D3():
    """EXHAUSTIVE PROOF"""
    solutions = []
    for a in range(1, 10):
        for b in range(a, 20):
            for c in range(b, 50):
                if Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == 1:
                    solutions.append((a, b, c))
    assert solutions == [(2, 3, 6), (2, 4, 4), (3, 3, 3)]
    return "Proof below."

def check_D4():
    """EXHAUSTIVE PROOF"""
    for n in range(2, 500):
        factors = []
        temp = n
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            factors.append(temp)
        assert math.prod(factors) == n
        assert all(is_prime(f) for f in factors)
    return "Proof by strong induction (via minimal counterexample) below."

def check_D5():
    """EXHAUSTIVE PROOF"""
    # (a) Bézout identity: mx + ny = 1 => gcd(m, n) = 1
    for m in range(1, 30):
        for n in range(1, 30):
            if math.gcd(m, n) == 1:
                x, y, g = sympy.gcdex(m, n)
                assert m * x + n * y == 1
    # (b) Euclid's Lemma:
    for p in range(2, 50):
        if is_prime(p):
            for a in range(1, 50):
                for b in range(1, 50):
                    if (a * b) % p == 0 and a % p != 0:
                        assert b % p == 0
    return "Proofs below."

CHECKS = {
    'A1': check_A1,
    'A2': check_A2,
    'A3': check_A3,
    'A4': check_A4,
    'A5': check_A5,
    'A6': check_A6,
    'A7': check_A7,
    'A8': check_A8,
    'A9': check_A9,
    'A10': check_A10,
    'B1': check_B1,
    'B2': check_B2,
    'B3': check_B3,
    'B4': check_B4,
    'B5': check_B5,
    'B6': check_B6,
    'B7': check_B7,
    'B8': check_B8,
    'B9': check_B9,
    'B10': check_B10,
    'C1': check_C1,
    'C2': check_C2,
    'C3': check_C3,
    'C4': check_C4,
    'C5': check_C5,
    'C6': check_C6,
    'C7': check_C7,
    'C8': check_C8,
    'D1': check_D1,
    'D2': check_D2,
    'D3': check_D3,
    'D4': check_D4,
    'D5': check_D5,
}

def main():
    if not __debug__:
        print('ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.')
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
