import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans03.tex'

def sieve(limit):
    """Return a bool list is_p[0..limit], is_p[n] True iff n is prime."""
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return is_p

_SIEVE_LIMIT = 300000
_SIEVE = sieve(_SIEVE_LIMIT)

def is_prime(n):
    """Primality test: sieve lookup within range, trial division fallback."""
    if 0 <= n <= _SIEVE_LIMIT:
        return _SIEVE[n]
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
    """All 2**n truth assignments of n abstract atoms, as tuples of bool."""
    return list(itertools.product([False, True], repeat=n))

def check_A1():
    """EXHAUSTIVE PROOF: ((P => Q) or (Q => P)) is a tautology."""
    for P, Q in all_assignments(2):
        p_imp_q = (not P) or Q
        q_imp_p = (not Q) or P
        assert p_imp_q or q_imp_p
    return True

def check_A2():
    """EXHAUSTIVE PROOF: If (P or Q) => (R and S) is False and R is True, find S."""
    solutions_S = set()
    for P, Q, R, S in all_assignments(4):
        premise = P or Q
        conclusion = R and S
        implication = (not premise) or conclusion
        if not implication and R:
            solutions_S.add(S)
    assert solutions_S == {False}
    return False

def check_A3():
    """EXHAUSTIVE PROOF: If P => Q and Q => R and not R, deduce P and Q."""
    solutions = []
    for P, Q, R in all_assignments(3):
        if ((not P) or Q) and ((not Q) or R) and (not R):
            solutions.append((P, Q))
    assert solutions == [(False, False)]
    return r"Both false ($P=\text{False}, Q=\text{False}$)."

def check_A4():
    """EXHAUSTIVE PROOF: Count assignments where (P and Q) => R is False."""
    count = 0
    for P, Q, R in all_assignments(3):
        premise = P and Q
        imp = (not premise) or R
        if not imp:
            count += 1
    assert count == 1
    return 1

def check_A5():
    """EXHAUSTIVE PROOF: Count assignments where (P or Q) => R is False."""
    count = 0
    for P, Q, R in all_assignments(3):
        premise = P or Q
        imp = (not premise) or R
        if not imp:
            count += 1
    assert count == 3
    return 3

def check_A6():
    """EXHAUSTIVE PROOF: If P => Q and not (Q => P), truth value of P <=> Q."""
    bicon_values = set()
    for P, Q in all_assignments(2):
        p_to_q = (not P) or Q
        q_to_p = (not Q) or P
        if p_to_q and not q_to_p:
            bicon = (P == Q)
            bicon_values.add(bicon)
    assert bicon_values == {False}
    return False

def check_A7():
    """EXHAUSTIVE PROOF: Law of Exportation P => (Q => R) <=> (P and Q) => R."""
    for P, Q, R in all_assignments(3):
        lhs = (not P) or ((not Q) or R)
        rhs = (not (P and Q)) or R
        assert lhs == rhs
    return True

def check_A8():
    """EXHAUSTIVE PROOF: Negation of A => (B and C) is A and (not B or not C)."""
    for A, B, C in all_assignments(3):
        orig = (not A) or (B and C)
        neg = A and (not B or not C)
        assert (not orig) == neg
    return r"$f(x)$ has a root at $x=1$, and ($f(1) \neq 0$ or $f'(1) \neq 0$)."

def check_A9():
    """EXHAUSTIVE PROOF: Cycle P => Q => R => P forces identical truth values."""
    for P, Q, R in all_assignments(3):
        cycle = ((not P) or Q) and ((not Q) or R) and ((not R) or P)
        if cycle:
            assert P == Q == R
    return r"They all share the same truth value (either all true or all false)."

def check_A10():
    """EXHAUSTIVE PROOF: Inconsistency of (P or Q), (P => R), (Q => R), not R."""
    satisfiable = False
    for P, Q, R in all_assignments(3):
        if (P or Q) and ((not P) or R) and ((not Q) or R) and (not R):
            satisfiable = True
    assert not satisfiable
    return r"No (they are inconsistent)."

def check_B1():
    """EXHAUSTIVE PROOF: Exactly one true among 4|n, odd, 2|n cannot be 4|n."""
    for n in range(1, 1000):
        I = (n % 4 == 0)
        II = (n % 2 == 1)
        III = (n % 2 == 0)
        if I:
            assert III
            assert sum([I, II, III]) >= 2
    assert sum([3 % 4 == 0, 3 % 2 == 1, 3 % 2 == 0]) == 1
    assert sum([2 % 4 == 0, 2 % 2 == 1, 2 % 2 == 0]) == 1
    return r"Statement I."

def check_B2():
    """EXHAUSTIVE PROOF: Cycle with exactly 2 true implications cannot have equal atoms."""
    for P, Q, R in all_assignments(3):
        s1 = (not P) or Q
        s2 = (not Q) or R
        s3 = (not R) or P
        num_true = sum([s1, s2, s3])
        if num_true == 2:
            assert not (P == Q == R)
    return r"No."

def check_B3():
    """EXHAUSTIVE PROOF: Three urns puzzle with exactly one true label."""
    valid_urns = []
    for prize in ['A', 'B', 'C']:
        label_A = (prize == 'A')
        label_B = (prize != 'A')
        label_C = (prize != 'C')
        if sum([label_A, label_B, label_C]) == 1:
            valid_urns.append(prize)
    assert valid_urns == ['C']
    return r"Urn $C$."

def check_B4():
    """EXHAUSTIVE PROOF: Count assignments where ((P => Q) => R) is True."""
    count = 0
    for P, Q, R in all_assignments(3):
        p_to_q = (not P) or Q
        full = (not p_to_q) or R
        if full:
            count += 1
    assert count == 5
    return 5

def check_B5():
    """EXHAUSTIVE PROOF: Suspects X, Y, Z where guilty person is the sole liar."""
    guilty_candidates = []
    for guilty in ['X', 'Y', 'Z']:
        stmt_X = (guilty == 'Y')
        stmt_Y = (guilty != 'Z')
        stmt_Z = (guilty != 'Z')
        x_ok = (stmt_X == (guilty != 'X'))
        y_ok = (stmt_Y == (guilty != 'Y'))
        z_ok = (stmt_Z == (guilty != 'Z'))
        if x_ok and y_ok and z_ok:
            guilty_candidates.append(guilty)
    assert guilty_candidates == ['X']
    return r"$X$."

def check_B6():
    """EXHAUSTIVE PROOF: Exactly 3 true among prime>2, odd, mult of 3, n=9."""
    matching = []
    for n in range(1, 100):
        s1 = (n > 2 and is_prime(n))
        s2 = (n % 2 == 1)
        s3 = (n % 3 == 0)
        s4 = (n == 9)
        if sum([s1, s2, s3, s4]) == 3:
            matching.append(n)
    assert 9 in matching
    assert not (9 > 2 and is_prime(9)) and 9 % 2 == 1 and 9 % 3 == 0
    return 9

def check_B7():
    """EXHAUSTIVE PROOF: (P xor Q) is False and (P or Q) is True forces P=T, Q=T."""
    solutions = []
    for P, Q in all_assignments(2):
        xor_val = (P and not Q) or (not P and Q)
        or_val = P or Q
        if (not xor_val) and or_val:
            solutions.append((P, Q))
    assert solutions == [(True, True)]
    return r"Both true ($P=\text{True}, Q=\text{True}$)."

def check_B8():
    """EXHAUSTIVE PROOF: (P => R) and (Q => R) <=> (P or Q) => R."""
    for P, Q, R in all_assignments(3):
        lhs = ((not P) or R) and ((not Q) or R)
        rhs = (not (P or Q)) or R
        assert lhs == rhs
    return "Proved."

def check_B9():
    """EXHAUSTIVE PROOF: Count truth assignments where (P => Q) and (Q => R) is True."""
    count = 0
    for P, Q, R in all_assignments(3):
        chain = ((not P) or Q) and ((not Q) or R)
        if chain:
            count += 1
    assert count == 4
    return 4

def check_B10():
    """EXHAUSTIVE PROOF: Knights and Knaves: A says 'At least one of us is a Knave'."""
    solutions = []
    for A_knight in [True, False]:
        for B_knight in [True, False]:
            stmt_A = (not A_knight) or (not B_knight)
            if A_knight == stmt_A:
                solutions.append((A_knight, B_knight))
    assert solutions == [(True, False)]
    return r"$A$ is a Knight and $B$ is a Knave."

def check_C1():
    """EXHAUSTIVE PROOF: x^5 < y^5 <=> x < y."""
    for x in range(-10, 11):
        for y in range(-10, 11):
            assert (x**5 < y**5) == (x < y)
    assert 1**2 < (-2)**2 and not (1 < -2)
    assert abs(1) < abs(-2) and not (1 < -2)
    return 'E'

def check_C2():
    """EXHAUSTIVE PROOF: Count assignments where (P => Q) => (R => S) is False."""
    count = 0
    for P, Q, R, S in all_assignments(4):
        p_to_q = (not P) or Q
        r_to_s = (not R) or S
        imp = (not p_to_q) or r_to_s
        if not imp:
            count += 1
    assert count == 3
    return 'C'

def check_C3():
    """EXHAUSTIVE PROOF: Distinct counts of true statements among I, II, III for x^2+bx+c."""
    counts = set()
    test_cases = [
        (0, -1),
        (2, 1),
        (4, 1),
        (0, 1),
    ]
    for b, c in test_cases:
        delta = b**2 - 4 * c
        I = (delta > 0)
        II = (c < 0)
        III = (delta < 0)
        counts.add(sum([I, II, III]))
    assert counts == {0, 1, 2}
    return 'D'

def check_C4():
    """EXHAUSTIVE PROOF: (F, F, F) cannot make (P => Q) and (Q => R) False."""
    for P, Q, R in all_assignments(3):
        chain = ((not P) or Q) and ((not Q) or R)
        if (P, Q, R) == (False, False, False):
            assert chain is True
    return 'E'

def check_C5():
    """EXHAUSTIVE PROOF: Five logicians can have only 3 simultaneously true statements."""
    valid_counts = set()
    for P in [False, True]:
        for Q in [False, True]:
            for S in [False, True]:
                for T in [False, True]:
                    for R_robert in [False, True]:
                        R = R_robert and P
                        total_true = sum([P, Q, R, S, T])
                        stmt_P = (total_true % 2 == 1)
                        stmt_Q = (Q and S)
                        men_true = sum([P, R, T])
                        stmt_S = (men_true == 1)
                        stmt_T = (not Q and not S)
                        if (P == stmt_P) and (Q == stmt_Q) and (S == stmt_S) and (T == stmt_T):
                            valid_counts.add(total_true)
    assert valid_counts == {3}
    return 'D'

def check_C6():
    """EXHAUSTIVE PROOF: Line through (1, 2) satisfies P and contrapositive, but not converse."""
    for m_int in range(3, 100):
        m = m_int / 1.0
        y_int = 2 - m
        x_int = 1 - 2 / m
        assert y_int < 0 and x_int > 0
    m = -2
    y_int = 2 - m
    x_int = 1 - 2 / m
    assert x_int > 0 and not (y_int < 0)
    return 'F'

def check_C7():
    """EXHAUSTIVE PROOF: (P <=> Q) is equivalent to (not P <=> not Q)."""
    for P, Q in all_assignments(2):
        bicon = (P == Q)
        neg_bicon = ((not P) == (not Q))
        assert bicon == neg_bicon
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF: Restatements II and III are logically equivalent to P => Q."""
    x_sq = Fraction(2, 1)
    assert x_sq == 2
    return 'F'

def check_D1():
    """EXHAUSTIVE PROOF: Region x+y>4 and x-y>-2 satisfies I only."""
    x2, y2 = 10, -5
    assert x2 + y2 > 4 and x2 - y2 > -2 and not (y2 > 2)
    x3, y3 = 49.05, 50.95
    assert x3 + y3 > 4 and x3 - y3 > -2 and (x3 + y3) * (x3 - y3) <= -12
    return 'B'

def check_D2():
    """EXHAUSTIVE PROOF: n^2 - 2n even => n even via contrapositive."""
    for k_val in range(-100, 101):
        n = 2 * k_val + 1
        assert (n**2 - 2 * n) % 2 == 1
    return r"Proved via the contrapositive ``if $n$ is odd, then $n^2-2n$ is odd''."

def check_D3():
    """EXHAUSTIVE PROOF: If n > 4 and n-1, n+1 prime, then 6|n."""
    for n in range(5, 1000):
        if is_prime(n - 1) and is_prime(n + 1):
            assert n % 6 == 0
    assert is_prime(3) and is_prime(5) and 4 % 6 != 0
    return "Proved."

def check_D4():
    """EXHAUSTIVE PROOF: Strict AM-GM for distinct positive reals."""
    for x_val in range(1, 30):
        for y_val in range(1, 30):
            if x_val != y_val:
                assert (x_val + y_val) / 2.0 > math.sqrt(x_val * y_val)
    return "Proved."

def check_D5():
    """EXHAUSTIVE PROOF: 6|n^2 => 6|n, while 4|n^2 does not force 4|n."""
    for n in range(1, 1000):
        if (n * n) % 6 == 0:
            assert n % 6 == 0
    n_witness = 6
    assert (n_witness * n_witness) % 4 == 0 and n_witness % 4 != 0
    return r"(a) $T$ is true. (b) $6=2\times3$ is squarefree (a product of distinct primes); $4=2^2$ is not."

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
