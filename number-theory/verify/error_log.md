# Quantitative Error Log — Number Theory Verification Pipeline

This document logs parsing nuances, Property-Based Testing (Hypothesis) considerations, and mathematical verification details encountered during the robustification of verification scripts for Sheets 01 through 07 in the **Number Theory** pillar.

---

## 1. Summary of Verification Issues & Resolutions

| Sheet / Question | Error Category | Root Cause | Resolution | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Sheets 01–07 / main()** | Optimization Guard | `main()` raised generic `Exception("Do not run with -O!...")` which exited with code 1 instead of raising `SystemExit(2)`. | Replaced with standard `if not __debug__: raise SystemExit(2)` optimization guard. | **Resolved** |
| **Sheets 01–07 / Global** | Hardcoded Assertions | Scripts used hardcoded numbers (`assert 3**4 * 5**2 == 2025`, `assert d == 4`, etc.) rather than reading directly from LaTeX `.tex` files. | Fully integrated dynamic LaTeX parsing using `tools.latex_bridge.get_answer(TEX_PATH, label)` and SymPy equality simplification. | **Resolved** |
| **Sheets 01–07 / B5 (Last Two Digits)** | String Padding | Single digit / two digit remainders like `'01'` evaluated to integer `1` when parsed via standard arithmetic parsers, losing leading zero. | Handled via padded string comparison `str(expected_ans).zfill(2) == '01'` and raw string retention in `latex_bridge`. | **Resolved** |
| **Sheet 01 / C7, D5 & Sheet 03 / C1, C3** | Multi-tuple Representation | Multiple solution tuples (e.g. `(4,12), (6,6), (12,4)`) returned comma-separated string format. | Parsed into structured list of integer coordinate tuples and asserted equivalence. | **Resolved** |

---

## 2. Detailed Mathematical Verification Notes

### Sheet 01
- **A1–A10 (Rapid Recognition):** Prime factorisation of $2025 = 3^4 \times 5^2$, modular powers ($10^6 \equiv 1 \pmod 7$, $3^{2024} \equiv 1 \pmod{10}$), divisibility digit searches ($73d4$ mod 9), GCD/LCM product relations ($\gcd \times \text{lcm} = ab$), Legendre's formula for $v_2(20!) = 18$, and Fermat's Little Theorem proved.
- **B1–B10 (Manipulation Drills):** Divisor count functions ($\tau(360) = 24$), Chinese Remainder Theorem intersections, powers of 10 digit sums, modular inverse linear congruences ($4x \equiv 5 \pmod 7$), binomial expansions of $99^2 \pmod{100}$, $\gcd(a^m-1, a^n-1) = a^{\gcd(m,n)}-1$, and consecutive integer cube bounds proved.
- **C1–C8 (Substitution & Structure):** Rational function integer values via polynomial division ($\frac{x^2+5}{x+1} = x-1+\frac{6}{x+1}$), Simon's Favourite Factoring Trick ($\frac{1}{a}+\frac{1}{b}=\frac{1}{6} \implies (a-6)(b-6)=36$), roots of unity dividing $x^n-1$, simultaneous mod 9 & mod 11 digit constraints, $v_2(3^{256}-1)$ difference of squares cascade, and palindromic concatenation divisibility by 11 proved.
- **D1–D5 (Olympiad Challenge):** Divisor sum invariants ($\frac{n^3+100}{n+10} = n^2-10n+100 - \frac{900}{n+10} \implies \sum n = -540$), base-3 digit combination mod 3 counting, integer polynomial root bounds ($P(r)=0 \implies (r-a) \mid P(a)$), multi-power LCM conditions ($n/2$ sq, $n/3$ cube, $n/5$ 5th power), and Diophantine factorial equation $x^2 - y! = 2016 \implies (84, 7)$ proved.

### Sheet 02
- **A1–A10 (Rapid Recognition):** Complete factorisation of $1001 = 7 \times 11 \times 13$, $10^5 \equiv -1 \equiv 10 \pmod{11}$, $7^{100} \equiv 1 \pmod{10}$, square completion factors, Euclidean algorithm GCD, smallest primes $> 30$, and prime factor sums proved.
- **B1–B10 (Manipulation Drills):** Number of divisors $\tau(144) = 15$, simultaneous LCM congruences ($x \equiv 1 \pmod{3,4,5} \implies x=61$), modular inverses ($5x \equiv 1 \pmod 7$), Legendre's formula for $v_5(100!) = 24$, binomial expansion for $51^2 \pmod{100}$, factorial divisibility thresholds, and digit sum invariant of $2^{10} \times 5^8$ proved.
- **C1–C8 (Substitution & Structure):** Algebraic factorisation for prime values ($n^2-4n-5 = (n-5)(n+1)$), rational function domain bounds, completing the square for Diophantine equations ($n^2+8n = k^2$), prime digit product counting, quadratic residues mod 5, Euler totient coprime pairs ($\phi(20) = 8$), and sum of cubes remainder isolation proved.
- **D1–D5 (Olympiad Challenge):** Place value summation of digit permutations ($\sum \text{perm}(1,2,3,4) = 66660$), parity matching difference of squares ($a^2-b^2=2024$), Legendre trailing zero remainder mod 100, bivariate modular residue counting ($x^2+y^2 \equiv 0 \pmod 5$), and Euclidean polynomial GCD bounds $\gcd(n^2+3, n+2) = 7$ proved.

### Sheet 03
- **A1–A10 (Rapid Recognition):** Rapid modular evaluations ($(10^{10}+10^5+1) \pmod 9 = 3$), unit digit cycles, prime factorisations, product congruences mod 5, linear congruence inverses, and square completion proved.
- **B1–B10 (Manipulation Drills):** Factor extraction from exponential sums ($3^{2026}+3^{2025}+3^{2024} = 13 \times 3^{2024}$), Legendre $v_2(100!) = 97$, integer ratio maximisation $\frac{10a+b}{a+b} \le 9$, integer divisor pairs $xy=24$, prime forms $p^2+2$, and terminal digits of $5^{2026}+6^{2026}$ proved.
- **C1–C8 (Substitution & Structure):** SFFT for Egyptian fractions ($1/x+1/y=1/3$), minimal coordinate difference of squares, Sophie Germain factoring for $x^4+x^2+1 = (x^2-x+1)(x^2+x+1)$, divisibility by 36 digit constraints, subset mod 3 combinatorial partition counting, and binomial expansion for $2019^{2025} \pmod{100}$ proved.
- **D1–D5 (Olympiad Challenge):** Combinatorial prime exponent LCM pairs ($(2x+1)(2y+1)(2z+1)$), prime solutions to $p^2-2q^2=1$, infinite descent on $x^3+2y^3=4z^3 \implies (0,0,0)$, and 3-digit terminal cycles of $7^{9999}$ and $2025^{2026}$ proved.

### Sheet 04
- **A1–A10 (Rapid Recognition):** Modular sums $(2^{10}+3^{10}) \pmod 5 = 3$, Euclidean algorithm remainders, divisor counting, LCM computations, and Legendre valuations proved.
- **B1–B10 (Manipulation Drills):** Square scaling factors, trailing zeros $v_5(50!) = 12$, Fermat's Little Theorem reductions ($5^{2025} \pmod 7$), modular polynomial evaluation, CRT intersections, divisor sums $\sigma(100) = 217$, and odd exponent divisibility $a+b \mid a^n+b^n$ proved.
- **C1–C8 (Substitution & Structure):** Difference of squares decompositions ($x^2-y^2=45$), prime difference constraints $p=a^2-b^2$, polynomial division remainders, integer divisor lists for rational fractions, perfect square divisor counts ($10^{10}$), Principle of Inclusion-Exclusion (PIE) for non-multiples of $2,3,5$, and prime relations $p=q^2-36$ proved.
- **D1–D5 (Olympiad Challenge):** Catalan's conjecture special case $3^m-2^n=1 \implies (1,1), (2,3)$, Sophie Germain identity for $n^4+4^n$, Fibonacci sequence modulo 3 periodicity (period 8), prime difference of squares $p=9q^2-r^2$, and Lifting The Exponent (LTE) lemma for $v_2(3^{1024}-1) = 12$ proved.

### Sheet 05
- **A1–A10 (Rapid Recognition):** Modular cycles for powers of 3, 7, prime factorisations of 1001 and 360, GCD and divisor counts, and Chinese Remainder Theorem basics proved.
- **B1–B10 (Manipulation Drills):** Legendre valuations $v_7(50!) = 8$, cube completion factors ($15n$ cube $\implies n=225$), factorial sum mod 12 ($k! \equiv 0 \pmod{12}$ for $k \ge 4$), exponent comparison ($3^{40} > 4^{30}$), Euler totient last digits, square divisors of 1000, and SFFT for $xy=x+y+3$ proved.
- **C1–C8 (Substitution & Structure):** Rational polynomial integer sum $\frac{n^2+3n+5}{n+1}$, power of 2 factor detection, prime difference of squares ($x^2-y^2=17$), LCM ordered pair counts ($(2a+1)(2b+1)(2c+1) = 75$), prime square divisor counts, and cyclic integer triples $xyz=x+y+z \implies (1,2,3)$ proved.
- **D1–D5 (Olympiad Challenge):** Primes $p^2+2$, algebraic curve parameterisation $x^2 y = x^2 + 3y + 2 \implies (2,6)$, Egyptian fraction bounding $1/x+1/y=1/6 \implies 5$ pairs, symmetric modular sum cancellation $\sum_{x=1}^{10} x^{2025} \equiv 0 \pmod{11}$, and Sophie Germain prime identity $n^4+4 \implies \sum n = 0$ proved.

### Sheet 06
- **A1–A10 (Rapid Recognition):** Prime factorisations, GCD/LCM, unit digits, digit sum divisibility ($47d53$ div by 9), and base comparison ($3^{200} > 2^{300}$) proved.
- **B1–B10 (Manipulation Drills):** Trailing zeros of $20! = 4$, linear congruences mod 7, prime differences $p^2-q^2=24 \implies p+q=12$, modular periodicity $5^n \equiv 25 \pmod{100}$, square divisors of 3600, 3-adic valuation of $27^5 \times 9^4 = 23$, smallest integer with 6 divisors ($12$), and maximum sum under GCD constraints proved.
- **C1–C8 (Substitution & Structure):** SFFT for $xy+x+y=23$, prime structure mod 3, 3-digit palindrome divisibility by 11 ($8$ cases), consecutive product roots ($n(n^2-1)=336$), 4-digit reversed difference place value equations, rational quotient sum, and Euclidean GCD bounds proved.
- **D1–D5 (Olympiad Challenge):** Factorion digit sum equation $abc = a!+b!+c! \implies 145$, Euclidean polynomial GCD values $\gcd(n^2+3, n+1) \in \{1,2,4\} \implies \sum = 7$, last 3 digits of $2025^{2025} = 625$, exponent parity conditions for $n^n$ square ($55$), and Egyptian fraction triple maximum sum ($x+y+z = 11$) proved.

### Sheet 07
- **A1–A10 (Rapid Recognition):** Prime factorisations ($91 = 7 \times 13$, $323 = 17 \times 19$), GCD evaluations, modular reductions, divisor counts, and power comparisons proved.
- **B1–B10 (Manipulation Drills):** Binomial last two digits ($7^4 \equiv 01 \pmod{100}$), trailing zeros, square completion ($120n \implies 30$), Legendre $v_3(50!) = 22$, prime difference of squares ($x^2-y^2=17$), linear modular inverses, divisor sums $\sigma(50)=93$, and CRT bounds proved.
- **C1–C8 (Substitution & Structure):** Prime square divisor products ($\prod_{p^2 < 50} p^2 = 44100$), divisor count optimisation ($\tau(n)=15 \implies \min n = 144$), multiple-of-45 divisor counts ($64$), square divisors of $10!$, Euclidean polynomial GCD $\gcd(n^2+5, n+2) = 9$, 15-digit place value difference digit sum, and cubic difference $(x-y)(x^2+xy+y^2)=37 \implies (4,3)$ proved.
- **D1–D5 (Olympiad Challenge):** Quadratic Diophantine circle bounding $(2x+y)^2+3y^2=28 \implies 12$ integer pairs, exponent parity square counts ($55$), difference of squares factor systems $a^2-4b^2=45$, Fermat prime factorisation of $2^{16}-1 \implies 257$, and prime parity Diophantine $p^2-2q^2=1 \implies p+q=5$ proved.

---

## 3. Verification Suite Architecture & Compliance

- **No Hardcoded Values:** Every check dynamically queries `tools.latex_bridge.get_answer()` and asserts mathematical equivalence against independently computed values.
- **Optimization Guard:** Every verification script includes `if not __debug__:` to prevent running under `-O` where assertions are stripped.
- **Exhaustive & Property-Based:** All check functions carry `"""EXHAUSTIVE PROOF: ..."""` or `"""SAMPLED CHECK: ..."""` docstrings.
- **Validation:** All scripts pass `tools/validate_verify_scripts.py` and `number-theory/verify/run_all.py` with exit code 0.
