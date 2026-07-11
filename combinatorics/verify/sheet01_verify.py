"""Computational verification for combinatorics/answers/ans01.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...). Each function must:

  1. Independently re-derive the \\ans{} value (brute force, direct
     computation, or a full game-tree/DP solve — not a copy of the method's
     arithmetic) and assert it matches.
  2. Assert every checkable factual/numeric claim made in the \\method{}
     text — not just the final answer. A correct \\ans{} sitting on a
     \\method{} whose intermediate step doesn't actually check out is a
     documentation bug this script exists to catch.

Claims that are pure framing or motivation ("this is startling", "the
surest way to find a recurrence") are not checkable statements and are
left alone on purpose — that's still a human reviewer's job.

Run directly:
    python3 sheet01_verify.py
"""

import functools
import itertools
import math

# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────
# A1 — Evaluate 5!. \ans{120}
# \method claims: 5*4*3*2*1 = 120; 1! through 7! are 1,2,6,24,120,720,5040.
# ─────────────────────────────────────────────────────────────────────────
def check_A1():
    """EXHAUSTIVE PROOF: 5! independently re-derived by counting permutations
    of a 5-element set (not by multiplying 5*4*3*2*1, which is the method's
    own route). Also checks the method's stated factorial ladder 1!..7!."""
    ans_val = len(list(itertools.permutations(range(5))))
    assert ans_val == 120, f"Expected 5! to be 120, got {ans_val}"

    assert 5 * 4 * 3 * 2 * 1 == 120, "5*4*3*2*1 calculation mismatch"

    expected_factorials = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}
    for k, expected_val in expected_factorials.items():
        perms_len = len(list(itertools.permutations(range(k))))
        assert perms_len == expected_val, f"Expected {k}! to be {expected_val}, got {perms_len}"


# ─────────────────────────────────────────────────────────────────────────
# A2 — Simplify 8!/6!. \ans{56}
# \method claims: 8!/6! = 8*7 = 56.
# ─────────────────────────────────────────────────────────────────────────
def check_A2():
    """EXHAUSTIVE PROOF: 8!/6! independently re-derived as the count of
    2-permutations of an 8-element set (itertools.permutations), a route
    that never touches the method's cancellation trick."""
    ans_val = len(list(itertools.permutations(range(8), 2)))
    assert ans_val == 56, f"Expected 8!/6! to be 56, got {ans_val}"
    assert 8 * 7 == 56, "8*7 calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A3 — 4 starters, 5 mains, 3 desserts: three-course meals. \ans{60}
# \method claims: 4*5*3 = 60.
# ─────────────────────────────────────────────────────────────────────────
def check_A3():
    """EXHAUSTIVE PROOF: full Cartesian product of the three menus is
    materialised and counted directly."""
    meals = list(itertools.product(range(4), range(5), range(3)))
    assert len(meals) == 60, f"Expected 60 meals, got {len(meals)}"
    assert 4 * 5 * 3 == 60, "4*5*3 calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A4 — Arrangements of 4 different books on a shelf. \ans{24}
# \method claims: 4*3*2*1 = 4! = 24.
# ─────────────────────────────────────────────────────────────────────────
def check_A4():
    """EXHAUSTIVE PROOF: all permutations of 4 distinct books generated
    and counted directly via itertools."""
    arrangements = list(itertools.permutations(range(4)))
    assert len(arrangements) == 24, f"Expected 24 arrangements, got {len(arrangements)}"
    assert 4 * 3 * 2 * 1 == 24, "4! calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A5 — Evaluate 6!/(4! 2!). \ans{15}
# \method claims: (6*5)/2 = 15.
# ─────────────────────────────────────────────────────────────────────────
def check_A5():
    """EXHAUSTIVE PROOF: 6!/(4!2!) independently re-derived as C(6,2),
    counted by enumerating all 2-element combinations of a 6-set."""
    combs = list(itertools.combinations(range(6), 2))
    assert len(combs) == 15, f"Expected C(6,2) to be 15, got {len(combs)}"
    assert (6 * 5) // 2 == 15, "(6*5)/2 calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A6 — 3-letter strings from 26 letters, repeats allowed. \ans{26^3=17576}
# \method claims: 26*26*26.
# ─────────────────────────────────────────────────────────────────────────
def check_A6():
    """EXHAUSTIVE PROOF: all length-3 strings over a 26-symbol alphabet with
    repetition are materialised via itertools.product and counted."""
    strings = list(itertools.product(range(26), repeat=3))
    assert len(strings) == 17576, f"Expected 26^3 to be 17576, got {len(strings)}"
    assert 26 * 26 * 26 == 17576, "26*26*26 calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A7 — 3-letter strings from 26 letters, no repeats. \ans{26*25*24=15600}
# \method claims: 26*25*24.
# ─────────────────────────────────────────────────────────────────────────
def check_A7():
    """EXHAUSTIVE PROOF: all length-3 no-repeat strings enumerated via
    itertools.permutations and counted."""
    strings = list(itertools.permutations(range(26), 3))
    assert len(strings) == 15600, f"Expected P(26,3) to be 15600, got {len(strings)}"
    assert 26 * 25 * 24 == 15600, "26*25*24 calculation mismatch"


# ─────────────────────────────────────────────────────────────────────────
# A8 — Solve n! = 720. \ans{n=6}
# \method claims: 6! = 720 (recall).
# ─────────────────────────────────────────────────────────────────────────
def check_A8():
    """EXHAUSTIVE PROOF (over a generously wide finite search): search
    n = 1..15 (n! is already > 720 well before 15) for n! == 720 via
    math.factorial, and confirm n=6 is the unique solution found."""
    import math
    solutions = [n for n in range(1, 16) if math.factorial(n) == 720]
    assert len(solutions) == 1, f"Expected exactly one solution, got {solutions}"
    assert solutions[0] == 6, f"Expected solution n=6, got {solutions[0]}"
    assert len(list(itertools.permutations(range(6)))) == 720, "6! is not 720"


# ─────────────────────────────────────────────────────────────────────────
# A9 — Two-digit numbers with both digits odd. \ans{25}
# \method claims: 5*5 = 25; odd digits are never 0.
# ─────────────────────────────────────────────────────────────────────────
def check_A9():
    """EXHAUSTIVE PROOF: every two-digit number 10..99 is scanned directly
    and filtered by both digits being odd."""
    odd_digits = {1, 3, 5, 7, 9}
    count = sum(1 for num in range(10, 100) if num // 10 in odd_digits and num % 10 in odd_digits)
    assert count == 25, f"Expected 25 such numbers, got {count}"
    assert len(odd_digits) == 5, "Number of odd digits is not 5"
    assert 5 * 5 == 25, "5*5 calculation mismatch"
    assert all(d != 0 for d in odd_digits), "Found zero in odd digits set"


# ─────────────────────────────────────────────────────────────────────────
# A10 — Simplify (n+1)!/(n-1)!. \ans{n(n+1)}
# \method claims: (n+1)! = (n+1)*n*(n-1)!.
# ─────────────────────────────────────────────────────────────────────────
def check_A10():
    """STRONG-BUT-FINITE: this is an algebraic identity in n, so it cannot
    be brute-forced over an infinite domain. Verified for n = 1..30 using
    math.factorial computed directly (a route independent of the method's
    manual cancellation) — strong evidence, not a full symbolic proof."""
    for n in range(1, 31):
        lhs = math.factorial(n + 1) // math.factorial(n - 1)
        rhs = n * (n + 1)
        assert lhs == rhs, f"Identity failed for n={n}: {lhs} != {rhs}"
        assert math.factorial(n + 1) == (n + 1) * n * math.factorial(n - 1), \
            f"Factorial expansion failed for n={n}"


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────
# B1 — 6 people in a line; Amara first. \ans{720; 120}
# \method claims: 6!=720, 5!=120, and 120 = (1/6)*720 by symmetry.
# ─────────────────────────────────────────────────────────────────────────
def check_B1():
    """EXHAUSTIVE PROOF: all 720 permutations of 6 labelled people generated
    directly; both counts (total, and Amara-first) come from filtering that
    same enumeration, not from evaluating 6! and 5! as formulas."""
    people = range(6)
    all_arrangements = list(itertools.permutations(people))
    total_ways = len(all_arrangements)
    assert total_ways == 720, f"Expected 720 arrangements, got {total_ways}"

    amara_first_ways = sum(1 for p in all_arrangements if p[0] == 0)
    assert amara_first_ways == 120, f"Expected 120 with Amara first, got {amara_first_ways}"

    assert amara_first_ways * 6 == total_ways, "Amara-first count should be exactly 1/6 of total"
    assert math.factorial(6) == 720 and math.factorial(5) == 120, "6! / 5! claims wrong"


# ─────────────────────────────────────────────────────────────────────────
# B2 — Simplify n!/(n-2)!, solve =42. \ans{n(n-1); n=7}
# \method claims: consecutive integers with product 42 are 7 and 6.
# ─────────────────────────────────────────────────────────────────────────
def check_B2():
    """EXHAUSTIVE PROOF (over a generous finite range): search n = 2..100
    computing n!/(n-2)! directly via math.factorial (never assuming the
    n(n-1) simplification) and confirm the unique solution is n=7, and that
    the simplification n(n-1) matches the ratio for every n checked."""
    for n in range(2, 100):
        lhs = math.factorial(n) // math.factorial(n - 2)
        rhs = n * (n - 1)
        assert lhs == rhs, f"Simplification failed for n={n}: {lhs} != {rhs}"

    solutions = [n for n in range(2, 100) if math.factorial(n) // math.factorial(n - 2) == 42]
    assert len(solutions) == 1, f"Expected unique solution, found {solutions}"
    assert solutions[0] == 7, f"Expected solution n=7, got {solutions[0]}"
    assert 7 * 6 == 42, "Consecutive integers product check failed"


# ─────────────────────────────────────────────────────────────────────────
# B3 — 4-digit code, digits 0-9, no repeats. \ans{10*9*8*7=5040}
# \method claims: codes may start with 0, so 10*9*8*7.
# ─────────────────────────────────────────────────────────────────────────
def check_B3():
    """EXHAUSTIVE PROOF: all no-repeat 4-digit codes over {0..9} generated
    via itertools.permutations, counted directly."""
    codes = list(itertools.permutations(range(10), 4))
    assert len(codes) == 5040, f"Expected 5040 unique codes, got {len(codes)}"
    assert 10 * 9 * 8 * 7 == 5040, "Formula 10*9*8*7 should equal 5040"
    assert any(p[0] == 0 for p in codes), "Codes starting with 0 should be present (it's a code, not a number)"


# ─────────────────────────────────────────────────────────────────────────
# B4 — 3-digit numbers, all digits different. \ans{9*9*8=648}
# \method claims: hundreds 9, tens 9, units 8.
# ─────────────────────────────────────────────────────────────────────────
def check_B4():
    """EXHAUSTIVE PROOF: explicit nested loops over all 900 three-digit
    numbers (hundreds 1-9, tens/units 0-9), filtering by digit distinctness
    directly — no use of the 9*9*8 product rule."""
    count = 0
    for hundreds in range(1, 10):
        for tens in range(0, 10):
            for units in range(0, 10):
                if hundreds != tens and hundreds != units and tens != units:
                    count += 1
    assert count == 648, f"Expected 648 three-digit numbers with unique digits, got {count}"
    assert 9 * 9 * 8 == 648, "Formula 9*9*8 should equal 648"


# ─────────────────────────────────────────────────────────────────────────
# B5 — Gold/silver/bronze among 8 runners. \ans{8*7*6=336}
# \method claims: P(8,3) = 8!/5!.
# ─────────────────────────────────────────────────────────────────────────
def check_B5():
    """EXHAUSTIVE PROOF: all ordered triples of medal winners generated via
    itertools.permutations(range(8), 3), counted directly."""
    arrangements = list(itertools.permutations(range(8), 3))
    assert len(arrangements) == 336, f"Expected 336 ways, got {len(arrangements)}"
    assert 8 * 7 * 6 == 336, "8*7*6 should be 336"
    assert math.factorial(8) // math.factorial(5) == 336, "8!/5! should be 336"


# ─────────────────────────────────────────────────────────────────────────
# B6 — Arrangements of SPEED. \ans{5!/2!=60}
# \method claims: 5 letters, E repeated twice.
# ─────────────────────────────────────────────────────────────────────────
def check_B6():
    """EXHAUSTIVE PROOF: all 5! permutations of the letter multiset are
    generated and deduplicated as strings via a set — the distinct-string
    count is the independent route, not the 5!/2! formula."""
    word = "SPEED"
    assert len(word) == 5, "Word SPEED must have length 5"
    assert word.count("E") == 2, "E must be repeated twice in SPEED"

    unique_words = set("".join(p) for p in itertools.permutations(word))
    assert len(unique_words) == 60, f"Expected 60 distinct words, got {len(unique_words)}"
    assert math.factorial(5) // math.factorial(2) == 60, "5!/2! should be 60"


# ─────────────────────────────────────────────────────────────────────────
# B7 — 3-stripe flag, 5 colours, adjacent stripes differ. \ans{5*4*4=80}
# \method claims: top 5, each later stripe 4.
# ─────────────────────────────────────────────────────────────────────────
def check_B7():
    """EXHAUSTIVE PROOF: all 5^3 colour triples enumerated via
    itertools.product and filtered by the adjacent-different rule directly."""
    valid_flags = [f for f in itertools.product(range(5), repeat=3) if f[0] != f[1] and f[1] != f[2]]
    assert len(valid_flags) == 80, f"Expected 80 flags, got {len(valid_flags)}"
    assert 5 * 4 * 4 == 80, "Formula 5*4*4 should equal 80"


# ─────────────────────────────────────────────────────────────────────────
# B8 — Subsets of a 6-element set. \ans{2^6=64}
# \method claims: includes the empty set and the whole set.
# ─────────────────────────────────────────────────────────────────────────
def check_B8():
    """EXHAUSTIVE PROOF: subsets counted by summing itertools.combinations
    over every size 0..6 — a route independent of evaluating 2**6."""
    s = list(range(6))
    subsets = []
    for r in range(7):
        subsets.extend(itertools.combinations(s, r))
    assert len(subsets) == 64, f"Expected 64 subsets, got {len(subsets)}"
    assert 2 ** 6 == 64, "Formula 2^6 should equal 64"
    assert () in subsets, "Empty set should be in subsets"
    assert tuple(range(6)) in subsets, "Whole set should be in subsets"


# ─────────────────────────────────────────────────────────────────────────
# B9 — Solve (n+1)! = 12(n-1)!. \ans{n=3}
# \method claims: consecutive integers with product 12 are 4 and 3.
# ─────────────────────────────────────────────────────────────────────────
def check_B9():
    """EXHAUSTIVE PROOF (generous finite range): search n=1..100 computing
    (n+1)! and 12*(n-1)! directly via math.factorial, confirming n=3 is the
    unique solution and that (n+1)!/(n-1!) = (n+1)*n for every n checked."""
    for n in range(1, 100):
        lhs = math.factorial(n + 1) // math.factorial(n - 1)
        rhs = (n + 1) * n
        assert lhs == rhs, f"Identity failed for n={n}: {lhs} != {rhs}"

    solutions = [n for n in range(1, 100) if math.factorial(n + 1) == 12 * math.factorial(n - 1)]
    assert len(solutions) == 1, f"Expected unique solution, found {solutions}"
    assert solutions[0] == 3, f"Expected solution n=3, got {solutions[0]}"
    assert 4 * 3 == 12, "Consecutive integers product check failed"


# ─────────────────────────────────────────────────────────────────────────
# B10 — Number plate: 2 different letters + 3 digits (repeats OK). \ans{650000}
# \method claims: letters 26*25, digits 10^3, independent blocks multiply.
# ─────────────────────────────────────────────────────────────────────────
def check_B10():
    """EXHAUSTIVE PROOF: letter-pairs and digit-triples each independently
    enumerated in full via itertools, then multiplied — the two block
    counts are derived from enumeration, not assumed from the formula."""
    letter_pairs = list(itertools.permutations(range(26), 2))
    assert len(letter_pairs) == 26 * 25, f"Expected letter pairs count to be 650, got {len(letter_pairs)}"

    digit_triples = list(itertools.product(range(10), repeat=3))
    assert len(digit_triples) == 1000, f"Expected digit triples count to be 1000, got {len(digit_triples)}"

    total_plates = len(letter_pairs) * len(digit_triples)
    assert total_plates == 650000, f"Expected 650000 plates, got {total_plates}"
    assert 26 * 25 * (10 ** 3) == 650000, "Formula 26*25*10^3 should equal 650000"


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────
# C1 — Even 3-digit numbers, all digits different. \ans{328}
# \method claims: units=0 case gives 72; units in {2,4,6,8} case gives 256.
# ─────────────────────────────────────────────────────────────────────────
def check_C1():
    """EXHAUSTIVE PROOF: every three-digit number 100..999 is scanned
    directly and filtered for evenness + digit distinctness — a route
    independent of the method's units-digit case split. The two stated
    sub-case counts (72, 256) are also verified by direct sub-filtering."""
    total = 0
    case_units_0 = 0
    case_units_even_nz = 0

    for n in range(100, 1000):
        h, t, u = n // 100, (n // 10) % 10, n % 10
        digits = (h, t, u)
        if n % 2 == 0 and len(set(digits)) == 3:
            total += 1
            if u == 0:
                case_units_0 += 1
            elif u in {2, 4, 6, 8}:
                case_units_even_nz += 1

    assert total == 328, f"Expected 328 even distinct-digit 3-digit numbers, got {total}"
    assert case_units_0 == 72, f"Expected 72 with units=0, got {case_units_0}"
    assert case_units_even_nz == 256, f"Expected 256 with units in {{2,4,6,8}}, got {case_units_even_nz}"
    assert case_units_0 + case_units_even_nz == total, "Sub-cases should partition the total"


# ─────────────────────────────────────────────────────────────────────────
# C2 — 6 people in a line, Priya & Quinn adjacent. \ans{2*5!=240}
# \method claims: glue into a block, 5! orders, 2 internal orders.
# ─────────────────────────────────────────────────────────────────────────
def check_C2():
    """EXHAUSTIVE PROOF: all 720 permutations of 6 labelled people are
    generated directly and filtered for Priya/Quinn adjacency — independent
    of the method's block-gluing argument."""
    people = list(range(6))  # 0=Priya, 1=Quinn
    all_perms = list(itertools.permutations(people))
    assert len(all_perms) == 720, f"Expected 720 permutations, got {len(all_perms)}"

    adjacent_count = sum(1 for p in all_perms if abs(p.index(0) - p.index(1)) == 1)
    assert adjacent_count == 240, f"Expected 240 arrangements with Priya & Quinn adjacent, got {adjacent_count}"
    assert 2 * math.factorial(5) == 240, "2*5! should equal 240"


# ─────────────────────────────────────────────────────────────────────────
# C3 — Same 6 people, Priya & Quinn NOT adjacent. \ans{720-240=480}
# \method claims: complementary counting (total minus together).
# ─────────────────────────────────────────────────────────────────────────
def check_C3():
    """EXHAUSTIVE PROOF: the same full enumeration as C2, but the
    NOT-adjacent count is accumulated directly during the single pass
    (never by subtracting from 720) — the complementary-counting identity
    the method invokes is then cross-checked as a separate assertion."""
    people = list(range(6))
    all_perms = list(itertools.permutations(people))
    total_perms = len(all_perms)
    assert total_perms == 720 == math.factorial(6)

    not_adjacent_count = 0
    adjacent_count = 0
    for p in all_perms:
        if abs(p.index(0) - p.index(1)) == 1:
            adjacent_count += 1
        else:
            not_adjacent_count += 1

    assert not_adjacent_count == 480, f"Expected 480 arrangements NOT adjacent, got {not_adjacent_count}"
    assert total_perms - adjacent_count == not_adjacent_count, "Complementary identity failed"
    assert adjacent_count == 240, "Adjacent count should match C2's 240"


# ─────────────────────────────────────────────────────────────────────────
# C4 — Five-digit palindromes. \ans{900}
# \method claims: determined by first three digits, 9*10*10.
# ─────────────────────────────────────────────────────────────────────────
def check_C4():
    """EXHAUSTIVE PROOF: every five-digit integer 10000..99999 is scanned
    and tested for the palindrome property directly via string reversal —
    no reliance on the "determined by first 3 digits" argument."""
    palindrome_count = sum(1 for n in range(10000, 100000) if str(n) == str(n)[::-1])
    assert palindrome_count == 900, f"Expected 900 five-digit palindromes, got {palindrome_count}"
    assert 9 * 10 * 10 == 900, "9*10*10 should equal 900"


# ─────────────────────────────────────────────────────────────────────────
# C5 — 3 married couples, row of 6, each couple together. \ans{3!*2^3=48}
# \method claims: glue each couple, 3! block orders, 2^3 internal flips.
# ─────────────────────────────────────────────────────────────────────────
def check_C5():
    """EXHAUSTIVE PROOF: all 720 permutations of 6 labelled individuals
    (3 couples) are generated and filtered for "each couple adjacent" —
    independent of the block-gluing argument."""
    couple_A, couple_B, couple_C = {0, 1}, {2, 3}, {4, 5}
    all_perms = list(itertools.permutations(range(6)))
    assert len(all_perms) == 720

    def couple_adjacent(perm, couple):
        members = [i for i, p in enumerate(perm) if p in couple]
        return abs(members[0] - members[1]) == 1

    valid_count = sum(
        1 for perm in all_perms
        if couple_adjacent(perm, couple_A) and couple_adjacent(perm, couple_B) and couple_adjacent(perm, couple_C)
    )
    assert valid_count == 48, f"Expected 48 seating arrangements, got {valid_count}"
    assert math.factorial(3) * (2 ** 3) == 48, "3!*2^3 should equal 48"


# ─────────────────────────────────────────────────────────────────────────
# C6 — Positive factors of 360 = 2^3*3^2*5. \ans{24}
# \method claims: (3+1)(2+1)(1+1) = 24.
# ─────────────────────────────────────────────────────────────────────────
def check_C6():
    """EXHAUSTIVE PROOF: every integer 1..360 is trial-divided directly to
    count actual divisors — independent of the prime-exponent product
    formula. The claimed factorisation 360=2^3*3^2*5 is verified separately."""
    assert 2 ** 3 * 3 ** 2 * 5 == 360, "Claimed factorisation does not equal 360"
    divisor_count = sum(1 for d in range(1, 361) if 360 % d == 0)
    assert divisor_count == 24, f"Expected 24 positive divisors of 360, got {divisor_count}"
    assert (3 + 1) * (2 + 1) * (1 + 1) == 24, "(3+1)(2+1)(1+1) should equal 24"


# ─────────────────────────────────────────────────────────────────────────
# C7 — Four-digit odd numbers, all digits different. \ans{5*8*8*7=2240}
# \method claims: units odd (5), thousands (8), then 8 and 7.
# ─────────────────────────────────────────────────────────────────────────
def check_C7():
    """EXHAUSTIVE PROOF: every four-digit integer 1000..9999 is scanned
    directly and filtered by oddness + digit distinctness."""
    total = 0
    for n in range(1000, 10000):
        digits = [n // 1000, (n // 100) % 10, (n // 10) % 10, n % 10]
        if n % 2 == 1 and len(set(digits)) == 4:
            total += 1
    assert total == 2240, f"Expected 2240 four-digit odd distinct-digit numbers, got {total}"
    assert 5 * 8 * 8 * 7 == 2240, "5*8*8*7 should equal 2240"


# ─────────────────────────────────────────────────────────────────────────
# C8 — Solve n! = 20(n-2)!. \ans{n=5}
# \method claims: n(n-1)=20, consecutive integers 5*4.
# ─────────────────────────────────────────────────────────────────────────
def check_C8():
    """EXHAUSTIVE PROOF (generous finite range): search n=2..40 computing
    n! and 20*(n-2)! directly via math.factorial, confirming n=5 is the
    unique solution."""
    for n in range(2, 41):
        ratio = math.factorial(n) // math.factorial(n - 2)
        assert ratio == n * (n - 1), f"n!/(n-2)! should equal n*(n-1) for n={n}"

    solutions = [n for n in range(2, 41) if math.factorial(n) == 20 * math.factorial(n - 2)]
    assert len(solutions) == 1, f"Expected exactly one solution, found {solutions}"
    assert solutions[0] == 5, f"Expected unique solution n=5, got n={solutions[0]}"
    assert 5 * 4 == 20, "5*4 should equal 20"


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────
# D1 — Three different even digits, three-digit number, div by 3. \ans{20}
# \method claims: valid digit-sets {0,2,4},{0,4,8},{2,4,6},{4,6,8}; the two
# containing 0 give 4 arrangements each, the other two give 6 each.
# ─────────────────────────────────────────────────────────────────────────
def check_D1():
    """EXHAUSTIVE PROOF over all 900 three-digit numbers (100-999): loops
    every n, checks all-even + all-distinct digits + divisible by 3, with
    no use of the digit-set/case-split argument at all. Separately,
    re-derives the method's structural claims: the valid 3-subsets of
    {0,2,4,6,8} summing to 0 mod 3 (via itertools.combinations) and the
    per-set arrangement counts (via itertools.permutations)."""
    even_digits = {0, 2, 4, 6, 8}

    brute_count = 0
    for n in range(100, 1000):
        digits = [n // 100, (n // 10) % 10, n % 10]
        if all(d in even_digits for d in digits) and len(set(digits)) == 3 and n % 3 == 0:
            brute_count += 1
    assert brute_count == 20, f"Route 1 brute force gave {brute_count}, expected 20"

    valid_sets = [frozenset(c) for c in itertools.combinations(sorted(even_digits), 3) if sum(c) % 3 == 0]
    expected_sets = {frozenset({0, 2, 4}), frozenset({0, 4, 8}), frozenset({2, 4, 6}), frozenset({4, 6, 8})}
    assert set(valid_sets) == expected_sets, f"Valid digit-sets found: {set(valid_sets)}, expected {expected_sets}"

    sets_with_zero = [s for s in valid_sets if 0 in s]
    sets_without_zero = [s for s in valid_sets if 0 not in s]
    assert len(sets_with_zero) == 2 and len(sets_without_zero) == 2

    structural_total = 0
    for dset in sets_with_zero:
        count = sum(1 for perm in itertools.permutations(sorted(dset)) if perm[0] != 0)
        assert count == 4, f"Digit-set {dset} (contains 0): expected 4 valid arrangements, got {count}"
        structural_total += count
    for dset in sets_without_zero:
        count = sum(1 for _ in itertools.permutations(sorted(dset)))
        assert count == 6, f"Digit-set {dset} (no zero): expected 6 valid arrangements, got {count}"
        structural_total += count

    assert structural_total == 20 == brute_count


# ─────────────────────────────────────────────────────────────────────────
# D2 — Rectangles in a 3x3 grid of unit squares. \ans{36}
# \method claims: choose 2 of 4 vertical + 2 of 4 horizontal lines, C(4,2)=6.
# ─────────────────────────────────────────────────────────────────────────
def check_D2():
    """EXHAUSTIVE PROOF: every axis-aligned rectangle is explicitly
    constructed as a (x1,y1,x2,y2) tuple via nested loops over the grid
    coordinates {0,1,2,3} and collected — no C(4,2) formula assumed. The
    method's C(4,2)=6 claim is instead DERIVED from the enumeration
    (counting the distinct x-interval and y-interval pairs actually used)."""
    grid_coords = [0, 1, 2, 3]
    rectangles = []
    for x1 in grid_coords:
        for x2 in grid_coords:
            if x1 >= x2:
                continue
            for y1 in grid_coords:
                for y2 in grid_coords:
                    if y1 >= y2:
                        continue
                    rectangles.append((x1, y1, x2, y2))

    assert len(rectangles) == len(set(rectangles)), "Duplicate rectangles found -- logic error"
    assert len(rectangles) == 36, f"Enumerated {len(rectangles)} rectangles, expected 36"

    x_pairs = set((r[0], r[2]) for r in rectangles)
    y_pairs = set((r[1], r[3]) for r in rectangles)
    assert len(x_pairs) == 6, f"Derived x-pair count is {len(x_pairs)}, expected 6 (C(4,2))"
    assert len(y_pairs) == 6, f"Derived y-pair count is {len(y_pairs)}, expected 6 (C(4,2))"
    assert len(x_pairs) * len(y_pairs) == len(rectangles)

    expected_pairs = set(itertools.combinations([0, 1, 2, 3], 2))
    assert x_pairs == expected_pairs and y_pairs == expected_pairs


# ─────────────────────────────────────────────────────────────────────────
# D3 — Split 8 people into 4 unlabelled pairs. \ans{105}
# \method claims: 7*5*3*1 = 105, anchoring on first unpaired person.
# ─────────────────────────────────────────────────────────────────────────
def check_D3():
    """EXHAUSTIVE PROOF: a recursive generator builds every complete perfect
    matching of {0..7} explicitly as a frozenset of frozensets (always
    anchoring the smallest remaining element and trying every partner), and
    the answer is the literal COUNT of matchings actually built and
    validated — never the arithmetic product 7*5*3*1 itself."""
    def generate_matchings(people):
        if not people:
            yield frozenset()
            return
        people_sorted = sorted(people)
        first = people_sorted[0]
        rest = people_sorted[1:]
        for i, partner in enumerate(rest):
            pair = frozenset({first, partner})
            remaining = frozenset(rest[:i] + rest[i + 1:])
            for sub_matching in generate_matchings(remaining):
                yield frozenset({pair}) | sub_matching

    all_matchings = list(generate_matchings(frozenset(range(8))))
    assert len(all_matchings) == len(set(all_matchings)), "Duplicate matchings generated -- logic error"

    for m in all_matchings:
        assert len(m) == 4, f"Matching {m} does not have exactly 4 pairs"
        covered = set()
        for pair in m:
            assert len(pair) == 2
            for p in pair:
                assert p not in covered, f"Person {p} appears twice in {m}"
                covered.add(p)
        assert covered == set(range(8))

    assert len(all_matchings) == 105, f"Enumerated {len(all_matchings)} perfect matchings, expected 105"


# ─────────────────────────────────────────────────────────────────────────
# D4 — Trailing zeros of 100!. \ans{24}
# \method claims: floor(100/5)+floor(100/25)=20+4=24; 2s outnumber 5s.
# ─────────────────────────────────────────────────────────────────────────
def check_D4():
    """EXHAUSTIVE PROOF: 100! is computed exactly as a Python big integer
    and its trailing zero digits are counted directly from the decimal
    string — exact, not an estimate. The Legendre-formula claims (both the
    method's partial sum and the full "2s outnumber 5s" statement) are
    verified separately via an independently implemented Legendre function."""
    factorial_100 = math.factorial(100)
    s = str(factorial_100)
    trailing_zeros = len(s) - len(s.rstrip('0'))
    assert trailing_zeros == 24, f"100! has {trailing_zeros} trailing zeros, expected 24"

    assert 100 // 5 == 20 and 100 // 25 == 4
    assert (100 // 5) + (100 // 25) == 24, "floor(100/5)+floor(100/25) should be 24"
    assert 100 // 125 == 0

    def legendre_power(n, p):
        total, pk = 0, p
        while pk <= n:
            total += n // pk
            pk *= p
        return total

    power_of_5 = legendre_power(100, 5)
    power_of_2 = legendre_power(100, 2)
    assert power_of_5 == 24
    assert power_of_2 == 97
    assert min(power_of_2, power_of_5) == trailing_zeros
    assert power_of_2 > power_of_5, "Method's claim '2s vastly outnumber 5s' failed"


# ─────────────────────────────────────────────────────────────────────────
# D5 — 30 squares, shading rules, max-min shaded. \ans{15-9=6}
# \method claims: distances in [2,4] summing to 29; max 15 via
# 1,3,...,27,30; min 9 via 1,5,9,...,25,27,30.
# ─────────────────────────────────────────────────────────────────────────
def check_D5():
    """EXHAUSTIVE PROOF: a fully memoized reachability DP operates directly
    on square positions 1..30 (never on the method's abstract "distance"
    reformulation) — every next shaded position q from p must satisfy
    2 <= q-p <= 4 and q <= 30. This enumerates the FULL finite reachability
    set exactly, so max/min are exact, not sampled. The method's two
    example sequences are also explicitly constructed and validated
    against a from-scratch legality predicate."""
    @functools.lru_cache(maxsize=None)
    def reachable_counts(p):
        if p == 30:
            return frozenset({0})
        results = set()
        for step in range(2, 5):
            q = p + step
            if q > 30:
                break
            if q == 30:
                results.add(1)
            else:
                for c in reachable_counts(q):
                    results.add(c + 1)
        return frozenset(results)

    additional_counts = reachable_counts(1)
    assert len(additional_counts) > 0, "No legal shadings found from position 1"
    total_counts = frozenset(1 + c for c in additional_counts)

    max_shaded, min_shaded = max(total_counts), min(total_counts)
    assert max_shaded == 15, f"Maximum shaded squares = {max_shaded}, expected 15"
    assert min_shaded == 9, f"Minimum shaded squares = {min_shaded}, expected 9"
    assert max_shaded - min_shaded == 6

    def is_valid_shading(seq):
        if not seq or seq[0] != 1 or seq[-1] != 30:
            return False
        return all(2 <= seq[i + 1] - seq[i] <= 4 for i in range(len(seq) - 1))

    max_example = list(range(1, 28, 2)) + [30]  # 1,3,5,...,27,30
    assert is_valid_shading(max_example), f"Method's maximum example is invalid: {max_example}"
    assert len(max_example) == 15
    assert max_example[-1] - max_example[-2] == 3, "Method's noted final step of 3 doesn't hold"

    min_example = [1, 5, 9, 13, 17, 21, 25, 27, 30]
    assert is_valid_shading(min_example), f"Method's minimum example is invalid: {min_example}"
    assert len(min_example) == 9

    assert 15 in total_counts and 9 in total_counts


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
        # python -O (or PYTHONOPTIMIZE=1) strips every `assert` statement
        # at compile time — every check below would silently report PASS
        # while verifying nothing. This is an `if`, not an `assert`, on
        # purpose: it is the one check that survives -O.
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
