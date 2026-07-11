# BRIEFING — 2026-07-11T19:55:40+01:00

## Mission
Write a Python script at tools/validate_verify_scripts.py to validate sheet verification scripts, and run it to verify existing ones.

## 🔒 My Identity
- Archetype: developer worker
- Roles: implementer, qa, specialist
- Working directory: /home/cereal-dev/Documents/speed-maths/.agents/worker_validate
- Original parent: 48cb6d3e-9d66-481b-8fdf-b3dcd4d8c274
- Milestone: Validate Verification Scripts

## 🔒 Key Constraints
- Run the verification script without -O flag and verify exit code 0.
- Run with -O flag (python3 -O ...) and verify exit code 2.
- Parse content to check for:
  - optimization guard (if not __debug__:) inside main()
  - CHECKS dictionary
  - check functions for A1-A10, B1-B10, C1-C8, D1-D5
  - each check function docstring must contain "EXHAUSTIVE PROOF" or "SAMPLED CHECK" (case-insensitive)
- Exit with code 0 on success, non-zero on failure.
- Report status of existing verification scripts (sheet01_verify.py, etc.).

## Current Parent
- Conversation ID: 48cb6d3e-9d66-481b-8fdf-b3dcd4d8c274
- Updated: yes

## Task Summary
- **What to build**: tools/validate_verify_scripts.py
- **Success criteria**: All checks pass, exits with 0 if all scripts are valid, reports status, runs successfully.
- **Interface contracts**: None
- **Code layout**: tools/

## Key Decisions Made
- Use Python's `ast` module to perform robust source code parsing on the target scripts.
- Use `subprocess` to run verification scripts with and without `-O` flag.

## Change Tracker
- **Files modified**: tools/validate_verify_scripts.py (Created new validator script).
- **Build status**: Pass (compilation check succeeds).
- **Pending issues**: None.

## Quality Status
- **Build/test result**: Tested validator on the 3 existing scripts. Verified it catches expected failures.
- **Lint status**: Checked syntax with py_compile. No standard linters available on user machine.
- **Tests added/modified**: E2E check of current scripts (algebra/verify/sheet01_verify.py, combinatorics/verify/sheet01_verify.py, combinatorics/verify/sheet07_verify.py).

## Loaded Skills
- None

## Artifact Index
- tools/validate_verify_scripts.py — Python script that validates the structure and execution constraints of sheet verification scripts.
