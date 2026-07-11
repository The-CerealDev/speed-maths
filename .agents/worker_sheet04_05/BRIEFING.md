# BRIEFING — 2026-07-11T19:59:14+01:00

## Mission
Implement and verify the Python verification scripts for Algebra Sheet 04 and Sheet 05.

## 🔒 My Identity
- Archetype: worker
- Roles: implementer, qa, specialist
- Working directory: /home/cereal-dev/Documents/speed-maths/.agents/worker_sheet04_05
- Original parent: 466bff0e-c0ed-4bb0-9733-b579a67fac58
- Milestone: M3, M4

## 🔒 Key Constraints
- R1: Independent Verification (genuine check route, not duplicating the method).
- R2: Exact Arithmetic Only (strictly standard library modules: math, itertools, fractions.Fraction. No sympy or other third-party libraries).
- R3: Strict Structure (boilerplate from sheet01_verify.py, -O guard, CHECKS dict, check_A1...check_D5 functions, matching the exact format of sheet01_verify.py).
- R4: Error Correction Protocol (if a mathematical error is found in the source .tex file, directly edit the .tex file to fix it, then ensure the script passes).
- Network Restrictions: CODE_ONLY network mode.

## Current Parent
- Conversation ID: 466bff0e-c0ed-4bb0-9733-b579a67fac58
- Updated: not yet

## Task Summary
- **What to build**: Verification scripts `algebra/verify/sheet04_verify.py` and `algebra/verify/sheet05_verify.py`.
- **Success criteria**: Validation tool `python3 tools/validate_verify_scripts.py` passes for all scripts. All questions checked and verified using exact arithmetic/independent routes.
- **Interface contracts**: PROJECT.md
- **Code layout**: PROJECT.md § Code Layout

## Key Decisions Made
- Use exact rational arithmetic (fractions.Fraction) and float assertions with 1e-9 tolerance for surds.
- Strictly adhere to structure format matching `sheet01_verify.py` (with comments specifying check type: e.g., "SAMPLED CHECK", "EXHAUSTIVE PROOF").

## Change Tracker
- **Files modified**:
  - `algebra/verify/sheet04_verify.py` — Verification script for Algebra Sheet 04
  - `algebra/verify/sheet05_verify.py` — Verification script for Algebra Sheet 05
- **Build status**: PASS
- **Pending issues**: None

## Quality Status
- **Build/test result**: PASS
- **Lint status**: PASS (verified structure and execution with `tools/validate_verify_scripts.py`)
- **Tests added/modified**: Implemented 33 check functions for Sheet 04 and 33 check functions for Sheet 05 (66 total functions).

## Loaded Skills
- None loaded.

## Artifact Index
- `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheet04_05/ORIGINAL_REQUEST.md` — Original prompt request
- `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheet04_05/BRIEFING.md` — Agent Briefing
- `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheet04_05/progress.md` — Progress tracker
- `/home/cereal-dev/Documents/speed-maths/.agents/worker_sheet04_05/handoff.md` — Final handoff report

