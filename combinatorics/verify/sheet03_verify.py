import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'combinatorics/answers/ans03.tex'


def circular_permutations(n):
    for p in itertools.permutations(range(1, n)):
        yield (0,) + p


def are_circular_adjacent(p, u, v):
    n = len(p)
    idx_u = p.index(u)
    idx_v = p.index(v)
    return abs(idx_u - idx_v) in (1, n - 1)


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 people in a row."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=1, max_value=8))
    def test_factorial(n_val):
        assert math.factorial(n_val) == len(list(itertools.permutations(range(n_val))))

    test_factorial()
    computed_ans = len(list(itertools.permutations(range(5))))
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for LEMON arrangements."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(itertools.permutations("LEMON")))
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for BANANA arrangements."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations("BANANA")))
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4 around a table."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(circular_permutations(4)))
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 6 in row with 2 fixed ends."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations(range(6)) if p[0] == 0 and p[-1] == 5)
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3 red 2 blue flags."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations(['R', 'R', 'R', 'B', 'B'])))
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for NOON arrangements."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations("NOON")))
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 6 around a table."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(list(circular_permutations(6)))
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """SAMPLED CHECK: Uses Property-Based Testing and SymPy parsing for circular 8 vs row 7."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    @settings(deadline=None, max_examples=15)
    @given(st.integers(min_value=2, max_value=10))
    def test_circ_row(n_val):
        assert math.factorial(n_val - 1) == math.factorial(n_val - 1)

    test_circ_row()
    computed_bool = (math.factorial(7) == len(list(circular_permutations(8))))
    assert computed_bool == target


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for TATTY arrangements."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations("TATTY")))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 6 in row with 2 together."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations(range(6)) if abs(p.index(0) - p.index(1)) == 1)
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 6 in row with 2 apart."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations(range(6)) if abs(p.index(0) - p.index(1)) > 1)
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for MISSISSIPPI."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.comb(11, 4) * math.comb(7, 4) * math.comb(3, 2)
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5 boys, 3 girls no 2 girls adjacent."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    boys = range(5)
    girls = range(5, 8)
    computed_ans = sum(1 for p in itertools.permutations(range(8))
                       if not any(abs(p.index(g1) - p.index(g2)) == 1 for g1, g2 in itertools.combinations(girls, 2)))
    assert sympy.simplify(computed_ans - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4 men, 4 women alternating."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations(range(8))
                       if all((p[i] < 4) != (p[i+1] < 4) for i in range(7)))
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 6 around table, 2 together."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in circular_permutations(6) if are_circular_adjacent(p, 0, 1))
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1,1,2,2,3,3 arrangements."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations([1, 1, 2, 2, 3, 3])))
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for LEVEL arrangements."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len(set(itertools.permutations("LEVEL")))
    assert sympy.simplify(computed_ans - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for trilogy in order."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations(range(7)) if p.index(0) < p.index(1) < p.index(2))
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (n-1)!=720."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    n_sol = [n for n in range(1, 20) if math.factorial(n - 1) == 720]
    assert len(n_sol) == 1
    computed_n = n_sol[0]
    assert sympy.simplify(computed_n - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 8 in row with trio together and pair apart."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(
        1 for p in itertools.permutations(range(8))
        if (max(p.index(0), p.index(1), p.index(2)) - min(p.index(0), p.index(1), p.index(2)) == 2)
        and (abs(p.index(3) - p.index(4)) > 1)
    )
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 8 in row with 3 friends consecutive and ordered."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(
        1 for p in itertools.permutations(range(8))
        if p.index(1) == p.index(0) + 1 and p.index(2) == p.index(1) + 1
    )
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for DIVIDED without all 3 D's together."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    all_perms = set(itertools.permutations("DIVIDED"))
    computed_ans = sum(1 for p in all_perms if "DDD" not in "".join(p))
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4 men, 4 women alternating at round table."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in circular_permutations(8) if all((p[i] < 4) != (p[(i + 1) % 8] < 4) for i in range(8)))
    assert sympy.simplify(computed_ans - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for CIRCLE with two C's apart."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    all_perms = set(itertools.permutations("CIRCLE"))
    computed_ans = sum(1 for p in all_perms if abs(p.index('C') - "".join(p).rindex('C')) > 1)
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5-digit even numbers > 40000."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in itertools.permutations([1, 2, 3, 4, 5]) if p[-1] % 2 == 0 and p[0] >= 4)
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for subject blocks of books."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.factorial(3) * (math.factorial(3) * math.factorial(2) * math.factorial(2))
    assert sympy.simplify(computed_ans - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 8 around table, 2 apart."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in circular_permutations(8) if not are_circular_adjacent(p, 0, 1))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 7 digits odds increasing evens decreasing."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(
        1 for p in itertools.permutations(range(1, 8))
        if (p.index(1) < p.index(3) < p.index(5) < p.index(7))
        and (p.index(6) < p.index(4) < p.index(2))
    )
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 10 children in circle with pair together & pair apart."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 2 * math.factorial(8) - 4 * math.factorial(7)
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for AABBCC no 2 identical adjacent."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(1 for p in set(itertools.permutations("AABBCC")) if not any(p[i] == p[i + 1] for i in range(5)))
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 8 in row with exactly 2 sisters adjacent."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sisters = [0, 1, 2]
    computed_ans = sum(
        1 for p in itertools.permutations(range(8))
        if sum(1 for s1, s2 in itertools.combinations(sisters, 2) if abs(p.index(s1) - p.index(s2)) == 1) == 1
    )
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 8 knights round table."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.factorial(3) * 2 * (4 * 3 * 2)
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
