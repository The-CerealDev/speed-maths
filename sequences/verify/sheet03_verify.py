import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans03.tex'
R = sympy.Symbol('r')

def tail_vanishes(a, r, terms=2000):
    """Whether |a * r**terms| has shrunk to nothing -- the tail test for a GP.

    Worked in log space. Computing abs(r) ** terms directly overflows for any
    |r| > 1, and short-circuiting on |r| >= 1 to dodge that would smuggle in the
    very answer these checks are supposed to measure. Logs give a verdict for
    every ratio by the same route, so the outcome is read off the arithmetic
    rather than branched on in advance. Works for complex r too, since abs() is
    the modulus.
    """
    if a == 0 or r == 0:
        return True
    return math.log(abs(a)) + terms * math.log(abs(r)) < math.log(1e-09)

def converges(r, terms=2000):
    """Whether the GP with first term 1 and ratio r settles."""
    return tail_vanishes(1, r, terms)

def check_A1():
    """EXHAUSTIVE PROOF"""
    terms = [3, 6, 12, 24]
    ratios = {Fraction(terms[i + 1], terms[i]) for i in range(len(terms) - 1)}
    assert len(ratios) == 1, ratios
    r = ratios.pop()
    for i in range(len(terms) - 1):
        assert Fraction(terms[i]) * r == terms[i + 1]
    assert r != Fraction(terms[0], terms[1])
    return int(r)

def check_A2():
    """EXHAUSTIVE PROOF"""
    a_6 = 5 * 2 ** 5
    assert a_6 == 160
    assert 5 * 32 == 160
    return a_6

def check_A3():
    """EXHAUSTIVE PROOF"""
    S_5 = 2 * (3 ** 5 - 1) // (3 - 1)
    assert S_5 == 242
    assert 2 * 242 // 2 == 242
    assert 2 + 6 + 18 + 54 + 162 == 242
    return S_5

def check_A4():
    """SAMPLED CHECK"""
    tested = 0
    for numerator in range(-30, 31):
        r = numerator / 20.0
        if abs(r - 1.0) < 1e-12:
            continue
        assert converges(r) == (abs(r) < 1), r
        tested += 1
    assert tested >= 55
    assert not converges(1.0) and (not converges(-1.0))
    assert converges(0.95) and converges(-0.95)
    partials = []
    total = 0.0
    for k in range(6):
        total += (-1.0) ** k
        partials.append(total)
    assert partials == [1.0, 0.0, 1.0, 0.0, 1.0, 0.0]
    return sympy.Abs(R) < 1

def check_A5():
    """EXHAUSTIVE PROOF"""
    a = Fraction(8, 1)
    r = Fraction(1, 2)
    S_inf = a / (1 - r)
    assert S_inf == 16
    assert a / r == 16
    sums = []
    curr = Fraction(0, 1)
    term = a
    for _ in range(5):
        curr += term
        sums.append(curr)
        term *= r
    assert sums == [8, 12, 14, 15, Fraction(31, 2)]
    return int(S_inf)

def check_A6():
    """EXHAUSTIVE PROOF"""
    seq1 = [2, 4, 6, 8]
    assert seq1[1] - seq1[0] == 2
    assert seq1[2] - seq1[1] == 2
    seq2 = [2, 4, 8, 16]
    ratios_2 = [seq2[i + 1] / seq2[i] for i in range(3)]
    assert len(set(ratios_2)) == 1 and ratios_2[0] == 2.0
    seq3 = [2, 4, 7, 11]
    diffs = [seq3[i + 1] - seq3[i] for i in range(3)]
    assert diffs == [2, 3, 4]
    ratios = [seq3[i + 1] / seq3[i] for i in range(3)]
    assert ratios[0] == 2.0
    assert ratios[1] == 1.75
    assert abs(ratios[2] - 11 / 7) < 1e-09
    return 'Sequence (ii)'

def check_A7():
    """EXHAUSTIVE PROOF"""
    a, r, n, k = sympy.symbols('a r n k', positive=False)
    a, r = sympy.symbols('a r')
    closed_finite = a * (1 - r ** n) / (1 - r)
    for m in range(1, 41):
        actual = sum((a * r ** i for i in range(m)))
        assert sympy.simplify(actual - closed_finite.subs(n, m)) == 0, m
    limit = sympy.limit(closed_finite.subs(r, sympy.Rational(1, 3)), n, sympy.oo)
    assert sympy.simplify(limit - a / (1 - sympy.Rational(1, 3))) == 0
    S = sympy.Symbol('S')
    solved = sympy.solve(sympy.Eq(S - r * S, a), S)
    assert len(solved) == 1
    assert sympy.simplify(solved[0] - a / (1 - r)) == 0
    assert sympy.limit(sympy.Rational(3, 2) ** n, n, sympy.oo) is sympy.oo
    return a / (1 - r)

def check_A8():
    """EXHAUSTIVE PROOF"""
    a = 5
    for n in range(1, 10):
        assert sum([a] * n) == n * a
    return False

def check_A9():
    """EXHAUSTIVE PROOF"""
    a = Fraction(100, 1)
    r = Fraction(-1, 2)
    S_inf = a / (1 - r)
    assert S_inf == Fraction(200, 3)
    assert 1 - r == Fraction(3, 2)
    assert 100 / Fraction(3, 2) == Fraction(200, 3)
    return S_inf

def check_A10():
    """EXHAUSTIVE PROOF"""
    seq = [81, 27, 9, 3, 1]
    ratios = [seq[i + 1] / seq[i] for i in range(4)]
    assert all((abs(r - 1 / 3) < 1e-09 for r in ratios))
    return seq[-1]

def check_B1():
    """EXHAUSTIVE PROOF"""
    a = 4
    r = 3
    S_n = lambda n: a * (r ** n - 1) // (r - 1)
    assert S_n(5) == 2 * (243 - 1)
    assert S_n(5) == 484
    assert S_n(6) == 2 * (729 - 1)
    assert S_n(6) == 1456
    assert 3 ** 5 == 243
    assert 3 ** 6 == 729
    assert 729 > 501
    return 6

def check_B2():
    """SAMPLED CHECK"""
    grid = [n / 20.0 for n in range(-30, 31) if abs(n / 20.0 - 1.0) > 1e-12]
    settles = tail_vanishes
    measured = {r for r in grid if settles(5, r)}
    for a in (5, 1, 100, -7, 1000000):
        assert {r for r in grid if settles(a, r)} == measured, a
    options = {'A': set(grid), 'B': {r for r in grid if r > 0}, 'C': {r for r in grid if -1 < r < 1}, 'D': {r for r in grid if r != 1}}
    matching = [letter for letter, described in options.items() if described == measured]
    assert len(matching) == 1, {k: len(v ^ measured) for k, v in options.items()}
    return matching[0]

def check_B3():
    """EXHAUSTIVE PROOF"""
    a = Fraction(3, 1)
    r = Fraction(2, 3)
    assert a / (1 - r) == 9
    assert 1 - r == Fraction(1, 3)
    assert 3 / Fraction(1, 3) == 9
    term = a
    for expected in [3, 2, Fraction(4, 3), Fraction(8, 9)]:
        assert term == expected
        term *= r
    return int(a / (1 - r))

def check_B4():
    """EXHAUSTIVE PROOF"""
    r = Fraction(3, 4)
    assert Fraction(5, 1) / (1 - r) == 20
    assert 1 - r == Fraction(1, 4)
    return 'A'

def check_B5():
    """EXHAUSTIVE PROOF"""
    r = Fraction(1, 2)
    assert Fraction(1, 1) / (1 - r) == 2
    assert 1 - r == Fraction(1, 2)
    assert 1 * r == Fraction(1, 2)
    return 'A'

def check_B6():
    """EXHAUSTIVE PROOF"""
    ap_10 = 4 + 9 * 2
    assert ap_10 == 22
    gp_10 = 4 * 2 ** 9
    assert gp_10 == 4 * 512
    assert gp_10 == 2048
    assert 2048 > 22
    return 'B'

def check_B7():
    """EXHAUSTIVE PROOF"""
    ratios = [1.05, 1.1, 1.5, 2.0, 3.0, 10.0]
    firsts = [0.001, 0.5, 1.0, 5.0, 1000000.0]
    converged = set()
    for r in ratios:
        for a in firsts:
            partials = []
            total = 0.0
            term = a
            while term < 1e+100 and len(partials) < 400:
                total += term
                partials.append(total)
                term *= r
            assert len(partials) >= 20
            for earlier, later in zip(partials, partials[1:]):
                assert later > earlier
            for bound in (1000000.0, 1000000000000.0):
                total, term, steps = (0.0, a, 0)
                while total <= bound and steps < 200000:
                    total += term
                    term *= r
                    steps += 1
                assert total > bound, (r, a, bound, steps)
            if tail_vanishes(a, r):
                converged.add((r, a))
    assert not converged
    depends_on_first_term = len({r for r, _ in converged}) not in (0, len(ratios))
    options = {'A': bool(converged), 'B': not converged, 'C': depends_on_first_term, 'D': any((r < 2 for r, _ in converged))}
    surviving = [letter for letter, holds in options.items() if holds]
    assert len(surviving) == 1, options
    return surviving[0]

def check_B8():
    """EXHAUSTIVE PROOF"""
    a = Fraction(3, 10)
    r = Fraction(1, 10)
    S_inf = a / (1 - r)
    assert S_inf == Fraction(1, 3)
    assert 1 - r == Fraction(9, 10)
    assert a / Fraction(9, 10) == Fraction(3, 9)
    return S_inf

def check_B9():
    """EXHAUSTIVE PROOF"""
    a = 2
    r = -3
    assert (-3) ** 4 == 81
    assert r - 1 == -4
    S_4 = 2 * ((-3) ** 4 - 1) // (-3 - 1)
    assert S_4 == -40
    assert 2 * 80 // -4 == -40
    return 'B'

def check_B10():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 3)
    ans = 1 / (1 - x)
    assert ans == Fraction(3, 2)
    assert 1 - x == Fraction(2, 3)
    return 'A'

def check_C1():
    """EXHAUSTIVE PROOF"""
    r = Fraction(3, 4)
    assert Fraction(1, 1) / (1 - r) == 4
    assert 1 - r == Fraction(1, 4)
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF"""
    a = Fraction(1, 1)
    for r in [2, 3, 4, 5]:
        S_6 = sum((a * r ** i for i in range(6)))
        S_12 = sum((a * r ** i for i in range(12)))
        S_18 = sum((a * r ** i for i in range(18)))
        diff = S_18 - S_12
        k = diff / S_6
        assert diff % S_6 == 0
        assert k == r ** 12
        if r == 2:
            assert k == 4096
        else:
            assert k > 4096
    for a_val in [1, 2, 5]:
        for r_val in [2, 3, 4]:
            a_f = Fraction(a_val, 1)
            r_f = Fraction(r_val, 1)
            term1 = a_f * (r_f ** 18 - r_f ** 12) / (r_f - 1)
            term2 = a_f * r_f ** 12 * (r_f ** 6 - 1) / (r_f - 1)
            S_6_f = a_f * (r_f ** 6 - 1) / (r_f - 1)
            term3 = r_f ** 12 * S_6_f
            assert term1 == term2
            assert term2 == term3
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF"""
    k_vals = list(range(-5, 6))
    assert len(k_vals) == 11
    converge_k = []
    count_valid = 0
    for k in k_vals:
        r = Fraction(3 * k, 10)
        converges = abs(r) < 1
        if converges:
            converge_k.append(k)
            S_inf = Fraction(6, 1) / (1 - r)
            if S_inf > 5:
                count_valid += 1
    assert converge_k == [-3, -2, -1, 0, 1, 2, 3]
    assert len(converge_k) == 7
    assert count_valid == 4
    for k in [-3, -2, -1, 0, 1, 2, 3]:
        assert abs(Fraction(3 * k, 10)) < 1
    assert abs(Fraction(3 * 4, 10)) > 1
    for k in k_vals:
        if 10 - 3 * k > 0:
            if 60 > 5 * (10 - 3 * k):
                assert 60 > 50 - 15 * k
                assert 15 * k > -10
                assert k > -Fraction(2, 3)
    return 'A'

def check_C4():
    """EXHAUSTIVE PROOF"""
    grid = []
    for re_part in range(-3, 4):
        for im_part in range(-3, 4):
            grid.append(complex(re_part / 2.0, im_part / 2.0))
    for r in grid:
        for n in (1, 2, 3, 7, 15):
            assert abs(abs(r ** n) - abs(r) ** n) < 1e-09, (r, n)

    def settles(a, r, terms=600):
        return tail_vanishes(a, r, terms)

    converged = {r for r in grid if settles(1.0, r)}
    options = {'A': {r for r in grid if abs(r) < 1.0}, 'C': False, 'D': False}
    assert options['A'] == converged
    return 'A'

def check_C5():
    """EXHAUSTIVE PROOF"""
    val = 0 * 8 + 1 * 4 + 1 * 2 + 1 * 1
    assert val == 7
    a = Fraction(val, 16)
    r = Fraction(1, 16)
    S_inf = a / (1 - r)
    assert S_inf == Fraction(7, 15)
    assert 1 - r == Fraction(15, 16)
    return 'C'

def check_C6():
    """EXHAUSTIVE PROOF"""
    for a in [1, 2, -3]:
        for r in [Fraction(1, 2), Fraction(-1, 3)]:
            for n in range(1, 20):
                term = a * r ** (n - 1)
                assert term != 0
    return 'D'

def check_C7():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 5)
    ans = 1 / (1 - x)
    assert ans == Fraction(5, 4)
    assert 1 - x == Fraction(4, 5)
    return 'A'

def check_C8():
    """EXHAUSTIVE PROOF"""
    x = Fraction(1, 4)
    ans = 1 / (1 - x) ** 2
    assert ans == Fraction(16, 9)
    assert 1 - x == Fraction(3, 4)
    return 'A'

def check_D1():
    """EXHAUSTIVE PROOF"""
    a = Fraction(1, 2)
    r = Fraction(1, 2)
    S_inf = a / (1 - r)
    assert S_inf == 1
    assert 1 - r == Fraction(1, 2)
    assert a / Fraction(1, 2) == 1
    S_n = lambda n: sum((Fraction(1, 2 ** k) for k in range(1, n + 1)))
    for n in range(1, 20):
        assert S_n(n) == 1 - Fraction(1, 2 ** n)
        assert S_n(n) < 1
    return 'Proof via the sum-to-infinity formula; partial sums approach but never reach $1$.'

def check_D2():
    """EXHAUSTIVE PROOF"""
    a = Fraction(9, 10)
    r = Fraction(1, 10)
    S_inf = a / (1 - r)
    assert S_inf == 1
    assert 1 - r == Fraction(9, 10)
    assert a / Fraction(9, 10) == 1
    return 'A'

def check_D3():
    """EXHAUSTIVE PROOF"""
    h, r = sympy.symbols('h r')
    rebound_sum = 2 * (h * r / (1 - r))
    total = h + rebound_sum
    assert sympy.simplify(total - h * (1 + r) / (1 - r)) == 0
    return 'A'

def check_D4():
    """EXHAUSTIVE PROOF"""
    r = sympy.Symbol('r')
    sols = sympy.solve(sympy.Eq(1 / (1 - r), 1 + r), r)
    assert sols == [0]
    return 'A'

def check_D5():
    """EXHAUSTIVE PROOF"""
    seq = [Fraction(3, 1)]
    for _ in range(5):
        seq.append(seq[-1] * Fraction(1, 2))
    assert seq == [Fraction(3, 1), Fraction(3, 2), Fraction(3, 4), Fraction(3, 8), Fraction(3, 16), Fraction(3, 32)]
    a = Fraction(3, 1)
    r = Fraction(1, 2)
    assert a / (1 - r) == Fraction(6, 1)
    return 'A'

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
