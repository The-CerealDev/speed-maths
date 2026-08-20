<!--
Thanks for contributing. Delete whichever section below does not apply.
Nothing here is a trick question — an honest "no" is more useful than a
checked box that isn't true.
-->

## What this changes

<!-- One or two sentences. -->

---

## If this touches a question, answer or sheet

- [ ] I have solved every question I added or changed, myself, start to finish
- [ ] Adapted questions carry their `(after ...)` credit
- [ ] Nothing is a verbatim past-paper question
- [ ] No question needs a calculator

**Did you edit only `.tex` in the browser, and cannot compile the PDF?**
That is fine — say so here and a maintainer will compile it for you. Do not
leave the PDF out silently, since the site serves PDFs and the stale one would
keep showing.

- [ ] I compiled the PDF and committed it, **or** I have said above that I need help with it

**Verification.** Every question needs a check in `<pillar>/verify/sheetNN_verify.py`
that re-derives the answer independently (see
[CONTRIBUTING.md](../CONTRIBUTING.md#verification-pipeline)).

- [ ] I added or updated the check, and `python3 <pillar>/verify/run_all.py` exits 0
- [ ] I broke one assertion on purpose and confirmed it fails — so the check isn't vacuous
- [ ] **or:** I cannot write Python. Please add the check for me.

The last option is a genuine option, not a failing. Say it and someone will
pair with you.

---

## If this touches tooling, the site or docs

- [ ] `python3 tools/build_website.py` runs clean, and I did not hand-edit
      `index.html` or `classic.html` (they are generated)
- [ ] `python3 tools/validate_verify_scripts.py` passes

---

## AI assistance

AI help is welcome and this repo is built with it. Undisclosed use that a
reviewer only discovers via a wrong answer is what damages trust.

- [ ] Used none
- [ ] Used it, and disclosed how below

<!-- e.g. "questions drafted with Claude, all solved and verified by hand" -->
