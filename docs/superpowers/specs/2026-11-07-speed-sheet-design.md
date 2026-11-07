# Speed Sheet (iPad edition, issue #13): design

Date: 2026-11-07. Status: awaiting approval.

## Why

Students (David included) use Speed Maths as a timed warm-up before papers. The real failure was never checking answers: the answers lived in a separate PDF, so checking took effort, so it didn't happen, and questions you got stuck on were forgotten. The Speed Sheet puts the answer on the same page, out of sight until you want it, and one tap away from the full worked answer.

It becomes the **default sheet** on the website. It is also a ship-blocker for Henry's Calculus & Graphs pillar (his `PLAN.md` §17 requires it).

## What a student gets

One PDF per sheet (`<pillar>/sheets/sheetNN-speed.pdf`), A4, for annotating in GoodNotes/Notability or printing:

- Same title block, toolkit line and Sections A–D as today. Title reads "… — Speed Sheet".
- Working space under every question: A 3cm, B 4.5cm, C 6cm, D 7cm.
- The answer sits at the bottom of each question's space, **in the right page margin**: upside down, 4pt, 22% grey, right edge about 6mm from the paper edge. Invisible at normal zoom; readable by pinch-zooming and rotating.
- **Tapping the answer opens the answers PDF at that exact question** (method + "Investigate further"). Verified working on David's iPad with the 2026-11-07 spike.
- No question is split across pages; no section heading is left alone at the bottom of a page.
- Not on the sheet: `\method`, `\inv`, "Top 5 Patterns Today", "Common Traps" (they give answers away; they stay in the answers PDF).

## Goals

1. One Speed Sheet per published sheet, built from the existing answers `.tex`, with no second hand-maintained source.
2. Every answer link lands on the right question, in every pillar.
3. They never drift from the checked answers: one command rebuilds them all, and CI flags any that are stale or broken.
4. Website: the archive view (`index.html`) shows **Speed Sheet** and **Answers** per sheet. The classic view (`classic.html`) keeps the original **Questions** and **Answers**. The original `sheetNN.pdf` files stay hosted.

## Non-goals

- Score tracking, ✓/✗ marks, tally boxes: these belong to the future online mode. (David tried them in the spike and rejected them: "pdfs could be printed".)
- Any change to question content or to how the answers PDFs look.
- STEP links, Day 8, concept links (#11): parked separately.

## Anti-goals (would count as failure even if it builds)

- The answer is readable at a glance at normal zoom (spoils the question).
- Any link lands on the wrong question.
- A second copy of question text exists anywhere.

## Constraints and facts found

- **Anchors already exist.** hyperref gives every numbered `enumerate` item a named destination `Item.N`; MCQ options (`itemize`) and `\item[...]` labels don't step it. Checked 2026-11-07: in all 42 answers files the Nth `\ans` sits under numbered item N, and every answers PDF has `Item.1`–`Item.43` (33 questions, then the 10 pattern/trap bullets). So no preamble change and no answers PDF is reissued. This only holds while questions never contain a nested numbered list, so a test must guard it.
- Links use the absolute URL `https://speedmaths.co.uk/<pillar>/answers/ansNN.pdf#nameddest=Item.N`, so they work after the PDF is downloaded or imported into GoodNotes (tested: Chrome jumps to the right page; iPad confirmed by David).
- Keep-together and section spacing must live in macros/hooks, not a text rewrite of the `.tex` (the spike used `sed`; that's throwaway). Keep-together must apply only to top-level question items, not MCQ options or sub-parts.
- Geometry answers also `\input{../geometry-preamble}`; the Speed Sheet must build there too.
- 33 questions per sheet; 42 sheets live across 6 pillars.

## Decided by David

- Speed Sheet replaces Questions as the default; classic view keeps the originals.
- Answer position: like the #13 prototype, pushed further right into the margin.
- Answer taps through to the exact question in the answers PDF (replaces a separate "method & extension" link).
- No ticks/tally on the sheet.

## Claude's calls (check these)

- Name **"Speed Sheet"** and filename `sheetNN-speed.pdf` (#13 said "iPad edition"; Henry's plan says "Annotate Edition" / `sheetNN-ipad.pdf`, and needs updating to match).
- Cut "Top 5 Patterns" and "Common Traps" from the Speed Sheet.
- Make the link's tap area bigger than the 4pt text (invisible), so it's easy to hit on an iPad.
- Checks, run on every built Speed Sheet: exactly one answer link per question, to `Item.1…Item.N` in order; every answers `.tex` keeps the Nth `\ans` under numbered item N; no page starts with an orphaned answer; no page ends on a section heading (via `pdftotext`, as the #13 prototype did).
- Follow the repo's existing PDF model: Speed Sheet PDFs are built locally and committed like every other PDF; CI rebuilds the ones whose answers `.tex` changed and flags any that are stale (as `compile.yml` already does), rather than pushing PDFs itself.

## Left to the builder

- How the build selects Speed mode without new `.tex` files (e.g. compiling `ansNN.tex` with a `\def` flag and `-jobname`/`-output-directory`), and how the URL is passed in.
- How Sections A–D get their spacing and how the post-D sections are suppressed.
- Website template and `sheets.json` changes for the new button.
- Reference: the macros in #13. The 2026-11-07 spike overrode `\ans` to put the answer in a box, `\rotatebox{180}`, and place it with `\hfill\rlap{\hspace{\dimexpr16mm-\wd\box}…}` so its right edge lands 16mm into the 22mm margin, wrapped in `\href`. It was throwaway and is not kept.
