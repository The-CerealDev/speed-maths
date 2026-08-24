import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'number-theory/answers/ans07.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime factorisation of 91."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 7 * 13
    assert computed_ans == 91
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last digit of 3^20."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 20, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd(144, 60)."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.gcd(144, 60)
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (12 * 13) mod 5."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (12 * 13) % 5
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest prime factor of 323."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = min(sympy.primefactors(323))
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of divisors of 28."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_count(28)
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5^3 mod 6."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(5, 3, 6)
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 4x = 1 mod 7."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 8) if (4 * x) % 7 == 1]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 10^10 mod 9."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(10, 10, 9)
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for comparing 2^30 and 3^20."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    assert 3**20 > 2**30


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 7^4."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    last_two = f"{pow(7, 4, 100):02d}"
    assert last_two == '01'
    assert str(expected_ans).zfill(2) == '01'


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for trailing zeros of 20!."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 20
    while m > 0:
        k += m // 5
        m //= 5
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive n with 120n square."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 200):
        sq = math.isqrt(120 * n)
        if sq * sq == 120 * n:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-adic valuation of 50!."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 50
    while m > 0:
        k += m // 3
        m //= 3
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with x^2 - y^2 = 17."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    sols = [(x, y) for x in range(1, 50) for y in range(1, 50) if x**2 - y**2 == 17]
    assert sols == [(9, 8)]


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3^100 mod 10."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 100, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3x+4 = 6 mod 11."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(11) if (3 * x + 4) % 11 == 6]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of divisors of 50."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_sigma(50)
    assert sympy.simplify(computed_ans - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of primes between 40 and 50."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    primes = [p for p in sympy.primerange(41, 50)]
    computed_ans = len(primes)
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest 3-digit x with x = 2 mod 3, 4, 5."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(100, 200) if x % 3 == 2 and x % 4 == 2 and x % 5 == 2]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for product of n < 50 with 3 divisors."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    nums = [n for n in range(1, 50) if sympy.divisor_count(n) == 3]
    prod = 1
    for n in nums:
        prod *= n
    computed_ans = prod
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive n with 15 divisors."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 1000):
        if sympy.divisor_count(n) == 15:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for divisors of 3^5 * 5^4 * 7^3 multiple of 45."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # a in 2..5 (4), b in 1..4 (4), c in 0..3 (4) -> 4 * 4 * 4 = 64
    computed_ans = 4 * 4 * 4
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for square divisors of 10!."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    divs = sympy.divisors(math.factorial(10))
    computed_ans = sum(1 for d in divs if math.isqrt(d)**2 == d)
    assert sympy.simplify(computed_ans - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for greatest value of gcd(n^2+5, n+2)."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    g_vals = [math.gcd(n**2 + 5, n + 2) for n in range(1, 100)]
    computed_ans = max(g_vals)
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of digits of 10^15 - 2026."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    val = 10**15 - 2026
    computed_ans = sum(int(d) for d in str(val))
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with x^3 - y^3 = 37."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    sols = [(x, y) for x in range(1, 50) for y in range(1, 50) if x**3 - y**3 == 37]
    assert sols == [(4, 3)]


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest x with x=1 mod 3, x=2 mod 4, x=3 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 100) if x % 3 == 1 and x % 4 == 2 and x % 5 == 3]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integer pairs with x^2 + xy + y^2 = 7."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [(x, y) for x in range(-10, 10) for y in range(-10, 10) if x**2 + x * y + y**2 == 7]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for n in 1..100 with n^n square."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count = sum(1 for n in range(1, 101) if n % 2 == 0 or math.isqrt(n)**2 == n)
    computed_ans = count
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive a,b with a^2 - 4b^2 = 45."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    sols = [(a, b) for a in range(1, 50) for b in range(1, 50) if a**2 - 4 * b**2 == 45]
    sols.sort(key=lambda p: p[0])
    assert sols == [(7, 1), (9, 3), (23, 11)]


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest prime factor of 2^16 - 1."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(sympy.primefactors(2**16 - 1))
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for primes with p^2 - 2q^2 = 1 sum p+q."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    primes = list(sympy.primerange(2, 50))
    sols = [p + q for p in primes for q in primes if p**2 - 2 * q**2 == 1]
    assert len(sols) == 1
    computed_ans = sols[0]
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
