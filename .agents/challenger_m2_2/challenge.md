# Challenge Report — Combinatorics Sheets 02, 03, 04

## Challenge Summary

**Overall risk assessment**: LOW

The verification scripts for Combinatorics Sheets 02, 03, and 04 (`sheet02_verify.py`, `sheet03_verify.py`, `sheet04_verify.py`) are highly robust. They use exact integer arithmetic or exact rational fractions, and they independently compute answers via combinatorial generation (e.g., `itertools.combinations`, `itertools.permutations`, custom polynomial expansion) rather than simply hardcoding values. 

However, we identified one structural risk in how the verification scripts are coupled with the LaTeX files.

---

## Challenges

### [Medium] Challenge 1: Lack of Direct Coupling Between Verification Scripts and LaTeX Answers

- **Assumption challenged**: The verify scripts guarantee the correctness of the published LaTeX files.
- **Attack scenario**: If a developer modifies an answer in the answer sheet (`ansNN.tex`) but fails to update the corresponding verification script (`sheetNN_verify.py`), the verify script will still pass in CI, leaving the incorrect answer in the published worksheet.
- **Blast radius**: Wrong answers inside the LaTeX answer key (`ansNN.tex`) and the generated PDFs could slip into the repository undetected, defeating the purpose of having automated verification.
- **Mitigation**: Introduce a check in the verify scripts or in the E2E script (`tools/validate_verify_scripts.py`) to parse `\ans{...}` macros from the LaTeX files and assert that they match the expected values verified by the python scripts.

---

## Stress Test Results

### 1. Script Mutation Test (Verify scripts are NOT dummy/facade checks)

- **Scenario**: Temporarily modify the expected answer in the verification script (e.g., changing C(7,2) to 22 in `sheet02_verify.py`, 5! to 121 in `sheet03_verify.py`, and coefficient of x^2 in (1+x)^5 to 11 in `sheet04_verify.py`).
- **Expected behavior**: Running the mutated script fails with `AssertionError`.
- **Actual behavior**:
  - `sheet02_verify.py` → `AssertionError: Expected 22, got 21` (PASS)
  - `sheet03_verify.py` → `AssertionError` (PASS)
  - `sheet04_verify.py` → `AssertionError` (PASS)
- **Verdict**: **PASS**

### 2. LaTeX Mutation Test

- **Scenario**: Temporarily modify the answer of question A1 in `ans02.tex` from `21` to `22` and run `sheet02_verify.py`.
- **Expected behavior**: Ideally, the script should fail to signal that the LaTeX file is out of sync.
- **Actual behavior**: The script passed successfully (no error raised).
- **Verdict**: **FAIL** (This confirms the vulnerability described in Challenge 1).

### 3. Exact Arithmetic Test

- **Scenario**: Check for any use of floating-point division `/` or floating-point approximations where exact results are expected.
- **Expected behavior**: All divisions must use integer division `//` or exact fraction classes (`fractions.Fraction`), and all combinatorial functions must return integers.
- **Actual/predicted behavior**: 
  - All divisions in the scripts are integer division `//`.
  - Combinatorial counts are computed via `math.comb` and `math.factorial` (returning integers) or by enumerating and taking the length of lists/sets.
  - Rational approximations (e.g., in `sheet04_verify.py` question C3) use `fractions.Fraction`.
- **Verdict**: **PASS**

---

## Unchallenged Areas

- **Worksheets 01, 05, 06, 07** — Out of scope.
