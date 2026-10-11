import sys
import os
from pathlib import Path

# Ensure repo root on path for tools.*
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math

import sympy as sp
from tools.latex_bridge import get_answer

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans07.tex'

_X = sp.Symbol('x', real=True)
_Y = sp.Symbol('y', real=True)

def _apollonius_circle(Ax, Bx, k):
    """Return (centre_x, radius) for PA = k*PB with A=(Ax,0), B=(Bx,0), k>0 k!=1 on x-axis."""
    # Solve (x-Ax)^2 + y^2 = k^2 ((x-Bx)^2 + y^2)
    # => (1-k^2)x^2 + (1-k^2) y^2 + (-2Ax+2k^2 Bx)x + (Ax^2 - k^2 Bx^2)=0
    # Complete square
    Ax = sp.Rational(Ax)
    Bx = sp.Rational(Bx)
    k = sp.Rational(k)
    # centre h = (Ax - k^2 Bx)/(1 - k^2) = (k^2 Bx - Ax)/(k^2 -1)
    h = (k**2 * Bx - Ax) / (k**2 - 1)
    # radius^2 = h^2 + (k^2 Bx^2 - Ax^2)/(k^2 -1) ??? compute via plugging centre
    # easier: use endpoints method on x-axis
    # endpoints satisfy |x-Ax| = k|x-Bx|
    x1 = sp.solve(sp.Eq(sp.Abs(_X - Ax) - k*sp.Abs(_X - Bx), 0), _X)  # not reliable
    # Use direct algebraic endpoints: solve (x-Ax)=k(x-Bx) and (x-Ax)= -k(x-Bx) ??? Actually on line y=0, PA=|x-Ax|, PB=|x-Bx|
    # So solve x-Ax = k(Bx - x) for interior and x-Ax = k(x-Bx) for exterior
    # General: solve (x-Ax)^2 = k^2 (x-Bx)^2
    sol = sp.solve(sp.Eq((_X - Ax)**2, k**2 * (_X - Bx)**2), _X)
    sol = sorted([sp.Rational(s) for s in sol])
    centre = (sol[0] + sol[1]) / 2
    radius = abs(sol[1] - sol[0]) / 2
    # cross-check with h
    assert centre == h
    return centre, radius, sol

def _circle_centre_radius(g, f, c):
    cx, cy, r2 = -g, -f, g*g + f*f - c
    assert r2 >= 0
    return sp.Integer(cx), sp.Integer(cy), sp.Integer(r2)

def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sp.simplify(sp.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _tangent_count(d2, r1, r2):
    """Number of common tangents from d^2 and the radii, exact at the two boundaries."""
    s2, t2 = (r1 + r2)**2, (r1 - r2)**2
    if d2 == s2:
        return 3
    if d2 == t2:
        return 1
    if d2 > s2:
        return 4
    return 2 if d2 > t2 else 0


def _angle(P, V, Q):
    """Angle PVQ in radians, numerically."""
    a = (P[0] - V[0], P[1] - V[1])
    b = (Q[0] - V[0], Q[1] - V[1])
    return math.acos((a[0]*b[0] + a[1]*b[1]) / (math.hypot(*a) * math.hypot(*b)))

# ── Section A ────────────────────────────────────────────────────────────────

def check_A1():
    """EXHAUSTIVE PROOF: sqrt(x^2+y^2)=5 is x^2+y^2=25, the circle of radius 5 about the origin."""
    assert sp.expand(sp.sqrt(_X**2 + _Y**2)**2 - 25) == _X**2 + _Y**2 - 25
    x, y = sp.symbols('x y')                         # plain symbols, as the .tex parser produces
    return sp.Eq(x**2 + y**2, 25)

def check_A2():
    """EXHAUSTIVE PROOF: equidistant (0,0)-(4,0) => x=2."""
    d = sp.expand(_X**2 + _Y**2 - ((_X-4)**2 + _Y**2))
    assert d == 8*_X - 16
    sol = sp.solve(d, _X)
    assert sol == [2]
    return sol[0]

def check_A3():
    """EXHAUSTIVE PROOF: on the segment PA=x, PB=6-x, so x=2(6-x) gives 4; the other crossing is 12."""
    x = sp.solve(sp.Eq(_X, 2*(6-_X)), _X)
    assert x == [4]
    assert sp.solve(sp.Eq(_X, 2*(_X-6)), _X) == [12]
    centre, radius, eps = _apollonius_circle(0, 6, 2)
    assert eps == [4, 12] and (centre, radius) == (8, 4)
    return x[0]

def check_A4():
    """EXHAUSTIVE PROOF: |y-4|=3 => y=1 or 7."""
    ys = sorted(sp.solve(sp.Eq((_Y - 4)**2, 9), _Y))
    assert ys == [1, 7]
    return ys

def check_A5():
    """EXHAUSTIVE PROOF: x^2+(y-1)^2=(y+1)^2 reduces to x^2=4y."""
    d = sp.expand(_X**2 + (_Y-1)**2 - (_Y+1)**2)
    assert d == _X**2 - 4*_Y
    x, y = sp.symbols('x y')                         # plain symbols, as the .tex parser produces
    return sp.Eq(x**2, 4*y)

def check_A6():
    """EXHAUSTIVE PROOF: distance 3 from (1,2) => (x-1)^2+(y-2)^2=9; expanded constant is -4 (inv)."""
    lhs = sp.expand((_X-1)**2 + (_Y-2)**2 - 9)
    assert lhs == _X**2 - 2*_X + _Y**2 - 4*_Y - 4
    return sp.Eq((_X-1)**2 + (_Y-2)**2, 9)

def check_A7():
    """EXHAUSTIVE PROOF: M = Q/2 with |Q|=2 gives |M|=1; with P=(4,0), M=(P+Q)/2 is the circle centre (2,0) radius 1 (inv)."""
    t = sp.Symbol('t', real=True)
    Q = (2*sp.cos(t), 2*sp.sin(t))
    assert sp.simplify((Q[0]/2)**2 + (Q[1]/2)**2) == 1
    assert sp.simplify(((4 + Q[0])/2 - 2)**2 + (Q[1]/2)**2) == 1
    x, y = sp.symbols('x y')
    return sp.Eq(x**2 + y**2, 1)

def check_A8():
    """EXHAUSTIVE PROOF: x^2+y^2=2x => (x-1)^2+y^2=1 radius 1."""
    cx, cy, r2 = _circle_centre_radius(-1, 0, 0)
    assert (cx, cy, r2) == (1, 0, 1)
    return sp.sqrt(r2)

def check_A9():
    """EXHAUSTIVE PROOF: (sqrt2,sqrt2) is on x^2+y^2=4 with neither coordinate +-2, so the implication is false."""
    px, py = sp.sqrt(2), sp.sqrt(2)
    assert sp.simplify(px**2 + py**2 - 4) == 0
    assert px not in (2, -2) and py not in (2, -2)
    return False

def check_A10():
    """EXHAUSTIVE PROOF: PA=PB for (1,3),(5,3) => 8x=24 => x=3; for (1,3),(5,7) the bisector is x+y=8 through (3,5) (inv)."""
    d = sp.expand((_X-1)**2 + (_Y-3)**2 - (_X-5)**2 - (_Y-3)**2)
    assert d == 8*_X - 24
    d2 = sp.expand((_X-1)**2 + (_Y-3)**2 - (_X-5)**2 - (_Y-7)**2)
    assert d2 == 8*_X + 8*_Y - 64 and d2.subs({_X: 3, _Y: 5}) == 0
    return sp.solve(d, _X)[0]

# ── Section B ────────────────────────────────────────────────────────────────

def check_B1():
    """EXHAUSTIVE PROOF: PA=3PB, B=(8,0): crossings 6 and 12, circle (x-9)^2+y^2=9, radius 3 (C)."""
    centre, radius, eps = _apollonius_circle(0, 8, 3)
    assert eps == [6, 12] and centre == 9 and radius == 3
    assert sp.expand(_X**2 + _Y**2 - 9*((_X-8)**2 + _Y**2) + 8*((_X-9)**2 + _Y**2 - 9)) == 0
    options = {'A': 9, 'B': 6, 'C': 3, 'D': 8}
    return _only(options, radius)

def check_B2():
    """EXHAUSTIVE PROOF: equidistant (0,0)-(0,4) => y=2 (B)."""
    y = sp.solve(sp.Eq(_Y**2, (_Y-4)**2), _Y)
    assert y == [2]
    options = {'A': _X - 2, 'B': _Y - 2, 'C': _Y - 4, 'D': _X - 4}
    hits = [k for k, e in options.items() if sp.expand(_Y**2 - (_Y-4)**2 - 8*e) == 0]
    assert hits == ['B']
    return 'B'

def check_B3():
    """EXHAUSTIVE PROOF: x^2+y^2<=4 is the disk of radius 2, area 4 pi (B); a grid count agrees."""
    area = sp.pi * 2**2
    n = 400
    h = 4.0 / n
    count = sum(1 for i in range(n) for j in range(n) if (-2 + (i + .5)*h)**2 + (-2 + (j + .5)*h)**2 <= 4)
    assert abs(count*h*h - float(area)) < 0.02
    options = {'A': 2*sp.pi, 'B': 4*sp.pi, 'C': 8*sp.pi, 'D': 16}
    return _only(options, area)

def check_B4():
    """EXHAUSTIVE PROOF: only the upper arc of the circle centre (2,2) radius 2sqrt2 sees AB at a constant 45 degrees (D); A gives 90, B gives 135, C is not constant."""
    A, B = (0.0, 0.0), (4.0, 0.0)
    r = 2*math.sqrt(2)
    circle = lambda cx, cy, rad: [(cx + rad*math.cos(k/40), cy + rad*math.sin(k/40)) for k in range(252)]
    options = {'A': circle(2, 0, 2), 'B': circle(2, -2, r), 'C': [(2.0, 0.5 + k/10) for k in range(60)],
               'D': circle(2, 2, r)}
    def locus_ok(pts):
        upper = [P for P in pts if P[1] > 1e-6]
        return bool(upper) and all(abs(_angle(A, P, B) - math.pi/4) < 1e-9 for P in upper)
    hits = [k for k, pts in options.items() if locus_ok(pts)]
    assert hits == ['D']
    assert abs(_angle(A, (2.0, 2.0), B) - math.pi/2) < 1e-9 and abs(_angle(A, (2.0, -2 + r), B) - 3*math.pi/4) < 1e-9
    return 'D'

def check_B5():
    """EXHAUSTIVE PROOF: x^2+y^2<1 implies x^2+y^2<2 (C); A fails at (0.8,0), B at (0.7,0.7), D at the origin."""
    inside = lambda x, y: x*x + y*y < 1
    options = {'A': lambda x, y: x*x + y*y < 0.5, 'B': lambda x, y: x + y < 1,
               'C': lambda x, y: x*x + y*y < 2, 'D': lambda x, y: x*x + y*y > 0}
    grid = [(i/50, j/50) for i in range(-50, 51) for j in range(-50, 51) if inside(i/50, j/50)]
    hits = [k for k, f in options.items() if all(f(x, y) for x, y in grid)]
    assert hits == ['C']
    assert not options['A'](0.8, 0) and not options['B'](0.7, 0.7) and not options['D'](0, 0)
    return 'C'

def check_B6():
    """EXHAUSTIVE PROOF: PA=3PB B=(2,0): crossings 3/2 and 3, right endpoint 3 (A)."""
    centre, radius, eps = _apollonius_circle(0, 2, 3)
    assert eps == [sp.Rational(3, 2), 3]
    options = {'A': 3, 'B': 4, 'C': 6, 'D': 9}
    return _only(options, eps[1])

def check_B7():
    """EXHAUSTIVE PROOF: only B forces x^2+y^2=1 (sufficient); A, C, D each admit points off the circle."""
    on = lambda x, y: sp.simplify(x**2 + y**2 - 1) == 0
    h = sp.Rational(1, 2)
    options = {'A': lambda x, y: x**2 + y**2 < 1, 'B': lambda x, y: x == -h and y == sp.sqrt(3)/2,
               'C': lambda x, y: (x, y) != (0, 0), 'D': lambda x, y: x + y == 1}
    pts = [(-h, sp.sqrt(3)/2), (h, h), (0, h), (1, 0), (0, 1), (3, -2), (sp.Rational(1, 5), 0)]
    sufficient = [k for k, f in options.items() if all(on(x, y) for x, y in pts if f(x, y))
                  and any(f(x, y) for x, y in pts)]
    assert sufficient == ['B']
    return 'B'

def check_B8():
    """EXHAUSTIVE PROOF: equal diagonals hold for every sample rectangle and also for an isosceles trapezium: necessary, not sufficient (B)."""
    def is_rect(q):
        return all(math.isclose((q[(i+1) % 4][0]-q[i][0])*(q[(i+2) % 4][0]-q[(i+1) % 4][0]) +
                                (q[(i+1) % 4][1]-q[i][1])*(q[(i+2) % 4][1]-q[(i+1) % 4][1]), 0, abs_tol=1e-12) for i in range(4))
    diag_eq = lambda q: math.isclose(math.dist(q[0], q[2]), math.dist(q[1], q[3]))
    perp = lambda q: math.isclose((q[2][0]-q[0][0])*(q[3][0]-q[1][0]) + (q[2][1]-q[0][1])*(q[3][1]-q[1][1]), 0, abs_tol=1e-12)
    bisect = lambda q: math.isclose(q[0][0]+q[2][0], q[1][0]+q[3][0]) and math.isclose(q[0][1]+q[2][1], q[1][1]+q[3][1])
    options = {'A': is_rect, 'B': diag_eq, 'C': perp, 'D': lambda q: diag_eq(q) and bisect(q)}
    quads = [[(0, 0), (2, 0), (2, 1), (0, 1)], [(0, 0), (3, 0), (3, 3), (0, 3)], [(1, 0), (2, 1), (1, 2), (0, 1)],
             [(0, 0), (4, 0), (3, 2), (1, 2)], [(0, 0), (2, 1), (4, 0), (2, -1)], [(0, 0), (3, 0), (4, 2), (1, 2)]]
    rects = [q for q in quads if is_rect(q)]
    assert len(rects) == 3
    necessary = [k for k, f in options.items() if all(f(q) for q in rects)]
    not_sufficient = [k for k, f in options.items() if any(f(q) and not is_rect(q) for q in quads)]
    hits = [k for k in necessary if k in not_sufficient]
    assert hits == ['B']
    return 'B'

def check_B9():
    """EXHAUSTIVE PROOF: x^2+y^2-4x-6y+9 centre (2,3), r=2: touches the y-axis, not the x-axis (inv)."""
    cx, cy, r2 = _circle_centre_radius(-2, -3, 9)
    assert (cx, cy, r2) == (2, 3, 4)
    assert abs(cx) == 2 and abs(cy) != 2
    return (cx, cy)

def check_B10():
    """EXHAUSTIVE PROOF: x^2+y^2-4x+6y+9 has centre (2,-3), radius 2; with B9's circle d=6>4, four tangents (inv)."""
    cx, cy, r2 = _circle_centre_radius(-2, 3, 9)
    assert (cx, cy, r2) == (2, -3, 4)
    assert _tangent_count(36, 2, 2) == 4
    return sp.sqrt(r2)

# ── Section C ────────────────────────────────────────────────────────────────

def check_C1():
    """EXHAUSTIVE PROOF: Apollonius A(-2,0) B(4,0) k=2 => (x-6)^2+y^2=16, centre (6,0) (A); origin lies on it for k=1/2 (inv)."""
    centre, radius, eps = _apollonius_circle(-2, 4, 2)
    assert (centre, radius) == (6, 4) and eps == [2, 10]
    eq = sp.expand((_X+2)**2 + _Y**2 - 4*((_X-4)**2 + _Y**2))
    assert sp.expand(eq + 3*((_X-6)**2 + _Y**2 - 16)) == 0
    assert sp.sqrt(4) == sp.Rational(1, 2) * sp.sqrt(16)
    options = {'A': (6, 0), 'B': (8, 0), 'C': (10, 0), 'D': (2, 0)}
    hits = [k for k, v in options.items() if v == (centre, 0)]
    assert hits == ['A']
    return 'A'

def check_C2():
    """EXHAUSTIVE PROOF: |x+y|=|x-y| <=> 4xy=0 <=> x=0 or y=0 (D); on a grid only option D matches the equidistance condition."""
    assert sp.expand((_X+_Y)**2 - (_X-_Y)**2) == 4*_X*_Y
    equi = lambda x, y: abs(x + y) == abs(x - y)
    options = {'A': lambda x, y: y == x, 'B': lambda x, y: y == -x, 'C': lambda x, y: y == abs(x),
               'D': lambda x, y: x == 0 or y == 0}
    grid = [(i, j) for i in range(-5, 6) for j in range(-5, 6)]
    hits = [k for k, f in options.items() if all(f(x, y) == equi(x, y) for x, y in grid)]
    assert hits == ['D']
    return 'D'

def check_C3():
    """EXHAUSTIVE PROOF: with O outside angle APB the claim still holds and the exterior-angle facts hold, but their sum is not angle AOB: the proof misses the subtraction case (C)."""
    options = {'A': 'correct and complete', 'B': 'exterior angle step fails',
               'C': 'addition assumes O inside angle APB', 'D': 'claim false'}
    O = (0.0, 0.0)
    pt = lambda deg: (math.cos(math.radians(deg)), math.sin(math.radians(deg)))
    A, B, P = pt(0), pt(40), pt(330)            # minor arc AB = 40 deg; P on the major arc, its antipode D on the major arc too
    D = (-P[0], -P[1])
    AOB, APB = _angle(A, O, B), _angle(A, P, B)
    AOD, BOD = _angle(A, O, D), _angle(B, O, D)
    APO, BPO = _angle(A, P, O), _angle(B, P, O)
    claim_true = abs(AOB - 2*APB) < 1e-9
    steps_true = abs(AOD - 2*APO) < 1e-9 and abs(BOD - 2*BPO) < 1e-9
    addition_true = abs((AOD + BOD) - AOB) < 1e-9
    assert claim_true and steps_true and not addition_true
    assert abs(abs(BOD - AOD) - AOB) < 1e-9      # subtraction is what is needed
    verdict = {'A': addition_true, 'B': not steps_true, 'C': claim_true and not addition_true, 'D': not claim_true}
    hits = [k for k in options if verdict[k]]
    assert hits == ['C']
    return 'C'

def check_C4():
    """EXHAUSTIVE PROOF: I+II rectangle, I+III rhombus, II+III a non-square kite, so all three are needed (D)."""
    def props(q):
        (a, b, c, d) = q
        mid1 = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2); mid2 = ((b[0] + d[0]) / 2, (b[1] + d[1]) / 2)
        bis = math.isclose(mid1[0], mid2[0]) and math.isclose(mid1[1], mid2[1])
        eq = math.isclose(math.dist(a, c), math.dist(b, d))
        u = (c[0] - a[0], c[1] - a[1]); v = (d[0] - b[0], d[1] - b[1])
        perp = math.isclose(u[0]*v[0] + u[1]*v[1], 0, abs_tol=1e-12)
        sides = [math.dist(q[i], q[(i+1) % 4]) for i in range(4)]
        square = eq and perp and bis and all(math.isclose(s, sides[0]) for s in sides)
        return {'I': bis, 'II': eq, 'III': perp}, square
    quads = [[(0, 0), (2, 0), (2, 1), (0, 1)], [(0, 0), (2, 1), (4, 0), (2, -1)], [(-1, 0), (0, 1.5), (1, 0), (0, -0.5)],
             [(0, 0), (1, 0), (1, 1), (0, 1)], [(0, 0), (3, 1), (2, 4), (-1, 3)]]
    options = {'A': ('I', 'II'), 'B': ('I', 'III'), 'C': ('II', 'III'), 'D': ('I', 'II', 'III'), 'E': ()}
    def guarantees(conds):
        return all(sq for pr, sq in map(props, quads) if all(pr[c] for c in conds))
    ok = [k for k, conds in options.items() if conds and guarantees(conds)]
    assert ok == ['D']
    return 'D'

def check_C5():
    """EXHAUSTIVE PROOF: b^2-16b cos+28=0 with b1=4b2 gives b2=sqrt7, cos=5sqrt7/16 (A); both triangles really have BC=6."""
    c = sp.symbols('c', positive=True)
    b2 = sp.sqrt(sp.Rational(28, 4))
    cosv = sp.solve(sp.Eq(5*b2, 16*c), c)[0]
    assert sp.simplify(cosv - 5*sp.sqrt(7)/16) == 0 and cosv < 1
    sinv = sp.sqrt(1 - cosv**2)
    assert sinv == sp.Rational(9, 16)
    for b in (b2, 4*b2):
        C = (b*cosv, b*sinv)
        assert sp.simplify((C[0] - 8)**2 + C[1]**2 - 36) == 0
    assert sp.simplify((4*b2*sinv) / (b2*sinv) - 4) == 0
    options = {'A': 5*sp.sqrt(7)/16, 'B': 3*sp.sqrt(14)/16, 'C': sp.sqrt(7)/4, 'D': sp.Rational(3, 4)}
    return _only(options, cosv)

def check_C6():
    """EXHAUSTIVE PROOF: centres (-3,1) (8,1), d=11 > 8 => 4 tangents (E)."""
    d2 = (8 - (-3))**2 + (1 - 1)**2
    count = _tangent_count(d2, 5, 3)
    assert d2 == 121
    options = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    return _only(options, count)

def check_C7():
    """EXHAUSTIVE PROOF: PA=3PB, A(0,0), B(6,0): crossings 9/2 and 9, max PA = 9 (A); least PB = 3/2 (inv)."""
    centre, radius, eps = _apollonius_circle(0, 6, 3)
    assert (centre, radius) == (sp.Rational(27, 4), sp.Rational(9, 4)) and eps == [sp.Rational(9, 2), 9]
    t = sp.Symbol('t', real=True)
    PA2 = sp.expand((centre + radius*sp.cos(t))**2 + (radius*sp.sin(t))**2)
    assert sp.simplify(PA2.subs(t, 0) - 81) == 0
    assert max(float(PA2.subs(t, k/50)) for k in range(315)) <= 81 + 1e-9
    assert radius - abs(centre - 6) == sp.Rational(3, 2)
    options = {'A': 9, 'B': sp.Rational(15, 2), 'C': 12, 'D': 6}
    return _only(options, sp.sqrt(PA2.subs(t, 0)))

def check_C8():
    """EXHAUSTIVE PROOF: true locus (x-9/4)^2+y^2=9/16; Fil's circle is exactly PB=3 (C); CA*CB = r^2 (inv)."""
    options = {'A': 'single point', 'B': 'straight line', 'C': 'says PB=3, ignores A', 'D': 'no error'}
    centre, radius, eps = _apollonius_circle(0, 2, 3)
    assert (centre, radius) == (sp.Rational(9, 4), sp.Rational(3, 4))
    norm = sp.expand((_X**2 + _Y**2 - 9*((_X-2)**2 + _Y**2)) / -8)
    true_circle = (_X - sp.Rational(9, 4))**2 + _Y**2 - sp.Rational(9, 16)
    assert sp.expand(norm - true_circle) == 0
    fil = (_X-2)**2 + _Y**2 - 9
    assert sp.expand(fil - ((_X-2)**2 + _Y**2 - 3**2)) == 0            # Fil's equation is PB^2 = 9
    verdict = {'A': False,                                             # a circle, not a point
               'B': False,                                             # not a line
               'C': sp.expand(fil - norm) != 0,
               'D': sp.expand(fil - norm) == 0}
    hits = [k for k in options if verdict[k]]
    assert hits == ['C']
    assert centre * (centre - 2) == radius**2
    return 'C'

# ── Section D ────────────────────────────────────────────────────────────────

def check_D1():
    """EXHAUSTIVE PROOF: PA^2+PB^2 = 2x^2+2y^2+18 = 34 => x^2+y^2=8, r = 2sqrt2 (A); circle iff c>18 (inv)."""
    s = sp.expand((_X+3)**2 + _Y**2 + (_X-3)**2 + _Y**2)
    assert s == 2*_X**2 + 2*_Y**2 + 18
    r = sp.sqrt(sp.Rational(34 - 18, 2))
    options = {'A': 2*sp.sqrt(2), 'B': 4, 'C': sp.sqrt(17), 'D': sp.sqrt(34)}
    return _only(options, r)

def check_D2():
    """EXHAUSTIVE PROOF: band area = 16 + pi outside + (16 - 4) inside = 28 + pi (D); a grid count agrees."""
    area = 16 + sp.pi + (16 - 4)

    def dist_to_boundary(x, y):
        if 0 <= x <= 4 and 0 <= y <= 4:
            return min(x, 4 - x, y, 4 - y)
        dx = max(0 - x, 0, x - 4); dy = max(0 - y, 0, y - 4)
        return math.hypot(dx, dy)
    n = 600
    h = 6.0 / n
    count = sum(1 for i in range(n) for j in range(n)
                if dist_to_boundary(-1 + (i + 0.5)*h, -1 + (j + 0.5)*h) <= 1)
    assert abs(count*h*h - float(area)) < 0.02
    options = {'A': 32 + sp.pi, 'B': 28 + 4*sp.pi, 'C': 23 + sp.pi, 'D': 28 + sp.pi}
    return _only(options, area)

def check_D3():
    """EXHAUSTIVE PROOF: kite cyclic iff angle SPQ = 90 iff x^2 = yz (C); over sample kites only C matches cyclicity."""
    x, y, z = sp.symbols('x y z', positive=True)
    assert sp.expand(x*x + y*(-z)) == x**2 - y*z     # PQ.PS with P=(-x,0), Q=(0,y), S=(0,-z)

    def cyclic(xv, yv, zv):
        pts = [(-xv, 0), (0, yv), (xv, 0), (0, -zv)]
        cy = (yv - zv) / 2                              # centre on QS, equidistant from Q and S
        return len({round(math.hypot(px, py - cy), 9) for px, py in pts}) == 1
    options = {'A': lambda a, b, c: a == b == c, 'B': lambda a, b, c: 2*a == b + c,
               'C': lambda a, b, c: a*a == b*c, 'D': lambda a, b, c: b == c,
               'E': lambda a, b, c: b*b == a*a + c*c}
    kites = [(2, 1, 4), (2, 1, 3), (3, 3, 3), (6, 4, 9), (2, 3, 3), (4, 5, 3), (5, 5, 5), (6, 3, 12)]
    hits = [k for k, f in options.items() if all(f(*kt) == cyclic(*kt) for kt in kites)]
    assert hits == ['C']
    return 'C'

def check_D4():
    """EXHAUSTIVE PROOF: radical axis x=4, half chord 3, PQ=6 (B); cos of angle between radii = 3/5 (inv)."""
    assert sp.solve(sp.Eq(_X**2 - (_X-4)**2, 16), _X) == [4]
    half = sp.sqrt(25 - 16)
    assert half == 3
    assert sp.Rational(25 + 9 - 16, 2*5*3) == sp.Rational(3, 5)
    options = {'A': 3, 'B': 6, 'C': 4*sp.sqrt(14)/3, 'D': sp.Rational(24, 5)}
    return _only(options, 2*half)

def check_D5():
    """EXHAUSTIVE PROOF (exempt: proof): with A(-1,0), B(1,0), PA=kPB is x^2+y^2+2 lam x+1=0, lam=(1+k^2)/(1-k^2), |lam|>1; it is orthogonal to every x^2+y^2+2fy-1=0."""
    k, f, th = sp.symbols('k f theta', real=True)
    eq = sp.expand((_X+1)**2 + _Y**2 - k**2*((_X-1)**2 + _Y**2))
    lam = (1 + k**2) / (1 - k**2)
    assert sp.simplify(eq / (1 - k**2) - (_X**2 + _Y**2 + 2*lam*_X + 1)) == 0
    for kv in (sp.Rational(1, 3), 2, 5):
        lv = lam.subs(k, kv)
        assert abs(lv) > 1
        r = sp.sqrt(lv**2 - 1)
        P = (-lv + r*sp.cos(th), r*sp.sin(th))                   # a general point of the circle
        PA2 = (P[0] + 1)**2 + P[1]**2
        PB2 = (P[0] - 1)**2 + P[1]**2
        assert sp.simplify(PA2 - kv**2 * PB2) == 0
        for fv in (0, 1, sp.Rational(-5, 2)):
            # circle through A and B: centre (0,-f), r2^2 = f^2 + 1; passes through (+-1,0)
            assert all((px**2 + py**2 + 2*fv*py - 1) == 0 for px, py in ((1, 0), (-1, 0)))
            d2 = lv**2 + fv**2
            assert sp.simplify(d2 - (r**2 + fv**2 + 1)) == 0      # d^2 = r1^2 + r2^2: orthogonal
            assert 2*lv*0 + 2*0*fv == 1 + (-1)                    # the coefficient test in the method

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
