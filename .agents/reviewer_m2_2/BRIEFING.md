# BRIEFING — 2026-07-11T20:00:10+01:00

## Mission
Independently review the verification scripts for Combinatorics worksheets 02, 03, and 04, checking project conformance, exact math, strength tags, questions coverage, and CLI/assertion behavior.

## 🔒 My Identity
- Archetype: Reviewer and Adversarial Critic
- Roles: reviewer, critic
- Working directory: /home/cereal-dev/Documents/speed-maths/.agents/reviewer_m2_2
- Original parent: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0
- Milestone: Combinatorics worksheets 02, 03, 04 Review
- Instance: 1 of 1

## 🔒 Key Constraints
- Review-only — do NOT modify implementation code (if bugs or conformance issues are found, report them, do not fix them yourself).
- Check conformance to speed-maths project requirements (R1, R2, R3, R4).
- Ensure all 33 questions are correctly mapped in the CHECKS dict and check functions.
- Verify that every check function's docstring starts with a valid strength tag (EXHAUSTIVE PROOF or SAMPLED CHECK).
- Check that the scripts execute successfully with code 0 and exit with code 2 under the -O flag.
- Run `tools/validate_verify_scripts.py` and verify these three scripts pass.

## Current Parent
- Conversation ID: 3cfb6e73-dc42-472a-8f00-bafaa3912dd0
- Updated: 2026-07-11T20:00:10+01:00

## Review Scope
- **Files to review**:
  - `combinatorics/verify/sheet02_verify.py`
  - `combinatorics/verify/sheet03_verify.py`
  - `combinatorics/verify/sheet04_verify.py`
- **Interface contracts**: `PROJECT.md` / `SCOPE.md` if available.
- **Review criteria**: Conformance to speed-maths project requirements, 33 questions coverage, strength tags, exit codes with and without -O flag.

## Key Decisions Made
- Confirmed that sheet02, sheet03, and sheet04 verification scripts fully conform to all speed-maths project requirements.
- Completed direct execution runs and direct execution runs under the `-O` optimization flag.
- Completed validation using `tools/validate_verify_scripts.py`.

## Artifact Index
- `/home/cereal-dev/Documents/speed-maths/.agents/reviewer_m2_2/review.md` — The final review report.

## Review Checklist
- **Items reviewed**:
  - `combinatorics/verify/sheet02_verify.py`
  - `combinatorics/verify/sheet03_verify.py`
  - `combinatorics/verify/sheet04_verify.py`
- **Verdict**: PASS
- **Unverified claims**: none

## Attack Surface
- **Hypotheses tested**:
  - Exit code under normal run: verified exits with code 0.
  - Exit code under -O optimization flag: verified exits with code 2 and outputs an error.
  - Correctness of exact arithmetic (R2): verified standard library only, no float calculations or sympy used.
  - Correctness of R1 (Independent Verification): verified the logic in check functions actually brute-forces/enumerates permutations, combinations, cartesian products, or cycles instead of just duplicating LaTeX formula math.
  - Conformance to docstring strength tags: verified all start with either "EXHAUSTIVE PROOF" or "SAMPLED CHECK".
- **Vulnerabilities found**: none
- **Untested angles**: none
