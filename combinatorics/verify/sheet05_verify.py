"""Computational verification for combinatorics/answers/ans05.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer.

Run directly:
    python3 sheet05_verify.py
"""

import functools
import itertools
import math

# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
  """EXHAUSTIVE PROOF: Count non-negative pairs (x,y) with x+y=10 directly
  and verify the method's claim about x taking values from 0 to 10."""
  ans_val = sum(1 for x in range(11) for y in range(11) if x + y == 10)
  assert ans_val == 11, f"Expected 11, got {ans_val}"
  x_vals = [x for x in range(11) if 10 - x >= 0]
  assert x_vals == list(range(11)), f"Expected x from 0 to 10, got {x_vals}"


def check_A2():
  """EXHAUSTIVE PROOF: Count distributions of 5 identical sweets to 3 children
  by generating all valid tuples (x,y,z) and verify stars and bars formula."""
  triples = [(x, y, z) for x in range(6) for y in range(6) for z in range(6) if x + y + z == 5]
  assert len(triples) == 21, f"Expected 21 distributions, got {len(triples)}"
  assert math.comb(7, 2) == 21, "Stars and bars formula mismatch"


def check_A3():
  """EXHAUSTIVE PROOF: Verify two-set inclusion-exclusion by instantiating concrete
  sets A and B with sizes 15 and 12 overlapping by 5, checking their union size."""
  A = set(range(15))
  B = set(range(10, 22))
  assert len(A) == 15
  assert len(B) == 12
  assert len(A & B) == 5
  assert len(A | B) == 22, f"Expected union size 22, got {len(A | B)}"
  assert 15 + 12 - 5 == 22


def check_A4():
  """EXHAUSTIVE PROOF: Count multiples of 3 in 1..100 directly and check quotient floor."""
  multiples = [n for n in range(1, 101) if n % 3 == 0]
  assert len(multiples) == 33, f"Expected 33 multiples, got {len(multiples)}"
  assert 100 // 3 == 33


def check_A5():
  """EXHAUSTIVE PROOF: Verify intersection size for two sets with sizes 8 and 6
  and union size 11 by constructing concrete sets."""
  A = set(range(8))
  B = set(range(5, 11))
  assert len(A) == 8
  assert len(B) == 6
  assert len(A | B) == 11
  assert len(A & B) == 3, f"Expected intersection size 3, got {len(A & B)}"
  assert 8 + 6 - 11 == 3


def check_A6():
  """EXHAUSTIVE PROOF: Count non-negative triples x+y+z=4 directly and verify
  stars and bars formula."""
  triples = [(x, y, z) for x in range(5) for y in range(5) for z in range(5) if x + y + z == 4]
  assert len(triples) == 15, f"Expected 15 triples, got {len(triples)}"
  assert math.comb(6, 2) == 15


def check_A7():
  """EXHAUSTIVE PROOF: Count positive triples x+y+z=6 directly and verify the shift method."""
  triples = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7) if x + y + z == 6]
  assert len(triples) == 10, f"Expected 10 positive triples, got {len(triples)}"
  assert math.comb(5, 2) == 10


def check_A8():
  """EXHAUSTIVE PROOF: Model the class of 30 with sets for French and German,
  verifying the complement (neither)."""
  french = set(range(20))
  german = set(range(12, 27))
  universe = set(range(30))
  assert len(french) == 20
  assert len(german) == 15
  assert len(french & german) == 8
  neither = universe - (french | german)
  assert len(neither) == 3, f"Expected 3, got {len(neither)}"
  assert 30 - (20 + 15 - 8) == 3


def check_A9():
  """EXHAUSTIVE PROOF: Generate and count ordered two-part positive sums of 7."""
  sums = [(x, y) for x in range(1, 8) for y in range(1, 8) if x + y == 7]
  assert len(sums) == 6, f"Expected 6 sums, got {len(sums)}"
  assert all(1 <= x <= 6 for x, y in sums)


def check_A10():
  """EXHAUSTIVE PROOF: Count pairs (x,y) of non-negative integers summing to 4."""
  pairs = [(x, y) for x in range(5) for y in range(5) if x + y == 4]
  assert len(pairs) == 5, f"Expected 5 pairs, got {len(pairs)}"


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
  """EXHAUSTIVE PROOF: Count non-negative triples x+y+z=12 directly."""
  triples = [(x, y, z) for x in range(13) for y in range(13) for z in range(13) if x + y + z == 12]
  assert len(triples) == 91, f"Expected 91 triples, got {len(triples)}"
  assert math.comb(14, 2) == 91


def check_B2():
  """EXHAUSTIVE PROOF: Count positive triples x+y+z=12 directly."""
  triples = [(x, y, z) for x in range(1, 13) for y in range(1, 13) for z in range(1, 13) if x + y + z == 12]
  assert len(triples) == 55, f"Expected 55 triples, got {len(triples)}"
  assert math.comb(11, 2) == 55


def check_B3():
  """EXHAUSTIVE PROOF: Count positive quadruples summing to 10 directly."""
  quads = [(x, y, z, w) for x in range(1, 11) for y in range(1, 11) for z in range(1, 11) for w in range(1, 11) if x + y + z + w == 10]
  assert len(quads) == 84, f"Expected 84 ways, got {len(quads)}"
  assert math.comb(9, 3) == 84


def check_B4():
  """EXHAUSTIVE PROOF: Count numbers in 1..1000 not divisible by 2 and not divisible by 5."""
  nums = [n for n in range(1, 1001) if n % 2 != 0 and n % 5 != 0]
  assert len(nums) == 400, f"Expected 400, got {len(nums)}"
  assert 1000 - 500 - 200 + 100 == 400


def check_B5():
  """EXHAUSTIVE PROOF: Count non-negative triples x+y+z=10 with x >= 2."""
  triples = [(x, y, z) for x in range(2, 11) for y in range(11) for z in range(11) if x + y + z == 10]
  assert len(triples) == 45, f"Expected 45 triples, got {len(triples)}"
  assert math.comb(10, 2) == 45


def check_B6():
  """EXHAUSTIVE PROOF: Count arrangements of [1, 2, 3, 4] with 1 not first."""
  perms = list(itertools.permutations([1, 2, 3, 4]))
  valid = [p for p in perms if p[0] != 1]
  assert len(valid) == 18, f"Expected 18 arrangements, got {len(valid)}"
  assert len(perms) == 24
  assert sum(1 for p in perms if p[0] == 1) == 6
  assert 24 - 6 == 18


def check_B7():
  """EXHAUSTIVE PROOF: Count numbers in 1..100 divisible by 2 or 3."""
  nums = [n for n in range(1, 101) if n % 2 == 0 or n % 3 == 0]
  assert len(nums) == 67, f"Expected 67 numbers, got {len(nums)}"
  assert 50 + 33 - 16 == 67


def check_B8():
  """EXHAUSTIVE PROOF: Count positive triples x+y+z=8 directly."""
  triples = [(x, y, z) for x in range(1, 9) for y in range(1, 9) for z in range(1, 9) if x + y + z == 8]
  assert len(triples) == 21, f"Expected 21 triples, got {len(triples)}"
  assert math.comb(7, 2) == 21


def check_B9():
  """EXHAUSTIVE PROOF: Count non-negative pairs with sum <= 5 directly."""
  pairs = [(x, y) for x in range(6) for y in range(6) if x + y <= 5]
  assert len(pairs) == 21, f"Expected 21 pairs, got {len(pairs)}"
  triples = [(x, y, s) for x in range(6) for y in range(6) for s in range(6) if x + y + s == 5]
  assert len(triples) == 21
  assert math.comb(7, 2) == 21


def check_B10():
  """EXHAUSTIVE PROOF: Count 5-letter A/B strings using both letters."""
  strings = ["".join(p) for p in itertools.product('AB', repeat=5)]
  valid = [s for s in strings if 'A' in s and 'B' in s]
  assert len(valid) == 30, f"Expected 30 strings, got {len(valid)}"
  assert len(strings) == 32
  assert 32 - 2 == 30


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
  """EXHAUSTIVE PROOF: Count positive quadruples summing to 15, each <= 5,
  and verify the inclusion-exclusion values."""
  quads = [(x, y, z, w) for x in range(1, 6) for y in range(1, 6) for z in range(1, 6) for w in range(1, 6) if x + y + z + w == 15]
  assert len(quads) == 52, f"Expected 52 quadruples, got {len(quads)}"
  
  unrestricted = math.comb(14, 3)
  assert unrestricted == 364
  single_violation = math.comb(9, 3) * 4
  assert single_violation == 336
  double_violation = math.comb(4, 3) * 6
  assert double_violation == 24
  assert unrestricted - single_violation + double_violation == 52


def check_C2():
  """EXHAUSTIVE PROOF: Count non-negative triples summing to 15, each <= 6,
  and verify the inclusion-exclusion values."""
  triples = [(x, y, z) for x in range(7) for y in range(7) for z in range(7) if x + y + z == 15]
  assert len(triples) == 10, f"Expected 10 triples, got {len(triples)}"
  
  assert math.comb(17, 2) == 136
  assert math.comb(10, 2) * 3 == 135
  assert math.comb(3, 2) * 3 == 9
  assert 136 - 135 + 9 == 10


def check_C3():
  """EXHAUSTIVE PROOF: Verify three-set inclusion-exclusion on concrete sets."""
  T = set(range(0, 5)) | set(range(5, 15)) | set(range(15, 30)) | set(range(35, 55))
  C = set(range(0, 5)) | set(range(15, 30)) | set(range(30, 35)) | set(range(55, 70))
  J = set(range(0, 5)) | set(range(5, 15))  | set(range(30, 35)) | set(range(70, 80))
  
  assert len(T) == 50
  assert len(C) == 40
  assert len(J) == 30
  assert len(T & C) == 20
  assert len(T & J) == 15
  assert len(C & J) == 10
  assert len(T & C & J) == 5
  
  union_size = len(T | C | J)
  assert union_size == 80
  assert 50 + 40 + 30 - 20 - 15 - 10 + 5 == 80
  assert 100 - union_size == 20


def check_C4():
  """EXHAUSTIVE PROOF: Count numbers in 1..1000 divisible by 2, 3, or 5."""
  divisible = [n for n in range(1, 1001) if n % 2 == 0 or n % 3 == 0 or n % 5 == 0]
  assert len(divisible) == 734, f"Expected 734 numbers, got {len(divisible)}"
  
  assert sum(1 for n in range(1, 1001) if n % 2 == 0) == 500
  assert sum(1 for n in range(1, 1001) if n % 3 == 0) == 333
  assert sum(1 for n in range(1, 1001) if n % 5 == 0) == 200
  assert sum(1 for n in range(1, 1001) if n % 6 == 0) == 166
  assert sum(1 for n in range(1, 1001) if n % 10 == 0) == 100
  assert sum(1 for n in range(1, 1001) if n % 15 == 0) == 66
  assert sum(1 for n in range(1, 1001) if n % 30 == 0) == 33
  assert 500 + 333 + 200 - 166 - 100 - 66 + 33 == 734


def check_C5():
  """EXHAUSTIVE PROOF: Count distributions of 8 apples to 3 children, each at most 4."""
  triples = [(x, y, z) for x in range(5) for y in range(5) for z in range(5) if x + y + z == 8]
  assert len(triples) == 15, f"Expected 15 distributions, got {len(triples)}"
  assert math.comb(10, 2) == 45
  assert math.comb(5, 2) * 3 == 30
  assert 45 - 30 == 15


def check_C6():
  """EXHAUSTIVE PROOF: Count arrangements of ABCDE with A not first, B not second."""
  perms = list(itertools.permutations("ABCDE"))
  valid = [p for p in perms if p[0] != 'A' and p[1] != 'B']
  assert len(valid) == 78, f"Expected 78 arrangements, got {len(valid)}"
  assert len(perms) == 120
  assert sum(1 for p in perms if p[0] == 'A') == 24
  assert sum(1 for p in perms if p[1] == 'B') == 24
  assert sum(1 for p in perms if p[0] == 'A' and p[1] == 'B') == 6
  assert 120 - 24 - 24 + 6 == 78


def check_C7():
  """EXHAUSTIVE PROOF: Count three dice summing to 10."""
  dice = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7) if x + y + z == 10]
  assert len(dice) == 27, f"Expected 27 ways, got {len(dice)}"
  assert math.comb(9, 2) == 36
  assert math.comb(3, 2) * 3 == 9
  assert 36 - 9 == 27


def check_C8():
  """EXHAUSTIVE PROOF: Count integers in 1..999 with digit sum 12."""
  ans_val = 0
  for n in range(1, 1000):
    d1 = n // 100
    d2 = (n // 10) % 10
    d3 = n % 10
    if d1 + d2 + d3 == 12:
      ans_val += 1
  assert ans_val == 73, f"Expected 73 numbers, got {ans_val}"
  assert math.comb(14, 2) == 91
  assert math.comb(4, 2) * 3 == 18
  assert 91 - 18 == 73


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
  """EXHAUSTIVE PROOF: Count derangements of a 4-element set."""
  perms = list(itertools.permutations(range(4)))
  derangements = [p for p in perms if all(p[i] != i for i in range(4))]
  assert len(derangements) == 9, f"Expected 9 derangements, got {len(derangements)}"
  assert math.comb(4, 1) * math.factorial(3) - math.comb(4, 2) * math.factorial(2) + math.comb(4, 3) * math.factorial(1) - math.comb(4, 4) * math.factorial(0) == 15
  assert 24 - 15 == 9


def check_D2():
  """EXHAUSTIVE PROOF: Verify composition count formula by generating compositions recursively."""
  def count_compositions(n):
    if n == 0:
      return 1
    if n < 0:
      return 0
    return sum(count_compositions(n - i) for i in range(1, n + 1))
  
  for n in range(1, 16):
    assert count_compositions(n) == 2**(n-1), f"Failed for n={n}"


def check_D3():
  """EXHAUSTIVE PROOF: Count integers 1..360 coprime to 360 and verify inclusion-exclusion."""
  coprime = [n for n in range(1, 361) if math.gcd(n, 360) == 1]
  assert len(coprime) == 96, f"Expected 96 coprime numbers, got {len(coprime)}"
  assert 360 - 180 - 120 - 72 + 60 + 36 + 24 - 12 == 96


def check_D4():
  """EXHAUSTIVE PROOF: Count surjective assignments from 5 students to 3 clubs."""
  assignments = list(itertools.product(range(3), repeat=5))
  surjections = [a for a in assignments if len(set(a)) == 3]
  assert len(surjections) == 150, f"Expected 150 surjections, got {len(surjections)}"
  assert len(assignments) == 243
  assert 3**5 - 3 * 2**5 + 3 * 1**5 == 150


def check_D5():
  """EXHAUSTIVE PROOF: Count numbers in 1..10^6 that are neither squares nor cubes."""
  squares = {i**2 for i in range(1, 1001)}
  cubes = {i**3 for i in range(1, 101)}
  assert len(squares) == 1000
  assert len(cubes) == 100
  sixth_powers = squares & cubes
  assert len(sixth_powers) == 10
  assert sixth_powers == {i**6 for i in range(1, 11)}
  squares_or_cubes = squares | cubes
  assert len(squares_or_cubes) == 1090
  assert 10**6 - len(squares_or_cubes) == 998910


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
