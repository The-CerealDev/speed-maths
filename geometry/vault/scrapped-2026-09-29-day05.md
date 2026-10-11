# Vault — geometry Day 5: scrapped 2026-09-29

Henry Koduthore's original Day 5 ("Tangents from an external point"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 29 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet05.tex` (and `answers/ans05.tex`, `verify/sheet05_verify.py`).

## A1

```latex
Write down the length of the tangent from $(0,5)$ to $x^2+y^2=9$.
```

- Original answer: `$4$`
- Original method: Tangent length $=\sqrt{OP^2-r^2}=\sqrt{25-9}=\sqrt{16}=4$. Right triangle $OP$ hypotenuse $5$, leg $r=3$.

## A2

```latex
The point $(0,5)$ sits outside $x^2+y^2=9$ with $OP=5$ and $r=3$. Write down $\tan\frac{\theta}{2}$, where $\theta$ is the angle between the two tangents.
```

- Original answer: `$\dfrac{3}{4}$`
- Original method: $\tan\frac{\theta}{2}=\frac{r}{\sqrt{OP^2-r^2}}=\frac{3}{4}$. The half-angle uses the tangent length $4$ from A1 as adjacent.

## A3

```latex
Write down the equation of the chord of contact (polar) drawn from the point $(5,3)$ to $x^2+y^2=25$.
```

- Original answer: `"$5x+3y=25$"`
- Original method: Polar of $(x_1,y_1)$ w.r.t.\ $x^2+y^2=r^2$ is $xx_1+yy_1=r^2$: $5x+3y=25$.

## A4

```latex
The circle $x^2+y^2=25$ has director circle $x^2+y^2=2r^2$. Write down the radius of that director circle.
```

- Original answer: `$5\sqrt{2}$`
- Original method: $r^2=25$, director circle $x^2+y^2=2r^2=50$, radius $\sqrt{50}=5\sqrt{2}$. Radius scales by $\sqrt2$.

## A7

```latex
Write down the equation of the chord of contact drawn from $(5,0)$ to $x^2+y^2=4$ (the two tangency points join in a vertical line).
```

- Original answer: `"$5x=4$"`
- Original method: Polar $xx_1+yy_1=r^2$ with $(5,0)$, $r^2=4$: $5x=4$, i.e.\ $x=4/5$, the vertical chord.

## A8

```latex
A tangent from the point $P$ to $x^2+y^2=25$ has length $12$. Write down $OP$.
```

- Original answer: `$13$`
- Original method: $OP=\sqrt{12^2+5^2}=\sqrt{144+25}=13$ by $5$--$12$--$13$.

## A10

```latex
The chord of contact from the point $P$ to $x^2+y^2=16$ is the line $x+y=4$. Write down $P$.
```

- Original answer: `"$(4,4)$"`
- Original method: Compare $xx_1+yy_1=16$ with $x+y=4$: multiply by $4$ to get $4x+4y=16$, so $(x_1,y_1)=(4,4)$.

## B1

```latex
The length of the tangent from $(3,4)$ to $x^2+y^2=9$ is?
\begin{itemize}
\item[A)] $\sqrt{7}$
\item[B)] $4$
\item[C)] $5$
\item[D)] $2$
\end{itemize}
```

- Original answer: `B) $4$`
- Original method: $OP=\sqrt{9+16}=5$, $r=3$, tangent $=\sqrt{25-9}=4$.

## B3

```latex
Write down the equation of the chord of contact drawn from the point $(3,5)$ to $x^2+y^2=25$.
```

- Original answer: `"$3x+5y=25$"`
- Original method: Polar $xx_1+yy_1=25$ with $(3,5)$ gives $3x+5y=25$.

## B4

```latex
The director circle of $x^2+y^2=4$ has radius?
\begin{itemize}
\item[A)] $2$
\item[B)] $2\sqrt{2}$
\item[C)] $4$
\item[D)] $\sqrt{2}$
\end{itemize}
```

- Original answer: `B) $2\sqrt{2}$`
- Original method: Director circle $x^2+y^2=2r^2=8$, radius $\sqrt8=2\sqrt2$.

## B5

```latex
The length of the tangent from $(1,2)$ to $x^2+y^2=1$ is?
\begin{itemize}
\item[A)] $1$
\item[B)] $\sqrt{5}$
\item[C)] $2$
\item[D)] $\sqrt{3}$
\end{itemize}
```

- Original answer: `C) $2$`
- Original method: $\sqrt{1^2+2^2-1}= \sqrt{4}=2$.

## B6

```latex
A tangent from $P$ to a circle of radius $5$ has length $12$. How far is $P$ from the centre?
\begin{itemize}
\item[A)] $17$
\item[B)] $7$
\item[C)] $13$
\item[D)] $\sqrt{119}$
\end{itemize}
```

- Original answer: `C) $13$`
- Original method: $OP=\sqrt{12^2+5^2}=13$.

## B7

```latex
The chord of contact from $P=(a,0)$ to $x^2+y^2=16$ is the line $x=4$. Find $a$.
\begin{itemize}
\item[A)] $2$
\item[B)] $4$
\item[C)] $8$
\item[D)] $16$
\end{itemize}
```

- Original answer: `B) $4$`
- Original method: Polar of $(a,0)$ is $ax=16$, i.e.\ $x=16/a$. Set $16/a=4\Rightarrow a=4$.

## B8

```latex
The two tangents from $P$ to $x^2+y^2=25$ meet at right angles (so $P$ lies on the director circle). Write down the length of each tangent.
```

- Original answer: `$5$`
- Original method: Orthogonal tangents $\Rightarrow P$ on director circle: $OP^2=2r^2=50$, tangent $=\sqrt{50-25}=5$.

## B9

```latex
The tangent to $x^2+y^2=8$ with slope $1$ has positive $y$-intercept equal to?
\begin{itemize}
\item[A)] $4$
\item[B)] $2\sqrt{2}$
\item[C)] $8$
\item[D)] $4\sqrt{2}$
\end{itemize}
```

- Original answer: `A) $4$`
- Original method: Tangent $y=mx\pm r\sqrt{1+m^2}$: $r=\sqrt8$, $m=1\Rightarrow c=\sqrt8\sqrt2=4$.

## B10

```latex
A tangent from $P$ to a circle has length $6$, and $OP=10$. Write down the circle's radius.
```

- Original answer: `$8$`
- Original method: $r^2=OP^2-\ell^2=100-36=64\Rightarrow r=8$.

## C1

```latex
From $P(8,12)$, two tangents are drawn to $x^2+y^2=36$ (centre $O$, $r=6$). Let $T_1T_2$ be the chord of contact. What is the distance from $O$ to the line $T_1T_2$? \textit{\small(after TMUA 2020 Paper 1 Q16 / BMO1 2013 Q4)}
\begin{itemize}
\item[A)] $\tfrac{9}{5}$
\item[B)] $\tfrac{18}{5}$
\item[C)] $\tfrac{36}{5}$
\item[D)] $\tfrac{9}{2}$
\end{itemize}
```

- Original answer: `$\dfrac{9\sqrt{13}}{13}$`
- Original method: Polar is $8x+12y=36\Rightarrow 2x+3y=9$. $OP=\sqrt{8^2+12^2}=4\sqrt{13}$, and $d=r^2/OP=36/(4\sqrt{13})=9/\sqrt{13}=9\sqrt{13}/13$. The listed options give $18/5$ which is $r^2/OP$ for $P(6,8)$ ($OP=10$); for the printed $P(8,12)$ the exact value is $9/\sqrt{13}$.

## C2

```latex
The locus of points $P$ where the tangent length to $x^2+y^2=4$ equals the tangent length to $(x-6)^2+y^2=16$ is the radical axis. Which line is it? \textit{\small(adapted from TMUA 2018 Paper 1 Q7)}
\begin{itemize}
\item[A)] $x=1$
\item[B)] $x=2$
\item[C)] $x=3$
\item[D)] $x=4$
\end{itemize}
```

- Original answer: `B) $x=2$`
- Original method: Equal powers: $x^2+y^2-4=(x-6)^2+y^2-16\Rightarrow -4=-12x+20\Rightarrow x=2$.

## C3

```latex
\vspace{0pt}
The circle $x^2+y^2-6x-8y+24=0$ has centre $(3,4)$, $r=1$. The point $P(6,8)$ is outside. What is the length of the tangent from $P$ to the circle? \textit{\small(after MAT 2021 Q5)}
\begin{itemize}
\item[A)] $4$
\item[B)] $2\sqrt5$
\item[C)] $5$
\item[D)] $\sqrt{26}$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.42]
\draw (0,0) circle (1.2);
\draw (1.2,0) -- (2.5,0.8);
\draw[fill=black] (0,0) circle (1pt) node[below]{\tiny $O$};
\draw (0,0) -- (1.2,0) node[midway, below]{\tiny $r$};
\end{tikzpicture}
\end{minipage}
```

- Original answer: `$2\sqrt{6}$`
- Original method: Centre $C=(3,4)$, $PC=\sqrt{9+16}=5$, $r=1$: tangent $=\sqrt{25-1}=2\sqrt6\approx4.90$. None of the printed numerals equals this exactly; $4$ would need $r=3$.

## C4

```latex
For the $13$-$14$-$15$ triangle ($s=21$, $r=4$), the two tangent lengths from the vertex opposite side $14$ are $s-b$. With $b=14$, what is that length? \textit{\small(adapted from BMO1 2015 Q3)}
\begin{itemize}
\item[A)] $6$
\item[B)] $7$
\item[C)] $8$
\item[D)] $9$
\end{itemize}
```

- Original answer: `B) $7$`
- Original method: $s-b=21-14=7$. The $s-a$ rule gives equal tangents from each vertex.

## C5

```latex
The circle $(x-4)^2+y^2=9$ has director circle $x^2+y^2=2r^2$ for a centred circle, but this circle is translated. What is the locus of points from which the two tangents to $(x-4)^2+y^2=9$ are perpendicular? \textit{\small(after TMUA 2022 Paper 1 Q19)}
\begin{itemize}
\item[A)] $(x-4)^2+y^2=18$
\item[B)] $(x-4)^2+y^2=9$
\item[C)] $x^2+y^2=18$
\item[D)] $x^2+y^2=9$
\end{itemize}
```

- Original answer: `A) $(x-4)^2+y^2=18$`
- Original method: Director circle is centred at the same centre $(4,0)$ with radius $r\sqrt2=3\sqrt2$, so $(x-4)^2+y^2=18$.

## C6

```latex
\vspace{0pt}
The point $(8,6)$ is at distance $10$ from the origin. Tangents from $(8,6)$ to $x^2+y^2=1$ have length $\sqrt{99}$. What is the distance from the origin to the chord of contact? \textit{\small(adapted from TMUA 2020 Paper 1 Q16)}
\begin{itemize}
\item[A)] $\tfrac{1}{10}$
\item[B)] $\tfrac{1}{\sqrt{101}}$
\item[C)] $\tfrac{1}{\sqrt{99}}$
\item[D)] $\tfrac{10}{\sqrt{101}}$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.4]
\draw (0,0) circle (1.2);
\draw (-0.8,-0.8) -- (0.8,0.8);
\draw[fill=black] (0,0) circle (1pt);
\end{tikzpicture}
\end{minipage}
```

- Original answer: `A) $\dfrac{1}{10}$`
- Original method: Polar $8x+6y=1$, $d=1/10$; equivalently $d=r^2/OP=1/10$. Since $d<r$, the chord cuts the circle.

## C7

```latex
The triangle with sides $13,14,15$ has incircle touching $BC$ at $D$. If $BD=6$, $DC=9$, and $s=21$, the two equal tangents from $A$ are $s-a$. What is $AE$ (tangents from $A$)? \textit{\small(after BMO1 2020 Q3)}
\begin{itemize}
\item[A)] $6$
\item[B)] $7$
\item[C)] $8$
\item[D)] $9$
\end{itemize}
```

- Original answer: `A) $6$`
- Original method: $a=BC=15$, $s-a=21-15=6$. The incircle tangents from each vertex are $s-a$, $s-b$, $s-c$.

## C8

```latex
The chord of contact of $(2,1)$ w.r.t. $x^2+y^2=1$ is $2x+y=1$. What is its distance from the origin, and is it inside, on, or outside the circle? \textit{\small(adapted from TMUA 2021 Paper 2 Q7)}
\begin{itemize}
\item[A)] $\tfrac{1}{\sqrt5}$ (inside, $d<r$)
\item[B)] $\tfrac{1}{\sqrt5}$ (outside, $d>r$)
\item[C)] $\tfrac{\sqrt5}{5}$ (inside)
\item[D)] $1$ (tangent)
\end{itemize}
```

- Original answer: `A) $\dfrac{1}{\sqrt5}$`
- Original method: Distance $=1/\sqrt{4+1}=1/\sqrt5=\sqrt5/5\approx0.45<r=1$, so the line cuts the circle (inside).

## D1

```latex
\vspace{0pt}
Two tangents from $P$ to $x^2+y^2=9$ with $OP=6$ enclose angle $\theta$. What is $\theta$? \textit{\small(after TMUA 2018 Paper 1 Q7 / BMO1 2023 Q4)}
\begin{itemize}
\item[A)] $30^\circ$
\item[B)] $60^\circ$
\item[C)] $90^\circ$
\item[D)] $120^\circ$
\end{itemize}
\end{minipage}\hfill

\vspace{0pt}
\centering
\begin{tikzpicture}[scale=0.45]
\draw (0,0) circle (1.2);
\draw (0,0) -- (1.5,0.8);
\draw (1.5,0.8) -- (0.8,1.5);
\node at (0.6,0.6) {\tiny $\theta$};
\draw[fill=black] (0,0) circle (1pt);
\end{tikzpicture}
\end{minipage}
```

- Original answer: `B) $60^{\circ}$`
- Original method: $\sin\frac{\theta}{2}=r/OP=3/6=1/2\Rightarrow \theta/2=30^{\circ}\Rightarrow\theta=60^{\circ}$.

## D2

```latex
From $P$ to $x^2+y^2=25$, tangent length is $5\sqrt3$. Find $OP$ (use $OP^2=r^2+\text{tangent}^2$). \textit{\small(adapted from TMUA 2020 Paper 1 Q16)}
\begin{itemize}
\item[A)] $10$
\item[B)] $5\sqrt{10}$
\item[C)] $10\sqrt{3}$
\item[D)] $75$
\end{itemize}
```

- Original answer: `A) $10$`
- Original method: $OP^2=25+75=100\Rightarrow OP=10$.

## D3

```latex
The chord of contact from $P(3,3)$ to $x^2+y^2=9$ is $x+y=3$. What is its length? (Hint: distance from $O$ to chord is $3/\sqrt2$, $r=3$) \textit{\small(adapted from TMUA 2019 Paper 1 Q6)}
\begin{itemize}
\item[A)] $3\sqrt2$
\item[B)] $\tfrac{3\sqrt{14}}{2}$
\item[C)] $3\sqrt{6}$
\item[D)] $6$
\end{itemize}
```

- Original answer: `A) $3\sqrt2$`
- Original method: Distance $d=3/\sqrt2$, half-chord $\sqrt{9-9/2}=3/\sqrt2$, chord $=3\sqrt2$.

## D4

```latex
Two tangents from $P$ make $60^\circ$ and $OP=10$, $r=OP\sin(\theta/2)=5$, tangent length $=OP\cos(\theta/2)$. What is the length? \textit{\small(after BMO1 2015 Q3)}
\begin{itemize}
\item[A)] $5$
\item[B)] $5\sqrt3$
\item[C)] $10$
\item[D)] $5/2$
\end{itemize}
```

- Original answer: `B) $5\sqrt3$`
- Original method: $r=10\sin30^{\circ}=5$, tangent $=\sqrt{100-25}=5\sqrt3=10\cos30^{\circ}$.

## D5

```latex
The polar of $(9,12)$ w.r.t. $x^2+y^2=81$ is $3x+4y=27$. What is its distance from the origin, and is $P$ outside/inside/on? \textit{\small(adapted from MAT 2021 Q5)}
\begin{itemize}
\item[A)] $27/5$ (outside, $d<r$? No, $d=27/5=5.4<r=9$? Actually $r=9$, $d=5.4<r$, so chord inside)
\item[B)] $27/15$ (outside)
\item[C)] $9/5$ (inside)
\item[D)] $81/15$ (outside)
\end{itemize}
```

- Original answer: `A) $\dfrac{27}{5}$`
- Original method: $9x+12y=81\Rightarrow 3x+4y=27$, $d=27/5=5.4<r=9$ (chord inside), $OP=15>r$ (point outside).
