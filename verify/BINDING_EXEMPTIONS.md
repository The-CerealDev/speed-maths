# Binding exemptions

`tools/check_binding.py` requires every published question's check to be bound
to the answer printed in its PDF — either by returning the value it computed so
the harness can compare it, or by letting the value from `get_answer()` reach an
assertion.

The 77 questions below cannot be bound that way, because their `\ans{}` is not
a value. It is a pointer to the prose: "Proof: see method", "Proved below".
There is nothing to compare a computed value against.

That makes them the *weakest* questions in the corpus, not the safest, so they
carry an obligation instead. For an exempt question, the check must assert the
claims the `\method{}` actually makes — each factorisation, modular fact,
identity and stated intermediate value — because those claims are all a student
gets. A wrong intermediate step in a proof whose final line is "hence proved"
has nothing else to catch it.

Two rules for this file:

1. **An exemption waives `UNBOUND` and nothing else.** An exempt check still
   fails the gate on an empty body, on no assertions, or on assertions that only
   compare literals.
2. **Adding a row is a review decision, not a fix.** If an answer can be
   restated as a value — "Proof: see method" becoming the identity or the bound
   it establishes — restate it in the `.tex` and delete the row. That is
   strictly better than exempting it, because it gives the student a checkable
   answer and the pipeline something to verify.

Rows are `pillar/sheetNN LABEL` so `check_binding.py` can find them, followed by
the answer text as printed.


## algebra (13)

- `algebra/sheet03 C3` — Proof: see method.
- `algebra/sheet03 D3` — Proof via AM--GM: see method.
- `algebra/sheet03 D4` — Proof: see method.
- `algebra/sheet04 D1` — Proved below.
- `algebra/sheet05 B9` — Proof by partial fractions, then telescoping.
- `algebra/sheet05 C2` — Proved below.
- `algebra/sheet05 D4` — Proved below.
- `algebra/sheet06 C5` — Proved below.
- `algebra/sheet06 D1` — Proved below.
- `algebra/sheet07 B9` — Proved below.
- `algebra/sheet07 C1` — Proved below.
- `algebra/sheet07 C3` — All three inequalities proved below.
- `algebra/sheet07 C5` — Proved below.

## combinatorics (10)

- `combinatorics/sheet04 D1` — Proof below.
- `combinatorics/sheet04 D5` — Proof below.
- `combinatorics/sheet05 D2` — Proof below.
- `combinatorics/sheet06 D1` — Proof below.
- `combinatorics/sheet06 D2` — Proof below.
- `combinatorics/sheet06 D3` — Proof below.
- `combinatorics/sheet06 D4` — Proof below; some pair chosen by $\geq2$ students (in fact $\geq\lceil20/10\rceil=2$).
- `combinatorics/sheet06 D5` — Proof below.
- `combinatorics/sheet07 D2` — Proof below.
- `combinatorics/sheet07 D4` — Proof below (induction).

## logic (48)

- `logic/sheet02 C2` — Proved.
- `logic/sheet03 A1` — Proved.
- `logic/sheet03 A10` — Proved via the contrapositive ``if $x>1$, then $x^2>1$'' (A9).
- `logic/sheet03 A2` — Proved.
- `logic/sheet03 A3` — Proved.
- `logic/sheet03 A5` — Proved.
- `logic/sheet03 A7` — Proved via the contrapositive ``if $n$ is even, then $n^2$ is even'' (A1).
- `logic/sheet03 A9` — Proved.
- `logic/sheet03 B1` — Proved.
- `logic/sheet03 B2` — Proved via the contrapositive ``if $n$ is a multiple of $3$, then $n^2$ is a multiple of $3$''.
- `logic/sheet03 B4` — Proved.
- `logic/sheet03 B5` — Proved via the contrapositive ``if $x=1$ or $x=3$, then $x^2-4x+3=0$''.
- `logic/sheet03 B6` — Proved.
- `logic/sheet03 B8` — Proved.
- `logic/sheet03 B9` — Proved via the contrapositive ``if $n^2$ is a multiple of $16$, then $n$ is a multiple of $4$''.
- `logic/sheet03 C2` — Proved via the contrapositive ``if $n$ is odd, then $n^3$ is odd''.
- `logic/sheet03 C3` — Proved.
- `logic/sheet03 C4` — Proved.
- `logic/sheet03 C5` — Proved via the contrapositive ``if $x=0$ or $y=0$, then $xy$ is rational''.
- `logic/sheet03 C6` — Proved via the contrapositive ``if $n$ is a multiple of $3$, then $2n^2+1$ is not a multiple of $3$''.
- `logic/sheet03 C7` — Proved.
- `logic/sheet03 D2` — Proved via the contrapositive ``if $n$ is odd, then $n^2-2n$ is odd''.
- `logic/sheet03 D3` — Proved.
- `logic/sheet03 D4` — Proved.
- `logic/sheet04 B10` — Proof by contradiction
- `logic/sheet04 B4` — Proof by contradiction
- `logic/sheet04 B7` — Proof by contradiction
- `logic/sheet04 C4` — Proof by contradiction
- `logic/sheet04 C7` — Proof by contradiction
- `logic/sheet04 D2` — Proof by contradiction
- `logic/sheet06 B3` — Proof by induction
- `logic/sheet06 B5` — Proof by induction
- `logic/sheet06 B6` — Proof
- `logic/sheet06 B7` — Proof by induction
- `logic/sheet06 B9` — Proof by induction
- `logic/sheet06 D2` — Proof by strong induction below, via the key gap lemma.
- `logic/sheet06 D3` — Proof by induction below; the condition $x>-1$ is required when multiplying the inequality by $(1+x)$.
- `logic/sheet06 D4` — Proof by induction below (via the lemma $a_n-1=\prod_{i=1}^{n-1}a_i$).
- `logic/sheet06 D5` — Proof by induction below.
- `logic/sheet07 B1` — Proof by contrapositive
- `logic/sheet07 B2` — Proof by contradiction
- `logic/sheet07 B3` — Proof by induction
- `logic/sheet07 B7` — Proof by induction
- `logic/sheet07 B8` — Proof by contradiction
- `logic/sheet07 D1` — Proof below.
- `logic/sheet07 D2` — Proof below, via the invariant $m-n\bmod2$.
- `logic/sheet07 D3` — Proof below.
- `logic/sheet07 D4` — Proof by strong induction (via minimal counterexample) below.

## sequences (8)

- `sequences/sheet01 B3` — Proof by the AP sum formula.
- `sequences/sheet01 D3` — Proof: see method.
- `sequences/sheet02 B1` — Proof by substitution $x=1$.
- `sequences/sheet02 D3` — Proof by differentiating $(1+x)^n$.
- `sequences/sheet03 D1` — Proof via the sum-to-infinity formula; partial sums approach but never reach $1$.
- `sequences/sheet05 B1` — Proof: $a_{n+1}-a_n=\dfrac1{(n+1)(n+2)}>0$.
- `sequences/sheet06 D3` — Proof via the finite-$k$ bound.
- `sequences/sheet07 D2` — Proof by induction using Day 6's construction.

## Status

| pillar | exempt |
|---|---|
| algebra | 13 |
| combinatorics | 10 |
| logic | 48 |
| sequences | 7 |
| **total** | **78** |

Every one of these is a candidate for removal by rewriting the `\ans{}` as
a value. The count going down is a real improvement to the corpus; it going
up needs a reason in the PR.
