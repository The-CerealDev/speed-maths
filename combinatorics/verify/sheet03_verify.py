"""Computational verification for combinatorics/answers/ans03.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer.

Run directly:
    python3 sheet03_verify.py
"""

import itertools
import math

# Helper to generate circular permutations of N elements
def circular_permutations(n):
    # Fix the first element as 0, permute the rest
    for p in itertools.permutations(range(1, n)):
        yield (0,) + p

# Helper to check circular adjacency
def are_circular_adjacent(p, u, v):
    n = len(p)
    idx_u = p.index(u)
    idx_v = p.index(v)
    return abs(idx_u - idx_v) in (1, n - 1)

# Helper to count unique permutations of a multiset
def unique_permutations(elements):
    return set(itertools.permutations(elements))

# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: 5 people in a row independently counted by enumerating permutations."""
    ans_val = len(list(itertools.permutations(range(5))))
    assert ans_val == 120
    assert math.factorial(5) == 120

def check_A2():
    """EXHAUSTIVE PROOF: arrangements of LEMON counted by enumerating permutations."""
    ans_val = len(list(itertools.permutations("LEMON")))
    assert ans_val == 120

def check_A3():
    """EXHAUSTIVE PROOF: arrangements of BANANA counted by unique permutations set."""
    ans_val = len(unique_permutations("BANANA"))
    assert ans_val == 60
    assert math.factorial(6) // (math.factorial(3) * math.factorial(2)) == 60

def check_A4():
    """EXHAUSTIVE PROOF: 4 people around a table circular arrangements."""
    ans_val = len(list(circular_permutations(4)))
    assert ans_val == 6
    assert math.factorial(3) == 6

def check_A5():
    """EXHAUSTIVE PROOF: 6 people in a row, Ali first and Zara last."""
    # Ali = 0, Zara = 5
    count = 0
    for p in itertools.permutations(range(6)):
        if p[0] == 0 and p[-1] == 5:
            count += 1
    assert count == 24
    assert math.factorial(4) == 24

def check_A6():
    """EXHAUSTIVE PROOF: 3 red flags and 2 blue flags unique permutations."""
    ans_val = len(unique_permutations(['R', 'R', 'R', 'B', 'B']))
    assert ans_val == 10
    assert math.comb(5, 2) == 10

def check_A7():
    """EXHAUSTIVE PROOF: arrangements of NOON."""
    ans_val = len(unique_permutations("NOON"))
    assert ans_val == 6
    assert math.factorial(4) // (math.factorial(2) * math.factorial(2)) == 6

def check_A8():
    """EXHAUSTIVE PROOF: 6 people around a table circular arrangements."""
    ans_val = len(list(circular_permutations(6)))
    assert ans_val == 120
    assert math.factorial(5) == 120

def check_A9():
    """SAMPLED CHECK: circular 8 == row 7, and checks that (2n-1)! == n! has no solution for n > 1."""
    assert math.factorial(7) == 5040
    # circular 8 is (8-1)! = 7!
    # row 7 is 7!
    # check that for n > 1, (2n-1)! == n! is false
    for n in range(2, 10):
        assert math.factorial(2 * n - 1) != math.factorial(n)

def check_A10():
    """EXHAUSTIVE PROOF: arrangements of TATTY."""
    ans_val = len(unique_permutations("TATTY"))
    assert ans_val == 20
    assert math.factorial(5) // math.factorial(3) == 20

# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: 6 in a row, Priya (0) and Quinn (1) together."""
    count = 0
    for p in itertools.permutations(range(6)):
        idx_p = p.index(0)
        idx_q = p.index(1)
        if abs(idx_p - idx_q) == 1:
            count += 1
    assert count == 240
    assert 2 * math.factorial(5) == 240

def check_B2():
    """EXHAUSTIVE PROOF: 6 in a row, Priya (0) and Quinn (1) not together."""
    count = 0
    for p in itertools.permutations(range(6)):
        idx_p = p.index(0)
        idx_q = p.index(1)
        if abs(idx_p - idx_q) != 1:
            count += 1
    assert count == 480
    assert math.factorial(6) - 2 * math.factorial(5) == 480

def check_B3():
    """EXHAUSTIVE PROOF: arrangements of MISSISSIPPI."""
    ans_val = len(unique_permutations("MISSISSIPPI"))
    assert ans_val == 34650
    assert math.factorial(11) // (math.factorial(4) * math.factorial(4) * math.factorial(2)) == 34650

def check_B4():
    """EXHAUSTIVE PROOF: 5 boys and 3 girls in a row, no two girls adjacent.
    Checks that the gap method calculation matches."""
    # Boys = 0..4, Girls = 5..7
    count = 0
    for p in itertools.permutations(range(8)):
        # Check if girls are adjacent
        girls_adjacent = False
        for i in range(7):
            if p[i] >= 5 and p[i+1] >= 5:
                girls_adjacent = True
                break
        if not girls_adjacent:
            count += 1
    assert count == 14400
    assert math.factorial(5) * (6 * 5 * 4) == 14400

def check_B5():
    """EXHAUSTIVE PROOF: 4 men and 4 women in a row, alternating."""
    # Men = 0..3, Women = 4..7
    count = 0
    for p in itertools.permutations(range(8)):
        alternating = True
        # Genders: p[i] < 4 is Man, >= 4 is Woman
        genders = [p[i] < 4 for i in range(8)]
        for i in range(7):
            if genders[i] == genders[i+1]:
                alternating = False
                break
        if alternating:
            count += 1
    assert count == 1152
    assert 2 * math.factorial(4) * math.factorial(4) == 1152

def check_B6():
    """EXHAUSTIVE PROOF: 6 around a table, two particular people (0 and 1) together."""
    count = 0
    for p in circular_permutations(6):
        if are_circular_adjacent(p, 0, 1):
            count += 1
    assert count == 48
    assert 2 * math.factorial(4) == 48

def check_B7():
    """EXHAUSTIVE PROOF: 6-digit strings from 1,1,2,2,3,3."""
    ans_val = len(unique_permutations([1, 1, 2, 2, 3, 3]))
    assert ans_val == 90
    assert math.factorial(6) // (2 * 2 * 2) == 90

def check_B8():
    """EXHAUSTIVE PROOF: arrangements of LEVEL."""
    ans_val = len(unique_permutations("LEVEL"))
    assert ans_val == 30
    assert math.factorial(5) // (2 * 2) == 30

def check_B9():
    """EXHAUSTIVE PROOF: 7 books, trilogy (0, 1, 2) in volume order (not necessarily adjacent)."""
    count = 0
    for p in itertools.permutations(range(7)):
        idx_0 = p.index(0)
        idx_1 = p.index(1)
        idx_2 = p.index(2)
        if idx_0 < idx_1 < idx_2:
            count += 1
    assert count == 840
    assert math.factorial(7) // math.factorial(3) == 840

def check_B10():
    """SAMPLED CHECK: solve (n-1)! == 720, verifying unique solution n=7."""
    solutions = [n for n in range(2, 20) if math.factorial(n - 1) == 720]
    assert len(solutions) == 1
    assert solutions[0] == 7

# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: 8 in a row, three friends consecutive (0,1,2),
    two enemies (3,4) not adjacent."""
    count = 0
    for p in itertools.permutations(range(8)):
        # 3 friends consecutive: difference of max/min indices is 2
        idx_f = [p.index(0), p.index(1), p.index(2)]
        consecutive = (max(idx_f) - min(idx_f)) == 2
        
        # 2 enemies not adjacent
        idx_3 = p.index(3)
        idx_4 = p.index(4)
        not_adj = abs(idx_3 - idx_4) != 1
        
        if consecutive and not_adj:
            count += 1
            
    assert count == 2880
    assert math.factorial(3) * math.factorial(6) - math.factorial(3) * math.factorial(2) * math.factorial(5) == 2880

def check_C2():
    """EXHAUSTIVE PROOF: same 8, friends (0,1,2) consecutive and in order."""
    count = 0
    for p in itertools.permutations(range(8)):
        idx_0 = p.index(0)
        idx_1 = p.index(1)
        idx_2 = p.index(2)
        if idx_1 == idx_0 + 1 and idx_2 == idx_1 + 1:
            count += 1
    assert count == 720
    assert math.factorial(6) == 720

def check_C3():
    """EXHAUSTIVE PROOF: arrangements of DIVIDED without all three D's together."""
    # DIVIDED: D (0,1,2), I (3,4), V (5), E (6)
    all_perms = unique_permutations(['D', 'I', 'V', 'I', 'D', 'E', 'D'])
    assert len(all_perms) == 420
    
    # Filter those where the three D's are together
    count_not_together = 0
    for p in all_perms:
        # Check if D's are together: find all indices of D in p
        d_indices = [i for i, char in enumerate(p) if char == 'D']
        if max(d_indices) - min(d_indices) != 2:
            count_not_together += 1
            
    assert count_not_together == 360
    assert 420 - 60 == 360

def check_C4():
    """EXHAUSTIVE PROOF: 4 men and 4 women alternating around table circular arrangements."""
    # Men = 0..3, Women = 4..7
    count = 0
    for p in circular_permutations(8):
        # genders check
        genders = [p[i] < 4 for i in range(8)]
        alternating = True
        for i in range(7):
            if genders[i] == genders[i+1]:
                alternating = False
                break
        if alternating:
            count += 1
    assert count == 144
    assert math.factorial(3) * math.factorial(4) == 144

def check_C5():
    """EXHAUSTIVE PROOF: arrangements of CIRCLE with two C's apart."""
    all_perms = unique_permutations(['C', 'I', 'R', 'C', 'L', 'E'])
    assert len(all_perms) == 360
    
    count_apart = 0
    for p in all_perms:
        c_indices = [i for i, char in enumerate(p) if char == 'C']
        if abs(c_indices[0] - c_indices[1]) != 1:
            count_apart += 1
            
    assert count_apart == 240
    assert 360 - 120 == 240

def check_C6():
    """EXHAUSTIVE PROOF: 5-digit even numbers over 40,000 using 1,2,3,4,5 once."""
    count = 0
    for p in itertools.permutations([1, 2, 3, 4, 5]):
        val = p[0]*10000 + p[1]*1000 + p[2]*100 + p[3]*10 + p[4]
        if val > 40000 and val % 2 == 0:
            count += 1
    assert count == 18

def check_C7():
    """EXHAUSTIVE PROOF: 3 maths (0,1,2), 2 physics (3,4), 2 chemistry (5,6) books, subjects together."""
    count = 0
    for p in itertools.permutations(range(7)):
        # Maths block check
        math_idx = [p.index(0), p.index(1), p.index(2)]
        math_together = (max(math_idx) - min(math_idx)) == 2
        
        # Physics block check
        phys_idx = [p.index(3), p.index(4)]
        phys_together = (max(phys_idx) - min(phys_idx)) == 1
        
        # Chemistry block check
        chem_idx = [p.index(5), p.index(6)]
        chem_together = (max(chem_idx) - min(chem_idx)) == 1
        
        if math_together and phys_together and chem_together:
            count += 1
            
    assert count == 144
    assert math.factorial(3) * (math.factorial(3) * math.factorial(2) * math.factorial(2)) == 144

def check_C8():
    """EXHAUSTIVE PROOF: 8 people around a table, two (0 and 1) refusing to be adjacent."""
    count = 0
    for p in circular_permutations(8):
        if not are_circular_adjacent(p, 0, 1):
            count += 1
    assert count == 3600
    assert math.factorial(7) - 2 * math.factorial(6) == 3600

# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: 7-digit numbers from 1..7, odds (1,3,5,7) increasing, evens (2,4,6) decreasing."""
    count = 0
    for p in itertools.permutations(range(1, 8)):
        odds = [x for x in p if x % 2 == 1]
        evens = [x for x in p if x % 2 == 0]
        if odds == [1, 3, 5, 7] and evens == [6, 4, 2]:
            count += 1
    assert count == 35
    assert math.comb(7, 4) == 35

def check_D2():
    """EXHAUSTIVE PROOF: 10 children in circle, Mia (0) and Noah (1) adjacent, Omar (2) and Priya (3) not."""
    count = 0
    for p in circular_permutations(10):
        if are_circular_adjacent(p, 0, 1) and not are_circular_adjacent(p, 2, 3):
            count += 1
    assert count == 60480
    assert 2 * math.factorial(8) - 4 * math.factorial(7) == 60480

def check_D3():
    """EXHAUSTIVE PROOF: unique permutations of AABBCC with no two identical letters adjacent."""
    all_perms = unique_permutations(['A', 'A', 'B', 'B', 'C', 'C'])
    assert len(all_perms) == 90
    
    count = 0
    for p in all_perms:
        adjacent = False
        for i in range(5):
            if p[i] == p[i+1]:
                adjacent = True
                break
        if not adjacent:
            count += 1
            
    assert count == 30

def check_D4():
    """EXHAUSTIVE PROOF: 8 people in a row, exactly two of three sisters (0,1,2) adjacent."""
    sisters = {0, 1, 2}
    count = 0
    for p in itertools.permutations(range(8)):
        # count adjacent sisters pairs
        adj_pairs = 0
        for i in range(7):
            if p[i] in sisters and p[i+1] in sisters:
                adj_pairs += 1
        if adj_pairs == 1:
            count += 1
            
    assert count == 21600
    assert math.factorial(8) - 14400 - 4320 == 21600

def check_D5():
    """EXHAUSTIVE PROOF: 8 knights around table, 3 feuders (2,3,4) pairwise non-adjacent, King (0) and Queen (1) together."""
    count = 0
    for p in circular_permutations(8):
        # King and Queen adjacent
        kq_adj = are_circular_adjacent(p, 0, 1)
        
        # Feuders pairwise non-adjacent
        feuders_peaceful = (
            not are_circular_adjacent(p, 2, 3) and
            not are_circular_adjacent(p, 3, 4) and
            not are_circular_adjacent(p, 2, 4)
        )
        
        if kq_adj and feuders_peaceful:
            count += 1
            
    assert count == 288
    assert math.factorial(3) * 2 * (4 * 3 * 2) == 288

# ═══════════════════════════════════════════════════════════════════════
# Execution setup
# ═══════════════════════════════════════════════════════════════════════

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
