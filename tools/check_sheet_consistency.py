#!/usr/bin/env python3
"""The printed sheet, its answer key and its checks must describe the same questions.

The binding gate proves a check agrees with the `\\ans{}` in the answer key.
Neither is what a student reads. Geometry Day 1 C1 printed y = x/2 - 4 while its
answer key and check both solved y = x/2 + 3: the suite passed, and on the
printed question the right answer was not among the options. This gate reads
the sheet itself and compares it with the other two.

Usage: python3 tools/check_sheet_consistency.py <pillar> [--sheets 01,02] [--balance]
Exits 1 if any rule is broken.
"""

import argparse
import ast
import difflib
import importlib.util
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import sympy

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.answer_binding import _numeric_equal, mcq_letter  # noqa: E402
from tools.latex_bridge import extract_tex_answers, parse_tex_math  # noqa: E402

_SECTION = re.compile(
    r"\\section\*\{Section ([A-D])[^\n]*\n(.*?)(?=\\section\*|\\SpeedClosing|\\end\{document\})", re.S)
_ITEM = re.compile(r"^\s*\\item(?!\[)", re.M)
_OPTION = re.compile(r"\\item\[([A-H])\)\]\s*(.*)")
_MATH = re.compile(r"\$([^$]+)\$")
_LEAD = re.compile(r"^\$([^$]+)\$\s*(.*)$", re.S)
_TIKZ = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.S)
_CITE = re.compile(r"\\textit\{\\small\(.*?\)\}")
_LAYOUT = re.compile(
    r"\\(?:begin|end)\{(?:minipage|itemize|enumerate)\}(?:\[t\])?(?:\{[^}]*\})?"
    r"|\\vspace\{0pt\}|\\hfill|\\centering|\\noindent|%[^\n]*")


def _parts(item):
    """(stem, {letter: option tex}) for one question's LaTeX."""
    options = {k: v.strip() for k, v in _OPTION.findall(item)}
    stem = _LAYOUT.sub(" ", _CITE.sub(" ", item.split("\\item[")[0]))
    return " ".join(stem.split()), options


def _sheet_items(path):
    text = _TIKZ.sub("", path.read_text(encoding="utf-8"))
    return {f"{sec}{n}": item
            for sec, body in _SECTION.findall(text)
            for n, item in enumerate(_ITEM.split(body)[1:], 1)}


def _answer_key_items(path):
    """{label: restated question} from an answer key; empty where the key does not restate.

    The k-th `\\ans` in Section X answers Xk (as tools.latex_bridge counts them).
    The restated question is whatever follows the last plain `\\item` before it.
    """
    if not path.exists():
        return {}
    text = _TIKZ.sub("", path.read_text(encoding="utf-8"))
    out = {}
    for sec, body in _SECTION.findall(text):
        chunks = body.split("\\ans{")
        for n, chunk in enumerate(chunks[:-1], 1):
            starts = list(_ITEM.finditer(chunk))
            out[f"{sec}{n}"] = chunk[starts[-1].end():] if starts else ""
    return out


def _maths(tex):
    """The `$...$` spans of some LaTeX, normalised so spacing and fraction style do not count."""
    spans = []
    for m in _MATH.findall(tex):
        m = re.sub(r"\\[dt]frac", r"\\frac", m)
        spans.append(re.sub(r"\\left|\\right|\\[,;!:]|\s", "", m))
    return Counter(spans)


def _option_value(tex):
    """An option's value: its leading maths when the rest is only a parenthetical remark."""
    m = _LEAD.match(tex)
    if m and (not m.group(2) or m.group(2).startswith("(")):
        tex = f"${m.group(1)}$"
    try:
        return parse_tex_math(tex)
    except Exception:
        return None


def _canon(x):
    """A value in a form `_numeric_equal` compares faithfully.

    Fractions become Rationals, a parsed `\\pi` becomes the constant, and an
    equation becomes lhs - rhs: `_numeric_equal` reads an equation by its
    right-hand side alone, which would make 5x-3y=1 and 5x+3y=1 "equal".
    """
    if isinstance(x, Fraction):
        return sympy.Rational(x.numerator, x.denominator)
    if isinstance(x, sympy.Basic):
        x = x.subs(sympy.Symbol("pi"), sympy.pi)
        if isinstance(x, sympy.Equality):
            return sympy.expand(x.lhs - x.rhs)
    return x


def _same(a, b):
    if a is None or b is None:
        return False
    try:
        return bool(_numeric_equal(_canon(a), _canon(b)))
    except Exception:
        return False


def _is_number(v):
    v = _canon(v)
    return (isinstance(v, (int, float)) and not isinstance(v, bool)) or (
        isinstance(v, sympy.Basic) and v.is_number)


def _load(script):
    spec = importlib.util.spec_from_file_location(f"_consistency_{abs(hash(script))}", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _check_options(script):
    """{label: {letter: value} or None}: a check's literal `options` dict (None if it has none)."""
    if not script.exists():
        return {}
    module = _load(script)
    found = {}
    for fn in ast.parse(script.read_text(encoding="utf-8")).body:
        if not (isinstance(fn, ast.FunctionDef) and fn.name.startswith("check_")):
            continue
        values = None
        for node in ast.walk(fn):
            if (isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict)
                    and any(isinstance(t, ast.Name) and t.id == "options" for t in node.targets)):
                values = {}
                for k, v in zip(node.value.keys, node.value.values):
                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                        try:
                            values[k.value] = eval(  # noqa: S307 - the repo's own verify scripts
                                compile(ast.Expression(v), str(script), "eval"), vars(module))
                        except Exception:
                            pass  # refers to a local the gate cannot see
        found[fn.name[len("check_"):]] = values
    return found


def check(pillar, sheets=None, balance=False, root=REPO_ROOT):
    """Every violation, as 'pillar/sheetNN LABEL: rule: detail'."""
    base = Path(root) / pillar
    numbers = sorted(p.stem[len("sheet"):] for p in (base / "sheets").glob("sheet[0-9][0-9].tex"))
    chosen = [n for n in numbers if sheets is None or n in sheets]
    problems, stems, letters = [], {}, Counter()
    for num in numbers:
        sheet = {lab: _parts(item) for lab, item in _sheet_items(base / "sheets" / f"sheet{num}.tex").items()}
        for lab, (stem, _) in sheet.items():
            stems[f"{pillar}/sheet{num} {lab}"] = stem
        if num not in chosen:
            continue
        key = base / "answers" / f"ans{num}.tex"
        answers = extract_tex_answers(str(key))
        restated = {lab: _parts(t) for lab, t in _answer_key_items(key).items()}
        in_check = _check_options(base / "verify" / f"sheet{num}_verify.py")
        for lab, (stem, options) in sheet.items():
            where = f"{pillar}/sheet{num} {lab}"
            if options:
                letter = mcq_letter(answers.get(lab))
                if letter is None or letter not in options:
                    problems.append(f"{where}: letter: answer {answers.get(lab)!r} names no option on the sheet")
                else:
                    letters[letter] += 1
                values = {k: _option_value(v) for k, v in options.items()}
                for a, b in combinations(sorted(values), 2):
                    if _same(values[a], values[b]):
                        problems.append(f"{where}: distinct: options {a} and {b} are equal")
                if in_check.get(lab) is None:
                    problems.append(f"{where}: check-options-missing: check_{lab} has no literal options dict")
                else:
                    for k, v in in_check[lab].items():
                        if k not in options:
                            problems.append(f"{where}: check-options: check has option {k}, the sheet does not")
                        elif _is_number(v) and _is_number(values[k]) and not _same(values[k], v):
                            problems.append(f"{where}: check-options: check's {k} is {v}, the sheet prints {options[k]}")
            r_stem, r_options = restated.get(lab, ("", {}))
            if r_stem and _maths(r_stem) != _maths(stem):
                problems.append(f"{where}: restated-stem: the answer key restates different maths")
            for k, v in r_options.items():
                a, b = _option_value(v), _option_value(options.get(k, ""))
                if k not in options or not (_same(a, b) or _maths(v) == _maths(options[k])):
                    problems.append(f"{where}: restated-options: the answer key's option {k} differs from the sheet")
    for a, b in combinations(sorted(stems), 2):
        if not any(f"/sheet{n} " in a or f"/sheet{n} " in b for n in chosen):
            continue
        ma = _maths(stems[a])
        if ma and ma == _maths(stems[b]) and difflib.SequenceMatcher(None, stems[a], stems[b]).ratio() > 0.85:
            problems.append(f"{a}: duplicate: same question as {b}")
    if balance and letters:
        total = sum(letters.values())
        for letter in "ABCD":
            share = letters[letter] / total
            if not 0.15 <= share <= 0.30:
                problems.append(f"{pillar}/all *: balance: {letter} is correct for {share:.0%} of {total} MCQs")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pillar")
    ap.add_argument("--sheets", help="comma-separated sheet numbers, e.g. 01,02")
    ap.add_argument("--balance", action="store_true", help="also check pillar-wide letter balance")
    args = ap.parse_args()
    sheets = set(args.sheets.split(",")) if args.sheets else None
    problems = check(args.pillar, sheets=sheets, balance=args.balance)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
