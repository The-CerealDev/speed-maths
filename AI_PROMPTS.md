# Speed Maths AI Workflow & Prompts

Because this project mandates strict computational verification for every mathematical question, we heavily encourage using AI to do the heavy lifting! 

If you are using a standard web interface (like ChatGPT or Claude.ai) rather than a CLI coding agent, the AI cannot "see" our repository. You must feed it the exact structural rules so it formats the LaTeX correctly. Follow the workflow below.

## 1. Drafting Questions (Agent 1)
Open a new chat in your web browser. Use this "Killer Prompt" to draft a new sheet with perfect structural compliance.

**Copy & Paste this Prompt:**
> I am writing a math worksheet for the open-source Speed Maths project. The target competition is [TMUA / MAT / SMC / BMO1]. 
> Please generate a new [Algebra / Combinatorics / Number Theory / Geometry] sheet. 
> 
> **Structural Rules:**
> 1. You must generate exactly 33 questions split into four sections:
>    - `\section*{A — Rapid Recognition}`: 10 questions (Foundational, easy)
>    - `\section*{B — Manipulation Drills}`: 10 questions (Direct application)
>    - `\section*{C — Substitution & Structure}`: 8 questions (Harder, requires case splits or insight)
>    - `\section*{D — Challenge (SMC / BMO1 difficulty)}`: 5 questions (Hardest, proof-heavy). *Note: The section title must include this difficulty tag!*
> 2. The document must start exactly like this:
>    `\documentclass[11pt,a4paper]{article}`
>    `\input{../../shared/preamble}`
>    `\SpeedHeader{<Pillar Name>}{<Sheet Number>}`
>    `\begin{document}`
>    `\SpeedTitleBlock{Daily <Pillar> Drill \#<N>}{<Your Name>}`
> 
> **Mathematical Rules:**
> 1. Do not use a calculator. Numbers must cancel cleanly or telescope elegantly.
> 2. Do not output the answers inside the main sheet file. 
> 3. Provide a separate "Answers" output. For every question, you MUST provide:
>    - `\ans{...}`: Just the final answer.
>    - `\method{...}`: A fast, competition-style method. **State intermediate factual/numeric claims clearly** (e.g. "x factors to (y)(z)") so they can be computationally verified by a Python script later.
>    - `\inv{...}`: An extension or generalization.

**Your manual step:** 
1. Copy the LaTeX question output and paste it into `[pillar]/sheets/sheet01.tex`. 
2. Copy the Answers output and paste it into `[pillar]/answers/ans01.tex`.
3. Compile both PDFs locally by running `pdflatex sheet01.tex` and `pdflatex ans01.tex` to make sure they look right.

---

## 2. Writing Verification Scripts (Agent 2)
*Crucial Rule: You must open a **fresh, new chat window** to write the verification script. The AI checking the answer must not have the memory of drafting it!*

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
> 3. You MUST `assert` every single checkable factual or numeric claim made in the `\method{}` text.
> 4. Add a docstring to the top of the function that is EXACTLY either `"""EXHAUSTIVE PROOF"""` or `"""SAMPLED CHECK"""`. Do not use any other phrasing.
> 
> Output the raw Python function.

**Your manual step:** 
1. Copy the Python function and append it to `[pillar]/verify/sheet01_verify.py`.
2. Open your local terminal and run the test: `python3 <pillar>/verify/run_all.py`
3. **The Feedback Loop:** If the script fails, copy the error from your terminal and paste it back into your chat so the AI can fix the script (or point out if the math itself is actually wrong!).
4. Run `python3 tools/validate_verify_scripts.py` right before opening your Pull Request.
