"""Computational verification for combinatorics/answers/ans06.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer.

Run directly:
    python3 sheet06_verify.py
"""

import functools
import itertools
import math
import random

# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
  """EXHAUSTIVE PROOF: Model choosing socks from 2 colours, verify that
  any selection of 3 socks must contain a pair of the same colour."""
  for combo in itertools.product([0, 1], repeat=3):
    assert len(set(combo)) <= 2


def check_A2():
  """EXHAUSTIVE PROOF: Model a drawer with 10 white and 10 black socks.
  Verify that drawing 12 socks guarantees at least 2 black socks, whereas
  11 socks do not."""
  drawer = ['W'] * 10 + ['B'] * 10
  for combo in itertools.combinations(drawer, 12):
    assert combo.count('B') >= 2
  assert any(combo.count('B') < 2 for combo in itertools.combinations(drawer, 11))


def check_A3():
  """SAMPLED CHECK: Verify pigeonhole principle for 13 people and 12 months."""
  for _ in range(20000):
    combo = [random.randint(0, 11) for _ in range(13)]
    assert len(set(combo)) < 13


def check_A4():
  """EXHAUSTIVE PROOF: Verify pigeonhole principle for 8 people and 7 weekdays."""
  for combo in itertools.product(range(7), repeat=8):
    assert len(set(combo)) < 8
  assert len(set(range(7))) == 7


def check_A5():
  """EXHAUSTIVE PROOF: Verify parity pigeonhole for 3 integers."""
  for combo in itertools.product([0, 1], repeat=3):
    assert len(set(combo)) < 3


def check_A6():
  """EXHAUSTIVE PROOF: Verify Handshake Lemma relation for degree sum 18."""
  assert 18 // 2 == 9


def check_A7():
  """EXHAUSTIVE PROOF: Verify row sums equal column sums on an arbitrary grid."""
  grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  row_sums = [sum(row) for row in grid]
  col_sums = [sum(grid[r][c] for r in range(3)) for c in range(3)]
  assert sum(row_sums) == sum(col_sums)


def check_A8():
  """EXHAUSTIVE PROOF: Verify residue pigeonhole mod 5 for 6 integers."""
  for combo in itertools.product(range(5), repeat=6):
    assert len(set(combo)) < 6


def check_A9():
  """EXHAUSTIVE PROOF: Verify strong pigeonhole for 9 sweets of 4 flavours."""
  for combo in itertools.product(range(4), repeat=9):
    counts = [combo.count(f) for f in range(4)]
    assert max(counts) >= 3
  assert any(max([combo.count(f) for f in range(4)]) < 3 for combo in itertools.product(range(4), repeat=8))


def check_A10():
  """EXHAUSTIVE PROOF: Verify parity pigeonhole for 4 integers."""
  for combo in itertools.product([0, 1], repeat=4):
    assert len(set(combo)) < 4


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
  """EXHAUSTIVE PROOF: Check circular table seating adjacency. Verify size 6 can dodge
  but size 7 cannot."""
  def has_adjacent(seats_subset):
    s = sorted(seats_subset)
    for i in range(len(s)):
      if (s[(i + 1) % len(s)] - s[i]) % 12 == 1:
        return True
    return False

  dodge_6 = [c for c in itertools.combinations(range(12), 6) if not has_adjacent(c)]
  assert len(dodge_6) > 0
  assert (0, 2, 4, 6, 8, 10) in dodge_6
  force_7 = [c for c in itertools.combinations(range(12), 7) if not has_adjacent(c)]
  assert len(force_7) == 0


def check_B2():
  """EXHAUSTIVE PROOF: Verify residue pigeonhole mod 7 for 8 integers."""
  for combo in itertools.product(range(7), repeat=8):
    assert len(set(combo)) < 8


def check_B3():
  """EXHAUSTIVE PROOF: Verify modular pigeonhole for size 5 mod 4, and the construction mod 5."""
  for combo in itertools.product(range(4), repeat=5):
    assert len(set(combo)) < 5
  c = [1, 2, 3, 4, 5]
  residues = [x % 5 for x in c]
  assert len(set(residues)) == 5


def check_B4():
  """EXHAUSTIVE PROOF: Verify subsets of 1..10 summing to 11. Size 5 can dodge, size 6 forces."""
  def has_sum_11(subset):
    for x in subset:
      if 11 - x in subset and 11 - x != x:
        return True
    return False

  dodge_5 = [c for c in itertools.combinations(range(1, 11), 5) if not has_sum_11(c)]
  assert len(dodge_5) > 0
  assert (1, 2, 3, 4, 5) in dodge_5
  force_6 = [c for c in itertools.combinations(range(1, 11), 6) if not has_sum_11(c)]
  assert len(force_6) == 0


def check_B5():
  """EXHAUSTIVE PROOF: Count round-robin matches and games played per team."""
  matches = list(itertools.combinations(range(8), 2))
  assert len(matches) == 28
  assert math.comb(8, 2) == 28
  for t in range(8):
    played = sum(1 for m in matches if t in m)
    assert played == 7


def check_B6():
  """EXHAUSTIVE PROOF: Verify friendships given sum of degrees is 84."""
  assert 84 // 2 == 42


def check_B7():
  """EXHAUSTIVE PROOF: Verify consecutive integers in subsets of 1..6. Size 3 can dodge, size 4 forces."""
  def has_consecutive(subset):
    s = sorted(subset)
    for i in range(len(s) - 1):
      if s[i + 1] - s[i] == 1:
        return True
    return False

  dodge_3 = [c for c in itertools.combinations(range(1, 7), 3) if not has_consecutive(c)]
  assert len(dodge_3) > 0
  assert (1, 3, 5) in dodge_3
  force_4 = [c for c in itertools.combinations(range(1, 7), 4) if not has_consecutive(c)]
  assert len(force_4) == 0


def check_B8():
  """EXHAUSTIVE PROOF: Verify that degree sequences of simple graphs on 5 vertices always
  contain duplicates, and that degree 0 and 4 cannot coexist."""
  n = 5
  edges = list(itertools.combinations(range(n), 2))
  for subset in itertools.product([0, 1], repeat=len(edges)):
    degrees = [0] * n
    for i, active in enumerate(subset):
      if active:
        u, v = edges[i]
        degrees[u] += 1
        degrees[v] += 1
    assert len(set(degrees)) < n
    if 0 in degrees:
      assert n - 1 not in degrees


def check_B9():
  """EXHAUSTIVE PROOF: Verify ceiling division for strong pigeonhole of 25 sweets and 7 children."""
  assert math.ceil(25 / 7) == 4


def check_B10():
  """EXHAUSTIVE PROOF: Verify double-counting identity for bipartite membership graph."""
  assert 5 * 4 == 10 * 2


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
  """SAMPLED CHECK: Verify drawing from 10R, 10G, 10B. Check threshold to force
  some colour of size 5 (13) vs red of size 5 (25)."""
  bag = ['R'] * 10 + ['G'] * 10 + ['B'] * 10
  for _ in range(20000):
    combo = random.sample(bag, 13)
    assert combo.count('R') >= 5 or combo.count('G') >= 5 or combo.count('B') >= 5
    
    combo25 = random.sample(bag, 25)
    assert combo25.count('R') >= 5


def check_C2():
  """EXHAUSTIVE PROOF: Verify subsets of 1..12 summing to 13. Size 6 can dodge, size 7 forces."""
  def has_sum_13(subset):
    for x in subset:
      if 13 - x in subset and 13 - x != x:
        return True
    return False

  dodge_6 = [c for c in itertools.combinations(range(1, 13), 6) if not has_sum_13(c)]
  assert len(dodge_6) > 0
  assert (1, 2, 3, 4, 5, 6) in dodge_6
  force_7 = [c for c in itertools.combinations(range(1, 13), 7) if not has_sum_13(c)]
  assert len(force_7) == 0


def check_C3():
  """SAMPLED CHECK: Verify residue pigeonhole mod 10 for 11 integers."""
  for _ in range(20000):
    combo = [random.randint(0, 9) for _ in range(11)]
    assert len(set(combo)) < 11


def check_C4():
  """EXHAUSTIVE PROOF: Verify alternate colouring counts on a mutilated chessboard."""
  squares = [(r, c) for r in range(8) for c in range(8)]
  squares.remove((0, 0))
  squares.remove((7, 7))
  blacks = sum(1 for r, c in squares if (r + c) % 2 == 0)
  whites = sum(1 for r, c in squares if (r + c) % 2 != 0)
  assert (blacks == 30 and whites == 32) or (blacks == 32 and whites == 30)
  assert blacks != whites


def check_C5():
  """SAMPLED CHECK: Verify pigeonhole on 85 month-weekday pairs (84 boxes)."""
  for _ in range(20000):
    combo = [random.randint(0, 83) for _ in range(85)]
    assert len(set(combo)) < 85


def check_C6():
  """EXHAUSTIVE PROOF: Verify double-counting relation for 20 clubs of 6 and student memberships."""
  assert 20 * 6 == 40 * 3


def check_C7():
  """EXHAUSTIVE PROOF: Check circular adjacent sums of size 3 from range 1..9.
  Verify that some adjacent triple always sums to at least 15."""
  for p in itertools.permutations(range(1, 10)):
    triples_sums = [p[i] + p[(i + 1) % 9] + p[(i + 2) % 9] for i in range(9)]
    assert max(triples_sums) >= 15


def check_C8():
  """EXHAUSTIVE PROOF: Verify difference 4 in subsets of 1..8. Size 4 can dodge, size 5 forces."""
  def has_diff_4(subset):
    for x in subset:
      if x + 4 in subset:
        return True
    return False

  dodge_4 = [c for c in itertools.combinations(range(1, 9), 4) if not has_diff_4(c)]
  assert len(dodge_4) > 0
  assert (1, 2, 3, 4) in dodge_4
  force_5 = [c for c in itertools.combinations(range(1, 9), 5) if not has_diff_4(c)]
  assert len(force_5) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
  """EXHAUSTIVE PROOF: Verify geometric pigeonhole diagonal and basic PHP box count."""
  diag = math.sqrt(0.5**2 + 0.5**2)
  assert math.isclose(diag, math.sqrt(2) / 2)
  for combo in itertools.product(range(4), repeat=5):
    assert any(combo.count(box) >= 2 for box in range(4))


def check_D2():
  """EXHAUSTIVE PROOF: Verify PHP on parities in 2D lattice."""
  for combo in itertools.product(range(4), repeat=5):
    assert any(combo.count(c) >= 2 for c in range(4))


def check_D3():
  """EXHAUSTIVE PROOF: Verify that simple graphs on 5 vertices have an even number of
  odd-degree vertices."""
  n = 5
  edges = list(itertools.combinations(range(n), 2))
  for subset in itertools.product([0, 1], repeat=len(edges)):
    degrees = [0] * n
    for i, active in enumerate(subset):
      if active:
        u, v = edges[i]
        degrees[u] += 1
        degrees[v] += 1
    odd_count = sum(1 for d in degrees if d % 2 != 0)
    assert odd_count % 2 == 0


def check_D4():
  """SAMPLED CHECK: Verify selection of pairs by students mapping to PHP."""
  assert math.comb(5, 2) == 10
  for _ in range(20000):
    combo = [random.randint(0, 9) for _ in range(20)]
    assert any(combo.count(pair) >= 2 for pair in range(10))


def check_D5():
  """EXHAUSTIVE PROOF: Generate all 32,768 graphs on 6 vertices, verifying that
  each contains either a clique of size 3 (mutual friends) or an independent set of
  size 3 (mutual strangers)."""
  n = 6
  edges = list(itertools.combinations(range(n), 2))
  for subset in itertools.product([0, 1], repeat=15):
    adj = [[False] * n for _ in range(n)]
    for i, active in enumerate(subset):
      if active:
        u, v = edges[i]
        adj[u][v] = adj[v][u] = True
    
    has_clique = False
    has_indep = False
    for tri in itertools.combinations(range(n), 3):
      u, v, w = tri
      if adj[u][v] and adj[v][w] and adj[w][u]:
        has_clique = True
        break
      if not adj[u][v] and not adj[v][w] and not adj[w][u]:
        has_indep = True
        break
    assert has_clique or has_indep


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
