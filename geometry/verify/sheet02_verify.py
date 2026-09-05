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
def check_A1():
    """EXHAUSTIVE PROOF: x^2+y^2-6x-8y+24=0 completes to (x-3)^2+(y-4)^2=1,
    so its centre is (3,4)."""
    expr = _complete_square(_X**2 + _Y**2 - 6*_X - 8*_Y + 24)
    cx, cy, r2 = expr
    assert cx == 3 and cy == 4
    assert r2 == 1
    return (3, 4)


def check_A2():
    """EXHAUSTIVE PROOF: Radius squared of the same circle is 1, so r = 1."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 6*_X - 8*_Y + 24)
    assert (cx, cy) == (3, 4)
    assert r2 == 1
    r = sympy.sqrt(r2)
    assert r == 1
    return 1


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
    """EXHAUSTIVE PROOF: Centre (-1,2) radius 3 expands to
    x^2+y^2+2x-4y-4=0, whose orthocentric data completes back to (-1,2), r=3."""
    poly = _circle_poly(-1, 2, 3)
    assert sympy.simplify(poly - (_X**2 + _Y**2 + 2*_X - 4*_Y - 4)) == 0
    cx, cy, r2 = _complete_square(poly)
    assert (cx, cy) == (-1, 2) and r2 == 9
    return _circle_equation_string(-1, 2, 3)


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
    options = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
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
    """EXHAUSTIVE PROOF: y=2x+5 is 2x-y+5=0, at distance 5/sqrt(5)=sqrt(5) from
    the origin; tangency forces r=sqrt(5), so r^2=5, option B."""
    d = _dist_point_line(0, 0, 2, -1, 5)
    assert sympy.simplify(d - sympy.sqrt(5)) == 0
    r2 = sympy.simplify(d**2)
    assert r2 == 5
    options = {'A': 1, 'B': 5, 'C': 25, 'D': 5 * sympy.sqrt(5)}
    matches = [let for let, v in options.items() if sympy.simplify(v - r2) == 0]
    assert matches == ['B']
    return 'B'


def check_C2():
    """EXHAUSTIVE PROOF: With g=f, substituting (2,-1) into
    x^2+y^2+2gx+2fy-3=0 gives 2+2g=0, so g=-1, option A."""
    g = sympy.Symbol('g')
    f = g
    value = sympy.simplify(2**2 + (-1)**2 + 2*g*2 + 2*f*(-1) - 3)
    assert sympy.simplify(value - (2 + 2*g)) == 0
    sols = sympy.solve(sympy.Eq(value, 0), g)
    assert sols == [-1]
    options = {'A': -1, 'B': 0, 'C': 1, 'D': 2}
    matches = [let for let, v in options.items() if v == sols[0]]
    assert matches == ['A']
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: Circle (2,-1), r=4; distance to x-y+1=0 is 2sqrt(2)<4,
    so the line is a secant, option A."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 4*_X + 2*_Y - 11)
    assert (cx, cy) == (2, -1) and r2 == 16
    d = _dist_point_line(cx, cy, 1, -1, 1)
    assert sympy.simplify(d - 2 * sympy.sqrt(2)) == 0
    assert d < sympy.sqrt(r2)
    options = {'A': 'secant', 'B': 'tangent', 'C': 'misses', 'D': 'centre'}
    assert options['A'] == 'secant'
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: Tangent at (2,sqrt(5)) to x^2+y^2=9 is xx1+yy1=r^2, so
    2x+sqrt(5)y=9, option A, and the point lies on both."""
    x1, y1 = 2, sympy.sqrt(5)
    assert sympy.simplify(x1**2 + y1**2 - 9) == 0
    tangent = sympy.simplify(x1 * _X + y1 * _Y - 9)
    assert tangent == 2*_X + sympy.sqrt(5)*_Y - 9
    options = {
        'A': 2*_X + sympy.sqrt(5)*_Y - 9,
        'B': 2*_X - sympy.sqrt(5)*_Y - 9,
        'C': 2*_X + sympy.sqrt(5)*_Y - 3,
        'D': sympy.sqrt(5)*_X + 2*_Y - 9,
    }
    matches = [let for let, eq in options.items() if sympy.simplify(eq - tangent) == 0]
    assert matches == ['A']
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: r^2=40, chord midpoint 2 from centre, so half-chord
    = sqrt(40-4)=6 and the chord is 12, option A."""
    half = sympy.sqrt(40 - 4)
    assert half == 6
    chord = 2 * half
    assert chord == 12
    options = {'A': 12, 'B': 6 * sympy.sqrt(2), 'C': 8, 'D': 4 * sympy.sqrt(10)}
    matches = [let for let, v in options.items() if sympy.simplify(v - chord) == 0]
    assert matches == ['A']
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: A circle is tangent to the x-axis iff the centre's
    y-distance equals the radius; only option A satisfies it."""
    options = {
        'A': _X**2 + _Y**2 - 6*_Y,
        'B': _X**2 + _Y**2 + 4*_X,
        'C': _X**2 + _Y**2 - 6*_X + 9,
        'D': _X**2 + _Y**2 - 2*_Y - 3,
    }
    result = {}
    for let, eq in options.items():
        cx, cy, r2 = _complete_square(eq)
        # A circle touching the x-axis needs a real radius with |y-centre| = r.
        # A is the only real circle with that property; C is degenerate (r=0).
        tangent = r2 > 0 and sympy.simplify(sympy.Abs(cy) - sympy.sqrt(r2)) == 0
        result[let] = bool(tangent)
    assert result['A'] is True
    assert result['B'] is False and result['C'] is False and result['D'] is False
    assert _complete_square(options['C'])[2] == 0   # option C has no real radius
    matches = [let for let, t in result.items() if t]
    assert matches == ['A']
    return 'A'


def check_C7():
    """EXHAUSTIVE PROOF: On the y-axis x=0, the circle x^2+y^2-8x-4y-21=0 gives
    y^2-4y-21=0=(y-7)(y+3), so the intercepts are 7 and -3, distance 10."""
    sols = sympy.solve(_Y**2 - 4*_Y - 21, _Y)
    assert set(sols) == {-3, 7}
    dist = sols[1] - sols[0]
    assert dist == 10
    # cross-check via half-chord: centre (4,2), r=sqrt(41), distance to y-axis 4
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 8*_X - 4*_Y - 21)
    assert (cx, cy) == (4, 2) and r2 == 41
    half = sympy.sqrt(r2 - 4**2)
    assert half == 5
    assert 2 * half == 10
    options = {'A': 4, 'B': 6, 'C': 8, 'D': 10}
    matches = [let for let, v in options.items() if v == 10]
    assert matches == ['D']
    return 'D'


def check_C8():
    """EXHAUSTIVE PROOF: Circle centre (3,4) r=1; the lines y=kx+5 all pass
    through (0,5), which is sqrt(10)>1 from the centre, so there are exactly two
    tangents; the k equation has a positive discriminant."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 6*_X - 8*_Y + 24)
    assert (cx, cy) == (3, 4) and r2 == 1
    assert sympy.simplify((0 - cx)**2 + (5 - cy)**2 - r2) > 0   # (0,5) external
    k = sympy.Symbol('k', real=True)
    eq = sympy.Eq(sympy.Abs(3*k - 4) / sympy.sqrt(k**2 + 1), 1)
    sols = sympy.solve(eq, k)
    assert len(sols) == 2
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    matches = [let for let, v in options.items() if v == len(sols)]
    assert matches == ['C']
    return 'C'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: Circle centre (4,3) r=3; distance to 3x+4y-12=0 is
    12/5, half-chord=sqrt(9-144/25)=9/5, chord=18/5, option A."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 8*_X - 6*_Y + 16)
    assert (cx, cy) == (4, 3) and r2 == 9
    d = _dist_point_line(cx, cy, 3, 4, -12)
    assert sympy.simplify(d - Fraction(12, 5)) == 0
    assert d < sympy.sqrt(r2)
    half = sympy.sqrt(sympy.Rational(9) - d**2)
    assert sympy.simplify(half - Fraction(9, 5)) == 0
    chord = sympy.simplify(2 * half)
    assert sympy.simplify(chord - Fraction(18, 5)) == 0
    options = {'A': Fraction(18, 5), 'B': Fraction(12, 5), 'C': 6, 'D': Fraction(36, 5)}
    matches = [let for let, v in options.items() if sympy.simplify(v - chord) == 0]
    assert matches == ['A']
    return 'A'


def check_D2():
    """EXHAUSTIVE PROOF: Centre (3,k) tangent to the x-axis has radius |k|;
    passing through (0,4) gives 9+(4-k)^2=k^2, so k=25/8, option A."""
    k = sympy.Symbol('k')
    eq = sympy.Eq((0 - 3)**2 + (4 - k)**2, k**2)
    sols = sympy.solve(eq, k)
    assert sols == [sympy.Rational(25, 8)]
    r = sols[0]
    assert r == Fraction(25, 8)
    options = {'A': Fraction(25, 8), 'B': Fraction(25, 9), 'C': 3, 'D': 4}
    matches = [let for let, v in options.items() if sympy.simplify(v - r) == 0]
    assert matches == ['A']
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: Tangent at P=(x1,y1) is x1x+y1y=25; through (7,1) gives
    7x1+y1=25 with x1^2+y1^2=25, solved to x1=3 (first-quadrant root), option B."""
    x1, y1 = sympy.symbols('x1 y1')
    sols = sympy.solve([sympy.Eq(7*x1 + y1, 25), sympy.Eq(x1**2 + y1**2, 25)],
                       [x1, y1])
    assert len(sols) == 2
    first_q = [p for p in sols if p[1] > 0]
    assert first_q == [(3, 4)]
    assert first_q[0][0] == 3
    options = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
    matches = [let for let, v in options.items() if v == first_q[0][0]]
    assert matches == ['B']
    return 'B'


def check_D4():
    """EXHAUSTIVE PROOF: Radius to the tangent line y=2x+1 from centre (1,4) is
    |2-4+1|/sqrt(5)=1/sqrt(5), option A."""
    d = _dist_point_line(1, 4, 2, -1, 1)
    assert sympy.simplify(d - 1 / sympy.sqrt(5)) == 0
    options = {'A': 1 / sympy.sqrt(5), 'B': Fraction(1, 5), 'C': 1, 'D': sympy.sqrt(5)}
    matches = [let for let, v in options.items() if sympy.simplify(v - d) == 0]
    assert matches == ['A']
    return 'A'


def check_D5():
    """EXHAUSTIVE PROOF: The perpendicular bisectors of (0,0)-(6,0) (x=3) and of
    (0,0)-(3,-1) meet at (3,4), which is equidistant from all three points,
    option A."""
    # bisector of (0,0),(6,0): x = 3
    xe = sympy.Symbol('x', real=True)
    ye = sympy.Symbol('y', real=True)
    bis_x = sympy.Eq(xe, 3)
    # bisector of (0,0),(3,-1): gradient 3 through (1.5,-0.5)
    seg_grad = Fraction(-1 - 0, 3 - 0)
    assert seg_grad == Fraction(-1, 3)
    perp_grad = Fraction(-1, seg_grad)
    assert perp_grad == 3
    bis_oe = sympy.Eq(ye + Fraction(1, 2), 3 * (xe - Fraction(3, 2)))
    sol = sympy.solve([bis_x, bis_oe], [xe, ye])
    assert sol == {xe: 3, ye: 4}
    centre = (3, 4)
    dists = [(0 - centre[0])**2 + (0 - centre[1])**2,
             (6 - centre[0])**2 + (0 - centre[1])**2,
             (3 - centre[0])**2 + (-1 - centre[1])**2]
    assert dists[0] == dists[1] == dists[2] == 25
    options = {'A': (3, 4), 'B': (3, 2), 'C': (4, 3), 'D': (5, 0)}
    matches = [let for let, pt in options.items() if pt == centre]
    assert matches == ['A']
    return 'A'


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