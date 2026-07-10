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


def extract_items(text: str) -> list[str]:
    parts = re.split(r"\\item\b", text)[1:]  # drop preamble before first \item
    items = []
    for part in parts:
        end = min(
            (part.find(m) for m in (r"\item", r"\end{enumerate}") if part.find(m) != -1),
            default=len(part),
        )
        items.append(part[:end].strip())
    return items


def load_corpus() -> dict[str, set[tuple[str, ...]]]:
    if not CORPUS_DIR.exists():
        print(f"No local corpus at {CORPUS_DIR} — nothing to check against.")
        return {}
    corpus = {}
    for f in sorted(CORPUS_DIR.glob("*.txt")):
        tokens = normalize_tokens(f.read_text(encoding="utf-8", errors="ignore"))
        corpus[f.name] = tokens
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
    ap.add_argument("--threshold", type=float, default=0.2)
    ap.add_argument("--shingle", type=int, default=8)
    ap.add_argument("--include-method", action="store_true", default=True)
    args = ap.parse_args()

    corpus = load_corpus()
    if not corpus:
        raise SystemExit(1)

    text = args.file.read_text(encoding="utf-8")
    items = extract_items(text)

    flagged = 0
    for idx, item in enumerate(items, start=1):
        has_credit = bool(CREDIT_RE.search(item))
        candidates = {"question": item}
        for method_block in extract_macro_blocks(item, "method"):
            candidates["method"] = method_block

        for kind, candidate_text in candidates.items():
            tokens = normalize_tokens(candidate_text)
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
    if flagged:
        print(f"{flagged} block(s) at or above {args.threshold:.0%} containment. "
              f"'REVIEW' entries need a human to compare by hand before merge.")
    else:
        print(f"No block reached {args.threshold:.0%} containment against the local corpus.")


if __name__ == "__main__":
    main()
