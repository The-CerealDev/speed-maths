# Vault — geometry Day 2: scrapped 2026-09-29

Henry Koduthore's original Day 2 ("Circle equations, tangents and line--circle interactions"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 13 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet02.tex` (and `answers/ans02.tex`, `verify/sheet02_verify.py`).

## A2

```latex
Write down the radius of the circle $\;x^2 + y^2 - 6x - 8y + 24 = 0$.
```

- Original answer: `$1$`
- Original method: From A1, $(x-3)^2+(y-4)^2=1$, so $r=\sqrt{1}=1$.

## A8

```latex
Write down the equation of the circle with centre $(-1,2)$ and radius $3$.
```

- Original answer: `"$x^2+y^2+2x-4y-4=0$"`
- Original method: $(x+1)^2+(y-2)^2=9$ expands to $x^2+y^2+2x-4y+5=9$, i.e. $x^2+y^2+2x-4y-4=0$.

## C1

```latex
A tangent to the circle $x^2+y^2=144$ passes through $(20,0)$ and meets the positive $y$-axis at $T$. What is the $y$-coordinate of $T$? \textit{\small(after TMUA 2017 Paper 1 Q6)}
\begin{itemize}
\item[A)] $12$
\item[B)] $15$
\item[C)] $\tfrac{49}{3}$
\item[D)] $20$
\end{itemize}
```

- Original answer: `B) $15$`
- Original method: Radius to touch point is $\perp$ tangent. Let $T=(0,t)$, line through $(20,0)$ and $(0,t)$ has equation $x/20+y/t=1$, i.e. $tx+20y-20t=0$. Distance from origin $=r=12$: $| -20t|/\sqrt{t^2+400}=12\Rightarrow 400t^2=144(t^2+400)\Rightarrow256t^2=57600\Rightarrow t^2=225\Rightarrow t=15$ (positive). Check $t=15$ gives line $3x+4y=60$, distance $60/5=12$ \checkmark.

## C3

```latex
The circles $(x+4)^2+(y+1)^2=64$ and $(x-8)^2+(y-4)^2=r^2$ have exactly one point in common. If $r<13$, what is $r$? \textit{\small(after TMUA 2019 Paper 1 Q6)}
\begin{itemize}
\item[A)] $5$
\item[B)] $8$
\item[C)] $13$
\item[D)] $21$
\end{itemize}
```

- Original answer: `A) $5$`
- Original method: Centre distance $d=\sqrt{12^2+5^2}=13$. One point $\Rightarrow$ internal tangency $r=|d-8|=5$ (since $r<13$). External would give $21$.

## C4

```latex
A circle has equation $x^2+y^2-18x-22y+178=0$ (centre $(9,11)$, $r=5$). A regular hexagon $ABCDEF$ is inscribed so that all vertices lie on the circle. What is the area of the hexagon? \textit{\small(adapted from TMUA 2017 Paper 1 Q9)}
\begin{itemize}
\item[A)] $18\sqrt3$
\item[B)] $36\sqrt3$
\item[C)] $ \tfrac{75\sqrt3}{2}$
\item[D)] $75$
\end{itemize}
```

- Original answer: `C) $\tfrac{75\sqrt3}{2}$`
- Original method: Regular hexagon = 6 equilateral triangles side $r=5$: area $=6\cdot \tfrac{\sqrt3}{4}r^2 = \tfrac{3\sqrt3}{2}r^2 = \tfrac{75\sqrt3}{2}$.

## C5

```latex
The line $y=2x+5$ is a tangent to the circle $x^2+y^2=r^2$. Which $r^2$ makes the distance from the centre to the line equal to $r$?
\begin{itemize}
\item[A)] $1$
\item[B)] $5$
\item[C)] $20$
\item[D)] $25$
\end{itemize}
```

- Original answer: `B) $5$`
- Original method: Distance $=|5|/\sqrt{5}= \sqrt5 =r$, so $r^2=5$.

## C7

```latex
The circle $x^2+y^2-8x-4y-21=0$ ($r= \sqrt{41}$) is cut by the $y$-axis ($x=0$). What is the length of the chord intercepted on the $y$-axis?
\begin{itemize}
\item[A)] $2\sqrt{21}$
\item[B)] $2\sqrt{41}$
\item[C)] $8$
\item[D)] $10$
\end{itemize}
```

- Original answer: `D) $10$`
- Original method: Centre $(4,2)$, distance to $x=0$ is $4$, half-chord $\sqrt{41-16}=5$, length $10$. Also $x=0\Rightarrow y^2-4y-21=0\Rightarrow y=7,-3$, distance $10$.

## C8

```latex
The line $y=kx+5$ is tangent to the circle $x^2+y^2-6x-8y+24=0$ (centre $(3,4)$, $r=1$). How many distinct $k$ satisfy this? \textit{\small(after TMUA 2020 Paper 1 Q7)}
\begin{itemize}
\item[A)] $0$
\item[B)] $1$
\item[C)] $2$
\item[D)] Infinitely many
\end{itemize}
```

- Original answer: `C) $2$`
- Original method: Point $(0,5)$ is distance $\sqrt{10}>1$ from centre, so external: two tangents. Solve $|3k-4+5|/\sqrt{k^2+1}=1$ gives $2$ slopes.

## D1

```latex
The circles $C_1:(x+2)^2+(y-3)^2=18$ and $C_2:(x-7)^2+(y+6)^2=2$ have centres $O_1,O_2$. What is the \emph{shortest} distance between a point on $C_1$ and a point on $C_2$? \textit{\small(adapted from TMUA 2018 Paper 1 Q7 / 2022 Paper 1 Q3)}
\begin{itemize}
\item[A)] $5\sqrt2-4$
\item[B)] $5\sqrt2-5$
\item[C)] $5\sqrt2$
\item[D)] $5\sqrt2+5$
\end{itemize}
```

- Original answer: `C) $5\sqrt2$`
- Original method: $O_1=(-2,3)$, $O_2=(7,-6)$, $O_1O_2=\sqrt{9^2+9^2}=9\sqrt2$, $r_1=3\sqrt2$, $r_2=\sqrt2$, sum $4\sqrt2$, shortest $=9\sqrt2-4\sqrt2=5\sqrt2$. Externally separated ($d>r_1+r_2$).

## D2

```latex
The segment joining $(3,3)$ and $(7,5)$ is a diameter of circle $C$. $C$ is translated $3$ left, reflected in the $x$-axis, then enlarged scale factor $4$ about its centre. What is the equation of the final circle? \textit{\small(after TMUA Specimen Paper 1 Q9)}
\begin{itemize}
\item[A)] $(x-2)^2+(y-4)^2=80$
\item[B)] $(x-2)^2+(y+4)^2=80$
\item[C)] $(x-2)^2+(y-4)^2=320$
\item[D)] $(x-2)^2+(y+4)^2=320$
\end{itemize}
```

- Original answer: `B) $(x-2)^2+(y+4)^2=80$`
- Original method: Original centre $(5,4)$, $r^2=(2)^2+1^2=5$. Translate $3$ left: $(2,4)$, reflect in $x$-axis: $(2,-4)$, enlarge $4\times$ about centre: $r^2=5\cdot16=80$, so $(x-2)^2+(y+4)^2=80$.

## D3

```latex
Circle $O$ radius $6$, $\angle POQ\ge \pi/2$, area $[POQ]=9\sqrt3$. For variable $R$ on the major arc $PQ$, what is the \emph{greatest possible} area of $\triangle PRQ$? \textit{\small(adapted from TMUA 2022 Paper 1 Q14)}
\begin{itemize}
\item[A)] $18+9\sqrt3$
\item[B)] $27\sqrt3$
\item[C)] $27+9\sqrt3$
\item[D)] $36+9\sqrt3$
\end{itemize}
```

- Original answer: `B) $27\sqrt3$`
- Original method: $[POQ]=\tfrac12 r^2\sin\theta=18\sin\theta=9\sqrt3\Rightarrow\sin\theta=\sqrt3/2$, $\theta=120^\circ$. Chord $PQ=6\sqrt3$, maximal height $9$, area $27\sqrt3$.

## D4

```latex
Let $P(p,q)$ and circle $C: x^2+2fx+y^2+2gy+h=0$ with centre $(-f,-g)$ and $L=|PC_0|$. Which set is \emph{minimal sufficient} to compute $L$? \textit{\small(after MAT 2020 Q1H)}
\begin{itemize}
\item[A)] $f,g,h$
\item[B)] $f,g,p,q$
\item[C)] $f,h,p,q$
\item[D)] $g,h,p,q$
\end{itemize}
```

- Original answer: `B) $f,g,p,q$`
- Original method: $L^2=(p+f)^2+(q+g)^2$ needs $f,g,p,q$; $h$ irrelevant.

## D5

```latex
$ABCD$ is a cyclic quadrilateral with perpendicular diagonals intersecting at $E$. The line through $E$ perpendicular to $AB$ meets $CD$ at $F$. Which statement is \emph{necessarily true}? \textit{\small(adapted from BMO1 2010 Q4)}
\begin{itemize}
\item[A)] $F$ is the midpoint of $CD$ (Brahmagupta)
\item[B)] $F$ bisects $\angle CED$
\item[C)] $EF = AB/2$
\item[D)] $ABCD$ must be an isosceles trapezium
\end{itemize}
```

- Original answer: `A) $F$ is the midpoint of $CD$ (Brahmagupta)`
- Original method: Brahmagupta: In a cyclic quadrilateral with $\perp$ diagonals, the perpendicular from the intersection to a side bisects the opposite side.
