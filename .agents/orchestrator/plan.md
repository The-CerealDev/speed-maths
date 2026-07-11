# Project Plan — Speed Maths Verification Scripts Generation

## Project Overview
The objective is to generate exhaustive Python verification scripts for the remaining 12 math worksheet answer keys (Algebra 02-07, Combinatorics 02-07) in the repository. We must ensure all requirements (R1: Independent Verification, R2: Exact Arithmetic, R3: Strict Structure, R4: Error Correction Protocol) are fully met.

## Milestones

### Milestone 1: Exploration & Global Planning
- Retrieve and catalog all questions, answers, and method claims for Algebra 02-07 and Combinatorics 02-07.
- Establish baseline verification infrastructure (E2E Test Track).
- Output: `PROJECT.md` and `TEST_INFRA.md` initialized.

### Milestone 2: Algebra Verification (Part 1 - Sheets 02, 03, 04)
- Generate `sheet02_verify.py`, `sheet03_verify.py`, `sheet04_verify.py`.
- Run checks, fix any `.tex` file errors if discovered (Error Correction Protocol).
- Output: Passed verification scripts for Algebra 02-04.

### Milestone 3: Algebra Verification (Part 2 - Sheets 05, 06, 07)
- Generate `sheet05_verify.py`, `sheet06_verify.py`, `sheet07_verify.py`.
- Run checks, fix any `.tex` file errors if discovered (Error Correction Protocol).
- Output: Passed verification scripts for Algebra 05-07.

### Milestone 4: Combinatorics Verification (Part 1 - Sheets 02, 03, 04)
- Generate `sheet02_verify.py`, `sheet03_verify.py`, `sheet04_verify.py`.
- Run checks, fix any `.tex` file errors if discovered (Error Correction Protocol).
- Output: Passed verification scripts for Combinatorics 02-04.

### Milestone 5: Combinatorics Verification (Part 2 - Sheets 05, 06, 07)
- Generate `sheet05_verify.py`, `sheet06_verify.py`, `sheet07_verify.py` (expanding/overwriting existing sheet07).
- Run checks, fix any `.tex` file errors if discovered (Error Correction Protocol).
- Output: Passed verification scripts for Combinatorics 05-07.

### Milestone 6: E2E Verification & Hardening
- Run the E2E validator across all 12 sheets.
- Perform white-box/adversarial coverage checks (Tier 5).
- Ensure all 12 sheets pass `run_all.py` for both pillars.
- Output: Final handoff.md and completion report.

## Parallel Track Strategy
- **Implementation Track**: Spawn sub-orchestrators/workers to analyze the `.tex` files, write the verification scripts, and run verification.
- **E2E Testing Track**: Spawn a tester agent to build an independent validator script (`tools/validate_verify_scripts.py`) that checks that each generated verification script conforms to the format requirements (main guard, correct number of functions, check function naming, docstring presence, etc.).
