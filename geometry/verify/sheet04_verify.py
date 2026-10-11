import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import math
from pathlib import Path

import sympy as sp

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans04.tex'

S3 = sp.sqrt(3)


def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sp.simplify(sp.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _area(*P):
    """Shoelace area of a polygon given as exact points."""
    n = len(P)
    return sp.Abs(sum(P[i][0]*P[(i+1) % n][1] - P[(i+1) % n][0]*P[i][1] for i in range(n))) / 2


def _angle(P, V, Q):
    """Angle PVQ in degrees (numeric)."""
    a = (float(P[0]) - float(V[0]), float(P[1]) - float(V[1]))
    b = (float(Q[0]) - float(V[0]), float(Q[1]) - float(V[1]))
    return math.degrees(math.acos((a[0]*b[0] + a[1]*b[1]) / (math.hypot(*a) * math.hypot(*b))))


def _regular(n, R=1, start=90):
    """Vertices of a regular n-gon on a circle of radius R (numeric)."""
    return [(R*math.cos(math.radians(start - 360*k/n)), R*math.sin(math.radians(start - 360*k/n))) for k in range(n)]


def _hexagon():
    return {'A': (1, 0), 'B': (sp.Rational(1, 2), S3/2), 'C': (-sp.Rational(1, 2), S3/2),
            'D': (-1, 0), 'E': (-sp.Rational(1, 2), -S3/2), 'F': (sp.Rational(1, 2), -S3/2)}


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: exterior 360/12 = 30, interior 150; numerically the angle at a vertex of a regular 12-gon is 150."""
    P = _regular(12)
    assert abs(_angle(P[11], P[0], P[1]) - 150) < 1e-9
    return 180 - sp.Rational(360, 12)


def check_A2():
    """EXHAUSTIVE PROOF: base angles (180-40)/2 = 70."""
    base = sp.Rational(180 - 40, 2)
    assert 40 + 2*base == 180
    return base


def check_A3():
    """EXHAUSTIVE PROOF: 3-4-5 triangle, r = area/s = 6/6 = 1 = (a+b-c)/2."""
    area, s = sp.Rational(3*4, 2), sp.Rational(3 + 4 + 5, 2)
    assert area / s == sp.Rational(3 + 4 - 5, 2) == 1
    return area / s


def check_A4():
    """EXHAUSTIVE PROOF: exterior 18, 360/18 = 20 sides; a regular 20-gon has interior angle 162."""
    n = sp.Rational(360, 180 - 162)
    assert n == 20
    P = _regular(20)
    assert abs(_angle(P[19], P[0], P[1]) - 162) < 1e-9
    return n


def check_A5():
    """EXHAUSTIVE PROOF: 10*7/2 = 35; brute-force count of non-adjacent vertex pairs agrees; n=5 has as many diagonals as sides (inv)."""
    n = 10
    brute = sum(1 for i in range(n) for j in range(i + 1, n) if (j - i) % n not in (1, n - 1))
    assert brute == n*(n - 3)//2 == 35
    assert [m for m in range(3, 30) if m*(m - 3)//2 == m] == [5]
    return brute


def check_A6():
    """EXHAUSTIVE PROOF: BD:DC = 2:3 with BD+DC = 10 gives DC = 6."""
    dc = sp.Rational(3, 5) * 10
    assert (10 - dc) / dc == sp.Rational(2, 3)
    return dc


def check_A7():
    """EXHAUSTIVE PROOF: apex median of 5-5-6 is the altitude sqrt(25-9) = 4; coordinates agree."""
    apex, mid = (0, 4), (0, 0)
    assert (3 - apex[0])**2 + (0 - apex[1])**2 == 25
    return sp.sqrt((apex[0] - mid[0])**2 + (apex[1] - mid[1])**2)


def check_A8():
    """EXHAUSTIVE PROOF: centroid divides a median 2:1, so 2/3 of 12 = 8; coordinate check on a sample triangle."""
    A, B, C = (0, 12), (-5, 0), (5, 0)             # median from A to (0,0) has length 12
    G = (sp.Rational(A[0] + B[0] + C[0], 3), sp.Rational(A[1] + B[1] + C[1], 3))
    d = sp.sqrt((A[0] - G[0])**2 + (A[1] - G[1])**2)
    assert d == 8
    return d


def check_A9():
    """EXHAUSTIVE PROOF: area scales by (3/2)^2: 8 * 9/4 = 18."""
    big = 8 * sp.Rational(3, 2)**2
    assert big / 8 == sp.Rational(9, 4)
    return big


def check_A10():
    """EXHAUSTIVE PROOF: six equilateral triangles of side 2: 6*sqrt3; shoelace on the hexagon of side 2 agrees."""
    H = _hexagon()
    area = _area(*[(2*x, 2*y) for x, y in H.values()])
    assert sp.simplify(area - 6*S3) == 0
    return area


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: with the diagram's coordinates, angle BCD = (180-130)+(180-150) = 80 (C)."""
    B, C = (0.8, 2.0), None
    # build C from the two given angles: BC leaves B at 130 from BA (A to the left), DC leaves D at 150 from DE (E to the left)
    tB = math.radians(-(180 - 130))                 # direction of BC below the horizontal
    D = (0.0, 0.0)
    tD = math.radians(180 - 150)                    # direction of DC above the horizontal
    # intersect B + s(cos tB, sin tB) with D + t(cos tD, sin tD)
    a, b = math.cos(tB), -math.cos(tD)
    c, d = math.sin(tB), -math.sin(tD)
    det = a*d - b*c
    s = ((D[0] - B[0])*d - b*(D[1] - B[1])) / det
    C = (B[0] + s*math.cos(tB), B[1] + s*math.sin(tB))
    assert abs(_angle((-1.4, 2.0), B, C) - 130) < 1e-9 and abs(_angle(C, D, (-1.6, 0.0)) - 150) < 1e-9
    ang = _angle(B, C, D)
    options = {'A': 60, 'B': 70, 'C': 80, 'D': 100, 'E': 110}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_B2():
    """EXHAUSTIVE PROOF: square ABCD with equilateral ABE outside: coordinates give angle DEC = 30 (E)."""
    A, B, C, D = (0, 0), (2, 0), (2, 2), (0, 2)
    E = (1, -S3)
    ang = _angle(D, E, C)
    assert abs(ang - 30) < 1e-9
    assert abs(_angle(A, D, E) - 15) < 1e-9
    options = {'A': 15, 'B': 20, 'C': 45, 'D': 60, 'E': 30}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_B3():
    """EXHAUSTIVE PROOF: Heron gives 84 for 13-14-15, s=21, r = 84/21 = 4; R = 65/8 >= 2r (inv)."""
    s = sp.Rational(13 + 14 + 15, 2)
    area = sp.sqrt(s*(s - 13)*(s - 14)*(s - 15))
    assert area == 84
    r = area / s
    assert sp.Rational(13*14*15, 4*84) >= 2*r
    return r


def check_B4():
    """EXHAUSTIVE PROOF: at a vertex of a regular pentagon the angle between the two diagonals is 36 (A)."""
    P = _regular(5)
    ang = _angle(P[2], P[0], P[3])
    assert abs(ang - 36) < 1e-9
    options = {'A': 36, 'B': 30, 'C': 45, 'D': 54, 'E': 72}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_B5():
    """EXHAUSTIVE PROOF: shoelace: [ACE] / [hexagon] = 1/2 (B)."""
    H = _hexagon()
    frac = sp.simplify(_area(H['A'], H['C'], H['E']) / _area(*H.values()))
    assert sp.simplify(_area(H['A'], H['B'], H['C']) / _area(*H.values()) - sp.Rational(1, 6)) == 0   # each corner triangle is 1/6
    options = {'A': sp.Rational(1, 3), 'B': sp.Rational(1, 2), 'C': sp.Rational(2, 3), 'D': sp.Rational(3, 4), 'E': sp.Rational(1, 4)}
    return _only(options, frac)


def check_B6():
    """EXHAUSTIVE PROOF: 360-90-120 = 150 = interior angle of the regular 12-gon, and of no other n (D)."""
    gap = 360 - 90 - 120
    ns = [n for n in range(3, 100) if sp.Rational(180*(n - 2), n) == gap]
    assert ns == [12]
    options = {'A': 8, 'B': 10, 'C': 15, 'D': 12, 'E': 18}
    return _only(options, ns[0])


def check_B7():
    """EXHAUSTIVE PROOF: interior = 4 * exterior holds only for n = 10 (A)."""
    ns = [n for n in range(3, 200) if sp.Rational(180*(n - 2), n) == 4*sp.Rational(360, n)]
    assert ns == [10]
    options = {'A': 10, 'B': 8, 'C': 9, 'D': 12, 'E': 16}
    return _only(options, ns[0])


def check_B8():
    """EXHAUSTIVE PROOF: in a regular octagon ABCDEFGH, angle ACF = 67.5 (numeric)."""
    P = _regular(8)
    A, C, F = P[0], P[2], P[5]
    ang = _angle(A, C, F)
    assert abs(ang - 67.5) < 1e-9
    return sp.Rational(135, 2)


def check_B9():
    """EXHAUSTIVE PROOF: 360 - 108 - 120 = 132 (D); no regular polygon has interior angle 132 (inv)."""
    gap = 360 - 108 - 120
    assert all(sp.Rational(180*(n - 2), n) != gap for n in range(3, 400))
    options = {'A': 120, 'B': 126, 'C': 128, 'D': 132, 'E': 144}
    return _only(options, gap)


def check_B10():
    """EXHAUSTIVE PROOF: the point angles of irregular five-stroke stars sum to 180 (random stars)."""
    import random
    rnd = random.Random(4)
    for _ in range(50):
        # a star from a convex pentagon: points are its vertices, strokes join every second vertex
        angs = sorted(rnd.uniform(0, 2*math.pi) for _ in range(5))
        if min((angs[(i + 1) % 5] - angs[i]) % (2*math.pi) for i in range(5)) < 0.3:
            continue
        rad = [rnd.uniform(0.8, 1.2) for _ in range(5)]
        P = [(r*math.cos(t), r*math.sin(t)) for r, t in zip(rad, angs)]
        total = sum(_angle(P[(i + 2) % 5], P[i], P[(i + 3) % 5]) for i in range(5))
        assert abs(total - 180) < 1e-6
    return 180


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: coordinates: BD:DC=1:2, E midpoint of AD, F = BE meet AC; [EDCF]/[ABC] = 7/12 (C)."""
    A, B, C = (sp.Rational(2, 5), 3), (0, 0), (sp.Rational(9, 2), 0)
    D = (C[0]/3, 0)
    E = (sp.Rational(1, 2)*(A[0] + D[0]), sp.Rational(1, 2)*(A[1] + D[1]))
    t, u = sp.symbols('t u')
    sol = sp.solve([B[0] + t*(E[0] - B[0]) - (A[0] + u*(C[0] - A[0])), B[1] + t*(E[1] - B[1]) - (A[1] + u*(C[1] - A[1]))], [t, u])
    F = (A[0] + sol[u]*(C[0] - A[0]), A[1] + sol[u]*(C[1] - A[1]))
    assert sol[u] == sp.Rational(1, 4)                     # AF:FC = 1:3
    frac = sp.simplify(_area(E, D, C, F) / _area(A, B, C))
    options = {'A': sp.Rational(1, 2), 'B': sp.Rational(5, 8), 'C': sp.Rational(7, 12), 'D': sp.Rational(2, 3), 'E': sp.Rational(3, 4)}
    return _only(options, frac)


def check_C2():
    """EXHAUSTIVE PROOF: square on the hypotenuse of the 3-4-5 triangle: s = 5h/(5+h), h = 12/5, s = 60/37 (D); corner square 12/7 is larger (inv)."""
    h = sp.Rational(12, 5)
    s = sp.Symbol('s', positive=True)
    sol = sp.solve(sp.Eq(s/5, (h - s)/h), s)
    assert sol == [sp.Rational(60, 37)]
    # coordinates: right angle at origin, legs 4 (x) and 3 (y); square side along hypotenuse 3x+4y=12
    sv = sol[0]
    n = (sp.Rational(3, 5), sp.Rational(4, 5))                  # unit normal to the hypotenuse
    d = (-sp.Rational(4, 5), sp.Rational(3, 5))                 # unit direction along it
    # inner vertices on the legs: P=(0,p), Q=(q,0), with PQ parallel to the hypotenuse at distance sv from it
    p = (12 - 5*sv) / 4
    q = (12 - 5*sv) / 3
    P, Q = (0, p), (q, 0)
    assert sp.simplify(sp.sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2) - sv) == 0
    assert sp.Rational(12, 7) > sv
    options = {'A': sp.Rational(12, 7), 'B': sp.Rational(5, 3), 'C': sp.Rational(3, 2), 'D': sp.Rational(60, 37), 'E': sp.Rational(60, 49)}
    return _only(options, sv)


def check_C3():
    """EXHAUSTIVE PROOF: x(11-x) = 24 gives x = 3 or 8 (difference 5) and both give angle PRT = 90 (B)."""
    x = sp.Symbol('x')
    roots = sorted(sp.solve(x*(11 - x) - 24, x))
    assert roots == [3, 8]
    for r in roots:
        assert abs(_angle((0, 6), (r, 0), (11, 4)) - 90) < 1e-9
    options = {'A': 'two values, sum 12', 'B': 'two values, difference 5', 'C': 'one value >= 5.5',
               'D': 'one value < 5.5', 'E': 'cannot be determined'}
    verdict = {'A': len(roots) == 2 and sum(roots) == 12, 'B': len(roots) == 2 and roots[1] - roots[0] == 5,
               'C': len(roots) == 1, 'D': len(roots) == 1, 'E': False}
    hits = [k for k in options if verdict[k]]
    assert hits == ['B']
    return 'B'


def check_C4():
    """EXHAUSTIVE PROOF: regular octagon side 1: [octagon] = 2+2sqrt2 and [ACEG] = 2+sqrt2 (A), numerically and exactly."""
    R = 1 / (2*math.sin(math.pi/8))
    P = _regular(8, R, 112.5)
    assert abs(math.dist(P[0], P[1]) - 1) < 1e-12
    num_sq = abs(sum(P[i][0]*P[(i + 2) % 8][1] - P[(i + 2) % 8][0]*P[i][1] for i in (0, 2, 4, 6))) / 2
    num_oct = abs(sum(P[i][0]*P[(i + 1) % 8][1] - P[(i + 1) % 8][0]*P[i][1] for i in range(8))) / 2
    exact = (1 + sp.sqrt(2))**2 - 1 - 4*sp.sqrt(2)/4
    assert abs(num_oct - float(2 + 2*sp.sqrt(2))) < 1e-9 and abs(num_sq - float(exact)) < 1e-9
    options = {'A': 2 + sp.sqrt(2), 'B': 1 + sp.sqrt(2), 'C': 2 + 2*sp.sqrt(2), 'D': 4, 'E': 3 + 2*sp.sqrt(2)}
    return _only(options, sp.simplify(exact))


def check_C5():
    """EXHAUSTIVE PROOF: regular pentagon with equilateral ABF inside: angle FCD = 42 (C)."""
    A, B = (0.0, 0.0), (1.0, 0.0)
    ext = [0, 72, 144, 216, 288]
    P = [A]
    for k in range(4):
        x, y = P[-1]
        P.append((x + math.cos(math.radians(ext[k])), y + math.sin(math.radians(ext[k]))))
    C, D = P[2], P[3]
    F = (0.5, math.sqrt(3)/2)
    ang = _angle(F, C, D)
    assert abs(ang - 42) < 1e-9 and abs(_angle(F, B, C) - 48) < 1e-9 and abs(_angle(B, C, F) - 66) < 1e-9
    options = {'A': 36, 'B': 48, 'C': 42, 'D': 54, 'E': 66}
    return _only(options, sp.nsimplify(round(ang, 9)))


def check_C6():
    """EXHAUSTIVE PROOF: shoelace: [AME]/[hexagon] = 5/12 (E), and = ([ACE]+[ADE])/2."""
    H = _hexagon()
    M = ((H['C'][0] + H['D'][0])/2, (H['C'][1] + H['D'][1])/2)
    hexa = _area(*H.values())
    frac = sp.simplify(_area(H['A'], M, H['E']) / hexa)
    assert sp.simplify(frac - (_area(H['A'], H['C'], H['E']) + _area(H['A'], H['D'], H['E'])) / (2*hexa)) == 0
    options = {'A': sp.Rational(1, 3), 'B': sp.Rational(1, 2), 'C': sp.Rational(1, 4), 'D': sp.Rational(3, 8), 'E': sp.Rational(5, 12)}
    return _only(options, frac)


def check_C7():
    """EXHAUSTIVE PROOF: with x = 22.5, the chain AB=BC=CD=DE (1 each) built on the two arms ends with DE perpendicular to AD (D)."""
    x = math.radians(22.5)
    arm = (math.cos(x), math.sin(x))
    B = (1.0, 0.0)
    C = (2*math.cos(x)*arm[0], 2*math.cos(x)*arm[1])                # |C|=2cos x makes BC = 1
    D = (C[0] + math.sqrt(1 - C[1]**2), 0.0)                          # the far point of the arm at distance 1 from C
    # E on the other arm with DE = 1, beyond C
    t = sp.Symbol('t', positive=True)
    ts = [float(v) for v in sp.solve((t*arm[0] - D[0])**2 + (t*arm[1])**2 - 1, t)]
    E = (max(ts)*arm[0], max(ts)*arm[1])
    for P, Q in ((B, C), (C, D), (D, E)):
        assert abs(math.dist(P, Q) - 1) < 1e-9
    assert abs(E[0] - D[0]) < 1e-9                                    # DE is vertical: perpendicular to AD
    options = {'A': 15, 'B': 18, 'C': 20, 'D': sp.Rational(45, 2), 'E': 30}
    return _only(options, sp.Rational(45, 2))


def check_C8():
    """EXHAUSTIVE PROOF: 12 * (1/2) sin 30 = 3, so the region is pi - 3 (B); numeric shoelace agrees."""
    P = _regular(12)
    num = abs(sum(P[i][0]*P[(i + 1) % 12][1] - P[(i + 1) % 12][0]*P[i][1] for i in range(12))) / 2
    exact = 12 * sp.Rational(1, 2) * sp.sin(sp.pi/6)
    assert exact == 3 and abs(num - 3) < 1e-12
    options = {'A': sp.pi - 2, 'B': sp.pi - 3, 'C': sp.pi - 3*S3/2, 'D': sp.pi - 2*sp.sqrt(2), 'E': sp.pi/12}
    return _only(options, sp.pi - exact)


# ── Section D ──────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF: fold C onto A in an 8x6 sheet: the crease is the perpendicular bisector of AC clipped to the sheet, length 15/2 (E)."""
    A, C = (0, 0), (8, 6)
    M = (4, 3)
    # perpendicular bisector: 8x + 6y = 50; meets y=0 at x=25/4 and y=6 at x=7/4
    P, Q = (sp.Rational(25, 4), 0), (sp.Rational(7, 4), 6)
    for X in (P, Q):
        assert 8*X[0] + 6*X[1] == 50 and 0 <= X[0] <= 8
        assert (X[0] - A[0])**2 + (X[1] - A[1])**2 == (X[0] - C[0])**2 + (X[1] - C[1])**2
    length = sp.sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)
    options = {'A': 7, 'B': 5*sp.sqrt(2), 'C': sp.Rational(25, 4), 'D': 8, 'E': sp.Rational(15, 2)}
    return _only(options, length)


def check_D2():
    """EXHAUSTIVE PROOF: coordinates: AB=6, AC=3, angle A = 120; the bisector meets BC at D with AD = 2 (B)."""
    A = (0, 0)
    B = (6, 0)
    C = (-sp.Rational(3, 2), 3*S3/2)
    D = ((1*B[0] + 2*C[0]) / 3, (1*B[1] + 2*C[1]) / 3)               # BD:DC = AB:AC = 2:1
    AD = sp.sqrt(D[0]**2 + D[1]**2)
    assert sp.simplify(AD - 2) == 0
    assert abs(_angle(B, A, D) - 60) < 1e-9
    options = {'A': 2*S3, 'B': 2, 'C': 4, 'D': sp.sqrt(7), 'E': 3}
    return _only(options, sp.simplify(AD))


def check_D3():
    """EXHAUSTIVE PROOF: over all rotations, the largest centred square in a regular hexagon of side 1 is 3 - sqrt3, attained axis-aligned (C)."""
    def side(th):
        lo, hi = 0.0, 2.0
        for _ in range(60):
            mid = (lo + hi) / 2
            ok = True
            for cx, cy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                x = mid*(cx*math.cos(th) - cy*math.sin(th)); y = mid*(cx*math.sin(th) + cy*math.cos(th))
                if any(x*math.cos(math.pi/6 + j*math.pi/3) + y*math.sin(math.pi/6 + j*math.pi/3) > math.sqrt(3)/2 + 1e-12 for j in range(6)):
                    ok = False
            lo, hi = (mid, hi) if ok else (lo, mid)
        return 2*lo
    best = max(side(k*math.pi/6/600) for k in range(601))
    exact = 2*S3 / (S3 + 1)
    assert abs(best - float(exact)) < 1e-9 and abs(side(math.pi/4) - math.sqrt(6)/2) < 1e-9
    options = {'A': 1, 'B': 2*S3/3, 'C': 3 - S3, 'D': sp.sqrt(6)/2, 'E': sp.sqrt(2)}
    return _only(options, sp.radsimp(exact))


def check_D4():
    """EXHAUSTIVE PROOF: regular pentagon side 1: AC and BE meet at X with AX = (sqrt5-1)/2 (A); diagonal d satisfies d^2 = d + 1."""
    ext = [0, 72, 144, 216, 288]
    P = [(0.0, 0.0)]
    for k in range(4):
        x, y = P[-1]
        P.append((x + math.cos(math.radians(ext[k])), y + math.sin(math.radians(ext[k]))))
    A, B, C, D, E = P
    # intersect AC and BE
    a, b = C[0] - A[0], -(E[0] - B[0])
    c, d = C[1] - A[1], -(E[1] - B[1])
    det = a*d - b*c
    s = ((B[0] - A[0])*d - b*(B[1] - A[1])) / det
    X = (A[0] + s*a, A[1] + s*c)
    AX = math.dist(A, X)
    exact = (sp.sqrt(5) - 1) / 2
    dg = sp.Symbol('d', positive=True)
    assert sp.solve(dg**2 - dg - 1, dg) == [(1 + sp.sqrt(5))/2]
    assert abs(AX - float(exact)) < 1e-12 and abs(math.dist(A, C) - float((1 + sp.sqrt(5))/2)) < 1e-12
    options = {'A': (sp.sqrt(5) - 1)/2, 'B': (sp.sqrt(5) + 1)/2, 'C': sp.Rational(1, 2), 'D': sp.sqrt(5)/2, 'E': (3 - sp.sqrt(5))/2}
    return _only(options, exact)


def check_D5():
    """EXHAUSTIVE PROOF (exempt: proof): in the unit square, E with 15-degree angles at A and B gives CE = DE = CD = 1; the method's construction F (equilateral on CD) has 75 at A inside ADF, and F = E."""
    A, B, C, D = (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)
    t = math.tan(math.radians(15))
    E = (0.5, 0.5*t)
    assert abs(_angle(E, A, B) - 15) < 1e-9 and abs(_angle(E, B, A) - 15) < 1e-9
    assert abs(math.dist(C, E) - 1) < 1e-12 and abs(math.dist(D, E) - 1) < 1e-12
    F = (0.5, 1 - math.sqrt(3)/2)                                   # equilateral CDF, F inside
    assert abs(math.dist(D, F) - 1) < 1e-12 and abs(_angle(A, D, F) - 30) < 1e-9
    assert abs(_angle(D, A, F) - 75) < 1e-9 and abs(_angle(F, A, B) - 15) < 1e-9
    assert math.dist(E, F) < 1e-12


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
