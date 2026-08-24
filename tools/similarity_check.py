"""Flag questions/methods that read too close to a real past paper.

Compares each \\item block (and, in answer files, each \\method{} block)
in a .tex file against every extract in the local research corpus
(research/txt/*.txt), using word-shingle containment — robust to the
pdftotext line-wrapping/column-interleaving noise in the corpus extracts,
without needing any third-party dependency.

This is a LOCAL-ONLY tool by design: it reads research/txt/, which is
gitignored because the papers are UKMT/OCR/Oxford copyright. It cannot
run in public CI for the same reason the corpus itself can't be
committed — don't try to wire this into a GitHub Action.

A high containment score is not automatically a problem — a credited
adaptation ("after SMC 2025 Q12") is *supposed* to be structurally close
to its source. The flag that actually matters is high containment with
no `(after ...)` credit tag nearby: that's the uncredited-reproduction
case CONTRIBUTING.md's non-negotiable #2 exists to catch.

Usage:
    python3 tools/similarity_check.py <path/to/sheet-or-answers.tex>
    python3 tools/similarity_check.py <file> --threshold 0.35 --shingle 8
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CORPUS_DIR = REPO_ROOT / "research" / "txt"

CREDIT_RE = re.compile(r"\\textit\{\\small\(after[^)]*\)\}")


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


def load_corpus() -> dict[str, list[str]]:
    if not CORPUS_DIR.exists():
        print(f"No local corpus at {CORPUS_DIR} — nothing to check against.")
        return {}
    corpus = {}
    for f in sorted(CORPUS_DIR.glob("*.txt")):
        raw = f.read_text(encoding="utf-8", errors="ignore")
        corpus[f.name] = normalize_tokens(strip_boilerplate(raw))
    return corpus


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
    args = ap.parse_args()

    corpus = load_corpus()
    if not corpus:
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
                severity = "OK (credited)" if has_credit else "REVIEW — no credit tag"
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
