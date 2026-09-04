# Systems Architecture & Security Design: Hardening Incremental CI for High-Stakes Educational Software

**Author:** David Akinyele-Aje & Contributors  
**Project:** Speed Maths (TMUA 9.0 & BMO1 Competition Engine)  
**Status:** Architecture Decision Record (ADR) & Portfolio Case Study  

---

## 1. Executive Summary & Context

Speed Maths publishes competition mathematics worksheets and verified answer keys for top-tier university entrance exams (TMUA 9.0, BMO1, MAT, SMC). 
As the codebase scaled from 1 pillar (7 sheets, 231 questions) to 5 pillars (35 sheets, 1,155 questions), and now expanding to 8 pillars (56 sheets, 1,848 questions), the continuous integration (CI) test suite faced a severe **monolithic scaling bottleneck**:
- Every commit—even a one-line typo fix in a `README.md`—spun up **8 separate Ubuntu VMs**, executing over **3,300+ dynamic assertions** and running full AST analysis across all 1,155 questions.
- A single run consumed 1.5 to 2 minutes of compute and burned hundreds of GitHub Actions runner minutes per month.

Transitioning from a **monolithic test runner** to **change-aware (incremental/differential) verification** solves the speed problem, but introduces critical **security and integrity attack vectors**. 

This document defines the **Threat Model**, the **Attack Vectors** by which a malicious or careless contributor could exploit incremental CI, and the **5-Layer Defense Architecture** engineered to make the system mathematically and architecturally tamper-proof.

---

## 2. Threat Model: 7 Ways a Malicious Actor Can Break Incremental CI

When an automated pipeline stops testing "everything on every commit" and only tests "what changed", it creates attack surfaces where broken math, malicious code, or unverified answer keys can slip through:

```
+-------------------------------------------------------------------------------+
|                             ATTACK TAXONOMY                                   |
+-------------------------------------------------------------------------------+
| [1. Doc-Masking]           Hide code/math edits behind ignored doc paths.      |
| [2. Core Subversion]       Tamper with shared bridge/binding tools to pass.    |
| [3. Facade Injection]      Inject tautologies (`assert True`) to fake tests.  |
| [4. Baseline Poisoning]    Whitelist broken checks into baseline files.       |
| [5. Optimization Bypass]   Run Python with `-O` to strip all `assert` calls.  |
| [6. Cross-Pillar Collision] Duplicate or collide with another pillar's domain.|
| [7. PR Merge Skew]         Drift regressions during non-conflicting merges.   |
+-------------------------------------------------------------------------------+
```

### Attack 1: The "Doc-Masking" Exploit
- **Mechanism:** Naive differential testing checks `if any file is .md: skip`. An attacker commits an unverified or corrupted answer in `logic/answers/ans01.tex` while simultaneously touching `README.md`.
- **Impact:** The CI pipeline skips verification, merging a false mathematical proof to production.

### Attack 2: The "Core Library Subversion" (Dependency Invalidation Failure)
- **Mechanism:** An attacker cannot get their broken geometry question to pass. They edit `tools/latex_bridge.py` or `tools/answer_binding.py` so that `bind()` always returns `True` or swallows comparison mismatches. They submit a PR touching `tools/` and `geometry/`.
- **Impact:** If the incremental tester only scopes tests to `geometry/`, the compromised core library passes silently, breaking verification integrity for all 1,155 questions across the entire repository.

### Attack 3: The "Facade & Tautology Injection"
- **Mechanism:** An attacker or lazy AI assistant writes dummy tests:
  ```python
  def check_A1():
      x = 5
      assert x == 5  # Tautological assertion between literals
      return 5
  ```
  Or:
  ```python
  def check_A2():
      assert True
      return 12
  ```
- **Impact:** The test suite reports 100% green execution, but the question was never verified computationally.

### Attack 4: The "Baseline Poisoning" Attack
- **Mechanism:** In repos with a ratchet baseline (e.g. `verify/BINDING_BASELINE.json`), an attacker adds their failing check to the baseline JSON to bypass the test harness.
- **Impact:** The failure is silently masked as a "known exemption" rather than an active regression.

### Attack 5: The "Runtime Optimization Bypass" (`PYTHONOPTIMIZE`)
- **Mechanism:** An attacker modifies the CI step or environment to run `python -O script.py`. In Python, the `-O` flag strips all `assert` statements from bytecode during compilation.
- **Impact:** Every single `check_` function exits with a clean exit code 0 without executing a single mathematical verification step!

### Attack 6: Cross-Pillar Territory Collision
- **Mechanism:** A contributor writes a new pillar sheet that duplicates or encroaches on another pillar's signature technique (e.g. teaching recurrence relations using counting rather than algebraic series).
- **Impact:** Dilutes pedagogical separation of concerns and violates repository standards established in `PILLAR-PLAYBOOK.md`.

### Attack 7: Merge Skew & Branch Interaction Regressions
- **Mechanism:** A PR only touches `geometry/`, which passes locally and in differential CI. However, a concurrent PR merged into `main` updated a shared macro in `shared/preamble.tex`. The git merge is clean (no conflict), but the runtime interaction breaks a compiled PDF or answer parser.
- **Impact:** Differential CI passes on the PR branch, but `main` is broken post-merge.

---

## 3. The 5-Layer Defense Architecture

To achieve both **sub-15-second PR feedback** and **100% mathematical certainty**, the system implements a multi-tier defense matrix:

```
                       [Incoming Git Commit]
                                 |
                                 v
        [Layer 1: Path Filter & Doc Exemption Gate]
               |                               |
        (All files docs/assets)       (Contains code/math)
               |                               |
               v                               v
           [SKIPPED]        [Layer 2: Core Invalidation Check]
                                   /                \
                         (Touches tools/)      (Pillar-only)
                                 /                    \
                                v                      v
                       [FULL 100% SUITE]      [DIFFERENTIAL RUN]
                                |                      |
                                v                      v
                      [Layer 3: AST Facade & Binding Ratchet]
                                |
                                v
                   [Layer 4: Bytecode Assert Enforcer]
                                |
                                v
               [Layer 5: Two-Tier Main & Nightly Parity]
```

### Layer 1: Strict Negative & Positive Glob Pathing
- GitHub Actions `paths-ignore` is configured with strict atomic patterns.
- **Rule:** If even a single byte outside the ignore list is modified, the ignore rule is immediately invalidated, and the test pipeline fires.

### Layer 2: The Core Invalidation Principle (Circuit Breaker)
- Any PR touching core shared infrastructure **aborts incremental mode** and forces a full monolithic test run across all 1,155 questions.
- **Trigger Paths for Full Invalidation:**
  - `tools/**`
  - `tests/**`
  - `shared/**`
  - `verify/BINDING_BASELINE.json`
  - `requirements*.txt`
  - `.github/workflows/**`

### Layer 3: AST Static Verification & Zero-Baseline Ratchet
- Even in differential mode, all modified verify scripts must pass through Python Abstract Syntax Tree (AST) inspection via `tools/analyze_facades.py --strict` and `tools/check_binding.py`.
- **AST Rules:**
  1. No empty bodies or `pass`.
  2. No assertions between literal constants (`assert 5 == 5` or `assert True`).
  3. Every assertion must operate on a computed variable derived from runtime calculations.
  4. **Zero-Baseline Ratchet:** The baseline is locked at **0 violations**. Any attempt to whitelist a broken check fails the build immediately.

### Layer 4: Bytecode Assertion Enforcement (`if not __debug__:`)
- Every verification script's `main()` begins with an unskippable runtime bytecode check:
  ```python
  if not __debug__:
      print("ERROR: Assertions are disabled! Do not run with -O or PYTHONOPTIMIZE.")
      sys.exit(1)
  ```
- `tools/validate_verify_scripts.py` uses AST inspection to confirm that this check is literally the first executable statement in `main()`.

### Layer 5: Two-Tier Execution (Fast PRs vs Monolithic Main)
- **Tier 1 (Pull Requests):** Differential testing runs in $\sim 10$ seconds, providing instant developer iteration while checking facades, bindings, and unit tests for the touched pillar.
- **Tier 2 (`push` to `main` + Nightly Scheduled Run):** Full monolithic execution. Every night at 02:00 UTC and on direct pushes to `main`, all 35+ sheets and 1,155+ questions are verified end-to-end to prevent merge-skew or hidden environmental drift.

---

## 4. Benchmark & Performance Impact

| Metric | Monolithic Pipeline | Hardened Incremental Pipeline | Improvement |
|:---|:---:|:---:|:---:|
| **Docs / Typo PR** | 1m 45s (8 VMs) | **0s (0 VMs)** | **100% saved** |
| **Single Sheet PR** | 1m 45s (8 VMs) | **12s (1 VM)** | **88% faster** |
| **Runner Minutes / Month** | ~450 min | **~45 min** | **90% reduction** |
| **Security / Math Integrity** | 100% Verified | **100% Verified** | **Zero compromise** |

---

## 5. Architectural Conclusion

By combining **path-aware change detection** with **AST facade analysis**, **circuit-breaker core invalidation**, and **two-tier mainline scheduling**, Speed Maths achieves enterprise-grade CI performance without sacrificing the absolute mathematical rigor demanded by Oxford/Cambridge admissions and Olympiad mathematics.
