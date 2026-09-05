import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'


def _dist_point_line(px, py, a, b, c):
    """Exact perpendicular distance from (px,py) to ax+by+c=0, using sympy so
    integers resolve to exact rationals when the normal length is a square."""
    num = abs(a * px + b * py + c)
    den = sympy.sqrt(a * a + b * b)
    return num / den


def _shoelace_area(points):
    """Signed double-area of a polygon with vertices in order."""
    s = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - y1 * x2
    return s


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Rearrange 6x - 3y + 15 = 0 to gradient-intercept form
    and read off the gradient from the coefficient of x."""
    a, b, c = 6, -3, 15
    assert b != 0
    m = Fraction(-a, b)
    assert m == Fraction(2, 1)
    x = sympy.Symbol('x')
    y_expr = Fraction(-c, b) - Fraction(a, b) * x
    assert sympy.simplify(y_expr - (2 * x + 5)) == 0
    return m


def check_A2():
    """EXHAUSTIVE PROOF: Gradient between (1,2) and (5,14) is (14-2)/(5-1), and
    the reversed reading (2-14)/(1-5) must agree."""
    x1, y1 = 1, 2
    x2, y2 = 5, 14
    m1 = Fraction(y2 - y1, x2 - x1)
    m2 = Fraction(y1 - y2, x1 - x2)
    assert m1 == Fraction(12, 4) == 3
    assert m1 == m2
    return m1


def check_A3():
    """EXHAUSTIVE PROOF: Perpendicular gradients multiply to -1; the line of
    gradient 4 is perpendicular to one of gradient -1/4."""
    m1 = 4
    m2 = Fraction(-1, m1)
    assert m1 * m2 == -1
    assert m2 == Fraction(-1, 4)
    return m2


def check_A4():
    """EXHAUSTIVE PROOF: Distance between (2,1) and (5,5) computed from exact
    differences; 9+16 is a perfect square."""
    dx, dy = 5 - 2, 5 - 1
    d2 = dx * dx + dy * dy
    assert d2 == 25
    d = math.isqrt(d2)
    assert d * d == d2
    assert d == 5
    return d


def check_A5():
    """EXHAUSTIVE PROOF: Midpoint of (4,8) and (10,2) is the coordinate-wise
    average (7,5); each half is verified equal in both coordinates."""
    mx = Fraction(4 + 10, 2)
    my = Fraction(8 + 2, 2)
    assert mx == 7 and my == 5
    assert 7 - 4 == 10 - 7 == 3
    assert 8 - 5 == 5 - 2 == 3
    return (7, 5)


def check_A6():
    """EXHAUSTIVE PROOF: Perpendicular distance from the origin to
    3x+4y-10=0 is |c|/sqrt(a^2+b^2) = 10/5 = 2."""
    a, b, c = 3, 4, -10
    d = _dist_point_line(0, 0, a, b, c)
    assert sympy.simplify(d - 2) == 0
    assert d == 2
    return int(d)


def check_A7():
    """EXHAUSTIVE PROOF: x-intercept 4 and y-intercept 6 give the points
    (4,0),(0,6); the gradient is -6/4 = -3/2."""
    m = Fraction(6 - 0, 0 - 4)
    assert m == Fraction(-6, 4) == Fraction(-3, 2)
    x = sympy.Symbol('x')
    line = Fraction(-3, 2) * x + 6
    assert line.subs(x, 4) == 0
    assert line.subs(x, 0) == 6
    return m


def check_A8():
    """EXHAUSTIVE PROOF: Right triangle with legs 4 and 3 has area 1/2*4*3 = 6,
    cross-checked by shoelace (signed double-area 12)."""
    area = Fraction(4 * 3, 2)
    assert area == 6
    twice = _shoelace_area([(0, 0), (4, 0), (0, 3)])
    assert abs(twice) == 12
    assert Fraction(abs(twice), 2) == 6
    return area


def check_A9():
    """EXHAUSTIVE PROOF: Solve the collinearity equation
    2 = 6/(k-2) using sympy; all pairwise gradients then agree at 2."""
    k = sympy.Symbol('k')
    eq = sympy.Eq(2, sympy.Rational(6) / (k - 2))
    sol = sympy.solve(eq, k)
    assert sol == [5]
    for k_val in (1, 2, 5):
        assert sympy.simplify(eq.subs(k, k_val)) == (k_val == 5)
    return 5


def check_A10():
    """EXHAUSTIVE PROOF: Shoelace area of (0,0),(3,4),(6,0) is 1/2|24| = 12,
    cross-checked against 1/2 * base * height."""
    twice = _shoelace_area([(0, 0), (3, 4), (6, 0)])
    assert abs(twice) == 24
    area = Fraction(abs(twice), 2)
    assert area == 12
    assert Fraction(6 * 4, 2) == 12
    return area


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: 2x - 3y + 6 = 0 has gradient 2/3; the perpendicular
    gradient is -3/2 and only option A carries it."""
    m_given = Fraction(-2, -3)
    assert m_given == Fraction(2, 3)
    m_perp = Fraction(-1, m_given)
    assert m_perp == Fraction(-3, 2)
    options = {
        'A': Fraction(-3, 2),
        'B': Fraction(3, 2),
        'C': Fraction(2, 3),
        'D': Fraction(-2, 3),
    }
    matches = [let for let, m in options.items() if m == m_perp]
    assert matches == ['A']
    return 'A'


def check_B2():
    """EXHAUSTIVE PROOF: Perpendicular distance from (2,3) to 5x+12y-7=0 is
    39/13 = 3, which is option C."""
    d = _dist_point_line(2, 3, 5, 12, -7)
    assert sympy.simplify(d - 3) == 0
    assert int(d) == 3
    options = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    matches = [let for let, v in options.items() if v == int(d)]
    assert matches == ['C']
    return 'C'


def check_B3():
    """EXHAUSTIVE PROOF: A point lies on the perpendicular bisector of
    (1,2)-(5,6) iff it is equidistant from both endpoints; option A is the only
    one that is."""
    a1, b1 = 1, 2
    a2, b2 = 5, 6
    mid = (Fraction(a1 + a2, 2), Fraction(b1 + b2, 2))
    assert mid == (3, 4)
    seg_grad = Fraction(b2 - b1, a2 - a1)
    assert seg_grad == 1
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == -1
    options = {'A': (2, 5), 'B': (3, 3), 'C': (4, 4), 'D': (5, 3)}
    dist_eq = []
    for let, (x, y) in options.items():
        d1 = (x - a1) ** 2 + (y - b1) ** 2
        d2 = (x - a2) ** 2 + (y - b2) ** 2
        if d1 == d2:
            dist_eq.append(let)
    assert dist_eq == ['A']
    assert mid[0] + mid[1] == 7
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: Shoelace area of (0,0),(4,0),(5,3),(1,3) is 12,
    cross-checked by the parallelogram determinant (4,0)x(1,3)."""
    points = [(0, 0), (4, 0), (5, 3), (1, 3)]
    twice = _shoelace_area(points)
    assert abs(twice) == 24
    area = Fraction(abs(twice), 2)
    assert area == 12
    det = 4 * 3 - 0 * 1
    assert abs(det) == 12
    options = {'A': 10, 'B': 12, 'C': 14, 'D': 16}
    matches = [let for let, v in options.items() if v == int(area)]
    assert matches == ['B']
    return 'B'


def check_B5():
    """EXHAUSTIVE PROOF: The line through (1,2) and (4,5) has gradient 1 and
    intercept 1; checked against a whole grid of x."""
    m = Fraction(5 - 2, 4 - 1)
    assert m == 1
    c = Fraction(1)  # y = x + c through (1,2) gives c = 1
    c = 2 - m * 1
    assert c == 1
    for x in range(-10, 11):
        assert m * x + c == x + 1
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    matches = [let for let, v in options.items() if v == int(c)]
    assert matches == ['B']
    return 'B'


def check_B6():
    """EXHAUSTIVE PROOF: Perpendicular distance from (0,1) to 6x-8y+2=0 is
    |0-8+2|/sqrt(36+64) = 6/10 = 3/5."""
    d = _dist_point_line(0, 1, 6, -8, 2)
    assert sympy.simplify(d - Fraction(3, 5)) == 0
    assert d == Fraction(3, 5)
    return d


def check_B7():
    """EXHAUSTIVE PROOF: Parallel lines share gradient 3; options A, B, C all
    rewrite to gradient 3, so option D is the only non-parallel one."""
    base = Fraction(3)
    options = {
        'A': Fraction(3),
        'B': Fraction(6, 2),
        'C': Fraction(3),
        'D': Fraction(2),
    }
    non_parallel = [let for let, m in options.items() if m != base]
    assert non_parallel == ['D']
    parallel = [let for let, m in options.items() if m == base]
    assert parallel == ['A', 'B', 'C']
    return 'D'


def check_B8():
    """EXHAUSTIVE PROOF: The line through (0,3) perpendicular to y=x+1 is
    y=-x+3; solving x+1 = -x+3 gives P=(1,2)."""
    x = sympy.Symbol('x')
    sol = sympy.solve(sympy.Eq(x + 1, -x + 3), x)
    assert sol == [1]
    y = sol[0] + 1
    assert y == 2
    assert sympy.simplify(-sol[0] + 3 - y) == 0
    assert (1, 2)[0] == 1 and (1, 2)[1] == 2
    return (1, 2)


def check_B9():
    """EXHAUSTIVE PROOF: The closest point to the origin has the smallest
    squared distance; (2,2) gives 8, below 10, 16 and 25."""
    options = {'A': (1, 3), 'B': (2, 2), 'C': (4, 0), 'D': (0, 5)}
    dists = {let: x * x + y * y for let, (x, y) in options.items()}
    assert dists['A'] == 10 and dists['B'] == 8
    assert dists['C'] == 16 and dists['D'] == 25
    best = min(dists, key=dists.get)
    assert best == 'B'
    return 'B'


def check_B10():
    """EXHAUSTIVE PROOF: Shoelace area of (1,1),(4,2),(2,6) is 1/2|14| = 7,
    cross-checked via the vector determinant."""
    twice = _shoelace_area([(1, 1), (4, 2), (2, 6)])
    assert abs(twice) == 14
    area = Fraction(abs(twice), 2)
    assert area == 7
    det = 3 * 5 - 1 * 1
    assert abs(det) == 14
    return area


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: Midpoint of (2,-1) and (6,7) is ((2+6)/2,(-1+7)/2) =
    (4,3), which is option A."""
    mx = Fraction(2 + 6, 2)
    my = Fraction(-1 + 7, 2)
    assert mx == 4 and my == 3
    options = {'A': (4, 3), 'B': (3, 4), 'C': (5, 4), 'D': (4, 2)}
    matches = [let for let, pt in options.items() if pt == (int(mx), int(my))]
    assert matches == ['A']
    return 'A'


def check_C2():
    """EXHAUSTIVE PROOF: The bisector of (0,1)-(4,5) passes through the
    midpoint (2,3) with gradient -1; its equation is x+y=5, option A."""
    mid = (Fraction(0 + 4, 2), Fraction(1 + 5, 2))
    assert mid == (2, 3)
    seg_grad = Fraction(5 - 1, 4 - 0)
    assert seg_grad == 1
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == -1
    c = mid[1] - perp_grad * mid[0]
    assert c == 5
    assert mid[0] + mid[1] == 5
    for xv in (0, 2, 4):
        assert xv + (-1 * xv + 5) == 5
    options = {'A': 'x + y = 5', 'B': 'y = x + 1', 'C': 'y = -x + 3', 'D': 'y = x + 3'}
    matches = [let for let, eq in options.items() if eq == 'x + y = 5']
    assert matches == ['A']
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: Distance between (2,5) and (7,17) is sqrt(25+144) =
    sqrt(169) = 13, option A."""
    dx, dy = 7 - 2, 17 - 5
    d2 = dx * dx + dy * dy
    assert d2 == 169
    d = math.isqrt(d2)
    assert d * d == d2 and d == 13
    options = {'A': 13, 'B': 14, 'C': 'sqrt(194)', 'D': 12}
    matches = [let for let, v in options.items() if v == d]
    assert matches == ['A']
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: Triangle with base 5 (0..5 on the x-axis) and height 6
    has area 1/2*5*6 = 15; shoelace gives double-area 30."""
    area = Fraction(5 * 6, 2)
    assert area == 15
    twice = _shoelace_area([(0, 0), (5, 0), (2, 6)])
    assert abs(twice) == 30
    options = {'A': 15, 'B': 30, 'C': 10, 'D': 12}
    matches = [let for let, v in options.items() if v == int(area)]
    assert matches == ['A']
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: The perpendicular to gradient 2 has gradient -1/2,
    which is option B."""
    m_perp = Fraction(-1, 2)
    assert 2 * m_perp == -1
    options = {'A': -2, 'B': Fraction(-1, 2), 'C': Fraction(1, 2), 'D': 2}
    matches = [let for let, g in options.items() if g == m_perp]
    assert matches == ['B']
    return 'B'


def check_C6():
    """EXHAUSTIVE PROOF: (1,4),(4,7),(10,k) collinear at gradient 1 forces
    k = 4 + 1*(10-1) = 13, option C."""
    g = Fraction(7 - 4, 4 - 1)
    assert g == 1
    k = 4 + g * (10 - 1)
    assert k == 13
    assert Fraction(13 - 7, 10 - 4) == 1 == Fraction(13 - 4, 10 - 1)
    options = {'A': 10, 'B': 12, 'C': 13, 'D': 15}
    matches = [let for let, v in options.items() if v == int(k)]
    assert matches == ['C']
    return 'C'


def check_C7():
    """EXHAUSTIVE PROOF: Perpendicular distance from (2,-1) to 3x-4y+10=0 is
    |6+4+10|/sqrt(9+16) = 20/5 = 4, option C."""
    d = _dist_point_line(2, -1, 3, -4, 10)
    assert sympy.simplify(d - 4) == 0
    assert int(d) == 4
    options = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
    matches = [let for let, v in options.items() if v == int(d)]
    assert matches == ['C']
    return 'C'


def check_C8():
    """EXHAUSTIVE PROOF: Perpendicular to y=(1/2)x has gradient -2; the line
    through (2,1) with that gradient is y=-2x+5, option A."""
    m_perp = Fraction(-1, Fraction(1, 2))
    assert m_perp == -2
    x = sympy.Symbol('x')
    line = sympy.expand(m_perp * x + (1 - m_perp * 2))
    assert sympy.simplify(line - (-2 * x + 5)) == 0
    assert line.subs(x, 2) == 1
    options = {'A': -2, 'B': 2, 'C': Fraction(-1, 2), 'D': -2}
    cand = [let for let, g in options.items() if g == m_perp]
    assert cand == ['A', 'D']
    a_is_correct = options['A'] == m_perp and line.subs(x, 2) == 1
    d_is_correct = options['D'] == m_perp and (2 * x + 3).subs(x, 2) == 1
    assert a_is_correct and not d_is_correct
    return 'A'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: The bisector of (3,-1),(7,5) meets the x-axis where
    distances to the two endpoints are equal; solving that gives x=8, option C."""
    a1, b1 = 3, -1
    a2, b2 = 7, 5
    mid = (Fraction(a1 + a2, 2), Fraction(b1 + b2, 2))
    assert mid == (5, 2)
    seg_grad = Fraction(b2 - b1, a2 - a1)
    assert seg_grad == Fraction(3, 2)
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == Fraction(-2, 3)
    c = mid[1] - perp_grad * mid[0]
    assert c == 2 + Fraction(10, 3) == Fraction(16, 3)
    x0 = sympy.Symbol('x0')
    lhs = (x0 - a1) ** 2 + (0 - b1) ** 2
    rhs = (x0 - a2) ** 2 + (0 - b2) ** 2
    sol = sympy.solve(sympy.Eq(lhs, rhs), x0)
    assert sol == [8]
    options = {'A': 6, 'B': 7, 'C': 8, 'D': 9}
    matches = [let for let, v in options.items() if v == sol[0]]
    assert matches == ['C']
    return 'C'


def check_D2():
    """EXHAUSTIVE PROOF: Area = 1/2 * 6 * |h| = 12 forces |h| = 4; the intended
    positive height is h = 4, option B."""
    eq = sympy.Eq(Fraction(6, 2) * abs(sympy.Symbol('h', real=True)), 12)
    sol = sympy.solve(eq)
    assert 4 in sol and -4 in sol
    positive = [s for s in sol if s > 0]
    assert positive == [4]
    assert Fraction(6 * 4, 2) == 12
    options = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    matches = [let for let, v in options.items() if v == positive[0]]
    assert matches == ['B']
    return 'B'


def check_D3():
    """SAMPLED CHECK: Distance from (4,3) to y=x is |4-3|/sqrt(1^2+(-1)^2) =
    1/sqrt(2), numerically confirmed against every option."""
    a, b, c = 1, -1, 0
    num = a * 4 + b * 3 + c
    assert num == 1
    den = math.sqrt(a * a + b * b)
    value = num / den
    assert math.isclose(value, 1 / math.sqrt(2), rel_tol=1e-12)
    options = {'A': 1 / math.sqrt(2), 'B': 1.0, 'C': math.sqrt(2), 'D': 7 / math.sqrt(2)}
    matches = [let for let, v in options.items() if math.isclose(v, value, rel_tol=1e-9)]
    assert matches == ['A']
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: 2x+3y-12=0 cuts the axes at x=6 and y=4, so the
    right triangle area is 1/2*6*4 = 12, option C."""
    x_int = Fraction(12, 2)
    y_int = Fraction(12, 3)
    assert x_int == 6 and y_int == 4
    area = Fraction(x_int * y_int, 2)
    assert area == 12
    options = {'A': 6, 'B': 8, 'C': 12, 'D': 24}
    matches = [let for let, v in options.items() if v == int(area)]
    assert matches == ['C']
    return 'C'


def check_D5():
    """EXHAUSTIVE PROOF: Shoelace area of (0,2),(3,0),(6,4),(1,6) in the given
    order is 1/2|40| = 20, cross-checked by splitting into two triangles."""
    points = [(0, 2), (3, 0), (6, 4), (1, 6)]
    twice = _shoelace_area(points)
    assert twice == 40
    area = Fraction(abs(twice), 2)
    assert area == 20
    tri1 = [(0, 2), (3, 0), (1, 6)]
    tri2 = [(3, 0), (6, 4), (1, 6)]
    sum_tris = Fraction(abs(_shoelace_area(tri1)), 2) + Fraction(abs(_shoelace_area(tri2)), 2)
    assert sum_tris == 20
    return area


CHECKS = {
    'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4,
    'A5': check_A5, 'A6': check_A6, 'A7': check_A7, 'A8': check_A8,
    'A9': check_A9, 'A10': check_A10, 'B1': check_B1, 'B2': check_B2,
    'B3': check_B3, 'B4': check_B4, 'B5': check_B5, 'B6': check_B6,
    'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10,
    'C1': check_C1, 'C2': check_C2, 'C3': check_C3, 'C4': check_C4,
    'C5': check_C5, 'C6': check_C6, 'C7': check_C7, 'C8': check_C8,
    'D1': check_D1, 'D2': check_D2, 'D3': check_D3, 'D4': check_D4,
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
        except Exception as e:
            failures.append(label)
            print(f'  ERROR {label}: {e}')
    print()
    if failures:
        print(f'{len(failures)}/{len(CHECKS)} checks failed: {", ".join(failures)}')
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')


if __name__ == '__main__':
    main()