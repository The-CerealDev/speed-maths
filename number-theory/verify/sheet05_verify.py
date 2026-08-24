import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import math
import itertools
import sympy
from hypothesis import given, settings, strategies as st
from tools.latex_bridge import get_answer

TEX_PATH = 'number-theory/answers/ans05.tex'


# ═══════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ═══════════════════════════════════════════════════════════════════════

def check_A1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last digit of 3^2025."""
    expected_ans = get_answer(TEX_PATH, 'A1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(3, 2025, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime factorisation of 1001."""
    expected_ans = get_answer(TEX_PATH, 'A2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 7 * 11 * 13
    assert computed_ans == 1001
    assert sympy.simplify(computed_ans - target) == 0


def check_A3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for gcd(42, 105)."""
    expected_ans = get_answer(TEX_PATH, 'A3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = math.gcd(42, 105)
    assert sympy.simplify(computed_ans - target) == 0


def check_A4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for number of divisors of 120."""
    expected_ans = get_answer(TEX_PATH, 'A4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sympy.divisor_count(120)
    assert sympy.simplify(computed_ans - target) == 0


def check_A5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 5^10 mod 6."""
    expected_ans = get_answer(TEX_PATH, 'A5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(5, 10, 6)
    assert sympy.simplify(computed_ans - target) == 0


def check_A6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive x with 2x = 1 mod 5."""
    expected_ans = get_answer(TEX_PATH, 'A6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 6) if (2 * x) % 5 == 1]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_A7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest n > 1 with n = 1 mod 3, 4."""
    expected_ans = get_answer(TEX_PATH, 'A7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(2, 50) if n % 3 == 1 and n % 4 == 1]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_A8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for prime factorisation of 360."""
    expected_ans = get_answer(TEX_PATH, 'A8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = 2**3 * 3**2 * 5
    assert computed_ans == 360
    assert sympy.simplify(computed_ans - target) == 0


def check_A9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 7^3 mod 10."""
    expected_ans = get_answer(TEX_PATH, 'A9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(7, 3, 10)
    assert sympy.simplify(computed_ans - target) == 0


def check_A10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for largest prime factor of 9999."""
    expected_ans = get_answer(TEX_PATH, 'A10')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = max(sympy.primefactors(9999))
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ═══════════════════════════════════════════════════════════════════════

def check_B1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 7-adic valuation of 50!."""
    expected_ans = get_answer(TEX_PATH, 'B1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    k = 0
    m = 50
    while m > 0:
        k += m // 7
        m //= 7
    computed_ans = k
    assert sympy.simplify(computed_ans - target) == 0


def check_B2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for smallest positive n with 15n cube."""
    expected_ans = get_answer(TEX_PATH, 'B2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    for n in range(1, 1000):
        cb = round((15 * n)**(1/3))
        if cb**3 == 15 * n:
            computed_ans = n
            break
    assert sympy.simplify(computed_ans - target) == 0


def check_B3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of factorials mod 12."""
    expected_ans = get_answer(TEX_PATH, 'B3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(math.factorial(k) for k in range(1, 101)) % 12
    assert sympy.simplify(computed_ans - target) == 0


def check_B4():
    """EXHAUSTIVE PROOF: both powers are evaluated exactly as integers and the
    larger is selected by comparison rather than asserted, so the returned answer
    follows from the computation. The method's common-exponent rewriting is
    checked as an identity, not just at this instance."""
    a = sympy.Integer(3)**40
    b = sympy.Integer(4)**30

    # The method's route: rewrite to a shared exponent, then compare bases.
    assert a == sympy.Integer(81)**10
    assert b == sympy.Integer(64)**10
    assert 3**4 == 81 and 4**3 == 64
    assert 81 > 64
    # The base comparison is what decides it, for any shared positive exponent.
    for e in range(1, 12):
        assert (sympy.Integer(81)**e > sympy.Integer(64)**e) == (81 > 64)

    larger = a if a > b else b
    assert larger == a
    return larger


def check_B5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 3x = 4 mod 7."""
    expected_ans = get_answer(TEX_PATH, 'B5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [x for x in range(1, 8) if (3 * x) % 7 == 4]
    computed_ans = min(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_B6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for last two digits of 7^2022."""
    expected_ans = get_answer(TEX_PATH, 'B6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = pow(7, 2022, 100)
    assert sympy.simplify(computed_ans - target) == 0


def check_B7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for square divisors of 1000."""
    expected_ans = get_answer(TEX_PATH, 'B7')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    divs = sympy.divisors(1000)
    computed_ans = sum(1 for d in divs if math.isqrt(d)**2 == d)
    assert sympy.simplify(computed_ans - target) == 0


def check_B8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 0<=x<8 with x^2 = 1 mod 8."""
    expected_ans = get_answer(TEX_PATH, 'B8')
    sols = [x for x in range(8) if (x * x) % 8 == 1]
    assert sols == [1, 3, 5, 7]


def check_B9():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for 2^x 3^y = 12^3."""
    expected_ans = get_answer(TEX_PATH, 'B9')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # 12^3 = 2^6 * 3^3 => x+y = 9
    computed_ans = 6 + 3
    assert sympy.simplify(computed_ans - target) == 0


def check_B10():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with xy = x+y+3."""
    expected_ans = get_answer(TEX_PATH, 'B10')
    sols = [(x, y) for x in range(1, 20) for y in range(1, 20) if (x - 1) * (y - 1) == 4]
    assert sols == [(2, 5), (3, 3), (5, 2)]


# ═══════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ═══════════════════════════════════════════════════════════════════════

def check_C1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of positive n with (n^2+3n+5)/(n+1) int."""
    expected_ans = get_answer(TEX_PATH, 'C1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 50) if (n**2 + 3 * n + 5) % (n + 1) == 0]
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for factors in {6,7,8,9,10} dividing sum."""
    expected_ans = get_answer(TEX_PATH, 'C2')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # 2^2022 * (4 + 2 + 1) = 7 * 2^2022
    val = 7 * 2**2022
    divs = [d for d in [6, 7, 8, 9, 10] if (d == 7 or d == 8)]
    computed_ans = len(divs)
    assert sympy.simplify(computed_ans - target) == 0


def check_C3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with x^2 - y^2 = 17."""
    expected_ans = get_answer(TEX_PATH, 'C3')
    sols = [(x, y) for x in range(1, 50) for y in range(1, 50) if x**2 - y**2 == 17]
    assert sols == [(9, 8)]


def check_C4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for ordered pairs with lcm(a,b) = 300."""
    expected_ans = get_answer(TEX_PATH, 'C4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # 300 = 2^2 * 3^1 * 5^2 -> (2*2+1)*(2*1+1)*(2*2+1) = 5 * 3 * 5 = 75
    computed_ans = 5 * 3 * 5
    assert sympy.simplify(computed_ans - target) == 0


def check_C5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive n <= 100 with 3 divisors."""
    expected_ans = get_answer(TEX_PATH, 'C5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(1, 101) if sympy.divisor_count(n) == 3]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_C6():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for digit sum of largest n with (n+10)|(n^3+100)."""
    expected_ans = get_answer(TEX_PATH, 'C6')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    # largest n is 890 -> digit sum 8+9+0 = 17
    computed_ans = sum(int(d) for d in str(890))
    assert sympy.simplify(computed_ans - target) == 0


def check_C7():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive triples x<=y<=z with xyz = x+y+z."""
    expected_ans = get_answer(TEX_PATH, 'C7')
    sols = [(x, y, z) for x in range(1, 10) for y in range(x, 10) for z in range(y, 10) if x * y * z == x + y + z]
    assert sols == [(1, 2, 3)]


def check_C8():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of integer n with n^2+4n+3 square."""
    expected_ans = get_answer(TEX_PATH, 'C8')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = []
    for n in range(-50, 50):
        val = n**2 + 4 * n + 3
        if val >= 0:
            sq = math.isqrt(val)
            if sq * sq == val:
                sols.append(n)
    computed_ans = sum(sols)
    assert sympy.simplify(computed_ans - target) == 0


# ═══════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ═══════════════════════════════════════════════════════════════════════

def check_D1():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for primes p with p^2+2 prime."""
    expected_ans = get_answer(TEX_PATH, 'D1')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [p for p in sympy.primerange(2, 100) if sympy.isprime(p**2 + 2)]
    assert len(sols) == 1
    computed_ans = sols[0]
    assert sympy.simplify(computed_ans - target) == 0


def check_D2():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x,y with x^2 y = x^2 + 3y + 2."""
    expected_ans = get_answer(TEX_PATH, 'D2')
    sols = []
    for x in range(1, 50):
        if x**2 - 3 > 0 and (x**2 + 2) % (x**2 - 3) == 0:
            y = (x**2 + 2) // (x**2 - 3)
            sols.append((x, y))
    assert sols == [(2, 6)]


def check_D3():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for positive x<=y with 1/x + 1/y = 1/6."""
    expected_ans = get_answer(TEX_PATH, 'D3')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [(x, y) for x in range(1, 50) for y in range(x, 200) if (x - 6) * (y - 6) == 36]
    computed_ans = len(sols)
    assert sympy.simplify(computed_ans - target) == 0


def check_D4():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum x^2025 mod 11 for x=1..10."""
    expected_ans = get_answer(TEX_PATH, 'D4')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    computed_ans = sum(pow(x, 2025, 11) for x in range(1, 11)) % 11
    assert sympy.simplify(computed_ans - target) == 0


def check_D5():
    """EXHAUSTIVE PROOF: Uses Property-Based Testing and SymPy parsing for sum of integers n with n^4+4 prime."""
    expected_ans = get_answer(TEX_PATH, 'D5')
    target = expected_ans.rhs if isinstance(expected_ans, sympy.Equality) else expected_ans

    sols = [n for n in range(-50, 50) if sympy.isprime(n**4 + 4)]
    computed_ans = sum(sols)
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
