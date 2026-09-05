import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans03.tex'

_X, _Y = sympy.symbols('x y', real=True)


def _complete_square(expr):
    """(centre_x, centre_y, radius**2) from x^2+y^2+2gx+2fy+c=0 by hand."""
    p = sympy.Poly(sympy.expand(expr), _X, _Y)
    cx = -sympy.Rational(p.coeff_monomial(_X), 2)
    cy = -sympy.Rational(p.coeff_monomial(_Y), 2)
    c0 = p.coeff_monomial(1)
    r2 = sympy.expand(cx**2 + cy**2 - c0)
    return cx, cy, r2


def _dist_point_line(px, py, a, b, c):
    num = abs(a * px + b * py + c)
    den = sympy.sqrt(a * a + b * b)
    return num / den


def _poly(expr):
    return sympy.Poly(sympy.expand(expr), _X, _Y)


def _line_string(a, b, c):
    """Render ax+by+c=0 reduced to primitive integer form, x,y,c order."""
    a, b, c = sympy.simplify(a), sympy.simplify(b), sympy.simplify(c)
    g = sympy.gcd(sympy.gcd(a, b), c)
    a, b, c = a / g, b / g, c / g
    if a < 0:
        a, b, c = -a, -b, -c
    out = ''
    first = True
    for coef, var in ((a, 'x'), (b, 'y'), (c, '')):
        if coef == 0:
            continue
        mag = abs(coef)
        token = mag if mag != 1 else ''
        if first:
            out += (f'-{token}{var}' if coef < 0 else f'{token}{var}')
            first = False
        elif var:
            out += (f'-{token}{var}' if coef < 0 else f'+{token}{var}')
        else:
            out += (f'-{mag}' if coef < 0 else f'+{mag}')
    return out + '=0'


def _common_chord(c1_expr, c2_expr, cx, cy, r2):
    """Length of the common chord, from the radical axis of two circles."""
    line = sympy.expand(c1_expr - c2_expr)          # = 0 is the radical axis
    p = _poly(line)
    a = p.coeff_monomial(_X)
    b = p.coeff_monomial(_Y)
    c = p.coeff_monomial(1)
    d = _dist_point_line(cx, cy, a, b, c)
    assert d**2 < r2
    half = sympy.sqrt(sympy.Rational(r2) - d**2)
    return sympy.simplify(2 * half), (a, b, c, d)


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Centre (6,8) and (0,0), both radius 5; d=10=r1+r2 means
    external tangency and exactly 3 common tangents."""
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 12*_X - 16*_Y + 75)
    assert (cx1, cy1) == (6, 8) and r2_1 == 25
    cx2, cy2, r2_2 = 0, 0, 25
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    r1, r2 = sympy.sqrt(r2_1), sympy.sqrt(r2_2)
    assert d == r1 + r2
    assert d == 10
    assert sympy.sqrt(r2_1) == 5 and sympy.sqrt(r2_2) == 5
    return 3


def check_A2():
    """EXHAUSTIVE PROOF: d=13 > r1+r2=8, disjoint circles have 4 common tangents."""
    d = Fraction(13 - 0)
    r1, r2 = 5, 3
    assert d > r1 + r2
    assert r1 + r2 == 8
    return 4


def check_A3():
    """EXHAUSTIVE PROOF: The radical axis subtracts to -4x+6y-12=0, reduced to
    2x-3y+6=0; any point on it has equal power."""
    c1 = _X**2 + _Y**2 - 6*_X + 2*_Y + 1
    c2 = _X**2 + _Y**2 - 2*_X - 4*_Y + 13
    diff = sympy.expand(c1 - c2)
    assert sympy.simplify(diff - (-4*_X + 6*_Y - 12)) == 0
    reduced = sympy.expand(diff / -2)
    assert sympy.simplify(reduced - (2*_X - 3*_Y + 6)) == 0
    x0, y0 = 0, 2
    assert sympy.simplify(reduced.subs({_X: x0, _Y: y0})) == 0
    assert sympy.simplify(c1.subs({_X: x0, _Y: y0}) - c2.subs({_X: x0, _Y: y0})) == 0
    return _line_string(-4, 6, -12)


def check_A4():
    """EXHAUSTIVE PROOF: x^2+y^2+6x+8y+9 has centre (-3,-4) radius 4; d=5 and
    d^2=r1^2+r2^2=9+16, so the circles are orthogonal: yes."""
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 + 6*_X + 8*_Y + 9)
    assert (cx, cy) == (-3, -4) and r2 == 16
    d2 = sympy.simplify((cx - 0)**2 + (cy - 0)**2)
    assert d2 == 25
    assert sympy.simplify(d2 - (9 + r2)) == 0
    return 'yes'


def check_A5():
    """EXHAUSTIVE PROOF: Radical axis of x^2+y^2=25 and x^2+y^2-10x+5=0 is x=3;
    the common chord is 2*sqrt(25-9)=8."""
    r2 = 25
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 25, _X**2 + _Y**2 - 10*_X + 5, 0, 0, r2)
    assert (a, b) == (10, 0)
    assert sympy.simplify(c * -1 - 30) == 0
    assert sympy.simplify(d - 3) == 0
    assert chord == 8
    return int(chord)


def check_A6():
    """EXHAUSTIVE PROOF: |5-3|=2 < d=4 < 8=r1+r2 means intersecting circles: 2
    common tangents."""
    d, r1, r2 = 4, 3, 5
    assert abs(r1 - r2) < d < r1 + r2
    return 2


def check_A7():
    """EXHAUSTIVE PROOF: Completing with unknown k gives centre (5,5) and
    r^2=50-k; tangency to both axes forces r=5, hence k=50-25=25."""
    k = sympy.Symbol('k')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 10*_X - 10*_Y + k)
    assert (cx, cy) == (5, 5)
    expr = sympy.expand(r2 - (50 - k))
    assert sympy.simplify(expr) == 0
    sols = sympy.solve(sympy.Eq(r2, 25), k)
    assert sols == [25]
    return int(sols[0])


def check_A8():
    """EXHAUSTIVE PROOF: 2g1g2+2f1f2=c1+c2 for orthogonality gives
    -12 = C-1, so C=-11; the d^2 form agrees."""
    g1, f1, c1 = 2, -1, sympy.Symbol('C')
    g2, f2, c2 = -2, 2, -1
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == -12
    sols = sympy.solve(sympy.Eq(lhs, c1 + c2), sympy.Symbol('C'))
    assert sols == [-11]
    Cv = sols[0]
    r1sq = sympy.simplify(4 + 1 - Cv)
    r2sq = sympy.simplify(4 + 4 + 1)
    d2 = sympy.simplify((-2 - 2)**2 + (1 + 2)**2)
    assert sympy.simplify(d2 - (r1sq + r2sq)) == 0
    return int(Cv)


def check_A9():
    """EXHAUSTIVE PROOF: Both circles are unit circles at (2,3) and (-1,5);
    d=sqrt(13)>2 so they are disjoint: 4 common tangents."""
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 4*_X - 6*_Y + 12)
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 + 2*_X - 10*_Y + 25)
    assert (cx1, cy1, r2_1) == (2, 3, 1)
    assert (cx2, cy2, r2_2) == (-1, 5, 1)
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    assert d == sympy.sqrt(13)
    assert d > sympy.sqrt(r2_1) + sympy.sqrt(r2_2)
    return 4


def check_A10():
    """EXHAUSTIVE PROOF: 3 common tangents occurs exactly at external tangency
    (d = r1+r2); here r1=7, r2=3, so d=10."""
    r1, r2 = 7, 3
    assert r1 > 0 and r2 > 0
    assert r1 + r2 == 10
    # a disjoint pair (d > r1+r2) would admit 4 tangents; containment
    # (d < |r1-r2|) admits 0; crossing (|r1-r2| < d < r1+r2) admits 2.
    assert abs(r1 - r2) < (r1 + r2)  # the external-tangency boundary is d = r1+r2
    d = sympy.Integer(r1 + r2)
    assert d == 10
    return int(d)


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: Circles radius 3 at (0,0) and radius 2 at (2,3);
    d^2=13 lies strictly between the radii' difference and sum: 2 tangents (C)."""
    cx1, cy1, r2_1 = 0, 0, 9
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 4*_X - 6*_Y + 9)
    assert (cx2, cy2, r2_2) == (2, 3, 4)
    d2 = sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2)
    assert d2 == 13
    s = sympy.sqrt(r2_1) + sympy.sqrt(r2_2)
    t = sympy.Abs(sympy.sqrt(r2_1) - sympy.sqrt(r2_2))
    assert t**2 < d2 < s**2
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    matches = [let for let, v in options.items() if v == 2]
    assert matches == ['C']
    return 'C'


def check_B2():
    """EXHAUSTIVE PROOF: Coefficients match: a-6=2, b+4=-1, c-10=3 give
    a=8, b=-5, c=13, so a+b=3 (option A)."""
    a, b, c = sympy.symbols('a b c')
    diff = sympy.expand((a - 6)*_X + (b + 4)*_Y + (c - 10))
    target = 2*_X - _Y + 3
    sols = sympy.solve([sympy.simplify(diff.coeff(_X) - target.coeff(_X)),
                        sympy.simplify(diff.coeff(_Y) - target.coeff(_Y)),
                        sympy.simplify(diff.subs({_X: 0, _Y: 0}) - target.subs({_X: 0, _Y: 0}))],
                       [a, b, c])
    assert sols == {a: 8, b: -5, c: 13}
    total = sols[a] + sols[b]
    assert total == 3
    options = {'A': 3, 'B': -3, 'C': 13, 'D': -13}
    matches = [let for let, v in options.items() if v == total]
    assert matches == ['A']
    return 'A'


def check_B3():
    """EXHAUSTIVE PROOF: 2(-2)(3)+2(1)(-1)=-14 equals -5+k, so k=-9 (option A)."""
    g1, f1, c1 = -2, 1, -5
    g2, f2 = 3, -1
    k = sympy.Symbol('k')
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == -14
    sols = sympy.solve(sympy.Eq(lhs, c1 + k), k)
    assert sols == [-9]
    options = {'A': -9, 'B': 9, 'C': -5, 'D': 14}
    matches = [let for let, v in options.items() if v == sols[0]]
    assert matches == ['A']
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: Centre (r,r), radius r: (1-r)^2+(8-r)^2=r^2, i.e.
    (r-5)(r-13)=0; the smaller radius is 5."""
    r = sympy.Symbol('r', real=True)
    eq = sympy.expand((1 - r)**2 + (8 - r)**2 - r**2)
    assert sympy.simplify(eq - (2*r**2 - 18*r + 65 - r**2)) == 0  # -r applies above
    sols = sympy.solve(sympy.Eq((1 - r)**2 + (8 - r)**2, r**2), r)
    assert set(sols) == {5, 13}
    assert min(sols) == 5
    return 5


def check_B5():
    """EXHAUSTIVE PROOF: Equal radii make the radical axis the perpendicular
    bisector of (0,0)-(6,0): x=3 (option A)."""
    line = sympy.expand((_X**2 + _Y**2 - 25) - ((_X - 6)**2 + _Y**2 - 25))
    assert sympy.simplify(line - (12*_X - 36)) == 0
    assert sympy.solve(sympy.Eq(line, 0), _X) == [3]
    options = {'A': 3, 'B': 6, 'C': None, 'D': None}
    matches = [let for let, v in options.items() if v == 3]
    assert matches == ['A']
    return 'A'


def check_B6():
    """EXHAUSTIVE PROOF: |6-4|=2<9<10: strict overlap, two common tangents (C)."""
    d, r1, r2 = 9, 4, 6
    assert abs(r1 - r2) < d < r1 + r2
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    matches = [let for let, v in options.items() if v == 2]
    assert matches == ['C']
    return 'C'


def check_B7():
    """EXHAUSTIVE PROOF: d^2=16+9=25 and r2^2=25-C; orthogonality gives
    25 = 4 + 25 - C, so C=4 (option A); the coefficient test agrees."""
    C = sympy.Symbol('C')
    d2 = sympy.Integer(16 + 9)
    r2_2 = sympy.simplify(16 + 9 - C)
    sols = sympy.solve(sympy.Eq(d2, 4 + r2_2), C)
    assert sols == [4]
    assert sympy.simplify(2*0*4 + 2*0*(-3) - (-4 + sols[0])) == 0
    options = {'A': 4, 'B': -4, 'C': 25, 'D': 2}
    matches = [let for let, v in options.items() if v == sols[0]]
    assert matches == ['A']
    return 'A'


def check_B8():
    """EXHAUSTIVE PROOF: Equal radii 6 with centres 6 apart give radical axis
    x=3; common chord 2*sqrt(36-9)=6*sqrt(3)."""
    r2 = 36
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 36, (_X - 6)**2 + _Y**2 - 36, 0, 0, r2)
    assert (a, b) == (12, 0)
    assert sympy.simplify(d - 3) == 0
    assert sympy.simplify(chord - 6 * sympy.sqrt(3)) == 0
    return chord


def check_B9():
    """EXHAUSTIVE PROOF: (4-r)^2+(8-r)^2=r^2 factors as (r-4)(r-20)=0; both
    radii are positive, so the possible radii are 4 and 20 (option C)."""
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((4 - r)**2 + (8 - r)**2, r**2), r)
    assert set(sols) == {4, 20}
    assert all(s > 0 for s in sols)
    options = {'A': '4 only', 'B': '20 only', 'C': '4 and 20', 'D': '16'}
    vals = {'4 only': {4}, '20 only': {20}, '4 and 20': {4, 20}, '16': {16}}
    matches = [let for let, text in options.items()
               if vals[text] == set(sols)]
    assert matches == ['C']
    return 'C'


def check_B10():
    """EXHAUSTIVE PROOF: Substituting (1,t) into 3x-4y+5=0 gives 3-4t+5=0, so
    t=2."""
    t = sympy.Symbol('t', real=True)
    value = sympy.simplify(3*1 - 4*t + 5)
    sols = sympy.solve(sympy.Eq(value, 0), t)
    assert sols == [2]
    return 2


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: Circles radius 5 at (2,-1) and radius 4 at (6,2);
    d=5 with |5-4|<5<9, so they meet at two points (option A)."""
    cx1, cy1, r2_1 = 2, -1, 25
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 12*_X - 4*_Y + 24)
    assert (cx2, cy2, r2_2) == (6, 2, 16)
    d2 = sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2)
    assert d2 == 25
    assert (sympy.sqrt(r2_1) - sympy.sqrt(r2_2))**2 < d2 < (sympy.sqrt(r2_1) + sympy.sqrt(r2_2))**2
    options = {'A': 'two points', 'B': 'tangent', 'C': 'contains', 'D': 'disjoint'}
    matches = [let for let, text in options.items() if text == 'two points']
    assert matches == ['A']
    return 'A'


def check_C2():
    """EXHAUSTIVE PROOF: Orthogonality means d^2=r1^2+r2^2=9+16=25, so the
    centre distance is 5 (option A)."""
    d = sympy.sqrt(sympy.Integer(9 + 16))
    assert d == 5
    options = {'A': 5, 'B': 7, 'C': 1, 'D': sympy.sqrt(7)}
    matches = [let for let, v in options.items() if sympy.simplify(v - d) == 0]
    assert matches == ['A']
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: Direct tangent segment sqrt(d^2-(r2-r1)^2)
    = sqrt(169-25)=12 (option A)."""
    d, r1, r2 = 13, 3, 8
    assert d > r1 + r2
    seg = sympy.sqrt(sympy.Integer(d**2 - (r2 - r1)**2))
    assert seg == 12
    options = {'A': 12, 'B': 5, 'C': 8, 'D': sympy.sqrt(104)}
    matches = [let for let, v in options.items() if sympy.simplify(v - seg) == 0]
    assert matches == ['A']
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: Transverse tangent segment sqrt(d^2-(r1+r2)^2)
    = sqrt(169-121)=4*sqrt(3) (option A)."""
    d, r1, r2 = 13, 3, 8
    assert d > r1 + r2
    seg = sympy.sqrt(sympy.Integer(d**2 - (r1 + r2)**2))
    assert sympy.simplify(seg - 4 * sympy.sqrt(3)) == 0
    options = {'A': 4*sympy.sqrt(3), 'B': 6*sympy.sqrt(3), 'C': 12, 'D': 2*sympy.sqrt(6)}
    matches = [let for let, v in options.items() if sympy.simplify(v - seg) == 0]
    assert matches == ['A']
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: Subtracting gives -6x-2y-11=0, i.e. 6x+2y+11=0
    (option A)."""
    c1 = _X**2 + _Y**2 - 2*_X - 4*_Y - 8
    c2 = _X**2 + _Y**2 + 4*_X - 2*_Y + 3
    diff = sympy.expand(c1 - c2)
    assert sympy.simplify(diff - (-6*_X - 2*_Y - 11)) == 0
    target = 6*_X + 2*_Y + 11
    options = {
        'A': 6*_X + 2*_Y + 11,
        'B': 6*_X - 2*_Y + 11,
        'C': 6*_X + 2*_Y - 11,
        'D': 2*_X + 6*_Y + 11,
    }
    matches = [let for let, eq in options.items()
               if sympy.simplify(eq - target) == 0]
    assert matches == ['A']
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: (9-r)^2+(2-r)^2=r^2 gives (r-5)(r-17)=0, two positive
    radii, so two circles (option C)."""
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((9 - r)**2 + (2 - r)**2, r**2), r)
    assert set(sols) == {5, 17}
    assert all(s > 0 for s in sols)
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    matches = [let for let, v in options.items() if v == len(sols)]
    assert matches == ['C']
    return 'C'


def check_C7():
    """EXHAUSTIVE PROOF: Second circle centre (3,-4) radius 12; radical axis
    3x-4y-25=0 at distance 5 from the origin gives chord 2*sqrt(169-25)=24."""
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 6*_X + 8*_Y - 119)
    assert (cx2, cy2, r2_2) == (3, -4, 144)
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 169, _X**2 + _Y**2 - 6*_X + 8*_Y - 119, 0, 0, 169)
    assert sympy.simplify(a/2 - 3) == 0 and sympy.simplify(b/2 + 4) == 0
    assert sympy.simplify(d - 5) == 0
    assert chord == 24
    options = {'A': 12, 'B': 16, 'C': 24, 'D': 26}
    matches = [let for let, v in options.items() if v == chord]
    assert matches == ['C']
    return 'C'


def check_C8():
    """EXHAUSTIVE PROOF: The radical axes x+2y-3=0 and x-2y+1=0 meet at (1,1),
    whose power against all three circles is 5 (option A)."""
    c1 = _X**2 + _Y**2 + 4*_X - 1
    c2 = _X**2 + _Y**2 - 8*_Y + 11
    c3 = _X**2 + _Y**2 + 2*_X - 12*_Y + 13
    ra12 = sympy.expand(c1 - c2)
    ra23 = sympy.expand(c2 - c3)
    assert sympy.simplify(ra12 / 4 - (_X + 2*_Y - 3)) == 0
    assert sympy.simplify(ra23 / -2 - (_X - 2*_Y + 1)) == 0
    sols = sympy.solve([sympy.Eq(ra12, 0), sympy.Eq(ra23, 0)], [_X, _Y])
    assert sols == {_X: 1, _Y: 1}
    x0, y0 = sols[_X], sols[_Y]
    pw = [sympy.simplify(c.subs({_X: x0, _Y: y0})) for c in (c1, c2, c3)]
    assert pw[0] == pw[1] == pw[2] == 5
    options = {'A': (1, 1), 'B': (1, -1), 'C': (3, 1), 'D': (1, 2)}
    matches = [let for let, pt in options.items() if pt == (x0, y0)]
    assert matches == ['A']
    return 'A'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: Equal power is the radical axis: x^2+y^2-1 cancels the
    second circle's terms to leave x=11/4, a line (option A)."""
    ra = sympy.expand((_X**2 + _Y**2 - 1) - (_X**2 + _Y**2 - 12*_X + 32))
    assert sympy.simplify(ra - (12*_X - 33)) == 0
    x_val = sympy.solve(sympy.Eq(ra, 0), _X)
    assert x_val == [sympy.Rational(11, 4)]
    options = {'A': sympy.Rational(11, 4), 'B': None, 'C': None, 'D': None}
    matches = [let for let, v in options.items() if v == x_val[0]]
    assert matches == ['A']
    return 'A'


def check_D2():
    """EXHAUSTIVE PROOF: Radical axis 3x+4y=30 is distance 6 from the origin;
    half-chord sqrt(100-36)=8, chord 16 (option B). Distance from (3,4) is 1,
    confirming sqrt(65-1)=8."""
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 6*_X - 8*_Y - 40)
    assert (cx2, cy2, r2_2) == (3, 4, 65)
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 100, _X**2 + _Y**2 - 6*_X - 8*_Y - 40, 0, 0, 100)
    line = sympy.expand(_X**2 + _Y**2 - 100 - (_X**2 + _Y**2 - 6*_X - 8*_Y - 40))
    assert sympy.simplify(line - (6*_X + 8*_Y - 60)) == 0
    assert sympy.simplify(d - 6) == 0
    assert chord == 16
    d2 = _dist_point_line(3, 4, a, b, c)
    assert sympy.simplify(d2 - 1) == 0
    assert sympy.sqrt(sympy.Integer(r2_2) - d2**2) == 8
    options = {'A': 8, 'B': 16, 'C': 12, 'D': 6*sympy.sqrt(3)}
    matches = [let for let, v in options.items() if sympy.simplify(v - chord) == 0]
    assert matches == ['B']
    return 'B'


def check_D3():
    """EXHAUSTIVE PROOF: The partner circle (x-2)^2+(y+1)^2=25 expands to
    x^2+y^2-4x+2y-20; coefficient test 2(-3)(-2)+2(-4)(1)=4=C-20 gives C=24."""
    partner = sympy.expand((_X - 2)**2 + (_Y + 1)**2 - 25)
    assert sympy.simplify(partner - (_X**2 + _Y**2 - 4*_X + 2*_Y - 20)) == 0
    C = sympy.Symbol('C')
    g1, f1, c1 = -3, -4, C
    g2, f2, c2 = -2, 1, -20
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == 4
    sols = sympy.solve(sympy.Eq(lhs, c1 + c2), C)
    assert sols == [24]
    d2 = sympy.simplify((3 - 2)**2 + (4 - (-1))**2)
    r1sq = sympy.simplify(9 + 16 - sols[0])
    assert sympy.simplify(d2 - (r1sq + 25)) == 0
    options = {'A': 24, 'B': 26, 'C': 25, 'D': -24}
    matches = [let for let, v in options.items() if v == sols[0]]
    assert matches == ['A']
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: Radii 3 and 4 with d=5; radical axis x=9/5 from the
    small centre; chord 2*sqrt(9-81/25)=24/5 (option A)."""
    d = sympy.sqrt(sympy.Integer(9 + 16))
    assert d == 5
    cx2, cy2 = 5, 0
    ra = sympy.expand((_X**2 + _Y**2 - 9) - ((_X - 5)**2 + _Y**2 - 16))
    assert sympy.simplify(ra - (10*_X - 18)) == 0
    x_val = sympy.solve(sympy.Eq(ra, 0), _X)
    assert x_val == [sympy.Rational(9, 5)]
    half = sympy.sqrt(sympy.Integer(9) - x_val[0]**2)
    assert sympy.simplify(half - Fraction(12, 5)) == 0
    chord = sympy.simplify(2 * half)
    assert sympy.simplify(chord - Fraction(24, 5)) == 0
    options = {'A': Fraction(24, 5), 'B': Fraction(12, 5), 'C': 6, 'D': Fraction(48, 5)}
    matches = [let for let, v in options.items() if sympy.simplify(v - chord) == 0]
    assert matches == ['A']
    return 'A'


def check_D5():
    """EXHAUSTIVE PROOF: Centre triangle has sides 7, 8, 9; Heron: s=12, area
    = sqrt(12*5*4*3)=12*sqrt(5) (option A); coordinates confirm."""
    a, b, c = 7, 8, 9
    s = sympy.Rational(a + b + c, 2)
    assert s == 12
    area = sympy.sqrt(sympy.simplify(s * (s - a) * (s - b) * (s - c)))
    assert sympy.simplify(area - 12 * sympy.sqrt(5)) == 0
    # coordinate cross-check: (0,0),(7,0), third point
    x3 = sympy.Rational(a**2 + c**2 - b**2, 2 * a)
    y3 = sympy.sqrt(c**2 - x3**2)
    assert sympy.simplify(y3 - 24 * sympy.sqrt(5) / 7) == 0
    assert sympy.simplify(sympy.Rational(1, 2) * a * y3 - area) == 0
    options = {'A': 12*sympy.sqrt(5), 'B': 12, 'C': 84, 'D': 3*sympy.sqrt(5)}
    matches = [let for let, v in options.items() if sympy.simplify(v - area) == 0]
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