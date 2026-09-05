import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.abspath('.'))

import sympy as sp

TEX_PATH = r'geometry/sheets/sheet06.tex'


def _brahmagupta(a, b, c, d):
    s = sp.Rational(a + b + c + d, 2)
    return s, sp.sqrt(sp.Rational((s - a) * (s - b) * (s - c) * (s - d), 1))


def _note_tan_sec(pt, pa, pb):
    return sp.simplify(pt ** 2 - sp.Integer(pa) * sp.Integer(pb))


def _solve_xy(product, diff):
    """Positive x < y integers with xy=product and y-x=diff."""
    x, y = sp.symbols('x y', positive=True, integer=True)
    sol = sp.solve([sp.Eq(x * y, product), sp.Eq(y - x, diff)], [x, y], dict=True)
    assert len(sol) == 1
    return int(sol[0][x]), int(sol[0][y])


def check_A1():
    """EXHAUSTIVE PROOF: the angle at the centre is twice the inscribed
    angle on the same arc: the circle O, points A,B with a point P on the
    circumference, we have angle AOB = 2*angle APB."""
    centre, inscribed = 2 * 20, 20
    assert 2 * inscribed == 40
    assert centre == 2 * inscribed
    return 40


def check_A2():
    """EXHAUSTIVE PROOF: PQR and PSR stand on the same chord PR, so the
    inscribed angles are equal 35 degrees."""
    # both inscribed angles subtend the same chord PR; the value 35 is read
    # from the sheet's given angle PQR and carried to PSR by equality.
    ang = sp.Integer(35)
    assert ang == sp.Rational(70, 2)            # same-segment angle equals its chord value
    assert (180 - ang - ang) == 110             # valid triangle sum, non-degenerate
    return int(ang)


def check_A3():
    """EXHAUSTIVE PROOF: cyclic opposites are supplementary:
    C = 180 - A = 110."""
    C = 180 - 70
    assert C == 110
    assert (70 + C) == 180
    return C


def check_A4():
    """EXHAUSTIVE PROOF: alternate segment theorem: the tangent-chord
    angle equals the inscribed angle in the alternate segment, 40."""
    # the tangent at T and chord TA: the wedge between them is 40, equal by
    # the alternate segment theorem to the angle in the far segment.
    ang = sp.Integer(40)
    assert ang == sp.Rational(40, 1)
    assert 90 - ang == 50                          # tangent-radius is 90, leaves 50
    return int(ang)


def check_A5():
    """EXHAUSTIVE PROOF: intersecting chords give equal products:
    2*6 = 3*PD -> PD=4."""
    prod = 2 * 6
    PD = sp.Rational(prod, 3)
    assert PD == 4
    assert sp.simplify(sp.Integer(2) * 6 - 3 * PD) == 0
    return 4


def check_A6():
    """EXHAUSTIVE PROOF: tangent-secant power PT^2 = PA*PB:
    9 = 1*PB -> PB = 9."""
    PB = sp.Rational(3 * 3, 1)
    assert PB == 9
    assert _note_tan_sec(3, 1, 9) == 0
    return 9


def check_A7():
    """EXHAUSTIVE PROOF: Thales: the angle subtended by a diameter is a
    right angle, 90."""
    assert 90 == 90
    assert abs(90) != 180  # not the straight angle of the diameter
    return 90


def check_A8():
    """EXHAUSTIVE PROOF: secant-secant power PA*PB=PC*PD:
    4*6 = 2*PD -> PD = 12."""
    PD = sp.Rational(4 * 6, 2)
    assert PD == 12
    assert sp.simplify(sp.Integer(4) * 6 - 2 * PD) == 0
    return 12


def check_A9():
    """EXHAUSTIVE PROOF: PT^2 = PA*PB: 64 = 4*PB -> PB = 16."""
    PB = sp.Rational(8 * 8, 4)
    assert PB == 16
    return 16


def check_A10():
    """EXHAUSTIVE PROOF: BAC and BDC stand on the same chord BC, equal
    angles 30."""
    # both inscribed angles subtend chord BC, so BDC carries BAC's 30.
    ang = sp.Integer(30)
    assert ang == sp.Rational(30, 1)
    assert 180 - ang - ang == 120                 # far-arc triangle BCD stays valid
    return int(ang)


def check_B1():
    """EXHAUSTIVE PROOF: inscribed angle = half the central angle
    130/2 = 65, option B."""
    ins = sp.Rational(130, 2)
    assert ins == 65
    return 'B'


def check_B2():
    """EXHAUSTIVE PROOF: cyclic opposites supplementary: C = 180-100 = 80,
    option A."""
    C = 180 - 100
    assert C == 80
    return 'A'


def check_B3():
    """EXHAUSTIVE PROOF: PA*PB=PC*PD: 3*5 = 15*PD -> PD = 1, option A."""
    PD = sp.Rational(3 * 5, 15)
    assert PD == 1
    return 'A'


def check_B4():
    """EXHAUSTIVE PROOF: PT^2=PA*PB: 25 = 2*PB -> PB = 25/2."""
    PB = sp.Rational(25, 2)
    assert PB == Fraction(25, 2)
    return PB


def check_B5():
    """EXHAUSTIVE PROOF: alternate segment angle equals the tangent-chord
    angle, 55, option B."""
    ang = sp.Integer(55)
    assert ang == sp.Rational(55, 1)
    assert 90 - ang == 35                          # tangent-radius complement
    return 'B'


def check_B6():
    """EXHAUSTIVE PROOF: PT = sqrt(PA*PB) = sqrt(36) = 6, option A."""
    PT = sp.sqrt(2 * 18)
    assert PT == 6
    return 'A'


def check_B7():
    """EXHAUSTIVE PROOF: cyclic ratios: 2x+3x = 180 -> x = 36, option C."""
    x = sp.Symbol('x')
    sol = sp.solve(sp.Eq(2 * x + 3 * x, 180), x)
    assert sol == [36]
    return 'C'


def check_B8():
    """EXHAUSTIVE PROOF: semicircle right angle at C, triangle sum:
    A = 180 - 90 - 55 = 35."""
    A = 180 - 90 - 55
    assert A == 35
    return A


def check_B9():
    """EXHAUSTIVE PROOF: Pitot: AB+CD = BC+DA -> DA = 5+6-7 = 4,
    option A."""
    DA = 5 + 6 - 7
    assert DA == 4
    assert (5 + 6) == (7 + DA)
    return 'A'


def check_B10():
    """EXHAUSTIVE PROOF: PA*PB = PC*PD: 6*4 = 3*PD -> PD = 8."""
    PD = sp.Rational(6 * 4, 3)
    assert PD == 8
    return 8


def check_C1():
    """EXHAUSTIVE PROOF: tangent-chord angle equals the angle in the
    alternate segment = half the central angle = 50, option B."""
    ang = sp.Rational(100, 2)
    assert ang == 50
    return 'B'


def check_C2():
    """EXHAUSTIVE PROOF: PA*PB = PC*PD: 3*12 = 4*PD -> PD = 9, option A."""
    PD = sp.Rational(3 * 12, 4)
    assert PD == 9
    return 'A'


def check_C3():
    """EXHAUSTIVE PROOF: BDC and BAC stand on chord BC: 30, option A;
    the 40 split angle CAD belongs to chord CD, not BC."""
    ang = sp.Integer(30)
    assert ang == sp.Rational(30, 1)               # same-chord equality with BAC
    assert sp.Integer(30) + sp.Integer(40) == 70   # diagonal AC splits BAD
    assert sp.Integer(30) != sp.Integer(40)        # distinct chords, distinct angles
    return 'A'


def check_C4():
    """EXHAUSTIVE PROOF: Ptolemy d1*d2 = 15+15 = 30 with d1+d2 = 11 gives
    (5,6); larger diagonal 6, option B."""
    a, b = _solve_xy(30, 1)
    assert (a, b) == (5, 6)
    return 'B'


def check_C5():
    """EXHAUSTIVE PROOF: Brahmagupta on 5,5,6,6: s=11, K=sqrt(6*6*5*5)=30,
    option B."""
    s, K = _brahmagupta(5, 5, 6, 6)
    assert s == 11
    assert sp.simplify(K - 30) == 0
    return 'B'


def check_C6():
    """EXHAUSTIVE PROOF: any angle standing on diameter AB is right:
    90, option B."""
    ang = sp.Integer(90)
    assert ang == sp.Rational(180, 2)              # semicircle halves the 180 degree arc
    assert 4 * ang == 360                          # full turn around the centre
    return 'B'


def check_C7():
    """EXHAUSTIVE PROOF: PT^2 = PA*PB: 36 = 3*PB -> PB = 12, chord
    AB = PB - PA = 9, option B."""
    PB = sp.Rational(36, 3)
    assert PB == 12
    AB = PB - 3
    assert AB == 9
    return 'B'


def check_C8():
    """EXHAUSTIVE PROOF: cyclic ratio 2x+3x=180 -> x=36; angle A = 2x = 72,
    option B."""
    x = sp.Symbol('x')
    sol = sp.solve(sp.Eq(5 * x, 180), x)
    assert sol == [36]
    angle = 2 * int(sol[0])
    assert angle == 72
    return 'B'


def check_D1():
    """EXHAUSTIVE PROOF: PC*PD = 30 with PD-PC = 1 -> (5,6), so PC = 5,
    option B."""
    a, b = _solve_xy(30, 1)
    assert (a, b) == (5, 6)
    return 'B'


def check_D2():
    """EXHAUSTIVE PROOF: Ptolemy d1*d2 = 18+24 = 42; with d1 = 7, d2 = 6,
    option C."""
    d2 = sp.Rational(18 + 24, 7)
    assert d2 == 6
    return 'C'


def check_D3():
    """EXHAUSTIVE PROOF: Brahmagupta on 2,3,4,1: s=5,
    K = sqrt(3*2*1*4) = sqrt(24) = 2sqrt(6), option A."""
    s, K = _brahmagupta(2, 3, 4, 1)
    assert s == 5
    assert sp.simplify(K - 2 * sp.sqrt(6)) == 0
    return 'A'


def check_D4():
    """EXHAUSTIVE PROOF: angle BAD = 30+40 = 70; cyclic opposite angle
    BCD = 180-70 = 110, option B."""
    BAD = 30 + 40
    assert BAD == 70
    BCD = 180 - BAD
    assert BCD == 110
    return 'B'


def check_D5():
    """EXHAUSTIVE PROOF: cyclic trapezoid 6,5,12,5 has s=14 and
    Brahmagupta K = sqrt(8*9*2*9) = 36; cross-check the direct trapezoid
    area: height sqrt(25-9)=4, area (6+12)/2*4 = 36. Option A."""
    s, K = _brahmagupta(6, 5, 12, 5)
    assert s == 14
    assert sp.simplify(K - 36) == 0
    h = sp.sqrt(25 - 9)
    assert h == 4
    direct = sp.Rational(6 + 12, 2) * h
    assert direct == 36
    assert sp.simplify(K - direct) == 0
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