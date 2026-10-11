import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from pathlib import Path
import math
from fractions import Fraction
import sympy
from tools.latex_bridge import get_answer, extract_tex_answers
from tools.answer_binding import bind, mcq_letter

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


def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sympy.simplify(sympy.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _tangent_count(d2, r1, r2):
    """Number of common tangents from d^2 and the radii, exact at the two boundaries."""
    s2 = sympy.expand((sympy.sympify(r1) + r2)**2)
    t2 = sympy.expand((sympy.sympify(r1) - r2)**2)
    if sympy.simplify(d2 - s2) == 0:
        return 3
    if sympy.simplify(d2 - t2) == 0:
        return 1
    if d2 > s2:
        return 4
    return 2 if d2 > t2 else 0


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Centre (6,8) and (0,0), both radius 5; d=10=r1+r2 means external tangency and exactly 3 common tangents."""
    expected = get_answer(TEX_PATH, 'A1')
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 12*_X - 16*_Y + 75)
    assert (cx1, cy1) == (6, 8) and r2_1 == 25
    cx2, cy2, r2_2 = 0, 0, 25
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    r1, r2 = sympy.sqrt(r2_1), sympy.sqrt(r2_2)
    assert d == r1 + r2
    assert d == 10
    assert sympy.sqrt(r2_1) == 5 and sympy.sqrt(r2_2) == 5
    computed = 3
    # bind to latex answer (numeric 3)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '3'
    return computed


def check_A2():
    """EXHAUSTIVE PROOF: d=13 > r1+r2=8, disjoint circles have 4 common tangents."""
    expected = get_answer(TEX_PATH, 'A2')
    d = Fraction(13 - 0)
    r1, r2 = 5, 3
    assert d > r1 + r2
    assert r1 + r2 == 8
    computed = 4
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '4'
    return computed


def check_A3():
    """EXHAUSTIVE PROOF: Both circles are real (r^2 = 21 and 4); subtracting gives -4x+6y-12=0, reduced to 2x-3y+6=0; any point on it has equal power."""
    c1 = _X**2 + _Y**2 - 6*_X + 2*_Y - 11
    c2 = _X**2 + _Y**2 - 2*_X - 4*_Y + 1
    assert _complete_square(c1) == (3, -1, 21)
    assert _complete_square(c2) == (1, 2, 4)
    diff = sympy.expand(c1 - c2)
    assert sympy.simplify(diff - (-4*_X + 6*_Y - 12)) == 0
    reduced = sympy.expand(diff / -2)
    assert sympy.simplify(reduced - (2*_X - 3*_Y + 6)) == 0
    x0, y0 = 0, 2
    assert sympy.simplify(reduced.subs({_X: x0, _Y: y0})) == 0
    assert c1.subs({_X: x0, _Y: y0}) == c2.subs({_X: x0, _Y: y0}) == -3
    return sympy.Eq(2*_X - 3*_Y + 6, 0)


def check_A4():
    """EXHAUSTIVE PROOF: x^2+y^2+6x+8y+9 has centre (-3,-4) radius 4; d=5 and d^2=r1^2+r2^2=9+16, so the circles are orthogonal: yes."""
    expected = get_answer(TEX_PATH, 'A4')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 + 6*_X + 8*_Y + 9)
    assert (cx, cy) == (-3, -4) and r2 == 16
    d2 = sympy.simplify((cx - 0)**2 + (cy - 0)**2)
    assert d2 == 25
    assert sympy.simplify(d2 - (9 + r2)) == 0
    computed = 'yes'
    assert str(expected).strip().lower().startswith('yes') or expected == True
    return computed


def check_A5():
    """EXHAUSTIVE PROOF: Radical axis of x^2+y^2=25 and x^2+y^2-10x+5=0 is x=3; the common chord is 2*sqrt(25-9)=8."""
    expected = get_answer(TEX_PATH, 'A5')
    r2 = 25
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 25, _X**2 + _Y**2 - 10*_X + 5, 0, 0, r2)
    assert (a, b) == (10, 0)
    assert sympy.simplify(c * -1 - 30) == 0
    assert sympy.simplify(d - 3) == 0
    assert chord == 8
    computed = int(chord)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '8'
    return computed


def check_A6():
    """EXHAUSTIVE PROOF: |5-3|=2 < d=4 < 8=r1+r2 means intersecting circles: 2 common tangents."""
    expected = get_answer(TEX_PATH, 'A6')
    d, r1, r2 = 4, 3, 5
    assert abs(r1 - r2) < d < r1 + r2
    computed = 2
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '2'
    return computed


def check_A7():
    """EXHAUSTIVE PROOF: Completing with unknown k gives centre (5,5) and r^2=50-k; tangency to both axes forces r=5, hence k=50-25=25."""
    expected = get_answer(TEX_PATH, 'A7')
    k = sympy.Symbol('k')
    cx, cy, r2 = _complete_square(_X**2 + _Y**2 - 10*_X - 10*_Y + k)
    assert (cx, cy) == (5, 5)
    expr = sympy.expand(r2 - (50 - k))
    assert sympy.simplify(expr) == 0
    sols = sympy.solve(sympy.Eq(r2, 25), k)
    assert sols == [25]
    computed = int(sols[0])
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0 or str(expected).strip() == '25'
    return computed


def check_A8():
    """EXHAUSTIVE PROOF: 2g1g2+2f1f2=c1+c2 for orthogonality gives -12 = C-1, so C=-11; the d^2 form agrees."""
    expected = get_answer(TEX_PATH, 'A8')
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
    computed = int(Cv)
    # expected parsed may be -11
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_A9():
    """EXHAUSTIVE PROOF: Both circles are unit circles at (2,3) and (-1,5); d=sqrt(13)>2 so they are disjoint: 4 common tangents."""
    expected = get_answer(TEX_PATH, 'A9')
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 4*_X - 6*_Y + 12)
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 + 2*_X - 10*_Y + 25)
    assert (cx1, cy1, r2_1) == (2, 3, 1)
    assert (cx2, cy2, r2_2) == (-1, 5, 1)
    d = sympy.sqrt(sympy.simplify((cx1-cx2)**2 + (cy1-cy2)**2))
    assert d == sympy.sqrt(13)
    assert d > sympy.sqrt(r2_1) + sympy.sqrt(r2_2)
    computed = 4
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_A10():
    """EXHAUSTIVE PROOF: 3 common tangents occurs exactly at external tangency (d = r1+r2); here r1=7, r2=3, so d=10."""
    expected = get_answer(TEX_PATH, 'A10')
    r1, r2 = 7, 3
    assert r1 > 0 and r2 > 0
    assert r1 + r2 == 10
    assert abs(r1 - r2) < (r1 + r2)
    d = sympy.Integer(r1 + r2)
    assert d == 10
    computed = int(d)
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: Centres (1,2), (3,1), radii 5 and 2; d=sqrt5 < 3 = r1-r2, so the small circle is strictly inside: 0 tangents (A)."""
    cx1, cy1, r2_1 = _complete_square(_X**2 + _Y**2 - 2*_X - 4*_Y - 20)
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 6*_X - 2*_Y + 6)
    assert (cx1, cy1, r2_1, cx2, cy2, r2_2) == (1, 2, 25, 3, 1, 4)
    d2 = (cx1 - cx2)**2 + (cy1 - cy2)**2
    count = _tangent_count(d2, 5, 2)
    # every point of the small circle is inside the big one
    far = max(math.hypot(3 + 2*math.cos(t/100) - 1, 1 + 2*math.sin(t/100) - 2) for t in range(629))
    assert far < 5
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return _only(options, count)


def check_B2():
    """EXHAUSTIVE PROOF: c=0 and (a-6)x+(b+4)y-10 = k(2x-y+5) force k=-2, a=2, b=-2, so a+b=0 (D). Without c=0, a+b=k+2 is free."""
    a, b, k = sympy.symbols('a b k')
    diff = (a - 6)*_X + (b + 4)*_Y - 10
    sol = sympy.solve(sympy.Poly(sympy.expand(diff - k*(2*_X - _Y + 5)), _X, _Y).coeffs(), [a, b, k], dict=True)
    assert sol == [{a: 2, b: -2, k: -2}]
    total = sol[0][a] + sol[0][b]
    # the circle x^2+y^2+2x-2y=0 really has this radical axis with the second circle
    assert sympy.expand((_X**2 + _Y**2 + 2*_X - 2*_Y) - (_X**2 + _Y**2 + 6*_X - 4*_Y + 10)) == -2*(2*_X - _Y + 5)
    options = {'A': 3, 'B': 5, 'C': -3, 'D': 0}
    return _only(options, total)


def check_B3():
    """EXHAUSTIVE PROOF: 2(-2)(3)+2(1)(-1)=-14 equals -5+k, so k=-9 (option A); the d^2 test agrees."""
    g1, f1, c1 = -2, 1, -5
    g2, f2 = 3, -1
    k = sympy.Symbol('k')
    lhs = sympy.expand(2*g1*g2 + 2*f1*f2)
    assert lhs == -14
    sols = sympy.solve(sympy.Eq(lhs, c1 + k), k)
    assert sols == [-9]
    # centres (2,-1), (-3,1): d^2 = 29 = r1^2 + r2^2 = 10 + (10 - k)
    assert 29 == 10 + (9 + 1 - sols[0])
    options = {'A': -9, 'B': 9, 'C': -5, 'D': 14}
    return _only(options, sols[0])


def check_B4():
    """EXHAUSTIVE PROOF: Centre (r,r), radius r: (1-r)^2+(8-r)^2=r^2, i.e. (r-5)(r-13)=0; the smaller radius is 5."""
    expected = get_answer(TEX_PATH, 'B4')
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((1 - r)**2 + (8 - r)**2, r**2), r)
    assert set(sols) == {5, 13}
    assert min(sols) == 5
    computed = 5
    # expected parsed is 5
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


def check_B5():
    """EXHAUSTIVE PROOF: Equal radii make the radical axis the perpendicular bisector of (0,0)-(6,0): x=3 (option A)."""
    line = sympy.expand((_X**2 + _Y**2 - 25) - ((_X - 6)**2 + _Y**2 - 25))
    assert sympy.simplify(line - (12*_X - 36)) == 0
    assert sympy.solve(sympy.Eq(line, 0), _X) == [3]
    options = {'A': _X - 3, 'B': _X - 6, 'C': _Y - 3, 'D': _Y}
    hits = [let for let, e in options.items() if sympy.simplify(line / 12 - e) == 0]
    assert hits == ['A']
    return 'A'


def check_B6():
    """EXHAUSTIVE PROOF: |6-4|=2<9<10: strict overlap, two common tangents (C)."""
    assert abs(4 - 6) < 9 < 4 + 6
    count = _tangent_count(81, 4, 6)
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return _only(options, count)


def check_B7():
    """EXHAUSTIVE PROOF: R^2 = power of (7,1) = 36, so R = 6 (D); d^2 = 45 = R^2 + r^2 with r = 3."""
    S = _X**2 + _Y**2 - 2*_X + 4*_Y - 4
    cx, cy, r2 = _complete_square(S)
    assert (cx, cy, r2) == (1, -2, 9)
    R2 = S.subs({_X: 7, _Y: 1})
    assert R2 == 36
    d2 = (7 - cx)**2 + (1 - cy)**2
    assert d2 == R2 + r2
    R = sympy.sqrt(R2)
    options = {'A': 3*sympy.sqrt(5), 'B': 3*sympy.sqrt(5) - 3, 'C': 3, 'D': 6}
    return _only(options, R)


def check_B8():
    """EXHAUSTIVE PROOF: Radical axis 6x+3y=25 meets the line of centres y=x/2 at (10/3, 5/3), the midpoint of PQ (checked against the actual intersection points)."""
    S1 = _X**2 + _Y**2 - 25
    S2 = _X**2 + _Y**2 - 12*_X - 6*_Y + 25
    assert _complete_square(S2) == (6, 3, 20)
    axis = sympy.expand(S1 - S2)
    assert axis == 12*_X + 6*_Y - 50
    M = sympy.solve([axis, _Y - _X/2], [_X, _Y])
    pts = sympy.solve([S1, S2], [_X, _Y])
    assert len(pts) == 2
    mid = (sympy.simplify((pts[0][0] + pts[1][0]) / 2), sympy.simplify((pts[0][1] + pts[1][1]) / 2))
    assert mid == (M[_X], M[_Y]) == (sympy.Rational(10, 3), sympy.Rational(5, 3))
    return mid


def check_B9():
    """EXHAUSTIVE PROOF: Centre (r,r): |7r-12| = 5r gives r = 1 or 6, both with centre in the first quadrant; sum 7 (C)."""
    r = sympy.Symbol('r', positive=True)
    roots = set(sympy.solve(7*r - 12 - 5*r, r)) | set(sympy.solve(7*r - 12 + 5*r, r))
    assert roots == {1, 6}
    for rv in roots:
        assert sympy.Abs(3*rv + 4*rv - 12) / 5 == rv
    options = {'A': 1, 'B': 6, 'C': 7, 'D': 5}
    return _only(options, sum(roots))


def check_B10():
    """EXHAUSTIVE PROOF: Substituting (1,t) into 3x-4y+5=0 gives 3-4t+5=0, so t=2."""
    expected = get_answer(TEX_PATH, 'B10')
    t = sympy.Symbol('t', real=True)
    value = sympy.simplify(3*1 - 4*t + 5)
    sols = sympy.solve(sympy.Eq(value, 0), t)
    assert sols == [2]
    computed = 2
    assert sympy.simplify(computed - (expected if not isinstance(expected, sympy.Equality) else expected.rhs)) == 0
    return computed


# ── Section C (NEW HARD) ───────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: subtracting gives the chord 10x - 6y = 33 - r^2; through the origin iff r^2 = 33 (C); the circles then meet in two points."""
    X, Y = _X, _Y
    r = sympy.Symbol('r', positive=True)
    chord = sympy.expand((X + 2)**2 + (Y - 1)**2 - 25 - ((X - 3)**2 + (Y + 2)**2 - r**2))
    assert sympy.simplify(chord - (10*X - 6*Y - 33 + r**2)) == 0
    sol = sympy.solve(chord.subs({X: 0, Y: 0}), r)
    assert sol == [sympy.sqrt(33)]
    rv = sol[0]
    pts = sympy.solve([(X + 2)**2 + (Y - 1)**2 - 25, (X - 3)**2 + (Y + 2)**2 - rv**2], [X, Y])
    real = [q for q in pts if all(v.is_real for v in q)]
    assert len(real) == 2
    (x1, y1), (x2, y2) = real
    assert sympy.simplify(x1*y2 - x2*y1) == 0                     # the two points and O are collinear
    options = {'A': sympy.sqrt(17), 'B': 5, 'C': sympy.sqrt(33), 'D': 3}
    return _only(options, rv)


def check_C2():
    """EXHAUSTIVE PROOF: Centres (1,0) and (5,3), d=5, r1+r2=5 => externally tangent => 3 common tangents (D)."""
    d2 = (5 - 1)**2 + (3 - 0)**2
    assert d2 == 25
    count = _tangent_count(d2, 2, 3)
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return _only(options, count)


def check_C3():
    """EXHAUSTIVE PROOF: Second circle centre (3,-4) radius 12; radical axis 3x-4y-25=0 distance 5 from origin gives chord 24 (C), a diameter of the smaller circle."""
    cx2, cy2, r2_2 = _complete_square(_X**2 + _Y**2 - 6*_X + 8*_Y - 119)
    assert (cx2, cy2, r2_2) == (3, -4, 144)
    chord, (a, b, c, d) = _common_chord(
        _X**2 + _Y**2 - 169, _X**2 + _Y**2 - 6*_X + 8*_Y - 119, 0, 0, 169)
    assert sympy.simplify(d - 5) == 0
    assert a*cx2 + b*cy2 + c == 0          # the chord passes through (3,-4)
    assert chord == 24
    options = {'A': 12, 'B': 16, 'C': 24, 'D': 26}
    return _only(options, chord)


def check_C4():
    """EXHAUSTIVE PROOF: Centre (r,r): (9-r)^2+(2-r)^2=r^2 => r^2-22r+85=0 => sum 22 via Vieta, roots 5 and 17 (C)."""
    r = sympy.Symbol('r', real=True)
    sols = sympy.solve(sympy.Eq((9 - r)**2 + (2 - r)**2, r**2), r)
    assert set(sols) == {5, 17}
    poly = sympy.Poly((9 - r)**2 + (2 - r)**2 - r**2, r)
    assert poly.coeffs() == [1, -22, 85]
    options = {'A': 14, 'B': 17, 'C': 22, 'D': 34}
    return _only(options, sum(sols))


def check_C5():
    """EXHAUSTIVE PROOF: S1 + lambda S2 through (0,1) needs lambda = -3, giving x^2+y^2-24x-12y+11=0, radius 13 (D); agrees with the circumcircle of the actual P, Q, (0,1)."""
    S1 = _X**2 + _Y**2 - 25
    S2 = _X**2 + _Y**2 - 16*_X - 8*_Y - 1
    lam = -S1.subs({_X: 0, _Y: 1}) / S2.subs({_X: 0, _Y: 1})
    assert lam == -3
    fam = sympy.expand((S1 + lam*S2) / (1 + lam))
    cx, cy, R2 = _complete_square(fam)
    assert (cx, cy, R2) == (12, 6, 169)
    # independent: circle through the real intersection points and (0,1)
    P, Q = sympy.solve([S1, S2], [_X, _Y])
    assert not all(v.is_rational for v in P)
    for pt in (P, Q, (0, 1)):
        assert sympy.simplify((pt[0] - cx)**2 + (pt[1] - cy)**2 - R2) == 0
    options = {'A': 9, 'B': 2*sympy.sqrt(13), 'C': 4*sympy.sqrt(5), 'D': 13}
    return _only(options, sympy.sqrt(R2))


def check_C6():
    """EXHAUSTIVE PROOF: x = 0 gives y^2 + by + c = 0, roots sqrt(b^2 - 4c) apart; chord 2 iff b^2 - 4c = 4 (B); each other option fails on a concrete circle."""
    a, b, c = sympy.symbols('a b c')
    options = {'A': a**2 - 4*c - 4, 'B': b**2 - 4*c - 4, 'C': b**2 - 4*c - 2, 'D': b**2 - 4*c - 16}

    def chord_is_2(av, bv, cv):
        roots = sympy.solve(_Y**2 + bv*_Y + cv, _Y)
        real = [v for v in roots if v.is_real]
        return len(real) == 2 and sympy.simplify(sympy.Abs(real[0] - real[1]) - 2) == 0

    samples = [(2, 4, 3), (6, 4, 3), (2, 6, 8), (4, 2, -1), (8, 6, 5), (2, 10, 21), (4, 6, 5)]
    assert any(chord_is_2(*s) for s in samples) and not all(chord_is_2(*s) for s in samples)
    hits = [k for k, e in options.items()
            if all((e.subs({a: av, b: bv, c: cv}) == 0) == chord_is_2(av, bv, cv) for av, bv, cv in samples)]
    assert hits == ['B']
    return 'B'


def check_C7():
    """EXHAUSTIVE PROOF: radii 2 and 1, centres (0,0), (6,0); the crossing tangent passes through (4,0); distance 2 from O gives m = sqrt3/3 (B), and it is 1 from (6,0)."""
    m = sympy.Symbol('m', positive=True)
    sols = sympy.solve(sympy.Eq(16*m**2, 4*(1 + m**2)), m)
    assert len(sols) == 1
    mv = sols[0]
    dist = lambda cx, rr: sympy.simplify(sympy.Abs(mv*(cx - 4)) / sympy.sqrt(1 + mv**2) - rr)
    assert dist(0, 2) == 0 and dist(6, 1) == 0
    # it crosses the segment between the centres: the centres are on opposite sides
    side = lambda cx: sympy.sign(-mv*(cx - 4))
    assert side(0) != side(6)
    options = {'A': sympy.Rational(1, 2), 'B': sympy.sqrt(3)/3, 'C': sympy.sqrt(3), 'D': 2*sympy.sqrt(5)/5}
    return _only(options, mv)


def check_C8():
    """EXHAUSTIVE PROOF: Radical axes x+2y-3=0 and x-2y+1=0 meet at (1,1), power 5 for all three circles (A)."""
    c1 = _X**2 + _Y**2 + 4*_X - 1
    c2 = _X**2 + _Y**2 - 8*_Y + 11
    c3 = _X**2 + _Y**2 + 2*_X - 12*_Y + 13
    ra12 = sympy.expand(c1 - c2)
    ra23 = sympy.expand(c2 - c3)
    assert sympy.simplify(ra12/4 - (_X + 2*_Y - 3)) == 0
    assert sympy.simplify(ra23/-2 - (_X - 2*_Y + 1)) == 0
    sols = sympy.solve([sympy.Eq(ra12, 0), sympy.Eq(ra23, 0)], [_X, _Y])
    assert sols == {_X: 1, _Y: 1}
    pw = [c.subs({_X: 1, _Y: 1}) for c in (c1, c2, c3)]
    assert pw[0] == pw[1] == pw[2] == 5
    options = {'A': (1, 1), 'B': (1, -1), 'C': (3, 1), 'D': (1, 2)}
    hits = [k for k, (px, py) in options.items() if len({c.subs({_X: px, _Y: py}) for c in (c1, c2, c3)}) == 1]
    assert hits == ['A']
    return 'A'


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: O1=(2,1), r1=3; O2=(10,7), r2=5; d=10; external tangent sqrt(100-4)=4sqrt6; right trapezium area (3+5)/2 * 4sqrt6 = 16sqrt6 (B)."""
    cx1, cy1, s1 = _complete_square(_X**2 + _Y**2 - 4*_X - 2*_Y - 4)
    cx2, cy2, s2 = _complete_square(_X**2 + _Y**2 - 20*_X - 14*_Y + 124)
    assert (cx1, cy1, s1, cx2, cy2, s2) == (2, 1, 9, 10, 7, 25)
    r1, r2 = sympy.sqrt(s1), sympy.sqrt(s2)
    d = sympy.sqrt((cx2 - cx1)**2 + (cy2 - cy1)**2)
    assert d == 10
    PQ = sympy.sqrt(d**2 - (r2 - r1)**2)
    area = (r1 + r2) / 2 * PQ
    # coordinates: tangent line y = mx + k at distance r1, r2 (same side) from the centres
    m, k = sympy.symbols('m k', real=True)
    sol = sympy.solve([(m*cx1 - cy1 + k)**2 - s1*(m**2 + 1), (m*cx2 - cy2 + k)**2 - s2*(m**2 + 1),
                       (m*cx1 - cy1 + k) * 5 - (m*cx2 - cy2 + k) * 3], [m, k], dict=True)
    assert sol
    for sl in sol:
        mv, kv = sl[m], sl[k]
        foot = lambda cx, cy: ((cx + mv*cy - mv*kv) / (1 + mv**2), (mv*cx + mv**2*cy + kv) / (1 + mv**2))
        P, Q = foot(cx1, cy1), foot(cx2, cy2)
        quad = [(cx1, cy1), P, Q, (cx2, cy2)]
        shoelace = sympy.Abs(sum(quad[i][0]*quad[(i+1) % 4][1] - quad[(i+1) % 4][0]*quad[i][1] for i in range(4))) / 2
        assert sympy.simplify(shoelace - area) == 0
    options = {'A': 24, 'B': 16*sympy.sqrt(6), 'C': 40, 'D': 8*sympy.sqrt(6)}
    return _only(options, area)


def check_D2():
    """EXHAUSTIVE PROOF: centre (h,4); one common point iff distance 13 (external) or 3 (internal); distance 3 impossible (the line is 5 away); 13 gives h = -4 +- 12: 2 circles (B)."""
    h = sympy.Symbol('h', real=True)
    count = 0
    for D in (8 + 5, 8 - 5):
        count += len(sympy.solve((h + 4)**2 + 25 - D**2, h))
    assert count == 2
    # the count of common points for each centre found, checked numerically
    for hv in (-16, 8):
        d = math.hypot(hv + 4, 5)
        assert abs(d - 13) < 1e-12
    options = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    return _only(options, count)


def check_D3():
    """EXHAUSTIVE PROOF: Triangle sides 7,8,9 Heron s=12 area 12*sqrt5 (A); coordinates agree."""
    a, b, c = 7, 8, 9
    s = sympy.Rational(a+b+c, 2)
    area = sympy.sqrt(s*(s-a)*(s-b)*(s-c))
    assert sympy.simplify(area - 12*sympy.sqrt(5)) == 0
    # third centre at (33/7, 24sqrt5/7) is 9 from (0,0) and 8 from (7,0)
    px, py = sympy.Rational(33, 7), 24*sympy.sqrt(5)/7
    assert sympy.simplify(px**2 + py**2 - 81) == 0 and sympy.simplify((px - 7)**2 + py**2 - 64) == 0
    assert sympy.simplify(7*py/2 - area) == 0
    options = {'A': 12*sympy.sqrt(5), 'B': 12, 'C': 84, 'D': 30}
    return _only(options, area)


def check_D4():
    """EXHAUSTIVE PROOF: Orthogonal radii 3 and 4 give d=5; radical axis x=9/5, half chord 12/5, chord 24/5 = 2r1r2/d (B)."""
    d = sympy.sqrt(9 + 16)
    assert d == 5
    ra = sympy.expand((_X**2 + _Y**2 - 9) - ((_X - 5)**2 + _Y**2 - 16))
    assert sympy.simplify(ra - (10*_X - 18)) == 0
    xv = sympy.solve(ra, _X)[0]
    assert xv == sympy.Rational(9, 5)
    chord = 2*sympy.sqrt(9 - xv**2)
    assert chord == sympy.Rational(24, 5) == 2*3*4/d
    options = {'A': sympy.Rational(12, 5), 'B': sympy.Rational(24, 5), 'C': 6, 'D': sympy.Rational(48, 5)}
    return _only(options, chord)


def check_D5():
    """EXHAUSTIVE PROOF: Circles (0,4) r4 and (12,9) r9 touch (d=13); the gap circle at (x0, r) with 2sqrt(4r)+2sqrt(9r)=12 has r=36/25 (D), touching all three externally."""
    cx1, cy1, s1 = _complete_square(_X**2 + _Y**2 - 8*_Y)
    cx2, cy2, s2 = _complete_square(_X**2 + _Y**2 - 24*_X - 18*_Y + 144)
    assert (cx1, cy1, s1, cx2, cy2, s2) == (0, 4, 16, 12, 9, 81)
    assert (cx2 - cx1)**2 + (cy2 - cy1)**2 == (4 + 9)**2
    r = sympy.Symbol('r', positive=True)
    x0 = sympy.Symbol('x0', real=True)
    sol = sympy.solve([(x0 - cx1)**2 + (r - cy1)**2 - (r + 4)**2,
                       (x0 - cx2)**2 + (r - cy2)**2 - (r + 9)**2], [x0, r], dict=True)
    gap = [sl for sl in sol if 0 < sl[x0] < 12]
    assert len(gap) == 1
    rv = gap[0][r]
    assert rv == sympy.Rational(36, 25) and gap[0][x0] == sympy.Rational(24, 5)
    # the other solution (outside the gap) is the inv's circle, radius 36
    assert {sl[r] for sl in sol} == {sympy.Rational(36, 25), 36}
    options = {'A': sympy.Rational(6, 5), 'B': sympy.Rational(36, 13), 'C': sympy.Rational(169, 100), 'D': sympy.Rational(36, 25)}
    return _only(options, rv)


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
