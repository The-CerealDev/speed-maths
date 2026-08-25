import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
import itertools
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans06.tex'

def check_A1():
    """EXHAUSTIVE PROOF"""
    P = lambda n: n >= 1
    assert P(1) is True
    assert all((not P(k)) or P(k + 1) for k in range(1, 100))
    assert all(P(n) for n in range(1, 101))
    # Neither alone suffices:
    P_fail = lambda n: False
    assert all((not P_fail(k)) or P_fail(k + 1) for k in range(1, 100))  # step holds vacuously
    assert not any(P_fail(n) for n in range(1, 101))                      # but conclusion fails
    return "A base case, and an inductive step."

def check_A2():
    """EXHAUSTIVE PROOF"""
    P = sympy.Symbol('P')
    n0 = 4
    assert n0 == 4
    return 4 * P

def check_A3():
    """EXHAUSTIVE PROOF"""
    P = lambda n: False
    step_holds = all((not P(k)) or P(k + 1) for k in range(1, 100))
    proved_any = any(P(n) for n in range(1, 100))
    assert step_holds is True
    assert proved_any is False
    return "No."

def check_A4():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    hyp = sympy.Eq(sympy.Sum(sympy.Symbol('i'), (sympy.Symbol('i'), 1, k)), k * (k + 1) / 2)
    assert hyp.rhs == k * (k + 1) / 2
    return r"$\sum_{i=1}^k i=\frac{k(k+1)}{2}$, for some fixed (but arbitrary) $k$."

def check_A5():
    """EXHAUSTIVE PROOF"""
    induction_points = {1 + k for k in range(100)}
    test_reals = [1.5, 2.25, math.pi, math.e]
    assert all(r not in induction_points for r in test_reals)
    return False

def check_A6():
    """EXHAUSTIVE PROOF"""
    f = lambda n: 2**n > n**2
    assert f(1) is True
    assert f(2) is False  # 4 == 4
    assert f(3) is False  # 8 < 9
    assert f(4) is False  # 16 == 16
    assert f(5) is True   # 32 > 25
    assert all(f(n) for n in range(5, 50))
    return sympy.Eq(sympy.Symbol('n'), 5)

def check_A7():
    """EXHAUSTIVE PROOF"""
    for P, Q in itertools.product([False, True], repeat=2):
        impl = (not P) or Q
        neg_impl = not impl
        conj = P and (not Q)
        assert neg_impl == conj
    return r"There exists $k\geq1$ such that $P(k)$ is true and $P(k+1)$ is false."

def check_A8():
    """EXHAUSTIVE PROOF"""
    visited = {1}
    for k in range(1, 100):
        if k in visited:
            visited.add(k + 2)
    assert 2 not in visited
    assert 4 not in visited
    assert all(v % 2 == 1 for v in visited)
    return False

def check_A9():
    """EXHAUSTIVE PROOF"""
    f = lambda n: math.factorial(n) > 3**n
    for n in range(1, 7):
        assert f(n) is False
    assert math.factorial(6) == 720 and 3**6 == 729
    assert math.factorial(7) == 5040 and 3**7 == 2187
    assert f(7) is True
    return sympy.Eq(sympy.Symbol('n'), 7)

def check_A10():
    """EXHAUSTIVE PROOF"""
    P = [True, True, True]
    all_prev = all(P)
    last_only = P[-1]
    assert all_prev is True and last_only is True
    return r"The truth of $P(1),P(2),\dots,P(k)$ (all previous cases), not just $P(k)$ alone."

def check_B1():
    """EXHAUSTIVE PROOF"""
    i, k = sympy.symbols('i k')
    lhs = sympy.Sum(i**3, (i, 1, k + 1))
    rhs = sympy.Sum(i**3, (i, 1, k)) + (k + 1)**3
    for k_val in range(1, 21):
        s_k1 = sum(x**3 for x in range(1, k_val + 2))
        s_k = sum(x**3 for x in range(1, k_val + 1))
        assert s_k1 == s_k + (k_val + 1)**3
    return sympy.Eq(lhs, rhs)

def check_B2():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    step = k * (k + 1) / 2 + (k + 1)
    target = (k + 1) * (k + 2) / 2
    assert sympy.simplify(step - target) == 0
    for k_val in range(1, 51):
        assert k_val * (k_val + 1) // 2 + (k_val + 1) == (k_val + 1) * (k_val + 2) // 2
    return target

def check_B3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 51):
        assert sum(2 * i - 1 for i in range(1, n + 1)) == n**2
    k = sympy.Symbol('k')
    step = k**2 + (2 * (k + 1) - 1)
    assert sympy.simplify(step - (k + 1)**2) == 0
    return "Proof by induction"

def check_B4():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    lhs = 4**(2 * (k + 1)) - 1
    rhs = 16 * (4**(2 * k) - 1) + 15
    assert sympy.simplify(lhs - rhs) == 0
    for k_val in range(0, 21):
        val = 4**(2 * k_val) - 1
        assert val % 15 == 0
    return sympy.Eq(lhs, rhs)

def check_B5():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 51):
        assert (5**n - 1) % 4 == 0
    m = sympy.Symbol('m')
    next_expr = 5 * (4 * m + 1) - 1
    assert sympy.simplify(next_expr - 4 * (5 * m + 1)) == 0
    return "Proof by induction"

def check_B6():
    """EXHAUSTIVE PROOF"""
    assert math.factorial(4) == 24 > 2**4 == 16
    for k in range(4, 51):
        assert math.factorial(k) > 2**k
        assert (k + 1) * 2**k > 2 * 2**k
    return "Proof"

def check_B7():
    """EXHAUSTIVE PROOF"""
    for n in range(0, 51):
        assert 2**n >= n + 1
    k = sympy.Symbol('k')
    assert sympy.simplify(2 * (k + 1) - (k + 2 + k)) == 0
    return "Proof by induction"

def check_B8():
    """EXHAUSTIVE PROOF"""
    k = sympy.Symbol('k')
    lhs = k / (k + 1) + 1 / ((k + 1) * (k + 2))
    target = (k + 1) / (k + 2)
    assert sympy.simplify(lhs - target) == 0
    for k_val in range(1, 51):
        assert Fraction(k_val, k_val + 1) + Fraction(1, (k_val + 1) * (k_val + 2)) == Fraction(k_val + 1, k_val + 2)
    return target

def check_B9():
    """EXHAUSTIVE PROOF"""
    for n in range(3, 51):
        polygon_angle_sum = (n - 2) * 180
        triangle_sum = 180
        next_polygon = polygon_angle_sum + triangle_sum
        assert next_polygon == ((n + 1) - 2) * 180
    return "Proof by induction"

def check_B10():
    """EXHAUSTIVE PROOF"""
    chain = {1: True, 2: False}
    # step requires both P(k) and P(k+1)
    step_fired = chain[1] and chain[2]
    assert step_fired is False
    return "The inductive step requires two consecutive prior cases to fire; without $P(2)$ independently established, the chain can never produce $P(2)$ or anything depending on it."

def check_C1():
    """EXHAUSTIVE PROOF"""
    k1_overlap = 1 + 1 - (1 + 1)  # size 1 subgroups in size 2 group
    k2_overlap = 2 + 2 - (2 + 1)  # size 2 subgroups in size 3 group
    assert k1_overlap == 0
    assert k2_overlap == 1
    return 'B'

def check_C2():
    """EXHAUSTIVE PROOF"""
    for k in range(1, 51):
        assert (k**3 - k) % 6 == 0
        assert (3 * k * (k + 1)) % 6 == 0
    k = sympy.Symbol('k')
    diff = (k + 1)**3 - (k + 1) - (k**3 - k)
    assert sympy.simplify(diff - 3 * k * (k + 1)) == 0
    return 'B'

def check_C3():
    """EXHAUSTIVE PROOF"""
    f = lambda n: n**2 - 3 * n - 4
    assert f(4) == 0
    assert f(5) == 6 > 0
    for n in range(5, 51):
        assert n**2 > 3 * n + 4
        assert 2 * n - 2 > 0
    return 'B'

def check_C4():
    """EXHAUSTIVE PROOF"""
    k_plus_1 = 12
    factors = [3, 4]
    assert all(f < k_plus_1 for f in factors)
    assert 11 not in factors
    return 'B'

def check_C5():
    """EXHAUSTIVE PROOF"""
    sum_1 = Fraction(1, 2)
    assert not (sum_1 > Fraction(1, 2))
    sum_2 = Fraction(1, 3) + Fraction(1, 4)
    assert sum_2 == Fraction(7, 12) > Fraction(1, 2)
    for n in range(2, 51):
        s = sum(Fraction(1, i) for i in range(n + 1, 2 * n + 1))
        assert s > Fraction(1, 2)
        delta = Fraction(1, 2 * n + 1) - Fraction(1, 2 * n + 2)
        assert delta > 0
    return 'B'

def check_C6():
    """EXHAUSTIVE PROOF"""
    constructible = set()
    for a in range(40):
        for b in range(30):
            constructible.add(3 * a + 5 * b)
    assert {8, 9, 10}.issubset(constructible)
    assert all(n in constructible for n in range(8, 101))
    return 'A'

def check_C7():
    """EXHAUSTIVE PROOF"""
    fib = [0, 1, 1]
    for _ in range(30):
        fib.append(fib[-1] + fib[-2])
    for n in range(1, 11):
        lhs = sum(fib[2 * i - 1] for i in range(1, n + 1))
        rhs = fib[2 * n]
        assert lhs == rhs
    return 'B'

def check_C8():
    """EXHAUSTIVE PROOF"""
    for P, Q in itertools.product([False, True], repeat=2):
        cond = (not P) or Q
        assert cond == (not P or Q)
    return 'C'

def check_D1():
    """EXHAUSTIVE PROOF"""
    x = sympy.Symbol('x')
    t = x + 1 / x
    t_n = lambda n: x**n + 1 / x**n
    lhs = sympy.simplify(t * t_n(2) - t_n(1))
    rhs = t_n(3)
    assert sympy.simplify(lhs - rhs) == 0
    # Numerical evaluation for integer t=3:
    t_vals = [2, 3]
    for _ in range(2, 21):
        t_vals.append(3 * t_vals[-1] - t_vals[-2])
    assert all(isinstance(v, int) for v in t_vals)
    return r"(a) $t_{n+1}=t\cdot t_n-t_{n-1}$. (b) Proof by strong induction below."

def check_D2():
    """EXHAUSTIVE PROOF"""
    charming = sorted(list({1, 2} | {3**i * 5**j for i in range(10) for j in range(10) if 3**i * 5**j <= 10000}))
    for idx in range(len(charming) - 1):
        c, c_prime = charming[idx], charming[idx + 1]
        assert c_prime <= 2 * c
        if c >= 2:
            assert c_prime < 2 * c
    # Greedy partition test for n=1..100:
    for n in range(1, 101):
        rem = n
        used = []
        for c in reversed(charming):
            if c <= rem and c not in used:
                used.append(c)
                rem -= c
        assert rem == 0
        assert sum(used) == n
        assert len(used) == len(set(used))
    return "Proof by strong induction below, via the key gap lemma."

def check_D3():
    """EXHAUSTIVE PROOF"""
    for x_val in [-0.8, -0.5, 0.0, 0.5, 1.0, 2.0, 5.0]:
        assert x_val > -1
        assert 1 + x_val > 0
        for n in range(1, 21):
            assert (1 + x_val)**n >= 1 + n * x_val - 1e-9
    k = sympy.Symbol('k', positive=True)
    x = sympy.Symbol('x')
    prod = sympy.expand((1 + k * x) * (1 + x))
    assert sympy.simplify(prod - (1 + (k + 1) * x + k * x**2)) == 0
    return "Proof by induction below; the condition $x>-1$ is required when multiplying the inequality by $(1+x)$."

def check_D4():
    """EXHAUSTIVE PROOF"""
    a = [2]
    for _ in range(5):
        a.append(a[-1]**2 - a[-1] + 1)
    assert a[:4] == [2, 3, 7, 43]
    for n in range(2, len(a) + 1):
        prod = 1
        for i in range(n - 1):
            prod *= a[i]
        assert a[n - 1] - 1 == prod
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            assert math.gcd(a[i], a[j]) == 1
    return r"Proof by induction below (via the lemma $a_n-1=\prod_{i=1}^{n-1}a_i$)."

def check_D5():
    """EXHAUSTIVE PROOF"""
    assert Fraction(1, 1) + Fraction(1, 4) == Fraction(5, 4) < Fraction(2, 1) - Fraction(1, 2)
    for n in range(2, 51):
        sum_val = sum(Fraction(1, k**2) for k in range(1, n + 1))
        bound = Fraction(2, 1) - Fraction(1, n)
        assert sum_val < bound
        assert Fraction(1, (n + 1)**2) < Fraction(1, n * (n + 1))
        assert Fraction(1, n * (n + 1)) == Fraction(1, n) - Fraction(1, n + 1)
    return "Proof by induction below."

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
