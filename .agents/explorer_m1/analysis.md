# Codebase Analysis - Answer Keys (Milestone 1)

## Executive Summary
This report presents a thorough audit and structural classification of the LaTeX answer key files for algebra and combinatorics, covering **Sheets 2 through 7** (12 files total). Each sheet contains exactly 33 questions distributed across four sections:
- **Section A: Rapid Recognition** (10 questions, A1–A10)
- **Section B: Manipulation Drills** (10 questions, B1–B10)
- **Section C: Substitution & Structure** (8 questions, C1–C8)
- **Section D: Challenge** (5 questions, D1–D5)

In total, **396 questions** (198 for Algebra, 198 for Combinatorics) were extracted, along with their official answers (`\ans{...}`) and step-by-step methodologies (`\method{...}`). The mathematical types have been analyzed to plan exact, automated verification methods (e.g., symbolic computation with SymPy, numerical validation, and combinatorial simulation).

## Mathematical Classifications & Verification Plan

### 1. Algebra Questions
For the 198 algebra questions, the mathematical sub-disciplines are classified as follows:

| Math Type | Count | Description / Examples | Verification Method |
|---|---|---|---|
| polynomial algebra / factorisation | 105 | Factoring trinomials, Sophie Germain, difference of cubes (e.g. $x^3-27$, $3x^2-75$, $x^4-x^2-12$) | Use SymPy's `factor` or `expand` to verify identity equivalence: `simplify(LHS - RHS) == 0`. |
| surds / denesting | 25 | Rationalising denominators, denesting nested surds (e.g. $\sqrt{6+2\sqrt{5}}$) | Use SymPy's `sqrtdenest` or verify equivalence numerically via high-precision float comparison (`mpmath`). |
| algebraic inequalities | 20 | Weighted and unweighted AM-GM proofs, maximum/minimum value constraints | Symbolic verification of inequality boundaries; check sign of first/second derivatives. |
| Vieta's formulas & symmetric polynomials | 16 | Symmetric root sums ($p^2+q^2$, $a^3+b^3+c^3-3abc$ from coefficients) | Use SymPy's elementary symmetric polynomials module or construct the polynomial roots and check. |
| sequences & series / telescoping | 13 | Telescoping sums and products, infinite sums, geometric series | Use SymPy's `summation` or `product` symbolically, or evaluate finite series using Python loops. |
| functions | 9 | Function compositions, M"obius inverse functions ($f^{-1}(x)$) | Define SymPy `Lambda` expressions, compute composition, and check `f(f_inv(x)).simplify() == x`. |
| divisibility & number theory | 6 | Polynomial divisibility, prime counterexamples (e.g., Euler's trinomial prime counterexample) | Use SymPy's `div` for polynomial remainder, and `isprime` for number theory primality verification. |
| logarithms | 2 | Logarithm laws, base changes | Simplify with SymPy `log(x, base)`. |
| integer arithmetic | 2 | Evaluating purely numerical arithmetic expressions (e.g., $7^2-5^2+3^2-1^2$, $2^{10}-1$ factorisation) | Evaluate numerically using basic Python calculations. |

### 2. Combinatorics Questions
For the 198 combinatorics questions, the mathematical sub-disciplines are classified as follows:

| Math Type | Count | Description / Examples | Verification Method |
|---|---|---|---|
| combinatorial counting | 85 | Unordered/ordered selection with constraints (e.g. no adjacent items, circular arrangements) | Verify with exact recurrence relations, and double-check using brute-force state enumeration in Python. |
| combinations & permutations | 45 | Evaluating $\binom{n}{r}$, permuting subsets | Use Python's built-in `math.comb` and `math.perm`. |
| factorials | 41 | Simplifying factorial ratios (e.g., $(2n)! / (2n-1)!$) | Use SymPy's `factorial` or integer evaluation for test cases. |
| binomial theorem / coefficients | 17 | Identities like $\sum \binom{n}{k} = 2^n$ or finding coefficients | Use SymPy's symbolic expansion of $(x+y)^n$ or sum evaluations. |
| bijections / grid paths | 6 | Grid routing, bijection maps between sets | Compare combinatorial formula against dynamic programming grid traversal in Python. |
| stars and bars / distribution | 3 | Distributing identical items to distinct bins under constraints | Apply standard stars and bars formula: `math.comb(n + k - 1, k - 1)`. |
| inclusion-exclusion | 1 | PIE applications on multiple overlapping sets | Verify with Venn/set arithmetic or recursive exclusion formulas. |

## Detailed Question Index (Sheets 2–7)

### Algebra Answer Keys

#### Sheet 02

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$(x-3)(x^2+3x+9)$` | polynomial algebra / factorisation | Sum/difference of cubes: $a^3-b^3=(a-b)(a^2+ab+b^2)$ with $a=x$, $b=3$. The quadratic factor is irreducible over $\mathbb{R}$. |
| A2 | `$2$` | surds / denesting | Conjugate product: $(a+b)(a-b)=a^2-b^2 = 5-3=2$. This is the core move for rationalising surds. |
| A3 | `$998\,000$` | polynomial algebra / factorisation | $999^2-1^2=(999+1)(999-1)=1000\times 998=998\,000$. Treat every ``near-square minus 1'' as a difference of two squares. |
| A4 | `$26$` | polynomial algebra / factorisation | $(a-b)^2 = a^2-2ab+b^2 = 16$, so $a^2+b^2=16+2(5)=26$. Never solve for $a$ and $b$ individually. |
| A5 | `$3xy(x+y)$` | polynomial algebra / factorisation | Expand $(x+y)^3=x^3+3x^2y+3xy^2+y^3$ then cancel $x^3$ and $y^3$. Factor out $3xy$. Memorise: $(x+y)^3-x^3-y^3=3xy(x+y)$. |
| A6 | `$3(x-5)(x+5)$` | polynomial algebra / factorisation | Take out the common factor of 3 first, giving $3(x^2-25)$, then apply difference of two squares. Always extract scalars before factorising. |
| A7 | `$\sqrt{3}-\sqrt{2}$` | surds / denesting | Multiply top and bottom by the conjugate $(\sqrt{3}-\sqrt{2})$. Denominator becomes $3-2=1$. The result is exact and requires no further work. |
| A8 | `$(x-1)(x-1)(x+1)=(x-1)^2(x+1)$` | polynomial algebra / factorisation | $(x-1)$ is a common factor: $(x-1)(x^2-1)=(x-1)(x-1)(x+1)$. Always look for a common binomial factor before anything else. |
| A9 | `$19$` | polynomial algebra / factorisation | By Vieta: $p+q=5$, $pq=3$. Then $p^2+q^2=(p+q)^2-2pq=25-6=19$. This is Vieta + Newton identity: essential toolkit. |
| A10 | `$7$` | polynomial algebra / factorisation | Factor $2^n$ from the numerator: $\dfrac{2^n(2^3-1)}{2^n}=8-1=7$. Powers of 2 always simplify by factoring out the smallest power. |
| B1 | `$\dfrac{2x+1}{(x-1)(x+1)}$` | polynomial algebra / factorisation | Common denominator is $(x-1)(x+1)$. Numerator: $x + (x+1) = 2x+1$. Do not expand the denominator. |
| B2 | `$(x^2-4)(x^2+3)=(x-2)(x+2)(x^2+3)$` | polynomial algebra / factorisation | Let $u=x^2$: $(u-4)(u+3)=0$. Only $u=4$ gives real solutions. The factor $(x^2+3)$ is irreducible over $\mathbb{R}$. |
| B3 | `$r=1-\dfrac{a}{S}=\dfrac{S-a}{S}$` | sequences & series / telescoping | $S(1-r)=a \Rightarrow 1-r=a/S \Rightarrow r=1-a/S$. This is the geometric series sum formula --- essential for TMUA Paper 1. |
| B4 | `$\dfrac{x+1}{x}\cdot\dfrac{x}{x+1}=1$` | sequences & series / telescoping | Write each factor as a single fraction: $\tfrac{x+1}{x}\cdot\tfrac{x}{x+1}$. The product telescopes to 1. Recognise the cancellation \emph{before} multiplying out. |
| B5 | `$18$` | functions | $x^3+y^3=(x+y)(x^2-xy+y^2)=(x+y)\!\left[(x+y)^2-3xy\right]=3(9-3)=18$. Build up from symmetric functions --- never solve for $x$ and $y$. |
| B6 | `$1$` | polynomial algebra / factorisation | $(a+b)^2-(a-b)^2 = 4ab$ by the identity $(P+Q)^2-(P-Q)^2=4PQ$. The expression equals $4ab/4ab=1$. |
| B7 | `$(x-1)(x+1)(x+3)$` | polynomial algebra / factorisation | Group: $(x^3+3x^2)-(x+3)=x^2(x+3)-(x+3)=(x+3)(x^2-1)=(x+3)(x-1)(x+1)$. Grouping is faster than the factor theorem here. |
| B8 | `$x = 7$` | polynomial algebra / factorisation | Cross-multiply: $(x-1)(x+8)=(x+3)(x+2)$. Expand both sides: $x^2+7x-8=x^2+5x+6$. The $x^2$ terms cancel: $2x=14$, so $x=7$. Check: LHS $= \tfrac{6}{9}=\tfrac{2}{3}$, RHS $=\tfrac{10}{15}=\tfrac{2}{3}$. |
| B9 | `$\dfrac{2(a+b)}{a-b}$` | surds / denesting | Let $P=\sqrt{a}+\sqrt{b}$, $Q=\sqrt{a}-\sqrt{b}$. The expression is $\tfrac{Q}{P}+\tfrac{P}{Q}=\tfrac{P^2+Q^2}{PQ}$. $P^2+Q^2=2(a+b)$, $PQ=a-b$. |
| B10 | `$\alpha^2+\beta^2+\gamma^2=14$;\quad $\alpha\beta\gamma=6$` | Vieta's formulas & symmetric polynomials | By Vieta's formulas: $\alpha+\beta+\gamma=6$, $\alpha\beta+\beta\gamma+\gamma\alpha=11$, $\alpha\beta\gamma=6$. Then $\alpha^2+\beta^2+\gamma^2=(\alpha+\beta+\gamma)^2-2(\alpha\beta+\beta\gamma+\gamma\alpha)=36-22=14$. |
| C1 | `$x=\pm 2,\;\pm 3$` | polynomial algebra / factorisation | Let $u=x^2$: $(u-4)(u-9)=0$, giving $u=4$ or $u=9$. Both positive, so four real solutions $x=\pm2,\pm3$. |
| C2 | `$x=0$ and $x=-5$` | polynomial algebra / factorisation | Pair the outer and inner terms: $(x+1)(x+4)=x^2+5x+4$ and $(x+2)(x+3)=x^2+5x+6$. Let $u=x^2+5x+5$: $(u-1)(u+1)=24 \Rightarrow u^2=25 \Rightarrow u=\pm5$. $u=5$: $x^2+5x=0 \Rightarrow x(x+5)=0$. $u=-5$: $x^2+5x+10=0$, discriminant $<0$, no real solutions. |
| C3 | `$\sqrt{5}+1$` | surds / denesting | Write $6+2\sqrt{5}=5+2\sqrt{5}+1=(\sqrt{5}+1)^2$. Then $\sqrt{(\sqrt{5}+1)^2}=\sqrt{5}+1$ (positive root). |
| C4 | `$ab+bc+ca=0$;\quad $a^3+b^3+c^3-3abc=1$` | polynomial algebra / factorisation | $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca) \Rightarrow 1=1+2(ab+bc+ca)$, so $ab+bc+ca=0$. Then apply the factorisation $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)=1\cdot(1-0)=1$. Note $abc$ itself is \emph{not} determined by the given data --- only the combination $a^3+b^3+c^3-3abc$ is. |
| C5 | `$x=2,\;6,\;4\pm\sqrt{6}$\; (all four real)` | surds / denesting | Pair: $(x-1)(x-7)=x^2-8x+7$ and $(x-3)(x-5)=x^2-8x+15$. $(u-4)(u+4)=u^2-16$, so $u^2-16+15=u^2-1=0 \Rightarrow u=\pm1$. $u=1$: $x^2-8x+10=0 \Rightarrow x=4\pm\sqrt{6}$. $u=-1$: $x^2-8x+12=0 \Rightarrow (x-2)(x-6)=0$. |
| C6 | `$14$` | surds / denesting | Note $\tfrac{1}{x}=\tfrac{1}{2+\sqrt{3}}=2-\sqrt{3}$ (conjugate rationalisation). So $x+\tfrac{1}{x}=(2+\sqrt{3})+(2-\sqrt{3})=4$. Then $x^2+\tfrac{1}{x^2}=\left(x+\tfrac{1}{x}\right)^2-2=16-2=14$. |
| C7 | `$7$` | polynomial algebra / factorisation | Let $t=\tfrac{a}{b}+\tfrac{b}{a}=3$. Then $\tfrac{a^2}{b^2}+\tfrac{b^2}{a^2}=\left(\tfrac{a}{b}+\tfrac{b}{a}\right)^2-2=9-2=7$. |
| C8 | `$2$` | polynomial algebra / factorisation | Let $s=x^2+y^2+z^2$. Since $x+y+z=0$: $(x+y+z)^2=0 \Rightarrow x^2+y^2+z^2=-2(xy+yz+zx)$, so $xy+yz+zx=-s/2$. Then $(x^2+y^2+z^2)^2=x^4+y^4+z^4+2(x^2y^2+y^2z^2+z^2x^2)$. Also $(xy+yz+zx)^2=x^2y^2+y^2z^2+z^2x^2+2xyz(x+y+z)=x^2y^2+y^2z^2+z^2x^2$. So $s^2=x^4+y^4+z^4+2\cdot s^2/4$, giving $x^4+y^4+z^4=s^2/2$. The ratio is $s^2/(s^2/2)=2$. |
| D1 | `$\dfrac{11}{45}$` | sequences & series / telescoping | Partial fractions: $\dfrac{1}{n(n+1)(n+2)}=\dfrac{1}{2}\!\left(\dfrac{1}{n(n+1)}-\dfrac{1}{(n+1)(n+2)}\right)$. This is a telescoping sum! Sum from $n=1$ to $8$: $\dfrac{1}{2}\!\left(\dfrac{1}{1\cdot2}-\dfrac{1}{9\cdot10}\right) =\dfrac{1}{2}\!\left(\dfrac{1}{2}-\dfrac{1}{90}\right) =\dfrac{1}{2}\cdot\dfrac{44}{90}=\dfrac{22}{90}=\dfrac{11}{45}$. |
| D2 | `$x^2-(p^2-2q-p)\,x+(q^2-p^3+3pq+q)=0$` | Vieta's formulas & symmetric polynomials | By Vieta on the original: $r+s=-p$, $rs=q$. New sum: $(r^2+s)+(s^2+r)=(r^2+s^2)+(r+s)=[(r+s)^2-2rs]+(r+s)=(p^2-2q)+(-p)=p^2-2q-p$. New product: $(r^2+s)(s^2+r)=r^2s^2+r^3+s^3+rs=q^2+(r+s)^3-3rs(r+s)+q =q^2+(-p)^3-3q(-p)+q=-p^3+3pq+q^2+q$. Required quadratic: $x^2-(p^2-2q-p)x+(-p^3+3pq+q^2+q)=0$. |
| D3 | `Under $x+y+z\neq0$: \;$k=\tfrac{1}{2}$ only.` | polynomial algebra / factorisation | Set each ratio equal to $k$: $x=k(y+z)$, $y=k(x+z)$, $z=k(x+y)$. Adding gives $x+y+z=2k(x+y+z)$. Since $x+y+z\neq0$, divide through to get $k=\tfrac12$. |
| D4 | `$85\times65=5525=74^2+7^2=71^2+22^2$.` | polynomial algebra / factorisation | \textit{Proof:} Expand the right-hand side: $(ac+bd)^2+(ad-bc)^2 = a^2c^2+2abcd+b^2d^2+a^2d^2-2abcd+b^2c^2 =a^2(c^2+d^2)+b^2(c^2+d^2)=(a^2+b^2)(c^2+d^2)$. $\square$ \textit{Representations:} Use $85=2^2+9^2$, and $65=1^2+8^2$ and $65=4^2+7^2$. $(2^2+9^2)(1^2+8^2)=(2\cdot1+9\cdot8)^2+(2\cdot8-9\cdot1)^2=74^2+7^2=5476+49=5525$. $\checkmark$ $(2^2+9^2)(4^2+7^2)=(8+63)^2+(14-36)^2=71^2+22^2=5041+484=5525$. $\checkmark$ |
| D5 | `All integers $n\geq 1$.` | divisibility & number theory | Use the identity $n^3-1=(n-1)(n^2+n+1)$. Therefore $n^2+n+1$ divides $n^3-1$ for every integer $n$, hence for all $n\geq1$. |


#### Sheet 03

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$k = 6$` | functions | \textbf{Factor Theorem:} if $(x-2)$ is a factor then $f(2)=0$. $8-12+2k-8=0 \Rightarrow 2k=12 \Rightarrow k=6$. Never do polynomial long division when the factor theorem gives a one-line equation. |
| A2 | `$0$` | polynomial algebra / factorisation | $p(1)=1^{100}-1=0$. So the remainder is $0$ and $(x-1)$ is in fact a factor. The Remainder Theorem makes this instantaneous --- no division required. |
| A3 | `$(2x-3)(3x+4)$` | polynomial algebra / factorisation | Product $= 6\times(-12)=-72$. Seek pair summing to $-1$: $-9$ and $8$. Split: $6x^2-9x+8x-12=3x(2x-3)+4(2x-3)=(2x-3)(3x+4)$. |
| A4 | `$x^n+1$` | polynomial algebra / factorisation | Difference of two squares: $x^{2n}-1=(x^n-1)(x^n+1)$. Cancel $(x^n-1)$. This is the $m=2$ case of the general factorisation $x^{mn}-1$. |
| A5 | `$6$` | algebraic inequalities | AM--GM: $x+\dfrac{9}{x}\geq 2\sqrt{x\cdot\dfrac{9}{x}}=2\cdot3=6$. Equality when $x=\tfrac{9}{x}$, i.e.\ $x=3$. Always suspect AM--GM when you see a sum of a quantity and its reciprocal (scaled). |
| A6 | `$(x^2+y^2)(x+y)(x-y)$` | polynomial algebra / factorisation | Apply difference of two squares twice: $x^4-y^4=(x^2+y^2)(x^2-y^2)=(x^2+y^2)(x+y)(x-y)$. The factor $x^2+y^2$ does not factorise further over $\mathbb{R}$. |
| A7 | `$6$` | Vieta's formulas & symmetric polynomials | Vieta: $\alpha+\beta=3$, $\alpha\beta=\tfrac{3}{2}$. $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=9-3=6$. Note: for a non-monic quadratic $ax^2+bx+c=0$, Vieta gives $\alpha+\beta=-b/a$, $\alpha\beta=c/a$. |
| A8 | `$n^2$` | polynomial algebra / factorisation | Factor: $(n+1)!-n!=n!\cdot n = n\cdot n!$. Then $\dfrac{n\cdot n!}{(n-1)!}=n\cdot\dfrac{n!}{(n-1)!}=n\cdot n=n^2$. Always factor out the smaller factorial first. |
| A9 | `$ab+bc+ca=4$` | polynomial algebra / factorisation | Expand $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)$. Rearrange. Substituting: $16-8=2(ab+bc+ca) \Rightarrow ab+bc+ca=4$. |
| A10 | `$k=\pm 8$` | Vieta's formulas & symmetric polynomials | A perfect-square quadratic has discriminant zero: $k^2-64=0 \Rightarrow k=\pm8$. Then $x^2+8x+16=(x+4)^2$ and $x^2-8x+16=(x-4)^2$. |
| B1 | `$(x-3)(x+2)(2x-1)$;\; rational roots: $x=3,\;-2,\;\tfrac{1}{2}$` | polynomial algebra / factorisation | \textbf{Rational Root Theorem:} rational roots have the form $\pm\tfrac{p}{q}$ where $p\mid 6$ and $q\mid 2$. Candidates: $\pm1,\pm2,\pm3,\pm6,\pm\tfrac{1}{2},\pm\tfrac{3}{2}$. Test $x=3$: $54-27-33+6=0$. \checkmark\ Divide out $(x-3)$ to get $2x^2+3x-2=(2x-1)(x+2)$. |
| B2 | `$x+1$` | polynomial algebra / factorisation | Sum of cubes: $x^3+1=(x+1)(x^2-x+1)$. Cancel $(x^2-x+1)$. Check: $x^2-x+1\neq0$ for real $x$ (discriminant $<0$). |
| B3 | `$ab=\dfrac{p^3-q}{3p}$` | polynomial algebra / factorisation | $a^3+b^3=(a+b)(a^2-ab+b^2)=(a+b)\!\left[(a+b)^2-3ab\right]=p(p^2-3ab)=q$. So $p^3-3p\cdot ab=q$, giving $ab=\dfrac{p^3-q}{3p}$. |
| B4 | `$-1$` | polynomial algebra / factorisation | Factor the numerator: $x(x+1)\!\left[x-(x+1)\right]=x(x+1)(-1)$. Cancel $x(x+1)$. Result: $-1$. Always look for a common factor in the numerator before combining fractions. |
| B5 | `$(a-b)^2(a+b)$` | polynomial algebra / factorisation | Group: $(a^3+b^3)-(a^2b+ab^2)=(a+b)(a^2-ab+b^2)-ab(a+b)=(a+b)(a^2-2ab+b^2)=(a+b)(a-b)^2$. |
| B6 | `$n^2$` | sequences & series / telescoping | $\displaystyle\sum_{r=1}^n(2r-1)=2\cdot\frac{n(n+1)}{2}-n=n(n+1)-n=n^2$. The sum of the first $n$ odd numbers is always a perfect square. Elegant! |
| B7 | `$x=-\dfrac{1}{5}$` | polynomial algebra / factorisation | Common denominator $(x+3)(x-1)$: $(2x-1)(x-1)-(x+2)(x+3)=(x+3)(x-1)$. LHS: $(2x^2-3x+1)-(x^2+5x+6)=x^2-8x-5$. RHS: $x^2+2x-3$. So $x^2-8x-5=x^2+2x-3 \Rightarrow -10x=2 \Rightarrow x=-\tfrac{1}{5}$. Check in the original: LHS $=\tfrac{-7/5}{14/5}-\tfrac{9/5}{-6/5}=-\tfrac{1}{2}+\tfrac{3}{2}=1$. \checkmark |
| B8 | `$\dfrac{ab}{a+b}$` | polynomial algebra / factorisation | Numerator: $\dfrac{b-a}{ab}$. Denominator: $\dfrac{b^2-a^2}{a^2b^2}=\dfrac{(b-a)(b+a)}{a^2b^2}$. Dividing: $\dfrac{b-a}{ab}\cdot\dfrac{a^2b^2}{(b-a)(b+a)}=\dfrac{ab}{a+b}$. |
| B9 | `Divisible by 6 for all $n\in\mathbb{Z}$.` | divisibility & number theory | $n^3-n=n(n-1)(n+1)=(n-1)n(n+1)$: the product of three consecutive integers. \emph{Divisible by 2:} among any two consecutive integers, one is even. \emph{Divisible by 3:} among any three consecutive integers, one is divisible by 3. Since $\gcd(2,3)=1$, the product is divisible by $6$. $\square$ |
| B10 | `$\alpha^3+\beta^3=4$;\quad $\alpha^4+\beta^4=7$` | surds / denesting | Vieta: $\alpha+\beta=1$, $\alpha\beta=-1$. Newton recurrence $s_n=(\alpha+\beta)s_{n-1}-\alpha\beta\cdot s_{n-2}=s_{n-1}+s_{n-2}$. $s_1=1$, $s_2=(\alpha+\beta)^2-2\alpha\beta=1+2=3$. $s_3=s_2+s_1=4$. $s_4=s_3+s_2=7$. This recurrence is the \emph{Lucas sequence} --- the roots are the golden ratio and its conjugate. |
| C1 | `$x=0$ and $x=2$` | polynomial algebra / factorisation | Let $u=3^x$: $u^2-10u+9=0 \Rightarrow (u-1)(u-9)=0$. $u=1 \Rightarrow 3^x=1 \Rightarrow x=0$. $u=9 \Rightarrow 3^x=9 \Rightarrow x=2$. |
| C2 | `$5$` | algebraic inequalities | Substitute $x=5-2y$: minimise $(5-2y)^2+y^2=5y^2-20y+25$. Complete the square: $5(y-2)^2+5$. Minimum is $\mathbf{5}$ at $y=2$, $x=1$. Alternatively (elegant): by Cauchy--Schwarz, $(x+2y)^2\leq(x^2+y^2)(1^2+2^2)$, so $x^2+y^2\geq\tfrac{25}{5}=5$. |
| C3 | `Proof: see method.` | algebraic inequalities | $2(a^2+b^2+c^2)-2(ab+bc+ca)=(a-b)^2+(b-c)^2+(c-a)^2\geq0$. Divide by 2. Equality iff $a=b=c$. $\square$ This is the most important algebraic inequality after AM--GM. |
| C4 | `$x=4$` | surds / denesting | Isolate one radical: $\sqrt{x+5}=4-\sqrt{x-3}$. Square: $x+5=16-8\sqrt{x-3}+(x-3) \Rightarrow 8\sqrt{x-3}=8 \Rightarrow x-3=1 \Rightarrow x=4$. Check: $\sqrt9+\sqrt1=3+1=4$. \checkmark |
| C5 | `Minimum is $\mathbf{0}$, at $(x,y)=(-2,\,3)$` | algebraic inequalities | Complete the square in each variable separately: $(x+2)^2-4+(y-3)^2-9+13=(x+2)^2+(y-3)^2\geq0$. Minimum is $0$ when $x=-2$, $y=3$. |
| C6 | `$23$` | polynomial algebra / factorisation | $\dfrac{x^4+1}{x^2}=x^2+\dfrac{1}{x^2}=\left(x+\dfrac{1}{x}\right)^2-2=25-2=23$. |
| C7 | `$x=\pm1$` | polynomial algebra / factorisation | Let $u=x^2$: $(u+5)(u-1)=0$. $u=-5$ gives no real solutions. $u=1 \Rightarrow x=\pm1$. |
| C8 | `$4$` | algebraic inequalities | $\dfrac{1}{a}+\dfrac{1}{b}=\dfrac{a+b}{ab}=\dfrac{1}{ab}$. By AM--GM, $ab\leq\left(\dfrac{a+b}{2}\right)^2=\dfrac{1}{4}$, so $\dfrac{1}{ab}\geq4$. Equality when $a=b=\tfrac{1}{2}$. |
| D1 | `$x=1$ and $x=-1$\quad ($x=-1$ has multiplicity 3)` | polynomial algebra / factorisation | Group into two differences: $x^4+2x^3-2x-1=(x^4-1)+2x(x^2-1)$. Both terms share the factor $x^2-1$: $(x^2-1)(x^2+1)+2x(x^2-1)=(x^2-1)(x^2+2x+1)=(x-1)(x+1)(x+1)^2=(x-1)(x+1)^3$. The only real solutions are $x=1$ and $x=-1$. |
| D2 | `Smallest counterexample: $n=40$, giving $40^2+40+41=41^2=1681=41\times41$.` | divisibility & number theory | $n=40$: $1600+40+41=1681=41^2$. Composite. $\square$ For $0\leq n\leq39$: one approach is to observe that $f(n)=n^2+n+41$ --- any factor $d$ of $f(n)$ with $d\leq 40$ would divide $f(n)-f(0)=n(n+1)$ and also $41$, forcing $d=1$ or $d=41$. Since $f(n)<41^2$ for $n<40$, the factor 41 cannot appear. |
| D3 | `Proof via AM--GM: see method.` | algebraic inequalities | By AM--GM on three positive numbers: $\dfrac{a+b+c}{3}\geq\sqrt[3]{abc}=\sqrt[3]{1}=1$. Therefore $a+b+c\geq3$. Equality iff $a=b=c=1$. $\square$ This is the AM--GM inequality in its three-variable form, with the constraint doing all the work. |
| D4 | `Proof: see method.` | surds / denesting | \textit{Part 1:} Let $t=\tfrac{a}{b}>0$. Then $t+\tfrac{1}{t}-2=\dfrac{t^2-2t+1}{t}=\dfrac{(t-1)^2}{t}\geq0$. So $\tfrac{a}{b}+\tfrac{b}{a}\geq2$, equality iff $a=b$. $\square$ \textit{Part 2:} Apply Part 1 to the positive reals $\sqrt{a}$ and $\sqrt{b}$: $\dfrac{\sqrt{a}}{\sqrt{b}}+\dfrac{\sqrt{b}}{\sqrt{a}}\geq2 \;\Rightarrow\; \dfrac{a+b}{\sqrt{ab}}\geq2 \;\Rightarrow\; \dfrac{a+b}{2}\geq\sqrt{ab}$. $\square$ |
| D5 | `$2$\quad ($n=1$ and $n=5$)` | polynomial algebra / factorisation | $n^2-1=(n+3)(n-3)+8$, so $(n+3)\mid(n^2-1)$ iff $(n+3)\mid8$. Since $n\geq1$, we need $n+3\geq4$, and the only divisors of 8 that are $\geq4$ are 4 and 8, giving $n=1$ and $n=5$. Exactly \textbf{2} values in range. |


#### Sheet 04

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$39{,}999$` | polynomial algebra / factorisation | $(200+1)(200-1)=200^2-1=40000-1=39999$. DOTS with $a=200$. |
| A2 | `$(x-7)(x+6)$` | polynomial algebra / factorisation | Seek integers with product $-42$ and sum $-1$: that's $-7$ and $+6$. |
| A3 | `$1$` | polynomial algebra / factorisation | Substitute: $1-1+1-1+1=1$. Alternatively, an odd number of terms of $1+(-1)+\ldots$ always gives 1 when the last term is $+1$. |
| A4 | `$90$` | polynomial algebra / factorisation | $p^3+q^3=(p+q)[(p+q)^2-3pq]=6[36-21]=6\times15=90$. |
| A5 | `$0$` | functions | $f(1)=1+2-3=0$. By the Remainder Theorem the remainder is $f(1)=0$, so $(x-1)$ is a factor. |
| A6 | `$2x(x-3)(x+3)$` | polynomial algebra / factorisation | Factor out $2x$: $2x(x^2-9)=2x(x-3)(x+3)$. Extract scalars and common factors \emph{first}, always. |
| A7 | `$\dfrac{8}{3}$` | polynomial algebra / factorisation | Factor out $3^{n-1}$: $\dfrac{3^{n-1}(9-1)}{3^n}=\dfrac{8}{3}$. Always pull out the lowest power. |
| A8 | `$ab=10$` | polynomial algebra / factorisation | $(a-b)^2=a^2-2ab+b^2=9$, so $29-2ab=9$, giving $ab=10$. |
| A9 | `$(x^2+1)(x+1)(x-1)$` | polynomial algebra / factorisation | Two applications of DOTS: $(x^2+1)(x^2-1)=(x^2+1)(x+1)(x-1)$. The factor $x^2+1$ is irreducible over $\mathbb{R}$. |
| A10 | `$n(n-1)$` | polynomial algebra / factorisation | $\dfrac{n!}{(n-2)!}=n\cdot(n-1)\cdot\frac{(n-2)!}{(n-2)!}=n(n-1)$. |
| B1 | `$x^4+x^3+x^2+x+1$` | sequences & series / telescoping | $x^5-1=(x-1)(x^4+x^3+x^2+x+1)$. This is the finite geometric series: $1+x+\cdots+x^{n-1}=\frac{x^n-1}{x-1}$ with $n=5$. |
| B2 | `Remainder at $(x-1)$: $g(1)=1-3+2=0$. \quad Remainder at $(x+1)$: $g(-1)=1+3+2=6$.` | functions | Remainder Theorem: evaluate $g$ at the root of each linear factor. No division needed. |
| B3 | `$\dfrac{ab^2}{a^2-b^2}$` | polynomial algebra / factorisation | Common denominator $(a-b)(a+b)$: numerator is $ab(a+b)-a^2b=ab\left[(a+b)-a\right]=ab^2$. Result: $\dfrac{ab^2}{a^2-b^2}$. Factor the shared $ab$ out of the numerator before expanding anything. |
| B4 | `$(x-y)(x+y)(x^2+xy+y^2)(x^2-xy+y^2)$` | polynomial algebra / factorisation | Two routes then combined: $x^6-y^6=(x^3-y^3)(x^3+y^3)$, then sum/difference of cubes on each factor. Alternatively $(x^2)^3-(y^2)^3$ first, then DOTS on each. |
| B5 | `$\dfrac{5}{2}$` | Vieta's formulas & symmetric polynomials | $\frac{1}{\alpha}+\frac{1}{\beta}=\frac{\alpha+\beta}{\alpha\beta}=\frac{-5/3}{-2/3}=\frac{5}{2}$. |
| B6 | `$\dfrac{(x-1)(x+1)^2}{x}$` | polynomial algebra / factorisation | $\frac{x^2-1}{x^2}\cdot x(x+1)=\frac{(x-1)(x+1)}{x^2}\cdot x(x+1)=\frac{(x-1)(x+1)^2}{x}$. |
| B7 | `$13$` | polynomial algebra / factorisation | $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)\Rightarrow 25=a^2+b^2+c^2+12\Rightarrow a^2+b^2+c^2=13$. |
| B8 | `$y=\dfrac{3x+1}{x-2}$` | polynomial algebra / factorisation | $2y+1=x(y-3)=xy-3x\Rightarrow 2y-xy=-3x-1\Rightarrow y(2-x)=-(3x+1)\Rightarrow y=\dfrac{3x+1}{x-2}$. |
| B9 | `For $n\geq2$: $2n-1\geq3$ and $2n+1\geq5$, both greater than 1, so $4n^2-1$ is a product of two integers each $>1$. Hence composite.` | divisibility & number theory | The key is that $(2n-1)$ and $(2n+1)$ are \emph{both} greater than 1 for $n\geq2$. For $n=1$: $4-1=3$ which is prime, confirming the bound $n\geq2$ is tight. |
| B10 | `$x^2-12=0$` | Vieta's formulas & symmetric polynomials | Sum $=(\alpha+\beta)-\left(\frac{1}{\alpha}+\frac{1}{\beta}\right)=4-\frac{\alpha+\beta}{\alpha\beta}=4-4=0$. Product $=(\alpha-\frac{1}{\alpha})(\beta-\frac{1}{\beta})=\alpha\beta-\frac{\alpha}{\beta}-\frac{\beta}{\alpha}+\frac{1}{\alpha\beta}=1-\frac{\alpha^2+\beta^2}{\alpha\beta}+1=2-(16-2)=-12$. Quadratic: $x^2-0\cdot x+(-12)=x^2-12$. |
| C1 | `$x=0$ and $x=2$` | polynomial algebra / factorisation | Let $u=2^x$: $u^2-5u+4=(u-1)(u-4)=0$. $u=1\Rightarrow x=0$; $u=4\Rightarrow x=2$. |
| C2 | `$t^3-3t$` | polynomial algebra / factorisation | $x^2+\frac{1}{x^2}=t^2-2$. Then $x^3+\frac{1}{x^3}=\left(x+\frac{1}{x}\right)\!\!\left(x^2-1+\frac{1}{x^2}\right)=t(t^2-3)=t^3-3t$. |
| C3 | `Minimum is $18$ at $x=3$.` | algebraic inequalities | AM--GM: $3x+\frac{27}{x}\geq2\sqrt{3x\cdot\frac{27}{x}}=2\sqrt{81}=18$. Equality when $3x=\frac{27}{x}\Rightarrow x^2=9\Rightarrow x=3$. |
| C4 | `$x=12-4\sqrt{7}$\; (one real solution)` | surds / denesting | Isolate $\sqrt{2x-1}=2-\sqrt{x-1}$, requiring $2\geq\sqrt{x-1}$, i.e.\ $x\leq5$. Square: $2x-1=4-4\sqrt{x-1}+(x-1)$, so $x-4=-4\sqrt{x-1}$, requiring $x\leq4$. Square again: $(x-4)^2=16(x-1)\Rightarrow x^2-24x+32=0\Rightarrow x=12\pm4\sqrt{7}$. Since $x\leq4$: $x=12-4\sqrt{7}\approx1.42$. |
| C5 | `$k=16$` | polynomial algebra / factorisation | Pair: $(x+1)(x+7)=x^2+8x+7$ and $(x+3)(x+5)=x^2+8x+15$. Let $u=x^2+8x+11$: product $=(u-4)(u+4)=u^2-16$. This is a perfect square $u^2$ when $k=16$. |
| C6 | `Equality iff $ad=bc$.` | algebraic inequalities | $(a^2+b^2)(c^2+d^2)-(ac+bd)^2=a^2d^2-2abcd+b^2c^2=(ad-bc)^2\geq0$. $\square$ This is the Cauchy--Schwarz inequality in two dimensions. |
| C7 | `$\dfrac{u^4+v^4+6u^2v^2}{8}$` | polynomial algebra / factorisation | $x=\frac{u+v}{2}$, $y=\frac{u-v}{2}$. $x^4+y^4=\frac{1}{16}\!\left[(u+v)^4+(u-v)^4\right]=\frac{1}{16}\cdot2(u^4+6u^2v^2+v^4)=\frac{u^4+6u^2v^2+v^4}{8}$. |
| C8 | `$x=\pm2,\;\pm\sqrt{3}$` | surds / denesting | Let $u=x^2$: $(u-3)(u-4)=0$. $u=3\Rightarrow x=\pm\sqrt{3}$; $u=4\Rightarrow x=\pm2$. |
| D1 | `Proved below.` | polynomial algebra / factorisation | Every integer is even ($n=2m$) or odd ($n=2m+1$). \emph{Even:} $n^2=4m^2\equiv0$. \emph{Odd:} $n^2=4m^2+4m+1\equiv1$. So $n^2\equiv0$ or $1$, hence $n^2+2\equiv2$ or $3\pmod4$. Neither is $\equiv0$, so $4\nmid(n^2+2)$. $\square$ |
| D2 | `$x=1$ (double) and $x=1\pm\sqrt{2}$` | surds / denesting | Try $(x^2+ax+b)(x^2+cx+d)$ with $b+d+ac=4$, $bd=-1$, $a+c=-4$, $ad+bc=0$. Taking $b=1$, $d=-1$: $a=c=-2$ works. So $(x^2-2x+1)(x^2-2x-1)=0$, giving $(x-1)^2=0\Rightarrow x=1$ and $x^2-2x-1=0\Rightarrow x=1\pm\sqrt2$. |
| D3 | `$a_n=\dfrac{1}{2^n-1}$;\quad $a_{100}=\dfrac{1}{2^{100}-1}$` | polynomial algebra / factorisation | Let $b_n=\frac{1}{a_n}$: $b_{n+1}=\frac{a_n+2}{a_n}=1+\frac{2}{a_n}=1+2b_n$. This linear recurrence has homogeneous solution $C\cdot2^n$ and particular solution $-1$, giving $b_n=C\cdot2^n-1$. With $b_1=1$: $C=1$. So $b_n=2^n-1$ and $a_n=\frac{1}{2^n-1}$. |
| D4 | `$\dfrac{n+1}{2n}$;\quad limit $= \dfrac{1}{2}$` | sequences & series / telescoping | $1-\frac{1}{k^2}=\frac{(k-1)(k+1)}{k^2}$. Product $=\dfrac{\prod(k-1)}{\prod k}\cdot\dfrac{\prod(k+1)}{\prod k}=\frac{1}{n}\cdot\frac{n+1}{2}=\frac{n+1}{2n}$. Each factor telescopes separately: $\prod_{k=2}^n\frac{k-1}{k}=\frac{1}{n}$ and $\prod_{k=2}^n\frac{k+1}{k}=\frac{n+1}{2}$. |
| D5 | `$7752$` | polynomial algebra / factorisation | Define $q(x)=p(x)-10x$. Then $q(1)=q(2)=q(3)=q(4)=0$. Since $p$ is monic of degree 4: $q(x)=(x-1)(x-2)(x-3)(x-4)$. $p(0)=q(0)=(-1)(-2)(-3)(-4)=24$. $p(12)=q(12)+120=(11)(10)(9)(8)+120=7920+120=8040$. $p(12)-12p(0)=8040-288=7752$. |


#### Sheet 05

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$\dfrac{x-3}{x+2}$` | polynomial algebra / factorisation | $(x-3)(x+3)/[(x+2)(x+3)]$. Cancel $(x+3)$. Undefined at $x=-3$ and $x=-2$. |
| A2 | `$\sqrt7+\sqrt3$` | surds / denesting | Multiply by $\frac{\sqrt7+\sqrt3}{\sqrt7+\sqrt3}$: denominator $=7-3=4$. Cancel the 4. |
| A3 | `$25$` | polynomial algebra / factorisation | $(x-y)^2=(x+y)^2-4xy=9+16=25$. |
| A4 | `$(x-1)(x-2)(x+2)$` | polynomial algebra / factorisation | Group: $x^2(x-1)-4(x-1)=(x-1)(x^2-4)=(x-1)(x-2)(x+2)$. |
| A5 | `$6$` | polynomial algebra / factorisation | $\binom{4}{2}=6$. |
| A6 | `$x^2+3x-10=0$` | Vieta's formulas & symmetric polynomials | $x^2-(\alpha+\beta)x+\alpha\beta=x^2-(-3)x+(-10)=x^2+3x-10$. |
| A7 | `$4\sqrt{2}$` | surds / denesting | $5\sqrt2-3\sqrt2+2\sqrt2=4\sqrt2$. |
| A8 | `$133$` | polynomial algebra / factorisation | $ab=\frac{(a+b)^2-(a^2+b^2)}{2}=\frac{49-29}{2}=10$. Then $a^3+b^3=7(29-10)=7\times19=133$. |
| A9 | `$x=5$ or $x=-2$` | polynomial algebra / factorisation | $2x-3=7\Rightarrow x=5$; $2x-3=-7\Rightarrow x=-2$. Draw the $V$-shape: $y=\|2x-3\|$ meets $y=7$ at two points. |
| A10 | `$16$` | algebraic inequalities | $\frac{(x+4)^2}{x}=x+8+\frac{16}{x}\geq2\sqrt{16}+8=16$ by AM--GM on $x+\frac{16}{x}\geq8$. Equality at $x=4$. |
| B1 | `$\dfrac{4/3}{x+1}+\dfrac{11/3}{x-2}$, or $\dfrac{4}{3(x+1)}+\dfrac{11}{3(x-2)}$` | polynomial algebra / factorisation | $5x+1=A(x-2)+B(x+1)$. $x=2$: $11=3B\Rightarrow B=\frac{11}{3}$. $x=-1$: $-4=-3A\Rightarrow A=\frac{4}{3}$. |
| B2 | `$\dfrac{1}{x}-\dfrac{x}{x^2+3}$` | polynomial algebra / factorisation | $3=A(x^2+3)+(Bx+C)x$. $x=0$: $3=3A\Rightarrow A=1$. Coefficient of $x^2$: $0=A+B\Rightarrow B=-1$. Coefficient of $x$: $0=C$. Result: $\frac{1}{x}-\frac{x}{x^2+3}$. |
| B3 | `$3$` | surds / denesting | Rationalise: $\frac{\sqrt{n+1}-\sqrt{n}}{(n+1)-n}=\sqrt{n+1}-\sqrt{n}$. The sum telescopes: $(\sqrt{1}-\sqrt{0})+(\sqrt{2}-\sqrt{1})+\cdots+(\sqrt{9}-\sqrt{8})=\sqrt{9}-\sqrt{0}=3$. |
| B4 | `$(a^2+a+1)(a^2-a+1)$` | polynomial algebra / factorisation | Add and subtract $a^2$: $a^4+2a^2+1-a^2=(a^2+1)^2-a^2=(a^2+a+1)(a^2-a+1)$. |
| B5 | `$(s^2-4p)^2$` | polynomial algebra / factorisation | $(a-b)^2=(a+b)^2-4ab=s^2-4p$. Then $(a-b)^4=[(a-b)^2]^2=(s^2-4p)^2$. |
| B6 | `$1$` | polynomial algebra / factorisation | Factor everything: $\frac{(x-1)^2}{(x-1)(x+3)}\cdot\frac{(x+1)(x+3)}{(x-1)(x+1)}=\frac{x-1}{x+3}\cdot\frac{x+3}{x-1}=1$. |
| B7 | `$x^2-(p^2-2q)x+q^2=0$` | Vieta's formulas & symmetric polynomials | $r^2+s^2=(r+s)^2-2rs=p^2-2q$. $(rs)^2=q^2$. Quadratic: $x^2-(p^2-2q)x+q^2=0$. |
| B8 | `$x=2,\;y=3$` | polynomial algebra / factorisation | Let $u=\frac{1}{x}$, $v=\frac{1}{y}$: $u+v=\frac{5}{6}$, $u-v=\frac{1}{6}$. Adding: $2u=1\Rightarrow u=\frac{1}{2}$, $v=\frac{1}{3}$. |
| B9 | `Proof by partial fractions, then telescoping.` | sequences & series / telescoping | PF: $\frac{1}{(2k-1)(2k+1)}=\frac{A}{2k-1}+\frac{B}{2k+1}$. Solving: $A=\frac{1}{2}$, $B=-\frac{1}{2}$. Sum telescopes: $\frac{1}{2}\!\left(1-\frac{1}{2n+1}\right)=\frac{n}{2n+1}$. $\square$ |
| B10 | `$a+d=0$ (equivalently $d=-a$)` | functions | Compute $f(f(x))=\frac{a\cdot f(x)+b}{c\cdot f(x)+d}=\frac{(a^2+bc)x+(a+d)b}{(a+d)cx+(bc+d^2)}$. For this to equal $x$: need $a^2+bc=bc+d^2$ (i.e.\ $a^2=d^2$) and $(a+d)b=0$ and $(a+d)c=0$. If $a=-d$, all conditions hold automatically. |
| C1 | `$x-\dfrac{1}{x}=8$ (giving $x=4\pm\sqrt{17}$) or $x-\dfrac{1}{x}=-1$ (giving $x=\frac{-1\pm\sqrt5}{2}$)` | surds / denesting | Let $u=x-\frac{1}{x}$, so $x^2+\frac{1}{x^2}=u^2+2$. Then $(u^2+2)-7u-10=0\Rightarrow u^2-7u-8=0\Rightarrow(u-8)(u+1)=0$. $u=8$: $x^2-8x-1=0\Rightarrow x=4\pm\sqrt{17}$. $u=-1$: $x^2+x-1=0\Rightarrow x=\frac{-1\pm\sqrt5}{2}$. |
| C2 | `Proved below.` | algebraic inequalities | Titu: $\frac{a^2}{b}+\frac{b^2}{c}+\frac{c^2}{a}\geq\frac{(a+b+c)^2}{b+c+a}=\frac{9}{3}=3$. $\square$ Equality iff $\frac{a}{b}=\frac{b}{c}=\frac{c}{a}$, i.e.\ $a=b=c=1$. |
| C3 | `$(x,y)=(2\sqrt2,\;\sqrt2)$ and $(-2\sqrt2,\;-\sqrt2)$` | surds / denesting | Factor both left sides: $x(x+y)=12$ and $y(x+y)=6$. Neither $y$ nor $x+y$ can be zero (each would force $0=6$ or $0=12$), so divide: $\frac{x}{y}=2$, giving $x=2y$. Substitute into $xy+y^2=6$: $2y^2+y^2=6\Rightarrow y^2=2\Rightarrow y=\pm\sqrt2$, with $x=2y$ matching the sign. Check: $8+4=12$ \checkmark, $4+2=6$ \checkmark. |
| C4 | `$-1<k<4$ and $k\neq0$` | Vieta's formulas & symmetric polynomials | For a quadratic ($k\neq0$): discriminant $=16-4k(k-3)=16-4k^2+12k>0\Rightarrow4k^2-12k-16<0\Rightarrow k^2-3k-4<0\Rightarrow(k-4)(k+1)<0$. So $-1<k<4$. (Exclude $k=0$ since that makes it linear, not quadratic.) |
| C5 | `$2\sqrt2$` | surds / denesting | $3+2\sqrt2=(\sqrt2+1)^2$, so $\sqrt{3+2\sqrt2}=\sqrt2+1$. Similarly $3-2\sqrt2=(\sqrt2-1)^2\Rightarrow\sqrt{3-2\sqrt2}=\sqrt2-1$. Sum $=2\sqrt2$. |
| C6 | `$\sqrt{x}-\dfrac{1}{\sqrt{x}}=\sqrt{2\sqrt5-2}$.` | surds / denesting | Square the given relation: $(x-\frac1x)^2=16\Rightarrow x+\frac1x=2\sqrt5$ (positive since $x>0$). Let $t=\sqrt{x}-\frac1{\sqrt{x}}$. Then $t^2=x+\frac1x-2=2\sqrt5-2$, so $t=\sqrt{2\sqrt5-2}$ (positive branch). |
| C7 | `$(a-1)(b-1)=1$ always;\quad minimum of $a+b$ is $4$, at $a=b=2$.` | algebraic inequalities | From $\frac{1}{a}+\frac{1}{b}=1$: $a+b=ab$. $(a-1)(b-1)=ab-a-b+1=(a+b)-(a+b)+1=1$. $\square$ For minimum of $a+b=ab$: AM--GM gives $ab\leq\left(\frac{a+b}{2}\right)^2$, so $a+b\leq\frac{(a+b)^2}{4}$, giving $a+b\geq4$, with equality at $a=b=2$. |
| C8 | `$x=0,\;x=-1,\;x=\dfrac{3\pm\sqrt{17}}{2}$` | surds / denesting | $A^2=B^2\Leftrightarrow(A-B)(A+B)=0$. $A-B=x^2-3x-2$ and $A+B=x^2+x=x(x+1)$. $x(x+1)=0$: $x=0$ or $x=-1$. $x^2-3x-2=0$: $x=\frac{3\pm\sqrt{17}}{2}$. Four real solutions in total. |
| D1 | `$f(x)=\dfrac{x^3-x+1}{2x(x-1)}$` | functions | Let the substitution $\phi(x)=\frac{1}{1-x}$. Note $\phi(\phi(x))=\phi\!\left(\frac{1}{1-x}\right)=\frac{1}{1-\frac{1}{1-x}}=\frac{1-x}{-x}=\frac{x-1}{x}$ and $\phi^3(x)=x$ (three-cycle). So the three equations are: $f(x)+f\!\left(\frac{1}{1-x}\right)=x$ \quad(i) $f\!\left(\frac{1}{1-x}\right)+f\!\left(\frac{x-1}{x}\right)=\frac{1}{1-x}$ \quad(ii) $f\!\left(\frac{x-1}{x}\right)+f(x)=\frac{x-1}{x}$ \quad(iii) Add all three and divide by 2: $f(x)+f\!\left(\frac{1}{1-x}\right)+f\!\left(\frac{x-1}{x}\right)=\frac{1}{2}\!\left(x+\frac{1}{1-x}+\frac{x-1}{x}\right)$. Then subtract (ii): $f(x)=\frac{1}{2}\!\left(x+\frac{1}{1-x}+\frac{x-1}{x}\right)-\frac{1}{1-x}=\frac{1}{2}\!\left(x-\frac{1}{1-x}+\frac{x-1}{x}\right)=\frac{x^3-x+1}{2x(x-1)}$. Check at $x=2$: $f(2)+f(-1)=\frac{7}{4}+\frac{1}{4}=2$. \checkmark |
| D2 | `Minimum is $9$ at $x=\frac{1}{3}$.` | algebraic inequalities | \textit{Proof:} By standard C--S: $\left(\sum\frac{a_i^2}{b_i}\right)\!\left(\sum b_i\right)\geq\left(\sum a_i\right)^2$, giving $\sum\frac{a_i^2}{b_i}\geq\frac{(\sum a_i)^2}{\sum b_i}$. Apply with $a_1=1$, $b_1=x$, $a_2=2$, $b_2=1-x$: $\frac{1}{x}+\frac{4}{1-x}\geq\frac{(1+2)^2}{x+(1-x)}=9$. Equality when $\frac{1/1}{x/(1)}=\frac{2/(1)}{(1-x)/1}$, i.e.\ $\frac{1}{x}=\frac{2}{1-x}\Rightarrow x=\frac{1}{3}$. |
| D3 | `$f(x)=3x$ for $x\in\mathbb{Q}$; with continuity assumption, $f(x)=3x$ for all $x\in\mathbb{R}$.` | logarithms | $f(n)=3n$ for $n\in\mathbb{Z}$ (by induction). $f(p/q)=3(p/q)$ for $p/q\in\mathbb{Q}$ (from $q\cdot f(p/q)=f(p)=3p$). Without continuity or monotonicity, pathological solutions exist on $\mathbb{R}$ (via Hamel basis). With any regularity assumption: $f(x)=3x$. |
| D4 | `Proved below.` | polynomial algebra / factorisation | Every integer has residue $0,1,2,$ or $3\pmod4$ (four classes). By the Pigeonhole Principle, among 5 integers, at least two share the same residue. Their difference $\equiv0\pmod4$. $\square$ For the second part: $a\equiv b\pmod4\Rightarrow a^2-b^2=(a-b)(a+b)$. Since $4\mid(a-b)$, we have $4\mid(a^2-b^2)$, i.e.\ $a^2\equiv b^2\pmod4$. |
| D5 | `$(x,y)=(\pm507,\pm505),\;(\pm255,\pm251),\;(\pm57,\pm35),\;(\pm45,\pm1)$ --- all sign combinations, 16 solutions in total.` | polynomial algebra / factorisation | $(x-y)(x+y)=2024=2^3\times11\times23$. Write $x-y=a$, $x+y=b$ where $ab=2024$ and $a,b$ have the same parity (both even, since $2024$ is even). Set $a=2s$, $b=2t$: $4st=2024\Rightarrow st=506=2\times11\times23$. Factor pairs of 506 (both positive, $s\leq t$): $(1,506),(2,253),(11,46),(22,23)$. Each gives $x=s+t$, $y=t-s$. Include negative values of $x,y$. |


#### Sheet 06

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$x(x+2)(x+3)$` | polynomial algebra / factorisation | Factor out $x$: $x(x^2+5x+6)=x(x+2)(x+3)$. Always extract common factors before any other step. |
| A2 | `$3$` | surds / denesting | $\left(x+\frac{1}{x}\right)^2=x^2+2+\frac{1}{x^2}=5$, so $x^2+\frac{1}{x^2}=3$. |
| A3 | `$3$` | polynomial algebra / factorisation | $\binom{3}{1}=3$ (choosing 1 factor to contribute $x$, the rest give $y$). |
| A4 | `$2$` | surds / denesting | Rationalise both fractions: $\frac{\sqrt2+1}{(\sqrt2-1)(\sqrt2+1)} - \frac{\sqrt2-1}{(\sqrt2+1)(\sqrt2-1)} = (\sqrt2+1) - (\sqrt2-1) = 2$. |
| A5 | `$a=-12,\;b=16$` | divisibility & number theory | $(x-2)^2$ divides $f(x)$, so $f(x)=(x-2)^2(x-r)$ for some $r$. Expanding: $x^3-(r+4)x^2+(4r+4)x-4r$. Matching $f(x)=x^3+ax+b$ (no $x^2$ term): $r+4=0\Rightarrow r=-4$. Then $a=4(-4)+4=-12$ and $b=-4(-4)=16$. |
| A6 | `$\dfrac{2x}{y}$` | polynomial algebra / factorisation | $\frac{8x^3}{y^3}\div\frac{4x^2}{y^2}=\frac{8x^3}{y^3}\cdot\frac{y^2}{4x^2}=\frac{2x}{y}$. |
| A7 | `$30$` | polynomial algebra / factorisation | $\alpha^2\beta+\alpha\beta^2=\alpha\beta(\alpha+\beta)=6\times5=30$. |
| A8 | `$(2a-b)^2$` | polynomial algebra / factorisation | Perfect square trinomial with $(\alpha-\beta)^2$ form: $\alpha=2a$, $\beta=b$. |
| A9 | `$3\times 11\times 31$` | integer arithmetic | $2^{10}-1=1023=(2^5-1)(2^5+1)=31\times33=31\times3\times11$. |
| A10 | `$0$` | functions | $f(0) = 0^2-3(0)+2 = 2$. Then $f(f(0)) = f(2) = 2^2-3(2)+2 = 0$. |
| B1 | `$A=1,\;B=1,\;C=3$` | polynomial algebra / factorisation | Expand the right: $A(x^2+2x+1)+B(x+1)+C=Ax^2+(2A+B)x+(A+B+C)$. Compare: $A=1$, $2A+B=3\Rightarrow B=1$, $A+B+C=5\Rightarrow C=3$. Alternatively substitute $x=-1$: $C=1-3+5=3$. |
| B2 | `$a=\frac{11}{3},\;b=-3,\;c=-\frac{5}{3}$` | Vieta's formulas & symmetric polynomials | From $p(1)=0$: $a+b+c=-1$. From $p(-1)=4$: $a-b+c=5$. Subtracting gives $b=-3$, then $a+c=2$. Now $p(2)=15$ gives $8+4a+2b+c=15\Rightarrow4a+c=13$. Subtract $a+c=2$: $3a=11$, so $a=\frac{11}{3}$ and $c=-\frac{5}{3}$. So the coefficients are rational, not integers. |
| B3 | `$x-2$` | polynomial algebra / factorisation | Difference of cubes: $x^3-8=(x-2)(x^2+2x+4)$. Cancel $(x^2+2x+4)$. |
| B4 | `At $a=b=c=1$: LHS $=3-3=0$; RHS $=3(3-3)=0$. \checkmark` | polynomial algebra / factorisation | The factor $(a+b+c)$ on the RHS makes it obvious that if $a+b+c=0$, the expression vanishes, so $a^3+b^3+c^3=3abc$. The identity is proved by expanding the RHS. |
| B5 | `$3$` | polynomial algebra / factorisation | Since $a+b+c=0$, by the identity above: $a^3+b^3+c^3=3abc$. So the ratio is 3. |
| B6 | `$\sum_{k=1}^{10}(2k-1)^2=1330$` | sequences & series / telescoping | $\sum(2k-1)^2=\sum(4k^2-4k+1)=4\cdot\frac{10\cdot11\cdot21}{6}-4\cdot\frac{10\cdot11}{2}+10=1540-220+10=1330$. |
| B7 | `$\dfrac{-b}{a}$` | polynomial algebra / factorisation | Numerator: $\frac{(a-b)-(a+b)}{(a+b)(a-b)}=\frac{-2b}{a^2-b^2}$. Denominator: $\frac{2a}{a^2-b^2}$. Ratio: $\frac{-2b}{2a}=-\frac{b}{a}$. |
| B8 | `$b=\dfrac{ad}{c}$` | polynomial algebra / factorisation | Cross-multiply: $(a-b)(c+d)=(c-d)(a+b)$. Expand: $ac+ad-bc-bd=ac+bc-ad-bd$. Simplify: $2ad=2bc\Rightarrow ad=bc\Rightarrow b=\frac{ad}{c}$. |
| B9 | `$\alpha^2+\beta^2+\gamma^2=14$;\quad $\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2=49$` | sequences & series / telescoping | Vieta: $\alpha+\beta+\gamma=0$, $\alpha\beta+\beta\gamma+\gamma\alpha=-7$, $\alpha\beta\gamma=-6$. $\alpha^2+\beta^2+\gamma^2=(\sum\alpha)^2-2\sum\alpha\beta=0-2(-7)=14$. $(\alpha\beta+\beta\gamma+\gamma\alpha)^2=\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2+2\alpha\beta\gamma(\alpha+\beta+\gamma)=\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2+0$. So $\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2=(-7)^2=49$. |
| B10 | `No solution (the only candidate $x=1$ is excluded from the domain).` | polynomial algebra / factorisation | Multiply by $(x-1)(x+1)$: $2(x+1) - (x^2-1)/(x-1) = 3(x-1)$? No, $(x^2-1)$ is the common denominator. So $2 - (x+1) = 3(x-1) \Rightarrow 1-x = 3x-3 \Rightarrow 4x=4 \Rightarrow x=1$. But $x=1$ makes the original denominators zero, so it is extraneous. |
| C1 | `$x=9$` | surds / denesting | Let $t=\sqrt{x}>0$: $t-\frac{6}{t}=1\Rightarrow t^2-t-6=0\Rightarrow(t-3)(t+2)=0$. Since $t>0$: $t=3$, so $x=9$. |
| C2 | `Minimum is $7$, at $(x,y)=(3,-2)$.` | algebraic inequalities | $(x^2-6x+9)+(y^2+4y+4)+20-9-4=(x-3)^2+(y+2)^2+7\geq7$. Equality at $x=3$, $y=-2$. |
| C3 | `Counterexample: $a=b=1$: $2\geq\frac{1}{2}(16)=8$? False. Correct inequality: $(a^2-b^2)^2\geq0\Rightarrow a^4+b^4\geq2a^2b^2\Rightarrow2(a^4+b^4)\geq(a^2+b^2)^2$.` | algebraic inequalities | $\frac{1}{2}(a+b)^4=\frac{1}{2}(a^4+4a^3b+6a^2b^2+4ab^3+b^4)$. At $a=b=1$: $\frac{1}{2}(16)=8>2=a^4+b^4$. So the claimed inequality is false. Correct: $(a^2-b^2)^2\geq0$ gives $a^4-2a^2b^2+b^4\geq0$, so $a^4+b^4\geq2a^2b^2$, hence $2(a^4+b^4)\geq a^4+2a^2b^2+b^4=(a^2+b^2)^2$. |
| C4 | `$x=2$ (double root) and $x=-1$ (double root)` | divisibility & number theory | Try $x=2$: $16-16-12+8+4=0$. \checkmark So $(x-2)^2$ divides the polynomial. Divide: $x^4-2x^3-3x^2+4x+4=(x-2)^2(x^2+2x+1)$. So $(x-2)^2(x+1)^2=0$: $x=2$ or $x=-1$ (each a double root). |
| C5 | `Proved below.` | algebraic inequalities | $(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)=1$. Also $a^2+b^2+c^2\geq\frac{(a+b+c)^2}{3}=\frac{1}{3}$ (by C--S or AM inequality). So $2(ab+bc+ca)=1-(a^2+b^2+c^2)\leq1-\frac{1}{3}=\frac{2}{3}$, giving $ab+bc+ca\leq\frac{1}{3}$. $\square$ Equality iff $a=b=c=\frac{1}{3}$. |
| C6 | `$\dfrac{1}{4}$` | algebraic inequalities | $x^2y+xy^2=xy(x+y)=xy$. By AM--GM: $xy\leq\left(\frac{x+y}{2}\right)^2=\frac{1}{4}$. Equality at $x=y=\frac{1}{2}$. |
| C7 | `$x=5$ only` | surds / denesting | Isolate $\sqrt{3x+1}=1+\sqrt{x+4}$ and square: $3x+1=x+5+2\sqrt{x+4}\Rightarrow x-2=\sqrt{x+4}$. Hence $x\ge2$. Square again: $(x-2)^2=x+4\Rightarrow x^2-5x=0\Rightarrow x=0$ or $x=5$. Domain $x\ge2$ leaves $x=5$. Check: $\sqrt{16}-\sqrt9=1$. |
| C8 | `$b=c$` | Vieta's formulas & symmetric polynomials | For both quadratics to have the exact same roots, all corresponding coefficients must be equal (since both are monic). Therefore $b=c$. |
| D1 | `Proved below.` | algebraic inequalities | WLOG $a\geq b\geq c\geq0$. Group as $(a-b)[a^2(a-c) - b^2(b-c)] + c^2(c-a)(c-b)$. Since $c\geq0$, $(c-a)\leq0$ and $(c-b)\leq0$, so the second term is $\geq0$. For the first term, since $a\geq b\geq c\geq 0$, we have $a-c \geq b-c \geq 0$ and $a^2 \geq b^2$, so $a^2(a-c) \geq b^2(b-c)$. Thus the bracket is $\geq 0$, and $(a-b)\geq 0$. The sum is $\geq 0$. |
| D2 | `$p(x)=0$ and $p(x)=x^n$ for non-negative integers $n$.` | Vieta's formulas & symmetric polynomials | Suppose $p$ has degree $d$. Then $p(x^2)$ has degree $2d$ and $p(x)^2$ has degree $2d$: consistent. If $r$ is a root of $p$, then $p(r^2)=p(r)^2=0$, so $r^2$ is also a root. The sequence $r,r^2,r^4,\ldots$ must terminate (finitely many roots), so $r=0$ or $r=1$ or $r=-1$. If $r=-1$: $r^2=1$ is a root, and $1^2=1$, so $p(1)=p(1)^2\Rightarrow p(1)=0$ or $1$. Careful analysis gives only monomials $p(x)=x^n$ and the zero polynomial. |
| D3 | `$\dfrac{n(n+1)}{2(2n+1)}$` | sequences & series / telescoping | $\frac{k^2}{(2k-1)(2k+1)}=\frac{1}{4}\cdot\frac{4k^2}{(2k-1)(2k+1)}=\frac{1}{4}\cdot\frac{(2k-1)(2k+1)+1}{(2k-1)(2k+1)}=\frac{1}{4}\!\left(1+\frac{1}{(2k-1)(2k+1)}\right)$. Sum $=\frac{n}{4}+\frac{1}{4}\sum_{k=1}^n\frac{1}{(2k-1)(2k+1)}=\frac{n}{4}+\frac{1}{4}\cdot\frac{n}{2n+1}=\frac{n}{4}\cdot\frac{2n+2}{2n+1}=\frac{n(n+1)}{2(2n+1)}$. |
| D4 | `$p(5)=0$` | Vieta's formulas & symmetric polynomials | Consider $q(x)=xp(x)-1$. Then $q(n)=n\cdot\frac1n-1=0$ for $n=1,2,3,4$, so $q$ is a quartic with roots $1,2,3,4$: $q(x)=c(x-1)(x-2)(x-3)(x-4)$. At $x=0$: $q(0)=-1=24c$, so $c=-\frac1{24}$. Hence $q(5)=-\frac1{24}(4)(3)(2)(1)=-1$. But $q(5)=5p(5)-1$, so $5p(5)-1=-1$, giving $p(5)=0$. |
| D5 | `$(m,n)\in\{(53,52),\;(19,16),\;(13,8),\;(11,4)\}$` | polynomial algebra / factorisation | $(m-n)(m+n)=105=3\times5\times7$. Set $m-n=a$, $m+n=b$: $ab=105$, $b>a>0$, same parity (both odd since $105$ is odd and $a,b$ have same parity). Factor pairs of 105 with $a<b$, both odd: $(1,105),(3,35),(5,21),(7,15)$. Each gives $m=\frac{a+b}{2}$, $n=\frac{b-a}{2}$: $(1,105)\to(53,52)$; $(3,35)\to(19,16)$; $(5,21)\to(13,8)$; $(7,15)\to(11,4)$. |


#### Sheet 07

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$x(x-1)(x+1)(x^2+1)$` | polynomial algebra / factorisation | $x(x^4-1)=x(x^2-1)(x^2+1)=x(x-1)(x+1)(x^2+1)$. |
| A2 | `$8$` | polynomial algebra / factorisation | $(a+b+c)^2-(a^2+b^2+c^2)=2(ab+bc+ca)=8$. |
| A3 | `$32$` | integer arithmetic | Use $(a^2-b^2)=(a-b)(a+b)$: $(7^2-5^2)+(3^2-1^2)=(7-5)(7+5)+(3-1)(3+1)=2\times12+2\times4=24+8=32$. |
| A4 | `$-16$` | Vieta's formulas & symmetric polynomials | $\left(p-\frac{1}{p}\right)\!\!\left(q-\frac{1}{q}\right)=pq-\frac{p}{q}-\frac{q}{p}+\frac{1}{pq}=pq-\frac{p^2+q^2}{pq}+\frac{1}{pq}$. Vieta: $p+q=8$, $pq=3$. $p^2+q^2=(p+q)^2-2pq=64-6=58$. Result $=3-\frac{58}{3}+\frac{1}{3}=3-\frac{57}{3}=3-19=-16$. |
| A5 | `$n$` | polynomial algebra / factorisation | $\frac{(2n)!}{(2n-1)!}=2n$ and $\frac{n!}{(n-1)!}=n$. Difference $=2n-n=n$. |
| A6 | `$(3x-2)(9x^2+6x+4)$` | polynomial algebra / factorisation | Difference of cubes: $(3x)^3-2^3=(3x-2)(9x^2+6x+4)$. |
| A7 | `$\left(x+\dfrac{1}{x}\right)^2$` | polynomial algebra / factorisation | $t^2+4=\left(x-\frac{1}{x}\right)^2+4=x^2-2+\frac{1}{x^2}+4=x^2+2+\frac{1}{x^2}=\left(x+\frac{1}{x}\right)^2$. |
| A8 | `$0$` | logarithms | $3+2-5=0$. Convert to powers of 2: $8=2^3$, $4=2^2$, $32=2^5$. |
| A9 | `$-2x^2-4x-1$` | functions | $f(g(x))=2(x^2-1)+1=2x^2-1$. $g(f(x))=(2x+1)^2-1=4x^2+4x+1-1=4x^2+4x$. Difference $=2x^2-1-4x^2-4x=-2x^2-4x-1$. |
| A10 | `$b-c$` | polynomial algebra / factorisation | $\frac{(a-b)(a+b)}{a-b}-\frac{(a-c)(a+c)}{a-c}=(a+b)-(a+c)=b-c$. |
| B1 | `$\dfrac{1}{n}$;\quad at $n=100$: $\dfrac{1}{100}$` | sequences & series / telescoping | $\prod_{k=2}^n\frac{k-1}{k}=\frac{1}{2}\cdot\frac{2}{3}\cdot\frac{3}{4}\cdots\frac{n-1}{n}=\frac{1}{n}$ (telescoping). |
| B2 | `$\dfrac{(x+2)(x-1)}{(x+1)^2}$` | polynomial algebra / factorisation | $x^2+3x-10=(x+5)(x-2)$, $x^2-x-2=(x-2)(x+1)$, $x^2+x-2=(x+2)(x-1)$, $x^2+6x+5=(x+5)(x+1)$. So $\dfrac{(x+5)(x-2)}{(x-2)(x+1)}\cdot\dfrac{(x+2)(x-1)}{(x+5)(x+1)} =\dfrac{(x+2)(x-1)}{(x+1)^2}$. |
| B3 | `$8$` | polynomial algebra / factorisation | $ab+bc+ca=\frac{(a+b+c)^2-(a^2+b^2+c^2)}{2}=\frac{4-6}{2}=-1$. Then $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$. So $a^3+b^3+c^3-3(-2)=2(6-(-1))=14$, hence $a^3+b^3+c^3=8$. |
| B4 | `$(x^2+2x+2)(x^2-2x+2)$` | polynomial algebra / factorisation | Sophie Germain: $x^4+4=(x^4+4x^2+4)-4x^2=(x^2+2)^2-(2x)^2=(x^2+2x+2)(x^2-2x+2)$. |
| B5 | `$f^{-1}(x)=\dfrac{x+1}{x-2}$` | functions | Set $y=\frac{2x+1}{x-1}$: $y(x-1)=2x+1\Rightarrow xy-y=2x+1\Rightarrow x(y-2)=y+1\Rightarrow x=\frac{y+1}{y-2}$. So $f^{-1}(x)=\frac{x+1}{x-2}$. Verify: $f\!\left(\frac{x+1}{x-2}\right)=\frac{2\cdot\frac{x+1}{x-2}+1}{\frac{x+1}{x-2}-1}=\frac{\frac{2x+2+x-2}{x-2}}{\frac{x+1-x+2}{x-2}}=\frac{3x}{3}=x$. \checkmark |
| B6 | `$(n^2+n-1)^2-1$` | polynomial algebra / factorisation | Let the integers be $n-1, n, n+1, n+2$. Pair: $(n-1)(n+2)=n^2+n-2$ and $n(n+1)=n^2+n$. Let $m=n^2+n$: product $=(m-2)m=m^2-2m$. So product $+1=m^2-2m+1=(m-1)^2=(n^2+n-1)^2$. $\square$ |
| B7 | `$\dfrac{8}{1-x^8}$` | polynomial algebra / factorisation | $\frac{1}{1+x}+\frac{1}{1-x}=\frac{2}{1-x^2}$. Then $\frac{2}{1-x^2}+\frac{2}{1+x^2}=\frac{4}{1-x^4}$. Then $\frac{4}{1-x^4}+\frac{4}{1+x^4}=\frac{8}{1-x^8}$. |
| B8 | `$-3q$` | polynomial algebra / factorisation | Each root satisfies the equation: $\alpha^3=-p\alpha-q$. Similarly for $\beta,\gamma$. Add: $\alpha^3+\beta^3+\gamma^3=-p(\alpha+\beta+\gamma)-3q=-p(0)-3q=-3q$ (since $\alpha+\beta+\gamma=0$ for a depressed cubic). |
| B9 | `Proved below.` | polynomial algebra / factorisation | $a+b+c=0\Rightarrow(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)=0\Rightarrow ab+bc+ca=-\frac{s}{2}$ where $s=a^2+b^2+c^2$. $(ab+bc+ca)^2=a^2b^2+b^2c^2+c^2a^2+2abc(a+b+c)=a^2b^2+b^2c^2+c^2a^2$. $(a^2+b^2+c^2)^2=a^4+b^4+c^4+2(a^2b^2+b^2c^2+c^2a^2)=s^2$. And $(ab+bc+ca)^2=s^2/4$, so $a^2b^2+b^2c^2+c^2a^2=s^2/4$. Thus $a^4+b^4+c^4=s^2-2(s^2/4)=s^2/2$. So $(a^2+b^2+c^2)^2=s^2=2(s^2/2)=2(a^4+b^4+c^4)$. $\square$ |
| B10 | `$x=\dfrac{7}{2}$ and $x=-\dfrac{5}{2}$` | polynomial algebra / factorisation | Let $u=\frac{x+1}{x-2}$: $u+\frac{1}{u}=\frac{10}{3}\Rightarrow3u^2-10u+3=0\Rightarrow(3u-1)(u-3)=0$. $u=3$: $\frac{x+1}{x-2}=3\Rightarrow x+1=3x-6\Rightarrow x=\frac{7}{2}$. $u=\frac{1}{3}$: $\frac{x+1}{x-2}=\frac{1}{3}\Rightarrow3x+3=x-2\Rightarrow x=-\frac{5}{2}$. Check: at $x=7/2$: $\frac{9/2}{3/2}=3$ and $\frac{3/2}{9/2}=\frac{1}{3}$. Sum $=3+\frac{1}{3}=\frac{10}{3}$. \checkmark |
| C1 | `Proved below.` | polynomial algebra / factorisation | Weighted AM--GM with weights $\frac{1}{3}$ and $\frac{2}{3}$: $\frac{1}{3}\cdot x+\frac{2}{3}\cdot y\geq x^{1/3}y^{2/3}$. $\square$ (This is the standard statement of weighted AM--GM: $\lambda a+(1-\lambda)b\geq a^\lambda b^{1-\lambda}$ for $a,b>0$, $\lambda\in(0,1)$, here $\lambda=\frac{1}{3}$.) |
| C2 | `$\left(\dfrac{3}{2},-\dfrac{1}{2}\right)$ and $\left(-\dfrac{1}{2},\dfrac{3}{2}\right)$` | Vieta's formulas & symmetric polynomials | Let $p=xy$. Since $x+y=1$, we have $x^2+y^2=1-2p$. Then $x^4+y^4=(x^2+y^2)^2-2x^2y^2=(1-2p)^2-2p^2=1-4p+2p^2$. Set this equal to $\frac{41}{8}$: $1-4p+2p^2=\frac{41}{8}\Rightarrow16p^2-32p-33=0$. So $p=\frac{32\pm56}{32}$, hence $p=\frac{11}{4}$ or $p=-\frac{3}{4}$. But $x+y=1$ gives real roots only if $1-4p\ge0$, so $p=\frac{11}{4}$ is impossible. Thus $p=-\frac{3}{4}$. Now $x,y$ are roots of $t^2-t-\frac{3}{4}=0$, i.e. $4t^2-4t-3=0$. Hence $t=\frac{3}{2}$ or $t=-\frac{1}{2}$, so $(x,y)=\left(\frac{3}{2},-\frac{1}{2}\right)$ or $\left(-\frac{1}{2},\frac{3}{2}\right)$. |
| C3 | `All three inequalities proved below.` | surds / denesting | (Right) $\sqrt{ab}\geq\frac{2ab}{a+b}$: divide by $\sqrt{ab}>0$: $1\geq\frac{2\sqrt{ab}}{a+b}$, i.e.\ $a+b\geq2\sqrt{ab}$ --- AM--GM. \checkmark (Middle) $\frac{a+b}{2}\geq\sqrt{ab}$: AM--GM directly. \checkmark (Left) $\sqrt{\frac{a^2+b^2}{2}}\geq\frac{a+b}{2}$: square both sides (both positive): $\frac{a^2+b^2}{2}\geq\frac{(a+b)^2}{4}\Leftrightarrow2(a^2+b^2)\geq(a+b)^2\Leftrightarrow(a-b)^2\geq0$. \checkmark $\square$ |
| C4 | `$x=1$ and $x=0$` | polynomial algebra / factorisation | $27^x+\frac{27}{27^x}=28$. Let $u=27^x$: $u+\frac{27}{u}=28\Rightarrow u^2-28u+27=(u-1)(u-27)=0$. $u=1\Rightarrow x=0$; $u=27\Rightarrow x=1$. |
| C5 | `Proved below.` | algebraic inequalities | By AM--HM (or AM--GM): $\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\geq\frac{9}{a+b+c}=9$ by the AM--HM inequality $\frac{n}{\sum\frac{1}{x_i}}\leq\frac{\sum x_i}{n}$, i.e.\ $\sum\frac{1}{x_i}\geq\frac{n^2}{\sum x_i}$. Alternatively: Cauchy--Schwarz (Engel): $\frac{1}{a}+\frac{1}{b}+\frac{1}{c}=\frac{1^2}{a}+\frac{1^2}{b}+\frac{1^2}{c}\geq\frac{(1+1+1)^2}{a+b+c}=9$. $\square$ |
| C6 | `$3016$` | sequences & series / telescoping | $\sum_{k=3}^{10}k^3=\sum_{k=1}^{10}k^3-1^3-2^3=\left(\frac{10\times11}{2}\right)^2-1-8=3025-9=3016$. |
| C7 | `All real $x$.` | polynomial algebra / factorisation | $\|x^2-4\|=\|(x-2)(x+2)\|=\|x-2\|\cdot\|x+2\|$ by the multiplicative property of absolute values: $\|ab\|=\|a\|\|b\|$. This holds for all real $x$, with no restriction. So the solution set is $\mathbb{R}$. |
| C8 | `Maximum is $\dfrac{256}{27}$ at $x=\dfrac{8}{3}$, $y=\dfrac{4}{3}$.` | algebraic inequalities | Apply AM--GM to $\frac{x}{2},\frac{x}{2},y$: $\frac{x/2+x/2+y}{3}\ge\left(\frac{x^2y}{4}\right)^{1/3}$. Since $x+y=4$, this gives $\frac{4}{3}\ge\left(\frac{x^2y}{4}\right)^{1/3}$, so $x^2y\le\frac{256}{27}$. Equality when $x/2=x/2=y$, i.e. $x=\frac{8}{3}$, $y=\frac{4}{3}$. |
| D1 | `(a) $(a,b)=(8,2)$ gives $k=4$. (b) Vieta jumping establishes no new solutions beyond the obvious family.` | Vieta's formulas & symmetric polynomials | (a) $a=8,b=2$: $64+4=68=4(16+1)=68$. \checkmark So $k=4$ is achieved. (b) Fix $k$ and $b$; consider $a$ as a root of $x^2-kbx+(b^2-k)=0$. The other root $a'$ satisfies $a+a'=kb$ (sum of roots) and $aa'=b^2-k$ (product). So $a'=kb-a$ is an integer, and $a'\cdot b=b^2-k$, so $a'^2+b^2=k(a'b+1)$ (verify). If $a>b$, then $a'^2=k(a'b+1)-b^2$; since $a'\cdot b=b^2-k<b^2$ (if $k>0$), we get $a'<b$. So we can descend: $(a,b)\to(b,a')\to\ldots$ until we reach a base case. |
| D2 | `$p(x)=cx(x-1)(x+1)$ for any constant $c$.` | polynomial algebra / factorisation | $x=1$: $0=3p(1)\Rightarrow p(1)=0$. $x=-2$: $(-3)p(-1)=0\Rightarrow p(-1)=0$. $x=0$: $(-1)p(1)=2p(0)\Rightarrow p(0)=0$. So $x$, $(x-1)$, and $(x+1)$ divide $p$. Try $p(x)=x(x-1)(x+1)$: $(x-1)(x+1)(x)(x+2)=(x+2)x(x-1)(x+1)$. \checkmark By degree considerations, this is the unique (up to scalar) polynomial solution. |
| D3 | `$\dfrac{3}{2}$` | algebraic inequalities | $\frac{a}{1-a}=\frac{a}{b+c}$. So the sum is $\frac{a}{b+c}+\frac{b}{a+c}+\frac{c}{a+b}$. By Nesbitt's inequality: $\frac{a}{b+c}+\frac{b}{a+c}+\frac{c}{a+b}\geq\frac{3}{2}$. Equality at $a=b=c=\frac{1}{3}$. |
| D4 | `$\dfrac{2}{3}$` | sequences & series / telescoping | $\frac{n^3-1}{n^3+1}=\frac{(n-1)(n^2+n+1)}{(n+1)(n^2-n+1)}$. The infinite product splits into two: $\prod_{n=2}^N\frac{n-1}{n+1}=\frac{1}{2}\cdot\frac{2}{3}\cdot\frac{3}{4}\cdots\frac{N-1}{N+1}=\frac{1\cdot2}{N(N+1)}\to0$. $\prod_{n=2}^N\frac{n^2+n+1}{n^2-n+1}$: note $n^2+n+1=(n+1)^2-(n+1)+1$ and $n^2-n+1=n^2-n+1$. Setting $a_n=n^2-n+1$: $a_{n+1}=(n+1)^2-(n+1)+1=n^2+n+1$. So $\frac{n^2+n+1}{n^2-n+1}=\frac{a_{n+1}}{a_n}$. This telescopes: $\prod_{n=2}^N\frac{a_{n+1}}{a_n}=\frac{a_{N+1}}{a_2}=\frac{N^2+N+1}{3}$. Combined: $\prod_{n=2}^N\frac{n^3-1}{n^3+1}=\frac{1\cdot2}{N(N+1)}\cdot\frac{N^2+N+1}{3}=\frac{2(N^2+N+1)}{3N(N+1)}$. As $N\to\infty$: $\frac{2(N^2+N+1)}{3N^2+3N}\to\frac{2}{3}$. $\square$ |
| D5 | `$(n,-n)$ for all $n\in\mathbb{Z}$, and $(1,0), (0,1), (1,2), (2,1), (2,2)$` | polynomial algebra / factorisation | Let $s=x+y$ and $p=xy$. $x^3+y^3=s(s^2-3p)=s^2$. If $s=0$: $y=-x$ (infinitely many solutions $(n,-n)$). If $s\neq0$: $s^2-3p=s \Rightarrow p=\frac{s(s-1)}{3}$. For real $x,y$, discriminant $s^2-4p = s^2-\frac{4s(s-1)}{3} = \frac{4s-s^2}{3} \geq 0$. Thus $0<s\leq 4$. Try $s=1$: $p=0 \Rightarrow (1,0),(0,1)$. Try $s=2$: $p=2/3$ (reject). Try $s=3$: $p=2 \Rightarrow (1,2),(2,1)$. Try $s=4$: $p=4 \Rightarrow (2,2)$. |



### Combinatorics Answer Keys

#### Sheet 02

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$21$` | combinations & permutations | $\dbinom{7}{2}=\dfrac{7\cdot6}{2}=21$. For $\binom{n}{2}$, always: half of $n(n-1)$. |
| A2 | `$56$` | factorials | $\dbinom{8}{3}=\dfrac{8\cdot7\cdot6}{3!}=\dfrac{336}{6}=56$. Cancel before multiplying: $\frac{8\cdot7\cdot6}{6}=8\cdot7$. |
| A3 | `$36$` | combinations & permutations | Use symmetry first: $\dbinom{9}{7}=\dbinom{9}{2}=\dfrac{9\cdot8}{2}=36$. Never compute a large lower index directly. |
| A4 | `$\dbinom{6}{3}=20$` | combinations & permutations | A committee is unordered: $\dbinom{6}{3}=\dfrac{6\cdot5\cdot4}{6}=20$. |
| A5 | `$n=10$` | combinations & permutations | $\dfrac{n(n-1)}{2}=45\Rightarrow n(n-1)=90=10\cdot9\Rightarrow n=10$. Spot consecutive-integer products instantly. |
| A6 | `$\dbinom{5}{4}+\dbinom{5}{5}=5+1=6$` | combinations & permutations | ``At least 4'' means sizes 4 or 5. Two small cases --- add them. |
| A7 | `$2^6=64$` | combinations & permutations | Row sum of Pascal's triangle: every subset of a 6-set has \emph{some} size, so the sizes partition the $2^6$ subsets. |
| A8 | `$\dbinom{5}{2}=10$` | combinations & permutations | Unordered pairs from 5: $\frac{5\cdot4}{2}=10$. |
| A9 | `True` | combinations & permutations | $\dbinom{100}{98}=\dbinom{100}{2}=\dfrac{100\cdot99}{2}=4950$. |
| A10 | `$\dbinom{10}{4}=210$` | combinations & permutations | Pure choice, no order: $\dfrac{10\cdot9\cdot8\cdot7}{24}=210$. |
| B1 | `$n=7$` | combinations & permutations | $n(n-1)(n-2)=35\cdot6=210=7\cdot6\cdot5$. Three consecutive integers --- read off $n=7$. |
| B2 | `$\dbinom{8}{2}\dbinom{6}{2}=28\cdot15=420$` | combinations & permutations | Independent choices multiply: choose the men, then the women. |
| B3 | `$\dbinom{12}{2}=66$` | combinations & permutations | A handshake \emph{is} an unordered pair of people. |
| B4 | `$\dbinom{10}{2}=45$ segments;\quad $\dbinom{10}{3}=120$ triangles` | combinations & permutations | A segment is a pair of points; a triangle is a triple. The no-three-collinear condition guarantees every triple genuinely forms a triangle. |
| B5 | `$\dbinom{11}{5}\cdot5=2310=11\cdot\dbinom{10}{4}$` | combinations & permutations | Team first: $462\cdot5$. Captain first: 11 choices, then 4 teammates from the remaining 10: $11\cdot210$. Both give 2310. |
| B6 | `$\dbinom{8}{3}=56$` | combinations & permutations | A string is determined by \emph{which} 3 of the 8 positions hold the 1s. |
| B7 | `$\dbinom{5}{1}\dbinom{21}{2}=5\cdot210=1\,050$` | combinations & permutations | Choose the vowel, then the pair of consonants --- independent choices multiply. |
| B8 | `$n=6$` | combinations & permutations | $\frac{n(n-1)}{2}+n=\frac{n(n+1)}{2}=21\Rightarrow n(n+1)=42=6\cdot7\Rightarrow n=6$. |
| B9 | `Include: $\dbinom{8}{3}=56$;\quad exclude: $\dbinom{8}{4}=70$` | combinations & permutations | Include her: she is in, choose 3 companions from 8. Exclude her: choose all 4 from the other 8. |
| B10 | `$\dbinom{7}{3}=35$` | combinations & permutations | Every route is a string of 4 R's and 3 U's: choose which 3 of the 7 steps are U. |
| C1 | `$\dbinom{7}{4}\dbinom{6}{1}+\dbinom{7}{5}=35\cdot6+21=231$` | combinations & permutations | Exactly 4 women or exactly 5 women --- two disjoint cases, then add. |
| C2 | `$9000-9\cdot9\cdot8\cdot7=9000-4536=4464$` | combinatorial counting | Complement: all-distinct four-digit numbers number $9\cdot9\cdot8\cdot7$ (sheet 1 technique). Subtract from 9000. |
| C3 | `$\dbinom{12}{2}-12=66-12=54$` | combinations & permutations | Every pair of vertices gives a segment; remove the 12 sides. (Regularity is irrelevant --- only convexity matters.) |
| C4 | `$\dbinom{8}{3}=56$ in total;\quad $\dbinom{7}{3}=35$ avoid $A$` | combinations & permutations | All triples work (no three points on a circle are collinear). Avoiding $A$: all three vertices come from the other 7 points. Alternatively by complement: $56-\binom{7}{2}=56-21=35$ --- subtract the triangles \emph{through} $A$. |
| C5 | `$\dbinom{12}{6}-\dbinom{6}{3}^2=924-400=524$` | combinations & permutations | Complement: the only \emph{equal} split for a team of 6 is 3--3, counted by $\binom{6}{3}\binom{6}{3}=400$. Subtract from all $\binom{12}{6}=924$ teams. Listing the unequal splits (6--0, 5--1, 4--2 and mirrors) works too but is six cases instead of one subtraction. |
| C6 | `$\dbinom{4}{3}\dbinom{48}{2}+\dbinom{48}{1}=4512+48=4\,560$` | combinations & permutations | Two disjoint cases. \emph{Exactly three aces:} choose which 3 of the 4 aces, then 2 non-aces: $4\cdot1128$. \emph{All four aces:} the aces are forced, only the fifth card is free: $48$. |
| C7 | `$n=9$` | combinatorial counting | $\frac{n(n-3)}{2}=27\Rightarrow n(n-3)=54=9\cdot6\Rightarrow n=9$. (Product of two integers differing by 3 --- read it off.) |
| C8 | `$2^{10}-2^8=1024-256=768$` | combinatorial counting | Complement: subsets avoiding \emph{both} 1 and 2 are exactly the subsets of the remaining 8 elements: $2^8$. |
| D1 | `$\dbinom{5}{2}^2=100$` | bijections / grid paths | A rectangle is determined by choosing 2 of the 5 vertical gridlines and 2 of the 5 horizontal gridlines: $\binom{5}{2}\cdot\binom{5}{2}=10\cdot10$. Sheet 1 counted the spans by listing $(4+3+2+1)$; the binomial coefficient \emph{is} that sum. |
| D2 | `$55$` | factorials | Let $a_n$ count such subsets of $\{1,\ldots,n\}$. Split on whether $n$ is used: if not, $a_{n-1}$ subsets; if yes, $n-1$ is banned, leaving $a_{n-2}$. So $a_n=a_{n-1}+a_{n-2}$ with $a_1=2$, $a_2=3$ --- Fibonacci! The chain runs $2,3,5,8,13,21,34,55$, so $a_8=55$. |
| D3 | `$\dfrac{2^{12}-\binom{12}{6}}{2}=\dfrac{4096-924}{2}=1\,586$` | bijections / grid paths | Every committee has more juniors, more seniors, or a tie. Pair each junior with a senior once and for all; swapping every member for their partner is a bijection between ``more juniors'' committees and ``more seniors'' committees, so those two counts are equal. Ties (equal numbers, $k$ of each) number $\sum_k\binom{6}{k}^2=\binom{12}{6}=924$ by Vandermonde. Hence each majority count is $\frac{4096-924}{2}=1586$. No case-by-case summation needed. |
| D4 | `$70$` | factorials | Everyone having exactly two handshakes forces the handshake pattern to be a union of cycles of length $\geq3$ covering all 6 people: either one 6-cycle or two 3-cycles. \emph{One 6-cycle:} arrange 6 people in a cycle: $\frac{5!}{2}=60$ (rotations and reflection give the same handshake set). \emph{Two 3-cycles:} split into two trios: $\frac{1}{2}\binom{6}{3}=10$, each trio shaking hands in exactly one way. Total $60+10=70$. |
| D5 | `$\dbinom{10}{4}=210$` | combinations & permutations | The key insight: every interior intersection comes from exactly one set of 4 points on the circle (the two crossing chords are the diagonals of the quadrilateral those 4 points form), and every 4 points create exactly one interior crossing. So intersections $\leftrightarrow$ 4-subsets: $\binom{10}{4}=210$. No coordinate geometry, no counting chords. |


#### Sheet 03

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$5!=120$` | factorials | Distinct objects in a row: factorial. Instant. |
| A2 | `$5!=120$` | factorials | Five \emph{distinct} letters --- same question as A1 in costume. |
| A3 | `$\dfrac{6!}{3!\,2!}=60$` | factorials | Six letters: A$\times$3, N$\times$2, B$\times$1. Divide $6!$ by the repeats: $\frac{720}{6\cdot2}$. |
| A4 | `$(4-1)!=6$` | factorials | Fix one person to kill the rotational symmetry; arrange the remaining 3 freely. |
| A5 | `$4!=24$` | factorials | Two positions forced, four people free. |
| A6 | `$\dbinom{5}{2}=10$` | factorials | Only the \emph{positions} of the blue flags matter: choose 2 places from 5. Equivalently $\frac{5!}{3!2!}$. |
| A7 | `$\dfrac{4!}{2!\,2!}=6$` | factorials | Four letters, two pairs: $\frac{24}{4}$. |
| A8 | `$(6-1)!=120$` | factorials | Fix one person, arrange 5. |
| A9 | `True --- both are $7!=5040$` | factorials | Circular $n$ $=(n-1)!$ $=$ row arrangements of $n-1$. Fixing one diner \emph{is} reducing to a row of the rest. |
| A10 | `$\dfrac{5!}{3!}=20$` | factorials | Five letters with T$\times$3: divide by $3!$. |
| B1 | `$2\cdot5!=240$` | factorials | Glue the pair (block has 2 internal orders), arrange 5 objects. |
| B2 | `$720-240=480$` | combinatorial counting | Complement of B1. |
| B3 | `$\dfrac{11!}{4!\,4!\,2!}=34\,650$` | factorials | 11 letters: I$\times$4, S$\times$4, P$\times$2, M$\times$1. One division, no listing. |
| B4 | `$5!\cdot(6\cdot5\cdot4)=120\cdot120=14\,400$` | factorials | Gap method: arrange the boys ($5!$), creating 6 gaps (including the two ends); place the three distinct girls in three \emph{different} gaps, in order: $6\cdot5\cdot4$. |
| B5 | `$2\cdot4!\cdot4!=1\,152$` | factorials | Two gender patterns (MWMW\ldots{} or WMWM\ldots), then the men fill their 4 slots in $4!$ ways and the women theirs in $4!$. |
| B6 | `$2\cdot(5-1)!=48$` | factorials | Glue the pair into a block: 5 objects round a table $=(5-1)!$, times 2 internal orders. |
| B7 | `$\dfrac{6!}{2!\,2!\,2!}=90$` | factorials | Three pairs: divide $720$ by $2^3$. |
| B8 | `$\dfrac{5!}{2!\,2!}=30$` | factorials | L$\times$2, E$\times$2, V: divide $120$ by 4. |
| B9 | `$\dfrac{7!}{3!}=840$` | factorials | Forced-order trick: of the $3!$ orderings of the trilogy within any arrangement, exactly one is correct --- so divide $7!$ by $3!$. No gluing: they need not be adjacent. |
| B10 | `$n=7$` | factorials | $(n-1)!=720=6!$, so $n=7$. |
| C1 | `$3!\cdot6!-3!\cdot2!\cdot5!=4\,320-1\,440=2\,880$` | factorials | Layer the constraints (sheet's D2 pattern, arriving early). Glue the trio: $3!\cdot6!=4\,320$ arrangements. From these subtract those where the two enemies are also adjacent --- glue them too: $3!\cdot2!\cdot5!=1\,440$. Answer $2\,880$. |
| C2 | `$6!=720$` | factorials | The block's internal order is now forced: glue with factor 1, then 6 objects in a row. |
| C3 | `$\dfrac{7!}{3!\,2!}-\dfrac{5!}{2!}=420-60=360$` | factorials | Total arrangements: $\frac{7!}{3!2!}=420$. All-D's-together: glue [DDD] (identical letters, factor 1) and arrange it with I, I, V, E: $\frac{5!}{2!}=60$. Subtract. |
| C4 | `$3!\cdot4!=144$` | factorials | Seat the men first: circular, so $(4-1)!=6$. Their seating fixes 4 alternating gaps, into which the women go in $4!$ ways. (No extra factor 2: in a circle the two ``patterns'' are rotations of each other.) |
| C5 | `$\dfrac{6!}{2!}-5!=360-120=240$` | factorials | Total (with C repeated): 360. Together: glue CC (identical, no internal factor): $5!=120$. Subtract. |
| C6 | `$18$` | factorials | Two interacting constraints (units even, leading digit 4 or 5) --- case on the units digit, because it consumes a candidate leading digit or not. \emph{Units 2:} leading digit from $\{4,5\}$, rest free: $2\cdot3!=12$. \emph{Units 4:} leading digit must be 5, rest free: $3!=6$. Total $18$. |
| C7 | `$3!\cdot(3!\cdot2!\cdot2!)=6\cdot24=144$` | factorials | Arrange the three subject blocks ($3!$), then the books inside each block ($3!,2!,2!$). |
| C8 | `$7!-2\cdot6!=5\,040-1\,440=3\,600$` | factorials | All seatings ($7!$) minus glued-pair seatings ($2\cdot6!$). |
| D1 | `$\dbinom{7}{4}=35$` | factorials | Choose which 4 of the 7 positions hold the odd digits: $\binom{7}{4}=35$. Everything else is forced --- the odds $1,3,5,7$ must fill their positions in increasing order (one way), and the evens $6,4,2$ fill theirs in decreasing order (one way). A count that looks like it needs $7!$ cases collapses to a single choice. |
| D2 | `$2\cdot8!-4\cdot7!=80\,640-20\,160=60\,480$` | factorials | Layer the constraints. Glue Mia--Noah: $2\cdot(9-1)!=80\,640$ circles. From these subtract the ones where Omar--Priya are also adjacent (glue both pairs): $2\cdot2\cdot(8-1)!=20\,160$. Answer: $60\,480$. |
| D3 | `$30$` | factorials | Inclusion--exclusion on the ``bad pair'' events, computed cleanly by gluing. Total: $\frac{6!}{2!2!2!}=90$. Glue AA: $\frac{5!}{2!2!}=30$, same for BB, CC. Glue two pairs: $\frac{4!}{2!}=12$ each (3 ways). Glue all three: $3!=6$. Count with no glued pair $=90-3\cdot30+3\cdot12-6=30$. |
| D4 | `$8!-14\,400-4\,320=21\,600$` | factorials | Three disjoint outcomes partition all $8!=40\,320$ arrangements: \emph{no} adjacent sister-pair, \emph{exactly one} adjacent sister-pair, and \emph{two} adjacent sister-pairs (which is precisely ``all three consecutive''). \emph{None adjacent} (gap method): $5!\cdot6\cdot5\cdot4=14\,400$. \emph{All three consecutive}: $3!\cdot6!=4\,320$. ``Exactly two sisters adjacent'' is the middle category, so it equals $40\,320-14\,400-4\,320=21\,600$. |
| D5 | `$3!\cdot2\cdot(4\cdot3\cdot2)=288$` | factorials | Layer: glue first, then gaps. Glue the King--Queen pair (2 internal orders); the peaceful side is now 4 units (the KQ block plus 3 other knights). Seat those 4 units round the table: $(4-1)!=6$ circular orders, creating exactly 4 gaps. Place the three feuding knights into three different gaps (one each --- sharing a gap would make two feuders adjacent): $4\cdot3\cdot2=24$. Total $6\cdot2\cdot24=288$. |


#### Sheet 04

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$\dbinom{5}{2}=10$` | binomial theorem / coefficients | Binomial theorem: the $x^k$ coefficient in $(1+x)^n$ is $\binom{n}{k}$. |
| A2 | `$12$` | binomial theorem / coefficients | Term with $x^1$: $\binom{3}{1}x\cdot2^2=12x$. Keep track of which quantity is being raised to which power. |
| A3 | `$1,\;5,\;10,\;10,\;5,\;1$` | combinatorial counting | Adjacent sums of row 4 ($1,4,6,4,1$), or $\binom{5}{k}$ directly. |
| A4 | `$\dbinom{5}{2}=10$` | binomial theorem / coefficients | Choose which 2 of the 5 brackets contribute $y$: $\binom{5}{2}$. |
| A5 | `$2^7=128$` | binomial theorem / coefficients | Substitute $x=1$: the expansion collapses to its coefficient sum. |
| A6 | `$\dbinom{4}{2}=6$` | combinations & permutations | Powers cancel when the $x$'s and $\frac1x$'s balance: 2 of each. |
| A7 | `$\dbinom{10}{5}$\quad(which is 252)` | binomial theorem / coefficients | Pascal's rule: adjacent entries sum to the entry below. No evaluation needed --- the recognition is the answer. |
| A8 | `$0$` | combinations & permutations | Substitute $x=-1$ into $(1+x)^6$: $0^6=0$. |
| A9 | `False --- it is $+45$` | binomial theorem / coefficients | The $x^2$ term is $\binom{10}{2}(-x)^2=45x^2$: the square eats the sign. Signs alternate, and even powers are positive. |
| A10 | `$\dbinom{4}{2}=6$` | binomial theorem / coefficients | Rows of Pascal's triangle rise to the middle and fall symmetrically. |
| B1 | `$\dbinom{5}{3}2^2 3^3=10\cdot4\cdot27=1\,080$` | binomial theorem / coefficients | General term $\binom{5}{k}2^{5-k}(3x)^k$; set $k=3$. Both constants carry powers --- forgetting $2^{5-k}$ is the classic slip. |
| B2 | `$168$` | binomial theorem / coefficients | Convolve the tails only: from $(1+2x)^4$ take coefficients $16, 32, 24$ (of $x^4,x^3,x^2$) and from $(1+x)^3$ take $3, 3, 1$ (of $x,x^2,x^3$): $16\cdot3+32\cdot3+24\cdot1=168$. |
| B3 | `$\dbinom{6}{2}2^4=240$` | combinations & permutations | General term: $\binom{6}{k}(2x)^{6-k}x^{-2k}$ has degree $6-3k$. Zero degree forces $k=2$: $\binom{6}{2}2^4$. |
| B4 | `$n=12$` | binomial theorem / coefficients | $\binom{n}{2}=66\Rightarrow n(n-1)=132=12\cdot11$. |
| B5 | `$\dbinom{6}{2}=15$` | binomial theorem / coefficients | General term $\binom{6}{k}(x^2)^{6-k}x^{-k}$ has degree $12-3k$; degree 6 forces $k=2$. |
| B6 | `$9$` | binomial theorem / coefficients | Convolve only what is needed: $x^2$ coefficient $=24\cdot1+8\cdot(-2)+1\cdot1=9$, using $(1+2x)^4=1+8x+24x^2+\cdots$ and $(1-x)^2=1-2x+x^2$. |
| B7 | `$11^3=1\,331$;\quad $9^3=729$` | combinatorial counting | $(10+1)^3=1000+300+30+1$; $(10-1)^3=1000-300+30-1$. Pascal row 3 does the arithmetic. |
| B8 | `$k=2$` | binomial theorem / coefficients | $\binom{6}{3}k^3=20k^3=160\Rightarrow k^3=8$. |
| B9 | `$n=5$` | combinations & permutations | Equal entries sit symmetrically: $\binom{n}{r}=\binom{n}{s}$ (with $r\neq s$) forces $r+s=n$. So $n=2+3=5$. |
| B10 | `$\dfrac{5!}{2!\,2!\,1!}=30$` | factorials | Multinomial: distribute the 5 brackets among the letters --- exactly the BANANA formula from sheet 3 wearing algebra. |
| C1 | `$2^9=512$` | combinations & permutations | Substitute twice into $(1+x)^{10}$: $x=1$ gives $2^{10}$ (all terms), $x=-1$ gives $0$ (alternating). Adding kills the odd-index terms and doubles the even ones: sum $=(2^{10}+0)/2=512$. |
| C2 | `$\dbinom{8}{4}=70$` | binomial theorem / coefficients | Ratio test from A10's inv: $\frac{\binom{8}{k+1}}{\binom{8}{k}}=\frac{8-k}{k+1}>1$ exactly while $k<3.5$, so coefficients climb to $k=4$ then fall. |
| C3 | `$1+10(0.01)+45(0.01)^2=1.1045$` | combinatorial counting | $(1+x)^{10}$ at $x=0.01$; terms shrink so fast the tail is invisible at 4 d.p. |
| C4 | `$n=9$` | binomial theorem / coefficients | $\binom{n}{5}3^5=3\cdot\binom{n}{4}3^4$. The powers of 3 cancel completely ($3^5$ on both sides), leaving $\binom{n}{5}=\binom{n}{4}$, so $n=4+5=9$ by symmetry. |
| C5 | `$25$` | binomial theorem / coefficients | Convolution with signs, harvesting only degree-4 pairs: $5\cdot1+10\cdot(-6)+10\cdot12+5\cdot(-8)=5-60+120-40=25$. Lay the two coefficient lists side by side and zip them --- do not expand the product. |
| C6 | `$5\cdot2^4=80$` | combinations & permutations | Committee--chair (sheet 2, B5): $k\binom{5}{k}=5\binom{4}{k-1}$, and summing the right side gives $5\cdot2^4$. Alternatively differentiate $(1+x)^5$ and set $x=1$. |
| C7 | `$3^6=729$` | combinatorial counting | The sum is exactly $(1+x)^6$ at $x=2$: $(1+2)^6=729$. Recognising a binomial expansion \emph{in reverse} is the skill --- the $2^k$ pattern names the substitution. |
| C8 | `Row 7: $1,7,21,35,35,21,7,1$` | combinations & permutations | \emph{Proof.} A committee of $r$ from $n$ people either includes a distinguished person $P$ or not. Including $P$: $\binom{n-1}{r-1}$ choices for the rest. Excluding $P$: $\binom{n-1}{r}$. These cases are disjoint and exhaustive, so $\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}$. $\square$ Adjacent sums of row 6 ($1,6,15,20,15,6,1$) then give row 7. |
| D1 | `Proof below.` | combinations & permutations | \emph{Proof.} By Pascal's rule, $\binom{2n}{n}=\binom{2n-1}{n-1}+\binom{2n-1}{n}$. By the symmetry $\binom{m}{r}=\binom{m}{m-r}$ applied with $m=2n-1$: $\binom{2n-1}{n-1}=\binom{2n-1}{(2n-1)-(n-1)}=\binom{2n-1}{n}$. So $\binom{2n}{n}$ is the sum of two \emph{equal} integers, hence even. $\square$ |
| D2 | `Both count $\binom{20}{10}=184\,756$.` | combinatorial counting | \emph{Proof.} Consider choosing 10 people from a room of 10 women and 10 men: $\binom{20}{10}$ ways. Alternatively, classify each choice by the number $k$ of women chosen: $\binom{10}{k}$ ways for the women and $\binom{10}{10-k}$ for the men, and $\binom{10}{10-k}=\binom{10}{k}$ by symmetry. Summing the disjoint classes: $\sum_k\binom{10}{k}^2$. Two counts of one set are equal. $\square$ |
| D3 | `The odd ones are exactly $k=0,4,8,12$.` | binomial theorem / coefficients | \emph{Proof.} All congruences are mod 2. First, $(1+x)^2=1+2x+x^2\equiv1+x^2$, and squaring again, $(1+x)^4\equiv(1+x^2)^2\equiv1+x^4$. Hence $(1+x)^{12}=\left((1+x)^4\right)^3\equiv(1+x^4)^3=1+3x^4+3x^8+x^{12}\equiv1+x^4+x^8+x^{12}.$ Comparing coefficients of $x^k$ on both sides: $\binom{12}{k}$ is odd precisely when $k\in\{0,4,8,12\}$ --- four values. $\square$ |
| D4 | `$\dbinom{10}{3}=120$` | combinations & permutations | \emph{Proof (classify by largest element).} Count the 3-subsets of $\{1,2,\ldots,10\}$: there are $\binom{10}{3}$. Classify each subset by its largest element $m+1$ (so $m+1$ ranges over $3,\ldots,10$): the other two elements are then any 2-subset of $\{1,\ldots,m\}$, giving $\binom{m}{2}$ subsets in that class. The classes are disjoint and exhaustive, so $\sum_{m=2}^{9}\binom{m}{2}=\binom{10}{3}$. $\square$ |
| D5 | `Proof below.` | factorials | \emph{Proof.} Write $k!\,\binom{p}{k}=p(p-1)\cdots(p-k+1)$. The right side is visibly divisible by $p$, so $p\mid k!\binom{p}{k}$. Since $p$ is prime and every factor of $k!=1\cdot2\cdots k$ is less than $p$, we have $p\nmid k!$, so $p$ and $k!$ are coprime. A prime dividing a product must divide one of the factors; as it cannot divide $k!$, it divides $\binom{p}{k}$. $\square$ (Note where primality is used --- \emph{twice}.) |


#### Sheet 05

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$11$` | combinatorial counting | $x$ can be $0,1,\ldots,10$; then $y$ is forced. |
| A2 | `$\dbinom{7}{2}=21$` | stars and bars / distribution | Stars and bars: 5 stars, 2 bars in a row of 7 symbols; choose the bar positions. |
| A3 | `$15+12-5=22$` | combinatorial counting | Two-set inclusion--exclusion: adding double-counts the overlap once, so subtract it once. |
| A4 | `$\lfloor100/3\rfloor=33$` | combinatorial counting | Floor of the quotient. |
| A5 | `$8+6-11=3$` | combinatorial counting | Rearrange two-set inclusion--exclusion: $\|A\cap B\|=\|A\|+\|B\|-\|A\cup B\|$. |
| A6 | `$\dbinom{6}{2}=15$` | combinations & permutations | 4 stars, 2 bars. |
| A7 | `$\dbinom{5}{2}=10$` | combinations & permutations | Shift: $x'=x-1$ etc.\ gives non-negative $x'+y'+z'=3$: $\binom{5}{2}$. Equivalently, place 2 bars in the 5 gaps between six stars. |
| A8 | `$30-(20+15-8)=3$` | combinatorial counting | Union first (27), then complement. |
| A9 | `True\quad($1{+}6,\,2{+}5,\,\ldots,\,6{+}1$)` | combinatorial counting | The first part can be $1$ through $6$; the second is forced. |
| A10 | `$5$` | stars and bars / distribution | The first box holds $0$--$4$. |
| B1 | `$\dbinom{14}{2}=91$` | combinations & permutations | 12 stars, 2 bars: $\binom{14}{2}$. |
| B2 | `$\dbinom{11}{2}=55$` | combinations & permutations | Shift each variable down by 1: non-negative sum 9, so $\binom{11}{2}$. |
| B3 | `$\dbinom{9}{3}=84$` | combinations & permutations | Bars-in-gaps: ten stars have 9 internal gaps; choose 3. |
| B4 | `$1000-500-200+100=400$` | combinatorial counting | Complement of the union: subtract each, add back the multiples of 10. |
| B5 | `$\dbinom{10}{2}=45$` | combinations & permutations | Shift only $x$: $x'=x-2$ gives $x'+y+z=8$: $\binom{10}{2}$. |
| B6 | `$4!-3!=18$` | factorials | Complement: total minus those with 1 first. |
| B7 | `$50+33-16=67$` | combinatorial counting | Overlap is multiples of 6: $\lfloor100/6\rfloor=16$. |
| B8 | `$\dbinom{7}{2}=21$` | combinations & permutations | Compositions of 8 into 3 positive parts: bars in 2 of the 7 gaps. |
| B9 | `$\dbinom{7}{2}=21$` | combinations & permutations | Slack variable: introduce $s=5-x-y\geq0$; then $x+y+s=5$, a three-variable stars-and-bars. |
| B10 | `$2^5-2=30$` | combinatorial counting | Complement: only the all-A and all-B strings fail. |
| C1 | `$52$` | combinatorial counting | Both bound types at once. Unrestricted positive solutions: $\binom{14}{3}=364$ (bars in gaps). Violations are variables $\geq6$: shift one variable by 5 (positive $\geq6$ becomes positive $\geq1$), leaving sum 10: $\binom{9}{3}=84$, times 4 choices: 336. Double violations (two variables $\geq6$, sum drops to 5): $\binom{4}{3}=4$ each, $\binom{4}{2}=6$ pairs: 24. Triples impossible. Count: $364-336+24=52$. |
| C2 | `$10$` | combinatorial counting | Inclusion--exclusion on the \emph{violations}. Unrestricted: $\binom{17}{2}=136$. Violating $x\geq7$: shift by 7, sum 8: $\binom{10}{2}=45$, and 3 choices of violator: 135. Two violators ($\geq7$ twice, sum drops to 1): $\binom{3}{2}=3$ each, 3 pairs: 9. Three violators impossible. Count: $136-135+9=10$. |
| C3 | `$100-80=20$` | combinatorial counting | Three-set I--E: $\|T\cup C\cup J\|=50+40+30-20-15-10+5=80$. |
| C4 | `$734$` | combinatorial counting | $500+333+200-166-100-66+33=734$. The overlaps are lcm's: 6, 10, 15, 30. |
| C5 | `$15$` | combinatorial counting | Unrestricted: $\binom{10}{2}=45$. One child $\geq5$: shift 5, sum 3: $\binom{5}{2}=10$, times 3 children: 30. Two children $\geq5$ would need sum $\geq10>8$: impossible. Answer $45-30=15$. |
| C6 | `$120-24-24+6=78$` | factorials | I--E on the two bad events (A first: $4!$; B second: $4!$; both: $3!$). |
| C7 | `$27$` | stars and bars / distribution | Stars and bars with caps. Shift to $x'+y'+z'=7$ with each $x'\in[0,5]$: unrestricted $\binom{9}{2}=36$; one variable $\geq6$: sum 1, $\binom{3}{2}=3$, times 3: 9. Answer $36-9=27$. |
| C8 | `$\dbinom{14}{2}-3\dbinom{4}{2}=91-18=73$` | combinations & permutations | Write each number as a 3-digit string $d_1d_2d_3$ with leading zeros allowed: need $d_1+d_2+d_3=12$, digits $0$--$9$. Unrestricted: $\binom{14}{2}=91$. Violations $d_i\geq10$: shift by 10, sum 2 remains: $\binom{4}{2}=6$, times 3 digits: 18. Two violations impossible ($\geq20>12$). Count: $91-18=73$. |
| D1 | `$D_4=9$` | factorials | \emph{Proof.} For $i=1,\ldots,4$ let $A_i$ be the set of placements with letter $i$ correct. Placements fixing a given set of $k$ letters number $(4-k)!$, and there are $\binom{4}{k}$ such sets, so by inclusion--exclusion $\|A_1\cup A_2\cup A_3\cup A_4\|=\binom41 3!-\binom42 2!+\binom43 1!-\binom44 0!=24-12+4-1=15$. Hence the placements with \emph{no} letter correct number $24-15=9$. $\square$ |
| D2 | `Proof below.` | bijections / grid paths | \emph{Proof (bijection with gap subsets).} Write $n$ as a row of $n$ stars. A composition of $n$ corresponds to choosing, independently for each of the $n-1$ gaps between adjacent stars, whether to place a bar there: the bars cut the row into ordered positive parts, and every composition arises from exactly one set of cuts. Choices: $2^{n-1}$. Since compositions $\leftrightarrow$ subsets of the gap set, the count is $2^{n-1}$. $\square$ |
| D3 | `$96$` | combinatorial counting | $360=2^3\cdot3^2\cdot5$, so remove multiples of 2, 3, 5 by inclusion--exclusion: $360-180-120-72+60+36+24-12=96$. Equivalently $360\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac15\right)=360\cdot\frac12\cdot\frac23\cdot\frac45=96$ --- the product form is the I--E sum factorised. |
| D4 | `$3^5-3\cdot2^5+3\cdot1^5=150$` | combinatorial counting | \emph{Proof.} Unrestricted assignments: $3^5=243$. For each club $c$ let $A_c$ be the assignments leaving $c$ empty; $\|A_c\|=2^5$, $\|A_c\cap A_{c'}\|=1^5$, and all three clubs empty is impossible. By inclusion--exclusion the assignments missing at least one club number $3\cdot2^5-3\cdot1=93$, so surjective assignments number $243-93=150$. $\square$ |
| D5 | `$10^6-1000-100+10=998\,910$` | combinatorial counting | Squares up to $10^6$: exactly $1000$ (namely $k^2$ for $k\leq10^3$). Cubes: $100$ (since $100^3=10^6$). The double-counted numbers are those that are both square and cube, i.e.\ sixth powers: $10$ of them ($k^6$, $k\leq10$). By inclusion--exclusion, squares-or-cubes number $1000+100-10=1090$; the rest number $10^6-1090=998\,910$. $\square$ |


#### Sheet 06

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$3$` | combinatorial counting | Worst case: one of each colour (2 socks). One more forces a match. |
| A2 | `$12$` | combinatorial counting | Worst case: all 10 white socks first, then 2 black. |
| A3 | `True` | combinatorial counting | 13 pigeons, 12 month-boxes. |
| A4 | `$8$` | combinatorial counting | 7 boxes, so 8 people. |
| A5 | `$3$` | combinatorial counting | Two parity boxes. |
| A6 | `$9$` | combinatorial counting | Each handshake is counted twice, once by each participant: $18/2$. |
| A7 | `True` | bijections / grid paths | Both equal the sum of every entry --- one grid, two reading orders. |
| A8 | `$6$` | combinatorial counting | Boxes are the residues mod 5; same residue $\Rightarrow$ difference divisible by 5. |
| A9 | `$4\cdot2+1=9$` | combinatorial counting | Worst case: 2 of every flavour (8 sweets); the ninth forces a third somewhere. |
| A10 | `True` | combinatorial counting | Two parity boxes, four integers --- some two share parity, and their difference is even. |
| B1 | `$7$` | combinatorial counting | Six diners can sit in alternate seats (construction: seats $1,3,5,7,9,11$), so 6 does not force adjacency. With 7 diners, pair the seats into 6 adjacent couples $\{1,2\},\{3,4\},\ldots,\{11,12\}$: seven diners in six couples put two in the same couple --- adjacent. Answer: 7. |
| B2 | `$8$` | combinatorial counting | Seven residue boxes mod 7. |
| B3 | `Pigeonhole on 4 residues; construction: $1,2,3,4,5$` | combinatorial counting | Mod 4 there are only 4 residues, so 5 integers repeat one; equal residues difference $\equiv0$. For the second part, any complete residue system mod 5 works: $1,2,3,4,5$ have all differences $1$--$4$ mod 5, never $0$. |
| B4 | `Yes; the smallest forcing size is $6$` | combinatorial counting | Pair the set into $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$: five boxes each summing to 11. Six chosen numbers land two in one box. Five numbers can dodge (take one from each pair, e.g.\ $1,2,3,4,5$). |
| B5 | `$\dbinom{8}{2}=28$ matches; each team plays $7$` | combinations & permutations | A match is a pair of teams. Per team: everyone else once. |
| B6 | `$42$` | combinatorial counting | Handshake lemma: each friendship contributes 2 to the total. |
| B7 | `Forced; largest safe choice has 3 elements, e.g.\ $\{1,3,5\}$` | combinatorial counting | Boxes $\{1,2\},\{3,4\},\{5,6\}$: four numbers in three boxes put two in one box, and box-mates are consecutive. The construction $\{1,3,5\}$ (or $\{2,4,6\}$, $\{1,4,6\}$, \ldots) shows 3 can dodge. |
| B8 | `Someone shaking all $n-1$ hands has shaken the non-shaker's hand --- contradiction.` | combinatorial counting | Possible counts are $0,1,\ldots,n-1$: that is $n$ boxes for $n$ people, so pigeonhole alone fails. But the extreme boxes are incompatible: a count of $n-1$ (shook everyone) and a count of $0$ (shook no one) cannot both occur. So at most $n-1$ counts are actually available for $n$ people --- pigeonhole now bites. |
| B9 | `At least $\lceil25/7\rceil=4$` | combinatorial counting | If every child had at most 3, the total would be at most $21<25$. Contradiction. |
| B10 | `$\dfrac{5\cdot4}{2}=10$` | combinations & permutations | Count (person, committee) memberships two ways: committees give $5\cdot4=20$; people give $2\cdot(\text{members})$. So members $=10$. |
| C1 | `Some colour: $3\cdot4+1=13$.\quad Five red: $20+4+1=25$.` | combinatorial counting | \emph{Some colour} is plain strong pigeonhole: worst case 4 of each (12 beads), the 13th forces a fifth. \emph{Five red} is adversarial: the drawer hands you all 10 green and 10 blue first (20 useless beads), then 4 red --- so 24 can still fail, and the 25th guarantees a fifth red. |
| C2 | `Forced at 7; construction for 6: $\{1,2,3,4,5,6\}$` | combinatorial counting | Boxes $\{1,12\},\{2,11\},\{3,10\},\{4,9\},\{5,8\},\{6,7\}$ --- six boxes each summing to 13. Seven numbers double up somewhere. Taking the smaller element of each pair ($1$--$6$) dodges with six numbers: all pair-sums are at most $11<13$. |
| C3 | `$11$` | combinatorial counting | Ten digit-boxes $0$--$9$. |
| C4 | `Impossible.` | combinatorial counting | Colour the board alternately. Opposite corners share a colour, so the mutilated board has 32 squares of one colour and 30 of the other. Every domino covers one square of each colour, so 31 dominoes cover 31 of each --- but $31\neq32$. No tiling exists. $\square$ |
| C5 | `$12\cdot7+1=85$` | combinatorial counting | The pigeonholes are (month, weekday) pairs: $12\times7=84$ boxes. With 85 people, two land in the same box --- same month AND same weekday. |
| C6 | `$\dfrac{20\cdot6}{3}=40$` | combinatorial counting | Memberships counted by clubs: 120. Counted by students: $3S$. So $S=40$. |
| C7 | `Some three adjacent numbers sum to at least 15.` | combinatorial counting | The nine positions split into three \emph{disjoint} blocks of three consecutive seats. The three block-sums total $1+2+\cdots+9=45$, so some block sums to at least $\lceil45/3\rceil=15$. $\square$ |
| C8 | `Forced.` | combinatorial counting | Boxes $\{1,5\},\{2,6\},\{3,7\},\{4,8\}$: four boxes whose mates differ by exactly 4. Five numbers put two in one box. $\square$ |
| D1 | `Proof below.` | combinatorial counting | \emph{Proof.} Divide the unit square into four closed $\frac12\times\frac12$ quarter-squares. Five points in four quarters: by the pigeonhole principle two points, say $P$ and $Q$, lie in the same quarter. Any two points of a $\frac12\times\frac12$ square are at distance at most its diagonal, $\frac{\sqrt2}{2}$. Hence $\|PQ\|\leq\frac{\sqrt2}{2}$. $\square$ |
| D2 | `Proof below.` | combinatorial counting | \emph{Proof.} Classify each point $(x,y)$ by the parities of its coordinates: (even, even), (even, odd), (odd, even), (odd, odd) --- four classes. Five points give two in the same class, say $P=(a,b)$ and $Q=(c,d)$ with $a\equiv c$ and $b\equiv d\pmod 2$. Then $a+c$ and $b+d$ are both even, so the midpoint $\left(\frac{a+c}{2},\frac{b+d}{2}\right)$ has integer coordinates. $\square$ |
| D3 | `Proof below.` | combinatorial counting | \emph{Proof.} Let the guests be the vertices of a graph, with an edge for each handshake; write $d(v)$ for the number of hands $v$ shook. Every handshake has two participants, so summing over all guests counts each handshake twice: $\sum_{v}d(v)=2H$, where $H$ is the total number of handshakes --- an even number. Split the sum by parity: $\sum_{d(v)\text{ even}}d(v)$ is even (a sum of even numbers), and the whole sum is even, so $\sum_{d(v)\text{ odd}}d(v)$ is even too. But that last sum is a sum of odd numbers, and a sum of odd numbers is even only when there is an even count of them. Hence the number of guests with an odd handshake count is even. $\square$ |
| D4 | `Proof below; some pair chosen by $\geq2$ students (in fact $\geq\lceil20/10\rceil=2$).` | combinatorial counting | \emph{Proof.} Each student's choice of two problems from five is an unordered pair, and there are exactly $\binom{5}{2}=10$ such pairs. Regard the 10 pairs as pigeonholes and the 20 students as pigeons. Since $20>10$, by the pigeonhole principle some pigeonhole holds at least two students --- that is, some pair of problems was chosen by at least two students, who therefore solved exactly the same pair. (Strong pigeonhole sharpens this: at least $\lceil20/10\rceil=2$ share the most popular pair, and averaging shows some pair is chosen by at least 2 regardless of the distribution.) $\square$ |
| D5 | `Proof below.` | combinatorial counting | \emph{Proof.} Fix a person $X$. The other five people split into friends of $X$ and strangers to $X$; by pigeonhole one class contains at least $\lceil5/2\rceil=3$ people --- say (without loss of generality) $A,B,C$ are all friends of $X$. Now examine the three relations among $A,B,C$: if any pair, say $A$ and $B$, are friends, then $X,A,B$ are three mutual friends. Otherwise all three pairs among $A,B,C$ are strangers, and $A,B,C$ are three mutual strangers. Either way the claim holds. (If the majority class was strangers, the same argument runs with roles swapped.) $\square$ |


#### Sheet 07

| Question ID | Answer (`\ans{...}`) | Math Type | Checkable Method Claims (`\method{...}`) |
|---|---|---|---|
| A1 | `$5$` | combinatorial counting | Ways to reach step $n$: $f(n)=f(n-1)+f(n-2)$ (last move was a 1 or a 2). With $f(1)=1$, $f(2)=2$: $1,2,3,5$. |
| A2 | `$8$` | combinatorial counting | Continue the sequence one step: $f(5)=f(4)+f(3)=5+3=8$. |
| A3 | `$8$` | combinatorial counting | Let $g(n)$ count them. A valid string ends in 0 (then $g(n-1)$ ways) or in 01 (then $g(n-2)$): $g(n)=g(n-1)+g(n-2)$, with $g(1)=2$, $g(2)=3$. So $2,3,5,8$. |
| A4 | `$3$` | combinatorial counting | Tilings of $2\times n$: the last column is one vertical domino ($t(n-1)$) or two horizontals filling two columns ($t(n-2)$): $t(n)=t(n-1)+t(n-2)$, $t(1)=1$, $t(2)=2$. So $1,2,3$. |
| A5 | `$5$` | combinatorial counting | $t(4)=t(3)+t(2)=3+2=5$. |
| A6 | `$7$` | combinatorial counting | Each new line crosses all previous ones and gains (number of lines already present)$+1$ new regions: $R(n)=R(n-1)+n$, $R(0)=1$. So $1,2,4,7$. |
| A7 | `$5$` | combinatorial counting | The Catalan number $C_3=5$: \texttt{((()))}, \texttt{(()())}, \texttt{(())()}, \texttt{()(())}, \texttt{()()()}. |
| A8 | `$15$` | combinatorial counting | $1\to3\to7\to15$. (Each term is one less than a power of 2.) |
| A9 | `$21$` | combinatorial counting | $1,1,2,3,5,8,13,21$. |
| A10 | `True` | combinatorial counting | $1{+}1{+}2{+}3{+}5{+}8{+}13{+}21=54$. Also $F_{10}-1=55-1=54$. |
| B1 | `$89$` | combinatorial counting | Run $f(n)=f(n-1)+f(n-2)$ to $n=10$: $\ldots,55,89$. That is $F_{11}$. |
| B2 | `$55$` | combinatorial counting | $g(n)=g(n-1)+g(n-2)$, $g(1)=2,g(2)=3$: $\ldots,34,55$. ($g(n)=F_{n+2}$.) |
| B3 | `$89$` | combinatorial counting | $t(n)=F_{n+1}$, so $t(10)=F_{11}=89$. |
| B4 | `$56$` | combinatorial counting | $R(n)=1+\binom{n+1}{2}=1+\binom{11}{2}=1+55=56$. |
| B5 | `$41$` | combinatorial counting | $2\to5\to14\to41$. |
| B6 | `$24$` | combinatorial counting | Tribonacci: $f(n)=f(n-1)+f(n-2)+f(n-3)$, $f(1)=1,f(2)=2,f(3)=4$. So $1,2,4,7,13,24$. |
| B7 | `$16$` | combinatorial counting | Regions $=1+\binom{n}{2}+\binom{n}{4}$: with $n=5$, $1+10+5=16$. |
| B8 | `$23$` | inclusion-exclusion | Invariant: each snap turns one piece into two, so the number of pieces rises by exactly 1 per snap. Starting at 1 piece and ending at 24 needs $24-1=23$ snaps --- \emph{regardless} of the order or pattern of breaks. |
| B9 | `$63$` | combinatorial counting | $H(n)=2H(n-1)+1$ (move $n-1$ disks off, move the big one, move them back), $H(1)=1$: $1,3,7,15,31,63$. So $H(n)=2^n-1$. |
| B10 | `$372$` | combinatorial counting | Subtract two prefix sums: $F_4+\cdots+F_{12}=(F_1+\cdots+F_{12})-(F_1+F_2+F_3)=(F_{14}-1)-(F_5-1)=F_{14}-F_5=377-5=372$. |
| C1 | `$19$` | combinatorial counting | Track the last step: let $b(n)$ end in a 1-step, $c(n)$ end in a 2-step. A 1-step may follow anything: $b(n)=b(n-1)+c(n-1)$. A 2-step may not follow a 2-step: $c(n)=b(n-2)$. Building up to $n=8$ gives total $b(8)+c(8)=19$. |
| C2 | `$43$` | combinatorial counting | Fill left to right: a vertical domino advances 1 column ($a_{n-1}$); two horizontal dominoes or one $2\times2$ square advance 2 columns (2 ways, $2a_{n-2}$). So $a_n=a_{n-1}+2a_{n-2}$, $a_0=a_1=1$: $1,1,3,5,11,21,43$. |
| C3 | `$C_4=14$` | bijections / grid paths | These are \emph{Dyck paths}; they are counted by the Catalan number $C_4=\frac{1}{5}\binom{8}{4}=\frac{70}{5}=14$. (Reflection principle: all $\binom{8}{4}=70$ paths minus the $\binom{8}{3}=56$ that cross the diagonal.) |
| C4 | `$31$` | combinatorial counting | $1+\binom62+\binom64=1+15+15=31$. Each interior crossing (a $\binom{n}{4}$: one per 4 points, sheet 2 D5) adds one region beyond the $1+\binom{n}{2}$ that chords alone would give. |
| C5 | `$21$` | factorials | Let $d(n)$ count compositions of $n$ into odd parts. Peeling the first part (odd) gives $d(n)=d(n-1)+d(n-3)+d(n-5)+\cdots$; simplifying, $d(n)=d(n-1)+d(n-2)$ --- Fibonacci again! With $d(1)=1,d(2)=1$: $\ldots,13,21$, so $d(8)=21=F_8$. |
| C6 | `$448$` | combinatorial counting | Two-state recurrence on the last symbol. Let $z(n)$ count valid strings ending in 0 and $w(n)$ those ending in 1 or 2. A 0 may follow only a non-0: $z(n)=w(n-1)$. A 1 or 2 may follow anything, in 2 ways: $w(n)=2\bigl(z(n-1)+w(n-1)\bigr)$. Writing $a_n=z(n)+w(n)$ for the total gives $a_n=2a_{n-1}+2a_{n-2}$, seeded $a_1=3$, $a_2=8$: $3,8,22,60,164,448$. |
| C7 | `$11$` | bijections / grid paths | Odd-width strips need a genuine transfer-matrix (column-state) recurrence rather than a two-term one; carrying the profile of filled cells column by column yields $11$. (The $3\times n$ tiling counts run $1,3,11,41,153,\ldots$, satisfying $a_n=4a_{n-1}-a_{n-2}$.) |
| C8 | `$504$` | combinatorial counting | State $=$ number of 1s currently at the end (0, 1, or 2). A valid string of length $n$ ends in 0, in one trailing 1, or in two: summing gives $h(n)=h(n-1)+h(n-2)+h(n-3)$ (tribonacci), seeded $h(1)=2,h(2)=4,h(3)=7$. Running to $n=10$: $\ldots,274,504$. |
| D1 | `$a_6=13$` | combinatorial counting | \emph{Proof.} Consider where $n$ is sent. Since $\|p(n)-n\|\leq1$, either $p(n)=n$ or $p(n)=n-1$. \emph{Case $p(n)=n$:} the restriction of $p$ to $\{1,\ldots,n-1\}$ is any valid permutation of that set, giving $a_{n-1}$ possibilities. \emph{Case $p(n)=n-1$:} then some $i$ has $p(i)=n$, and $\|i-n\|\leq1$ forces $i=n-1$, so $p(n-1)=n$. Thus $n$ and $n-1$ are swapped, and $p$ restricted to $\{1,\ldots,n-2\}$ is any valid permutation: $a_{n-2}$ possibilities. The cases are disjoint and exhaustive, so $a_n=a_{n-1}+a_{n-2}$. With $a_1=1$, $a_2=2$ we get $1,2,3,5,8,13$, so $a_6=13$. $\square$ |
| D2 | `Proof below.` | combinatorial counting | \emph{Proof (parity invariant).} Track the parity of the sum $S$ of all numbers on the board. Replacing $a$ and $b$ by $\|a-b\|$ changes the sum by $\|a-b\|-(a+b)=-2\min(a,b)$, an even number. So $S\bmod 2$ never changes --- it is an \emph{invariant}. Initially $S=1+2+\cdots+10=55$, which is odd. When one number remains it equals $S$, whose parity is still odd; hence the final number is odd. $\square$ |
| D3 | `$C_4=14$` | combinatorial counting | \emph{Proof.} Let $T_n$ be the number of triangulations of a convex $(n{+}2)$-gon; we show $T_n=C_n$, the Catalan number. Fix the edge $AB$ of the polygon. In any triangulation, $AB$ lies in exactly one triangle $ABX$ for some other vertex $X$. That triangle splits the polygon into a smaller polygon on one side of $AX$ (with $i+2$ vertices) and another on the side of $XB$ (with $n-i+1$ vertices), each independently triangulated. Summing over the position of $X$ gives $T_n=\sum_{i=0}^{n-1}T_iT_{n-1-i}$ --- the Catalan recurrence, with $T_0=1$. Hence $T_n=C_n$; for a hexagon $n=4$ and $C_4=\frac{1}{5}\binom{8}{4}=14$. $\square$ |
| D4 | `Proof below (induction).` | combinatorial counting | \emph{Proof by induction on $n$.} \emph{Base $n=1$:} a $2\times2$ board with one square removed is exactly a single L-tromino. \emph{Step:} assume every $2^{n-1}\times2^{n-1}$ board with one square removed can be tiled. Given a $2^n\times2^n$ board with one square missing, cut it into four $2^{n-1}\times2^{n-1}$ quadrants. The missing square lies in one quadrant. Place one L-tromino at the centre covering one corner square from each of the \emph{other three} quadrants. Now every quadrant has exactly one square unavailable (the genuinely missing one, or the centre corner just covered), so by the inductive hypothesis each quadrant can be tiled. Together with the central tromino this tiles the whole board. $\square$ |
| D5 | `The second player.` | combinatorial counting | \emph{Proof.} Call a position (the number of stones the mover faces) \emph{losing} if the mover loses under optimal play; we claim the losing positions are exactly the multiples of 3. The key fact is that \emph{no power of 2 is divisible by 3}: since $2\equiv-1\pmod3$, we have $2^k\equiv(-1)^k\equiv\pm1\pmod3$, never $0$. \emph{From a multiple of 3:} subtracting any power of 2 (residue $\pm1$) leaves a non-multiple of 3 --- the mover cannot avoid handing the opponent a non-multiple. \emph{From a non-multiple of 3:} the mover removes 1 stone (if the residue is 1) or 2 stones (if the residue is 2) --- both are powers of 2 --- reaching a multiple of 3. Since position $0$ is losing, induction gives that the losing positions are precisely $0,3,6,\ldots$. As $2025=3\times675$ is a multiple of 3, the first player faces a losing position, so the \textbf{second} player wins by always restoring the pile to a multiple of 3. $\square$ |

