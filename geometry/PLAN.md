# Geometry Pillar — Build Plan & Syllabus

This document outlines the architectural syllabus, 7-day progression arc, and topic boundaries for the **Geometry Pillar**. 

Read this before drafting any sheets in `geometry/`. All repository-wide process conventions (research depth, MCQ splits, verification gates, mistake-linking) are defined in [`PILLAR-PLAYBOOK.md`](../PILLAR-PLAYBOOK.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 1. Vision & Target Audience

- **Target Audience:** High-achieving students preparing for **TMUA Paper 1 & 2 (target score: 9.0)**, **BMO1** (British Mathematical Olympiad Round 1), **SMC** (Senior Mathematical Challenge), and **MAT**.
- **No Calculators:** All competition problems must feature clean arithmetic, elegant geometric cancellations, integer/rational coordinates, or tidy surds. Avoid tedious arithmetic.
- **Speed through Structure:** Emphasize projective invariants, coordinate shortcuts (Shoelace, radical axis, perpendicular distance), and classical circle theorems over slow brute-force algebra.

---

## 2. Cross-Pillar Territory Map

Before drafting questions, consult this territory boundary to ensure Geometry does not duplicate techniques owned by other pillars:

| Topic / Technique | Owned By | Permitted in Geometry? |
|:---|:---|:---:|
| Polynomial curves, algebraic inequalities, functional equations | **Algebra** | ❌ (Keep curves purely linear/circular/conic) |
| Geometric counting (chords, diagonals, points in convex position) | **Combinatorics** | ❌ (Counting framing belongs to Combinatorics) |
| Geometric probability | **Combinatorics** | ❌ (Belongs to Combinatorics Day 5/6) |
| Coordinate lines, perpendicular bisectors, distance formula | **Geometry** | ✅ (Day 1 signature move) |
| Circle equations, tangents, circle-line discriminant vs distance | **Geometry** | ✅ (Day 2 signature move) |
| Multi-circle systems, radical axis by subtraction, common chords | **Geometry** | ✅ (Day 3 signature move) |
| Triangle centers (centroid, incenter, orthocenter, circumcenter) | **Geometry** | ✅ (Day 4 signature move) |
| Power of a Point ($PT^2 = PA \cdot PB$), alternate segment theorem | **Geometry** | ✅ (Day 5 signature move) |
| Cyclic quadrilaterals, Ptolemy's theorem, Brahmagupta, Pitot | **Geometry** | ✅ (Day 5–6 signature move) |
| Loci, Apollonius circles, geometric proof flaw diagnosis | **Geometry** | ✅ (Day 7 signature move) |

---

## 3. The 7-Day Progression Arc

Grounded directly in [`research/INDEX-tmua-geometry.md`](../research/INDEX-tmua-geometry.md):

### Day 1: Coordinate Geometry & Linear Systems
- **Theme:** Rapid line mechanics, perpendicularity, distance, and polygon areas.
- **Core Topics:**
  - Gradient relations ($m_1 m_2 = -1$), perpendicular bisectors between two points.
  - Distance formula and midpoint invariants.
  - Perpendicular distance from $(x_0, y_0)$ to $ax+by+c=0$: $d = \frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$.
  - **Shoelace Formula** for triangle and quadrilateral areas without altitude construction.
  - Linear intercept conditionals and collinearity tests.
- **Anchors from Corpus:** TMUA 2016 P1 Q8, 2021 P1 Q7, Hercules Mock P1 Q7, Tyler Tutoring pack 04.
- **Speed Invariant:** Use vector cross-product / Shoelace formula for area in $\le 15$ seconds.

### Day 2: Circle Equations, Tangents & Intersections
- **Theme:** Algebraic circles and line-circle interactions.
- **Core Topics:**
  - Completing the square on $x^2+y^2+2gx+2fy+c=0$ to find center $(-g, -f)$ and radius $r = \sqrt{g^2+f^2-c}$.
  - Tangent to circle at $(x_1, y_1)$ via line perpendicular to radius or split-variable identity $x x_1 + y y_1 + g(x+x_1) + f(y+y_1) + c = 0$.
  - Line-circle intersection via **perpendicular distance test** ($d < r, d = r, d > r$) instead of quadratic substitution.
  - Chords of circles: perpendicular from center bisects chord; half-chord length $\sqrt{r^2 - d^2}$.
- **Anchors from Corpus:** TMUA Specimen 1 Q8, 2017 P1 Q6, 2018 P1 Q7, 2020 P1 Q7, Tyler Tutoring pack 09.
- **Speed Invariant:** Never substitute $y = mx+c$ into a circle equation to check for tangency — always compare the perpendicular distance from the center to $r$.

### Day 3: Multi-Circle Systems & Radical Axes
- **Theme:** Two-circle geometry, common chords, and tangent lines.
- **Core Topics:**
  - Relative positions of two circles: $d > r_1+r_2$ (4 tangents), $d = r_1+r_2$ (3 tangents), $|r_1-r_2| < d < r_1+r_2$ (2 tangents), $d = |r_1-r_2|$ (1 tangent).
  - **Radical Axis**: Straight line $(a_1-a_2)x + (b_1-b_2)y + (c_1-c_2) = 0$ obtained by subtracting circle equations.
  - Common chord length via radical axis and distance from center.
  - Orthogonal circles: $d^2 = r_1^2 + r_2^2$ or $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$.
  - Tangency to both coordinate axes ($r = |x_0| = |y_0|$).
- **Anchors from Corpus:** TMUA 2016 P2 Q9, 2019 P1 Q7, JZMaths Mock 1 Q5, Vantage Mock P2 Q10, Oxbridge P1 Q8, BMO1 2017 Q4.
- **Speed Invariant:** Subtracting two circle equations instantly gives the common secant/chord in 1 line without solving for the intersection coordinates.

### Day 4: Triangle Centers & Euclidean Relations
- **Theme:** Centroids, incenters, circumcenters, orthocenters, and area formulas.
- **Core Topics:**
  - Triangle Centroid: $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$, median 2:1 division ratio.
  - Inradius formula: $A = r s$ (where $s = \frac{a+b+c}{2}$).
  - Right-angled triangle inradius shortcut: $r = \frac{a+b-c}{2}$.
  - Circumradius formula: $R = \frac{abc}{4A}$, Thales' theorem (right angle in semicircle).
  - **Angle Bisector Theorem**: $BD/DC = AB/AC$.
  - Apollonius' Theorem for medians: $b^2 + c^2 = 2m_a^2 + 2(a/2)^2$.
- **Anchors from Corpus:** TMUA 2016 P2 Q16, 2020 P2 Q10, 2021 P2 Q9, 2022 P2 Q5, 2023 P1 Q7, Beyond Horizon P1 Q16.
- **Speed Invariant:** Compute the inradius of a right triangle in 2 seconds via $(a+b-c)/2$.

### Day 5: Circle Theorems & Power of a Point
- **Theme:** Classical Euclidean circle geometry and projective metric invariants.
- **Core Topics:**
  - Angle at center is twice angle at circumference; angles in the same segment.
  - **Alternate Segment Theorem**: Angle between tangent and chord equals angle in alternate segment.
  - **Power of a Point Theorem**:
    - Intersecting chords: $PA \cdot PB = PC \cdot PD$.
    - Tangent-secant: $PT^2 = PA \cdot PB = d^2 - r^2$.
  - Cyclic quadrilaterals: Opposite angles sum to $180^\circ$.
  - **Ptolemy's Theorem**: $AC \cdot BD = AB \cdot CD + BC \cdot AD$.
- **Anchors from Corpus:** TMUA Specimen 2 Q9, 2017 P2 Q15, 2023 P2 Q9, BMO1 2011 Q2, Tyler Tutoring pack 09.
- **Speed Invariant:** Use Power of a Point to equate chord products instantly instead of constructing similar triangles from scratch.

### Day 6: BMO1 Capstone I — Written Euclidean & Cyclic Proofs
- **Theme:** Olympiad-level geometric reasoning and synthetic proof constructions.
- **Core Topics:**
  - Perpendicular diagonals in cyclic quadrilaterals (**Brahmagupta's Theorem**).
  - Tangent quadrilaterals (**Pitot's Theorem**: $AB + CD = BC + DA$).
  - Inscribed and circumscribed circle interactions; contact triangles.
  - Orthocenter and reflections in sides lying on the circumcircle.
  - Proof-heavy structure in Section D (written proofs rather than multiple-choice options).
- **Anchors from Corpus:** BMO1 2010 Q4, 2013 Q4, 2015 Q3, 2020 Q3, 2023 Q4.

### Day 7: TMUA 9.0 Capstone Synthesis & Geometric Logic
- **Theme:** Full synthesis across all 6 skills under TMUA Paper 1 and Paper 2 conditions.
- **Core Topics:**
  - **Loci & Circles of Apollonius**: Locus of points with ratio of distances $PA/PB = k$ ($k \neq 1$ yields a circle).
  - Geometry-logic conditionals: Necessary vs sufficient conditions for geometric properties (concyclicity, tangency, parallelism).
  - Spot-the-flaw in geometric proofs (e.g. convexity assumptions, betweenness fallacies, extraneous intersection branches).
  - Mixed multi-step challenge problems combining coordinates, circle theorems, and area optimization.
- **Anchors from Corpus:** TMUA 2018 P2 Q6, 2019 P2 Q14, 2022 P1 Q7, BMO1 2017 Q4.

---

## 4. Question Format & Distribution Rules

Each day must contain **exactly 33 questions**:

| Section | Role | Question Count | Format Policy | Time Limit |
|:---|:---|:---:|:---|:---:|
| **Section A** | Rapid Recognition | **10** (A1–A10) | **100% Non-MCQ** (Exact values, coordinates, equations). Never multiple-choice. | 2:30 |
| **Section B** | Manipulation Drills | **10** (B1–B10) | **~7/10 MCQ**, rest short structured response. | 8:00 |
| **Section C** | Substitution & Structure | **8** (C1–C8) | **100% MCQ** (Options A–D or A–E). High-speed TMUA/SMC standard. | 10:00 |
| **Section D** | Challenge Ramp | **5** (D1–D5) | Days 1–5: MCQ-leaning. Days 6–7: Proof-heavy (BMO1 style). | 15:00 |

---

## 5. Interleaving Convention

Starting on **Day 2**, each sheet's Section A and B must include **1–2 graded questions that reuse tools from earlier days**:
- Day 2 folds in 1–2 Day 1 linear/distance techniques.
- Day 3 folds in 1–2 Day 1–2 circle completing-the-square/perpendicular distance tests.
- Day 4 folds in 1–2 Day 2–3 circle chord/tangent mechanics.
- Day 5 folds in 1–2 Day 4 inradius/circumradius theorems.
- Days 6–7 synthesize the entire week's toolkit.

---

## 6. Mistake-Linking Convention

Every `ans0N.tex` must conclude with:
1. `\section*{Top 5 Patterns Today}` (5 items)
2. `\section*{Common Traps to Avoid}` (5 items)

Each item must include `\seealso{Label1, Label2}` pointing directly to questions in that sheet where the pattern or trap appears. **Exactly 10 `\seealso` links total per sheet.**
