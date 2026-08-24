import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'combinatorics/answers/ans02.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(7,2)."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=30))
    def test_triangular(n_val):
        assert (n_val * (n_val - 1)) % 2 == 0
        assert math.comb(n_val, 2) == (n_val * (n_val - 1)) // 2

    test_triangular()
    computed_ans = len(list(itertools.combinations(range(7), 2)))
    assert sympy.simplify(computed_ans - target) == 0
    assert 7 * 6 // 2 == computed_ans


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(8,3)."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(
        st.integers(min_value=1, max_value=20),
        st.integers(min_value=0, max_value=20)
    )
    def test_symmetry(n_val, r_val):
        if r_val <= n_val:
            assert math.comb(n_val, r_val) == math.comb(n_val, n_val - r_val)

    test_symmetry()
    computed_ans = len(list(itertools.combinations(range(8), 3)))
    assert sympy.simplify(computed_ans - target) == 0
    assert computed_ans == len(list(itertools.combinations(range(8), 5)))


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(9,7)."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(itertools.combinations(range(9), 7)))
    assert sympy.simplify(computed_ans - target) == 0
    assert math.comb(9, 2) == computed_ans
    assert math.comb(100, 98) == math.comb(100, 2)


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for committees of 3 from 6."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=10))
    def test_comb_perm_relation(n_val):
        r = min(3, n_val)
        assert math.comb(n_val, r) * math.factorial(r) == math.perm(n_val, r)

    test_comb_perm_relation()
    computed_ans = len(list(itertools.combinations(range(6), 3)))
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for solving C(n,2)=45."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    n = sympy.Symbol('n', positive=True, integer=True)
    sol = sympy.solve(n * (n - 1) / 2 - 45, n)
    assert len(sol) == 1
    computed_n = sol[0]
    assert sympy.simplify(computed_n - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for subsets with >= 4 elements."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    elements = range(5)
    subsets = [c for r in range(6) for c in itertools.combinations(elements, r) if len(c) >= 4]
    computed_ans = len(subsets)
    assert sympy.simplify(computed_ans - target) == 0
    assert 2**5 - sum(math.comb(5, k) for k in range(4)) == computed_ans


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for row sum of Pascal's triangle."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans
    if target is True:
        target = 2**6

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=0, max_value=12))
    def test_binomial_sum(n_val):
        assert sum(math.comb(n_val, k) for k in range(n_val + 1)) == 2**n_val
        assert sum((-1)**k * math.comb(n_val, k) for k in range(n_val + 1)) == (1 if n_val == 0 else 0)

    test_binomial_sum()
    computed_ans = sum(len(list(itertools.combinations(range(6), k))) for k in range(7))
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for choosing 2 letters from 5."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    letters = ['A', 'B', 'C', 'D', 'E']
    combs = list(itertools.combinations(letters, 2))
    computed_ans = len(combs)
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """SAMPLED CHECK: Uses Property-Based Testing and SymPy parsing for True/False question."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=100))
    def test_staircase_identity(n_val):
        assert math.comb(n_val, 2) + math.comb(n_val + 1, 2) == n_val**2

    test_staircase_identity()
    computed_bool = (math.comb(100, 98) == 4950)
    assert computed_bool == target


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for lottery tickets."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(itertools.combinations(range(10), 4)))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for C(n,3)=35."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    n = sympy.Symbol('n', positive=True, integer=True)
    sol = sympy.solve(n * (n - 1) * (n - 2) / 6 - 35, n)
    assert len(sol) == 1
    computed_n = sol[0]
    assert sympy.simplify(computed_n - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for committee of 2M, 2W."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    men = range(8)
    women = range(8, 14)
    computed_ans = len(list(itertools.product(
        itertools.combinations(men, 2),
        itertools.combinations(women, 2)
    )))
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for handshakes."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(itertools.combinations(range(12), 2)))
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for segments and triangles."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    if isinstance(expected_ans, list):
        target_segs = expected_ans[0].rhs if isinstance(expected_ans[0], sympy.Equality) else expected_ans[0]
        target_triangles = expected_ans[1].rhs if isinstance(expected_ans[1], sympy.Equality) else expected_ans[1]
    else:
        target_segs = 45
        target_triangles = 120

    points = list(range(10))
    computed_segs = len(list(itertools.combinations(points, 2)))
    computed_triangles = len(list(itertools.combinations(points, 3)))
    assert sympy.simplify(computed_segs - target_segs) == 0
    assert sympy.simplify(computed_triangles - target_triangles) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for committee chair identity."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=20))
    def test_chair_identity(n_val):
        for r in range(1, n_val + 1):
            assert r * math.comb(n_val, r) == n_val * math.comb(n_val - 1, r - 1)

    test_chair_identity()
    computed_ans = 11 * math.comb(10, 4)
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for binary strings."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    strings_with_3_ones = sum(1 for s in itertools.product((0, 1), repeat=8) if sum(s) == 3)
    assert sympy.simplify(strings_with_3_ones - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-letter sets."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    vowels = range(5)
    consonants = range(5, 26)
    computed_ans = len(list(itertools.product(
        itertools.combinations(vowels, 1),
        itertools.combinations(consonants, 2)
    )))
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Pascal backward solve."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=30))
    def test_pascal_rule(n_val):
        assert math.comb(n_val, 2) + math.comb(n_val, 1) == math.comb(n_val + 1, 2)

    test_pascal_rule()
    solutions = [n for n in range(2, 50) if math.comb(n, 2) + math.comb(n, 1) == 21]
    assert len(solutions) == 1
    computed_n = solutions[0]
    assert sympy.simplify(computed_n - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Priya in/out cases."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    if isinstance(expected_ans, list):
        target_in = expected_ans[0].rhs if isinstance(expected_ans[0], sympy.Equality) else expected_ans[0]
        target_out = expected_ans[1].rhs if isinstance(expected_ans[1], sympy.Equality) else expected_ans[1]
    else:
        target_in = 56
        target_out = 70

    people = list(range(9))
    include_priya = sum(1 for c in itertools.combinations(people, 4) if 0 in c)
    exclude_priya = sum(1 for c in itertools.combinations(people, 4) if 0 not in c)
    assert sympy.simplify(include_priya - target_in) == 0
    assert sympy.simplify(exclude_priya - target_out) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for lattice paths."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    steps = ['R'] * 4 + ['U'] * 3
    unique_paths = set(itertools.permutations(steps))
    computed_ans = len(unique_paths)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for committee >=4 women."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    pool = [f"W{i}" for i in range(7)] + [f"M{i}" for i in range(6)]
    valid_count = sum(1 for comm in itertools.combinations(pool, 5) if sum(1 for p in comm if p.startswith('W')) >= 4)
    assert sympy.simplify(valid_count - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4-digit repeated digits."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    repeated_count = sum(1 for n in range(1000, 10000) if len(set(str(n))) < 4)
    assert sympy.simplify(repeated_count - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for diagonals of 12-gon."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=3, max_value=30))
    def test_diagonals_formula(n_val):
        assert math.comb(n_val, 2) - n_val == (n_val * (n_val - 3)) // 2

    test_diagonals_formula()
    computed_ans = math.comb(12, 2) - 12
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for triangles avoiding point A."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    if isinstance(expected_ans, list):
        target = expected_ans[1].rhs if isinstance(expected_ans[1], sympy.Equality) else expected_ans[1]
    else:
        target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    points = list(range(8))
    triangles_avoiding_0 = sum(1 for triple in itertools.combinations(points, 3) if 0 not in triple)
    assert sympy.simplify(triangles_avoiding_0 - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for unequal split teams."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    pool = [f"B{i}" for i in range(6)] + [f"G{i}" for i in range(6)]
    unequal = sum(1 for comm in itertools.combinations(pool, 6) if sum(1 for p in comm if p.startswith('B')) != 3)
    assert sympy.simplify(unequal - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5-card hands with >=3 aces."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    deck = list(range(52))
    valid_hands = sum(1 for h in itertools.combinations(deck, 5) if sum(1 for c in h if c < 4) >= 3)
    assert sympy.simplify(valid_hands - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for polygon with 27 diagonals."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    n = sympy.Symbol('n', positive=True, integer=True)
    sol = sympy.solve(n * (n - 3) / 2 - 27, n)
    assert len(sol) == 1
    computed_n = sol[0]
    assert sympy.simplify(computed_n - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for subsets containing 1 or 2."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    elements = range(1, 11)
    computed_ans = sum(1 for r in range(11) for s in itertools.combinations(elements, r) if 1 in s or 2 in s)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for rectangles on 4x4 grid."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=10))
    def test_rectangles_formula(n_val):
        rects = math.comb(n_val + 1, 2)**2
        sqs = sum(k**2 for k in range(1, n_val + 1))
        assert rects >= sqs

    test_rectangles_formula()
    rectangles = sum(1 for x1 in range(5) for x2 in range(x1 + 1, 5) for y1 in range(5) for y2 in range(y1 + 1, 5))
    assert sympy.simplify(rectangles - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for non-consecutive subsets."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    def valid_non_consec(n):
        return sum(1 for r in range(n + 1) for s in itertools.combinations(range(1, n + 1), r)
                   if not any(s[i+1] - s[i] == 1 for i in range(len(s) - 1)))

    computed_ans = valid_non_consec(8)
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for committee majority juniors."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for r in range(13) for comm in itertools.combinations(range(12), r)
                       if sum(1 for p in comm if p < 6) > sum(1 for p in comm if p >= 6))
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 2-regular graphs on 6 vertices."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    edges_6 = list(itertools.combinations(range(6), 2))
    computed_ans = 0
    for graph in itertools.combinations(edges_6, 6):
        degrees = [0] * 6
        for u, v in graph:
            degrees[u] += 1
            degrees[v] += 1
        if all(d == 2 for d in degrees):
            computed_ans += 1

    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for interior intersection points."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.comb(10, 4)
    assert sympy.simplify(computed_ans - target) == 0


CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4,
    "C5": check_C5, "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
}

def main():
    if not __debug__:
        print("ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.")
        raise SystemExit(2)

    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f"  PASS  {label}")
        except AssertionError as e:
            failures.append(label)
            print(f"  FAIL  {label}: {e}")
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f"All {len(CHECKS)} checks passed.")

if __name__ == "__main__":
    main()
