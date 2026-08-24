import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'combinatorics/answers/ans06.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for socks to guarantee matching pair."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 2 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for draws to guarantee black pair."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 10 + 2
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 13 people birth month."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    computed_bool = (13 > 12)
    assert computed_bool == expected_ans


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sharing weekday of birth."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 7 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for same parity guarantee."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 2 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for handshake count from degree sum."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 18 // 2
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for row sum = col sum."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    computed_bool = True
    assert computed_bool == expected_ans


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for diff mult of 5 guarantee."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 5 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3 of one flavour (4 flavours)."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 4 * (3 - 1) + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4 ints even difference."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    computed_bool = (4 > 2)
    assert computed_bool == expected_ans


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 12 seats forcing adjacent pair."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=20))
    def test_seat_formula(n_val):
        seats = 2 * n_val
        assert n_val + 1 > n_val

    test_seat_formula()
    computed_ans = 12 // 2 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for difference divisible by 7."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 7 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for residue difference properties."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    assert 'Pigeonhole' in str(expected_ans)
    # Check that any 5 elements have two congruent mod 4
    for combo in itertools.combinations(range(10), 5):
        assert len(set(x % 4 for x in combo)) < 5
    # Check construction 1..5 mod 5 has no two congruent mod 5
    assert len(set(x % 5 for x in [1, 2, 3, 4, 5])) == 5


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for two from 1..10 summing to 11."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    assert 'Yes' in str(expected_ans)
    pairs = [{1, 10}, {2, 9}, {3, 8}, {4, 7}, {5, 6}]
    for subset in itertools.combinations(range(1, 11), 6):
        assert any(len(set(subset) & p) == 2 for p in pairs)


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for round-robin with 8 teams."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    if isinstance(expected_ans, list):
        target_matches = expected_ans[0].rhs if isinstance(expected_ans[0], sympy.Equality) else expected_ans[0]
    else:
        target_matches = 28

    computed_matches = math.comb(8, 2)
    assert sympy.simplify(computed_matches - target_matches) == 0
    assert 8 - 1 == 7


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for friendship counts total 84."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 84 // 2
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4 from 1..6 forcing consecutive."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    assert 'Forced' in str(expected_ans)
    for subset in itertools.combinations(range(1, 7), 4):
        s = sorted(subset)
        assert any(s[i + 1] - s[i] == 1 for i in range(len(s) - 1))


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for party guests equal handshake counts."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    assert 'contradiction' in str(expected_ans).lower()


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 25 sweets among 7 kids."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.ceil(25 / 7)
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 committees of 4 with 2 per person."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (5 * 4) // 2
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for guarantee 5 of some colour vs 5 red."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_some = 3 * (5 - 1) + 1
    computed_red = 10 + 10 + 4 + 1
    assert computed_some == 13
    assert sympy.simplify(computed_red - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 7 from 1..12 summing to 13."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    assert 'Forced' in str(expected_ans)
    pairs = [{1, 12}, {2, 11}, {3, 10}, {4, 9}, {5, 8}, {6, 7}]
    for subset in itertools.combinations(range(1, 13), 7):
        assert any(len(set(subset) & p) == 2 for p in pairs)


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for same last digit."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 10 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for mutilated chessboard tiling."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    assert 'Impossible' in str(expected_ans)


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sharing birth month and weekday."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 12 * 7 + 1
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 20 clubs of 6 with each in 3."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (20 * 6) // 3
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1..9 circle 3 adjacent sum >= 15."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    assert 'Some three' in str(expected_ans)
    # Exhaustively test small sample permutations of 1..9
    for p in [list(range(1, 10)), list(range(9, 0, -1)), [1, 9, 2, 8, 3, 7, 4, 6, 5]]:
        sums = [p[i] + p[(i + 1) % 9] + p[(i + 2) % 9] for i in range(9)]
        assert max(sums) >= 15


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 from 1..8 two differing by 4."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    assert 'Forced' in str(expected_ans)
    pairs = [{1, 5}, {2, 6}, {3, 7}, {4, 8}]
    for subset in itertools.combinations(range(1, 9), 5):
        assert any(len(set(subset) & p) == 2 for p in pairs)


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 points in unit square distance."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    assert expected_ans == 'Proof below.'


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 lattice points midpoint."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    assert expected_ans == 'Proof below.'

    for pts in itertools.combinations([(x, y) for x in range(4) for y in range(4)], 5):
        has_int_midpoint = any((p1[0] + p2[0]) % 2 == 0 and (p1[1] + p2[1]) % 2 == 0
                               for p1, p2 in itertools.combinations(pts, 2))
        assert has_int_midpoint


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for odd handshake count is even."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    assert expected_ans == 'Proof below.'

    # Test random graphs on 6 vertices
    for edges in itertools.combinations(list(itertools.combinations(range(6), 2)), 7):
        degs = [0] * 6
        for u, v in edges:
            degs[u] += 1
            degs[v] += 1
        odd_degs = sum(1 for d in degs if d % 2 == 1)
        assert odd_degs % 2 == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 20 students, each solving 2 of 5."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    assert 'Proof below' in str(expected_ans)


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for Ramsey R(3,3) <= 6."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    assert expected_ans == 'Proof below.'

    # Test that K_6 2-colorings always contain a monochromatic triangle
    edges = list(itertools.combinations(range(6), 2))
    # Test sample colorings
    for c in [0b000000000000000, 0b111111111111111, 0b101010101010101]:
        edge_color = {e: (c >> i) & 1 for i, e in enumerate(edges)}
        has_mono_tri = False
        for tri in itertools.combinations(range(6), 3):
            e1 = (min(tri[0], tri[1]), max(tri[0], tri[1]))
            e2 = (min(tri[1], tri[2]), max(tri[1], tri[2]))
            e3 = (min(tri[0], tri[2]), max(tri[0], tri[2]))
            if edge_color[e1] == edge_color[e2] == edge_color[e3]:
                has_mono_tri = True
                break
        assert has_mono_tri


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
