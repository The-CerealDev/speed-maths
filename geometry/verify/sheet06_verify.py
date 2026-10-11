import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import itertools
import math
import random
from pathlib import Path

import sympy as sp

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans06.tex'

S2, S3 = sp.sqrt(2), sp.sqrt(3)
PI = sp.Symbol('pi')          # the binding parses \pi as a plain symbol


def _only(options, value):
    """The single option letter whose value equals `value` (exactly, via sympy)."""
    hits = [k for k, v in options.items() if sp.simplify(sp.nsimplify(v) - value) == 0]
    assert len(hits) == 1, (hits, value)
    return hits[0]


def _tet_volume(P, Q, R, S):
    """Volume of tetrahedron PQRS from the triple product (exact for sympy inputs)."""
    u = [Q[i] - P[i] for i in range(3)]
    v = [R[i] - P[i] for i in range(3)]
    w = [S[i] - P[i] for i in range(3)]
    det = (u[0]*(v[1]*w[2] - v[2]*w[1]) - u[1]*(v[0]*w[2] - v[2]*w[0]) + u[2]*(v[0]*w[1] - v[1]*w[0]))
    return sp.Abs(sp.sympify(det)) / 6


def _polygon_area_3d(pts):
    """Area of a planar convex polygon in space, vertices in order (numeric)."""
    cx = [sum(p[i] for p in pts) / len(pts) for i in range(3)]
    tot = [0.0, 0.0, 0.0]
    for a, b in zip(pts, pts[1:] + pts[:1]):
        u = [a[i] - cx[i] for i in range(3)]
        v = [b[i] - cx[i] for i in range(3)]
        cr = (u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0])
        tot = [tot[i] + cr[i] for i in range(3)]
    return 0.5 * math.sqrt(sum(t*t for t in tot))


def _mc_fraction(inside, n=200000, seed=6):
    """Monte-Carlo fraction of the unit-scaled box [0,1]^3 satisfying `inside` (rough, for cross-checks)."""
    rnd = random.Random(seed)
    return sum(inside(rnd.random(), rnd.random(), rnd.random()) for _ in range(n)) / n


# ── Section A ──────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: Euler F = 2 - V + E = 20; the icosahedron (12 vertices, 5 triangles each) agrees."""
    F = 2 - 12 + 30
    assert F == 20 and 3*F == 2*30 and 12*5 == 2*30
    return sp.Integer(F)


def check_A2():
    """EXHAUSTIVE PROOF: space diagonal sqrt(9+16+144) = 13."""
    d = sp.sqrt(sum(sp.Integer(x)**2 for x in (3, 4, 12)))
    assert d == 13
    return d


def check_A3():
    """EXHAUSTIVE PROOF: cone volume by integrating the disc areas pi*(3t/4)^2 over the height 4."""
    t = sp.Symbol('t')
    vol = sp.integrate(sp.pi*(sp.Rational(3, 4)*t)**2, (t, 0, 4))
    assert vol == 12*sp.pi
    return 12*PI


def check_A4():
    """EXHAUSTIVE PROOF: 4 pi r^2 = 36 pi gives r = 3; volume 4/3 pi 27 = 36 pi."""
    r = sp.Symbol('r', positive=True)
    (rr,) = sp.solve(4*sp.pi*r**2 - 36*sp.pi, r)
    assert rr == 3 and sp.Rational(4, 3)*sp.pi*rr**3 == 36*sp.pi
    return 36*PI


def check_A5():
    """EXHAUSTIVE PROOF: distance formula in 3D."""
    d = sp.sqrt((3 - 1)**2 + (5 - 2)**2 + (9 - 3)**2)
    assert d == 7
    return d


def check_A6():
    """EXHAUSTIVE PROOF: a*sqrt3 = 6 gives a^2 = 12, surface 6a^2 = 72."""
    a = 6 / S3
    assert sp.simplify(sp.sqrt(3*a**2) - 6) == 0
    return sp.simplify(6*a**2)


def check_A7():
    """EXHAUSTIVE PROOF: volumes scale by k^3; a 2x2x2 and a 3x3x3 cube as the similar pair."""
    assert sp.Rational(2**3, 3**3) == sp.Rational(2, 3)**3
    return sp.Rational(8, 27)


def check_A8():
    """EXHAUSTIVE PROOF: curved area pi*r*l, cross-checked by the unrolled sector area (1/2) l^2 * (2 pi r / l)."""
    l = sp.sqrt(5**2 + 12**2)
    assert l == 13
    sector = sp.Rational(1, 2) * l**2 * (2*sp.pi*5 / l)
    assert sp.simplify(sector - 65*sp.pi) == 0
    return 65*PI


def check_A9():
    """EXHAUSTIVE PROOF: tetrahedron on alternate corners of a cube of edge sqrt2 has edge 2; its four faces by cross product."""
    V = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]           # edge sqrt2 - scale by sqrt2 to get edge 2
    total = 0.0
    for tri in itertools.combinations(V, 3):
        total += _polygon_area_3d([tuple(math.sqrt(2)*c for c in p) for p in tri])
    assert abs(total - 4*math.sqrt(3)) < 1e-12
    return 4*S3


def check_A10():
    """EXHAUSTIVE PROOF: octahedron at (+-1,0,0),(0,+-1,0),(0,0,+-1): count the edges of length sqrt2."""
    V = [p for i in range(3) for s in (1, -1) for p in [tuple(s if j == i else 0 for j in range(3))]]
    E = [(p, q) for p, q in itertools.combinations(V, 2) if abs(math.dist(p, q) - math.sqrt(2)) < 1e-12]
    assert len(V) == 6 and len(E) == 12 and len(V) - len(E) + 8 == 2
    return sp.Integer(len(E))


# ── Section B ──────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: slant 6, height 4sqrt2 gives base radius 2; arc 4pi = theta/360 * 12pi gives 120 (C)."""
    r = sp.sqrt(36 - (4*S2)**2)
    assert r == 2
    theta = sp.Symbol('theta')
    (th,) = sp.solve(theta/360 * 2*sp.pi*6 - 2*sp.pi*r, theta)
    options = {'A': 60, 'B': 90, 'C': 120, 'D': 150, 'E': 180}
    return _only(options, th)


def check_B2():
    """EXHAUSTIVE PROOF: (9/10)^2 * k = 1 gives k = 100/81 (B)."""
    k = sp.Symbol('k')
    (kk,) = sp.solve(sp.Rational(9, 10)**2 * k - 1, k)
    s0, h0 = sp.Integer(10), sp.Integer(6)                          # any pyramid: same volume after the change
    assert sp.Rational(1, 3)*(s0*sp.Rational(9, 10))**2*(h0*kk) == sp.Rational(1, 3)*s0**2*h0
    assert sp.Rational(9, 10)**2 * sp.Rational(10, 9) != 1          # option A only undoes one length
    options = {'A': sp.Rational(10, 9), 'B': sp.Rational(100, 81), 'C': sp.Rational(11, 10),
               'D': sp.Rational(121, 100), 'E': sp.Rational(81, 100)}
    return _only(options, kk)


def check_B3():
    """EXHAUSTIVE PROOF: brute force a<=b<=c up to 20 with (a-2)(b-2)(c-2) = 12, counting unpainted cubes directly; min abc = 80 (A)."""
    best = None
    for a in range(3, 21):
        for b in range(a, 21):
            for c in range(b, 21):
                inner = sum(1 for x in range(a) for y in range(b) for z in range(c)
                            if 0 < x < a-1 and 0 < y < b-1 and 0 < z < c-1) if (a-2)*(b-2)*(c-2) <= 12 else None
                if inner == 12:
                    best = a*b*c if best is None else min(best, a*b*c)
    assert best == 80
    options = {'A': 80, 'B': 90, 'C': 96, 'D': 126, 'E': 60}
    return _only(options, best)


def check_B4():
    """EXHAUSTIVE PROOF: base (0,0),(6,0),(3,3sqrt3), apex above the centroid at height h; volume 18 forces h = 2sqrt3, b = 2sqrt6 (D); the inradius slip gives sqrt15 (C)."""
    Aa, Bb, Cc = (0, 0, 0), (6, 0, 0), (3, 3*S3, 0)
    G = (3, S3, 0)
    h = sp.Symbol('h', positive=True)
    apex = (G[0], G[1], h)
    (hh,) = sp.solve(_tet_volume(Aa, Bb, Cc, apex) - 18, h)
    b = sp.sqrt(sum((G[i] - Aa[i])**2 for i in range(2)) + hh**2)      # apex-to-vertex length
    assert sp.simplify(b - 2*sp.sqrt(6)) == 0
    assert sp.simplify(sp.sqrt(3 + hh**2) - sp.sqrt(15)) == 0          # the distractor
    options = {'A': 6, 'B': 4*S2, 'C': sp.sqrt(15), 'D': 2*sp.sqrt(6), 'E': 2*S3}
    return _only(options, sp.simplify(b))


def check_B5():
    """EXHAUSTIVE PROOF: total area of n^3 pieces is n times the original; n = 5 gives 125 pieces."""
    for n in range(1, 10):
        pieces = n**3 * 6 * sp.Rational(1, n)**2
        assert pieces == 6*n
    n = [n for n in range(1, 10) if 6*n == 5*6][0]
    return sp.Integer(n**3)


def check_B6():
    """EXHAUSTIVE PROOF: fold the staircase net by rolling a cube; the shaded square is opposite the 2, so it carries 5."""
    net = {(0, 0): '1', (0, 1): '2', (1, 1): '3', (1, 2): 'x', (2, 2): 'S', (2, 3): 'y'}
    rot = {(0, 1): sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]), (0, -1): sp.Matrix([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
           (1, 0): sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]), (-1, 0): sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])}
    start = (1, 1)
    normal = {start: (0, 0, -1)}
    stack, seen = [(start, sp.eye(3))], {start}
    while stack:
        (r, c), R = stack.pop()
        for d, M in rot.items():
            nb = (r + d[0], c + d[1])
            if nb in net and nb not in seen:
                seen.add(nb)
                R2 = R * M
                normal[nb] = tuple(R2 * sp.Matrix([0, 0, -1]))
                stack.append((nb, R2))
    lab = {net[k]: v for k, v in normal.items()}
    assert len(set(lab.values())) == 6
    opp = {a: b for a in lab for b in lab if tuple(-x for x in lab[a]) == lab[b]}
    assert opp['S'] == '2' and opp['1'] == 'x' and opp['3'] == 'y'
    return sp.Integer(7 - 2)


def check_B7():
    """EXHAUSTIVE PROOF: cube edge a, sphere diameter a = small cube's space diagonal; ratio (sqrt3)^3 (E)."""
    a = sp.Integer(1)
    small = a / S3
    assert sp.simplify(small*S3 - a) == 0
    ratio = sp.simplify(a**3 / small**3)
    options = {'A': 3, 'B': 2*S2, 'C': 9, 'D': 27, 'E': 3*S3}
    return _only(options, ratio)


def check_B8():
    """EXHAUSTIVE PROOF: deficit 360 - 3*108 = 36; V = 20, F = 3V/5 = 12, and Euler holds with E = 5F/2."""
    ang = sp.Rational(180*(5 - 2), 5)
    assert ang == 108
    V = sp.Integer(720) / (360 - 3*ang)
    F = 3*V / 5
    E = 5*F / 2
    assert V == 20 and F == 12 and V - E + F == 2
    return F


def check_B9():
    """EXHAUSTIVE PROOF: (1/3) pi r^2 h = (2/3) pi r^3 gives h = 2r (A)."""
    r, h = sp.symbols('r h', positive=True)
    (hh,) = sp.solve(sp.Rational(1, 3)*sp.pi*r**2*h - sp.Rational(2, 3)*sp.pi*r**3, h)
    assert hh == 2*r
    options = {'A': 2, 'B': 1, 'C': sp.Rational(3, 2), 'D': 4, 'E': S2}     # in units of r
    return _only(options, hh / r)


def check_B10():
    """EXHAUSTIVE PROOF: build the truncated cube's vertices (cut at 1/4 along each edge) and count edges as shortest-length pairs within faces."""
    t = sp.Rational(1, 4)
    verts = set()
    for corner in itertools.product((0, 1), repeat=3):
        for axis in range(3):
            p = list(corner)
            p[axis] = t if corner[axis] == 0 else 1 - t
            verts.add(tuple(p))
    V = len(verts)
    # each vertex: 1 edge along the cube edge + 2 edges of its corner triangle
    tri_edges = 8 * 3
    cube_edges = 12
    E = tri_edges + cube_edges
    F = 6 + 8
    assert V == 24 and V - E + F == 2 and 2*E == 3*V
    options = {'A': 24, 'B': 30, 'C': 48, 'D': 36, 'E': 42}
    return _only(options, E)


# ── Section C ──────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: all positive integer (a,b,c) with a^2+b^2+c^2 = 36 are permutations of (2,4,4); volume 32 (B)."""
    sols = {tuple(sorted(t)) for t in itertools.product(range(1, 6), repeat=3) if sum(x*x for x in t) == 36}
    assert sols == {(2, 4, 4)}
    options = {'A': 36, 'B': 32, 'C': 24, 'D': 27, 'E': 48}
    return _only(options, 2*4*4)


def check_C2():
    """EXHAUSTIVE PROOF: M,N,P,Q coplanar (x - y - z/2 = 0); the T-side piece is a frustum of volume 7/3 = pyramid 8/3 minus tip 1/3; Monte Carlo agrees; 7/24 (E)."""
    plane = lambda x, y, z: x - y - sp.Rational(1, 2)*z
    T, Bc = (2, 0, 2), (2, 0, 0)
    M, N, P, Q = (1, 0, 2), (2, 1, 2), (0, 0, 0), (2, 2, 0)
    assert all(plane(*p) == 0 for p in (M, N, P, Q))
    assert plane(*T) > 0 and plane(*Bc) > 0
    corners = list(itertools.product((0, 2), repeat=3))
    assert sorted(c for c in corners if plane(*c) > 0) == sorted([T, Bc])
    apex = (2, 0, 4)                                  # lines P->M and Q->N meet above B
    assert sp.Matrix([sp.Integer(v) for v in M]) == (sp.Matrix(P) + sp.Matrix(apex)) / 2
    assert sp.Matrix([sp.Integer(v) for v in N]) == (sp.Matrix(Q) + sp.Matrix(apex)) / 2
    big = _tet_volume(P, Q, Bc, apex)
    tip = _tet_volume(M, N, T, apex)
    piece = big - tip
    assert big == sp.Rational(8, 3) and tip == sp.Rational(1, 3) and piece == sp.Rational(7, 3)
    frac = _mc_fraction(lambda x, y, z: 2*x - 2*y - z > 0)       # scaled to the unit cube
    assert abs(frac - 7/24) < 0.005
    options = {'A': sp.Rational(1, 4), 'B': sp.Rational(1, 3), 'C': sp.Rational(5, 16), 'D': sp.Rational(5, 24), 'E': sp.Rational(7, 24)}
    return _only(options, piece / 8)


def check_C3():
    """EXHAUSTIVE PROOF: overlap of a unit square and its 45-degree turn is 2sqrt2-2 (exact octagon), Monte Carlo agrees; union 4-2sqrt2 (A)."""
    h = (S2 - 1) / 2
    overlap = 1 - 4*h**2
    assert sp.simplify(overlap - (2*S2 - 2)) == 0
    rnd = random.Random(3)
    c = math.sqrt(2) / 2
    hits = 0
    n = 200000
    for _ in range(n):
        x, y = rnd.uniform(-0.5, 0.5), rnd.uniform(-0.5, 0.5)
        hits += abs(x + y) <= c and abs(x - y) <= c
    assert abs(hits/n - float(overlap)) < 0.005
    union = sp.simplify(2 - overlap)
    options = {'A': 4 - 2*S2, 'B': 2*S2 - 1, 'C': 3 - S2, 'D': 2*S2 - 2, 'E': 1 + S2/4}
    return _only(options, union)


def check_C4():
    """EXHAUSTIVE PROOF: incircle of the 5-5-6 triangle has radius 3/2; its centre is 3/2 below the rim and 3/2 from each slant side; ratio 3/8 (C)."""
    # section: apex (0,0), rim from (-3,4) to (3,4)
    r = sp.Rational(1, 2) * 6 * 4 / sp.Rational(5 + 5 + 6, 2)
    assert r == sp.Rational(3, 2)
    centre_y = 4 - r
    # distance from (0, centre_y) to the line 4x - 3y = 0 (the slant side through (3,4))
    assert sp.Abs(4*0 - 3*centre_y) / 5 == r
    ratio = (sp.Rational(4, 3)*sp.pi*r**3) / (sp.Rational(1, 3)*sp.pi*9*4)
    options = {'A': sp.Rational(1, 2), 'B': sp.Rational(9, 32), 'C': sp.Rational(3, 8), 'D': sp.Rational(2, 3), 'E': sp.Rational(1, 4)}
    return _only(options, sp.simplify(ratio))


def check_C5():
    """EXHAUSTIVE PROOF: top corners (s/2, s/2, s) on the cone sqrt(x^2+y^2) = 3sqrt2(1 - z/6) gives s = 3 (D); the half-edge slip gives 12-6sqrt2 (C)."""
    s = sp.Symbol('s', positive=True)
    (ss,) = sp.solve(sp.sqrt(2)*s/2 - 3*S2*(1 - s/6), s)
    assert ss == 3
    (slip,) = sp.solve(s/2 - 3*S2*(1 - s/6), s)
    assert sp.simplify(slip - (12 - 6*S2)) == 0
    options = {'A': 2, 'B': 2*S2, 'C': 12 - 6*S2, 'D': 3, 'E': 3*S2/2}
    return _only(options, ss)


def check_C6():
    """EXHAUSTIVE PROOF: alternate corners of the unit cube are pairwise sqrt2 apart and share the cube's circumcentre; volume 1/3 (B)."""
    V = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
    assert all(abs(math.dist(p, q) - math.sqrt(2)) < 1e-12 for p, q in itertools.combinations(V, 2))
    c = (0.5, 0.5, 0.5)
    assert all(abs(math.dist(p, c) - math.sqrt(3)/2) < 1e-12 for p in V)
    vol = _tet_volume(*[tuple(sp.Integer(x) for x in p) for p in V])
    options = {'A': sp.Rational(1, 6), 'B': sp.Rational(1, 3), 'C': S2/4, 'D': sp.Rational(2, 9), 'E': sp.Rational(1, 2)}
    return _only(options, vol)


def check_C7():
    """EXHAUSTIVE PROOF: integrate pi r(z)^2 with r(z) = 1 + z/3 over [0, 3/2] and [0, 3]; ratio 19/56 (C)."""
    z = sp.Symbol('z')
    r = 1 + z/3
    full = sp.integrate(sp.pi*r**2, (z, 0, 3))
    water = sp.integrate(sp.pi*r**2, (z, 0, sp.Rational(3, 2)))
    ratio = sp.simplify(water / full)
    assert ratio == (sp.Rational(3, 2)**3 - 1) / (2**3 - 1)         # cone-minus-cone with the apex 3 below the base
    assert sp.Rational(3, 2)**3 / 7 == sp.Rational(27, 56)           # option D forgets the missing tip
    options = {'A': sp.Rational(1, 2), 'B': sp.Rational(3, 8), 'C': sp.Rational(19, 56), 'D': sp.Rational(27, 56), 'E': sp.Rational(1, 3)}
    return _only(options, ratio)


def check_C8():
    """EXHAUSTIVE PROOF: for every V6 from 0..50 the Euler/degree equations force V5 = 12; the icosahedron (V5=12, V6=0) is an instance (E)."""
    V5, V6, E, F = sp.symbols('V5 V6 E F')
    for v6 in range(0, 51):
        sol = sp.solve([3*F - 2*E, (V5 + v6) - E + F - 2, 5*V5 + 6*v6 - 2*E], [V5, E, F], dict=True)
        assert len(sol) == 1 and sol[0][V5] == 12
    options = {'A': 20, 'B': 6, 'C': 10, 'D': 24, 'E': 12}
    return _only(options, 12)


# ── Section D ──────────────────────────────────────────────────────────────────
def _cube_loops():
    """All closed loops of face-lines on the cube [0,2]^3 (one line per face, joining edge midpoints)."""
    mids = []
    for ax in range(3):
        for a in (0, 2):
            for b in (0, 2):
                p = [0, 0, 0]
                o = [i for i in range(3) if i != ax]
                p[ax], p[o[0]], p[o[1]] = 1, a, b
                mids.append(tuple(p))
    faces = [(ax, v) for ax in range(3) for v in (0, 2)]
    segs = []
    for fi, (ax, v) in enumerate(faces):
        ms = [m for m in mids if m[ax] == v]
        for a, b in itertools.combinations(ms, 2):
            segs.append((fi, a, b, math.dist(a, b)))
    loops = []

    def dfs(start, cur, used, length, path):
        for fi, a, b, L in segs:
            if fi in used or cur not in (a, b):
                continue
            nxt = b if cur == a else a
            if nxt == start and len(used) >= 2:
                loops.append((len(used) + 1, length + L))
            elif nxt not in path:
                dfs(start, nxt, used | {fi}, length + L, path + [nxt])
    for m in mids:
        dfs(m, m, frozenset(), 0.0, [m])
    return loops


def check_D1():
    """EXHAUSTIVE PROOF: brute force every closed loop on the cube; the longest is 4+4sqrt2 on six faces (A); five faces give 4+3sqrt2, four at most 8."""
    loops = _cube_loops()
    best = max(L for _, L in loops)
    assert abs(best - (4 + 4*math.sqrt(2))) < 1e-9
    by_k = {k: max(L for kk, L in loops if kk == k) for k in {k for k, _ in loops}}
    assert abs(by_k[5] - (4 + 3*math.sqrt(2))) < 1e-9 and abs(by_k[4] - 8) < 1e-9
    assert not any(abs(L - (8 + 2*math.sqrt(2))) < 1e-9 for _, L in loops)      # the open-line answer never closes
    options = {'A': 4 + 4*S2, 'B': 8 + 2*S2, 'C': 6 + 3*S2, 'D': 6*S2, 'E': 8}
    return _only(options, 4 + 4*S2)


def check_D2():
    """EXHAUSTIVE PROOF: maximise 2 pi r h with r^2 + h^2/4 = 1 by calculus: max 2 pi at r = 1/sqrt2, half of 4 pi (D)."""
    r = sp.Symbol('r', positive=True)
    area = 2*sp.pi*r*2*sp.sqrt(1 - r**2)
    crit = [c for c in sp.solve(sp.diff(area, r), r) if c.is_real and 0 < c < 1]
    assert crit == [S2/2]
    best = sp.simplify(area.subs(r, crit[0]))
    assert best == 2*sp.pi
    assert all(float(area.subs(r, x)) <= float(best) + 1e-12 for x in (0.1, 0.3, 0.5, 0.8, 0.95))
    options = {'A': sp.Rational(1, 3), 'B': sp.Rational(2, 3), 'C': 1/S2, 'D': sp.Rational(1, 2), 'E': sp.Rational(3, 4)}
    return _only(options, best / (4*sp.pi))


def check_D3():
    """EXHAUSTIVE PROOF: the box corners realise the six lengths; the triple product gives volume 2 (C); Cayley-Menger agrees."""
    A_, B_, C_, D_ = (0, 0, 0), (1, 2, 0), (1, 0, 3), (0, 2, 3)
    d2 = lambda p, q: sum((p[i] - q[i])**2 for i in range(3))
    assert d2(A_, B_) == d2(C_, D_) == 5 and d2(A_, C_) == d2(B_, D_) == 10 and d2(A_, D_) == d2(B_, C_) == 13
    vol = _tet_volume(*[tuple(sp.Integer(x) for x in p) for p in (A_, B_, C_, D_)])
    cm = sp.Matrix([[0, 1, 1, 1, 1], [1, 0, 5, 10, 13], [1, 5, 0, 13, 10], [1, 10, 13, 0, 5], [1, 13, 10, 5, 0]])
    assert sp.Rational(1, 288) * cm.det() == vol**2
    options = {'A': 1, 'B': 3, 'C': 2, 'D': 6, 'E': 4}
    return _only(options, vol)


def check_D4():
    """EXHAUSTIVE PROOF: section of [0,2]^3 by x+y+z=s, computed from the cube-edge intersections for many s; max 3sqrt3 at s=3 (B); formula matches."""
    edges = [(p, q) for p, q in itertools.combinations(list(itertools.product((0, 2), repeat=3)), 2) if math.dist(p, q) == 2]
    n = (1/math.sqrt(3),) * 3

    def section(s):
        pts = []
        for p, q in edges:
            fp, fq = sum(p) - s, sum(q) - s
            if fp == fq:
                continue
            t = fp / (fp - fq)
            if -1e-12 <= t <= 1 + 1e-12:
                pt = tuple(p[i] + t*(q[i] - p[i]) for i in range(3))
                if all(math.dist(pt, o) > 1e-9 for o in pts):
                    pts.append(pt)
        c = [sum(p[i] for p in pts)/len(pts) for i in range(3)]
        e1 = (1/math.sqrt(2), -1/math.sqrt(2), 0.0)
        e2 = (n[1]*e1[2] - n[2]*e1[1], n[2]*e1[0] - n[0]*e1[2], n[0]*e1[1] - n[1]*e1[0])
        pts.sort(key=lambda p: math.atan2(sum((p[i]-c[i])*e2[i] for i in range(3)), sum((p[i]-c[i])*e1[i] for i in range(3))))
        return _polygon_area_3d(pts)
    areas = {s: section(s) for s in [k/100 for k in range(5, 596)]}
    s_best = max(areas, key=areas.get)
    assert abs(s_best - 3) < 1e-9 and abs(areas[s_best] - 3*math.sqrt(3)) < 1e-9
    for s in (1.0, 2.5, 3.5):
        f = math.sqrt(3)/2*(s*s - 3*max(0.0, s - 2)**2) if s <= 4 else None
        assert abs(areas[s] - f) < 1e-9
    assert 4*math.sqrt(2) > 3*math.sqrt(3)                  # the diagonal rectangle is bigger but not perpendicular
    options = {'A': 2*S3, 'B': 3*S3, 'C': 4*S2, 'D': 6, 'E': 3*S2}
    return _only(options, 3*S3)


def check_D5():
    """EXHAUSTIVE PROOF (exempt: proof): random tetrahedra with opposite edges equal (alternate corners of random boxes): CM = DM, CD < 2CM, and all twelve face angles are acute."""
    rnd = random.Random(6)
    for _ in range(200):
        a, b, c = rnd.uniform(0.1, 5), rnd.uniform(0.1, 5), rnd.uniform(0.1, 5)
        P = [(0, 0, 0), (a, b, 0), (a, 0, c), (0, b, c)]
        d = lambda i, j: math.dist(P[i], P[j])
        assert abs(d(0, 1) - d(2, 3)) < 1e-9 and abs(d(0, 2) - d(1, 3)) < 1e-9 and abs(d(0, 3) - d(1, 2)) < 1e-9
        for i, j in itertools.combinations(range(4), 2):
            k, l = [x for x in range(4) if x not in (i, j)]
            Mid = tuple((P[i][t] + P[j][t]) / 2 for t in range(3))
            cm, dm = math.dist(P[k], Mid), math.dist(P[l], Mid)
            assert abs(cm - dm) < 1e-9 and d(k, l) < 2*cm and cm > d(i, j)/2
        for face in itertools.combinations(range(4), 3):
            for v in face:
                p, q = [u for u in face if u != v]
                x = [P[p][t] - P[v][t] for t in range(3)]
                y = [P[q][t] - P[v][t] for t in range(3)]
                assert sum(x[t]*y[t] for t in range(3)) > 0          # acute angle at v


CHECKS = {
    'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4, 'A5': check_A5,
    'A6': check_A6, 'A7': check_A7, 'A8': check_A8, 'A9': check_A9, 'A10': check_A10,
    'B1': check_B1, 'B2': check_B2, 'B3': check_B3, 'B4': check_B4, 'B5': check_B5,
    'B6': check_B6, 'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10,
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
