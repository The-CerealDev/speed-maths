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
> The document must start exactly like this:
> ```latex
> \documentclass[11pt,a4paper]{article}
> \input{../../shared/preamble}
> \SpeedHeader{<Pillar>}{<Sheet Number>}
> \begin{document}
> \SpeedTitleBlock{Daily <Pillar> Drill \#<N>}{<Your Name>}
> ```
> 
> **Mathematical Rules:**
> No calculators. Numbers must cancel cleanly or telescope elegantly.

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
