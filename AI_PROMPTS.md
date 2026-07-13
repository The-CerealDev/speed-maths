# Speed Maths AI Workflow & Prompts

Because this project mandates strict computational verification for every mathematical question, we heavily encourage using AI to do the heavy lifting! 

If you are using a standard web interface (like ChatGPT or Claude.ai) rather than a CLI coding agent, you will need to manually copy the generated code into your local files and run the tests yourself. Follow the workflow and prompts below.

## 1. Drafting Questions (Agent 1)
Open a new chat in your web browser. Use this prompt to draft a new question.

**Copy & Paste this Prompt:**
> I am writing a math worksheet for the open-source Speed Maths project https://github.com/The-CerealDev/speed-maths . The target competition is [TMUA / MAT / SMC / BMO1]. 
> Look at the Existing context in that repo 
> Please generate a new [Algebra / Combinatorics / Number Theory / Geometry] question that fits Section [A (Easy) / B (Manipulation) / C (Structure) / D (Hard)]. 
> 
> **Rules:**
> 1. Do not use a calculator. The numbers must cancel cleanly or telescope elegantly.
> 2. Output the LaTeX question text.
> 3. Provide the final answer in an `\ans{...}` block.
> 4. Provide a fast, competition-style method in a `\method{...}` block. State intermediate factual claims clearly so they can be computationally verified later.
> 5. Provide an extension or generalization in an `\inv{...}` block.

**Your manual step:** 
1. Copy the LaTeX output and paste it into the appropriate worksheet file (e.g., `number-theory/sheets/sheet01.tex`) and answer file (e.g., `number-theory/answers/ans01.tex`). 
2. Compile the PDF locally by running `pdflatex sheet01.tex` inside the folder to make sure it looks right.

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
> 1. Use ONLY the Python Standard Library.
> 2. Independently re-derive the `\ans{}` value using brute force, dynamic programming, or random sampling.
> 3. You MUST `assert` every single checkable factual or numeric claim made in the `\method{}` text.
> 4. Add a docstring to the top of the function that is EXACTLY either `"""EXHAUSTIVE PROOF"""` or `"""SAMPLED CHECK"""`. Do not use any other phrasing.
> 
> Output the raw Python function.

**Your manual step:** 
1. Copy the Python function and append it to the appropriate verify script (e.g., `number-theory/verify/sheet01_verify.py`).
2. Open your local terminal and run the test: `python3 <pillar>/verify/run_all.py`
3. **The Feedback Loop:** If the script fails or throws an assertion error, copy the error from your terminal and paste it back into your chat so the AI can fix the script (or point out if the math itself is actually wrong!).
4. Run `python3 tools/validate_verify_scripts.py` right before opening your Pull Request to ensure your formatting is perfectly compliant.
