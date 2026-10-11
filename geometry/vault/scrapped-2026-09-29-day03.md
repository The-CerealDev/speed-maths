# Vault — geometry Day 3: scrapped 2026-09-29

Henry Koduthore's original Day 3 ("Two-circle systems, radical axes and common chords"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 11 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet03.tex` (and `answers/ans03.tex`, `verify/sheet03_verify.py`).

## A3

```latex
Write down the radical axis of the circles $\;x^2+y^2-6x+2y+1=0$ and $\;x^2+y^2-2x-4y+13=0$.
```

- Original answer: `"$2x-3y+6=0$"`
- Original method: At the radical axis powers are equal, so subtract: $(-6x+2y+1)-(-2x-4y+13)=0$, i.e.\ $-4x+6y-12=0$, i.e.\ $2x-3y+6=0$. The $x^2+y^2$ terms cancel in one stroke.

## B1

```latex
How many common tangents do the circles $\;x^2+y^2=9$ and $\;x^2+y^2-4x-6y+9=0$ have?
\begin{itemize}
\item[A)] $0$
\item[B)] $1$
\item[C)] $2$
\item[D)] $3$
\item[E)] $4$
\end{itemize}
```

- Original answer: `C) $2$`
- Original method: $x^2+y^2-4x-6y+9=0$: centre $(2,3)$, $r^2=4+9-9=4$. The other has centre $(0,0)$ radius $3$. $d=\sqrt{13}$; $|3-2|=1<\sqrt{13}<5$ --- intersecting --- $2$ common tangents.

## B2

```latex
The radical axis of the circles $\;x^2+y^2+ax+by+c=0$ and $\;x^2+y^2+6x-4y+10=0$ is $\;2x-y+3=0$. What is $a+b$?
\begin{itemize}
\item[A)] $3$
\item[B)] $-3$
\item[C)] $13$
\item[D)] $-13$
\end{itemize}
```

- Original answer: `A) $3$`
- Original method: Subtract: $(a-6)x+(b+4)y+(c-10)=0$. Compare with $2x-y+3=0$: $a-6=2\Rightarrow a=8$; $b+4=-1\Rightarrow b=-5$; $c-10=3\Rightarrow c=13$. So $a+b=3$.

## B7

```latex
The circle $\;x^2+y^2=4$ is orthogonal to $\;x^2+y^2+8x-6y+C=0$. Find $C$.
\begin{itemize}
\item[A)] $4$
\item[B)] $-4$
\item[C)] $25$
\item[D)] $2$
\end{itemize}
```

- Original answer: `A) $4$`
- Original method: Second circle: centre $(-4,3)$, $r_2^2=25-C$. $d^2=16+9=25$. Orthogonal: $d^2=r_1^2+r_2^2=4+(25-C)=29-C\Rightarrow C=4$.

## B8

```latex
The circles $\;x^2+y^2=36$ and $\;(x-6)^2+y^2=36$ intersect. Find the length of their common chord.
```

- Original answer: `$6\sqrt{3}$`
- Original method: Equal radii $6$ on centres $6$ apart: radical axis is the perpendicular bisector $x=3$. Half-chord $=\sqrt{36-9}=3\sqrt{3}$, chord $=6\sqrt{3}$.

## C1

```latex
Two circles have the same radius. Their centres are $C_1(-2,1)$ and $C_2(3,-2)$. The circles intersect in two distinct points $P$ and $Q$. Which is the equation of the line $PQ$? \textit{\small(after TMUA 2021 Paper 1 Q1)}
\begin{itemize}
\item[A)] $5x+3y=4$
\item[B)] $3x-5y=4$
\item[C)] $5x-3y=4$
\item[D)] $5x-3y=1$
\end{itemize}
```

- Original answer: `C) $5x-3y=4$`
- Original method: Equal radii: subtract $(x+2)^2+(y-1)^2=(x-3)^2+(y+2)^2$, i.e.\ $x^2+4x+4+y^2-2y+1=x^2-6x+9+y^2+4y+4$, so $10x-6y=8$, i.e.\ $5x-3y=4$. The $x^2+y^2$ cancel in one line. The midpoint $(\tfrac12,-\tfrac12)$ satisfies $5(\tfrac12)-3(-\tfrac12)=4$ \checkmark.

## C5

```latex
The circle $x^2+y^2+4x-2y+C=0$ is orthogonal to the circle $x^2+y^2-4x+4y-1=0$. What is $C$? \textit{\small(after Oxbridge Paper 1 Q8)}
\begin{itemize}
\item[A)] $-11$
\item[B)] $-8$
\item[C)] $11$
\item[D)] $5$
\end{itemize}
```

- Original answer: `A) $-11$`
- Original method: $g_1=2$, $f_1=-1$; $g_2=-2$, $f_2=2$, $c_2=-1$. Orthogonality $2g_1g_2+2f_1f_2=c_1+c_2\Rightarrow2(2)(-2)+2(-1)(2)=C-1\Rightarrow-8-4=C-1\Rightarrow C=-11$. Geometric check: centres $(-2,1)$ and $(2,-2)$, $d^2=25$, $r_1^2=5-C$, $r_2^2=9$, $25=5-C+9\Rightarrow C=-11$ \checkmark.

## C7

```latex
The equal circles $C_1:(x+2)^2+(y-1)^2=3$ and $C_2:(x-4)^2+(y-1)^2=3$ have centres $6$ apart. A transverse common tangent with positive gradient makes an acute angle $\theta$ with the $x$-axis. What is $\tan\theta$? \textit{\small(adapted from TMUA 2020 Paper 1 Q16)}
\begin{itemize}
\item[A)] $\dfrac12$
\item[B)] $\dfrac{\sqrt2}{2}$
\item[C)] $\sqrt2$
\item[D)] $\dfrac{\sqrt3}{3}$
\end{itemize}
```

- Original answer: `B) $\dfrac{\sqrt2}{2}$`
- Original method: Equal radii $\sqrt3$ at $(-2,1)$ and $(4,1)$. Transverse tangent passes through midpoint $(1,1)$: line $y-1=m(x-1)$, i.e.\ $mx-y+1-m=0$. Distance from $(-2,1)$ to line $=|{-}3m|/\sqrt{m^2+1}=\sqrt3\Rightarrow9m^2=3(m^2+1)\Rightarrow6m^2=3\Rightarrow m^2=1/2\Rightarrow m=\sqrt2/2$ (positive).

## D1

```latex
The circles $C_1:(x+2)^2+(y-3)^2=18$ and $C_2:(x-7)^2+(y+6)^2=2$ have centres $O_1$ and $O_2$. What is the shortest distance between a point on $C_1$ and a point on $C_2$? \textit{\small(adapted from TMUA 2018 Paper 1 Q3)}
\begin{itemize}
\item[A)] $5\sqrt2-4$
\item[B)] $5\sqrt2-5$
\item[C)] $5\sqrt2$
\item[D)] $9\sqrt2$
\end{itemize}
```

- Original answer: `C) $5\sqrt2$`
- Original method: $O_1=(-2,3)$, $O_2=(7,-6)$, $O_1O_2=\sqrt{9^2+9^2}=9\sqrt2$, $r_1=\sqrt{18}=3\sqrt2$, $r_2=\sqrt2$, sum $4\sqrt2$, shortest $=9\sqrt2-4\sqrt2=5\sqrt2$. Externally disjoint ($d>r_1+r_2$).

## D2

```latex
The circles $(x+4)^2+(y+1)^2=64$ and $(x-8)^2+(y-4)^2=r^2$ ($r>0$) have exactly one point in common. What is the difference between the two possible values of $r$? \textit{\small(after TMUA 2019 Paper 1 Q6)}
\begin{itemize}
\item[A)] $8$
\item[B)] $16$
\item[C)] $26$
\item[D)] $42$
\end{itemize}
```

- Original answer: `B) $16$`
- Original method: Centre distance $d=\sqrt{12^2+5^2}=13$, $r_1=8$. One point $\Rightarrow|r-8|=13$ (internal) or $r+8=13$ (external) $\Rightarrow r=21$ or $5$, difference $16$.

## D5

```latex
A point $P$ has equal power with respect to the circles $x^2+y^2=1$ and $(x-6)^2+y^2=4$. What does the locus of $P$ describe? \textit{\small(adapted from JZMaths $/$ Vantage)}
\begin{itemize}
\item[A)] the line $x=\dfrac{11}{4}$
\item[B)] the circle $x^2+y^2=1$
\item[C)] the $y$-axis
\item[D)] a single point $\left(\dfrac{11}{4},0\right)$
\end{itemize}
```

- Original answer: `A) the line $x=\dfrac{11}{4}$`
- Original method: Equal powers $=$ radical axis: $x^2+y^2-1=(x-6)^2+y^2-4=x^2-12x+32+y^2\Rightarrow12x=33\Rightarrow x=11/4$, a vertical line. Exists even though circles are disjoint ($d=6>3$).
