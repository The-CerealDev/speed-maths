# Geometry Pillar — Contributor Guide & Walkthrough

Welcome to the **Geometry Pillar** of Speed Maths! This guide provides a step-by-step playbook for contributors and AI agents to draft, verify, compile, and publish worksheets for this pillar.

Before starting, read:
1. [`geometry/PLAN.md`](PLAN.md) — The 7-day progression arc, topic syllabus, and cross-pillar territory map.
2. [`research/INDEX-tmua-geometry.md`](../research/INDEX-tmua-geometry.md) — The dedicated database of 300+ competition geometry questions mapped to real papers.
3. [`CONTRIBUTING.md`](../CONTRIBUTING.md) — The repo-wide verification, citation, and copyright guidelines.

---

## 1. Quickstart & Environment Setup

Ensure your local environment has the required Python tools and TeX Live packages:

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Install dependencies (SymPy, Hypothesis, pytest, etc.)
pip install -r requirements-dev.txt

# 3. Verify that pdflatex and python are accessible
pdflatex --version
python3 --version
```

---

## 2. Directory Structure

Work in the `geometry/` directory following this layout:

```
geometry/
├── README.md               <-- This guide
├── PLAN.md                 <-- 7-Day arc, syllabus, and anchors
├── sheets/
│   ├── sheet01.tex         <-- LaTeX source for Worksheet 1
│   ├── sheet01.pdf         <-- Compiled PDF
│   └── ...                 <-- sheet02.tex through sheet07.tex
├── answers/
│   ├── ans01.tex           <-- LaTeX source for Answer Sheet 1
│   ├── ans01.pdf           <-- Compiled PDF
│   └── ...                 <-- ans02.tex through ans07.tex
├── verify/
│   ├── run_all.py          <-- Pillar test runner (all 7 scripts)
│   ├── sheet01_verify.py   <-- Verification script (33 checks)
│   └── ...                 <-- sheet02_verify.py through sheet07_verify.py
└── vault/
    └── scrapped-*.md       <-- Scrapped draft questions (never delete old drafts)
```

---

## 3. Step-by-Step Workflow for Each Day

For each day $N \in \{1, 2, \dots, 7\}$, follow these 6 steps in order:

### Step 1: Select Grounded Archetypes from the Index
Open [`research/INDEX-tmua-geometry.md`](../research/INDEX-tmua-geometry.md) and [`geometry/PLAN.md`](PLAN.md). Select the target question archetypes for Day $N$.
- **Citation Format:** Credit adapted past-paper problems directly in the question line:
  `\textit{\small(after SMC 2023 Q15)}` or `\textit{\small(after TMUA Practice Paper 1 Q8)}`.
- **Naming Rule:** Never cite "TMUA 2016" (those files are identical to the TMUA Practice Paper; cite as "TMUA Practice Paper 1/2").
- **Copyright Rule:** **Never copy questions verbatim.** Adapt the structure, modify dimensions/coordinates, and preserve clean mental-math calculations.

### Step 2: Draft the Worksheet (`geometry/sheets/sheet0N.tex`)
Create `geometry/sheets/sheet0N.tex` using the standard template:

```latex
\documentclass[11pt,a4paper]{article}
\input{../../shared/preamble}

\SpeedHeader{Geometry}{1}

\begin{document}

\SpeedTitleBlock{Daily Geometry Drill \#1}{Your Name}

\SpeedMeta{
  pillar = Geometry,
  day = 1,
  title = Coordinate Lines \& Polygon Areas,
  tags = {coordinates, gradients, perpendicular-bisectors, shoelace-area},
  questions = 33,
  time = 35 minutes
}

\section*{Section A \quad Rapid Recognition \hfill \normalfont\small\textit{10 questions, 2:30}}
\begin{enumerate}
  \item Find the gradient of the line perpendicular to $3x - 4y + 12 = 0$.
  % ... items 2 to 10 (Strictly Non-MCQ)
\end{enumerate}

\section*{Section B \quad Manipulation Drills \hfill \normalfont\small\textit{10 questions, 8 minutes}}
\begin{enumerate}[resume]
  \item What is the perpendicular distance from $(2, 3)$ to the line $5x + 12y - 7 = 0$?
  \begin{itemize}
    \item[A)] $1$
    \item[B)] $2$
    \item[C)] $3$
    \item[D)] $4$
  \end{itemize}
  % ... items 12 to 20 (~7/10 MCQ)
\end{enumerate}

\section*{Section C \quad Substitution \& Structure \hfill \normalfont\small\textit{8 questions, 10 minutes}}
\begin{enumerate}[resume]
  % ... items 21 to 28 (100% MCQ)
\end{enumerate}

\section*{Section D \quad Challenge \hfill \normalfont\small\textit{5 questions, 15 minutes}}
% Add honest difficulty tag: (TMUA / SMC difficulty) or (SMC / BMO1 difficulty)
\textbf{\small (TMUA / SMC difficulty)}
\begin{enumerate}[resume]
  % ... items 29 to 33
\end{enumerate}

\end{document}
```

### Step 3: Draft the Answer Key (`geometry/answers/ans0N.tex`)
Create `geometry/answers/ans0N.tex` containing:
- `\ans{...}`: The exact answer.
- `\method{...}`: The fast contest solution / geometric invariant (not the slow textbook algebraic grind).
- `\inv{...}`: An extension or deeper prompt.
- **Top 5 Patterns Today** and **Common Traps to Avoid** at the end of the file, with `\seealso{...}` links to questions in that sheet.

> [!IMPORTANT]
> **The Quoting Rule for `\ans{}`:**
> If an answer contains **commas**, **coordinate pairs** (e.g. `$(2, 3)$`), **equations** (e.g. `$y = 2x + 1$`), or **prose** (e.g. `Center $(3,-2)$, radius $5$`), you **MUST** wrap the content in double quotes:
> ```latex
> \ans{"$(2, 3)$"}
> \ans{"$y = -x + 4$"}
> \ans{"Center $(3,-2)$, $r=5$."}
> ```
> This informs the automated binding engine (`latex_bridge.py`) that the answer is a single unified specification, rather than a comma-separated list of separate items.

Example answer structure:

```latex
\documentclass[11pt,a4paper]{article}
\input{../../shared/preamble}

\SpeedHeader{Geometry}{1}

\begin{document}

\SpeedTitleBlock{Daily Geometry Drill \#1 --- Worked Solutions}{Your Name}

\begin{enumerate}

%── A1 ──────────────────────────────────────────────────────────────────────────
\item Find the gradient of the line perpendicular to $3x - 4y + 12 = 0$.

\ans{$-\frac{4}{3}$}
\method{The line is $4y = 3x + 12 \implies m = \frac{3}{4}$. The perpendicular gradient is $m_\perp = -\frac{1}{m} = -\frac{4}{3}$.}
\inv{General rule: For $ax + by + c = 0$, the perpendicular gradient is always $b/a$.}

% ... (items A2 to D5)

\end{enumerate}

\section*{Top 5 Patterns Today}
\begin{enumerate}[leftmargin=2em, itemsep=4pt]
  \item \textbf{Perpendicular Gradients as Negative Reciprocals.}
        $m_1 m_2 = -1$ gives instantaneous perpendicular lines. \seealso{A1, B3}
  \item \textbf{Direct Perpendicular Distance Formula.}
        $d = \frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$ avoids constructing intersection points. \seealso{B1, C4}
  \item \textbf{Shoelace Formula for Coordinate Polygon Areas.}
        $\frac{1}{2}|(x_1 y_2 - y_1 x_2) + \dots|$ calculates polygon areas instantly. \seealso{C1, D2}
  \item \textbf{Perpendicular Bisector via Midpoint and Normal Vector.}
        The midpoint is on the line and $(x_2-x_1, y_2-y_1)$ serves as the normal vector. \seealso{A5, B6}
  \item \textbf{Collinearity via Determinant / Slope Equality.}
        Equal gradients between point pairs confirm collinearity in one step. \seealso{A4, C7}
\end{enumerate}

\section*{Common Traps to Avoid}
\begin{enumerate}[leftmargin=2em, itemsep=4pt]
  \item \textbf{Forgetting the Negative Sign in Perpendicular Slopes.}
        Writing $4/3$ instead of $-4/3$. \seealso{A1, B2}
  \item \textbf{Omission of Absolute Value in Perpendicular Distance.}
        Distance must be strictly non-negative; forgetting the numerator absolute value causes negative distances. \seealso{B1, C3}
  \item \textbf{Ordering Vertices Incorrectly in Shoelace Formula.}
        Vertices must be listed cyclically (clockwise or counterclockwise); crossing diagonals produces erroneous areas. \seealso{C1, D2}
  \item \textbf{Confusing Midpoint with Direction Vector.}
        Using $(x_1+x_2)/2$ instead of $(x_2-x_1)$ when setting up direction gradients. \seealso{A5, B7}
  \item \textbf{Assuming Triangles are Right-Angled Without Verification.}
        Applying Pythagoras without checking that a pair of slopes multiply to $-1$. \seealso{C5, D4}
\end{enumerate}

\SpeedClosing{``Speed comes from recognition, not from rushing. Every shortcut is a pattern you have internalised.''}

\end{document}
```

### Step 4: Compile PDFs & Check for Overfull Hboxes
Compile both `.tex` files with `pdflatex`:

```bash
cd geometry/sheets && pdflatex -interaction=nonstopmode sheet01.tex
cd ../answers && pdflatex -interaction=nonstopmode ans01.tex
cd ../..
```

**Zero Overfull Hboxes Rule:**
Check the compilation logs:
```bash
grep -i "overfull" geometry/sheets/sheet01.log geometry/answers/ans01.log || echo "CLEAN: 0 overfull hboxes"
```
If an overfull `\hbox` appears (e.g. wide equations or formulas spilling past the margin), break the formula across multiple lines or use displayed math (`\[ ... \]`).

Clean up auxiliary files after compiling:
```bash
rm -f geometry/sheets/*.aux geometry/sheets/*.log geometry/sheets/*.out \
      geometry/answers/*.aux geometry/answers/*.log geometry/answers/*.out
```

### Step 5: Write the Verification Script (`geometry/verify/sheet0N_verify.py`)
Create `geometry/verify/sheet0N_verify.py` with **exactly 33 `check_` functions**:

- Each function computes the answer programmatically (using `sympy`, `math`, `fractions`, or `itertools`).
- Every function must contain at least one non-vacuous assertion (`assert computed_var == expected`).
- Every function must `return` the computed value.
- If an answer was quoted in `\ans{"..."}`, return the quoted string (e.g. `return '"$y = -x + 4$"'`).

Template:

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
import math
from fractions import Fraction
import sympy

TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans01.tex'

def check_A1():
    """EXHAUSTIVE PROOF: Line 3x - 4y + 12 = 0 has m = 3/4; perpendicular is -4/3."""
    m = Fraction(3, 4)
    m_perp = -1 / m
    assert m_perp == Fraction(-4, 3)
    return Fraction(-4, 3)

# ... check_A2 through check_D5 (all 33 functions)

CHECKS = {
    'A1': check_A1,
    # ...
    'D5': check_D5
}

def main():
    if not __debug__:
        print("ERROR: Assertions are disabled! Do not run with -O or PYTHONOPTIMIZE.")
        sys.exit(1)

    passed = 0
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f"  PASS  {label}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {label}: {e}")

    print(f"\n{passed}/{len(CHECKS)} checks passed.")
    if passed != len(CHECKS):
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Step 6: Run Local Verification & CI Gates
Run the full test suite locally before committing:

```bash
# 1. Run the sheet's verification script directly
python3 geometry/verify/sheet01_verify.py

# 2. Run runtime binding test on this sheet
python3 -m pytest tests/test_answer_binding.py -k "geometry/sheet01"

# 3. Check AST assertions and binding baseline across the repository
python3 tools/check_binding.py

# 4. Check for facade tests (tautological assertions)
python3 tools/analyze_facades.py --strict

# 5. Check verify script structure
python3 tools/validate_verify_scripts.py --target geometry/verify/sheet01_verify.py
```

### Step 7: Archive Any Scrapped Questions
If you rewrite or discard draft questions during calibration, **never delete them**. Save them to `geometry/vault/scrapped-YYYY-MM-DD-day0N.md` with a note explaining why they were replaced (e.g. too tedious, duplicate of earlier question, etc.).

### Step 8: Commit Cleanly
Commit your changes using conventional commit formatting:
```bash
git add geometry/sheets/sheet01.* geometry/answers/ans01.* geometry/verify/sheet01_verify.py
git commit -m "feat(geometry): draft and verify Day 1 coordinate geometry & line mechanics"
```

---

## 4. Summary of Hard Rules

1. **33 Questions per Sheet:** Exactly A1–A10 (no MCQs), B1–B10 (~7/10 MCQ), C1–C8 (100% MCQ), D1–D5 (challenge).
2. **Exactly 33 `check_` Functions:** Every verification script must have all 33 checks implemented with non-vacuous assertions.
3. **No Calculators:** Design clean numbers, integers, and neat surds.
4. **Answer Quoting:** Wrap composite strings, coordinates, and equations in `\ans{"..."}`.
5. **Mistake Links:** Every answer sheet must end with 5 Patterns and 5 Traps, each with a valid `\seealso{Label}` link (10 links total).
6. **No Build Artifacts Tracked:** Delete `.aux`, `.log`, and `.out` files before committing.
