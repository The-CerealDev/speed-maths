# Vault — geometry Day 7: scrapped 2026-09-29

Henry Koduthore's original Day 7 ("TMUA-style synthesis: loci and geometric logic"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 16 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet07.tex` (and `answers/ans07.tex`, `verify/sheet07_verify.py`).

## A3

```latex
The locus of $P$ with $PA=2\,PB$, where $A=(0,0)$ and $B=(6,0)$, is a circle. Write down the $x$-coordinate of its (relevant) endpoint on the $x$-axis where $y=0$ between $A$ and $B$.
```

- Original answer: `$4$`
- Original method: On the $x$-axis, between $A$ and $B$ we have $PA=x$ and $PB=6-x$, so $x=2(6-x)$, giving $x=4$. The Apollonius circle's two $x$-axis endpoints are $x=4$ and $x=12$.

## A5

```latex
The locus of points whose distance to the fixed point $(0,1)$ equals their distance to the fixed line $y=-1$ is a parabola. Write down a point on it other than the origin with integer coordinates.
```

- Original answer: `$(2,1)$`
- Original method: A point equidistant from focus $(0,1)$ and directrix $y=-1$ satisfies $\sqrt{x^2+(y-1)^2}=|y+1|$, i.e.\ $x^2=4y$; $(2,1)$ works since $4=4$.

## B1

```latex
The circle of Apollonius for $PA = 2PB$ with $A=(0,0)$, $B=(6,0)$ has radius?
\begin{itemize}
\item[A)] $4$
\item[B)] $6$
\item[C)] $8$
\item[D)] $12$
\end{itemize}
```

- Original answer: `A) $4$`
- Original method: On the $x$-axis, $|x|=2|x-6|$ gives the endpoints $x=4$ and $x=12$; the circle between them has centre $(8,0)$ and radius $4$.

## B4

```latex
The distance from $P(x,y)$ to the origin is $\sqrt{x^2+y^2}$. The locus $\sqrt{x^2+y^2}=1$ is a circle. Write down its circumference.
```

- Original answer: `$2\pi$`
- Original method: Circumference $=2\pi r=2\pi\cdot 1=2\pi$.

## B8

```latex
The locus of $P$ with $PA=PB$ where $A=(0,0)$ and $B=(6,0)$ is the perpendicular bisector $\mathbf{x=3}$. Write down the distance from $(3,0)$ to $(0,0)$.
```

- Original answer: `$3$`
- Original method: Distance from $(3,0)$ to the origin is $\sqrt{9}=3$.

## C1

```latex
\vspace{0pt}
The locus of $P$ with $PA=2\,PB$ and $A=(-2,0)$, $B=(4,0)$ is a circle (Apollonius). What is its centre? \textit{\small(after TMUA 2022 Paper 1 Q7)}
\begin{itemize}
\item[A)] $(6,0)$
\item[B)] $(8,0)$
\item[C)] $(10,0)$
\item[D)] $(2,0)$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.45]
\draw[->] (-3,0) -- (9,0) node[right]{\tiny $x$};
\draw[->] (0,-2) -- (0,2);
\draw[thick] (-2,0) circle (0.08) node[below]{\tiny $A(-2,0)$};
\draw[thick] (4,0) circle (0.08) node[below]{\tiny $B(4,0)$};
\draw[thick, dashed] (6,0) circle (1.5);
\draw[fill=black] (6,0) circle (1pt) node[below]{\tiny $C$};
\node at (6,1.7) {\tiny $PA=2PB$};
\end{tikzpicture}
\end{minipage}
```

- Original answer: `A) $(6,0)$`
- Original method: Square $PA=2PB$: $(x+2)^2+y^2=4\big((x-4)^2+y^2\big)$. Expand: $x^2+4x+4+y^2=4x^2-32x+64+4y^2$, so $3x^2-36x+60+3y^2=0$, i.e.\ $x^2-12x+20+y^2=0$, $(x-6)^2+y^2=16$. Centre $(6,0)$, radius $4$. Option A. The $x$-axis endpoints from $|x+2|=2|x-4|$ are $x=2$ (internal) and $x=10$, midpoint $6$.

## C3

```latex
Fil argues: ``Let $D$ lie on segment $AB$ and $CD$ bisect $\angle C$. By the angle-bisector theorem $AD/DB=CA/CB$; hence any point $P$ with $PA=PB$ must lie on the bisector of $\angle C$.'' Where is the flaw? \textit{\small(after TMUA 2019 Paper 2 Q14)}
\begin{itemize}
\item[A)] The proof assumes $D$ lies {\em between} $A$ and $B$ (betweenness/convexity) without establishing it; $D$ could lie on the extension of $AB$ outside the segment.
\item[B)] Squaring the distance ratio loses the sign, so the locus is a single point not a circle.
\item[C)] The angle-bisector theorem is false for obtuse triangles.
\item[D)] There is no flaw; the conclusion is correct.
\end{itemize}
```

- Original answer: `A)`
- Original method: Fil invokes the internal angle-bisector theorem which requires $D$ to be {\em interior} to $AB$. The diagram may place $D$ on the extension of $AB$ beyond $B$ (or beyond $A$) where the external bisector ratio is $AD/DB=-CA/CB$; without proving convexity/betweenness the betweenness hypothesis is not established. This is the classic ``all triangles are isosceles'' fallacy class. Hence the argument assumes what it must prove. Option A names the betweenness gap; B miscasts a squared modulus, C misstates the theorem, D claims no flaw.

## C4

```latex
$PQRS$ is a parallelogram labelled anticlockwise. Consider: I.\ $PQ=QR$ \quad II.\ $PR\perp QS$ \quad III.\ $\angle PQR = 90^\circ$. Which of these conditions is/are individually {\em sufficient} for $PQRS$ to be a square? \textit{\small(after TMUA 2020 Paper 2 Q7)}
\begin{itemize}
\item[A)] I only
\item[B)] II only
\item[C)] III only
\item[D)] I and III only
\item[E)] none of them individually (all insufficient alone)
\end{itemize}
```

- Original answer: `E) none of them individually (all insufficient alone)`
- Original method: For a parallelogram: I.\ $PQ=QR$ forces a rhombus; a rhombus with angles $60^\circ,120^\circ$ (e.g.\ equilateral-parallelogram) is not a square. II.\ $PR\perp QS$ also forces a rhombus (equivalently to I) but not a square (same counterexample). III.\ $\angle PQR=90^\circ$ forces a rectangle; a $2\times3$ rectangle is not a square. So each alone is insufficient; $I+III$ or $II+III$ together would be sufficient. Hence no single condition suffices, option E. This mirrors TMUA 2020 P2 Q7 answer ``none individually sufficient'' (official answer H in the 8-option paper, here condensed to E).

## C5

```latex
In $\triangle PQR$, $PR=4$, $QR=p$ and $\angle RPQ=30^\circ$. For which values of $p$ does this information {\em uniquely} determine the length $PQ$? \textit{\small(after TMUA 2018 Paper 2 Q14)}
\begin{itemize}
\item[A)] $p=2$
\item[B)] $p=\sqrt3$
\item[C)] $1\le p<2$
\item[D)] $p\ge4$
\item[E)] $p=2$ or $p\ge4$
\item[F)] $p=\sqrt3$ or $p\ge4$
\item[G)] $p<4$
\item[H)] $p\ge2$
\end{itemize}
```

- Original answer: `E) $p=2$ or $p\ge4$`
- Original method: By the sine rule $\sin R / PR = \sin 30^\circ / p$, so $\sin R = 2/p$. The ambiguous case: for $p<4$ there are potentially two values of $R$ giving two triangles, except when $\sin R=1$ ($p=2$) where the two coalesce to a right-angled triangle uniquely determined. For $p\ge PR=4$ the side opposite the given angle is at least the other given side, so the angle $R$ is uniquely acute; $p=2$ also unique. Hence exactly $p=2$ or $p\ge4$ gives a unique $PQ$; all other $p<4$, $p\ne2$ give two possible $PQ$ (or none for $p<2\sin30^\circ$). This scales the official TMUA 2018 P2 Q14 answer $p=1$ or $p\ge2$ (with $PR=2$) by factor $2$.

## C7

```latex
The Apollonius circle $PA=3\,PB$ with $A=(0,0)$, $B=(6,0)$ is $(x-\tfrac{27}{4})^2+y^2=(\tfrac94)^2$. What is the greatest distance from the origin to a point on this circle? \textit{\small(after TMUA 2022 Paper 1 Q7)}
\begin{itemize}
\item[A)] $9$
\item[B)] $7.5$
\item[C)] $12$
\item[D)] $6$
\end{itemize}
```

- Original answer: `A) $9$`
- Original method: For $PA=3PB$, $x^2+y^2=9\big((x-6)^2+y^2\big)$ gives $8x^2-108x+8y^2+324=0$, i.e.\ $(x-\tfrac{27}{4})^2+y^2=(\tfrac94)^2$. Centre $C(\tfrac{27}{4},0)= (6.75,0)$, radius $r=\tfrac94=2.25$. The furthest point from the origin on the circle is on the ray $OC$ beyond $C$: $OC+r=6.75+2.25=9$; the nearest is $OC-r=4.5$. So $\max OP=9$, option A.

## C8

```latex
Fil finds the circle of Apollonius $PA=3PB$ with $A=(0,0)$, $B=(2,0)$ by writing $(x-2)^2+y^2=9$ and claiming this is the locus. Where is the error? \textit{\small(after TMUA 2019 Paper 2 Q14)}
\begin{itemize}
\item[A)] His equation is a circle centred at $B$ with radius $3$, but the true locus from $x^2+y^2=9\big((x-2)^2+y^2\big)$ is $\left(x-\tfrac94\right)^2+y^2=\tfrac{9}{16}$ (centre $(\tfrac94,0)$, radius $\tfrac34$); it incorrectly ignores the distance to $A$.
\item[B)] Squaring loses the sign information, so the locus is really a single point.
\item[C)] The set $PA=3PB$ is a straight line, not a circle at all.
\item[D)] There is no error; $(x-2)^2+y^2=9$ is correct.
\end{itemize}
```

- Original answer: `A)`
- Original method: Expand correctly: $x^2+y^2=9\big((x-2)^2+y^2\big)$ gives $x^2+y^2=9x^2-36x+36+9y^2$, so $8x^2-36x+8y^2+36=0$, i.e.\ $(x-\tfrac94)^2+y^2=\tfrac{9}{16}$, centre $(\tfrac94,0)$, radius $\tfrac34$. Fil's $(x-2)^2+y^2=9$ is the circle centred at $B=(2,0)$ with radius $3$; it uses only $PB$ and ignores $A$ entirely. Option A's locus is the true Apollonius circle; B claims the locus collapses, C claims it is a line ($k=1$ only), D claims no error.

## D1

```latex
The locus of $P$ with $PA^2+PB^2=34$, where $A=(-3,0)$, $B=(3,0)$, is a circle. What is its radius? \textit{\small(after BMO1 2017 Q4 $/$ TMUA 2022 Paper 1 Q7)}
\begin{itemize}
\item[A)] $2\sqrt2$
\item[B)] $4$
\item[C)] $\sqrt8$
\item[D)] $\sqrt{34}$
\end{itemize}
```

- Original answer: `A) $2\sqrt2$`
- Original method: $PA^2=(x+3)^2+y^2$, $PB^2=(x-3)^2+y^2$. Sum $=2x^2+18+2y^2=34$, so $x^2+y^2=8$, i.e.\ $(x-0)^2+y^2=8$, a circle centred at the midpoint $(0,0)$ with $r^2=8$, $r=2\sqrt2$. This is the $PA^2+PB^2$ locus (Apollonius's theorem generalisation). Check: $PA^2+PB^2=2m^2+AB^2/2$ with $m=OP$. Option A; B is $r^2$, D is total sum.

## D2

```latex
The graph $|x|+|y|=3$ is a square (diamond) with vertices $(3,0),(0,3),(-3,0),(0,-3)$. What is the finite area it encloses? \textit{\small(after TMUA 2021 Paper 1 Q9)}
\begin{itemize}
\item[A)] $6$
\item[B)] $12$
\item[C)] $18$
\item[D)] $9$
\end{itemize}
```

- Original answer: `C) $18$`
- Original method: $|x|+|y|=3$ is four lines $x+y=3$, $x-y=3$, etc., forming a diamond with vertices $(3,0),(0,3),(-3,0),(0,-3)$. Its diagonals are $6$ and $6$, so area $=\frac12\cdot6\cdot6=18$ (equivalently four right triangles each $\tfrac12\cdot3\cdot3=4.5$). For $|x|+|y|=1$ the area is $2$ (TMUA 2021 P1 Q9 answer C), scaling by factor $3^2$ gives $2\cdot9=18$. Option C.

## D3

```latex
The diagram shows a kite $PQRS$ whose diagonals meet at $O$ with $OP=x$, $OQ=y$, $OR=x$, $OS=z$. Which condition is {\em necessary and sufficient} for $\angle SPQ=90^\circ$? \textit{\small(after TMUA 2022 Paper 2 Q11)}
\begin{itemize}
\item[A)] $x=y=z$
\item[B)] $2x=y+z$
\item[C)] $x^2=yz$
\item[D)] $y=z$
\item[E)] $y^2=x^2+z^2$
\end{itemize}
```

- Original answer: `C) $x^2=yz$`
- Original method: Put $O$ at origin, let $SP^2=x^2+z^2$, $PQ^2=x^2+y^2$, $SQ^2=(y+z)^2$. Then $\triangle SPQ$ right at $P$ iff $SP^2+PQ^2=SQ^2$ (Pythagoras): $(x^2+z^2)+(x^2+y^2)=(y+z)^2$, so $2x^2+y^2+z^2=y^2+2yz+z^2$, i.e.\ $2x^2=2yz$, $x^2=yz$. Conversely $x^2=yz$ reverses the steps; hence the condition is both necessary and sufficient. This is exactly TMUA 2022 P2 Q11 (official answer C). Option C.

## D4

```latex
The circles $C_1:x^2+y^2=25$ and $C_2:(x-4)^2+y^2=9$ intersect at $P,Q$. What is the length $PQ$? \textit{\small(after BMO1 2017 Q4 $/$ TMUA Practice Paper 2 Q9)}
\begin{itemize}
\item[A)] $3$
\item[B)] $6$
\item[C)] $\dfrac{4\sqrt{14}}{3}$
\item[D)] $\dfrac{24}{5}$
\end{itemize}
```

- Original answer: `B) $6$`
- Original method: Radical axis: subtract $x^2+y^2=25$ and $(x-4)^2+y^2=9$, i.e.\ $x^2-(x-4)^2=16$, so $8x-16=16$, $x=4$. Distance from $O_1(0,0)$ to the line $x=4$ is $4$. Half-chord $=\sqrt{r_1^2-d_{\rm axis}^2}=\sqrt{25-16}=3$, so full chord $PQ=6$. Check with $O_2$: $4-4=0$, distance $0$, half-chord also $\sqrt{9-0}=3$. Option B. The diagram's dashed line is $x=4$.

## D5

```latex
Let the Apollonius circle $PA=2PB$ with $A=(0,0)$, $B=(6,0)$ be $(x-8)^2+y^2=16$. The triangle $PAB$ varies as $P$ runs over this circle. What is its maximum possible area? \textit{\small(after TMUA 2022 Paper 1 Q7 $/$ BMO1 2017 Q4)}
```

- Original answer: `$12$`
- Original method: Apollonius $PA=2PB$ with $A(0,0),B(6,0)$ is $(x-8)^2+y^2=16$, centre $C(8,0)$, radius $r=4$. For fixed base $AB=6$, $[PAB]=\tfrac12\cdot AB\cdot|y_P|$, so maximise $|y_P|$ among points on the circle: $\max|y_P|=r=4$ (topmost point $(8,4)$). Hence $\max[PAB]=\tfrac12\cdot6\cdot4=12$. Check: $(8,4)$ indeed satisfies $(0,4)$? $PA=\sqrt{80}=4\sqrt5$, $PB=\sqrt{20}=2\sqrt5$, ratio $2$ correct. Uniqueness up to reflection in $x$-axis.
