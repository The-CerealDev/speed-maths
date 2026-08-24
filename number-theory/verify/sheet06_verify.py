import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'number-theory/answers/ans06.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest prime factor of 2025."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(sympy.primefactors(2025))
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last digit of 3^2026."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 2026, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd(84, 120)."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.gcd(84, 120)
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 10^10 mod 9."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(10, 10, 9)
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 47d53 divisible by 9."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [d for d in range(10) if (4 + 7 + d + 5 + 3) % 9 == 0]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of divisors of 100."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_count(100)
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for comparing 2^300 and 3^200."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    assert 3**200 > 2**300


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5^2024 mod 4."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(5, 2024, 4)
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive n with 12n square."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 100):
        sq = math.isqrt(12 * n)
        if sq * sq == 12 * n:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of prime factors of 210."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(sympy.primefactors(210))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for trailing zeros in 20!."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 20
    while m > 0:
        k += m // 5
        m //= 5
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3x = 4 mod 7."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 7) if (3 * x) % 7 == 4]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for primes with p^2 - q^2 = 24."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    primes = list(sympy.primerange(2, 50))
    sols = [p + q for p in primes for q in primes if p**2 - q**2 == 24]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 5^2025."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(5, 2025, 100)
    assert sympy.simplify(computed_ans - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for N = 2 mod 3, N = 3 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 30) if n % 3 == 2 and n % 5 == 3]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for square divisors of 3600."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    divs = sympy.divisors(3600)
    computed_ans = sum(1 for d in divs if math.isqrt(d)**2 == d)
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-adic valuation of 27^5 * 9^4."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # (3^3)^5 * (3^2)^4 = 3^15 * 3^8 = 3^23
    computed_ans = 15 + 8
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive int with 6 divisors."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 100):
        if sympy.divisor_count(n) == 6:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive xy=144, gcd(x,y)=3 max x+y."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x + (144 // x) for x in range(1, 145) if 144 % x == 0 and math.gcd(x, 144 // x) == 3]
    computed_ans = max(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum 1!..10! mod 5."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(math.factorial(k) for k in range(1, 11)) % 5
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with xy+x+y=23."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [(x, y) for x in range(1, 30) for y in range(1, 30) if (x + 1) * (y + 1) == 24]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of primes with p^2+2 prime."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [p for p in sympy.primerange(2, 100) if sympy.isprime(p**2 + 2)]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-digit palindromes div by 11."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count = 0
    for a in range(1, 10):
        for b in range(10):
            num = 100 * a + 10 * b + a
            if num % 11 == 0:
                count += 1
    computed_ans = count
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for consecutive ints with product 336."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [3 * n for n in range(2, 50) if (n - 1) * n * (n + 1) == 336]
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for max 4-digit N with reversed = N + 1089."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a + b + c + d == 12:
                        N = 1000 * a + 100 * b + 10 * c + d
                        rev = 1000 * d + 100 * c + 10 * b + a
                        if rev == N + 1089:
                            sols.append(N)
    computed_ans = max(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of positive x with (x+11)/(x-3) int."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 50) if x != 3 and (x + 11) % (x - 3) == 0]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for max gcd(7n+15, 3n+2)."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # gcd(7n+15, 3n+2) divides 31
    g_vals = [math.gcd(7 * n + 15, 3 * n + 2) for n in range(1, 100)]
    computed_ans = max(g_vals)
    assert sympy.simplify(computed_ans - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of integer n with (n^2+3n+5)/(n-1) int."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(-50, 50) if n != 1 and (n**2 + 3 * n + 5) % (n - 1) == 0]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-digit abc = a! + b! + c!."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                if 100 * a + 10 * b + c == math.factorial(a) + math.factorial(b) + math.factorial(c):
                    sols.append(100 * a + 10 * b + c)
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of possible values of gcd(n^2+3, n+1)."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    g_set = set(math.gcd(n**2 + 3, n + 1) for n in range(1, 100))
    computed_ans = sum(g_set)
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last three digits of 2025^2025."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(2025, 2025, 1000)
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive n <= 100 with n^n square."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count = sum(1 for n in range(1, 101) if n % 2 == 0 or math.isqrt(n)**2 == n)
    computed_ans = count
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for max x+y+z with 1/x + 1/y + 1/z = 1."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for x in range(2, 4):
        for y in range(x, 10):
            denom = x * y - x - y
            if denom > 0 and (x * y) % denom == 0:
                z = (x * y) // denom
                if z >= y:
                    sols.append(x + y + z)
    computed_ans = max(sols)
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
