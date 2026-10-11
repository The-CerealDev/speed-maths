# Vault — geometry Day 1: scrapped 2026-09-29

Henry Koduthore's original Day 1 ("Coordinate geometry: lines, gradients, distances and polygon areas"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 12 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet01.tex` (and `answers/ans01.tex`, `verify/sheet01_verify.py`).

## B10

```latex
Using the shoelace formula, find the area of the triangle with vertices $(1,1)$, $(4,2)$, $(2,6)$.
```

- Original answer: `$7$`
- Original method: $\frac12|1\cdot2+4\cdot6+2\cdot1-(1\cdot4+2\cdot2+6\cdot1)|=\frac12|2+24+2-(4+4+6)|=\frac12|28-14|=7$.

## C1

```latex
The lines $l_1: y = 6 - 2x$ and $l_2: y = \tfrac12 x - 4$ are perpendicular and intersect at $P$. The three lines $l_1$, $l_2$ and the $x$-axis enclose a triangle $T$. What is the area of $T$? \textit{\small(after TMUA 2017 Paper 1 Q3)}
\begin{itemize}
\item[A)] $ \tfrac{81}{5}$
\item[B)] $ \tfrac{54}{5}$
\item[C)] $ \tfrac{81}{10}$
\item[D)] $ \tfrac{27}{2}$
\end{itemize}
```

- Original answer: `A) $\tfrac{81}{5}$`
- Original method: $l_1$ has $x$-intercept $3$ ($6-2x=0$), $l_2$ has $x$-intercept $-6$ ($x/2+3=0$). They meet where $6-2x = x/2+3 \Rightarrow 5x/2=3 \Rightarrow x=6/5$, $y=18/5$. Base on $x$-axis is $3-(-6)=9$, height is $y_P=18/5$, so area $=\tfrac12\cdot9\cdot\tfrac{18}{5}= \tfrac{81}{5}$. Shoelace on $(3,0),(-6,0),(6/5,18/5)$ gives the same $81/5$.

## C2

```latex
The perpendicular bisector of the segment joining $A(2,-6)$ and $B(5,4)$ meets the $x$-axis at $P$. What is the $x$-coordinate of $P$? \textit{\small(after TMUA Specimen Paper 1 Q3)}
\begin{itemize}
\item[A)] $ \tfrac16$
\item[B)] $ \tfrac13$
\item[C)] $ \tfrac{19}{5}$
\item[D)] $ \tfrac{41}{6}$
\end{itemize}
```

- Original answer: `A) $\tfrac16$`
- Original method: Midpoint $M=(7/2,-1)$, gradient $AB=(4-(-6))/(5-2)=10/3$, so perp gradient $-3/10$. Equation $y+1=-3/10(x-7/2)$. At $y=0$: $1=-3/10(x-7/2)\Rightarrow x-7/2=-10/3\Rightarrow x=7/2-10/3=21/6-20/6=1/6$. Equidistance check: $(p-2)^2+36=(p-5)^2+16$ with $p=1/6$ gives $49/36+36=...$ \checkmark.

## C3

```latex
Two circles have the same radius $r$. Their centres are $C_1(-2,1)$ and $C_2(3,-2)$. The circles intersect in two distinct points $P$ and $Q$. Which line is the common chord $PQ$? \textit{\small(adapted from TMUA 2021 Paper 1 Q1)}
\begin{itemize}
\item[A)] $5x-3y=1$
\item[B)] $5x-3y=4$
\item[C)] $5x+3y=1$
\item[D)] $3x-5y=4$
\end{itemize}
```

- Original answer: `B) $5x-3y=4$`
- Original method: Subtract: $(x+2)^2+(y-1)^2-r^2=0$ and $(x-3)^2+(y+2)^2-r^2=0$. $x^2$ and $y^2$ cancel: $(4x+4-2y+1)-(-6x+9+4y+4)=10x-6y-8=0$, so $5x-3y=4$. The $r^2$ terms cancel too --- the radical axis needs no radius.

## C4

```latex
For which values of $p$ does $x^2-2px+y^2-6y-p^2+8p+9=0$ represent a (real) circle? \textit{\small(after TMUA 2022 Paper 1 Q2)}
\begin{itemize}
\item[A)] $p<-1$ or $p>9$
\item[B)] $-1<p<9$
\item[C)] $0<p<4$
\item[D)] $p<0$ or $p>4$
\end{itemize}
```

- Original answer: `D) $p<0$ or $p>4$`
- Original method: Complete squares: $(x-p)^2-p^2+(y-3)^2-9-p^2+8p+9=0\Rightarrow (x-p)^2+(y-3)^2=2p^2-8p=2p(p-4)$. Radius$^2>0$ needs $p(p-4)>0$, so $p<0$ or $p>4$. At $p=0,4$ radius $0$ (a point).

## C6

```latex
The curve $y=4x^2$ is translated by $\begin{pmatrix}3\\-5\end{pmatrix}$, then reflected in the $x$-axis, then stretched parallel to the $x$-axis with scale factor $2$. What is the equation of the final curve? \textit{\small(adapted from TMUA 2020 Paper 1 Q10)}
\begin{itemize}
\item[A)] $y=-x^2+12x-31$
\item[B)] $y=-x^2+12x-41$
\item[C)] $y=-16x^2+48x-31$
\item[D)] $y=16x^2-48x+41$
\end{itemize}
```

- Original answer: `A) $y=-x^2+12x-31$`
- Original method: Start $y=4x^2$. Translate: $(x,y)\to(x-3,y+5)$ gives $y+5=4(x-3)^2$. Reflect $y\to -y$: $-y+5=4(x-3)^2$ or $y=-4(x-3)^2+5$. Stretch $x\to x/2$: $y=-4(x/2-3)^2+5=-4(x^2/4-3x+9)+5=-x^2+12x-31$.

## C7

```latex
The circles $(x+4)^2+(y+1)^2=64$ and $(x-8)^2+(y-4)^2=r^2$ ($r>0$) have exactly one point in common. What is the difference between the two possible values of $r$? \textit{\small(adapted from TMUA 2019 Paper 1 Q6)}
\begin{itemize}
\item[A)] $8$
\item[B)] $16$
\item[C)] $26$
\item[D)] $42$
\end{itemize}
```

- Original answer: `B) $16$`
- Original method: Centre distance $d=\sqrt{(12)^2+5^2}=13$. One point $\Rightarrow$ internally or externally tangent: $d=|r\pm r_1|$, so $r=|13\pm8|$ gives $r=21$ or $r=5$, difference $16$.

## D1

```latex
In $\triangle ABC$, $AB=10$, $BC=7$ and $\angle A=\theta$. There are two distinct non-congruent triangles $T_1$ (larger area) and $T_2$ (smaller area) satisfying these data. It is known that $\operatorname{Area}(T_1)=3\operatorname{Area}(T_2)$. Find $\cos\theta$. \textit{\small(adapted from TMUA 2018 Paper 1 Q19 / BMO1 2015 Q3)}
\begin{itemize}
\item[A)] $\tfrac57$
\item[B)] $\tfrac{\sqrt{17}}{5}$
\item[C)] $\tfrac{\sqrt{51}}{8}$
\item[D)] $\tfrac{\sqrt{34}}{8}$
\end{itemize}
```

- Original answer: `B) $\tfrac{\sqrt{17}}{5}$`
- Original method: Put $A(0,0)$, $B(10,0)$, $C$ with $AC=b$, $BC=7$, $\cos\theta$ unknown: $49=100+b^2-20b\cos\theta$, so $b^2-20b\cos\theta+51=0$. Two $b$'s are $b_1,b_2$ with $b_1b_2=51$, $b_1+b_2=20\cos\theta$. Areas $=5b\sin\theta$, ratio $b_1/b_2=3$, so $b_2^2=17$, $b_2=\sqrt{17}$, $b_1=3\sqrt{17}$, sum $4\sqrt{17}=20\cos\theta$, hence $\cos\theta=\sqrt{17}/5$.

## D2

```latex
The square $MNOP$ has perimeter $40$ (so side $10$). Points $R,S,T,U$ lie on $MN,NO,OP,PM$ respectively with $MR=x$ and $RSTU$ a rectangle whose sides are at $45^\circ$ to the square's sides. For $0<x<10$, the area of $RSTU$ is $A(x)=20x-2x^2+100-20x$ (simplified to $A= -2x^2+20x$ up to translation). What is the \emph{largest} $x$ for which $A(x)=20$? \textit{\small(after TMUA 2023 Paper 1 Q5)}
\begin{itemize}
\item[A)] $5+\sqrt5$
\item[B)] $5+\sqrt{15}$
\item[C)] $5+\sqrt{20}$
\item[D)] $10-\sqrt5$
\end{itemize}
```

- Original answer: `B) $5+\sqrt{15}$`
- Original method: $-2x^2+20x=20\Rightarrow x^2-10x+10=0\Rightarrow x=5\pm\sqrt{15}$. Larger is $5+\sqrt{15}$. The quadratic $A(x)$ is symmetric about $x=5$ (midpoint of side).

## D3

```latex
A circle has centre $O$ and radius $6$. Points $P,Q,R$ lie on the circle with $\angle POQ\ge \tfrac{\pi}{2}$ and $[POQ]=9\sqrt3$ (area). What is the \emph{greatest possible} area of $\triangle PRQ$? \textit{\small(adapted from TMUA 2022 Paper 1 Q14)}
\begin{itemize}
\item[A)] $18+9\sqrt3$
\item[B)] $27\sqrt3$
\item[C)] $27+9\sqrt3$
\item[D)] $36+9\sqrt3$
\end{itemize}
```

- Original answer: `B) $27\sqrt3$`
- Original method: $[POQ]=\tfrac12 r^2\sin\angle POQ=18\sin\theta=9\sqrt3\Rightarrow\sin\theta=\sqrt3/2$, so $\theta=60^\circ$ or $120^\circ$, but $\ge90^\circ$ forces $120^\circ$. For fixed chord $PQ$, $[PRQ]$ is maximal when $R$ is opposite the midpoint of arc $PQ$, height $=r+r\cos(\theta/2)=6+3=9$, base $PQ=6\sqrt3$, so max $= \tfrac12\cdot6\sqrt3\cdot9=27\sqrt3$.

## D4

```latex
Let $P(p,q)$ and circle $C: x^2+2fx+y^2+2gy+h=0$ with centre $C_0=(-f,-g)$ and radius $r=\sqrt{f^2+g^2-h}$. Let $L=|PC_0|$. Which data set is \emph{minimal sufficient} to determine $L$? \textit{\small(adapted from MAT 2020 Q1H / TMUA 2022 Paper 2 Q4)}
\begin{itemize}
\item[A)] $f,g,h$
\item[B)] $f,g,p,q$
\item[C)] $f,h,p,q$
\item[D)] $g,h,p,q$
\end{itemize}
```

- Original answer: `B) $f,g,p,q$`
- Original method: $L^2=(p+f)^2+(q+g)^2$ uses $p,q$ and $f,g$ only; $h$ (hence $r$) is irrelevant to centre-point distance. Any set missing $f$ or $g$ or $p$ or $q$ is insufficient, and $\{f,g,p,q\}$ already suffices, so it is minimal.

## D5

```latex
Circle $C_1: x^2+y^2=25$ is fixed. A second circle $C_2$ has radius $4$ and centre $(a,b)$ uniformly random in the rectangle $-2\le a\le2,\ -3\le b\le3$ (so the centre is equally likely to be anywhere in that $4\times6$ rectangle). What is the probability that $C_1$ and $C_2$ intersect (in two points, touching counts as intersecting)? \textit{\small(after TMUA 2022 Paper 1 Q19)}
\begin{itemize}
\item[A)] $\tfrac{9}{25}$
\item[B)] $\tfrac{16}{25}$
\item[C)] $\tfrac{16-\pi}{24}$
\item[D)] $\tfrac{24-\pi}{24}$
\end{itemize}
```

- Original answer: `D) $\tfrac{24-\pi}{24}$`
- Original method: Centres distance $d=\sqrt{a^2+b^2}$. Intersect iff $|5-4|\le d\le 9$, i.e. $1\le d\le9$. Max $d$ in rectangle is $\sqrt{13}<9$, so upper bound never fails; need $d\ge1$. Complement $d<1$ is disc radius $1$ area $\pi$, fully inside $4\times6$ rectangle, so $P=1-\pi/24$.
