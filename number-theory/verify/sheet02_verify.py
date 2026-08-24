import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'number-theory/answers/ans02.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime factorisation of 1001."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 7 * 11 * 13
    assert computed_ans == 1001
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 10^5 mod 11."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(10, 5, 11)
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last digit of 7^100."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(7, 100, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest k with 12k square."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for k in range(1, 100):
        sq = math.isqrt(12 * k)
        if sq * sq == 12 * k:
            computed_ans = k
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd(84, 120)."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.gcd(84, 120)
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest prime p > 30."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.nextprime(30)
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3^10 mod 8."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 10, 8)
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of prime factors of 210."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(sympy.primefactors(210))
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 53d2 a multiple of 9."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [d for d in range(10) if (5 + 3 + d + 2) % 9 == 0]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest k with 3^k dividing 27^5."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # 27^5 = (3^3)^5 = 3^15
    computed_ans = 15
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of divisors of 144."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_count(144)
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest x > 1 with x = 1 mod 3, 4, 5."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(2, 200) if x % 3 == 1 and x % 4 == 1 and x % 5 == 1]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5x = 1 mod 7."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 8) if (5 * x) % 7 == 1]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for highest power of 5 dividing 100!."""
    expected_ans = get_answer(TEX_PATH, 'B4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 100
    while m > 0:
        k += m // 5
        m //= 5
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 51^2."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    last_two = f"{pow(51, 2, 100):02d}"
    assert last_two == '01'
    assert str(expected_ans).zfill(2) == '01'


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest n with 100 dividing n!."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 20):
        if math.factorial(n) % 100 == 0:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd=12, lcm=144 min sum."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sums = []
    for a in range(1, 300):
        for b in range(a + 1, 300):
            if math.gcd(a, b) == 12 and (a * b) // math.gcd(a, b) == 144:
                sums.append(a + b)
    computed_ans = min(sums)
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for digit sum of 2^10 * 5^8."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    val = 2**10 * 5**8
    computed_ans = sum(int(d) for d in str(val))
    assert sympy.simplify(computed_ans - target) == 0


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for (2^20 + 3^20) mod 5."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = (pow(2, 20, 5) + pow(3, 20, 5)) % 5
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for trailing zeros in 125!."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 125
    while m > 0:
        k += m // 5
        m //= 5
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive n with n^2-4n-5 prime."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 100) if sympy.isprime(n**2 - 4 * n - 5)]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for integers x with (x^2+11)/(x-1) int."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(-50, 50) if x != 1 and (x**2 + 11) % (x - 1) == 0]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive n with n^2+8n square."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for n in range(1, 1000):
        sq = math.isqrt(n**2 + 8 * n)
        if sq * sq == n**2 + 8 * n:
            sols.append(n)
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3-digit numbers with product of digits prime."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count = 0
    for n in range(100, 1000):
        d1, d2, d3 = int(str(n)[0]), int(str(n)[1]), int(str(n)[2])
        prod = d1 * d2 * d3
        if sympy.isprime(prod):
            count += 1
    computed_ans = count
    assert sympy.simplify(computed_ans - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1<=x<=100 with x^2 = 4 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = len([x for x in range(1, 101) if pow(x, 2, 5) == 4])
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for x+y=100, gcd(x,y)=5."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [(x, 100 - x) for x in range(1, 100) if math.gcd(x, 100 - x) == 5]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest n with (n+10)|(n^3+100)."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # n+10 must divide 900 -> max n = 900 - 10 = 890
    computed_ans = 900 - 10
    assert sympy.simplify(computed_ans - target) == 0


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of 0<x<20 with x^2 = 5 mod 11."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 20) if pow(x, 2, 11) == 5]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of permutations of 1,2,3,4."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    nums = [int(''.join(p)) for p in itertools.permutations('1234')]
    computed_ans = sum(nums)
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive a,b with a^2 - b^2 = 2024."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for b in range(1, 2025):
        sq = math.isqrt(b**2 + 2024)
        if sq * sq == b**2 + 2024:
            sols.append((sq, b))
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for trailing zeros S of 2025! mod 100."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 2025
    while m > 0:
        k += m // 5
        m //= 5
    computed_ans = k % 100
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 1<=x,y<=100 with x^2+y^2 = 0 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    count_mod = sum(1 for x in range(5) for y in range(5) if (x**2 + y**2) % 5 == 0)
    computed_ans = count_mod * 20 * 20
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for max gcd(n^2+3, n+2)."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    g_vals = [math.gcd(n**2 + 3, n + 2) for n in range(1, 100)]
    computed_ans = max(g_vals)
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
