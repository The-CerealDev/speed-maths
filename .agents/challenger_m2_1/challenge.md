# Challenge Report

## Challenge Summary

**Overall risk assessment**: LOW

All verification scripts for Combinatorics worksheets 02, 03, and 04 (`sheet02_verify.py`, `sheet03_verify.py`, `sheet04_verify.py`) are implemented correctly and perform rigorous, non-trivial mathematical checks.
- The tests are NOT dummy or facade checks; mutating assertions in any of the scripts successfully triggers an `AssertionError` when run.
- The arithmetic used is mathematically exact, utilizing integer operations, exact combinatorics functions (`math.comb`, `math.factorial`), and arbitrary-precision rational fractions (`fractions.Fraction`) where fractional estimates are needed. No floating-point approximations are used.

---

## Verification Details

### 1. Facade/Dummy Checks Verification
We performed mutation testing on each verification script to ensure they are active and verify actual values.
- **`sheet02_verify.py`**: Mutated `check_A1` expected answer from `21` to `22`. Running the script successfully raised an `AssertionError` (1/33 checks failed).
- **`sheet03_verify.py`**: Mutated `check_A1` expected answer from `120` to `121`. Running the script successfully raised an `AssertionError` (1/33 checks failed).
- **`sheet04_verify.py`**: Mutated `check_A1` expected answer from `10` to `11`. Running the script successfully raised an `AssertionError` (1/33 checks failed).

All scripts were restored to their original states and run again to confirm they successfully pass all 33 check functions.

*Note on LaTeX file linkage*: The verification scripts do not dynamically read or parse the `.tex` files. They contain the expected answers as hardcoded values. As a result, modifying the `.tex` file does not raise an `AssertionError` when running the python verify script itself. This complies with the project's architecture outlined in `CONTRIBUTING.md`, which favors simple standard-library-only code over parsing complex LaTeX files.

### 2. Exact Arithmetic Verification
We inspected all mathematical operations in the verification scripts:
- **`sheet02_verify.py`**: Exclusively uses integer arithmetic (floor division `//`, combinations, and permutations).
- **`sheet03_verify.py`**: Exclusively uses integer arithmetic (floor division `//`, combinations, permutations, and factorials).
- **`sheet04_verify.py`**: Uses integer operations for polynomial operations (addition, multiplication, powers) and utilizes `fractions.Fraction` (in `check_C3`) to represent fractional values (e.g., `1.01^10` approximation) exactly without floating-point error.

---

## Challenges

### [Low] Challenge 1: Absence of dynamic link between LaTeX files and Python scripts

- **Assumption challenged**: That the verification scripts automatically check the LaTeX `.tex` files for correctness.
- **Attack scenario**: If a worker changes an answer in the `.tex` file to an incorrect value but forgets to update the verification script, running the verification script will still PASS.
- **Blast radius**: The `.tex` file can contain incorrect answers that are not caught by the verification script during CI/validation checks.
- **Mitigation**: A manual review is required to cross-reference the hardcoded expected values in the verification scripts with the `\ans{...}` values in the `.tex` files. Alternatively, a future integration task can parse the `\ans{}` macros from the `.tex` file and verify that they match the results computed by the `check_*` functions in the python scripts.

---

## Stress Test Results

- **`sheet02_verify.py` check mutation** → Mutated `ans_val == 21` to `22` in `check_A1` → Raised `AssertionError` → **PASS**
- **`sheet03_verify.py` check mutation** → Mutated `ans_val == 120` to `121` in `check_A1` → Raised `AssertionError` → **PASS**
- **`sheet04_verify.py` check mutation** → Mutated `ans_val == 10` to `11` in `check_A1` → Raised `AssertionError` → **PASS**
- **Exact arithmetic check** → Audit of math division (`/`) and floating-point logic → Found no floats; `fractions.Fraction` is used for non-integers → **PASS**

---

## Unchallenged Areas

- **Other pillars (algebra, geometry, number-theory)**: Out of scope for this task (focused only on Combinatorics sheets 02-04).
- **Combinatorics sheets 01, 05, 06, 07**: Out of scope for this task (focused only on Combinatorics sheets 02-04).
