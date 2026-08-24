# Preparing your local research corpus

`tools/similarity_check.py` compares a draft question against real past papers so
you can catch an accidental reproduction before it reaches a PR. To do that it
needs a local corpus at `research/txt/`. This file explains how to build one.

## What this file will not do

An earlier version of this document told an AI agent to go and download five
years of SMC, BMO1, MAT and TMUA papers off the web, naming rights holders'
websites as targets, and then to strip the copyright notices out of the extracted
text. That was wrong on both counts and it has been removed.

- **Nobody should fetch papers on your behalf.** Whether you may hold a copy of a
  given paper depends on where it came from and on that publisher's terms, and
  that is a judgement for you, not for an automated agent working from a prompt in
  a public repo. This project will not instruct anyone to acquire material it has
  no standing to distribute.
- **Do not remove rights notices.** The reason the old instruction existed was
  technical: page furniture repeats on every page, so it dominates the shingle set
  and inflates every similarity score. That is now handled properly, in
  `tools/similarity_check.py`, which ignores boilerplate lines *at comparison
  time* while leaving the stored files exactly as they are. Notices stay where
  they are.

If you cannot assemble a corpus, that is fine — see "Working without a corpus"
below. It costs you one check, not the ability to contribute.

## Building the corpus from papers you already hold

You need papers you have lawfully obtained and may keep a local copy of. Once you
have them, the rest is mechanical and an agent can do all of it.

### 1. Set up the directory

```bash
mkdir -p research/pdfs research/txt
printf 'pdfs/\ntxt/\nquestions_only.txt\n' > research/.gitignore
```

`research/` is already gitignored at the repo root as well. Both layers are
deliberate: the corpus is never committed, because this repo is public and the
papers are not ours to redistribute. Nothing in `research/` should ever appear in
`git status`.

### 2. Put your PDFs in `research/pdfs/`

Name them so the source is recoverable from the filename, because the similarity
report prints the filename and that is what tells you what you matched against:

```
smc-2023.pdf   bmo1-2021.pdf   mat-2013.pdf   tmua_2022_2.pdf
```

Prefer the question papers. Solution documents work too, and are useful, but they
inflate matches on `\method{}` blocks for the obvious reason.

### 3. Extract text

Any PDF-to-text route is fine — `pypdf`, `pdfminer.six`, or `pdftotext` from
poppler, which is usually already installed:

```bash
for f in research/pdfs/*.pdf; do
  pdftotext -layout "$f" "research/txt/$(basename "${f%.pdf}").txt"
done
```

Keep the text as extracted. Do not clean it up, and in particular do not delete
headers, footers or notices — `similarity_check.py` filters page furniture itself,
and it expects to receive the file intact. The column-interleaving and
line-wrapping noise `pdftotext` produces is also fine: word-shingle containment
is chosen precisely because it survives that.

Some official papers extract as mojibake because their fonts carry no usable
character map. If a file comes out unreadable, drop it rather than trying to
repair it by hand; a corpus with gaps still works, and a garbled file only
produces meaningless scores.

### 4. Check it loads

```bash
python3 tools/similarity_check.py algebra/sheets/sheet01.tex
```

You should see the corpus files being scored against, and a summary line. On the
published sheets the expected result is a small number of hits, all of them marked
`OK (credited)` — those are credited adaptations, which are *supposed* to score
highly. A `REVIEW — no credit tag` line is the one that needs a human.

Blocks shorter than 25 words are skipped and counted separately. Containment over
a 10-word block is meaningless, and reporting it was training people to ignore the
tool.

## Working without a corpus

The check is a local pre-PR step, not a merge gate, and it cannot run in CI for
the same copyright reason the corpus is not committed. Without a corpus:

- Say so in your PR. "No local corpus; questions checked by hand against my own
  knowledge of the papers" is a useful, honest note for a reviewer.
- Lean harder on the rule the tool exists to support: adapt the *structure*,
  change the numbers and the context, and credit the source in the question line
  as `\textit{\small(after SMC 2025 Q12)}`. See CONTRIBUTING.md, non-negotiable #2.
- A reviewer with a corpus can run the check on your branch.
