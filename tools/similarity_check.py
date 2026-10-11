"""Flag questions/methods that read too close to a real past paper.

Compares each \\item block (and, in answer files, each \\method{} block)
in a .tex file against every extract in the local research corpus
(research/txt/*.txt), using word-shingle containment — robust to the
pdftotext line-wrapping/column-interleaving noise in the corpus extracts,
without needing any third-party dependency.

It also compares against the per-question JSON banks in
variant_retriever/data/materialised/ (official TMUA, SMC, MAT, BMO and
community mocks) when they exist. Those store the questions in LaTeX, so a
copied stem matches token for token; the pdftotext extracts do not (they
flatten x^2 to "x2"), which let verbatim TMUA copies score under 30%.

This is a LOCAL-ONLY tool by design: it reads research/txt/, which is
gitignored because the papers are UKMT/OCR/Oxford copyright. It cannot
run in public CI for the same reason the corpus itself can't be
committed — don't try to wire this into a GitHub Action.

A high containment score is not automatically a problem — a credited
adaptation ("after SMC 2025 Q12") is *supposed* to be structurally close
to its source. The flag that actually matters is high containment with
no `(after ...)` credit tag nearby: that's the uncredited-reproduction
case CONTRIBUTING.md's non-negotiable #2 exists to catch. A credit does not
cover a near-verbatim copy, though: at --near-verbatim containment or above
(default 60%) a credited block is still reported for review.

Usage:
    python3 tools/similarity_check.py <path/to/sheet-or-answers.tex>
    python3 tools/similarity_check.py <file> --threshold 0.35 --shingle 8
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CORPUS_DIR = REPO_ROOT / "research" / "txt"
JSON_CORPUS_DIR = REPO_ROOT / "variant_retriever" / "data" / "materialised"

CREDIT_RE = re.compile(r"\\textit\{\\small\(after[^)]*\)\}")
TIKZ_RE = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.DOTALL)


def strip_latex(text: str) -> str:
    text = re.sub(r"%.*", "", text)  # comments
    # unwrap common formatting macros, keep their contents
    text = re.sub(r"\\(emph|textit|textbf|text)\{([^{}]*)\}", r"\2", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)  # remaining bare commands
    text = text.replace("{", " ").replace("}", " ")
    return text


def normalize_tokens(text: str) -> list[str]:
    text = strip_latex(text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


def shingles(tokens: list[str], k: int) -> set[tuple[str, ...]]:
    if len(tokens) < k:
        return {tuple(tokens)} if tokens else set()
    return {tuple(tokens[i : i + k]) for i in range(len(tokens) - k + 1)}


def find_matching_brace(text: str, open_idx: int) -> int:
    depth = 0
    for i in range(open_idx, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return -1


def extract_macro_blocks(text: str, macro: str) -> list[str]:
    blocks = []
    for m in re.finditer(r"\\" + macro + r"\{", text):
        open_idx = m.end() - 1
        close_idx = find_matching_brace(text, open_idx)
        if close_idx != -1:
            blocks.append(text[open_idx + 1 : close_idx])
    return blocks


_ITEM_RE = re.compile(r"\\item\b([ \t]*\[[^\]]*\])?")


def extract_items(text: str) -> list[str]:
    r"""Question blocks, with multiple-choice options folded into their parent.

    `\item[A)] ...` is a labelled list entry — one option of the question above it,
    not a question in its own right. Treating each option as its own block was the
    largest source of false positives in this tool: an option line runs 9 to 13
    tokens, which at 8-word shingles yields one or two shingles, so a single common
    phrase scores 100% containment. In a sweep of all 70 published .tex files every
    single "REVIEW — no credit tag" hit was an option line or a one-line question,
    and none was a real reproduction. A gate whose every alert is spurious teaches
    people to ignore it.

    Folding options into the question is also the right comparison unit: a question
    and its options are what a past paper prints together.
    """
    blocks: list[str] = []
    matches = list(_ITEM_RE.finditer(text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        stop = text.find(r"\end{enumerate}", m.end(), end)
        body = text[m.end(): stop if stop != -1 else end].strip()
        if m.group(1) and blocks:
            blocks[-1] = f"{blocks[-1]} {body}"
            continue
        blocks.append(body)
    return blocks


# Running heads, footers and rights notices repeat on every page of a paper, so
# they dominate the shingle set and inflate every score. They are dropped here, at
# comparison time, and only from the tokens this tool compares — never from the
# stored file. Deleting a rights notice out of a document you have been given is
# not a thing this project asks anyone to do, and the earlier corpus instructions
# asking for exactly that have been rewritten.
BOILERPLATE_RE = re.compile(
    r"©|\(c\)\s*\d{4}|copyright|all rights reserved"
    r"|www\.|https?://"
    r"|united kingdom mathematics trust|ukmt"
    r"|senior mathematical challenge|british mathematical olympiad"
    r"|mathematics admissions test|test of mathematics for university admission"
    r"|do not turn over|page \d+ of \d+",
    re.IGNORECASE,
)


def strip_boilerplate(text: str) -> str:
    """Drop lines that are page furniture rather than question content."""
    return "\n".join(line for line in text.splitlines()
                     if not BOILERPLATE_RE.search(line))


def load_corpus(corpus_dir: Path = CORPUS_DIR) -> dict[str, list[str]]:
    if not corpus_dir.exists():
        return {}
    corpus = {}
    for f in sorted(corpus_dir.glob("*.txt")):
        raw = f.read_text(encoding="utf-8", errors="ignore")
        corpus[f.name] = normalize_tokens(strip_boilerplate(raw))
    return corpus


def load_json_corpus(json_dir: Path) -> dict[str, list[str]]:
    """One document per question from every *.json question bank in `json_dir`.

    A bank is either a list of question dicts or a dict with a "questions" list.
    Per-question documents keep one long paper from outscoring the question a
    block was actually copied from.
    """
    corpus = {}
    for f in sorted(Path(json_dir).glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (ValueError, UnicodeDecodeError):
            continue
        questions = data.get("questions") if isinstance(data, dict) else data
        if not isinstance(questions, list):
            continue
        for q in questions:
            if not isinstance(q, dict):
                continue
            stem = q.get("text", q.get("question"))
            if not isinstance(stem, str):
                continue
            # options are printed with the question, and our blocks fold them in too
            opts = q.get("options") if isinstance(q.get("options"), list) else []
            opts = [o.get("text", "") if isinstance(o, dict) else str(o) for o in opts]
            corpus[f"{f.name}:{q.get('id')}"] = normalize_tokens(" ".join([stem, *map(str, opts)]))
    return corpus


def number_shingles(tokens: list[str], k: int = 3) -> set[tuple[str, ...]]:
    """Runs of k consecutive numbers: the question's data, whatever the wording.

    0, 1 and 2 are dropped: exponents and unit coefficients put them in almost
    every question, and they made unrelated circles look like copies.
    """
    nums = [t for t in tokens if t.isdigit() and t not in ("0", "1", "2")]
    return {tuple(nums[i : i + k]) for i in range(len(nums) - k + 1)}


def containment(candidate_shingles: set, doc_tokens: list[str], k: int) -> float:
    if not candidate_shingles:
        return 0.0
    doc_shingles = shingles(doc_tokens, k)
    hit = len(candidate_shingles & doc_shingles)
    return hit / len(candidate_shingles)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", type=Path)
    ap.add_argument("--threshold", type=float, default=0.30,
                    help="containment at or above which a block is reported "
                         "(default 0.30; was 0.20, which reported constantly)")
    ap.add_argument("--shingle", type=int, default=8)
    ap.add_argument("--min-tokens", type=int, default=25,
                    help="skip blocks shorter than this many words (default 25). "
                         "A 10-word block yields 3 shingles at k=8, so one shared "
                         "phrase reads as 33%% or 100%% containment and means nothing")
    ap.add_argument("--include-method", action="store_true", default=True)
    ap.add_argument("--near-verbatim", type=float, default=0.60,
                    help="containment at or above which even a credited block is "
                         "reported as a near-verbatim copy (default 0.60)")
    ap.add_argument("--bank-shingle", type=int, default=5,
                    help="word-run length for the per-question bank comparison "
                         "(default 5: a bank question is one short stem, so 8-word "
                         "runs rarely survive even light rewording)")
    ap.add_argument("--bank-threshold", type=float, default=0.35)
    ap.add_argument("--source-share", type=float, default=0.30,
                    help="the shared number runs must also be at least this share "
                         "of the source question's own runs (default 0.30)")
    ap.add_argument("--data-threshold", type=float, default=0.65,
                    help="share of a question's number runs found in one bank "
                         "question at or above which it is reported as the same data "
                         "(default 0.65; needs at least --min-numbers numbers)")
    ap.add_argument("--min-numbers", type=int, default=6)
    ap.add_argument("--txt-corpus", type=Path, default=CORPUS_DIR,
                    help="directory of pdftotext paper extracts (default research/txt)")
    ap.add_argument("--json-corpus", type=Path, default=JSON_CORPUS_DIR,
                    help="directory of per-question JSON banks (default: the "
                         "variant retriever's materialised/ directory, if present)")
    args = ap.parse_args()

    corpus = load_corpus(args.txt_corpus)
    bank = load_json_corpus(args.json_corpus) if args.json_corpus.exists() else {}
    bank_words = {name: shingles(toks, args.bank_shingle) for name, toks in bank.items()}
    bank_numbers = {name: number_shingles(toks) for name, toks in bank.items()}
    # Weight each run by its rarity in the bank: a run that hundreds of questions
    # share (an answer-key tail, a pi/3-style option) says nothing about copying.
    df: dict = {}
    for runs in bank_numbers.values():
        for r in runs:
            df[r] = df.get(r, 0) + 1
    idf = lambda r: math.log((len(bank_numbers) + 1) / (df.get(r, 0) + 1))
    # Either corpus is enough to check against; with neither there is nothing to do.
    if not corpus and not bank:
        print(f"No local corpus at {args.txt_corpus} or {args.json_corpus} — nothing to check against.")
        raise SystemExit(1)

    text = args.file.read_text(encoding="utf-8")
    items = extract_items(text)

    flagged = 0
    skipped = 0
    for idx, item in enumerate(items, start=1):
        has_credit = bool(CREDIT_RE.search(item))
        candidates = {"question": item}
        for method_block in extract_macro_blocks(item, "method"):
            candidates["method"] = method_block

        # Same data, reworded stem: word shingles miss it, the numbers do not.
        # Diagram coordinates are drawing data, not question data.
        data_text = TIKZ_RE.sub(" ", CREDIT_RE.sub("", item))

        # The stem against single bank questions, with shorter word runs.
        words = shingles(normalize_tokens(data_text), args.bank_shingle)
        if len(words) >= args.min_tokens - args.bank_shingle:
            best_name, best_score = None, 0.0
            for name, doc in bank_words.items():
                score = len(words & doc) / len(words)
                if score > best_score:
                    best_name, best_score = name, score
            if best_score >= args.bank_threshold:
                flagged += 1
                if not has_credit:
                    note = "no credit tag"
                elif best_score >= args.near_verbatim:
                    note = "near-verbatim despite credit"
                else:
                    note = "credited — check it is a real perturbation"
                print(f"item {idx} [bank]: {best_score:.0%} containment vs {best_name}  -> REVIEW — {note}")
        values = [t for t in normalize_tokens(data_text) if t.isdigit() and t not in ("0", "1", "2")]
        nums = number_shingles(normalize_tokens(data_text))
        if len(nums) >= args.min_numbers - 2 and len(set(values)) >= 4:
            best_name, best_share = None, 0.0
            total = sum(idf(r) for r in nums) or 1.0
            for name, doc_nums in bank_numbers.items():
                shared = nums & doc_nums
                # The match must also be a real part of the source: a bank entry
                # ending in a long answer table contains almost any short run.
                if len(shared) < args.source_share * len(doc_nums):
                    continue
                share = sum(idf(r) for r in shared) / total
                if share > best_share:
                    best_name, best_share = name, share
            if best_share >= args.data_threshold:
                flagged += 1
                note = "credited — check it is a real perturbation" if has_credit else "no credit tag"
                print(f"item {idx} [data]: {best_share:.0%} of its data (rarity-weighted) matches {best_name}  -> REVIEW — {note}")

        for kind, candidate_text in candidates.items():
            tokens = normalize_tokens(candidate_text)
            if len(tokens) < args.min_tokens:
                skipped += 1
                continue
            cand_shingles = shingles(tokens, args.shingle)
            if not cand_shingles:
                continue
            best_file, best_score = None, 0.0
            for fname, doc_tokens in corpus.items():
                score = containment(cand_shingles, doc_tokens, args.shingle)
                if score > best_score:
                    best_file, best_score = fname, score

            if best_score >= args.threshold:
                flagged += 1
                if not has_credit:
                    severity = "REVIEW — no credit tag"
                elif best_score >= args.near_verbatim:
                    severity = "REVIEW — near-verbatim despite credit"
                else:
                    severity = "OK (credited)"
                print(f"item {idx} [{kind}]: {best_score:.0%} containment vs {best_file}  -> {severity}")

    print()
    if skipped:
        print(f"{skipped} block(s) shorter than {args.min_tokens} words were not "
              f"scored — too short for containment to mean anything. Read those "
              f"yourself if they are close adaptations.")
    if flagged:
        print(f"{flagged} block(s) at or above {args.threshold:.0%} containment. "
              f"'REVIEW' entries need a human to compare by hand before merge.")
    else:
        print(f"No block reached {args.threshold:.0%} containment against the local corpus.")


if __name__ == "__main__":
    main()
