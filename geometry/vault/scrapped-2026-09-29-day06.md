# Vault — geometry Day 6: scrapped 2026-09-29

Henry Koduthore's original Day 6 ("Circle theorems and power of a point"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 21 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet06.tex` (and `answers/ans06.tex`, `verify/sheet06_verify.py`).

## A2

```latex
Points $P,Q,R,S$ lie on a circle, and $\angle PQR = 35^\circ$. Write down $\angle PSR$.
```

- Original answer: `$35$`
- Original method: $\angle PQR$ and $\angle PSR$ stand on the same chord $PR$, so they are equal.

## A8

```latex
Two secants from the external point $P$ cut the circle as $P$--$A$--$B$ and $P$--$C$--$D$, with $PA=4$, $PB=6$ and $PC=2$. Write down $PD$.
```

- Original answer: `$12$`
- Original method: Secant--secant power: $PA\cdot PB = PC\cdot PD$, so $4\cdot 6 = 2\cdot PD$, $PD=12$.

## A9

```latex
A tangent from $P$ has length $8$, and a secant through $P$ meets the circle at $A$ (nearer) and $B$, with $PA=4$. Write down $PB$.
```

- Original answer: `$16$`
- Original method: $PT^2 = PA\cdot PB$: $64=4\cdot PB$, $PB=16$.

## B1

```latex
$O$ is the centre of a circle and $\angle AOB=130^\circ$. The angle at the circumference subtending $AB$ is?
\begin{itemize}
\item[A)] $60^\circ$
\item[B)] $65^\circ$
\item[C)] $70^\circ$
\item[D)] $130^\circ$
\end{itemize}
```

- Original answer: `B) $65$`
- Original method: Half the central angle: $\frac12\cdot 130^\circ = 65^\circ$.

## B2

```latex
$ABCD$ is cyclic with $\angle A=100^\circ$. Then $\angle C$ is?
\begin{itemize}
\item[A)] $80^\circ$
\item[B)] $100^\circ$
\item[C)] $90^\circ$
\item[D)] $160^\circ$
\end{itemize}
```

- Original answer: `A) $80$`
- Original method: Opposite angles are supplementary: $180^\circ - 100^\circ = 80^\circ$.

## B3

```latex
Chords $AB$ and $CD$ cross at an interior point $P$, with $PA=3$, $PB=5$ and $PC=15$. Then $PD$ is?
\begin{itemize}
\item[A)] $1$
\item[B)] $3$
\item[C)] $5$
\item[D)] $9$
\end{itemize}
```

- Original answer: `A) $1$`
- Original method: $3\cdot 5 = 15\cdot PD$, so $PD=1$.

## B4

```latex
A tangent from $P$ has length $5$, and a secant through $P$ gives outer segment $PA=2$. Write down $PB$ (the full secant segment).
```

- Original answer: `$\dfrac{25}{2}$`
- Original method: $PT^2=PA\cdot PB$: $25 = 2\cdot PB$, $PB=\frac{25}{2}$.

## B6

```latex
The secant $PAB$ from an external point has $PA=2$, $PB=18$. The length of the tangent $PT$ drawn from $P$ is?
\begin{itemize}
\item[A)] $6$
\item[B)] $9$
\item[C)] $12$
\item[D)] $36$
\end{itemize}
```

- Original answer: `A) $6$`
- Original method: $PT=\sqrt{PA\cdot PB}=\sqrt{2\cdot 18}=\sqrt{36}=6$.

## B10

```latex
Chords $AB$ and $CD$ intersect at $P$ with $PA=6$, $PB=4$ and $PC=3$. Write down $PD$.
```

- Original answer: `$8$`
- Original method: $PA\cdot PB=PC\cdot PD$: $6\cdot 4=3\cdot PD$, $PD=8$.

## C1

```latex
\vspace{0pt}
Chords $AB$ and $CD$ meet at $P$ inside a circle with $PA=6$, $PB=8$ and $CP:PD=3:4$. Find $CP$. \textit{\small(after TMUA 2023 Paper 2 Q9)}
\begin{itemize}
\item[A)] $4$
\item[B)] $6$
\item[C)] $8$
\item[D)] $12$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.45]
\draw (0,0) circle (1.5);
\draw (-1.3,-0.8) -- (1.2,1.0);
\draw (-1.2,1.0) -- (1.3,-0.7);
\fill (0.02,0.14) circle (1.5pt) node[above right]{\tiny $P$};
\node at (-1.3,-0.8) [left]{\tiny $A$};
\node at (1.2,1.0) [right]{\tiny $B$};
\node at (-1.2,1.0) [left]{\tiny $C$};
\node at (1.3,-0.7) [right]{\tiny $D$};
\end{tikzpicture}
\end{minipage}
```

- Original answer: `B) $6$`
- Original method: Let $CP=3k$, $PD=4k$. Intersecting chords: $PA\cdot PB=CP\cdot PD$, i.e.\ $6\cdot 8=3k\cdot 4k=12k^{2}$. So $48=12k^{2}$, $k^{2}=4$, $k=2$, $CP=6$ and $PD=8$. Check: $6$ and $8$ are consecutive multiples of $3,4$.

## C3

```latex
\vspace{0pt}
Cyclic quadrilateral $ABCD$ has $AB=6$, $BC=4$, $CD=5$, $DA=3$ and diagonal $AC=7$. Find the other diagonal $BD$ (Ptolemy: $AC\cdot BD=AB\cdot CD+BC\cdot AD$). \textit{\small(after TMUA 2017 Paper 2 Q15)}
\begin{itemize}
\item[A)] $5$
\item[B)] $7$
\item[C)] $6$
\item[D)] $13$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.48]
\draw (0,0) circle (1.4);
\coordinate (A) at (1.3,0.5);
\coordinate (B) at (0.3,1.36);
\coordinate (C) at (-1.2,0.7);
\coordinate (D) at (-0.4,-1.33);
\draw (A) -- (B) -- (C) -- (D) -- cycle;
\draw (A) -- (C);
\node at (A) [right]{\tiny $B$};
\node at (B) [above]{\tiny $A$};
\node at (C) [left]{\tiny $D$};
\node at (D) [below]{\tiny $C$};
\end{tikzpicture}
\end{minipage}
```

- Original answer: `C) $6$`
- Original method: Ptolemy for cyclic $ABCD$: $AC\cdot BD=AB\cdot CD+BC\cdot AD =6\cdot5+4\cdot3=30+12=42$. With $AC=7$, $BD=42/7=6$. Verify $BD<AB+AD$ etc.\ so cyclic existence holds.

## C4

```latex
A cyclic quadrilateral has sides $4,5,5,6$ (in order). By Brahmagupta $K=\sqrt{(s-a)(s-b)(s-c)(s-d)}$, its area is? \textit{\small(after BMO1 2010 Q4)}
\begin{itemize}
\item[A)] $10\sqrt{6}$
\item[B)] $12\sqrt{5}$
\item[C)] $30$
\item[D)] $24$
\end{itemize}
```

- Original answer: `A) $10\sqrt{6}$`
- Original method: $s=\tfrac{4+5+5+6}{2}=10$. Brahmagupta: $K=\sqrt{(10-4)(10-5)(10-5)(10-6)}=\sqrt{6\cdot5\cdot5\cdot4}=\sqrt{600}=10\sqrt6$.

## C5

```latex
A tangential quadrilateral $ABCD$ circumscribes a circle with $AB=3x$, $BC=8$, $CD=5$, $DA=2x+3$. Given Pitot $AB+CD=BC+DA$, find $x$ and hence $DA$. \textit{\small(after BMO1 2015 Q3)}
\begin{itemize}
\item[A)] $12$
\item[B)] $15$
\item[C)] $18$
\item[D)] $9$
\end{itemize}
```

- Original answer: `B) $15$`
- Original method: Pitot for tangential quadrilaterals: $AB+CD=BC+DA$. So $3x+5=8+2x+3$, giving $3x+5=2x+11$, $x=6$, hence $DA=2x+3=15$. Check opposite sums: $18+5=23$, $8+15=23$.

## C6

```latex
From external $P$, secants $PAB$ ($PA=4$, $PB=18$) and $PCD$ ($PC=6$) cut the same circle. Find $CD$. \textit{\small(after TMUA 2019 Paper 1 Q7)}
\begin{itemize}
\item[A)] $6$
\item[B)] $12$
\item[C)] $9$
\item[D)] $18$
\end{itemize}
```

- Original answer: `A) $6$`
- Original method: Secant--secant power from $P$: $PA\cdot PB=PC\cdot PD$. $PA\cdot PB=4\cdot18=72$, so $6\cdot PD=72$, $PD=12$, chord $CD=PD-PC=6$. Same product $72$ is $6\times12$.

## C7

```latex
Cyclic quadrilateral $ABCD$ has $AB=8$, $BC=6$, $CD=6$, $DA=6$ and $AC=12$. Find $BD$ (Ptolemy). \textit{\small(after TMUA Specimen Paper 2 Q9)}
\begin{itemize}
\item[A)] $7$
\item[B)] $12$
\item[C)] $14$
\item[D)] $84$
\end{itemize}
```

- Original answer: `A) $7$`
- Original method: Ptolemy: $AC\cdot BD=AB\cdot CD+BC\cdot DA=8\cdot6+6\cdot6=48+36=84$. With $AC=12$, $BD=84/12=7$. Check $7<8+6$ etc.\ valid.

## C8

```latex
Cyclic quadrilateral with sides $5,5,8,14$ has area (Brahmagupta, $s=16$) equal to? \textit{\small(after BMO1 2010 Q4)}
\begin{itemize}
\item[A)] $44$
\item[B)] $36$
\item[C)] $48$
\item[D)] $24$
\end{itemize}
```

- Original answer: `A) $44$`
- Original method: $s=\tfrac{5+5+8+14}{2}=16$. Brahmagupta: $K=\sqrt{(16-5)(16-5)(16-8)(16-14)}$\\ $=\sqrt{11\cdot11\cdot8\cdot2}=\sqrt{1936}=44$.

## D1

```latex
Cyclic quadrilateral $ABCD$ has sides $2,5,10,11$ (in order, $s=14$). Its Brahmagupta area is? \textit{\small(after BMO1 2010 Q4)}
\begin{itemize}
\item[A)] $36$
\item[B)] $44$
\item[C)] $30$
\item[D)] $48$
\end{itemize}
```

- Original answer: `A) $36$`
- Original method: $s=\tfrac{2+5+10+11}{2}=14$. $K=\sqrt{(14-2)(14-5)(14-10)(14-11)}=\sqrt{12\cdot9\cdot4\cdot3}=\sqrt{1296}=36$. Check trapezoid? Also equals Heron split via diagonal $12$: two triangles $5\!-\!12\!-\!13$ style.

## D2

```latex
Cyclic quadrilateral $ABCD$ has $AB=7$, $BC=8$, $CD=7$, $DA=9$ with $AC=11$. Find $BD$ via Ptolemy. \textit{\small(after BMO1 2011 Q2)}
\begin{itemize}
\item[A)] $11$
\item[B)] $7$
\item[C)] $14$
\item[D)] $18$
\end{itemize}
```

- Original answer: `A) $11$`
- Original method: Ptolemy: $AC\cdot BD=AB\cdot CD+BC\cdot DA=7\cdot7+8\cdot9=49+72=121$. With $AC=11$, $BD=121/11=11$. Both diagonals equal $11$; quadrilateral is an isosceles trapezoid in disguise.

## D3

```latex
From external $P$, tangent $PT=12$ and secant $PAB$ satisfies $PB=PA+10$ with $PT^{2}=PA\cdot PB$. Find $PA$. \textit{\small(after TMUA 2020 Paper 1 Q7)}
\begin{itemize}
\item[A)] $6$
\item[B)] $8$
\item[C)] $12$
\item[D)] $18$
\end{itemize}
```

- Original answer: `B) $8$`
- Original method: Tangent--secant power: $PT^{2}=PA\cdot PB$ with $PB=PA+10$. So $144=PA(PA+10)$, i.e.\ $PA^{2}+10PA-144=0$, $(PA+18)(PA-8)=0$, $PA=8$. Check: $8\cdot18=144=12^{2}$.

## D4

```latex
A quadrilateral with sides $5,5,8,8$ (in order $AB=5,BC=5,CD=8,DA=8$) is both tangential (Pitot $5+8=5+8$) and cyclic. Its Brahmagupta area is? \textit{\small(after BMO1 2015 Q3)}
\begin{itemize}
\item[A)] $40$
\item[B)] $30$
\item[C)] $36$
\item[D)] $44$
\end{itemize}
```

- Original answer: `A) $40$`
- Original method: Sides $5,5,8,8$ (order $AB=5,BC=5,CD=8,DA=8$): Pitot check $AB+CD=5+8=13=BC+DA$, so tangential confirms an incircle exists. Semiperimeter $s=13$. Brahmagupta (cyclic): $K=\sqrt{(13-5)(13-5)(13-8)(13-8)}=\sqrt{8\cdot8\cdot5\cdot5}=40$. Bicentric: both theorems hold; area also $=r\cdot s$ with $r=40/13$.

## D5

```latex
Cyclic quadrilateral $ABCD$ has $AB=6$, $BC=8$, $CD=12$, $DA=10$ and $AC=8$. Find $BD$. \textit{\small(after TMUA 2017 Paper 2 Q15)}
\begin{itemize}
\item[A)] $19$
\item[B)] $12$
\item[C)] $15$
\item[D)] $8$
\end{itemize}
```

- Original answer: `A) $19$`
- Original method: Ptolemy: $AC\cdot BD=AB\cdot CD+BC\cdot DA=6\cdot12+8\cdot10=72+80=152$. With $AC=8$, $BD=152/8=19$. Check $19<6+8+10$ etc.\ valid diagonal.
