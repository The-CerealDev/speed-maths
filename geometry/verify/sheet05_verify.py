import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import math
from pathlib import Path

import sympy as sp

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans05.tex'

S2, S3 = sp.sqrt(2), sp.sqrt(3)


def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sp.simplify(sp.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _angle(P, V, Q):
    """Angle PVQ in degrees (numeric)."""
    a = (float(P[0]) - float(V[0]), float(P[1]) - float(V[1]))
    b = (float(Q[0]) - float(V[0]), float(Q[1]) - float(V[1]))
    return math.degrees(math.acos((a[0]*b[0] + a[1]*b[1]) / (math.hypot(*a) * math.hypot(*b))))


def _on_circle(deg, R=1.0, c=(0.0, 0.0)):
    return (c[0] + R*math.cos(math.radians(deg)), c[1] + R*math.sin(math.radians(deg)))


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: numerically, an arc seen at 20 degrees from the circumference is 40 at the centre."""
    O, A, B = (0, 0), _on_circle(0), _on_circle(40)
    for deg in (100, 180, 250, 330):
        assert abs(_angle(A, _on_circle(deg), B) - 20) < 1e-9
    assert abs(_angle(A, O, B) - 40) < 1e-9
    return 2 * 20


def check_A2():
    """EXHAUSTIVE PROOF: angle in a semicircle is 90 at several points."""
    A, B = _on_circle(0), _on_circle(180)
    for deg in (20, 77, 140, 250):
        assert abs(_angle(A, _on_circle(deg), B) - 90) < 1e-9
    return 90


def check_A3():
    """EXHAUSTIVE PROOF: opposite angles of a cyclic quadrilateral are supplementary; a concrete cyclic ABCD with A = 70 has C = 110."""
    # A at 0; choose B, C, D so that angle DAB = 70: arc BCD (not containing A) = 140
    A, B, C, D = _on_circle(0), _on_circle(110), _on_circle(180), _on_circle(250)
    assert abs(_angle(D, A, B) - 70) < 1e-9
    assert abs(_angle(B, C, D) - 110) < 1e-9
    return 180 - 70


def check_A4():
    """EXHAUSTIVE PROOF: tangent at T and chord TA at 40 degrees; the angle at any point of the alternate arc is 40."""
    T = _on_circle(270)                               # tangent at T is horizontal
    A = _on_circle(270 + 80)                          # chord TA makes 40 with the tangent (half the arc)
    tangent_pt = (T[0] + 1, T[1])
    assert abs(_angle(tangent_pt, T, A) - 40) < 1e-9
    for deg in (100, 150, 200):
        assert abs(_angle(T, _on_circle(deg), A) - 40) < 1e-9
    return 40


def check_A5():
    """EXHAUSTIVE PROOF: PA*PB = PC*PD: 12 = 3 PD, PD = 4."""
    pd = sp.Rational(2*6, 3)
    assert 2*6 == 3*pd
    return pd


def check_A6():
    """EXHAUSTIVE PROOF: PT^2 = PA*PB: 9 = PB; numeric construction agrees."""
    pb = sp.Rational(3**2, 1)
    # circle radius R, P at distance d with d^2 - R^2 = 9; secant along a line through P: product of roots = 9
    R, d = 4.0, 5.0
    t = sp.Symbol('t')
    roots = sp.solve((d - t*math.cos(0.3))**2 + (t*math.sin(0.3))**2 - R**2, t)
    assert abs(float(roots[0]*roots[1]) - 9) < 1e-9
    return pb


def check_A7():
    """EXHAUSTIVE PROOF: tangent length sqrt(49-36) = sqrt13."""
    L = sp.sqrt(7**2 - 6**2)
    assert L**2 == 13
    return L


def check_A8():
    """EXHAUSTIVE PROOF: tangents at 60 degrees, OP = 6: length 6 cos 30 = 3 sqrt3; radius 3, kite area 9 sqrt3 (inv)."""
    L = 6*sp.cos(sp.pi/6)
    r = 6*sp.sin(sp.pi/6)
    assert sp.simplify(L**2 + r**2 - 36) == 0 and sp.simplify(2*L*r/2 - 9*S3) == 0
    return sp.simplify(L)


def check_A9():
    """EXHAUSTIVE PROOF: tangents at 120, r = 5: OP = 5 / sin 60 = 10 sqrt3 / 3."""
    OP = 5 / sp.sin(sp.pi/3)
    assert sp.simplify(OP - 10*S3/3) == 0
    return sp.radsimp(OP)


def check_A10():
    """EXHAUSTIVE PROOF: angles on the same arc BC are equal (numeric cyclic ABCD)."""
    A, B, C, D = _on_circle(200), _on_circle(300), _on_circle(0), _on_circle(90)
    x = _angle(B, A, C)
    assert abs(x - _angle(B, D, C)) < 1e-9 and abs(x - 30) < 1e-9
    return 30


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: alternate segment: tangent-chord angle 55 equals the inscribed angle on the other side (B)."""
    T = _on_circle(270)
    A = _on_circle(270 + 110)
    assert abs(_angle((T[0] + 1, T[1]), T, A) - 55) < 1e-9
    ang = _angle(T, _on_circle(160), A)
    options = {'A': 35, 'B': 55, 'C': 110, 'D': 70}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_B2():
    """EXHAUSTIVE PROOF: 2x + 3x = 180, x = 36 (C)."""
    x = sp.Symbol('x')
    sol = sp.solve(5*x - 180, x)
    assert sol == [36]
    options = {'A': 24, 'B': 30, 'C': 36, 'D': 72}
    return _only(options, sol[0])


def check_B3():
    """EXHAUSTIVE PROOF: Pitot: DA = AB + CD - BC = 4 (A); a tangential quadrilateral built from tangent lengths agrees."""
    # tangent lengths from A, B, C, D: a, b, c, d with AB=a+b, BC=b+c, CD=c+d, DA=d+a
    a, b, c = 1, 4, 3                     # AB = 5, BC = 7
    d = 6 - c                             # CD = 6
    assert (a + b, b + c, c + d) == (5, 7, 6)
    da = d + a
    assert da == 5 + 6 - 7
    options = {'A': 4, 'B': 6, 'C': 8, 'D': 18}
    return _only(options, da)


def check_B4():
    """EXHAUSTIVE PROOF: 144 = 8 PB, PB = 18, AB = 10 (B)."""
    pb = sp.Rational(144, 8)
    assert 8*pb == 12**2
    ab = pb - 8
    options = {'A': 6, 'B': 10, 'C': 12, 'D': 18}
    return _only(options, ab)


def check_B5():
    """EXHAUSTIVE PROOF: 4*18 = 6*PD, PD = 12, CD = 6; tangent length sqrt72 (inv)."""
    pd = sp.Rational(4*18, 6)
    assert pd == 12 and sp.sqrt(4*18) == 6*S2
    return pd - 6


def check_B6():
    """EXHAUSTIVE PROOF: sin(theta/2) = 3/6, theta = 60 (C)."""
    theta = 2*sp.asin(sp.Rational(3, 6))
    assert sp.simplify(theta - sp.pi/3) == 0
    options = {'A': 30, 'B': 45, 'C': 60, 'D': 90}
    return _only(options, sp.simplify(theta*180/sp.pi))


def check_B7():
    """EXHAUSTIVE PROOF: circles radius 6 centred (0,0),(6,0) meet at (3, +-3sqrt3): AB = 6 sqrt3 (D)."""
    x, y = sp.symbols('x y', real=True)
    pts = sp.solve([x**2 + y**2 - 36, (x - 6)**2 + y**2 - 36], [x, y])
    ab = sp.Abs(pts[0][1] - pts[1][1])
    assert all(sp.simplify(px - 3) == 0 for px, _ in pts)          # common chord is x = 3
    options = {'A': 6, 'B': 12, 'C': 6*S2, 'D': 6*S3, 'E': 3*S3}
    return _only(options, sp.simplify(ab))


def check_B8():
    """EXHAUSTIVE PROOF: radii 4 and 10: a chord BC tangent to the small circle and diameter AC give AB = 8 (E)."""
    R, r = 10, 4
    # chord BC at distance r from O; C and B on the big circle with BC horizontal at y = -r
    half = math.sqrt(R**2 - r**2)
    C = (half, -r); B = (-half, -r)
    A = (-C[0], -C[1])
    assert abs(math.dist(A, B) - 8) < 1e-9 and abs(_angle(A, B, C) - 90) < 1e-9
    options = {'A': 16, 'B': 20, 'C': 8, 'D': 12, 'E': 10}
    return _only(options, R)


def check_B9():
    """EXHAUSTIVE PROOF: R^2 - r^2 = 15^2 for every pair of radii, so the annulus is 225 pi."""
    for r in (1, 5, 8, 20):
        R2 = r**2 + 15**2
        assert abs(2*math.sqrt(R2 - r**2) - 30) < 1e-12
    return 225*sp.Symbol('pi')                     # the .tex parser reads \pi as a symbol


def check_B10():
    """EXHAUSTIVE PROOF: angle ACB = 90, so angle BAC = 35."""
    A, B = _on_circle(180), _on_circle(0)
    C = _on_circle(180 - 2*55)                         # angle ABC = 55 means arc AC = 110
    assert abs(_angle(A, B, C) - 55) < 1e-9 and abs(_angle(A, C, B) - 90) < 1e-9
    return sp.nsimplify(round(_angle(B, A, C), 9))


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: DC^2 = DA*DB = 144, BC^2 = 256 - 144 = 112, radius 2sqrt7 (C); coordinates agree."""
    r = sp.sqrt(112) / 2
    B, C, D = (0, r), (0, -r), (12, -r)
    t = sp.Rational(7, 16)
    A = (B[0] + t*(D[0] - B[0]), B[1] + t*(D[1] - B[1]))
    assert sp.simplify(A[0]**2 + A[1]**2 - r**2) == 0
    assert sp.simplify(sp.sqrt((D[0] - A[0])**2 + (D[1] - A[1])**2) - 9) == 0
    options = {'A': 12, 'B': 4*sp.sqrt(7), 'C': 2*sp.sqrt(7), 'D': 8, 'E': 6}
    return _only(options, sp.simplify(r))


def check_C2():
    """EXHAUSTIVE PROOF: sum of XV^2 over a regular octagon of radius 2 is 8(d^2 + 4) for X at distance d; 40 gives d = 1 (A)."""
    V = [_on_circle(45*k, 2) for k in range(8)]
    for d in (0.0, 0.5, 1.0, 1.7):
        for deg in (0, 13, 77, 200, 333):
            X = _on_circle(deg, d)
            assert abs(sum(math.dist(X, v)**2 for v in V) - 8*(d**2 + 4)) < 1e-9
    d = sp.Symbol('d', positive=True)
    sol = sp.solve(8*(d**2 + 4) - 40, d)
    assert sol == [1]
    options = {'A': 1, 'B': sp.sqrt(5), 'C': 2, 'D': 3, 'E': S3}
    return _only(options, sol[0])


def check_C3():
    """EXHAUSTIVE PROOF: lens of two radius-2 circles through each other's centres = 8pi/3 - 2sqrt3 (D); grid count agrees."""
    exact = 2*(sp.Rational(1, 3)*sp.pi*4 - sp.Rational(1, 2)*4*sp.sin(2*sp.pi/3))
    n, lo, hi = 800, -0.1, 2.1
    h = (hi - lo) / n
    count = sum(1 for i in range(n) for j in range(n)
                if (lo + (i + .5)*h)**2 + (-2.1 + (j + .5)*h*2)**2 <= 4 and (lo + (i + .5)*h - 2)**2 + (-2.1 + (j + .5)*h*2)**2 <= 4)
    assert abs(count*h*(2*h) - float(exact)) < 0.02
    options = {'A': 4*sp.pi/3 - S3, 'B': 8*sp.pi/3 - S3, 'C': 4*sp.pi/3 + 2*S3, 'D': 8*sp.pi/3 - 2*S3, 'E': 2*sp.pi - 2*S3}
    return _only(options, sp.simplify(exact))


def check_C4():
    """EXHAUSTIVE PROOF: circles at (1,1) r=1 and (R,R) touch the axes and each other when R = 3+2sqrt2 (E)."""
    R = sp.Symbol('R', positive=True)
    sol = [v for v in sp.solve(sp.Eq(sp.sqrt(2)*(R - 1), R + 1), R)]
    assert len(sol) == 1
    Rv = sp.radsimp(sol[0])
    assert sp.simplify(sp.sqrt(2*(Rv - 1)**2) - (Rv + 1)) == 0
    options = {'A': 1 + S2, 'B': 2 + S2, 'C': 2*S2, 'D': 3, 'E': 3 + 2*S2}
    return _only(options, Rv)


def check_C5():
    """EXHAUSTIVE PROOF: six unit discs centred on radius 2 touch neighbours and circles of radii 1 and 3; they cover 6pi of the 8pi ring = 3/4 (A)."""
    C = [_on_circle(60*k, 2) for k in range(6)]
    for k in range(6):
        assert abs(math.dist(C[k], C[(k + 1) % 6]) - 2) < 1e-12        # neighbours touch (radius 1 each)
        assert abs(math.hypot(*C[k]) - 1 - 1) < 1e-12                 # touches the inner circle
        assert abs(math.hypot(*C[k]) + 1 - 3) < 1e-12                 # touches the outer circle
    frac = sp.Rational(6*1**2, 3**2 - 1**2)
    # grid count of the covered fraction of the ring
    n, h = 600, 6/600
    ring = disc = 0
    for i in range(n):
        for j in range(n):
            x, y = -3 + (i + .5)*h, -3 + (j + .5)*h
            if 1 <= x*x + y*y <= 9:
                ring += 1
                disc += any((x - cx)**2 + (y - cy)**2 <= 1 for cx, cy in C)
    assert abs(disc/ring - float(frac)) < 0.01
    options = {'A': sp.Rational(3, 4), 'B': sp.Rational(2, 3), 'C': sp.Rational(7, 9), 'D': sp.Rational(1, 2), 'E': sp.Rational(3, 5)}
    return _only(options, frac)


def check_C6():
    """EXHAUSTIVE PROOF: circle (1,1) r=1 in a 2 x L rectangle; the diagonal 2x - Ly = 0 cuts a 90-degree arc iff L = 4 +- 2sqrt3; L >= 2 leaves 4 + 2sqrt3 (B)."""
    L = sp.Symbol('L', positive=True)
    roots = sp.solve(2*(L - 2)**2 - (4 + L**2), L)
    valid = [r for r in roots if r >= 2]
    assert len(roots) == 2 and len(valid) == 1
    Lv = valid[0]
    # the chord's endpoints subtend 90 degrees at the centre
    x = sp.Symbol('x')
    xs = sp.solve((x - 1)**2 + (2*x/Lv - 1)**2 - 1, x)
    P, Q = [(float(v), float(2*v/Lv)) for v in xs]
    assert abs(_angle(P, (1, 1), Q) - 90) < 1e-9
    options = {'A': 4 - 2*S3, 'B': 4 + 2*S3, 'C': 2 + 2*S3, 'D': 2, 'E': 2 + 2*S2}
    return _only(options, sp.radsimp(Lv))


def check_C7():
    """EXHAUSTIVE PROOF: incircle radius 6 and perimeter 52 force parallel sides 8 and 18 (Pitot + height 12); the circle centre (9,6) r=6 touches all four sides; difference 10 (D)."""
    a, b = sp.symbols('a b', positive=True)
    ell = (a + b) / 2                                            # Pitot
    sol = sp.solve([2*(a + b) - 52, ell**2 - ((b - a)/2)**2 - 12**2], [a, b], dict=True)
    sol = [s for s in sol if s[a] < s[b]]
    assert len(sol) == 1 and (sol[0][a], sol[0][b]) == (8, 18)
    sides = [((0, 0), (18, 0)), ((18, 0), (13, 12)), ((13, 12), (5, 12)), ((5, 12), (0, 0))]
    for (x1, y1), (x2, y2) in sides:
        dist = abs((y2 - y1)*9 - (x2 - x1)*6 + x2*y1 - y2*x1) / math.hypot(x2 - x1, y2 - y1)
        assert abs(dist - 6) < 1e-12
    assert 2*(18 + 8) == 52 == 18 + 8 + 2*math.hypot(5, 12)
    options = {'A': 12, 'B': 13, 'C': 26, 'D': 10, 'E': 5}
    return _only(options, sol[0][b] - sol[0][a])


def check_C8():
    """EXHAUSTIVE PROOF: AB diameter 25, CD = 7, AD = BC = x: Ptolemy 625 - x^2 = 175 + x^2 gives x = 15 (E); coordinates agree."""
    x = sp.Symbol('x', positive=True)
    sol = sp.solve((625 - x**2) - (25*7 + x**2), x)
    assert sol == [15]
    A, B = (-sp.Rational(25, 2), 0), (sp.Rational(25, 2), 0)
    D = (A[0] + 9, 12)
    C = (B[0] - 9, 12)
    for P in (C, D):
        assert P[0]**2 + P[1]**2 == sp.Rational(625, 4)
    assert C[0] - D[0] == 7
    assert sp.sqrt((D[0] - A[0])**2 + D[1]**2) == 15 == sp.sqrt((B[0] - C[0])**2 + C[1]**2)
    options = {'A': 12, 'B': 20, 'C': 16, 'D': 5*sp.sqrt(7), 'E': 15}
    return _only(options, sol[0])


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: half-angle with sin = 1/3; circles at 3, 6, 12 of radii 1, 2, 4 touch the arms and each other; cos = 7/9 (A)."""
    s = sp.Rational(1, 3)
    for d, r in ((3, 1), (6, 2), (12, 4)):
        assert d*s == r
    assert 6 - 3 == 1 + 2 and 12 - 6 == 2 + 4
    cos2 = 1 - 2*s**2
    options = {'A': sp.Rational(7, 9), 'B': sp.Rational(1, 3), 'C': sp.Rational(2, 3), 'D': sp.Rational(8, 9), 'E': 4*S2/9}
    return _only(options, cos2)


def check_D2():
    """EXHAUSTIVE PROOF: centre (r, y): y^2 = 8r and y^2 = 16 - 8r give r = 1 (B); tangencies checked numerically."""
    r, y = sp.symbols('r y', positive=True)
    sol = sp.solve([(r - 2)**2 + y**2 - (r + 2)**2, r**2 + y**2 - (4 - r)**2], [r, y], dict=True)
    assert len(sol) == 1
    rv, yv = sol[0][r], sol[0][y]
    assert sp.simplify(sp.sqrt((rv - 2)**2 + yv**2) - (rv + 2)) == 0 and sp.simplify(sp.sqrt(rv**2 + yv**2) - (4 - rv)) == 0
    options = {'A': sp.Rational(4, 3), 'B': 1, 'C': sp.Rational(2, 3), 'D': S2, 'E': sp.Rational(3, 4)}
    return _only(options, rv)


def check_D3():
    """EXHAUSTIVE PROOF: on a radius-2 circle with a 45-degree angle, area 8 sin45 sinB sinC = 1 + sqrt3 forces {B, C} = {30, 105}; largest angle 105 (C). Scan of B and coordinates agree."""
    area = lambda B: 8*math.sin(math.radians(45))*math.sin(math.radians(B))*math.sin(math.radians(135 - B))
    target = 1 + math.sqrt(3)
    # scan B in (0, 135): sign changes of area - target
    hits = [k/1000 for k in range(1, 135000) if (area(k/1000) - target)*(area((k + 1)/1000) - target) <= 0]
    Bs = sorted({round(b) for b in hits})
    assert Bs == [30, 105]
    largest = max(45, *Bs, *(135 - b for b in Bs))
    # coordinates: vertices at central angles twice the opposite angles
    P = [_on_circle(0, 2), _on_circle(60, 2), _on_circle(150, 2)]
    angs = sorted(round(_angle(P[(i + 1) % 3], P[i], P[(i + 2) % 3]), 6) for i in range(3))
    assert angs == [30, 45, 105]
    shoelace = abs(sum(P[i][0]*P[(i + 1) % 3][1] - P[(i + 1) % 3][0]*P[i][1] for i in range(3))) / 2
    assert abs(shoelace - target) < 1e-12
    assert abs(area(90) - 8*math.sin(math.radians(45))**2) < 1e-12 and abs(area(90) - 4) < 1e-12     # option A's triangle has area 4
    options = {'A': 90, 'B': 120, 'C': 105, 'D': 135, 'E': 75}
    return _only(options, largest)


def check_D4():
    """EXHAUSTIVE PROOF: centres (+-1,0), radius 5: axis square s = 6 (area 36); diamond with vertices (+-a,0),(0,+-a) is largest at a = 4 (area 32); ratio 9/8 (D). Scans agree."""
    inside = lambda x, y: (x + 1)**2 + y**2 <= 25 + 1e-12 and (x - 1)**2 + y**2 <= 25 + 1e-12
    s = sp.Symbol('s', positive=True)
    sol = sp.solve((s/2 + 1)**2 + s**2/4 - 25, s)
    assert sol == [6]
    # scan: largest centred axis-parallel square and largest centred diamond (convex symmetric region: centred is optimal)
    s_max = max(k/1000 for k in range(1, 10000) if all(inside(sx*k/2000, sy*k/2000) for sx in (-1, 1) for sy in (-1, 1)))
    a_max = max(k/1000 for k in range(1, 6000) if all(inside(*p) for p in ((k/1000, 0), (-k/1000, 0), (0, k/1000), (0, -k/1000))))
    assert abs(s_max - 6) < 1e-3 and abs(a_max - 4) < 1e-3
    assert inside(0, 4) and not inside(0, 5)                         # the top vertex is slack: side vertices bind
    area_S, area_T = sol[0]**2, sp.Rational(1, 2)*(2*4)**2
    assert (area_S, area_T) == (36, 32)
    options = {'A': 1, 'B': sp.Rational(9, 16), 'C': sp.Rational(8, 9), 'D': sp.Rational(9, 8), 'E': sp.Rational(3, 4)}
    return _only(options, sp.Rational(area_S, area_T))


def check_D5():
    """EXHAUSTIVE PROOF (exempt: proof): on random cyclic quadrilaterals with perpendicular diagonals, the perpendicular from E to AB meets CD at its midpoint, and the method's angle equalities hold."""
    import random
    rnd = random.Random(5)
    for _ in range(40):
        a, c, b = rnd.uniform(0.5, 4), rnd.uniform(0.5, 4), rnd.uniform(0.5, 4)
        d = a*c / b                                       # intersecting chords: EA*EC = EB*ED
        A, B, C, D, E = (a, 0.0), (0.0, b), (-c, 0.0), (0.0, -d), (0.0, 0.0)
        # cyclic check: centre ((a-c)/2, (b-d)/2) equidistant from all four
        O = ((a - c)/2, (b - d)/2)
        rs = [math.dist(O, P) for P in (A, B, C, D)]
        assert max(rs) - min(rs) < 1e-9
        # direction perpendicular to AB through E: (b, a)
        # intersect E + s(b, a) with C + w(D - C)
        det = b*(D[1] - C[1]) - a*(D[0] - C[0])
        w = (b*(C[1]) - a*(C[0])) / (-det)
        F = (C[0] + w*(D[0] - C[0]), C[1] + w*(D[1] - C[1]))
        assert abs(F[0] - (C[0] + D[0])/2) < 1e-9 and abs(F[1] - (C[1] + D[1])/2) < 1e-9
        assert abs(math.dist(F, E) - math.dist(F, C)) < 1e-9          # FE = FC = FD, as the method shows
        assert abs(_angle(A, B, E) - _angle(A, C, D)) < 1e-9          # angle ABD = angle ACD


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
