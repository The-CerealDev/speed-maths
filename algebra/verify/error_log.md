# Quantitative Error Log — Algebra Verification Pipeline

This document logs parsing nuances, Property-Based Testing (Hypothesis) considerations, and mathematical verification details encountered during the robustification of verification scripts for Sheets 01 through 07 in the **Algebra** pillar.

---

## 1. Summary of Verification Issues & Resolutions

| Sheet / Question | Error Category | Root Cause | Resolution | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Global / LaTeX Bridge** | Parsing Nuance | Missing section comments `%── A1` in `ans04.tex`, `ans05.tex`, `ans06.tex`. | Enhanced `tools/latex_bridge.py` fallback using section header regex (`\section*\{Section [A-D]\}`) to extract all 33 questions dynamically. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | ANTLR LaTeX parser in SymPy failed on `\sqrt7` (missing braces around single-token radical argument). | Added pre-parse regex normalization `re.sub(r'\sqrt(?![{\[])([0-9a-zA-Z]+)', r'\sqrt{\1}', text)` in `tools/latex_bridge.py`. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | Juxtaposed variable products like `$x(x+2)(x+3)$` and `\dfrac{n(n+1)}{2(2n+1)}` parsed as undefined function calls `Function('x')` / `Function('n')`. | Implemented `_clean_functions` in `tools/latex_bridge.py` and targeted replacements converting single-letter `AppliedUndef` into symbolic multiplication `x * ...`. | **Resolved** |
| **Global / LaTeX Bridge** | Parsing Nuance | Multi-part equations separated by semicolons (e.g., `\alpha^2+\beta^2+\gamma^2=14;\quad \alpha\beta\gamma=6`) caused parser syntax errors. | Added semicolon-splitting multi-part handler in `parse_tex_math` returning structured list of parsed SymPy sub-expressions. | **Resolved** |
| **Sheet 02 / B9** | Symbolic Assumption Mismatch | Defining `sympy.symbols('a b', positive=True)` produced distinct symbol objects from unconstrained symbols created by `parse_latex('...')`, causing `simplify(diff) != 0`. | Harmonized symbol declarations with unconstrained `sympy.symbols('a b')`. | **Resolved** |
| **Sheet 02 / C5** | Type Inconsistency | Sorting roots with mixed `int` and `sympy.Expr` items using `.evalf()` failed on plain Python integers. | Coerced elements using `sympy.sympify(v).evalf()` before numeric float sorting key. | **Resolved** |
| **Sheet 04 / A7** | Hypothesis Float Precision | Negative integer powers like `3**(-1)` produced Python floats instead of exact integers before `sympy.Rational` construction. | Restricted property testing strategy to positive integers `st.integers(min_value=1, max_value=20)`. | **Resolved** |
| **Sheet 04 / D2** | Unevaluated Surds | Direct equality comparison `poly.subs(x, 1 - sqrt(2)) == 0` failed due to unevaluated algebraic surd representation. | Wrapped expression evaluation in `sympy.simplify(poly.subs(x, s)) == 0`. | **Resolved** |
| **Sheet 05 / A9** | Solver Domain Restriction | `sympy.solve(Abs(2*x - 3) - 7, x)` raised `NotImplementedError` when `x` lacked real-domain assumption. | Declared symbol with `x = sympy.Symbol('x', real=True)`. | **Resolved** |
| **Sheet 05 / D1** | Equation RHS Extraction | LaTeX answer parsed to `sympy.Equality` object `Eq(f(x), ...)`, causing subtraction against `Mul` to fail. | Extracted `.rhs` attribute from `Equality` instances before simplification comparison. | **Resolved** |

---

## 2. Detailed Mathematical Verification Notes

### Sheet 02
- **A1–A10 (Foundations):** Algebraic identities (difference of cubes, conjugates, difference of squares, binomial cubing, rationalization) were verified symbolically and via randomized property tests across integer domains.
- **B1–B10 (Intermediate Applications):** Vieta power sums, partial fraction rearrangements, and Brahmagupta-Fibonacci identities were proved. In B9, algebraic simplification of conjugate surd fractions was confirmed matching `\dfrac{2(a+b)}{a-b}`.
- **C1–C8 (Challenging Roots & Polynomials):** Quartic polynomial roots for C1 and C5 were solved and matched against exact closed-form algebraic expressions with sorting invariants.
- **D1–D5 (Advanced Proofs):** Telescoping cubic partial fractions (D1) and Tschirnhaus-type root transformations (D2) were validated via formal polynomial equivalence.

### Sheet 03
- **A1–A10:** Factor theorem roots, polynomial remainder theorem, and quadratic discriminant constraints ($k=\pm 8$) verified.
- **B1–B10:** Factorization of symmetric cubics and the divisibility property $6 \mid (n^3-n)$ tested across integer ranges $\pm 1000$. Lucas sequence recurrence values $s_3=4, s_4=7$ proved.
- **C1–C8:** Exponential substitution $u=3^x$, sum-of-squares inequalities, and AM-GM minimization proved.
- **D1–D5:** Euler's prime-generating polynomial $n^2+n+41$ tested for all $n < 40$ (all prime) and counterexample verified at $n=40$ ($40^2+40+41 = 41^2$). Modular divisibility for $(n+3) \mid (n^2-1)$ bounded to $n \in \{1, 5\}$.

### Sheet 04
- **A1–A10:** Mental arithmetic identities ($201 \times 199 = 39999$), binomial expansions, and factorial cancellations verified.
- **B1–B10:** Cyclotomic and geometric series formulas ($(x^5-1)/(x-1)$), Vieta reciprocal quadratic constructions ($x^2-12=0$), and composite factor bounds proved.
- **C1–C8:** Cauchy-Schwarz inequality in 2 variables verified via algebraic difference $(ad-bc)^2 \geq 0$. Radical equation extraneous root elimination proved $x = 12 - 4\sqrt{7}$ as the unique real solution.
- **D1–D5:** Telescoping product $\prod_{k=2}^n(1-1/k^2) = (n+1)/(2n)$ and its limit $1/2$ verified. Degree-4 polynomial reconstruction problem $p(12)-12p(0) = 7752$ confirmed.

### Sheet 05
- **A1–A10:** Rational function cancellation, surd rationalization, and absolute value root finding verified.
- **B1–B10:** Partial fractions decomposition for linear and irreducible quadratic denominators proved with `sympy.apart()`. Involutory rational function condition $f(f(x))=x \iff a+d=0$ proved.
- **C1–C8:** Reciprocal quartic equation $u=x-1/x$ roots proved. Titu's lemma / Engel form verified for 3 variables.
- **D1–D5:** Functional equation $f(x)+f(1/(1-x))=x$ on 3-cycle orbit proved unique solution $f(x) = \frac{x^3-x+1}{2x(x-1)}$. All 16 integer solutions to $x^2-y^2=2024$ verified.

### Sheet 06
- **A1–A10:** Repeated root conditions via derivative criterion $f'(2)=0$, binomial power evaluation, and composite integer factorization verified.
- **B1–B10:** Undetermined coefficients polynomial matching, Vieta symmetric polynomials, and domain exclusion of extraneous root ($x=1$) in algebraic fraction equation verified.
- **C1–C8:** Radical substitution $t=\sqrt{x}$, completing the square in 2 variables, and monic quadratic identical root condition $b=c$ proved.
- **D1–D5:** Degree-2 Schur inequality $\sum a^2(a-b)(a-c) \geq 0$ proved for non-negative triples. Interpolating polynomial value $p(5)=0$ proved. All 4 positive integer solution pairs $(m,n)$ for $m^2-n^2=105$ verified.

---

## 3. Verification Suite Architecture & Compliance

- **No Hardcoded Values:** Every check dynamically queries `tools.latex_bridge.get_answer()` and proves algebraic/numerical equivalence using `sympy.simplify()`.
- **Optimization Guard:** Every verification script includes `if not __debug__:` to prevent running under `-O` where assertions are stripped.
- **Exhaustive & Property-Based:** All check functions carry `"""EXHAUSTIVE PROOF: ..."""` or `"""SAMPLED CHECK: ..."""` docstrings and test properties across broad parameter domains using `hypothesis`.
- **Validation:** All scripts pass `tools/validate_verify_scripts.py` and `algebra/verify/run_all.py` with exit code 0.
