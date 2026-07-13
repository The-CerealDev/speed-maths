# Speed Maths AI Workflow & Prompts

Because this project mandates strict computational verification for every mathematical question, we heavily encourage using AI agents to do the heavy lifting! If you aren't a Python expert or just want to speed up question generation, use the prompts below.

## 1. Drafting Questions (Agent 1)
Use this prompt with an AI like Claude, ChatGPT, or Gemini to draft a new question based on the competition style.

**Copy & Paste this Prompt:**
> I am writing a math worksheet for the open-source Speed Maths project. The target competition is [TMUA / MAT / SMC / BMO1]. 
> Please generate a new [Algebra / Combinatorics / Number Theory / Geometry] question that fits Section [A (Easy) / B (Manipulation) / C (Structure) / D (Hard)]. 
> 
> **Rules:**
> 1. Do not use a calculator. The numbers must cancel cleanly or telescope elegantly.
> 2. Output the LaTeX question text.
> 3. Provide the final answer in an `\ans{...}` block.
> 4. Provide a fast, competition-style method in a `\method{...}` block. State intermediate factual claims clearly so they can be computationally verified later.
> 5. Provide an extension or generalization in an `\inv{...}` block.

---

## 2. Writing Verification Scripts (Agent 2)
*Crucial Rule: You must use a **fresh** AI conversation to write the verification script. The AI checking the answer must not be the same one that wrote it!*

**Copy & Paste this Prompt:**
> You are verifying a mathematical worksheet for the Speed Maths project.
> I have a question labeled `[Question ID, e.g., A1]` with the following answer and method:
> 
> **[PASTE THE \ans{} AND \method{} TEXT HERE]**
>
> Please write a Python test function named `def check_[Question ID]():` that computationally verifies this answer.
> 
> **Rules:**
> 1. Use ONLY the Python Standard Library.
> 2. Independently re-derive the `\ans{}` value using brute force, dynamic programming, or random sampling.
> 3. You MUST `assert` every single checkable factual or numeric claim made in the `\method{}` text.
> 4. Add a docstring to the top of the function that is EXACTLY either `"""EXHAUSTIVE PROOF"""` or `"""SAMPLED CHECK"""`. Do not use any other phrasing (like "Monte Carlo Proof").
> 
> Output the raw Python function.
