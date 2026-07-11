# BRIEFING — 2026-07-11T20:00:43+01:00

## Mission
Generate and update Python verification scripts for Combinatorics worksheets 05, 06, and 07 to be exhaustive and correct.

## 🔒 My Identity
- Archetype: worker_sheets_05_07
- Roles: implementer, qa, specialist
- Working directory: /home/cereal-dev/Documents/speed-maths/.agents/worker_sheets_05_07
- Original parent: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0
- Milestone: [TBD]

## 🔒 Key Constraints
- CODE_ONLY network mode: No external network access.
- Standard libraries only (no sympy, etc.).
- Correctness and exhaustiveness of verify scripts (R1: Independent Verification).
- Exact boilerplate, -O optimization check, docstrings start with 'EXHAUSTIVE PROOF' or 'SAMPLED CHECK'.
- Edit .tex files directly if mathematical errors are found in source.

## Current Parent
- Conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0
- Updated: not yet

## Task Summary
- **What to build**: Verification scripts for worksheets 05, 06, 07 (`sheet05_verify.py`, `sheet06_verify.py`, `sheet07_verify.py`).
- **Success criteria**: All three run, pass, and pass validation with `tools/validate_verify_scripts.py`.
- **Interface contracts**: boilerplate from `sheet01_verify.py`.
- **Code layout**: `combinatorics/verify/` and `combinatorics/answers/`.

## Loaded Skills
- None loaded yet.

## Change Tracker
- **Files modified**: [TBD]
- **Build status**: [TBD]
- **Pending issues**: [TBD]

## Quality Status
- **Build/test result**: [TBD]
- **Lint status**: [TBD]
- **Tests added/modified**: [TBD]

## Artifact Index
- None
