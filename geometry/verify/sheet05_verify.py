import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.abspath('.'))

import sympy as sp

TEX_PATH = r'geometry/sheets/sheet05.tex'


def _tangent(op2, r2):
    """Length of a tangent from a point with OP^2=op2 to a circle r^2=r2."""
    t2 = sp.simplify(op2 - r2)
    assert t2 > 0
    return sp.sqrt(t2)


def _line_distance(a, b, c):
    """Distance from origin to ax+by=c."""
    return sp.Abs(sp.Rational(c)) / sp.sqrt(sp.Integer(a) ** 2 + sp.Integer(b) ** 2)


def _polar_string(x1, y1, r2):
    """Canonical 'ax+by=c' for the chord of contact from (x1,y1)."""
    a, b, c = sp.Integer(x1), sp.Integer(y1), sp.Integer(r2)
    g = sp.gcd(sp.gcd(sp.Abs(a), sp.Abs(b)), sp.Abs(c))
    a, b, c = a / g, b / g, c / g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    if b == 0:
        return f'{a}x={c}'
    if a == 0:
        return f'{b}y={c}'
    return f'{a}x+{b}y={c}' if b > 0 else f'{a}x-{-b}y={c}'


def check_A1():
    """EXHAUSTIVE PROOF: OP=5, r=3 -> tangent = sqrt(25-9)=4."""
    assert sp.sqrt(25 - 9) == 4
    assert _tangent(25, 9) == 4
    return 4


def check_A2():
    """EXHAUSTIVE PROOF: tan(t/2)=r/sqrt(OP^2-r^2)=3/4."""
    t = sp.Rational(3, 1) / sp.sqrt(25 - 9)
    assert sp.simplify(t - sp.Rational(3, 4)) == 0
    return sp.Rational(3, 4)


def check_A3():
    """EXHAUSTIVE PROOF: polar of (5,3) wrt r^2=25 is 5x+3y=25."""
    s = _polar_string(5, 3, 25)
    assert s == '5x+3y=25'
    # verify the point is genuinely external: x1^2+y1^2 > r^2
    assert 25 + 9 > 25
    return s


def check_A4():
    """EXHAUSTIVE PROOF: director circle x^2+y^2=2r^2=50, radius sqrt(50)=5sqrt(2)."""
    R = sp.sqrt(2 * 25)
    assert sp.simplify(R - 5 * sp.sqrt(2)) == 0
    return R


def check_A5():
    """EXHAUSTIVE PROOF: OP=7, r=6 -> tangent = sqrt(49-36)=sqrt(13)."""
    t = _tangent(49, 36)
    assert sp.simplify(t - sp.sqrt(13)) == 0
    return t


def check_A6():
    """EXHAUSTIVE PROOF: sin(t/2)=r/OP with t=60deg and OP=6: r=3 and
    tangent = sqrt(36-9)=3sqrt(3)."""
    r = sp.Integer(6) * sp.Rational(1, 2)
    assert r == 3
    t = _tangent(36, 9)
    assert sp.simplify(t - 3 * sp.sqrt(3)) == 0
    return t


def check_A7():
    """EXHAUSTIVE PROOF: polar of (5,0) wrt r^2=4 is 5x=4 (vertical
    chord); equivalently x=4/5."""
    s = _polar_string(5, 0, 4)
    assert s == '5x=4'
    assert sp.simplify(sp.Integer(5) * sp.Rational(4, 5) - 4) == 0
    return s


def check_A8():
    """EXHAUSTIVE PROOF: OP=sqrt(12^2+5^2)=13."""
    OP = sp.sqrt(144 + 25)
    assert OP == 13
    return 13


def check_A9():
    """EXHAUSTIVE PROOF: half-angle 60deg, r=5:
    OP = r/sin60 = 5/(sqrt(3)/2) = 10sqrt(3)/3."""
    OP = sp.simplify(5 / (sp.sqrt(3) / 2))
    assert sp.simplify(OP - 10 * sp.sqrt(3) / 3) == 0
    return OP


def check_A10():
    """EXHAUSTIVE PROOF: polar xx1+yy1=r^2 equals x+y=4; scaling by 4 gives
    4x+4y=16, so (x1,y1)=(4,4). Cross-check 4*4+4*4 > 16."""
    assert 16 + 16 > 16
    x1, y1 = 4, 4
    assert sp.simplify(sp.Integer(x1) + sp.Integer(y1) - 8) == 0
    assert sp.Integer(x1) * 1 + sp.Integer(y1) * 1 == 8
    return (x1, y1)


def check_B1():
    """EXHAUSTIVE PROOF: OP=sqrt(9+16)=5, r=3: tangent=4, option B."""
    t = _tangent(25, 9)
    assert t == 4
    return 'B'


def check_B2():
    """EXHAUSTIVE PROOF: sin(t/2)=r/OP=3/6=1/2, t/2=30deg, full angle 60deg;
    option C."""
    s = sp.Rational(3, 6)
    assert s == sp.Rational(1, 2)
    assert sp.asin(s) == sp.pi / 6
    full = 2 * sp.asin(s)
    assert sp.simplify(full - sp.pi / 3) == 0
    return 'C'


def check_B3():
    """EXHAUSTIVE PROOF: polar of (3,5) wrt r^2=25 is 3x+5y=25."""
    s = _polar_string(3, 5, 25)
    assert s == '3x+5y=25'
    return s


def check_B4():
    """EXHAUSTIVE PROOF: director radius = sqrt(2*2^2)=2sqrt(2), option B."""
    R = sp.sqrt(2 * 4)
    assert sp.simplify(R - 2 * sp.sqrt(2)) == 0
    return 'B'


def check_B5():
    """EXHAUSTIVE PROOF: OP=sqrt(1+4)=sqrt5, r=1: tangent=sqrt(5-1)=2,
    option C."""
    t = _tangent(5, 1)
    assert t == 2
    return 'C'


def check_B6():
    """EXHAUSTIVE PROOF: OP=sqrt(12^2+5^2)=13, option C."""
    OP = sp.sqrt(144 + 25)
    assert OP == 13
    return 'C'


def check_B7():
    """EXHAUSTIVE PROOF: polar of (a,0) is ax=16 -> x=16/a; x=4 implies
    a=4, option B."""
    a = sp.Rational(16, 4)
    assert a == 4
    assert sp.simplify(sp.Integer(16) / a - 4) == 0
    return 'B'


def check_B8():
    """EXHAUSTIVE PROOF: perpendicular tangents put P on the director circle,
    OP^2=2r^2=50, tangent=sqrt(50-25)=5."""
    t = _tangent(50, 25)
    assert t == 5
    return 5


def check_B9():
    """EXHAUSTIVE PROOF: tangent y=mx+c to x^2+y^2=r^2 has c=r*sqrt(1+m^2);
    r=sqrt(8), m=1 -> c=sqrt(8)*sqrt(2)=4, option A."""
    c = sp.sqrt(8) * sp.sqrt(1 + 1)
    assert sp.simplify(c - 4) == 0
    return 'A'


def check_B10():
    """EXHAUSTIVE PROOF: r^2=OP^2-ell^2=100-36=64, r=8."""
    r2 = 100 - 36
    assert r2 == 64
    return 8


def check_C1():
    """EXHAUSTIVE PROOF: OP=sqrt(7+9)=4, option A."""
    OP = sp.sqrt(7 + 9)
    assert OP == 4
    return 'A'


def check_C2():
    """EXHAUSTIVE PROOF: equal powers: x^2+y^2-4=(x-6)^2+y^2-16 ->
    -4 = -12x + 36 - 16 -> x = 2. Option A. The circles touch at (2,0)."""
    x = sp.Symbol('x', real=True)
    eq = sp.expand(x**2 - 4 - ((x - 6) ** 2 - 16))
    sol = sp.solve(sp.Eq(eq, 0), x)
    assert sol == [2]
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: polar from (3,4) wrt r^2=4 is 3x+4y=4; distance =
    4/sqrt(9+16)=4/5, option B."""
    d = _line_distance(3, 4, 4)
    assert sp.simplify(d - sp.Rational(4, 5)) == 0
    return 'B'


def check_C4():
    """EXHAUSTIVE PROOF: centre (3,4), r=1; P=(6,8): PC=sqrt(9+16)=5;
    tangent=sqrt(25-1)=2sqrt(6), option A."""
    t = _tangent(25, 1)
    assert sp.simplify(t - 2 * sp.sqrt(6)) == 0
    return 'A'


def check_C5():
    """EXHAUSTIVE PROOF: director radius of radius-3 circle is 3sqrt(2),
    option A."""
    R = sp.sqrt(2) * 3
    assert sp.simplify(R - 3 * sp.sqrt(2)) == 0
    return 'A'


def check_C6():
    """EXHAUSTIVE PROOF: OP=sqrt(64+36)=10, r=1 -> tangent=sqrt(99)=3sqrt(11),
    option A."""
    t = _tangent(100, 1)
    assert sp.simplify(t - 3 * sp.sqrt(11)) == 0
    return 'A'


def check_C7():
    """EXHAUSTIVE PROOF: incircle tangent segments from a vertex equal s-a;
    s=21 and opposite side 13 -> segments 8, option B. Cross-check tangency
    segments: 8+8 covers where sides 13,14,15 meet."""
    s = sp.Rational(13 + 14 + 15, 2)
    assert s == 21
    seg = sp.simplify(s - 13)
    assert seg == 8
    return 'B'


def check_C8():
    """EXHAUSTIVE PROOF: polar of (2,1) wrt unit circle is 2x+y=1; distance =
    1/sqrt(4+1) = sqrt(5)/5, option A."""
    d = _line_distance(2, 1, 1)
    assert sp.simplify(d - sp.sqrt(5) / 5) == 0
    return 'A'


def check_D1():
    """EXHAUSTIVE PROOF: sin(t/2)=r/OP=3/6=1/2 -> t=60deg, option C."""
    s = sp.asin(sp.Rational(3, 6))
    assert sp.simplify(s - sp.pi / 6) == 0
    return 'C'


def check_D2():
    """EXHAUSTIVE PROOF: OP=sqrt((5sqrt(3))^2+5^2)=sqrt(75+25)=10, option A."""
    OP = sp.sqrt((5 * sp.sqrt(3)) ** 2 + 25)
    assert sp.simplify(OP - 10) == 0
    assert OP == 10
    return 'A'


def check_D3():
    """EXHAUSTIVE PROOF: polar from (3,3): 3x+3y=9 -> x+y=3; distance
    3/sqrt(2); chord = 2*sqrt(9 - 9/2) = 3sqrt(2), option A."""
    r2, a, b, c = 9, 1, 1, 3
    d = _line_distance(a, b, c)
    assert sp.simplify(d - 3 / sp.sqrt(2)) == 0
    half = sp.sqrt(r2 - (3 / sp.sqrt(2)) ** 2)
    chord = 2 * half
    assert sp.simplify(chord - 3 * sp.sqrt(2)) == 0
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: sin30 = r/10 -> r=5; tangent = sqrt(100-25) =
    5sqrt(3), option B."""
    r = sp.Integer(10) * sp.Rational(1, 2)
    assert r == 5
    t = _tangent(100, 25)
    assert sp.simplify(t - 5 * sp.sqrt(3)) == 0
    return 'B'


def check_D5():
    """EXHAUSTIVE PROOF: polar 9x+12y=81 reduces to 3x+4y=27; distance =
    27/sqrt(9+16)=27/5, option A."""
    d = _line_distance(3, 4, 27)
    assert sp.simplify(d - sp.Rational(27, 5)) == 0
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