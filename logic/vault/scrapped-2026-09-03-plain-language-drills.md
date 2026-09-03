# Scrapped Questions: Logic Drill #1 (2026-09-03)

## Rationale for Removal
The original Section A and Section B contained elementary conversational or plain-language flashcard drills (e.g. "Negate: $n$ is even and $n$ is prime", "Is some prime numbers are even $\forall$ or $\exists$?", "Every day next week Fred will do at least one maths problem").
In the 122 TMUA Paper 2 logic questions mapped in `research/INDEX-tmua-logic.md`, standalone negation drills appear 0 times, and conversational English sentences never appear. TMUA tests high-speed multi-premise implication evaluations, truth-table deductions under "exactly one true" constraints, formal set negations ($\mathcal{S}$-numbers), and domain boundary tests. These questions were replaced with authentic TMUA Paper 2 archetypes.

---

## Scrapped Questions & Original Answers

### A1
- **Original**: Negate: ``For all integers $n$, $n^2 \geq 0$.''
- **Original Ans**: ``There exists an integer $n$ such that $n^2<0$.''
- **Replaced By**: Negate the nested statement: ``$\forall x \in \mathbb{R},\ \exists y \in \mathbb{R} : x^2 + y^2 < 1$.''

### A2
- **Original**: Negate: ``There exists a real number $x$ such that $x^2=-1$.''
- **Original Ans**: ``For all real numbers $x$, $x^2\neq-1$.''
- **Replaced By**: Over positive integers $\mathbb{Z}^+ = \{1, 2, \dots\}$, determine truth value of $\forall n \in \mathbb{Z}^+, \exists m \in \mathbb{Z}^+ : m < n$.

### A3
- **Original**: Negate: ``$n$ is even and $n$ is prime.''
- **Original Ans**: ``$n$ is odd, or $n$ is not prime.''
- **Replaced By**: State negation of implication: ``If $n$ is even, then $n$ is a multiple of $4$ or $n$ is a multiple of $6$.''

### A4
- **Original**: Negate: ``$n$ is a multiple of $4$ or $n$ is a multiple of $6$.''
- **Original Ans**: ``$n$ is not a multiple of $4$, and $n$ is not a multiple of $6$.''
- **Replaced By**: Over $\mathbb{R}$, determine truth value of $\exists x \in \mathbb{R}, \forall y \in \mathbb{R} : xy = 0$.

### A5
- **Original**: True or false: ``The negation of `for all $x$, $P(x)$' is `for all $x$, not $P(x)$'.''
- **Original Ans**: False.
- **Replaced By**: Over non-zero reals $\mathbb{R}^*$, determine truth value of $\forall y \in \mathbb{R}^*, \exists x \in \mathbb{R}^* : xy = 1$.

### A6
- **Original**: True or false: ``$\text{not}(P \text{ and } Q)$ is the same as $(\text{not } P) \text{ or } (\text{not } Q)$.''
- **Original Ans**: True.
- **Replaced By**: If $P \iff Q$ is false, what is the truth value of $(P \land \neg Q) \lor (\neg P \land Q)$?

### A7
- **Original**: Negate: ``$x>3$ and $x<10$.''
- **Original Ans**: ``$x\leq3$ or $x\geq10$.''
- **Replaced By**: Negate condition $x \in [-2, 5) \setminus \{0\}$.

### A8
- **Original**: Is the statement ``some prime numbers are even'' a $\forall$-statement or a $\exists$-statement in form?
- **Original Ans**: $\exists$-statement.
- **Replaced By**: Determine set of real $k$ where $\forall x \in \mathbb{R}, (x < 0 \implies x^2 > k)$ is true (TMUA 2022 P2 Q9 archetype).

### A9
- **Original**: True or false: ``$\exists x \, \forall y: x+y=0$'' and ``$\forall y \, \exists x: x+y=0$'' (both over the reals) mean the same thing.
- **Original Ans**: False.
- **Replaced By**: If conditional $(P \land Q) \implies (R \lor S)$ is false, state unique truth assignment for $P, Q, R, S$.

### A10
- **Original**: Negate: ``$n$ is prime or $n=1$.''
- **Original Ans**: ``$n$ is not prime, and $n\neq1$.''
- **Replaced By**: Negate Goldbach conjecture: ``For every even integer $n > 2$, there exist primes $p$ and $q$ such that $n = p + q$.''

### B1
- **Original**: Consider the statement about Fred: ``Every day next week, Fred will do at least one maths problem.'' State the negation.
- **Original Ans**: ``Some day next week, Fred will do no maths problems.''
- **Replaced By**: $\mathcal{S}$-number negation definition MCQ (after TMUA Specimen Paper 2 Q17).

### B2
- **Original**: True or false: ``$\text{not}(P \text{ or } Q \text{ or } R)$ is the same as $(\text{not } P) \text{ or } (\text{not } Q) \text{ and } (\text{not } R)$.''
- **Original Ans**: True.
- **Replaced By**: Cyclic implication chaining $(P \implies Q) \land (Q \implies R) \land (R \implies P)$ with exactly two true (after TMUA 2020 Paper 2 Q20).

### B3
- **Original**: Negate: ``$n$ is a multiple of $2$ and $n$ is a multiple of $3$ and $n$ is a multiple of $5$.''
- **Original Ans**: ``$n$ is not a multiple of $2$, or $n$ is not a multiple of $3$, or $n$ is not a multiple of $5$.''
- **Replaced By**: Quantifier set evaluation: determine set $S$ of $x$ where $\forall y \in (0, 1), xy < x+y$ (after TMUA 2022 Paper 2 Q13).

### B5
- **Original**: True or false: ``$\text{`}\forall n\,\exists m: m>n\text{'}$ and $\text{`}\exists m\,\forall n: m>n\text{'}$ (both over the integers) mean the same thing.''
- **Original Ans**: False.
- **Replaced By**: Exactly-one-true integer property deduction on $6 \mid n$, $n$ odd, $n > 3$ prime (after TMUA 2016 Paper 2 Q4).

### B7
- **Original**: Negate: ``$n$ is a multiple of $3$, or ($n$ is a multiple of $2$ and $n$ is a multiple of $5$).''
- **Original Ans**: ``$n$ is not a multiple of $3$, and ($n$ is not a multiple of $2$ or $n$ is not a multiple of $5$).''
- **Replaced By**: Divisibility implication negation & minimal composite counterexample $\forall a,b,c (a \mid bc \implies a \mid b \lor a \mid c)$ (after TMUA 2021 Paper 2 Q4).

### B8
- **Original**: True or false: ``$\text{not}(A \text{ and } (B \text{ or } C))$ is the same as $(\text{not } A) \text{ or } ((\text{not } B) \text{ and } (\text{not } C))$.''
- **Original Ans**: True.
- **Replaced By**: Compound implication $(P \lor Q) \implies R$ false, find consistent assignments out of 8.
