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
    """EXHAUSTIVE PROOF: Shoelace on (1,0),(5,2),(4,6),(0,3) in order: cross terms 2+22+12-3 = 33, area 33/2."""
    pts = [(1, 0), (5, 2), (4, 6), (0, 3)]
    twice = _shoelace_area(pts)
    assert twice == 33
    # convex, so the triangle split (1,0),(5,2),(4,6) + (1,0),(4,6),(0,3) agrees
    assert abs(_shoelace_area(pts[:3])) + abs(_shoelace_area([pts[0], pts[2], pts[3]])) == 33
    return Fraction(twice, 2)


# ── Section C ──────────────────────────────────────────────────────────────────
def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sympy.simplify(sympy.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _clip(subject, clipper):
    """Sutherland-Hodgman: the part of convex polygon `subject` inside convex, anticlockwise `clipper`."""
    def inside(p, a, b):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= 0

    def cross(p, q, a, b):
        d = (p[0] - q[0]) * (a[1] - b[1]) - (p[1] - q[1]) * (a[0] - b[0])
        t = Fraction((p[0] - a[0]) * (a[1] - b[1]) - (p[1] - a[1]) * (a[0] - b[0])) / d
        return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))

    out = list(subject)
    for i in range(len(clipper)):
        a, b = clipper[i], clipper[(i + 1) % len(clipper)]
        pts, out = out, []
        for j in range(len(pts)):
            p, q = pts[j], pts[(j + 1) % len(pts)]
            if inside(q, a, b):
                if not inside(p, a, b):
                    out.append(cross(p, q, a, b))
                out.append(q)
            elif inside(p, a, b):
                out.append(cross(p, q, a, b))
    return out


def check_C1():
    """EXHAUSTIVE PROOF: l: y=6-2x (A=(3,0)); m: y=(x-k)/2; triangle area (3-k)^2/5 = 20 with k<0 -> k=-7 (A); k=13 is the other root."""
    x, k = sympy.symbols('x k')
    l1 = 6 - 2 * x
    m = (x - k) / 2
    assert sympy.Rational(-2) * sympy.Rational(1, 2) == -1                  # perpendicular
    xp = sympy.solve(l1 - m, x)[0]
    area = sympy.Rational(1, 2) * (3 - k) * l1.subs(x, xp)
    assert sympy.simplify(area - (3 - k) ** 2 / 5) == 0
    roots = sympy.solve(area - 20, k)
    assert sorted(roots) == [-7, 13]
    kv = [r for r in roots if r < 0][0]
    pts = [(3, 0), (kv, 0), (xp.subs(k, kv), l1.subs(x, xp).subs(k, kv))]
    assert sympy.Abs(_shoelace_area(pts)) == 40
    options = {'A': -7, 'B': -10, 'C': 3 - 5 * sympy.sqrt(2), 'D': 3 - 2 * sympy.sqrt(5)}
    return _only(options, kv)


def check_C2():
    """EXHAUSTIVE PROOF: O on the perpendicular bisector of A(2,-6), B(b,4) iff OA = OB: 40 = b^2 + 16, b = 2 sqrt6 (D); the midpoint/gradient route agrees."""
    b = sympy.Symbol('b', positive=True)
    sol = sympy.solve(sympy.Eq(2 ** 2 + 6 ** 2, b ** 2 + 4 ** 2), b)
    assert sol == [2 * sympy.sqrt(6)]
    bv = sol[0]
    mid = ((2 + bv) / 2, sympy.Integer(-1))
    # O on the bisector: (O - mid) is perpendicular to (B - A)
    assert sympy.simplify((0 - mid[0]) * (bv - 2) + (0 - mid[1]) * (4 + 6)) == 0
    options = {'A': 2 * sympy.sqrt(10), 'B': 2 * sympy.sqrt(14), 'C': 12, 'D': 2 * sympy.sqrt(6)}
    return _only(options, bv)


def check_C3():
    """EXHAUSTIVE PROOF: Reflect A(2,9) in x+2y=5: A' = A - 2*15/5*(1,2) = (-4,-3), |OA'| = 5 (C)."""
    A = sympy.Matrix([2, 9]); n = sympy.Matrix([1, 2])
    k = (A.dot(n) - 5) / n.dot(n)
    A2 = A - 2 * k * n
    assert list(A2) == [-4, -3]
    assert (A + A2).dot(n) / 2 == 5                      # midpoint on the mirror
    assert (A2 - A).dot(sympy.Matrix([2, -1])) == 0      # AA' perpendicular to the mirror
    options = {'A': sympy.sqrt(85), 'B': sympy.sqrt(10), 'C': 5, 'D': sympy.sqrt(185)}
    return _only(options, sympy.sqrt(A2.dot(A2)))


def check_C4():
    """EXHAUSTIVE PROOF: At (1,1): 3x-4y+2=1, 4x-3y-5=-4 (opposite signs) -> bisector L1 + L2 = 0 -> 7x-7y=3 (D)."""
    x, y = sympy.symbols('x y')
    L1, L2 = 3 * x - 4 * y + 2, 4 * x - 3 * y - 5
    s1, s2 = L1.subs({x: 1, y: 1}), L2.subs({x: 1, y: 1})
    assert s1 > 0 and s2 < 0
    bis = sympy.expand(L1 + L2)
    assert bis == 7 * x - 7 * y - 3
    # every point on it is equidistant (normals both have length 5)
    t = sympy.Symbol('t'); pt = {x: t, y: t - sympy.Rational(3, 7)}
    assert sympy.simplify(sympy.Abs(L1.subs(pt)) - sympy.Abs(L2.subs(pt))) == 0
    cands = {'A': x - y - 7, 'B': x + y - 7, 'C': 7 * x + 7 * y - 3, 'D': 7 * x - 7 * y - 3}
    hits = [k for k, e in cands.items() if sympy.simplify(e - bis) == 0]
    assert hits == ['D']
    options = {'A': 'x-y=7', 'B': 'x+y=7', 'C': '7x+7y=3', 'D': '7x-7y=3'}
    assert set(options) == set(cands)
    return 'D'


def check_C5():
    """EXHAUSTIVE PROOF: A(1,4), B(4,7): gradient 1, so C=(10,13); the perpendicular y=23-x meets the y-axis at 23 (A)."""
    g = Fraction(7 - 4, 4 - 1)
    k = 4 + g * (10 - 1)
    assert k == 13
    yint = k - (Fraction(-1) / g) * 10          # y = k + m_perp (x - 10), at x = 0
    assert yint == 23
    options = {'A': 23, 'B': 24, 'C': 25, 'D': 26}
    return _only(options, yint)


def check_C6():
    """EXHAUSTIVE PROOF: [ABC]=36; [APQ]=(1/3)(2/3)[ABC]=8 -> [PBCQ]=28 (B), cross-checked by shoelace."""
    A, B, C = (0, 0), (9, 3), (3, 9)
    P = (Fraction(B[0], 3), Fraction(B[1], 3))
    Q = (Fraction(2 * C[0], 3), Fraction(2 * C[1], 3))
    abc = Fraction(abs(_shoelace_area([A, B, C])), 2)
    assert abc == 36
    quad = Fraction(abs(_shoelace_area([P, B, C, Q])), 2)
    assert quad == abc - Fraction(1, 3) * Fraction(2, 3) * abc
    options = {'A': 24, 'B': 28, 'C': 27, 'D': 32}
    return _only(options, quad)


def check_C7():
    """EXHAUSTIVE PROOF: Vertices (2,5), (6,1), (-2,-3); shoelace area 24 (C)."""
    x, y = sympy.symbols('x y')
    lines = [2 * x + 1, 7 - x, x / 2 - 2]
    pts = []
    for a, b in [(0, 1), (1, 2), (0, 2)]:
        xs = sympy.solve(lines[a] - lines[b], x)[0]
        pts.append((xs, lines[a].subs(x, xs)))
    assert pts == [(2, 5), (6, 1), (-2, -3)]
    area = sympy.Abs(_shoelace_area(pts)) / 2
    options = {'A': 12, 'B': 18, 'C': 24, 'D': 48}
    return _only(options, area)


def check_C8():
    """EXHAUSTIVE PROOF: Clip Q=(0,0),(4,0),(5,3),(1,3) by its reflection in y=x; the overlap has area 6 (A)."""
    Q = [(0, 0), (4, 0), (5, 3), (1, 3)]
    Qr = [(y, x) for (x, y) in Q][::-1]            # reflect, then restore anticlockwise order
    overlap = _clip(Q, Qr)
    area = Fraction(abs(_shoelace_area(overlap))) / 2
    assert Fraction(abs(_shoelace_area(Q))) / 2 == 12
    options = {'A': 6, 'B': 8, 'C': 9, 'D': 12}
    return _only(options, area)


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: A(1,3), B(7,5) lie on opposite sides of y=x, so min PA+PB = AB = 2*sqrt(10) (D), at P=(4,4)."""
    A, B = (1, 3), (7, 5)
    assert (A[1] - A[0]) * (B[1] - B[0]) < 0          # opposite sides
    t = sympy.Symbol('t')
    sol = sympy.solve(sympy.Eq(A[1] + t * (B[1] - A[1]), A[0] + t * (B[0] - A[0])), t)
    P = (A[0] + sol[0] * (B[0] - A[0]), A[1] + sol[0] * (B[1] - A[1]))
    assert P == (4, 4) and 0 < sol[0] < 1
    dist = lambda U, V: sympy.sqrt((U[0] - V[0]) ** 2 + (U[1] - V[1]) ** 2)
    best = dist(P, A) + dist(P, B)
    assert sympy.simplify(best - dist(A, B)) == 0
    # brute force along the line agrees to 1e-6
    grid = min(float(dist((s, s), A) + dist((s, s), B)) for s in [i / 1000 for i in range(0, 8001)])
    assert abs(grid - float(best)) < 1e-6
    options = {'A': 4 * sympy.sqrt(2), 'B': 2 * sympy.sqrt(34), 'C': 10, 'D': 2 * sympy.sqrt(10)}
    return _only(options, best)


def check_D2():
    """EXHAUSTIVE PROOF: R=(x,0), S=(10,10-x), U=(0,x): area 2x(10-x) = 20; diagonal^2 = 2[(10-x)^2 + x^2] = 160 for both roots -> 4 sqrt10 (B)."""
    x = sympy.Symbol('x', positive=True)
    R, S, T, U = (x, 0), (10, 10 - x), (10 - x, 10), (0, x)
    RS = (S[0] - R[0], S[1] - R[1]); RU = (U[0] - R[0], U[1] - R[1])
    assert sympy.simplify(RS[0] * RU[0] + RS[1] * RU[1]) == 0          # right angle at R
    assert sympy.simplify(RS[1] - RS[0]) == 0                            # RS at 45 degrees
    area = sympy.expand(RS[0] * RU[1] - RS[1] * RU[0])
    assert sympy.simplify(area - 2 * x * (10 - x)) == 0
    roots = [r for r in sympy.solve(sympy.Eq(area, 20), x) if 0 < r < 10]
    assert len(roots) == 2
    diags = {sympy.sqrt(sympy.expand((T[0] - R[0]) ** 2 + (T[1] - R[1]) ** 2).subs(x, r)) for r in roots}
    diags = {sympy.nsimplify(sympy.simplify(d)) for d in diags}
    assert len(diags) == 1
    d = diags.pop()
    options = {'A': 4 * sympy.sqrt(15), 'B': 4 * sympy.sqrt(10), 'C': 10, 'D': 4 * sympy.sqrt(5)}
    return _only(options, d)


def check_D3():
    """EXHAUSTIVE PROOF: Rhombus |x|+2|y|<=6 has area 36; the piece below y=x-2 has area 10 -> 26 (C)."""
    rhombus = [(6, 0), (0, 3), (-6, 0), (0, -3)]
    half_plane = [(-100, -102), (100, 98), (-100, 98)]      # y >= x - 2, anticlockwise, large
    region = _clip(rhombus, half_plane)
    area = Fraction(abs(_shoelace_area(region))) / 2
    assert Fraction(abs(_shoelace_area(rhombus))) / 2 == 36
    assert 36 - area == 10
    options = {'A': 10, 'B': 18, 'C': 26, 'D': 36}
    return _only(options, area)


def check_D4():
    """EXHAUSTIVE PROOF: (2m-3)^2 = 24|m|: two positive roots and the double root m=-3/2 -> 3 lines (D)."""
    m = sympy.Symbol('m', real=True)
    pos = [r for r in sympy.solve(sympy.Eq((2 * m - 3) ** 2, 24 * m), m) if r > 0]
    neg = [r for r in sympy.solve(sympy.Eq((2 * m - 3) ** 2, -24 * m), m) if r < 0]
    slopes = set(pos) | set(neg)
    for s in slopes:
        xi, yi = 2 - 3 / s, 3 - 2 * s
        assert sympy.simplify(sympy.Abs(xi * yi) / 2 - 12) == 0
    options = {'A': 1, 'B': 2, 'C': 4, 'D': 3}
    return _only(options, len(slopes))


def check_D5():
    """EXHAUSTIVE PROOF: d^2 = t^2(4-t)^2/(t^2+(4-t)^2) is maximal at t=2, where d = sqrt(2) (C)."""
    t = sympy.Symbol('t', positive=True)
    d2 = (t * (4 - t)) ** 2 / (t ** 2 + (4 - t) ** 2)
    crit = [c for c in sympy.solve(sympy.diff(d2, t), t) if 0 < c < 4]
    assert crit == [2]
    best = sympy.sqrt(d2.subs(t, 2))
    assert all(float(d2.subs(t, s / 100)) <= float(best ** 2) + 1e-12 for s in range(1, 400))
    options = {'A': 1, 'B': 2, 'C': sympy.sqrt(2), 'D': 2 * sympy.sqrt(2)}
    return _only(options, best)


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