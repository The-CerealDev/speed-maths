"""Compare a check's computed answer against the answer printed in the `.tex`.

This module is the single place where "does the verification agree with the
published answer key?" is decided. Before it existed, each `check_<label>()`
made that call for itself, and 622 of 1,155 checks silently declined to make it
at all — 363 never read the `.tex`, and 259 read it into a variable they then
ignored. A wrong `\\ans{}` passed the suite for 54% of the corpus.

The convention this supports: a check *returns* the value it claims is the
answer, and the harness compares. A check that returns nothing cannot pass, so
binding is structural rather than a per-author discipline.

Not every published answer can be bound equally strongly, and pretending
otherwise is how the last gate ended up decorative. Three honest strengths:

  EXACT      the published answer parses to a value and the computed value is
             mathematically equal to it. This is real verification.
  DRIFT_ONLY the published answer is prose ("All integers n >= 1"), so the
             comparison can only confirm the check and the `.tex` still agree
             on the same words. That catches an edited answer key; it does not
             prove the prose is true.
  EXEMPT     the published answer is a pointer, not a value ("Proof: see
             method"). Nothing can be compared. These must be listed in
             verify/BINDING_EXEMPTIONS.md with the method claims that are
             asserted instead.

`kind` is reported, never inferred away, so the README can state what fraction
of the corpus is actually EXACT instead of claiming all of it is proven.
"""

import re
from dataclasses import dataclass

import sympy

EXACT = "EXACT"
DRIFT_ONLY = "DRIFT_ONLY"
EXEMPT = "EXEMPT"

# "Proof: see method", "Proof via AM--GM: see method", "Shown below." — the
# answer key defers to the prose, so there is no value to compare against.
_PROOF_MARKER = re.compile(r"^\s*(proof|proved|shown|see\s+method)\b", re.IGNORECASE)

# "A) none of them", "(B) ...", "C) $P$ is necessary ..."
_MCQ_LETTER = re.compile(r"^\s*\(?([A-G])\)")

_YES_NO = re.compile(r"^\s*(yes|no|true|false)\b", re.IGNORECASE)

# Any maths at all: a `$...$` span or a LaTeX command. Its absence means the
# printed answer is plain prose.
_HAS_MATHS = re.compile(r"\$|\\[a-zA-Z]")

# A coordinate tuple of integers: (3,2), (-16, -2), (1, 2, 3).
_TUPLE_RE = re.compile(r"\(\s*-?\d+(?:\s*,\s*-?\d+)+\s*\)")


def as_tuple_list(published_raw):
    """Read a solution-set answer as actual numbers, or None if it is not one.

    Answers like "$(3,2)$" and "$(4,12), (6,6), (12,4)$" are the natural output of
    a Diophantine search, and they are extremely common in number theory. SymPy's
    LaTeX parser does not read them as values -- `parse_tex_math` hands back the
    raw string -- so without this they could only ever be compared as prose, and a
    check would have to format its solutions back into the printed spelling to
    bind. Reading them properly means a check can just return what it computed.

    Only accepts an answer that is *entirely* tuples and separators, so
    "$(2,3)$ and nothing else" or a tuple embedded in a sentence falls through to
    the prose path rather than being silently half-read.
    """
    body = str(published_raw).replace("$", "").strip()
    found = _TUPLE_RE.findall(body)
    if not found:
        return None
    if _TUPLE_RE.sub("", body).strip(" ,;.\t\n"):
        return None                      # there was more than tuples in there
    return [tuple(int(n) for n in re.findall(r"-?\d+", t)) for t in found]


def _tuple_sets_match(published, computed):
    """Compare two collections of coordinate tuples, ignoring order.

    A solution set has no canonical order -- the sheet may print ascending in x
    where a search yields ascending in y -- so order is not required. Duplicates
    are still significant, hence a multiset rather than a set.
    """
    if isinstance(computed, (tuple, list)) and computed and \
            all(isinstance(v, (int, float)) for v in computed):
        computed = [tuple(computed)]     # a lone solution, returned bare
    if not isinstance(computed, (list, tuple, set, frozenset)):
        return False
    try:
        got = [tuple(int(v) for v in item) for item in computed]
    except (TypeError, ValueError):
        return False
    remaining = list(got)
    if len(remaining) != len(published):
        return False
    for want in published:
        if want in remaining:
            remaining.remove(want)
        else:
            return False
    return True


@dataclass(frozen=True)
class BindResult:
    ok: bool
    kind: str
    detail: str = ""

    def __bool__(self):
        return self.ok


def is_proof_marker(published_raw):
    """True when the printed answer defers to the method instead of giving a value."""
    return bool(_PROOF_MARKER.match(str(published_raw)))


def mcq_letter(value):
    """The option letter a value denotes, or None.

    Accepts the printed form ("A) none of them") and the form a check is
    likely to return (just "A"), so a check does not have to echo the whole
    option text back to prove it picked the right one.

    Coerces through `str()` because `parse_tex_math` turns a bare option label
    into a one-letter sympy Symbol rather than a string, so the parsed form of
    "C) $k \\leq 0$" arrives here as Symbol('C').

    A multiple-choice answer binds on the letter, not on the option's value:
    naming the option is what proves the check solved the question the students
    were actually asked.
    """
    if value is None or isinstance(value, bool):
        return None
    # An option whose text contains a comma ("A) $A=1,B=1$") is split by
    # parse_tex_math into a list with the letter as its first element. Look
    # through that, so passing a parsed answer straight back in still resolves.
    if isinstance(value, (list, tuple)) and value:
        return mcq_letter(value[0])
    text = value if isinstance(value, str) else str(value)
    m = _MCQ_LETTER.match(text)
    if m:
        return m.group(1).upper()
    s = text.strip().rstrip(")").upper()
    if len(s) == 1 and "A" <= s <= "G":
        return s
    return None


def normalise_prose(text):
    """Reduce a prose answer to something two spellings of it will share.

    Deliberately crude: strips maths delimiters and LaTeX commands, folds
    whitespace and case, drops trailing punctuation. It exists to detect an
    edited answer key, not to judge meaning.
    """
    s = str(text)
    s = s.replace("$", " ")
    s = re.sub(r"\\[a-zA-Z]+", " ", s)          # \tfrac, \neq, \mathbb ...
    s = re.sub(r"[{}\\]", " ", s)
    s = re.sub(r"[\s,;.]+", " ", s)
    return s.strip().lower().rstrip(" .")


def _scalarise(value):
    """Take the right-hand side of an equation, so "d=4" compares as 4."""
    if isinstance(value, sympy.Equality):
        return value.rhs
    return value


def _numeric_equal(a, b):
    """Mathematical equality, not structural equality.

    `sympy.simplify(a - b) == 0` is the check CONTRIBUTING asks for. Falls back
    to a numeric comparison for values simplify cannot settle symbolically
    (nested radicals, mostly), and returns False rather than raising when the
    two are not comparable at all.
    """
    a, b = _scalarise(a), _scalarise(b)
    if isinstance(a, bool) or isinstance(b, bool):
        return bool(a) == bool(b)

    # Structural equality first. It is exact, cheap, and it is the only thing
    # that works for the values `parse_tex_math` hands back that are not
    # arithmetic: bare strings, and the Eq(...) objects it produces when a
    # multi-part answer contains prose ("rational roots: x=..."). Subtracting
    # those is meaningless, so simplify alone would report identical values as
    # different.
    try:
        if a is b or bool(a == b):
            return True
    except (TypeError, ValueError):
        pass
    if isinstance(a, str) or isinstance(b, str):
        # One side is unparseable text; only an exact textual match counts.
        return normalise_prose(a) == normalise_prose(b)

    try:
        if sympy.simplify(sympy.sympify(a) - sympy.sympify(b)) == 0:
            return True
    except (TypeError, ValueError, AttributeError, sympy.SympifyError):
        pass
    try:
        diff = complex(sympy.N(sympy.sympify(a) - sympy.sympify(b)))
        return abs(diff) < 1e-9
    except (TypeError, ValueError, AttributeError, sympy.SympifyError):
        return False


def _multiset_equal(published, computed):
    """Match two collections of values ignoring order.

    Order is meaningful in some answers (a row of Pascal's triangle) and not in
    others ("x=5 or x=-2"), and the printed answer does not say which. Ordered
    comparison is tried first so a genuine sequence still binds exactly; the
    unordered fallback keeps "or"-style answers from failing on spelling order.
    """
    pub = list(published)
    comp = list(computed)
    if len(pub) != len(comp):
        return False
    if all(_numeric_equal(p, c) for p, c in zip(pub, comp)):
        return True
    remaining = list(comp)
    for p in pub:
        for i, c in enumerate(remaining):
            if _numeric_equal(p, c):
                del remaining[i]
                break
        else:
            return False
    return True


def bind(published_raw, published, computed):
    """Decide whether `computed` matches the published answer.

    published_raw -- the literal text inside `\\ans{...}`
    published     -- that text as parsed by tools.latex_bridge.parse_tex_math
    computed      -- whatever the check function returned
    """
    if is_proof_marker(published_raw):
        return BindResult(
            True, EXEMPT,
            "published answer defers to the method; needs an entry in "
            "verify/BINDING_EXEMPTIONS.md",
        )

    if computed is None:
        return BindResult(
            False, EXACT,
            "check returned None — it never states which value it verified, so "
            "nothing can be compared against the printed answer",
        )

    # Multiple choice: compare the option letter, not the option prose.
    pub_letter = mcq_letter(published_raw)
    if pub_letter is not None:
        got = mcq_letter(computed)
        if got is None:
            return BindResult(
                False, EXACT,
                f"published answer is option {pub_letter}; check returned "
                f"{computed!r}, which names no option",
            )
        return BindResult(
            got == pub_letter, EXACT,
            "" if got == pub_letter
            else f"published option {pub_letter}, check computed {got}",
        )

    if isinstance(published, bool) or isinstance(computed, bool):
        ok = bool(published) == bool(computed)
        return BindResult(ok, EXACT,
                          "" if ok else f"published {published!r}, computed {computed!r}")

    # A solution set of coordinate tuples, which the LaTeX parser cannot read as
    # values. Compared as numbers rather than as text, so this is EXACT.
    published_tuples = as_tuple_list(published_raw)
    if published_tuples is not None:
        ok = _tuple_sets_match(published_tuples, computed)
        return BindResult(
            ok, EXACT,
            "" if ok else
            f"published solutions {published_tuples!r}, check computed {computed!r}",
        )

    # An answer with no maths markup at all is prose, whatever the parser made
    # of it. parse_tex_math runs parse_latex over everything and will happily
    # turn "Independent observations." into a product of one-letter symbols;
    # comparing against that is meaningless, and treating it as a value would
    # report DRIFT_ONLY work as EXACT.
    if not _HAS_MATHS.search(str(published_raw)):
        got = normalise_prose(computed)
        ok = got == normalise_prose(published_raw)
        return BindResult(
            ok, DRIFT_ONLY,
            "" if ok else
            f"prose answer changed: .tex says {normalise_prose(published_raw)!r}, "
            f"check says {got!r}",
        )

    if isinstance(published, (list, tuple)):
        if not isinstance(computed, (list, tuple, set, frozenset)):
            return BindResult(
                False, EXACT,
                f"published answer is a {len(published)}-value list; check "
                f"returned a single {type(computed).__name__}",
            )
        ok = _multiset_equal(published, computed)
        return BindResult(ok, EXACT,
                          "" if ok else f"published {published!r}, computed {list(computed)!r}")

    # A string survived parse_tex_math, so the answer is prose or an MCQ letter
    # we did not recognise. Only drift can be detected.
    if isinstance(published, str):
        if _YES_NO.match(published_raw) and isinstance(computed, bool):
            want = _YES_NO.match(published_raw).group(1).lower() in ("yes", "true")
            ok = computed is want
            return BindResult(ok, EXACT,
                              "" if ok else f"published {want!r}, computed {computed!r}")
        # Accept a match against either the literal `\ans{...}` text or the
        # cleaned form `parse_tex_math` produces. A check has no reason to
        # prefer one spelling, and `get_answer` hands back the cleaned one, so
        # requiring the raw form would fail checks that echo what they read.
        got = normalise_prose(computed)
        ok = got in (normalise_prose(published_raw), normalise_prose(published))
        return BindResult(
            ok, DRIFT_ONLY,
            "" if ok else
            f"prose answer changed: .tex says {normalise_prose(published_raw)!r}, "
            f"check says {got!r}",
        )

    ok = _numeric_equal(published, computed)
    return BindResult(ok, EXACT,
                      "" if ok else f"published {published!r}, computed {computed!r}")
