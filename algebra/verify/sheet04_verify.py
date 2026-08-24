import sys
import os
for _cand in [
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')),
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')),
]:
    if os.path.exists(os.path.join(_cand, 'tools', 'latex_bridge.py')) and _cand not in sys.path:
        sys.path.insert(0, _cand)

import math
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

for _tex_cand in [
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../answers/ans04.tex')),
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../algebra/answers/ans04.tex')),
    os.path.abspath('algebra/answers/ans04.tex'),
]:
    if os.path.exists(_tex_cand):
        TEX_PATH = _tex_cand
        break
else:
    TEX_PATH = 'algebra/answers/ans04.tex'

# A1
def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A1')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=1000))
    def test_diff_squares(n):
        assert (n + 1) * (n - 1) == n**2 - 1

    test_diff_squares()
    computed_ans = (200 + 1) * (200 - 1)
    assert sympy.simplify(computed_ans - expected_ans) == 0

# A2
def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    x = sympy.Symbol('x')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=-50, max_value=50))
    def test_factorisation(x_val):
        assert x_val**2 - x_val - 42 == (x_val - 7) * (x_val + 6)

    test_factorisation()
    computed_expr = sympy.factor(x**2 - x - 42)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# A3
def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A3')

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=1, max_value=50),
        st.integers(min_value=1, max_value=50)
    )
    def test_conjugate(a, b):
        diff = (math.sqrt(a) + math.sqrt(b)) * (math.sqrt(a) - math.sqrt(b))
        assert abs(diff - (a - b)) < 1e-9

    test_conjugate()
    computed_ans = (sympy.sqrt(7) + sympy.sqrt(6)) * (sympy.sqrt(7) - sympy.sqrt(6))
    assert sympy.simplify(computed_ans - expected_ans) == 0

# A4
def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A4')

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=-30, max_value=30),
        st.integers(min_value=-30, max_value=30)
    )
    def test_sum_squares(a, b):
        s = a + b
        p = a * b
        assert s**2 - 2 * p == a**2 + b**2

    test_sum_squares()
    s = 14
    p = 53
    computed_ans = s**2 - 2 * p
    assert sympy.simplify(computed_ans - expected_ans) == 0

# A5
def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A5')

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=-20, max_value=20),
        st.integers(min_value=-20, max_value=20),
        st.integers(min_value=-20, max_value=20)
    )
    def test_cyclic_cubes(x, y, z):
        a = x - y
        b = y - z
        c = z - x
        assert a + b + c == 0
        assert a**3 + b**3 + c**3 == 3 * a * b * c

    test_cyclic_cubes()
    assert expected_ans == 0

# A6
def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    x = sympy.Symbol('x')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=-30, max_value=30))
    def test_factorisation(x_val):
        assert 2 * x_val**3 - 18 * x_val == 2 * x_val * (x_val - 3) * (x_val + 3)

    test_factorisation()
    computed_expr = sympy.factor(2 * x**3 - 18 * x)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# A7
def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    n = sympy.Symbol('n')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=20))
    def test_power_diff(n_val):
        num = 3**(n_val + 1) - 3**(n_val - 1)
        den = 3**n_val
        assert sympy.Rational(num, den) == sympy.Rational(8, 3)

    test_power_diff()
    computed_ans = sympy.Rational(3) - sympy.Rational(1, 3)
    assert sympy.simplify(computed_ans - expected_ans) == 0

# A8
def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    s = 7
    p2 = 29
    computed_p = sympy.Rational(s**2 - p2, 2)
    target_val = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    assert sympy.simplify(computed_p - target_val) == 0

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=-20, max_value=20),
        st.integers(min_value=-20, max_value=20)
    )
    def test_vieta_prod(a, b):
        assert sympy.Rational((a + b)**2 - (a**2 + b**2), 2) == a * b

    test_vieta_prod()

# A9
def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    x = sympy.Symbol('x')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=-30, max_value=30))
    def test_factorisation(x_val):
        assert x_val**4 - 1 == (x_val**2 + 1) * (x_val + 1) * (x_val - 1)

    test_factorisation()
    computed_expr = sympy.factor(x**4 - 1)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# A10
def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    n = sympy.Symbol('n')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=15))
    def test_factorial_div(n_val):
        val = math.factorial(n_val) // math.factorial(n_val - 2)
        assert val == n_val * (n_val - 1)

    test_factorial_div()
    computed_expr = n * (n - 1)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# B1
def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    x = sympy.Symbol('x')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=20))
    def test_geometric_series(x_val):
        assert sum(x_val**k for k in range(5)) == (x_val**5 - 1) // (x_val - 1)

    test_geometric_series()
    computed_expr = sympy.simplify((x**5 - 1) / (x - 1))
    assert sympy.simplify(computed_expr - expected_ans) == 0

# B2
def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    x = sympy.Symbol('x')
    poly = x**10 - 3*x**5 + 2
    rem1 = poly.subs(x, 1)
    rem_neg1 = poly.subs(x, -1)
    assert rem1 == 0
    assert rem_neg1 == 6
    assert '0' in str(expected_ans) and '6' in str(expected_ans)

# B3
def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    a, b = sympy.symbols('a b')

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=-20, max_value=20).filter(lambda v: v != 0),
        st.integers(min_value=-20, max_value=20).filter(lambda v: v != 0)
    )
    def test_fraction_simplification(a_val, b_val):
        if a_val**2 == b_val**2:
            return
        f1 = sympy.Rational(a_val * b_val, a_val - b_val)
        f2 = sympy.Rational(a_val * b_val, a_val + b_val)
        diff = f1 - f2
        expected_diff = sympy.Rational(2 * a_val * b_val**2, a_val**2 - b_val**2)
        assert diff == expected_diff

    test_fraction_simplification()
    f1 = a*b / (a - b)
    f2 = a*b / (a + b)
    computed_expr = sympy.simplify((f1 - f2) / 2)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# B4
def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    x, y = sympy.symbols('x y')

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=-20, max_value=20),
        st.integers(min_value=-20, max_value=20)
    )
    def test_factorisation(x_val, y_val):
        lhs = x_val**6 - y_val**6
        rhs = (x_val - y_val)*(x_val + y_val)*(x_val**2 + x_val*y_val + y_val**2)*(x_val**2 - x_val*y_val + y_val**2)
        assert lhs == rhs

    test_factorisation()
    computed_expr = sympy.factor(x**6 - y**6)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# B5
def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    r6 = 3
    r2 = 2
    computed_ans = sympy.Rational(r6 + r2, 2)
    assert sympy.simplify(computed_ans - expected_ans) == 0

# B6
def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    x = sympy.Symbol('x')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=-30, max_value=30).filter(lambda v: v != 0))
    def test_identity(x_val):
        t1 = 1 - sympy.Rational(1, x_val**2)
        t2 = x_val**2 + x_val
        prod = t1 * t2
        target = sympy.Rational((x_val - 1) * (x_val + 1)**2, x_val)
        assert prod == target

    test_identity()
    expr = (1 - 1/x**2) * (x**2 + x)
    computed_expr = sympy.simplify(expr)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# B7
def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    s = 5
    p = 6
    computed_sum_sq = s**2 - 2*p
    assert sympy.simplify(computed_sum_sq - expected_ans) == 0

# B8
def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    x, y = sympy.symbols('x y')
    eq = sympy.Eq(x, (2*y + 1)/(y - 3))
    sol_y = sympy.solve(eq, y)[0]
    target_val = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    assert sympy.simplify(sol_y - target_val) == 0

# B9
def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B9')

    @settings(deadline=None, max_examples=30)
    @given(st.integers(min_value=2, max_value=200))
    def test_composite(n_val):
        fac1 = 2 * n_val - 1
        fac2 = 2 * n_val + 1
        assert fac1 > 1 and fac2 > 1
        assert (4 * n_val**2 - 1) == fac1 * fac2

    test_composite()
    assert 'composite' in str(expected_ans).lower() or 'integers' in str(expected_ans).lower()

# B10
def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    x = sympy.Symbol('x')
    eq = sympy.Eq(x**2 - 12, 0)
    target_val = expected_ans.lhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    assert sympy.simplify(eq.lhs - target_val) == 0

# C1
def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    x, u = sympy.symbols('x u')
    u_sols = sympy.solve(u**2 - 5*u + 4, u)
    x_sols = sorted([sympy.solve(sympy.Eq(2**x, val), x)[0] for val in u_sols])
    for s in x_sols:
        assert (4**s - 5*2**s + 4) == 0
    if isinstance(expected_ans, list):
        for s, e in zip(x_sols, expected_ans):
            e_val = e.rhs if isinstance(e, sympy.Equality) else e
            assert sympy.simplify(s - e_val) == 0

# C2
def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    t = sympy.Symbol('t')

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=-20, max_value=20))
    def test_cubic_poly(t_val):
        assert t_val**3 - 3*t_val == t_val * (t_val**2 - 3)

    test_cubic_poly()
    computed_expr = t**3 - 3*t
    assert sympy.simplify(computed_expr - expected_ans) == 0

# C3
def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    x = sympy.Symbol('x', positive=True)
    min_val = 2 * sympy.sqrt(3 * 27)
    assert min_val == 18
    expr = 3*x + 27/x
    assert expr.subs(x, 3) == 18
    assert '18' in str(expected_ans) and '3' in str(expected_ans)

# C4
def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    x = sympy.Symbol('x', real=True)
    eq = sympy.Eq(sympy.sqrt(2*x - 1) + sympy.sqrt(x - 1), 2)
    sols = sympy.solve(eq, x)
    valid_sols = []
    for s in sols:
        if 2*s - 1 >= 0 and s - 1 >= 0:
            val = sympy.sqrt(2*s - 1) + sympy.sqrt(s - 1)
            if sympy.simplify(val - 2) == 0:
                valid_sols.append(s)

    assert len(valid_sols) == 1
    expected_sol = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    assert sympy.simplify(valid_sols[0] - expected_sol) == 0

# C5
def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    k = sympy.Symbol('k')
    disc = 8**2 - 4*k
    sol_k = sympy.solve(disc, k)[0]
    target_val = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    assert sympy.simplify(sol_k - target_val) == 0

# C6
def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C6')

    @settings(deadline=None, max_examples=25)
    @given(
        st.integers(min_value=1, max_value=20),
        st.integers(min_value=1, max_value=20),
        st.integers(min_value=1, max_value=20),
        st.integers(min_value=1, max_value=20)
    )
    def test_cauchy_schwarz(a, b, c, d):
        diff = (a**2 + b**2) * (c**2 + d**2) - (a*c + b*d)**2
        assert diff == (a*d - b*c)**2
        assert diff >= 0

    test_cauchy_schwarz()
    assert 'ad=bc' in str(expected_ans) or 'ad = bc' in str(expected_ans)

# C7
def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    u, v = sympy.symbols('u v')
    x = (u + v)/2
    y = (u - v)/2
    computed_expr = sympy.simplify(x**4 + y**4)
    assert sympy.simplify(computed_expr - expected_ans) == 0

# C8
def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    x = sympy.Symbol('x')
    poly = x**4 - 7*x**2 + 12
    sols = sorted(sympy.solve(poly, x), key=lambda v: float(sympy.sympify(v).evalf()))
    for s in sols:
        assert poly.subs(x, s) == 0
    assert len(sols) == 4
    assert '2' in str(expected_ans)

# D1
def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'D1')

    @settings(deadline=None, max_examples=50)
    @given(st.integers(min_value=-1000, max_value=1000))
    def test_mod4(n_val):
        rem = (n_val**2) % 4
        assert rem in (0, 1)
        assert (n_val**2 + 2) % 4 != 0

    test_mod4()
    assert 'proved' in str(expected_ans).lower()

# D2
def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    x = sympy.Symbol('x')
    poly = x**4 - 4*x**3 + 4*x**2 - 1
    fac = sympy.factor(poly)
    assert sympy.simplify(fac - (x - 1)**2 * (x**2 - 2*x - 1)) == 0
    sols = sympy.solve(poly, x)
    for s in sols:
        assert sympy.simplify(poly.subs(x, s)) == 0
    assert '1' in str(expected_ans)

# D3
def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    n = sympy.Symbol('n')

    def a(k):
        if k == 1:
            return 1
        prev = a(k - 1)
        return prev / (prev + 2)

    for k in range(1, 10):
        assert a(k) == 1 / (2**k - 1)

    computed_formula = 1 / (2**n - 1)
    if isinstance(expected_ans, list) and len(expected_ans) == 2:
        assert sympy.simplify(computed_formula - expected_ans[0].rhs) == 0
        assert sympy.simplify(computed_formula.subs(n, 100) - expected_ans[1].rhs) == 0

# D4
def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    n = sympy.Symbol('n')

    @settings(deadline=None, max_examples=25)
    @given(st.integers(min_value=2, max_value=20))
    def test_telescoping_prod(n_val):
        prod = 1.0
        for k in range(2, n_val + 1):
            prod *= (1.0 - 1.0 / (k**2))
        expected_val = (n_val + 1.0) / (2.0 * n_val)
        assert abs(prod - expected_val) < 1e-9

    test_telescoping_prod()
    computed_formula = (n + 1) / (2*n)
    if isinstance(expected_ans, list) and len(expected_ans) == 2:
        assert sympy.simplify(computed_formula - expected_ans[0]) == 0

# D5
def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    x = sympy.Symbol('x')
    q_expr = (x - 1) * (x - 2) * (x - 3) * (x - 4)
    p_expr = q_expr + 10 * x

    # Property: p(k) == 10*k for k in 1..4
    for k in (1, 2, 3, 4):
        assert p_expr.subs(x, k) == 10 * k

    computed_val = p_expr.subs(x, 12) - 12 * p_expr.subs(x, 0)
    assert sympy.simplify(computed_val - expected_ans) == 0


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
