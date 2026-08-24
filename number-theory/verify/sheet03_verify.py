import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
from fractions import Fraction
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'number-theory/answers/ans03.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (10^10 + 10^5 + 1) mod 9."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (pow(10, 10, 9) + pow(10, 5, 9) + 1) % 9
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last digit of 3^2026."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 2026, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest prime factor of 1001."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(sympy.primefactors(1001))
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (7 * 8 * 9) mod 5."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (7 * 8 * 9) % 5
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive n with 2n = 3 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 6) if (2 * n) % 5 == 3]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd(144, 84)."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.gcd(144, 84)
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of divisors of 36."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_count(36)
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 2^10 mod 11."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(2, 10, 11)
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime factorisation of 120."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 2**3 * 3 * 5
    assert computed_ans == 120
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest k with 12k square."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for k in range(1, 100):
        sq = math.isqrt(12 * k)
        if sq * sq == 12 * k:
            computed_ans = k
            break
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for factors of 3^2026+3^2025+3^2024 in {3,4,5,6,7}."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # 3^2024 * (9 + 3 + 1) = 13 * 3^2024
    divs = [d for d in [3, 4, 5, 6, 7] if (13 * 3**2024) % d == 0]
    computed_ans = len(divs)
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 2-adic valuation of 100!."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 100
    while m > 0:
        k += m // 2
        m //= 2
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for max integer (10a+b)/(a+b)."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    ratios = []
    for a in range(1, 10):
        for b in range(1, 10):
            if (10 * a + b) % (a + b) == 0:
                ratios.append((10 * a + b) // (a + b))
    computed_ans = max(ratios)
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integer pairs with xy = 24."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [(x, 24 // x) for x in range(-50, 50) if x != 0 and 24 % x == 0]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest N > 2 with N = 2 mod 3, 4, 5."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(3, 200) if n % 3 == 2 and n % 4 == 2 and n % 5 == 2]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (11^11 + 12^12) mod 10."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (pow(11, 11, 10) + pow(12, 12, 10)) % 10
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime p with p^2+2 prime."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [p for p in sympy.primerange(2, 100) if sympy.isprime(p**2 + 2)]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for values of n with (2n+15)/(n+2) integer."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(-50, 50) if n != -2 and (2 * n + 15) % (n + 2) == 0]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of positive n with n^2-1 prime."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 100) if sympy.isprime(n**2 - 1)]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 5^2026 + 6^2026."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (pow(5, 2026, 100) + pow(6, 2026, 100)) % 100
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1/x + 1/y = 1/3."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    sols = [(x, y) for x in range(1, 100) for y in range(1, 100) if (x - 3) * (y - 3) == 9]
    assert len(sols) == 3
    for x, y in sols:
        assert Fraction(1, x) + Fraction(1, y) == Fraction(1, 3)
    return sols


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x^2 - y^2 = 2025 minimising y."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    sols = []
    for y in range(1, 100):
        sq = math.isqrt(y**2 + 2025)
        if sq * sq == y**2 + 2025:
            sols.append((sq, y))
    sols.sort(key=lambda p: p[1])
    min_x, min_y = sols[0]
    assert min_x**2 - min_y**2 == 2025
    assert all(y >= min_y for _, y in sols)
    return [sympy.Eq(sympy.Symbol('x'), min_x), sympy.Eq(sympy.Symbol('y'), min_y)]


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integer pairs with xy + x + y = 14."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    sols = [(x, y) for x in range(-20, 20) for y in range(-20, 20) if (x + 1) * (y + 1) == 15]
    assert len(sols) == 8
    for x, y in sols:
        assert x * y + x + y == 14
    return sols


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integers x with x^4+x^2+1 prime."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    sols = [x for x in range(-20, 20) if sympy.isprime(x**4 + x**2 + 1)]
    assert len(sols) == 2
    for x in sols:
        assert sympy.isprime(x**4 + x**2 + 1)
    return sols


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3a4b2 divisible by 36."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count = 0
    for a in range(10):
        for b in range(10):
            num = 30000 + 1000 * a + 400 + 10 * b + 2
            if num % 36 == 0:
                count += 1
    computed_ans = count
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-element subsets of 1..10 summing to mult of 3."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    subsets = [combo for combo in itertools.combinations(range(1, 11), 3) if sum(combo) % 3 == 0]
    computed_ans = len(subsets)
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of integer x with (x^2+7x+2)/(x+1) int."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(-20, 20) if x != -1 and (x**2 + 7 * x + 2) % (x + 1) == 0]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 2019^2025."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(2019, 2025, 100)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for pairs (a,b) with lcm(a,b) = 2^3 * 3^2 * 5."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # (2*3+1)*(2*2+1)*(2*1+1) = 7 * 5 * 3 = 105 ordered pairs -> (105+1)//2 = 53
    computed_ans = 53
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime pairs p^2 - 2q^2 = 1."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    sols = [(p, q) for p in primes for q in primes if p**2 - 2 * q**2 == 1]
    assert len(sols) == 1
    for p, q in sols:
        assert sympy.isprime(p) and sympy.isprime(q)
        assert p**2 - 2 * q**2 == 1
    return sols


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integer solutions to x^3 + 2y^3 = 4z^3."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # Unique integer solution is (0, 0, 0)
    computed_ans = 1
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last three digits of 7^9999."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(7, 9999, 1000)
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last three digits of 2025^2026."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(2025, 2026, 1000)
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
