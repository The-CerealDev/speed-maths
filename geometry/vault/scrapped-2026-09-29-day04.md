# Vault — geometry Day 4: scrapped 2026-09-29

Henry Koduthore's original Day 4 ("Triangle centres and Euclidean relations"), as it stood at commit `68c31ed` before the pillar-finish rebuild. Each question below was removed or rewritten; the questions not listed here are still on the sheet (possibly moved or edited).

Removed: 28 of 33. Full originals: `git show 68c31ed:geometry/sheets/sheet04.tex` (and `answers/ans04.tex`, `verify/sheet04_verify.py`).

## A1

```latex
Write down the centroid of the triangle with vertices $(0,0)$, $(6,0)$ and $(3,9)$.
```

- Original answer: `"$(3,3)$"`
- Original method: The centroid is the average of the three vertices: $\left(\frac{0+6+3}{3},\frac{0+0+9}{3}\right)=(3,3)$.

## A2

```latex
The triangle with vertices $(0,0)$, $(6,0)$ and $(0,8)$ is right-angled at the origin. Write down the circumcentre.
```

- Original answer: `"$(3,4)$"`
- Original method: In a right triangle the circumcentre is the midpoint of the hypotenuse, the midpoint of $(6,0)$ and $(0,8)$ is $(3,4)$.

## A4

```latex
A right triangle with legs $6$ and $8$ has incircle radius $r$ and circumcircle radius $R$. Write down $r+R$.
```

- Original answer: `$7$`
- Original method: Legs $6,8$ give hypotenuse $10$. The inradius is $\frac{6+8-10}{2}=2$ and the circumradius of a right triangle is half the hypotenuse, $R=5$, so $r+R=7$.

## A5

```latex
The sides of a triangle are $6$, $8$ and $10$. Write down its circumradius $R$.
```

- Original answer: `$5$`
- Original method: $A=\frac12\cdot 6\cdot 8=24$ and $R=\frac{abc}{4A}=\frac{6\cdot 8\cdot 10}{4\cdot 24}=5$. Equivalently the hypotenuse $10$ is a diameter, so $R=5$.

## A6

```latex
Write down the centroid of the triangle with vertices $(1,2)$, $(5,6)$ and $(3,-2)$.
```

- Original answer: `"$(3,2)$"`
- Original method: $\left(\frac{1+5+3}{3},\frac{2+6-2}{3}\right)=(3,2)$.

## A7

```latex
The triangle with vertices $(0,0)$, $(6,0)$ and $(0,8)$ is right-angled. Write down the orthocentre.
```

- Original answer: `"$(0,0)$"`
- Original method: A right triangle has its orthocentre at the right-angle vertex, which is the origin here.

## B1

```latex
The centroid of the triangle with vertices $(2,1)$, $(4,3)$ and $(6,5)$ is?
\begin{itemize}
\item[A)] $(4,4)$
\item[B)] $(3,3)$
\item[C)] $(4,3)$
\item[D)] $(3,4)$
\end{itemize}
```

- Original answer: `C) $(4,3)$`
- Original method: $\left(\frac{2+4+6}{3},\frac{1+3+5}{3}\right)=(4,3)$.

## B2

```latex
The incircle of a $5$-$12$-$13$ right triangle has what radius?
\begin{itemize}
\item[A)] $1$
\item[B)] $2$
\item[C)] $3$
\item[D)] $4$
\end{itemize}
```

- Original answer: `B) $2$`
- Original method: $r=\frac{5+12-13}{2}=2$. Sanity check via $A=rs$: area $30$, semiperimeter $15$, $r=2$.

## B3

```latex
The triangle with sides $7$, $24$ and $25$ has circumradius?
\begin{itemize}
\item[A)] $12$
\item[B)] $\dfrac{25}{2}$
\item[C)] $25$
\item[D)] $\dfrac{37}{2}$
\end{itemize}
```

- Original answer: `B) $\dfrac{25}{2}$`
- Original method: $25=7^2+24^2$, so this is a right triangle: hypotenuse $25$ is the diameter, $R=\frac{25}{2}$.

## B4

```latex
The centroid $G$ of a triangle lies on the median $AM$ with $AG=6$. Find $AM$.
```

- Original answer: `$9$`
- Original method: The centroid sits $\frac23$ along the median: $AG=\frac23 AM$, and $AM=\frac32\cdot 6=9$.

## B5

```latex
The triangle with vertices $(0,0)$, $(8,0)$ and $(0,6)$ has circumcentre?
\begin{itemize}
\item[A)] $(3,4)$
\item[B)] $(4,3)$
\item[C)] $(4,4)$
\item[D)] $(6,4)$
\end{itemize}
```

- Original answer: `B) $(4,3)$`
- Original method: Right angle at $(0,0)$, so the circumcentre is the midpoint of the hypotenuse $(8,0)$\textendash$(0,6)$, namely $(4,3)$.

## B6

```latex
In triangle $ABC$ the angle bisector from $A$ meets $BC$ at $D$. Given $AB=6$, $AC=9$ and $BD=4$, find $DC$.
\begin{itemize}
\item[A)] $3$
\item[B)] $6$
\item[C)] $9$
\item[D)] $\dfrac{13}{2}$
\end{itemize}
```

- Original answer: `B) $6$`
- Original method: By the angle bisector theorem $\frac{BD}{DC}=\frac{AB}{AC}$, so $DC=\frac{BD\cdot AC}{AB}=\frac{4\cdot 9}{6}=6$.

## B7

```latex
The isosceles triangle with sides $10$, $10$, $12$ has base $12$. The median from the apex to the base is?
\begin{itemize}
\item[A)] $6$
\item[B)] $8$
\item[C)] $9$
\item[D)] $10$
\end{itemize}
```

- Original answer: `B) $8$`
- Original method: The apex median is the altitude: $\sqrt{10^2-6^2}=\sqrt{64}=8$.

## B9

```latex
A right triangle with legs $8$ and $15$ has inradius?
\begin{itemize}
\item[A)] $2$
\item[B)] $3$
\item[C)] $4$
\item[D)] $\dfrac{17}{2}$
\end{itemize}
```

- Original answer: `B) $3$`
- Original method: Hypotenuse is $\sqrt{8^2+15^2}=17$; $r=\frac{8+15-17}{2}=3$.

## B10

```latex
The triangle with sides $13$, $14$, $15$ has area $84$. Find its circumradius $R$ (as a fraction).
```

- Original answer: `$\dfrac{65}{8}$`
- Original method: $R=\frac{abc}{4A}=\frac{13\cdot 14\cdot 15}{4\cdot 84}=\frac{2730}{336}=\frac{65}{8}$.

## C1

```latex
The centroid of the triangle with vertices $(1,-2)$, $(3,4)$ and $(-1,1)$ is?
\begin{itemize}
\item[A)] $(2,1)$
\item[B)] $(1,2)$
\item[C)] $(1,1)$
\item[D)] $(0,1)$
\end{itemize}
```

- Original answer: `C) $(1,1)$`
- Original method: $\left(\frac{1+3-1}{3},\frac{-2+4+1}{3}\right)=(1,1)$.

## C2

```latex
A triangle has area $84$ and inradius $4$. Its semiperimeter is?
\begin{itemize}
\item[A)] $21$
\item[B)] $42$
\item[C)] $84$
\item[D)] $\dfrac{21}{2}$
\end{itemize}
```

- Original answer: `A) $21$`
- Original method: $A=rs$ gives $s=A/r=84/4=21$.

## C3

```latex
The triangle with vertices $(0,0)$, $(8,0)$ and $(4,6)$ has circumcentre?
\begin{itemize}
\item[A)] $\left(4,\dfrac{5}{3}\right)$
\item[B)] $(4,3)$
\item[C)] $\left(2,\dfrac{5}{3}\right)$
\item[D)] $\left(5,\dfrac{5}{3}\right)$
\end{itemize}
```

- Original answer: `A) $\left(4,\dfrac{5}{3}\right)$`
- Original method: The perpendicular bisector of $(0,0)$\textendash$(8,0)$ is $x=4$. Let the centre be $(4,y)$: $(4)^2+y^2=(4-4)^2+(y-6)^2$ gives $12y=20$, $y=\frac53$.

## C4

```latex
A $3$-$4$-$5$ triangle has inradius $1$ and circumradius $\dfrac{5}{2}$. What is the distance between its incenter and circumcentre?
\begin{itemize}
\item[A)] $\dfrac{\sqrt{5}}{2}$
\item[B)] $\dfrac{3}{2}$
\item[C)] $1$
\item[D)] $\sqrt{2}$
\end{itemize}
```

- Original answer: `A) $\dfrac{\sqrt{5}}{2}$`
- Original method: Euler's formula $d^2=R^2-2Rr$ with $R=\frac52$, $r=1$: $d^2=\frac{25}{4}-5=\frac54$, $d=\frac{\sqrt5}{2}$.

## C5

```latex
The internal angle bisector from $A$ divides $BC$ in the ratio $3:4$, and $BC=14$. What is the length of the shorter segment $BD$?
\begin{itemize}
\item[A)] $6$
\item[B)] $8$
\item[C)] $3$
\item[D)] $4$
\end{itemize}
```

- Original answer: `A) $6$`
- Original method: $BD:DC=3:4$ with total $14$: $BD=\frac{3}{7}\cdot 14=6$.

## C6

```latex
The triangle with vertices $(0,0)$, $(8,0)$ and $(2,6)$ has centroid $G$. What is the distance from $G$ to the origin $O$?
\begin{itemize}
\item[A)] $\dfrac{2\sqrt{34}}{3}$
\item[B)] $\dfrac{10}{3}$
\item[C)] $2$
\item[D)] $4$
\end{itemize}
```

- Original answer: `A) $\dfrac{2\sqrt{34}}{3}$`
- Original method: $G=\left(\frac{0+8+2}{3},\frac{0+0+6}{3}\right)=\left(\frac{10}{3},2\right)$; $OG=\sqrt{\left(\frac{10}{3}\right)^2+2^2}=\frac{\sqrt{136}}{3}=\frac{2\sqrt{34}}{3}$.

## C7

```latex
The triangle with vertices $(0,0)$, $(6,0)$ and $(3,4)$ has orthocentre?
\begin{itemize}
\item[A)] $\left(3,\dfrac{9}{4}\right)$
\item[B)] $(3,4)$
\item[C)] $\left(4,\dfrac{9}{4}\right)$
\item[D)] $(3,3)$
\end{itemize}
```

- Original answer: `A) $\left(3,\dfrac{9}{4}\right)$`
- Original method: Altitude from $C$ is $x=3$. Side $AC$ has slope $\frac43$, so the altitude from $B$ is $y=-\frac34(x-6)$; at $x=3$, $y=\frac94$.

## C8

```latex
For the triangle with vertices $(0,0)$, $(8,0)$ and $(4,6)$, the centroid is $(4,2)$ and the circumcentre is $\left(4,\dfrac{5}{3}\right)$. The orthocentre lies on the Euler line three times as far from the centroid as the circumcentre. What is the orthocentre?
\begin{itemize}
\item[A)] $\left(4,\dfrac{8}{3}\right)$
\item[B)] $\left(4,\dfrac{5}{3}\right)$
\item[C)] $\left(4,2\right)$
\item[D)] $\left(\dfrac{8}{3},4\right)$
\end{itemize}
```

- Original answer: `A) $\left(4,\dfrac{8}{3}\right)$`
- Original method: On the Euler line $\overrightarrow{GH}=2\overrightarrow{GO}$, so $H=G+2(G-O)$; $G=(4,2)$, $O=\left(4,\frac53\right)$ gives $H=\left(4,\frac83\right)$. Cross-check with the altitude method.

## D1

```latex
The triangle with vertices $(0,0)$, $(9,0)$ and $(0,12)$ has inradius $r$ and circumradius $R$. What is $r+R$?
\begin{itemize}
\item[A)] $\dfrac{21}{2}$
\item[B)] $12$
\item[C)] $10$
\item[D)] $15$
\end{itemize}
```

- Original answer: `A) $\dfrac{21}{2}$`
- Original method: Right triangle $9,12,15$: $r=\frac{9+12-15}{2}=3$, $R=\frac{15}{2}$, $r+R=\frac{21}{2}$.

## D2

```latex
In triangle $ABC$, $AB=12$, $AC=16$ and $BC=14$. The internal angle bisector from $A$ meets $BC$ at $D$. What is the length of $BD$?
\begin{itemize}
\item[A)] $6$
\item[B)] $7$
\item[C)] $8$
\item[D)] $9$
\end{itemize}
```

- Original answer: `A) $6$`
- Original method: $\frac{BD}{DC}=\frac{AB}{AC}=\frac{12}{16}=\frac34$ and $BD+DC=14$ give $BD=\frac{3}{7}\cdot 14=6$.

## D3

```latex
A triangle has sides $6$, $7$ and $8$. What is the length of the median to the longest side (the side of length $8$)?
\begin{itemize}
\item[A)] $\dfrac{\sqrt{106}}{2}$
\item[B)] $\dfrac{\sqrt{53}}{2}$
\item[C)] $\sqrt{53}$
\item[D)] $\sqrt{26}$
\end{itemize}
```

- Original answer: `A) $\dfrac{\sqrt{106}}{2}$`
- Original method: Apollonius: $m_a^2=\frac{2b^2+2c^2-a^2}{4}$ with $a=8$, $b=6$, $c=7$: $m^2=\frac{72+98-64}{4}=\frac{106}{4}$, $m=\frac{\sqrt{106}}{2}$.

## D4

```latex
The triangle with vertices $(0,0)$, $(3,0)$ and $(0,4)$ has side lengths $3$, $4$ and $5$. The incenter $I$ is the weighted average of the vertices weighted by the {\em opposite} side lengths. Find $I$.
\begin{itemize}
\item[A)] $(1,1)$
\item[B)] $(1,2)$
\item[C)] $(2,1)$
\item[D)] $\left(\dfrac{4}{3},\dfrac{4}{3}\right)$
\end{itemize}
```

- Original answer: `A) $(1,1)$`
- Original method: Weight by opposite sides: $I=\frac{BC\cdot A+CA\cdot B+AB\cdot C}{a+b+c}=\frac{5(0,0)+4(3,0)+3(0,4)}{12}=\frac{(12,12)}{12}=(1,1)$.

## D5

```latex
A $13$-$14$-$15$ triangle has inradius $4$ and circumradius $\dfrac{65}{8}$. Euler's formula gives the distance $d$ between incenter and circumcentre via $d^2 = R^2 - 2Rr$. What is $d$?
\begin{itemize}
\item[A)] $\dfrac{\sqrt{65}}{8}$
\item[B)] $\dfrac{65}{8}$
\item[C)] $4$
\item[D)] $\dfrac{1}{2}$
\end{itemize}
```

- Original answer: `A) $\dfrac{\sqrt{65}}{8}$`
- Original method: $d^2=R^2-2Rr=\frac{65^2}{64}-2\cdot\frac{65}{8}\cdot 4=\frac{4225}{64}-\frac{4160}{64}=\frac{65}{64}$, so $d=\frac{\sqrt{65}}{8}$.
