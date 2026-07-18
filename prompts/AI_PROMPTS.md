# Speed Maths AI Workflow & Prompts

If you are using a standard web interface (like ChatGPT or Claude.ai) to contribute to this project, **the AI cannot see the repository**. If you ask it to generate 33 questions and answers at the same time, it will hallucinate, truncate, and break the strict structural rules of the repository.

To prevent this, you must split the generation into **three distinct turns**, and you must provide it with **real repository samples** so it knows exactly what to mimic.

---

## Turn 1: Generating the Questions
Open a new chat. Your goal is to generate ONLY the questions first. Do not ask for answers yet.

**Copy & Paste this Prompt:**
> I am writing a math worksheet for the open-source Speed Maths project. The target competition is [TMUA / MAT / SMC / BMO1]. 
> Please generate a new [Algebra / Combinatorics / Number Theory / Geometry] sheet. 
> 
> **Crucial Rule:** For this first step, output ONLY the main sheet (the questions). Do NOT output the answers yet.
> 
> **Structural Rules:**
> Generate exactly 33 questions split into:
> - `\section*{Section A \quad Rapid Recognition \hfill{\normalfont\small($\leq$15\,s each)}}`: 10 questions
> - `\section*{Section B \quad Manipulation Drills \hfill{\normalfont\small($\leq$50\,s each)}}`: 10 questions
> - `\section*{Section C \quad Substitution \& Structure \hfill{\normalfont\small($\leq$90\,s each)}}`: 8 questions
> - `\section*{Section D \quad Challenge \hfill{\normalfont\small(BMO1 difficulty)}}`: 5 questions
> 
> The document must EXACTLY match the structure, styling, and pacing of this complete sample sheet:
> 
> ```latex
> \documentclass[11pt,a4paper]{article}
> \input{../../shared/preamble}
> \SpeedHeader{Algebra}{1}
> 
> \begin{document}
> 
> \SpeedTitleBlock{Daily Algebra Drill \#1}{David Akinyele-Aje}
> \noindent\textit{New toolkit today: Difference / Sum of Squares \& Cubes $\cdot$ Newton's Identity Chain $\cdot$ Disguised Quadratics $\cdot$ Telescoping \& Partial Fractions.}
> 
> \vspace{2pt}
> \noindent\textit{Attempt each question before checking answers. Time yourself. No calculators.}
> 
> \section*{Section A \quad Rapid Recognition \hfill{\normalfont\small($\leq$15 s each)}}
> % ══════════════════════════════════════════════════════════════════════════════
> 
> \noindent\textit{Factorise, simplify, or evaluate. No expansion. Pure recognition.}
> 
> \begin{enumerate}
> 
> \item Factorise completely: $\;x^4 - 16$.
> 
> \item Simplify: $\;\dfrac{a^2 - b^2}{a^2 + 2ab + b^2}$.
> 
> \item Without expanding, evaluate: $\;103^2 - 97^2$.
> 
> \item Factorise: $\;2x^2 + 7x - 15$.
> 
> \item Simplify: $\;\left(x + \dfrac{1}{x}\right)^2 - \left(x - \dfrac{1}{x}\right)^2$.
> 
> \item Factorise: $\;x^3 + 8$.
> 
> \item Simplify: $\;\dfrac{x^2 - 5x + 6}{x^2 - 4}$.
> 
> \item Given $a + b = 5$ and $ab = 3$, find $a^2 + b^2$.
> 
> \item Factorise: $\;4x^2 - 12x + 9$.
> 
> \item Simplify: $\;\dfrac{1}{1\cdot2}+\dfrac{1}{2\cdot3}+\dfrac{1}{3\cdot4}+\cdots+\dfrac{1}{9\cdot10}$.
> 
> \end{enumerate}
> 
> % ══════════════════════════════════════════════════════════════════════════════
> \section*{Section B \quad Manipulation Drills \hfill{\normalfont\small($\leq$50 s each)}}
> % ══════════════════════════════════════════════════════════════════════════════
> 
> \noindent\textit{Algebraic fractions, rearranging, hidden structure. Resist the urge to expand.}
> 
> \begin{enumerate}
> 
> \item Simplify: $\;\dfrac{x^3 - 1}{x^2 - 1}$.
> 
> \item Simplify: $\;\dfrac{1}{x-1} - \dfrac{2}{x^2-1}$.
> 
> \item Make $x$ the subject: $\;\dfrac{x+a}{x-a} = k$ \quad ($k\neq 1$).
> 
> \item Given that $a+b+c=0$, express $\;(a+b)(b+c)(c+a)\;$ in terms of $abc$.
> 
> \item Simplify $\;\dfrac{x^2+3x+2}{x^2-x-2}$ and state all values of $x$ for which the original expression is undefined.
> 
> \item Simplify: $\;\left(\dfrac{x^2}{y} - \dfrac{y^2}{x}\right)\div\left(\dfrac{x}{y}+1+\dfrac{y}{x}\right)$.
> 
> \item Factorise: $\;a^2(b-c)+b^2(c-a)+c^2(a-b)$.
> 
> \item Solve for $x$: $\;\dfrac{3}{x+1}+\dfrac{4}{x+2} = \dfrac{11}{(x+1)(x+2)}$.
> 
> \item Simplify: $\;\dfrac{2^{n+2}+2^n}{2^{n+1}+2^{n-1}}$.
> 
> \item Given $p + q = 7$ and $p^3 + q^3 = 133$, find $pq$.
> 
> \end{enumerate}
> 
> % ══════════════════════════════════════════════════════════════════════════════
> \section*{Section C \quad Substitution \& Structure \hfill{\normalfont\small($\leq$90 s each)}}
> % ══════════════════════════════════════════════════════════════════════════════
> 
> \noindent\textit{Look for symmetry, disguised quadratics, and useful substitutions before computing.}
> 
> \begin{enumerate}
> 
> \item Solve: $\;x^4 - 5x^2 + 4 = 0$.
> 
> \item Given $x + \dfrac{1}{x} = 3$, find $x^3 + \dfrac{1}{x^3}$.
> 
> \item Find all real solutions to: $\;(x^2 - 3x)^2 - 2(x^2-3x) - 8 = 0$.
> 
> \item Simplify: $\;\dfrac{x^2 + y^2}{xy} - \dfrac{(x-y)^2}{xy}$.
> 
> \item Factorise $\;x^4 + 4y^4\;$ over the integers.
> 
> \item Given $\sqrt{2x+1}+\sqrt{2x-1} = t$ with $t > 0$, find $x$ in terms of $t$.
> 
> \item Given $a + b + c = 0$, evaluate $\;\dfrac{a^2}{bc}+\dfrac{b^2}{ca}+\dfrac{c^2}{ab}$.
> 
> \item Solve the system: $\;x + y = 5,\quad x^2 + y^2 = 17$.
> 
> \end{enumerate}
> 
> % ══════════════════════════════════════════════════════════════════════════════
> \section*{Section D \quad Challenge \hfill{\normalfont\small(TMUA / SMC difficulty)}}
> % ══════════════════════════════════════════════════════════════════════════════
> 
> \noindent\textit{Insight over computation. Each question has a short, elegant solution --- find it.}
> 
> \begin{enumerate}
> 
> \item Find the value of
> \[
>   \frac{(2025)^3 - (2024)^3 - (2023)^3 + (2022)^3}{(2025)^2-(2022)^2}.
> \]
> 
> \item Let $f(x) = \dfrac{x}{x+1}$. Define $f^n$ as $f$ composed with itself $n$ times.
>       Find a closed form for $f^n(x)$ and hence compute $f^{2025}(1)$.
> 
> \item Positive reals $a, b, c$ satisfy $abc = 1$. Simplify:
> \[
>   \frac{1}{1+a+ab}+\frac{1}{1+b+bc}+\frac{1}{1+c+ca}.
> \]
> 
> \item Without solving for $x$, find $x^2 + \dfrac{1}{x^2}$ given $x - \dfrac{1}{x} = \sqrt{5}$.
>       Hence find $x^4 + \dfrac{1}{x^4}$.
> 
> \item Find all integers $n$ such that $n^2 + 4n + 3$ is a perfect square.
> 
> \end{enumerate}
> 
> \SpeedClosing{``Speed comes from recognition, not from rushing.
> Every shortcut is a pattern you have internalised.''}
> 
> \end{document}
> ```
> 
> **Mathematical Rules:**
> 1. No calculators. Numbers must cancel cleanly or telescope elegantly.
> 2. Content MUST be strictly grounded in the TMUA, MAT, SMC, or BMO1 specifications. DO NOT use university-level math (e.g., explicitly ban Euler's Totient function, Wilson's Theorem, Fermat's Little Theorem, etc.). Rely entirely on the creative use of school-level syllabuses (e.g., divisibility rules, last digits, logic puzzles, basic Diophantine equations).
> 3. **Corpus Grounding (Agentic Workflows):** If you are an AI agent with filesystem access, you MUST read the `INDEX-*.md` and `txt/` files in the local `research/` directory before writing. Each sheet's question archetypes must be ones that actually occur in the corpus for its target competition (Sections A/B ↔ TMUA/SMC-early, Section C ↔ SMC-mid, Section D ↔ SMC-late/BMO1).
> 4. **Archetype Referencing:** When you base a question on a specific archetype from the corpus (especially in Sections C and D), you MUST append a reference to the end of the question text in italics, like this: `\textit{\small(after SMC 2022 Q3)}`. Furthermore, in the corresponding `\inv{}` block in the answer key, explicitly discuss how your question compares to or builds upon the original archetype.

*(Manual Step: Copy the output into `[pillar]/sheets/sheetXX.tex`)*

---

## Turn 2: Generating the Answers
Now that the AI has the context of the 33 questions, ask it to generate the Answer Key file.

**Copy & Paste this Prompt:**
> Perfect. Now generate the Answer Key file for those exactly 33 questions. 
> 
> **Crucial Rule:** For every single question, you MUST mimic this exact structural sample pulled from the repository:
> 
> ```latex
> %── A1 ──────────────────────────────────────────────────────────────────────────
> \item Factorise completely: $\;x^4 - 16$.
> 
> \ans{$(x^2+4)(x+2)(x-2)$}
> \method{Apply the difference of two squares twice: $(x^2)^2 - 4^2 = (x^2+4)(x^2-4) = (x^2+4)(x+2)(x-2)$.}
> \inv{Can you factorise $x^4+16$ over the real numbers? Hint: Add and subtract $8x^2$ to complete the square, creating a hidden difference of squares.}
> ```
> 
> Make sure your `\method{}` explicitly states intermediate factual/numeric claims so they can be computationally verified later. Output the full file for all 33 questions.

*(Manual Step: Copy the output into `[pillar]/answers/ansXX.tex`)*

---

## Turn 3: Writing Verification Scripts
*Crucial Rule: You must open a **fresh, new chat window** to write the verification script. The AI checking the answer must not have the memory of drafting it, so it is forced to do independent math!*

**Copy & Paste this Prompt:**
> You are verifying a mathematical worksheet for the Speed Maths project.
> I have a question labeled `[Question ID, e.g., A1]` with the following answer and method:
> 
> **[PASTE THE \ans{} AND \method{} TEXT HERE]**
>
> Please write a Python test function named `def check_[Question ID]():` that computationally verifies this answer.
> 
> **Rules:**
> 1. Use ONLY the Python Standard Library. No external packages.
> 2. Independently re-derive the `\ans{}` value using brute force, dynamic programming, or random sampling.
> 3. You MUST mimic this exact structural sample from the repository. Note the exact docstring required:
> 
> ```python
> # A2
> def check_A2():
>     """ SAMPLED CHECK: Random rational testing """
>     for _ in range(50):
>         a = fractions.Fraction(random.randint(-10, 10), random.randint(1, 10))
>         b = fractions.Fraction(random.randint(-10, 10), random.randint(1, 10))
>         if a + b != 0:
>             assert (a**2 - b**2) / (a**2 + 2*a*b + b**2) == (a - b) / (a + b)
> ```
> *(Use `"""EXHAUSTIVE PROOF"""` if you do not use sampling).*

*(Manual Step: Copy the Python function and append it to `[pillar]/verify/sheetXX_verify.py`)*
