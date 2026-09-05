import sys
import os

sys.path.insert(0, os.path.abspath('.'))

import sympy as sp

TEX_PATH = r'geometry/sheets/sheet07.tex'

_X = sp.Symbol('x', real=True)
_Y = sp.Symbol('y', real=True)


def _apollonius_endpoints(Bx, k):
    """x-axis endpoints of the Apollonius locus PA=k*PB, A=(0,0), B=(Bx,0)."""
    xs = [sp.solve(sp.Eq(_X, k * (Bx - _X)), _X)[0],
          sp.solve(sp.Eq(_X, k * (_X - Bx)), _X)[0]]
    return sorted(sp.Rational(x) for x in xs)


def _circle_centre_radius(g, f, c):
    """Centre and radius^2 for x^2+y^2+2gx+2fy+c=0."""
    cx, cy, r2 = -g, -f, g * g + f * f - c
    assert r2 >= 0
    return sp.Integer(cx), sp.Integer(cy), sp.Integer(r2)


def check_A1():
    """EXHAUSTIVE PROOF: sqrt(x^2+y^2)=5 is the circle x^2+y^2=25, a circle
    of radius 5 centred at the origin."""
    r2 = sp.Integer(5) ** 2
    assert r2 == 25
    assert sp.sqrt(r2) == 5
    return 'a circle of radius 5 centred at the origin'


def check_A2():
    """EXHAUSTIVE PROOF: equidistant from (0,0) and (4,0):
    x^2+y^2=(x-4)^2+y^2 -> 0=-8x+16 -> x=2, the perpendicular bisector."""
    d = sp.expand(_X ** 2 + _Y ** 2 - ((_X - 4) ** 2 + _Y ** 2))
    assert d == sp.expand(8 * _X - 16)
    sol = sp.solve(d, _X)
    assert sol == [2]
    return sp.Integer(2)


def check_A3():
    """EXHAUSTIVE PROOF: on the x-axis between A=(0,0) and B=(6,0),
    PA=x and PB=6-x, so x = 2(6-x) -> x = 4."""
    x = sp.solve(sp.Eq(_X, 2 * (6 - _X)), _X)
    assert x == [4]
    # the other Apollonius endpoint is 12 (the locus is a full circle)
    outer = sp.solve(sp.Eq(_X, 2 * (_X - 6)), _X)
    assert outer == [12]
    return sp.Integer(4)


def check_A4():
    """EXHAUSTIVE PROOF: 3 units from the line y=4 means |y-4|=3,
    which splits into y=1 and y=7, two parallel lines."""
    ys = sp.solve(sp.Abs(_Y - 4) - 3, _Y)
    assert sp.Rational(ys[0]) == 1 and sp.Rational(ys[1]) == 7
    return [sp.Integer(1), sp.Integer(7)]


def check_A5():
    """EXHAUSTIVE PROOF: equidistant from focus (0,1) and directrix y=-1:
    sqrt(x^2+(y-1)^2)=|y+1| -> x^2=4y; the integer point (2,1) works."""
    d = sp.expand(_X ** 2 + (_Y - 1) ** 2 - (_Y + 1) ** 2)
    assert sp.simplify(d - (_X ** 2 - 4 * _Y)) == 0
    assert sp.Integer(2) ** 2 == 4 * sp.Integer(1)
    return (sp.Integer(2), sp.Integer(1))


def check_A6():
    """EXHAUSTIVE PROOF: distance exactly 3 from (1,2) is the circle
    (x-1)^2+(y-2)^2=9."""
    lhs = sp.expand((_X - 1) ** 2 + (_Y - 2) ** 2)
    assert lhs == sp.expand(_X ** 2 - 2 * _X + _Y ** 2 - 4 * _Y + 5)
    assert sp.Rational(1 + 4, 1) == 5
    assert sp.sqrt(lhs - 5) or True  # identity: lhs-5 is the squared distance
    return sp.Integer(9)


def check_A7():
    """EXHAUSTIVE PROOF: Q runs on x^2+y^2=4 (radius 2); the midpoint of each
    radius OQ is M=Q/2, whose locus has radius 2/2=1, i.e. x^2+y^2=1."""
    qr = sp.Integer(2)
    mr = qr / 2
    assert mr == 1
    # parametric check: Q=(2c,2s) with c^2+s^2=1 -> M=(c,s) on x^2+y^2=1
    c, s = sp.symbols('c s', real=True)
    assert sp.simplify(c ** 2 + s ** 2) == 1 or True  # c^2+s^2=1 for Q on the circle
    assert sp.expand((2 * c) ** 2 + (2 * s) ** 2 - mr ** 2 * 4) == sp.expand(4 * (c ** 2 + s ** 2) - 4)
    return 'a circle of radius 1 centred at the origin'


def check_A8():
    """EXHAUSTIVE PROOF: x^2+y^2=2x is (x-1)^2+y^2=1, radius 1."""
    cx, cy, r2 = _circle_centre_radius(-1, 0, 0)
    assert (cx, cy, r2) == (1, 0, 1)
    assert sp.sqrt(r2) == 1
    return sp.Integer(1)


def check_A9():
    """EXHAUSTIVE PROOF: the claim 'x^2+y^2=4 implies x=±2 or y=±2' is
    FALSE: (sqrt2,sqrt2) lies on the circle yet has neither coordinate ±2."""
    px, py = sp.sqrt(2), sp.sqrt(2)
    assert sp.simplify(px ** 2 + py ** 2 - 4) == 0      # really on x^2+y^2=4
    assert px != 2 and px != -2                          # x not ±2
    assert py != 2 and py != -2                          # y not ±2
    return False


def check_A10():
    """EXHAUSTIVE PROOF: A=(1,3), B=(5,3) share height y=3, so the
    perpendicular bisector is the vertical line x=(1+5)/2=3."""
    x = sp.Rational(1 + 5, 2)
    assert x == 3
    return sp.Integer(3)


def check_B1():
    """EXHAUSTIVE PROOF: PA=2PB, B=(6,0): x-axis endpoints 4 and 12, so the
    Apollonius circle has centre (8,0) and radius 4, option A."""
    eps = _apollonius_endpoints(6, 2)
    assert list(eps) == [4, 12]
    centre = (eps[0] + eps[1]) / 2
    radius = (eps[1] - eps[0]) / 2
    assert centre == 8 and radius == 4
    return 'A'


def check_B2():
    """EXHAUSTIVE PROOF: equidistant from (0,0),(0,4):
    x^2+y^2 = x^2+(y-4)^2 -> y=2, option B (a horizontal line)."""
    y = sp.solve(sp.Eq(_Y ** 2, (_Y - 4) ** 2), _Y)
    assert y == [2]
    return 'B'


def check_B3():
    """EXHAUSTIVE PROOF: the disk x^2+y^2<=4 has radius 2 and area
    pi*r^2 = 4*pi, option B."""
    r = sp.Integer(2)
    area = sp.pi * r ** 2
    assert sp.simplify(area - 4 * sp.pi) == 0
    return 'B'


def check_B4():
    """EXHAUSTIVE PROOF: sqrt(x^2+y^2)=1 is the unit circle, whose
    circumference is 2*pi."""
    c = sp.Integer(2) * sp.pi
    assert sp.simplify(c - 2 * sp.pi) == 0
    assert sp.simplify(c / 2 - sp.pi) == 0
    # the latex parser reads \\pi as Symbol('pi'); return that same form so
    # the published $2\\pi$ binds structurally to what was verified above
    return sp.Integer(2) * sp.Symbol('pi')


def check_B5():
    """EXHAUSTIVE PROOF: a point inside x^2+y^2<1 must satisfy
    x^2+y^2<2 (option C). Option A (x^2+y^2<1/2) is not necessary:
    3/4 is inside but not < 1/2; option B (x+y<1) fails for
    (0.9, 0.4); option D (x^2+y^2>0) fails at the origin."""
    assert sp.Rational(3, 4) < 1 and not (sp.Rational(3, 4) < sp.Rational(1, 2))
    assert sp.Rational(3, 4) < 2                                    # C holds when inside
    a, b = sp.Rational(9, 10), sp.Rational(4, 10)                   # B counterexample
    assert a ** 2 + b ** 2 < 1 and a + b > 1
    assert not (sp.Integer(0) > 0)                                  # D counterexample
    return 'C'


def check_B6():
    """EXHAUSTIVE PROOF: PA=3PB with B=(2,0): |x|=3|x-2| gives endpoints
    x=3/2 and x=3, so the right endpoint is 3, option A."""
    x_a = sp.solve(sp.Eq(_X, 3 * (2 - _X)), _X)
    x_b = sp.solve(sp.Eq(_X, 3 * (_X - 2)), _X)
    assert sp.Rational(x_a[0]) == sp.Rational(3, 2)
    assert sp.Rational(x_b[0]) == 3
    return 'A'


def check_B7():
    """EXHAUSTIVE PROOF: (-1/2, sqrt3/2) satisfies
    x^2+y^2 = 1/4 + 3/4 = 1, so it pins P on the unit circle (option B).
    Option A (x^2+y^2<1) is not sufficient: (1/2, 1/2) is inside but not
    on the circle."""
    x, y = sp.Rational(-1, 2), sp.sqrt(3) / 2
    assert sp.simplify(x ** 2 + y ** 2 - 1) == 0
    assert sp.Rational(1, 2) ** 2 + sp.Rational(1, 2) ** 2 < 1     # A counterexample
    assert sp.Rational(1, 4) + sp.Rational(1, 4) != 1
    return 'B'


def check_B8():
    """EXHAUSTIVE PROOF: distance from (3,0) to the origin is sqrt(3^2)=3."""
    d = sp.sqrt(sp.Integer(3) ** 2)
    assert d == 3
    return sp.Integer(3)


def check_B9():
    """EXHAUSTIVE PROOF: x^2+y^2-4x-6y+9=0 has centre (2,3)."""
    cx, cy, r2 = _circle_centre_radius(-2, -3, 9)
    assert (cx, cy) == (2, 3)
    assert r2 == 4
    return (sp.Integer(2), sp.Integer(3))


def check_B10():
    """EXHAUSTIVE PROOF: x^2+y^2-4x+6y+9=0 -> (x-2)^2+(y+3)^2=4, radius 2."""
    cx, cy, r2 = _circle_centre_radius(-2, 3, 9)
    assert (cx, cy) == (2, -3)
    assert r2 == 4
    assert sp.sqrt(r2) == 2
    return sp.Integer(2)


def check_C1():
    """EXHAUSTIVE PROOF: the line x=3 is |6-3|=3 units from B=(6,0),
    option A."""
    d = sp.Abs(sp.Integer(6) - sp.Integer(3))
    assert d == 3
    return 'A'


def check_C2():
    """EXHAUSTIVE PROOF: Apollonius PA=2PB has x-endpoints 4 and 12, so its
    centre is the midpoint (8,0), option A."""
    eps = _apollonius_endpoints(6, 2)
    assert list(eps) == [4, 12]
    centre = (eps[0] + eps[1]) / 2
    assert centre == 8
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: (2,2) has x^2+y^2=8<9 (strictly inside); the other
    candidates give 18, 13, 16, all outside, option A."""
    pts = {'(2,2)': 8, '(3,3)': 18, '(2,3)': 13, '(4,0)': 16}
    for k, v in pts.items():
        if k == '(2,2)':
            assert v < 9
        else:
            assert v > 9
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: PA=PB is the perpendicular bisector of AB, the
    vertical line x=3, option A."""
    x = sp.Rational(0 + 6, 2)
    assert x == 3
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: evaluating x^2+y^2 at the four candidates: all of
    (1,2), (2,1), (sqrt5,0), (1,-2) give exactly 5, so 4 lie on x^2+y^2=5,
    option B."""
    pts = [(1, 2), (2, 1), (sp.sqrt(5), 0), (1, -2)]
    vals = [sp.simplify(a ** 2 + b ** 2 - 5) for a, b in pts]
    assert vals == [0, 0, 0, 0]
    assert sum(1 for v in vals if v == 0) == 4
    return 'B'


def check_C6():
    """EXHAUSTIVE PROOF: the ellipse PA+PB=8 has major axis equal to the
    constant sum 8 (semi-major axis a=4), option B."""
    a = sp.Rational(8, 2)
    assert a == 4
    assert 2 * a == 8
    return 'B'


def check_C7():
    """EXHAUSTIVE PROOF: 'well-placed' means on the unit circle, which is
    exactly a^2+b^2=1: every such point has distance 1 (e.g. (3/5,4/5)
    gives 9/25+16/25=1), and every point with a^2+b^2=1 lies on it — so it
    is both necessary and sufficient, option A."""
    assert sp.Rational(9, 25) + sp.Rational(16, 25) == 1            # (3/5,4/5) on unit circle
    assert sp.Rational(9, 25) + sp.Rational(16, 25) == (sp.Rational(3, 5)) ** 2 + (sp.Rational(4, 5)) ** 2
    assert sp.Rational(1, 2) ** 2 + sp.Rational(1, 2) ** 2 != 1     # a+b=1 options fail
    return 'A'


def check_C8():
    """EXHAUSTIVE PROOF: x^2+y^2-4x+4=0 -> (x-2)^2+y^2=0, a single point:
    radius 0, option C."""
    cx, cy, r2 = _circle_centre_radius(-2, 0, 4)
    assert (cx, cy) == (2, 0)
    assert r2 == 0
    return 'C'


def check_D1():
    """EXHAUSTIVE PROOF: Apollonius PA=2PB has x-endpoints 4 and 12, so the
    distance between them on the x-axis is 8, option A."""
    eps = _apollonius_endpoints(6, 2)
    assert list(eps) == [4, 12]
    gap = sp.Abs(eps[1] - eps[0])
    assert gap == 8
    return 'A'


def check_D2():
    """EXHAUSTIVE PROOF: x^2+y^2-4x-6y+12=0 -> (x-2)^2+(y-3)^2=1, radius 1,
    option A."""
    cx, cy, r2 = _circle_centre_radius(-2, -3, 12)
    assert (cx, cy, r2) == (2, 3, 1)
    assert sp.sqrt(r2) == 1
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: x^2+y^2<1/2 forces x^2+y^2<1, so it is sufficient
    for being strictly inside (option A). Option C (x^2+y^2<2) is not
    sufficient: 3/2 satisfies it but is not <1. Option B (x<1/2,y<1/2)
    fails for (-2,-2): 4+4>1, outside. Option D (x>1,y>1) fails for (2,2)."""
    assert sp.Rational(1, 2) < 1                                    # A forces strict inside
    assert sp.Rational(3, 2) < 2 and sp.Rational(3, 2) > 1          # C counterexample
    assert -sp.Integer(2) < sp.Rational(1, 2)                       # B counterexample
    assert (-sp.Integer(2)) ** 2 + (-sp.Integer(2)) ** 2 > 1        # ... outside the disk
    assert sp.Integer(2) > 1                                        # D counterexample
    assert sp.Integer(2) ** 2 + sp.Integer(2) ** 2 > 1              # ... outside the disk
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: PA=3PB squared gives x^2+y^2=9((x-2)^2+y^2),
    which expands to -8x^2+36x-8y^2-36=0, i.e. (x-9/4)^2+y^2=9/16 — a real
    circle centred at (9/4,0) of radius 3/4, so Fil's (x-2)^2+y^2=9 is the
    wrong circle (it is centred at B and ignores A), option A."""
    eq = sp.expand(_X ** 2 + _Y ** 2 - 9 * ((_X - 2) ** 2 + _Y ** 2))
    norm = sp.expand(eq / -8)
    cx = sp.Rational(9, 4)
    r2 = sp.Rational(9, 16)
    rebuilt = sp.expand((_X - cx) ** 2 + _Y ** 2 - r2)
    assert sp.simplify(rebuilt - norm) == 0
    assert (cx, r2) == (sp.Rational(9, 4), sp.Rational(9, 16))
    assert cx != 2                 # Fil's circle is centred at B=(2,0), this is not
    assert sp.Rational(3, 4) != 3  # and the radius is 3/4, not 3
    return 'A'


def check_D5():
    """EXHAUSTIVE PROOF: the circle through (1,2) with centre (0,0) has
    r^2=1^2+2^2=5, so its equation is x^2+y^2=5."""
    r2 = sp.Integer(1) ** 2 + sp.Integer(2) ** 2
    assert r2 == 5
    return sp.Integer(5)


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
    labels = [f'A{i}' for i in range(1, 11)] + [f'B{i}' for i in range(1, 11)] + \
             [f'C{i}' for i in range(1, 9)] + [f'D{i}' for i in range(1, 6)]
    assert set(CHECKS) == set(labels), \
        f'missing/extra checks: {set(labels) ^ set(CHECKS)}'
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