# BRIEFING — 2026-07-11T20:00:33Z

## Mission
Review the verification scripts algebra/verify/sheet04_verify.py and algebra/verify/sheet05_verify.py.

## 🔒 My Identity
- Archetype: reviewer and adversarial critic
- Roles: reviewer, critic
- Working directory: /home/cereal-dev/Documents/speed-maths/.agents/reviewer_sheet04_05
- Original parent: 466bff0e-c0ed-4bb0-9733-b579a67fac58
- Milestone: Algebra sheets 04 & 05 Review
- Instance: 1 of 1

## 🔒 Key Constraints
- Review-only — do NOT modify implementation code (report bugs/conformance issues, do not fix them yourself).
- Check conformance to speed-maths project requirements (R1, R2, R3, R4).
- Ensure all 33 questions are correctly mapped in the CHECKS dict and check functions.
- Verify that every check function's docstring starts with a valid strength tag (EXHAUSTIVE PROOF or SAMPLED CHECK).
- Check that the scripts execute successfully with code 0 and exit with code 2 under the -O flag.
- Run `tools/validate_verify_scripts.py` and verify both scripts pass.

## Current Parent
- Conversation ID: 466bff0e-c0ed-4bb0-9733-b579a67fac58
- Updated: 2026-07-11T20:00:33Z

## Review Scope
- **Files to review**:
  - `algebra/verify/sheet04_verify.py`
  - `algebra/verify/sheet05_verify.py`
- **Interface contracts**: `PROJECT.md`, `CONTRIBUTING.md`
- **Review criteria**: correctness, exact arithmetic, independent verification, structure compliance, exit codes with and without -O flag, and docstring strength tags.

## Key Decisions Made
- Initialized briefing and review setup.

## Artifact Index
- `/home/cereal-dev/Documents/speed-maths/.agents/reviewer_sheet04_05/BRIEFING.md` — Active briefing index.
- `/home/cereal-dev/Documents/speed-maths/.agents/reviewer_sheet04_05/ORIGINAL_REQUEST.md` — Incoming review request.
- `/home/cereal-dev/Documents/speed-maths/.agents/reviewer_sheet04_05/progress.md` — Progress tracker.

## Review Checklist
- **Items reviewed**: none yet
- **Verdict**: pending
- **Unverified claims**: all implementation details of `sheet04_verify.py` and `sheet05_verify.py`

## Attack Surface
- **Hypotheses tested**: none yet
- **Vulnerabilities found**: none yet
- **Untested angles**: all check functions of sheet04 and sheet05
