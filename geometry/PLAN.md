# Geometry Pillar — Build Plan & Syllabus (ONLY A PLAN; LOADS OF CHANGES CAN AND SHOULD BE MADE, THIS ISN'T PERFECT... yet)

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
| Polygon angle sums, angle chasing, similarity and area ratios | **Geometry** | ✅ (Day 4 signature move) |
| Circle theorems, power of a point, touching circles, Ptolemy, Pitot | **Geometry** | ✅ (Day 5 signature move) |
| Solids: volume, surface area, nets, cross-sections, Euler's formula | **Geometry** | ✅ (Day 6 signature move) |
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
- **Anchors (adapted, credited on the sheet):** TMUA Specimen P1 Q3, 2017 P1 Q3, 2023 P1 Q5.
- **Speed Invariant:** Use vector cross-product / Shoelace formula for area in $\le 15$ seconds.

### Day 2: Circle Equations, Tangents & Intersections
- **Theme:** Algebraic circles and line-circle interactions.
- **Core Topics:**
  - Completing the square on $x^2+y^2+2gx+2fy+c=0$ to find center $(-g, -f)$ and radius $r = \sqrt{g^2+f^2-c}$.
  - Tangent to circle at $(x_1, y_1)$ via line perpendicular to radius or split-variable identity $x x_1 + y y_1 + g(x+x_1) + f(y+y_1) + c = 0$.
  - Line-circle intersection via **perpendicular distance test** ($d < r, d = r, d > r$) instead of quadratic substitution.
  - Chords of circles: perpendicular from center bisects chord; half-chord length $\sqrt{r^2 - d^2}$.
- **Anchors (adapted, credited on the sheet):** TMUA Specimen P1 Q9, 2017 P1 Q6, 2017 P1 Q9, 2018 P1 Q3, 2022 P1 Q2, 2022 P1 Q14.
- **Speed Invariant:** Never substitute $y = mx+c$ into a circle equation to check for tangency — always compare the perpendicular distance from the center to $r$.

### Day 3: Multi-Circle Systems & Radical Axes
- **Theme:** Two-circle geometry, common chords, and tangent lines.
- **Core Topics:**
  - Relative positions of two circles: $d > r_1+r_2$ (4 tangents), $d = r_1+r_2$ (3 tangents), $|r_1-r_2| < d < r_1+r_2$ (2 tangents), $d = |r_1-r_2|$ (1 tangent).
  - **Radical Axis**: Straight line $(a_1-a_2)x + (b_1-b_2)y + (c_1-c_2) = 0$ obtained by subtracting circle equations.
  - Common chord length via radical axis and distance from center.
  - Orthogonal circles: $d^2 = r_1^2 + r_2^2$ or $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$.
  - Tangency to both coordinate axes ($r = |x_0| = |y_0|$).
- **Anchors (adapted, credited on the sheet):** TMUA 2019 P1 Q6, 2020 P1 Q16, 2021 P1 Q1, 2021 P2 Q15; Primer 1.4 P47.
- **Speed Invariant:** Subtracting two circle equations instantly gives the common secant/chord in 1 line without solving for the intersection coordinates.

### Day 4: Polygons & Angle Chasing
- **Theme:** SMC-style Euclid: the angle and area facts every later day leans on.
- **Core Topics:**
  - Interior and exterior angle sums of polygons; regular polygon angles.
  - Angle chasing with parallels, isosceles triangles and folded paper.
  - Similar triangles and area ratios (shared heights, $k^2$ scaling).
  - Triangles as the preview toolkit: inradius, angle bisector ratios.
- **Anchors (adapted, credited on the sheet):** Primer 1.4 P11, P48; SMC Q18–25 style throughout.
- **Section D:** D5 is a written angle chase or proof.

### Day 5: Circles, Arcs & Tangency
- **Theme:** Circle theorems, power of a point and touching circles.
- **Core Topics:**
  - Angle at the centre, angles on the same arc, cyclic quadrilaterals, alternate segment.
  - **Power of a Point**: $PA \cdot PB = PC \cdot PD$; $PT^2 = PA \cdot PB = d^2 - r^2$.
  - Touching circles (join the centres), circles in an angle, lenses and segments.
  - Ptolemy and Pitot on cyclic and tangential quadrilaterals.
- **Anchors (adapted, credited on the sheet):** Primer 1.4 P8, P13, P16, P24, P33, P35, P40; SMC 2011 Q24, 2012 Q20, 2014 Q19, 2016 Q21, 2017 Q19, 2019 Q25, 2021 Q22, 2025 Q21.
- **Section D:** D5 is a proof (Brahmagupta's theorem).

### Day 6: Solids & Spatial Reasoning
- **Theme:** Three-dimensional SMC geometry.
- **Core Topics:**
  - Volume and surface area of prisms, pyramids, cones, spheres and frustums; similar solids.
  - Nets, painted cubes and Euler's formula $V - E + F = 2$.
  - Cross-sections of cubes, solids inscribed in spheres and cones.
- **Anchors (adapted, credited on the sheet):** SMC 2011 Q25, 2014 Q18, 2016 Q23, 2019 Q23, 2022 Q25, 2023 Q16; Primer 1.4 P23, P28, 8.8 P12, 9.1 P41; community TMUA mocks.
- **Section D:** D5 is a proof (a tetrahedron with equal opposite edges has acute faces).

### Day 7: TMUA 9.0 Capstone Synthesis & Geometric Logic
- **Theme:** TMUA synthesis across the week under Paper 1 and Paper 2 conditions.
- **Core Topics:**
  - **Loci & Circles of Apollonius**: Locus of points with ratio of distances $PA/PB = k$ ($k \neq 1$ yields a circle).
  - Geometry-logic conditionals: Necessary vs sufficient conditions for geometric properties (concyclicity, tangency, parallelism).
  - Spot-the-flaw in geometric proofs (e.g. convexity assumptions, betweenness fallacies, extraneous intersection branches).
  - Mixed multi-step challenge problems combining coordinates, circle theorems, and area optimization.
- **Anchors (adapted, credited on the sheet):** TMUA 2018 P1 Q19, 2020 P2 Q7, 2022 P2 Q11; tmua.fyi Challenge Mock 1 P1 Q14.
- **After this pillar:** true BMO1 geometry belongs in sheets 8+.

---

## 4. Question Format & Distribution Rules

Each day must contain **exactly 33 questions**:

| Section | Role | Question Count | Format Policy | Time Limit |
|:---|:---|:---:|:---|:---:|
| **Section A** | Rapid Recognition | **10** (A1–A10) | **100% Non-MCQ** (Exact values, coordinates, equations). Never multiple-choice. | 2:30 |
| **Section B** | Manipulation Drills | **10** (B1–B10) | **~7/10 MCQ**, rest short structured response. | 8:00 |
| **Section C** | Substitution & Structure | **8** (C1–C8) | **100% MCQ** (Options A–D or A–E). High-speed TMUA/SMC standard. | 10:00 |
| **Section D** | Challenge Ramp | **5** (D1–D5) | Days 1–3: MCQ. Days 4–7: D5 is a written proof or angle chase. | 15:00 |

---

## 5. Interleaving Convention

Starting on **Day 2**, each sheet's Section A and B must include **1–2 graded questions that reuse tools from earlier days**:
- Day 2 folds in 1–2 Day 1 linear/distance techniques.
- Day 3 folds in 1–2 Day 1–2 circle completing-the-square/perpendicular distance tests.
- Day 4 folds in 1–2 Day 2–3 circle chord/tangent mechanics.
- Day 5 folds in 1–2 Day 4 angle-chasing and similarity moves.
- Days 6–7 synthesize the entire week's toolkit.

---

## 6. Mistake-Linking Convention

Every `ans0N.tex` must conclude with:
1. `\section*{Top 5 Patterns Today}` (5 items)
2. `\section*{Common Traps to Avoid}` (5 items)

Each item must include `\seealso{Label1, Label2}` pointing directly to questions in that sheet where the pattern or trap appears. **Exactly 10 `\seealso` links total per sheet.**
