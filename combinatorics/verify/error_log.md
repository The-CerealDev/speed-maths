# Quantitative Error Log — Combinatorics Verification Pipeline

This document logs parsing nuances, Property-Based Testing (Hypothesis) considerations, and mathematical verification details encountered during the robustification of verification scripts for Sheets 01 through 07 in the **Combinatorics** pillar.

---

## 1. Summary of Verification Issues & Resolutions

| Sheet / Question | Error Category | Root Cause | Resolution | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Global / LaTeX Bridge** | Parsing Nuance | Multi-part equations with text notes (e.g., `$\binom{10}{2}=45$ segments;\quad $\binom{10}{3}=120$ triangles`) parsed words as symbolic products. | Added regex to strip descriptive text units (`segments`, `triangles`, `in total`, `avoid A`, etc.) in `tools/latex_bridge.py`. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | Answers with arithmetic equations evaluating to True in SymPy (e.g. `2^6=64`) produced `BooleanTrue` instead of the numeric RHS. | Enhanced `parse_tex_math` in `tools/latex_bridge.py` to extract the numerical RHS when an equation string evaluates to boolean. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | Comma-separated list outputs (e.g., Pascal row entries `1,\;5,\;10,\;10,\;5,\;1`) parsed only the first element. | Generalized comma-separated parser in `tools/latex_bridge.py` to return structured lists of parsed SymPy integers. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | Floating-point representations in small decimal expansions (e.g., `1.01^{10} \approx 1.1045`) evaluated to `BooleanFalse` on equality check. | Fallback in `tools/latex_bridge.py` to parse the rightmost numeric literal of arithmetic equations. | **Resolved** |
| **Sheet 02 / C4** | Multi-part Answer Structure | LaTeX answer contained both total triangles and triangles avoiding point A; unpacking expected scalar. | Handled structured list response in `check_C4()` extracting the second element (`35`). | **Resolved** |
| **Sheet 04 / B2** | Exponent Index Alignment | Question asked for $x^5$ coefficient in $(1+2x)^4(1+x)^3$; initial test template had transposed indices. | Aligned polynomial product and power monomial target to $x^5$ ($168$). | **Resolved** |
| **Sheet 06 / C4, C8** | Non-numeric Descriptive Answers | Qualitative proof questions like "Impossible." and "Forced." parsed as symbolic multiplications of single-letter variables. | Added keyword classification in `tools/latex_bridge.py` returning verbatim strings for known descriptive answers. | **Resolved** |

---

## 2. Detailed Mathematical Verification Notes

### Sheet 02
- **A1–A10 (Combinations & Basic Choices):** Basic combinations $\binom{7}{2}=21$, $\binom{8}{3}=56$, $\binom{9}{7}=36$, $\binom{6}{3}=20$ verified via exhaustive subset enumeration. Symmetry and triangular number properties verified with Hypothesis.
- **B1–B10 (Manipulation Drills):** Grid paths, committee chair identity ($r\binom{n}{r}=n\binom{n-1}{r-1}$), binary strings, and backward Pascal solving verified symbolically and computationally.
- **C1–C8 (Substitution & Structure):** Restricted committees, 4-digit repetition counts ($4464$), polygon diagonals ($n(n-3)/2$), and card hands with $\geq 3$ aces ($4560$) independently computed.
- **D1–D5 (Challenge):** Rectangles on $4\times 4$ grid ($100$), Fibonacci non-consecutive subsets ($55$), majority junior committees ($1586$), 2-regular graphs ($70$), and circle chord intersections ($\binom{10}{4}=210$) verified.

### Sheet 03
- **A1–A10 (Arrangements & Circular Permutations):** Distinct permutations ($5!=120$), multiset arrangements (`BANANA` $=60$, `NOON` $=6$, `TATTY` $=20$), and circular arrangements ($(n-1)!$) proved.
- **B1–B10 (Blocks & Gaps):** Adjacent blocks ($2\cdot 5!=240$), non-adjacent complement ($480$), Mississippi multinomial ($34650$), gap placement ($14400$), alternating gender ($1152$), and forced trilogy ordering ($840$) proved.
- **C1–C8 (Layered Constraints):** Trio together + pair apart ($2880$), consecutive + height ordered ($720$), multiset with prohibited subwords (`DIVIDED` without `DDD` $=360$), alternating circular seating ($144$), and dice/even digit constraints proved.
- **D1–D5 (Advanced Challenges):** Seven-digit parity ordered numbers ($35$), circular two-pair constraints ($60480$), `AABBCC` no identical adjacent ($30$), exactly two sisters adjacent ($21600$), and 8-knights feuders with royal block ($288$) verified.

### Sheet 04
- **A1–A10 (Binomial Expansions):** Polynomial coefficient extractions, Pascal row expansions, constant terms in $(x+1/x)^4$, and alternating sums proved via SymPy polynomials and Hypothesis.
- **B1–B10 (Coefficient Extraction):** Convolution of $(1+2x)^4(1+x)^3$, binomial integer equations, multinomial $(a+b+c)^5$ coefficient $a^2b^2c=30$, and mental arithmetic $11^3=1331, 9^3=729$ proved.
- **C1–C8 (Identities & Roots):** Even-index binomial sums $\sum \binom{10}{2k} = 512$, $1.01^{10}$ Taylor approximation, derivative identity $\sum k\binom{n}{k} = n 2^{n-1}$, and reversal substitution $\sum \binom{6}{k}2^k = 729$ proved.
- **D1–D5 (Combinatorial Proofs):** Central binomial even parity $\binom{2n}{n} \equiv 0 \pmod 2$, sum of squares $\sum \binom{n}{k}^2 = \binom{2n}{n}$, Lucas parity patterns in $(1+x)^{12}$ ($k \in \{0,4,8,12\}$), hockey stick identity $\sum \binom{m}{2} = \binom{n}{3}$, and prime divisibility $p \mid \binom{p}{k}$ proved.

### Sheet 05
- **A1–A10 (Stars & Bars & Inclusion-Exclusion):** Non-negative vs positive partitions ($x+y+z=4 \implies 15$, $x+y+z=6 \implies 10$), two-set inclusion-exclusion, and compositions proved.
- **B1–B10 (Bound Shifts & Complements):** Per-variable lower bounds ($x \geq 2 \implies \binom{10}{2}=45$), integer divisibility counts, compositions into 3 parts ($21$), and slack variable inequality bounds ($x+y \leq 5 \implies 21$) proved.
- **C1–C8 (Capped Variables & Multi-set I-E):** Upper bounds with inclusion-exclusion ($x+y+z+w=15, x_i \leq 5 \implies 52$), 3-set beverage surveys ($20$), 3-dice sum 10 ($27$), and 3-digit number digit sum 12 ($73$) proved.
- **D1–D5 (Advanced Inclusions):** Derangements $D_4=9$, composition count $2^{n-1}$, Euler totient $\varphi(360)=96$, surjective assignments of 5 students to 3 clubs ($150$), and square/cube non-multiples up to $10^6$ ($998910$) verified.

### Sheet 06
- **A1–A10 (Pigeonhole & Handshake Lemma):** Adversarial sock drawing ($3$ and $12$), birthday/weekday pigeons, parity boxes, handshake lemma $\sum \deg = 2E$, and double counting proved.
- **B1–B10 (Residue Pigeons & Extremal Sets):** Table seating adjacency threshold ($7$), residue differences mod 7, subset sum pairs summing to 11 ($6$), round-robin matches ($28$), and committee-member double counting ($10$) proved.
- **C1–C8 (Multi-dimensional & Invariant Pigeons):** Adversarial beads ($13$ vs $25$), mutilated chessboard domino impossibility, 2D pigeonholes (month $\times$ weekday $=85$), circular triple averaging ($\geq 15$), and difference 4 pairs proved.
- **D1–D5 (Classic Olympiad Proofs):** Unit square diameter $\sqrt{2}/2$, lattice midpoint parity classes, even number of odd vertices, 2-problem selection pigeonhole, and Ramsey number $R(3,3)=6$ proved.

---

## 3. Verification Suite Architecture & Compliance

- **No Hardcoded Values:** Every check dynamically queries `tools.latex_bridge.get_answer()` and proves algebraic/numerical equivalence using `sympy.simplify()`.
- **Optimization Guard:** Every verification script includes `if not __debug__:` to prevent running under `-O` where assertions are stripped.
- **Exhaustive & Property-Based:** All check functions carry `"""EXHAUSTIVE PROOF: ..."""` or `"""SAMPLED CHECK: ..."""` docstrings and test properties across broad parameter domains using `hypothesis`.
- **Validation:** All scripts pass `tools/validate_verify_scripts.py` and `combinatorics/verify/run_all.py` with exit code 0.
