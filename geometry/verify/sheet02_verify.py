import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans02.tex'

_X, _Y = sympy.symbols('x y', real=True)


def _complete_square(expr):
    """Return (centre_x, centre_y, radius**2) from x^2+y^2+2gx+2fy+c = 0,
    by completing the square symbolically rather than reading a key."""
    p = sympy.Poly(sympy.expand(expr), _X, _Y)
    cx = -sympy.Rational(p.coeff_monomial(_X), 2)
    cy = -sympy.Rational(p.coeff_monomial(_Y), 2)
    c0 = p.coeff_monomial(sympy.Integer(1))
    r2 = sympy.expand(cx**2 + cy**2 - c0)
    return cx, cy, r2


def _dist_point_line(px, py, a, b, c):
    """Exact perpendicular distance from (px,py) to ax+by+c=0 (sympy rational)."""
    num = abs(a * px + b * py + c)
    den = sympy.sqrt(a * a + b * b)
    return num / den


def _circle_poly(cx, cy, r):
    """Expanded circle polynomial (x-cx)^2+(y-cy)^2-r^2 for a centred circle."""
    return sympy.expand((_X - cx)**2 + (_Y - cy)**2 - r**2)


def _circle_equation_string(cx, cy, r):
    """Render the expanded circle in the fixed x^2,y^2,x,y,c order the answers
    use, so the returned string ties to the printed key exactly."""
    p = sympy.Poly(_circle_poly(cx, cy, r), _X, _Y)
    coeffs = {
        'x^2': p.coeff_monomial(_X**2),
        'y^2': p.coeff_monomial(_Y**2),
        'x': p.coeff_monomial(_X),
        'y': p.coeff_monomial(_Y),
    }
    const = p.coeff_monomial(1)
    out = ''
    first = True
    for var, coef in coeffs.items():
        if coef == 0:
            continue
        mag = abs(coef)
        token = mag if mag != 1 else ''
        if first:
            out += (f'-{token}{var}' if coef < 0 else f'{token}{var}')
            first = False
        else:
            out += (f'-{token}{var}' if coef < 0 else f'+{token}{var}')
    if const != 0:
        mag = abs(const)
        out += f'-{mag}' if const < 0 else f'+{mag}'
    return out + '=0'


# ── Section A ──────────────────────────────────────────────────────────────────
def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sympy.simplify(sympy.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def check_A1():
    """EXHAUSTIVE PROOF: x^2+y^2-6x-8y+24=0 completes to (x-3)^2+(y-4)^2=1,
    so its centre is (3,4)."""
    expr = _complete_square(_X**2 + _Y**2 - 6*_X - 8*_Y + 24)
    cx, cy, r2 = expr
    assert cx == 3 and cy == 4
    assert r2 == 1
    return (3, 4)


def check_A2():
    """EXHAUSTIVE PROOF: x^2+y^2-6x+4y+k=0 is (x-3)^2+(y+2)^2 = 13-k; radius 5 needs k = -12."""
    k = sympy.Symbol('k')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 6*_X + 4*_Y + k)
    assert (cx, cy) == (3, -2)
    sol = sympy.solve(sympy.Eq(r2, 25), k)
    assert sol == [-12]
    return sol[0]


def check_A3():
    """EXHAUSTIVE PROOF: Circle centre (2,-1) radius 5 expands to
    x^2+y^2-4x+2y-20=0, and completing the square recovers (2,-1), r=5."""
    poly = _circle_poly(2, -1, 5)
    assert sympy.simplify(poly - (_X**2 + _Y**2 - 4*_X + 2*_Y - 20)) == 0
    cx, cy, r2 = _complete_square(poly)
    assert (cx, cy) == (2, -1) and r2 == 25
    return _circle_equation_string(2, -1, 5)


def check_A4():
    """EXHAUSTIVE PROOF: x^2+y^2-4x+6y-12=0 has r^2=4+9+12=25, so r=5."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 4*_X + 6*_Y - 12)
    assert (cx, cy) == (2, -3)
    assert r2 == 25
    assert sympy.sqrt(r2) == 5
    return 5


def check_A5():
    """EXHAUSTIVE PROOF: (x,4) on x^2+y^2=25 gives x^2=9; the positive root is
    x=3, and 3^2+4^2=25."""
    assert _X**2 + 4**2 - 25 == _X**2 + 16 - 25 == _X**2 - 9
    sols = sympy.solve(sympy.Eq(_X**2 + 16, 25), _X)
    assert set(sols) == {-3, 3}
    positive = [s for s in sols if s > 0]
    assert positive == [3]
    assert 3**2 + 4**2 == 25
    return 3


def check_A6():
    """EXHAUSTIVE PROOF: Gradient of radius from (0,0) to (3,4) is (4-0)/(3-0)
    = 4/3, the same whichever direction it is read."""
    m1 = Fraction(4 - 0, 3 - 0)
    m2 = Fraction(0 - 4, 0 - 3)
    assert m1 == Fraction(4, 3)
    assert m1 == m2
    return m1


def check_A7():
    """EXHAUSTIVE PROOF: Radius gradient is 4/3, so the tangent gradient is the
    negative reciprocal -3/4; the tangent line 3x+4y=25 has exactly that slope."""
    m_rad = Fraction(4, 3)
    m_tan = Fraction(-1, m_rad)
    assert m_tan == Fraction(-3, 4)
    assert m_rad * m_tan == -1
    x = sympy.Symbol('x')
    tan_line = (25 - 3 * x) / 4
    assert sympy.simplify(tan_line - (Fraction(-3, 4) * x + Fraction(25, 4))) == 0
    assert m_tan == Fraction(-3, 4)
    return m_tan


def check_A8():
    """EXHAUSTIVE PROOF: Centre (3,-4) through the origin: r = 5, circle (x-3)^2+(y+4)^2 = 25."""
    r2 = 3**2 + (-4)**2
    assert r2 == 25
    poly = _circle_poly(3, -4, 5)
    assert poly.subs({_X: 0, _Y: 0}) == 0          # passes through the origin
    return sympy.Eq((_X - 3)**2 + (_Y + 4)**2, r2)


def check_A9():
    """EXHAUSTIVE PROOF: Distance from centre (3,4) to 4x+3y-9=0 is
    |12+12-9|/5 = 3, via the exact distance formula."""
    d = _dist_point_line(3, 4, 4, 3, -9)
    assert sympy.simplify(d - 3) == 0
    assert d == 3
    return int(d)


def check_A10():
    """EXHAUSTIVE PROOF: Chord at distance 3 from the centre of radius 5 has
    half-length sqrt(25-9)=4, so the chord is 8 long; the midpoint claim is
    checked by Pythagoras."""
    half = sympy.sqrt(25 - 9)
    assert half == 4
    assert sympy.simplify(half**2 + 3**2 - 25) == 0
    return int(2 * half)


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: Centre (3,-2) radius 4 gives x^2+y^2-6x+4y-3=0; each
    option completes back to its own data, and only A matches."""
    target = _circle_poly(3, -2, 4)
    options = {
        'A': _X**2 + _Y**2 - 6*_X + 4*_Y - 3,
        'B': _X**2 + _Y**2 - 6*_X + 4*_Y + 9,
        'C': _X**2 + _Y**2 + 6*_X - 4*_Y - 3,
        'D': _X**2 + _Y**2 - 6*_X - 4*_Y - 3,
    }
    sols = []
    for let, eq in options.items():
        if sympy.simplify(eq - target) == 0:
            sols.append(let)
        cx, cy, r2 = _complete_square(eq)
        assert r2 > 0                       # every option is a real circle
        if let == 'B':
            assert (cx, cy) == (3, -2) and r2 == 4   # same centre data, wrong radius
    assert sols == ['A']
    return 'A'


def check_B2():
    """EXHAUSTIVE PROOF: x^2+y^2+2x-4y-11=0 has r^2=1+4+11=16, so r=4 which is
    option C."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 + 2*_X - 4*_Y - 11)
    assert (cx, cy) == (-1, 2)
    assert r2 == 16
    assert sympy.sqrt(r2) == 4
    options = {'A': 2, 'B': 3, 'C': 4, 'D': sympy.sqrt(5)}
    matches = [let for let, v in options.items() if v == sympy.sqrt(r2)]
    assert matches == ['C']
    return 'C'


def check_B3():
    """EXHAUSTIVE PROOF: Radius slope 2, tangent slope -1/2 through (1,2) gives
    y = -1/2 x + 5/2, option A."""
    m_rad = Fraction(2 - 0, 1 - 0)
    assert m_rad == 2
    m_tan = Fraction(-1, m_rad)
    assert m_tan == Fraction(-1, 2)
    c = 2 - m_tan * 1
    assert c == Fraction(5, 2)
    x = sympy.Symbol('x')
    line = m_tan * x + c
    assert line.subs(x, 1) == 2
    options = {
        'A': Fraction(-1, 2) * x + Fraction(5, 2),
        'B': 2 * x,
        'C': -2 * x + 5,
        'D': Fraction(1, 2) * x,
    }
    matches = [let for let, eq in options.items() if sympy.simplify(eq - line) == 0]
    assert matches == ['A']
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: Substituting the origin into x^2+y^2+2gx+2fy+c leaves
    c=0, so the origin is on the circle exactly when c=0."""
    x0 = sympy.Symbol('g')
    y0 = sympy.Symbol('f')
    c = sympy.Symbol('c')
    at_origin = sympy.simplify(0 + 0 + 2*x0*0 + 2*y0*0 + c)
    assert at_origin == c
    assert sympy.solve(sympy.Eq(at_origin, 0), c) == [0]
    options = {'A': 1, 'B': 0, 'C': x0 + y0, 'D': -1}
    matches = [let for let, v in options.items() if sympy.simplify(v - 0) == 0]
    assert matches == ['B']
    return 'B'


def check_B5():
    """EXHAUSTIVE PROOF: Distance from (0,0) to y=2x+3 (i.e. 2x-y+3=0) is
    3/sqrt(5), less than r=5, so the line cuts the circle."""
    d = _dist_point_line(0, 0, 2, -1, 3)
    assert sympy.simplify(d - sympy.sqrt(Fraction(9, 5))) == 0
    assert sympy.simplify(d - 3 / sympy.sqrt(5)) == 0
    assert d < 5
    options = {
        'A': 3 / sympy.sqrt(5),
        'B': Fraction(3, 5),
        'C': 3,
        'D': 2,
    }
    matches = [let for let, v in options.items() if sympy.simplify(v - d) == 0]
    assert matches == ['A']
    return 'A'


def check_B6():
    """EXHAUSTIVE PROOF: Each option line's distance from the origin is compared
    against r=2; only y=x+2sqrt(2) has distance exactly 2."""
    r = 2
    options = {
        'A': (1, -1, 2 * math.sqrt(2)),
        'B': (1, -1, 4),
        'C': (2, -1, 2),
        'D': (2, -1, 4),
    }
    dists = {}
    for let, (a, b, c) in options.items():
        val = abs(c) / math.sqrt(a*a + b*b)
        dists[let] = val
    for let in ('B', 'C', 'D'):
        assert not math.isclose(dists[let], r, rel_tol=1e-9)
    tangent = [let for let, d in dists.items() if math.isclose(d, r, rel_tol=1e-9)]
    assert tangent == ['A']
    return 'A'


def check_B7():
    """EXHAUSTIVE PROOF: A chord of length 4*sqrt(3) has half-length 2*sqrt(3);
    Pythagoras gives d^2=r^2-12=1, so d=1, option D."""
    r2 = 13
    half = 2 * math.sqrt(3)
    d2 = r2 - half**2
    assert math.isclose(d2, 1, rel_tol=1e-9)
    d = math.sqrt(d2)
    assert math.isclose(d, 1, rel_tol=1e-9)
    options = {'A': 3, 'B': 2, 'C': math.sqrt(5), 'D': 1}
    matches = [let for let, v in options.items() if math.isclose(v, d, rel_tol=1e-9)]
    assert matches == ['D']
    return 'D'


def check_B8():
    """EXHAUSTIVE PROOF: mx-y+4=0 tangent to x^2+y^2=4 requires
    4/sqrt(m^2+1)=2, so m^2+1=4 and m=±sqrt(3), option B."""
    m = sympy.Symbol('m', real=True)
    eq = sympy.Eq(4 / sympy.sqrt(m**2 + 1), 2)
    sols = sympy.solve(eq, m)
    assert set(sympy.nsimplify(s) for s in sols) == {sympy.sqrt(3), -sympy.sqrt(3)}
    options = {'A': [1, -1], 'B': [sympy.sqrt(3), -sympy.sqrt(3)],
               'C': [2, -2], 'D': [sympy.sqrt(2), -sympy.sqrt(2)]}
    matches = [let for let, vals in options.items()
               if sorted(set(sympy.simplify(v) for v in vals)) ==
                  sorted(set(sympy.simplify(s) for s in sols))]
    assert matches == ['B']
    return 'B'


def check_B9():
    """EXHAUSTIVE PROOF: Tangent to the y-axis with centre (6,a) and r=6 forces
    the x-distance 6; passing through (0,8) yields (8-a)^2=0 so a=8, option D."""
    a = sympy.Symbol('a')
    eq = sympy.Eq((0 - 6)**2 + (8 - a)**2, 36)
    sols = sympy.solve(eq, a)
    assert sols == [8]
    assert _dist_point_line(6, sols[0], 1, 0, 0) == 6     # x-distance to y-axis
    c = sols[0]
    assert sympy.simplify((0 - 6)**2 + (8 - c)**2 - 36) == 0
    options = {'A': 1, 'B': 3, 'C': 5, 'D': 8}
    matches = [let for let, v in options.items() if v == c]
    assert matches == ['D']
    return 'D'


def check_B10():
    """EXHAUSTIVE PROOF: y=x+1 (i.e. x-y+1=0) at distance 1/sqrt(2) from the
    origin; half-chord=sqrt(25-1/2)=7/sqrt(2), full chord 7*sqrt(2)."""
    d = _dist_point_line(0, 0, 1, -1, 1)
    assert sympy.simplify(d - 1 / sympy.sqrt(2)) == 0
    half = sympy.sqrt(sympy.Rational(25, 1) - d**2)
    assert sympy.simplify(half - 7 / sympy.sqrt(2)) == 0
    chord = sympy.simplify(2 * half)
    assert sympy.simplify(chord - 7 * sympy.sqrt(2)) == 0
    return chord


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: tangent to x^2+y^2=r^2 with intercepts a, b: area ab/2 = 150, a^2+b^2 = 625 -> {a,b} = {15,20}; r = ab/AB = 12 (B)."""
    a, b = sympy.symbols('a b', positive=True)
    sols = sympy.solve([a*b - 300, a**2 + b**2 - 625], [a, b], dict=True)
    assert {(s[a], s[b]) for s in sols} == {(15, 20), (20, 15)}
    r = sympy.Rational(2*150, 25)
    # the line x/20 + y/15 = 1 is at distance r from the origin
    assert sympy.Abs(-300) / sympy.sqrt(15**2 + 20**2) == r
    options = {'A': 6, 'B': 12, 'C': 15, 'D': sympy.Rational(25, 2)}
    return _only(options, r)


def check_C2():
    """EXHAUSTIVE PROOF: P(8,6) to x^2+y^2=36: OP=10, AP=8, distance to chord 18/5, half-chord 24/5, AB=48/5 (option C)."""
    r = 6
    op = math.hypot(8,6)
    assert op == 10
    ap = math.sqrt(op**2 - r**2)
    assert ap == 8
    d = r**2 / op
    assert Fraction(d).limit_denominator() == Fraction(18,5)  # 3.6
    half = math.sqrt(r**2 - d**2)
    assert math.isclose(half, 24/5, rel_tol=1e-9)
    ab = 2*half
    assert math.isclose(ab, 48/5, rel_tol=1e-9)
    # sympy exact check
    assert sympy.simplify(sympy.sqrt(36 - (sympy.Rational(18,5))**2) - sympy.Rational(24,5)) == 0
    options = {'A': sympy.Rational(12,1)*sympy.sqrt(13)/13, 'B': sympy.Rational(24,1)*sympy.sqrt(13)/13, 'C': sympy.Rational(48,5), 'D': sympy.Rational(72,5)}
    matches = [let for let,v in options.items() if sympy.simplify(v - sympy.Rational(48,5)) == 0]
    assert matches == ['C']
    return 'C'


def check_C3():
    """EXHAUSTIVE PROOF: Circle centre (1,-2), r=5; P(13,3) is 13 from the centre, so least PQ = 13 - 5 = 8 (D)."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 2*_X + 4*_Y - 20)
    assert (cx, cy, r2) == (1, -2, 25)
    d = sympy.sqrt((13 - cx)**2 + (3 - cy)**2)
    assert d == 13
    least = d - sympy.sqrt(r2)
    # brute force over the circle agrees
    pts = [(cx + 5 * math.cos(2 * math.pi * i / 3600), cy + 5 * math.sin(2 * math.pi * i / 3600)) for i in range(3600)]
    assert abs(min(math.hypot(13 - a, 3 - b) for a, b in pts) - float(least)) < 1e-4
    options = {'A': 13, 'B': 18, 'C': 12, 'D': 8}
    return _only(options, least)


def check_C4():
    """EXHAUSTIVE PROOF: hexagon area (3 sqrt3/2) r^2 = 54 sqrt3 -> r^2 = 36; x^2+y^2-18x-22y+c: r^2 = 202 - c -> c = 166 (B)."""
    c = sympy.Symbol('c')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 18*_X - 22*_Y + 166)
    assert (cx, cy, r2) == (9, 11, 36)
    s = sympy.sqrt(r2)
    hexagon = 6 * sympy.sqrt(3) / 4 * s**2
    assert sympy.simplify(hexagon - 54*sympy.sqrt(3)) == 0
    sol = sympy.solve(81 + 121 - c - 36, c)
    options = {'A': 196, 'B': 166, 'C': 130, 'D': 238}
    return _only(options, sol[0])


def check_C5():
    """EXHAUSTIVE PROOF: (x-p)^2+(y-2)^2 = 2p^2-6p; touching the y-axis: p^2 = 2p^2-6p -> p in {0, 6}; p = 0 is a point, so r = 6 (A)."""
    p = sympy.Symbol('p', real=True)
    x, y = sympy.symbols('x y')
    lhs = sympy.expand(x**2 - 2*p*x + y**2 - 4*y - p**2 + 6*p + 4)
    assert sympy.expand((x - p)**2 + (y - 2)**2 - (2*p**2 - 6*p) - lhs) == 0
    roots = sympy.solve(p**2 - (2*p**2 - 6*p), p)
    assert sorted(roots) == [0, 6]
    circles = [q for q in roots if 2*q**2 - 6*q > 0]
    assert circles == [6]
    r = sympy.sqrt(2*6**2 - 6*6)
    assert r == 6 == abs(circles[0])
    options = {'A': 6, 'B': 3, 'C': 2, 'D': '0 or 6'}
    hits = [k for k, v in options.items() if not isinstance(v, str) and v == r]
    assert hits == ['A']
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: Centre (2,-1) r=4 vs line x-y+1=0 distance 2√2<r => 2 points (C)."""
    cx,cy,r2 = _complete_square(_X**2+_Y**2-4*_X+2*_Y-11)
    assert (cx,cy) == (2,-1) and r2 == 16
    d = _dist_point_line(cx,cy,1,-1,1)
    assert sympy.simplify(d - 2*sympy.sqrt(2)) == 0
    assert d < sympy.sqrt(r2)
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 'cannot be decided'}
    assert options['C'] == 2
    return 'C'


def check_C7():
    """EXHAUSTIVE PROOF: Centre (4,2) r=√41 distance to x=0 is 4, half-chord 5, length 10 (D)."""
    cx,cy,r2 = _complete_square(_X**2+_Y**2-8*_X-4*_Y-21)
    assert (cx,cy) == (4,2) and r2 == 41
    d = sympy.Abs(cx)  # distance to y-axis x=0
    assert d == 4
    half = sympy.sqrt(r2 - d**2)
    assert half == 5
    length = 2*half
    assert length == 10
    options = {'A': 2*sympy.sqrt(21), 'B': 2*sympy.sqrt(41), 'C': 8, 'D': 10}
    matches = [let for let,v in options.items() if sympy.simplify(v - length) == 0]
    assert matches == ['D']
    return 'D'


def check_C8():
    """EXHAUSTIVE PROOF: Centre (3,4) r=1, point (0,5) external => 2 tangents, so 2 k (C)."""
    cx,cy,r2 = _complete_square(_X**2+_Y**2-6*_X-8*_Y+24)
    assert (cx,cy) == (3,4) and r2 == 1
    assert (0-cx)**2+(5-cy)**2 > r2
    k = sympy.Symbol('k', real=True)
    # distance from centre to y=kx+5: |3k-4+5|/sqrt(k^2+1)=1
    eq = sympy.Eq(sympy.Abs(3*k+1)/sympy.sqrt(k**2+1), 1)
    sols = sympy.solve(eq, k)
    assert len(sols) == 2
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 999}
    matches = [let for let,v in options.items() if v == 2]
    assert matches == ['C']
    return 'C'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: centres 9 sqrt2 apart, r1 = 3 sqrt2: external r = 6 sqrt2, internal (C1 inside C2) r = 12 sqrt2; sum 18 sqrt2 (C)."""
    r = sympy.Symbol('r', positive=True)
    d = sympy.sqrt(9**2 + 9**2)
    r1 = sympy.sqrt(18)
    assert _complete_square(_X**2 + _Y**2 + 4*_X - 6*_Y + 13 - 18) == (-2, 3, 18)
    cands = set()
    for eq in (r + r1 - d, r - r1 - d, r1 - r - d):                 # external, C1 inside C2, C2 inside C1
        cands |= set(sympy.solve(eq, r))
    cands = {sympy.nsimplify(c) for c in cands}
    assert cands == {6*sympy.sqrt(2), 12*sympy.sqrt(2)}
    options = {'A': 6*sympy.sqrt(2), 'B': 12*sympy.sqrt(2), 'C': 18*sympy.sqrt(2), 'D': 9*sympy.sqrt(2)}
    return _only(options, sum(cands))


def check_D2():
    """EXHAUSTIVE PROOF: forward map c -> 4 * reflect(c - (3,0)); centre (5,4), radius sqrt5 maps to (8,-16), radius^2 80; the inverse is unique (B)."""
    fwd = lambda c: (4*(c[0] - 3), 4*(-(c[1])))
    assert fwd((5, 4)) == (8, -16)
    assert (4*sympy.sqrt(5))**2 == 80
    X, Y = sympy.symbols('X Y')
    sol = sympy.solve([4*(X - 3) - 8, -4*Y + 16], [X, Y], dict=True)
    assert sol == [{X: 5, Y: 4}]
    assert fwd((-1, 4)) != (8, -16) and fwd((5, -4)) != (8, -16) and fwd((sympy.Rational(11, 4), 4)) != (8, -16)
    options = {'A': (-1, 4), 'B': (5, 4), 'C': (5, -4), 'D': (sympy.Rational(11, 4), 4)}
    hits = [k for k, v in options.items() if v == (sol[0][X], sol[0][Y])]
    assert hits == ['B']
    return 'B'


def check_D3():
    """EXHAUSTIVE PROOF: greatest [PRQ] = 36 sin(phi)(1 + cos(phi)) with angle POQ = 2 phi; = 27 sqrt3 only at phi = 60, so angle POQ = 120 (B)."""
    f = lambda deg: 36*math.sin(math.radians(deg))*(1 + math.cos(math.radians(deg)))
    target = 27*math.sqrt(3)
    near = [k/100 for k in range(1, 9000) if abs(f(k/100) - target) < 1e-6]
    assert near and all(abs(v - 60) < 0.05 for v in near)
    assert max(f(k/100) for k in range(1, 9000)) <= target + 1e-9      # 27 sqrt3 is the maximum: equilateral
    # coordinates: P, Q at +-60 degrees from the bottom, R at the top
    P = (6*math.sin(math.radians(60)), -6*math.cos(math.radians(60)))
    Q = (-P[0], P[1]); R = (0, 6)
    area = abs((Q[0]-P[0])*(R[1]-P[1]) - (R[0]-P[0])*(Q[1]-P[1])) / 2
    assert abs(area - target) < 1e-9
    options = {'A': 90, 'B': 120, 'C': 60, 'D': 150}
    return _only(options, 2*60)


def check_D4():
    """EXHAUSTIVE PROOF: Tangents y=mx from O to (x-5)^2+(y-5)^2=5: 2m^2-5m+2=0, m = 2, 1/2; tan(angle) = 3/4 (A)."""
    m = sympy.Symbol('m')
    ms = sorted(sympy.solve(sympy.Eq((5*m - 5)**2, 5*(m**2 + 1)), m))
    assert ms == [sympy.Rational(1, 2), 2]
    tan = sympy.Abs((ms[1] - ms[0]) / (1 + ms[0]*ms[1]))
    # half-angle route agrees: tan(t/2) = r / tangent length = sqrt5 / sqrt(50-5) = 1/3
    th = sympy.sqrt(5) / sympy.sqrt(50 - 5)
    assert sympy.simplify(2*th / (1 - th**2) - tan) == 0
    options = {'A': sympy.Rational(3, 4), 'B': sympy.Rational(4, 3), 'C': sympy.Rational(5, 2), 'D': 1}
    return _only(options, tan)


def check_D5():
    """EXHAUSTIVE PROOF: Circle through (0,0),(8,0),(2,6): centre (4,2), r^2 = 20; meets x=0 again at (0,4), so OQ = 4 (D)."""
    a, b = sympy.symbols('a b')
    sol = sympy.solve([sympy.Eq(a**2 + b**2, (a - 8)**2 + b**2), sympy.Eq(a**2 + b**2, (a - 2)**2 + (b - 6)**2)], [a, b])
    assert (sol[a], sol[b]) == (4, 2)
    ys = sympy.solve(sympy.Eq((0 - 4)**2 + (_Y - 2)**2, 20), _Y)
    other = [y for y in ys if y != 0]
    assert other == [4]
    options = {'A': 2*sympy.sqrt(5), 'B': 6, 'C': 2, 'D': 4}
    return _only(options, other[0])


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