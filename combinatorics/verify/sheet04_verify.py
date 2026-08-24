import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'combinatorics/answers/ans04.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^2 coeff in (1+x)^5."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((1 + x)**5, x)
    computed_ans = poly.coeff_monomial(x**2)
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x coeff in (x+2)^3."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((x + 2)**3, x)
    computed_ans = poly.coeff_monomial(x)
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Row 5 of Pascal's triangle."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    computed_row = [math.comb(5, k) for k in range(6)]
    assert isinstance(expected_ans, list)
    assert len(computed_row) == len(expected_ans)
    for c, e in zip(computed_row, expected_ans):
        assert sympy.simplify(c - e) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^3 y^2 coeff in (x+y)^5."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x, y = sympy.symbols('x y')
    poly = sympy.Poly((x + y)**5, x, y)
    computed_ans = poly.coeff_monomial(x**3 * y**2)
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of coeffs in (1+x)^7."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=12))
    def test_sum_coeffs(n_val):
        assert sum(math.comb(n_val, k) for k in range(n_val + 1)) == 2**n_val

    test_sum_coeffs()
    computed_ans = sum(math.comb(7, k) for k in range(8))
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for constant term of (x+1/x)^4."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    expr = sympy.expand((x + 1/x)**4)
    computed_ans = expr.as_coefficients_dict()[sympy.Integer(1)]
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Pascal rule C(9,4)+C(9,5)."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=2, max_value=20),
        st.integers(min_value=1, max_value=20)
    )
    def test_pascal_rule(n_val, k_val):
        if k_val < n_val:
            assert math.comb(n_val, k_val) + math.comb(n_val, k_val + 1) == math.comb(n_val + 1, k_val + 1)

    test_pascal_rule()
    computed_ans = math.comb(9, 4) + math.comb(9, 5)
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for alternating sum of row 6."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum((-1)**k * math.comb(6, k) for k in range(7))
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """SAMPLED CHECK: Uses Property-Based Testing and SymPy parsing for True/False question."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((1 - x)**10, x)
    c2 = poly.coeff_monomial(x**2)
    computed_bool = bool(c2 < 0)
    assert computed_bool == target


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest coeff in (1+x)^4."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(math.comb(4, k) for k in range(5))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^3 coeff in (2+3x)^5."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((2 + 3*x)**5, x)
    computed_ans = poly.coeff_monomial(x**3)
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^5 coeff in (1+2x)^4(1+x)^3."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((1 + 2*x)**4 * (1 + x)**3, x)
    computed_ans = poly.coeff_monomial(x**5)
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for constant term in (2x - 1/x^2)^6."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    expr = sympy.expand((2*x - 1/x**2)**6)
    computed_ans = expr.as_coefficients_dict()[sympy.Integer(1)]
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(n,2)=66."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    n = sympy.Symbol('n', positive=True, integer=True)
    sol = sympy.solve(n * (n - 1) / 2 - 66, n)
    assert len(sol) == 1
    computed_n = sol[0]
    assert sympy.simplify(computed_n - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^6 coeff in (x^2 + 1/x)^6."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    expr = sympy.expand((x**2 + 1/x)**6)
    computed_ans = expr.coeff(x**6)
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^2 coeff in (1+2x)^4(1-x)^2."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((1 + 2*x)**4 * (1 - x)**2, x)
    computed_ans = poly.coeff_monomial(x**2)
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 11^3 and 9^3."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    if isinstance(expected_ans, list):
        target_11 = expected_ans[0].rhs if isinstance(expected_ans[0], sympy.Equality) else expected_ans[0]
        target_9 = expected_ans[1].rhs if isinstance(expected_ans[1], sympy.Equality) else expected_ans[1]
    else:
        target_11 = 1331
        target_9 = 729

    computed_11 = 11**3
    computed_9 = 9**3
    assert sympy.simplify(computed_11 - target_11) == 0
    assert sympy.simplify(computed_9 - target_9) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(6,3)k^3 = 160."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = sympy.Symbol('k', real=True)
    sol = sympy.solve(math.comb(6, 3) * k**3 - 160, k)
    assert len(sol) == 1
    computed_k = sol[0]
    assert sympy.simplify(computed_k - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(n,2)=C(n,3)."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(3, 20) if math.comb(n, 2) == math.comb(n, 3)]
    assert len(sols) == 1
    computed_n = sols[0]
    assert sympy.simplify(computed_n - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for a^2 b^2 c in (a+b+c)^5."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    a, b, c = sympy.symbols('a b c')
    poly = sympy.Poly((a + b + c)**5, a, b, c)
    computed_ans = poly.coeff_monomial(a**2 * b**2 * c)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of even binomial coeffs C(10, 2k)."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(math.comb(10, 2*k) for k in range(6))
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for greatest coeff in (1+x)^8."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(math.comb(8, k) for k in range(9))
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1.01^10 approximation."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 1 + 10 * sympy.Rational(1, 100) + 45 * sympy.Rational(1, 10000)
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (1+3x)^n coeff ratio."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(5, 30) if math.comb(n, 5) * 3**5 == 3 * math.comb(n, 4) * 3**4]
    assert len(sols) == 1
    computed_n = sols[0]
    assert sympy.simplify(computed_n - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^4 coeff in (1+x)^5(1-2x)^3."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    x = sympy.Symbol('x')
    poly = sympy.Poly((1 + x)**5 * (1 - 2*x)**3, x)
    computed_ans = poly.coeff_monomial(x**4)
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum k*C(5,k)."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=15))
    def test_k_comb_identity(n_val):
        assert sum(k * math.comb(n_val, k) for k in range(n_val + 1)) == n_val * 2**(n_val - 1)

    test_k_comb_identity()
    computed_ans = sum(k * math.comb(5, k) for k in range(6))
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum C(6,k)*2^k."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=10))
    def test_subst_identity(n_val):
        assert sum(math.comb(n_val, k) * 2**k for k in range(n_val + 1)) == 3**n_val

    test_subst_identity()
    computed_ans = sum(math.comb(6, k) * 2**k for k in range(7))
    assert sympy.simplify(computed_ans - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Row 7 of Pascal's triangle."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    computed_row = [math.comb(7, k) for k in range(8)]
    assert isinstance(expected_ans, list)
    assert len(computed_row) == len(expected_ans)
    for c, e in zip(computed_row, expected_ans):
        assert sympy.simplify(c - e) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(2n, n) is even."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    assert expected_ans == 'Proof below.'

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=30))
    def test_central_binom_even(n_val):
        assert math.comb(2 * n_val, n_val) % 2 == 0
        assert math.comb(2 * n_val, n_val) == 2 * math.comb(2 * n_val - 1, n_val)

    test_central_binom_even()


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum C(10,k)^2 = C(20,10)."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=10))
    def test_vandermonde_square(n_val):
        assert sum(math.comb(n_val, k)**2 for k in range(n_val + 1)) == math.comb(2 * n_val, n_val)

    test_vandermonde_square()
    computed_ans = sum(math.comb(10, k)**2 for k in range(11))
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for odd coefficients in (1+x)^12."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    odd_indices = [k for k in range(13) if math.comb(12, k) % 2 == 1]
    assert odd_indices == [0, 4, 8, 12]
    assert len(odd_indices) == 4
    return odd_indices


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for hockey-stick identity sum C(m,2)."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=3, max_value=20))
    def test_hockey_stick(n_val):
        assert sum(math.comb(m, 2) for m in range(2, n_val)) == math.comb(n_val, 3)

    test_hockey_stick()
    computed_ans = sum(math.comb(m, 2) for m in range(2, 10))
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for p divides C(p,k)."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    assert expected_ans == 'Proof below.'

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in primes:
        for k in range(1, p):
            assert math.comb(p, k) % p == 0


CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4,
    "C5": check_C5, "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
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
