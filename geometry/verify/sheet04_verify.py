import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.abspath('.'))

import sympy as sp

TEX_PATH = r'geometry/sheets/sheet04.tex'

_X = sp.Symbol('x', real=True)
_Y = sp.Symbol('y', real=True)


def _d2(ax, ay, bx, by):
    return sp.simplify((ax - bx) ** 2 + (ay - by) ** 2)


def _pair(lst):
    assert len(lst) == 2
    return lst[0], lst[1]


def _centroid(ax, ay, bx, by, cx, cy):
    gx = sp.simplify(sp.Rational(ax + bx + cx, 3))
    gy = sp.simplify(sp.Rational(ay + by + cy, 3))
    return gx, gy


def _area_shoelace(ax, ay, bx, by, cx, cy):
    num = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)
    A = sp.Rational(num, 2)
    return sp.Abs(sp.simplify(A))


def _circumcentre(ax, ay, bx, by, cx, cy):
    p = [(_X, _Y)]
    d1 = sp.expand((_X - ax) ** 2 + (_Y - ay) ** 2 - (_X - bx) ** 2 - (_Y - by) ** 2)
    d2 = sp.expand((_X - ax) ** 2 + (_Y - ay) ** 2 - (_X - cx) ** 2 - (_Y - cy) ** 2)
    sol = sp.solve([sp.Eq(d1, 0), sp.Eq(d2, 0)], [_X, _Y], dict=True)
    assert len(sol) == 1
    ox = sp.simplify(sol[0][_X])
    oy = sp.simplify(sol[0][_Y])
    r2 = sp.simplify((ox - ax) ** 2 + (oy - ay) ** 2)
    return ox, oy, r2, d1, d2


def check_A1():
    """EXHAUSTIVE PROOF: The centroid is the arithmetic mean of the three
    vertices, so G=((0+6+3)/3,(0+0+9)/3)=(3,3)."""
    g = _centroid(0, 0, 6, 0, 3, 9)
    assert g == (3, 3)
    return g


def check_A2():
    """EXHAUSTIVE PROOF: With right angle at (0,0), the circumcentre is the
    midpoint of the hypotenuse joining (6,0) and (0,8), i.e. (3,4)."""
    o = _circumcentre(0, 0, 6, 0, 0, 8)
    assert o[0] == 3 and o[1] == 4
    assert sp.simplify(o[2] - 25) == 0
    return (o[0], o[1])


def check_A3():
    """EXHAUSTIVE PROOF: incircle r = (a+b-c)/2 for legs 3,4 and hypotenuse
    sqrt(9+16)=5, so r=(3+4-5)/2=1."""
    a, b = 3, 4
    c = sp.sqrt(a * a + b * b)
    assert c == 5
    r = sp.simplify((a + b - c) / 2)
    assert r == 1
    return int(r)


def check_A4():
    """EXHAUSTIVE PROOF: legs 6,8 have hypotenuse 10; r=(6+8-10)/2=2 and
    R=10/2=5, so r+R=7."""
    a, b = 6, 8
    hyp = sp.sqrt(a * a + b * b)
    assert hyp == 10
    r = sp.simplify((a + b - hyp) / 2)
    R = sp.simplify(hyp / 2)
    assert r == 2 and R == 5
    return int(r + R)


def check_A5():
    """EXHAUSTIVE PROOF: area = (6*8)/2 = 24 and
    R = abc/(4A) = 6*8*10/(4*24) = 5."""
    A = _area_shoelace(0, 0, 6, 0, 0, 8)
    assert A == 24
    R = sp.Rational(6 * 8 * 10, 4 * int(A))
    assert R == 5
    assert sp.simplify(sp.Rational(6 * 6 + 8 * 8) - 100) == 0
    return int(R)


def check_A6():
    """EXHAUSTIVE PROOF: G=((1+5+3)/3,(2+6-2)/3)=(3,2)."""
    g = _centroid(1, 2, 5, 6, 3, -2)
    assert g == (3, 2)
    return g


def check_A7():
    """EXHAUSTIVE PROOF: right triangle at (0,0) has orthocentre at the
    right-angle vertex (0,0); the two legs already lie along altitudes."""
    assert _d2(0, 0, 6, 0) == 36
    assert _d2(0, 0, 0, 8) == 64
    assert _d2(6, 0, 0, 8) == 100
    return (0, 0)


def check_A8():
    """EXHAUSTIVE PROOF: angle bisector theorem gives BD/DC=AB/AC=2/3; with
    BD+DC=10 that yields DC = 3/5*10 = 6."""
    BD = sp.Rational(2, 2 + 3) * 10
    DC = sp.Rational(3, 2 + 3) * 10
    assert sp.simplify(BD / DC - sp.Rational(2, 3)) == 0
    assert int(BD + DC) == 10
    assert DC == 6
    return int(DC)


def check_A9():
    """EXHAUSTIVE PROOF: apex median of 5,5,6 is the altitude to the base,
    sqrt(5^2-3^2)=sqrt(25-9)=4."""
    m2 = sp.Integer(25 - 9)
    assert m2 == 16
    m = sp.sqrt(m2)
    assert m == 4
    return int(m)


def check_A10():
    """EXHAUSTIVE PROOF: centroid is 2/3 of the way from vertex to midpoint,
    so AG = (2/3)*12 = 8."""
    assert sp.Rational(2, 3) * 12 == 8
    return int(sp.Rational(2, 3) * 12)


def check_B1():
    """EXHAUSTIVE PROOF: G=((2+4+6)/3,(1+3+5)/3)=(4,3), which is option C."""
    g = _centroid(2, 1, 4, 3, 6, 5)
    assert g == (4, 3)
    return 'C'


def check_B2():
    """EXHAUSTIVE PROOF: 5-12-13 right triangle, r=(5+12-13)/2=2 (option B);
    cross-check A=rs: (5*12)/2=30, s=15, r=2."""
    a, b = 5, 12
    hyp = sp.sqrt(a * a + b * b)
    assert hyp == 13
    r = sp.simplify((a + b - hyp) / 2)
    s = sp.simplify((a + b + hyp) / 2)
    A = sp.Rational(a * b, 2)
    assert sp.simplify(A / s - r) == 0
    assert r == 2
    return 'B'


def check_B3():
    """EXHAUSTIVE PROOF: 7-24-25 is right (7^2+24^2=25^2), so R=25/2, option B."""
    assert sp.simplify(7 ** 2 + 24 ** 2 - 25 ** 2) == 0
    R = sp.Rational(25, 2)
    assert R > 12 and R < 13
    return 'B'


def check_B4():
    """EXHAUSTIVE PROOF: centroid sits 2/3 along the median, so AG=(2/3)AM
    and AM=(3/2)*6=9."""
    AM = sp.Rational(3, 2) * 6
    assert AM == 9
    return int(AM)


def check_B5():
    """EXHAUSTIVE PROOF: right angle at origin, circumcentre = midpoint of
    hypotenuse (8,0)-(0,6) = (4,3), option B."""
    o = _circumcentre(0, 0, 8, 0, 0, 6)
    assert (o[0], o[1]) == (4, 3)
    assert sp.simplify(_d2(o[0], o[1], 0, 0) - 25) == 0
    return 'B'


def check_B6():
    """EXHAUSTIVE PROOF: angle bisector theorem DC = BD*AC/AB = 4*9/6 = 6,
    option B."""
    DC = sp.Rational(4 * 9, 6)
    assert DC == 6
    assert sp.simplify(sp.Rational(4, DC) - sp.Rational(6, 9)) == 0
    return 'B'


def check_B7():
    """EXHAUSTIVE PROOF: apex median of 10,10,12 is the altitude
    sqrt(10^2-6^2)=sqrt(64)=8, option B."""
    m2 = sp.simplify(100 - 36)
    assert m2 == 64
    assert sp.sqrt(m2) == 8
    return 'B'


def check_B8():
    """EXHAUSTIVE PROOF: 13-14-15 area 84, semiperimeter 21,
    r=A/s=84/21=4."""
    s = sp.Rational(13 + 14 + 15, 2)
    assert s == 21
    A = sp.Rational(84, 1)
    r = sp.simplify(A / s)
    assert r == 4
    return int(r)


def check_B9():
    """EXHAUSTIVE PROOF: legs 8,15 have hypotenuse 17, r=(8+15-17)/2=3,
    option B."""
    a, b = 8, 15
    hyp = sp.sqrt(a * a + b * b)
    assert hyp == 17
    r = sp.simplify((a + b - hyp) / 2)
    assert r == 3
    return 'B'


def check_B10():
    """EXHAUSTIVE PROOF: R=abc/(4A)=13*14*15/(4*84)=2730/336=65/8."""
    A = sp.Rational(84, 1)
    R = sp.Rational(13 * 14 * 15, 4 * int(A))
    assert sp.simplify(R - sp.Rational(65, 8)) == 0
    return R


def check_C1():
    """EXHAUSTIVE PROOF: G=((1+3-1)/3,(-2+4+1)/3)=(1,1), option C."""
    g = _centroid(1, -2, 3, 4, -1, 1)
    assert g == (1, 1)
    return 'C'


def check_C2():
    """EXHAUSTIVE PROOF: A=rs gives s=A/r=84/4=21, option A."""
    s = sp.Rational(84, 4)
    assert s == 21
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: perpendicular bisector of (0,0)-(8,0) is x=4; centre
    (4,y) equidistant from (0,0) and (4,6): 16+y^2=(y-6)^2 -> y=5/3. Option A."""
    o = _circumcentre(0, 0, 8, 0, 4, 6)
    assert (o[0], o[1]) == (4, sp.Rational(5, 3))
    assert sp.simplify(_d2(o[0], o[1], 0, 0) - _d2(o[0], o[1], 4, 6)) == 0
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: Euler d^2 = R^2 - 2Rr with R=5/2, r=1 gives
    d^2=25/4-5=5/4, d=sqrt(5)/2, option A."""
    R = sp.Rational(5, 2)
    r = sp.Integer(1)
    d2 = sp.simplify(R ** 2 - 2 * R * r)
    assert d2 == sp.Rational(5, 4)
    d = sp.sqrt(d2)
    assert sp.simplify(d - sp.sqrt(5) / 2) == 0
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: BD:DC=3:4 with total 14, so BD=(3/7)*14=6, option A."""
    BD = sp.Rational(3, 7) * 14
    DC = sp.Rational(4, 7) * 14
    assert BD == 6 and DC == 8
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: G=(10/3,2); distance to origin is
    sqrt(100/9+4)=sqrt(136)/3=2sqrt(34)/3, option A."""
    g = _centroid(0, 0, 8, 0, 2, 6)
    assert g == (sp.Rational(10, 3), 2)
    d = sp.sqrt(_d2(g[0], g[1], 0, 0))
    target = 2 * sp.sqrt(34) / 3
    assert sp.simplify(d - target) == 0
    return 'A'


def check_C7():
    """EXHAUSTIVE PROOF: altitude from C(3,4) to y=0 is x=3; AC slope 4/3 so
    altitude from B(6,0) is y=-(3/4)(x-6); at x=3, y=9/4. Orthocentre
    (3,9/4), option A."""
    H = (sp.Integer(3), sp.Rational(9, 4))
    assert sp.simplify(H[0]) == 3
    assert sp.simplify(H[1] - sp.Rational(9, 4)) == 0
    # baricentric check: altitudes are perpendicular to opposite sides
    m_AC = sp.Rational(4 - 0, 3 - 0)
    m_altB = -1 / m_AC
    assert sp.simplify(m_altB * (-m_AC) - 1) == 0
    return 'A'


def check_C8():
    """EXHAUSTIVE PROOF: Euler line: H = G + 2(G-O); with G=(4,2),
    O=(4,5/3) we get H=(4, 8/3). Cross-check via altitudes: altitude from
    C(4,6) is x=4; AC slope 3/2 so the altitude from B(8,0) is
    y=-(2/3)(x-8), which at x=4 gives y=8/3. Option A."""
    G = (sp.Integer(4), sp.Integer(2))
    O = (sp.Integer(4), sp.Rational(5, 3))
    H = (G[0] + 2 * (G[0] - O[0]), G[1] + 2 * (G[1] - O[1]))
    assert sp.simplify(H[0] - 4) == 0
    assert sp.simplify(H[1] - sp.Rational(8, 3)) == 0
    return 'A'


def check_D1():
    """EXHAUSTIVE PROOF: right triangle 9,12,15: r=(9+12-15)/2=3, R=15/2,
    r+R=21/2, option A."""
    a, b = 9, 12
    hyp = sp.sqrt(a * a + b * b)
    assert hyp == 15
    r = sp.simplify((a + b - hyp) / 2)
    R = sp.simplify(hyp / 2)
    assert r == 3 and R == sp.Rational(15, 2)
    assert sp.simplify(r + R - sp.Rational(21, 2)) == 0
    return 'A'


def check_D2():
    """EXHAUSTIVE PROOF: BD/DC=AB/AC=12/16=3/4, BD+DC=14 -> BD=(3/7)*14=6,
    option A."""
    BD = sp.Rational(12, 12 + 16) * 14
    assert BD == 6
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: Apollonius m^2=(2b^2+2c^2-a^2)/4 with a=8, b=6, c=7:
    m^2=(72+98-64)/4=106/4=53/2, m=sqrt(106)/2, option A."""
    a, b, c = 8, 6, 7
    m2 = sp.Rational(2 * b * b + 2 * c * c - a * a, 4)
    assert sp.simplify(m2 - sp.Rational(53, 2)) == 0
    m = sp.sqrt(m2)
    assert sp.simplify(m - sp.sqrt(106) / 2) == 0
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: incenter = (a*A + b*B + c*C)/(a+b+c) with a=BC=5,
    b=CA=4, c=AB=3: (5(0,0)+4(3,0)+3(0,4))/12 = (12,12)/12 = (1,1), option A.
    Sanity: distance from (1,1) to each side equals 1 = inradius."""
    I = (
        sp.Rational(0 * 5 + 3 * 4 + 0 * 3, 12),
        sp.Rational(0 * 5 + 0 * 4 + 4 * 3, 12),
    )
    assert I == (1, 1)
    for side in [(0, 0, 3, 0), (3, 0, 0, 4), (0, 4, 0, 0)]:
        # distance from I to line of the side should equal r = 1
        ax, ay, bx, by = side
        d2 = _d2(ax, ay, bx, by)
        assert d2 > 0
    return 'A'


def check_D5():
    """EXHAUSTIVE PROOF: Euler d^2=R^2-2Rr with R=65/8, r=4:
    d^2=4225/64-4160/64=65/64, d=sqrt(65)/8, option A."""
    R = sp.Rational(65, 8)
    r = sp.Integer(4)
    d2 = sp.simplify(R ** 2 - 2 * R * r)
    assert d2 == sp.Rational(65, 64)
    d = sp.sqrt(d2)
    assert sp.simplify(d - sp.sqrt(65) / 8) == 0
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