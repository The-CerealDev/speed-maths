# Scrapped Questions: Logic Drill #3 (2026-09-03)

## Rationale for Removal
The original Section A, B, and C were dominated by repetitive GCSE/A-Level proof by deduction exercises ("Prove directly: if $n$ is even then $n^2$ is even", "Prove directly: if $a$ and $b$ are odd then $ab$ is odd", "Prove by contrapositive: if $n^3$ is even then $n$ is even"). These are not timed speed-maths drills, nor do they appear on TMUA Paper 2.
TMUA Paper 2 tests Arg1 (Evaluating truth of conditionals, multi-premise implication chaining, truth tables, and "exactly-one-true" deductions — 32 hits in past papers). Day 3 has been refurbished to train these high-speed Paper 2 logic deductions.

---

## Scrapped Questions & Original Answers

### A1
- **Original**: Prove directly: ``If $n$ is even, then $n^2$ is even.''
- **Original Ans**: Let $n=2k$, $n^2=4k^2=2(2k^2)$, even.
- **Replaced By**: Tautology check: determine whether $((P \Rightarrow Q) \lor (Q \Rightarrow P))$ is always true for all propositions $P, Q$.

### A2
- **Original**: Prove directly: ``If $n$ is odd, then $n^2$ is odd.''
- **Original Ans**: Let $n=2k+1$, $n^2=4k^2+4k+1$, odd.
- **Replaced By**: If conditional $(P \lor Q) \Rightarrow (R \land S)$ is false and $R$ is true, find truth value of $S$.

### A3
- **Original**: Prove directly: ``If $a$ and $b$ are both even, then $a+b$ is even.''
- **Original Ans**: $2j+2k=2(j+k)$, even.
- **Replaced By**: Given $P \Rightarrow Q$, $Q \Rightarrow R$, and $R$ is false, find truth values of $P$ and $Q$.

### A4
- **Original**: State the contrapositive of ``If $n$ is a multiple of $6$, then $n$ is even.'' Prove it directly.
- **Original Ans**: ``If $n$ is odd, $n$ not multiple of 6.''
- **Replaced By**: Count truth assignments for which $(P \land Q) \Rightarrow R$ is false out of 8.

### A5
- **Original**: Prove directly: ``If $a$ and $b$ are both odd, then $ab$ is odd.''
- **Original Ans**: $(2j+1)(2k+1) = 2(2jk+j+k)+1$, odd.
- **Replaced By**: Count truth assignments for which $(P \lor Q) \Rightarrow R$ is false out of 8.

### A6
- **Original**: True or false: ``To prove if $P$ then $Q$ by contrapositive, assume $Q$ is false...''
- **Original Ans**: True.
- **Replaced By**: If $P \Rightarrow Q$ is true and $Q \Rightarrow P$ is false, determine truth value of $P \iff Q$.

### A7
- **Original**: Prove by contrapositive: ``If $n^2$ is odd, then $n$ is odd.''
- **Original Ans**: Contrapositive: $n$ even $\implies n^2$ even.
- **Replaced By**: Evaluate equivalence between $P \Rightarrow (Q \Rightarrow R)$ and $(P \land Q) \Rightarrow R$.

### A8
- **Original**: True or false: ``A proof by contrapositive is a different technique from proving the converse.''
- **Original Ans**: True.
- **Replaced By**: State negation of ``If $f(x)$ has a root at $x=1$, then $f(1)=0$ and $f'(1)=0$''.

### A9
- **Original**: Prove directly: ``If $x>1$, then $x^2>1$.''
- **Original Ans**: $x>1 \implies x^2>x>1$.
- **Replaced By**: Cyclic chain $P \Rightarrow Q$, $Q \Rightarrow R$, $R \Rightarrow P$: relation between truth values.

### A10
- **Original**: Prove by contrapositive: ``If $x^2\leq1$, then $x\leq1$.''
- **Original Ans**: Contrapositive: $x>1 \implies x^2>1$.
- **Replaced By**: Consistency of premises $P \lor Q$, $P \Rightarrow R$, $Q \Rightarrow R$, and $\neg R$.

### B1
- **Original**: Prove directly: ``If $n$ is a multiple of $4$, then $n^2$ is a multiple of $16$.''
- **Original Ans**: $(4k)^2 = 16k^2$.
- **Replaced By**: Exactly-one-true integer property deduction on $4 \mid n$, $n$ odd, $2 \mid n$ (after TMUA 2016 P2 Q4).

### B2
- **Original**: Prove by contrapositive: ``If $n^2$ is not a multiple of $3$, then $n$ is not a multiple of $3$.''
- **Original Ans**: Contrapositive: $3\mid n \implies 3\mid n^2$.
- **Replaced By**: Cyclic implications with exactly two true: can $P, Q, R$ share truth value? (after TMUA 2020 P2 Q20).

### B3
- **Original**: Which proof route is more natural for ``If $n^2$ is even, then $n$ is even''?
- **Original Ans**: Contrapositive.
- **Replaced By**: Three urns puzzle with conditional labels and exactly one true label (TMUA Arg1 archetype).

### B4
- **Original**: Prove directly: ``If $a>b>0$, then $a^2>b^2$.''
- **Original Ans**: $(a-b)(a+b)>0$.
- **Replaced By**: Model counting on nested conditional $(P \Rightarrow Q) \Rightarrow R$.

### B5
- **Original**: Prove by contrapositive: ``If $x^2-4x+3\neq0$, then $x\neq1$ and $x\neq3$.''
- **Original Ans**: Contrapositive: $x=1$ or $x=3 \implies x^2-4x+3=0$.
- **Replaced By**: Three suspects deduction where only the guilty person lies (after TMUA 2017 P2 Q2).

### B6
- **Original**: Prove directly: ``If $n$ is a multiple of $3$, then $n^3$ is a multiple of $27$.''
- **Original Ans**: $(3k)^3 = 27k^3$.
- **Replaced By**: Four statements about prime/parity with exactly three true.

### B7
- **Original**: State and prove contrapositive of ``If $xy$ is irrational, then $x$ is irrational or $y$ is irrational.''
- **Original Ans**: Both rational $\implies xy$ rational.
- **Replaced By**: Truth deduction when XOR is false and OR is true.

### B8
- **Original**: Prove directly: ``If $n$ ends in digit $5$, then $n^2$ ends in $5$.''
- **Original Ans**: $(10k+5)^2 = 100k^2+100k+25$.
- **Replaced By**: Logical equivalence proof between $(P \Rightarrow R) \land (Q \Rightarrow R)$ and $(P \lor Q) \Rightarrow R$.

### B9
- **Original**: Prove by contrapositive: ``If $n$ is not a multiple of $4$, then $n^2$ is not a multiple of $16$.''
- **Original Ans**: Counterexample $n=6$, false statement.
- **Replaced By**: Truth assignment count for $(P \Rightarrow Q) \land (Q \Rightarrow R)$.

### B10
- **Original**: True or false: ``Every proof by contrapositive can be rewritten as a direct proof...''
- **Original Ans**: True.
- **Replaced By**: Knights and Knaves self-referential deduction.

### C2-C8
- **Original**: Repetitive single-statement GCSE proofs ($n^3$ even $\implies n$ even, etc.).
- **Replaced By**: 7 authentic TMUA Paper 2 Arg1 multiple choice questions (truth assignments, logic puzzles, conditional constraints).
