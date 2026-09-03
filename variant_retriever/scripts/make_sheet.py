"""Build a drill worksheet PDF from corpus question ids, plus a separate mark-up.

Two files on purpose. The worksheet carries questions and options only: the
matched-error tag names the trap, so printing it beside the question hands over
the answer before the question is attempted. The mark-up sheet carries the
answer, its provenance, the error bracket and the derivation, and is meant to be
opened only after the attempt.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.render import display_options, display_text
from core import llm

HERE = Path(__file__).parent
CHECKPOINTS = ROOT / 'checkpoints'
DB = {q['id']: q for q in json.loads((HERE / 'database.json').read_text())['questions']}
LATEX = json.loads((CHECKPOINTS / '.latex_ckpt.json').read_text())
CODED = json.loads((CHECKPOINTS / '.opencode2_ckpt.json').read_text())

TIKZ_CKPT_FILE = CHECKPOINTS / '.tikz_ckpt.json'
if TIKZ_CKPT_FILE.exists():
    TIKZ = json.loads(TIKZ_CKPT_FILE.read_text())
else:
    TIKZ = {}

def get_tikz_options(qid, stem):
    if qid in TIKZ:
        return TIKZ[qid]
        
    stem_lower = stem.lower()
    if "which" in stem_lower and "graph" in stem_lower:
        print(f"Generating TikZ options for {qid}...", flush=True)
        prompt = f"""This is a multiple-choice math question:
{stem}
The original options were images. Generate 4 TikZ axis environments (using \\begin{{tikzpicture}}[scale=0.5] \\begin{{axis}}[axis lines=middle, width=6cm, height=4cm, xmin=-4, xmax=4, ymin=-4, ymax=4] ... \\end{{axis}} \\end{{tikzpicture}}) for the correct graph and 3 plausible distractors. 
Output ONLY the LaTeX code wrapped exactly in \\GraphOptions{{...}}{{...}}{{...}}{{...}}.
Do NOT include markdown formatting or backticks. Just the raw LaTeX code."""
        try:
            reply = llm.ask_text(prompt, verbose=True).strip()
            if reply.startswith("```"):
                reply = reply.split("\n", 1)[1]
                if reply.endswith("```"):
                    reply = reply.rsplit("\n", 1)[0]
            TIKZ[qid] = reply
            TIKZ_CKPT_FILE.write_text(json.dumps(TIKZ, indent=2))
            return reply
        except Exception as e:
            print(f"Failed to generate TikZ for {qid}: {e}", flush=True)
            return None
    return None

# Characters TeX treats as markup. Escaped only outside math, where they are
# almost always literal prose rather than intent.
SPECIALS = {'&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_'}

# pdflatex has no unicode maths. The coded error prose is model-written and
# routinely contains a bare π or ≤, which halts the build, so prose glyphs are
# mapped into math mode and anything still unmapped is dropped rather than
# allowed to fail the whole document.
UNI = {
    'π': r'$\pi$', 'θ': r'$\theta$', 'α': r'$\alpha$', 'β': r'$\beta$',
    'λ': r'$\lambda$', 'μ': r'$\mu$', 'σ': r'$\sigma$', 'ω': r'$\omega$',
    'δ': r'$\delta$', 'ε': r'$\epsilon$', 'ϵ': r'$\epsilon$', 'φ': r'$\phi$',
    '≤': r'$\le$', '≥': r'$\ge$', '⩽': r'$\le$', '⩾': r'$\ge$', '≠': r'$\ne$',
    '≈': r'$\approx$', '≡': r'$\equiv$', '∈': r'$\in$', '∞': r'$\infty$',
    '√': r'$\surd$', '×': r'$\times$', '÷': r'$\div$', '±': r'$\pm$',
    '∫': r'$\int$', '∑': r'$\sum$', '→': r'$\to$', '⇒': r'$\Rightarrow$',
    '∘': r'$^{\circ}$', '·': r'$\cdot$', '−': '-', '–': '-', '—': '---',
    '’': "'", '‘': "'", '“': "``", '”': "''", '…': r'\ldots ',
}


# Commands that require an argument. Extraction sometimes loses it, leaving
# `\frac{}` or a bare `\sqrt`, which halts pdflatex on a document that is
# otherwise fine. One damaged variant must not cost the whole sheet.
_ARG_CMDS = ('frac', 'sqrt', 'text', 'mathrm', 'overline', 'underline')

# Symbol commands that can end up butted against their operand. Matched
# longest-first so `\infty` wins over `\in` before the `f` is mistaken for the
# start of the operand.
_SYMBOL_CMDS = ('infty', 'approx', 'epsilon', 'lambda', 'Rightarrow', 'sigma',
                'omega', 'delta', 'theta', 'alpha', 'gamma', 'times', 'equiv',
                'ldots', 'cdot', 'surd', 'beta', 'circ', 'div', 'phi', 'int',
                'sum', 'pm', 'le', 'ge', 'ne', 'to', 'in', 'pi', 'mu')
# Commands that must never be split, because they legitimately begin with the
# letters of a shorter symbol: `\left` starts with `\le`, `\prod` with `\pi`.
_KNOWN_CMDS = frozenset(_SYMBOL_CMDS + _ARG_CMDS + (
    'left', 'right', 'ln', 'log', 'sin', 'cos', 'tan', 'sec', 'csc', 'cot',
    'exp', 'lim', 'limits', 'prod', 'begin', 'end', 'cases', 'quad', 'qquad',
    'langle', 'rangle', 'lfloor', 'rfloor', 'lceil', 'rceil', 'binom', 'vec',
    'hat', 'bar', 'partial', 'nabla', 'forall', 'exists', 'neq', 'leq', 'geq',
    'subset', 'subseteq', 'cup', 'cap', 'notin', 'Leftrightarrow', 'Leftarrow',
    'cdots', 'dots', 'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh',
    'deg', 'gcd', 'pmod', 'mathbb', 'mathcal', 'mathbf', 'operatorname',
    'displaystyle', 'textbf', 'textit', 'mp', 'perp', 'parallel', 'angle',
))

_LONGEST_FIRST = sorted(_SYMBOL_CMDS, key=len, reverse=True)
_CMD_RUN = re.compile(r'\\([A-Za-z]+)')


def _split_cmd(m):
    """Separate a symbol command from an operand fused onto it.

    Matching the whole letter run and deciding here, rather than with a lookahead,
    is what keeps `\\infty` intact: an alternation backtracks to the shorter
    `\\in` as soon as the longer one fails its lookahead.
    """
    name = m.group(1)
    if name in _KNOWN_CMDS:
        return m.group(0)
    for cmd in _LONGEST_FIRST:
        if name.startswith(cmd):
            return '\\' + cmd + ' ' + name[len(cmd):]
    return m.group(0)


# A control character in a question is always damage, and always the same
# damage: JSON's escape rules ate the backslash of a LaTeX command, so `\frac`
# arrived as form feed + "rac". Restoring the backslash recovers the command;
# anything else is dropped. Done here as well as at ingest because one bad
# character fails the entire document, not the question carrying it.
_CTRL_UNDO = {'\f': '\\f', '\b': '\\b', '\v': '\\v', '\r': '\\r'}


def _uncontrol(text):
    for ch, back in _CTRL_UNDO.items():
        text = text.replace(ch, back)
    text = re.sub(r'\t(?=[a-z]{2,})', r'\\t', text)
    return ''.join(c for c in text if ord(c) >= 32 or c in '\n\t')


def _fix_math(span):
    """Make a math span safe to compile, without changing what it means.

    Empty groups are the common damage: `\\frac{}{2}` and `\\frac{}` both come
    from a numerator that never made it out of the PDF. TeX will not typeset
    either, so the command is dropped and its surviving argument kept — the
    reader loses a fraction bar, which is visible, rather than the document,
    which is not.
    """
    for cmd in _ARG_CMDS:
        span = re.sub(r'\\' + cmd + r'\{\}\{([^{}]*)\}', r'\1', span)
        span = re.sub(r'\\' + cmd + r'\{([^{}]*)\}\{\}', r'\1', span)
        span = re.sub(r'\\' + cmd + r'\{\}', '', span)
        # A command with no group at all left behind by the same damage.
        span = re.sub(r'\\' + cmd + r'(?![A-Za-z{])', '', span)
    # TeX takes the longest run of letters as the command name, so `\surd` next
    # to its operand reads as `\surdx` and halts the build. Only a known command
    # can be separated from what follows it: a generic `\\[A-Za-z]+` backtracks
    # to satisfy the lookahead and splits `\frac{` into `\fra c{`.
    span = _CMD_RUN.sub(_split_cmd, span)

    # Inside maths, unicode is either a symbol with a TeX spelling or a glyph
    # the extractor mis-decoded — a Malayalam nine standing in for an exponent.
    # Map what is known and drop the rest: an expression missing a character is
    # legible, a document that will not compile is not.
    for glyph, tex in UNI.items():
        if glyph in span:
            span = span.replace(glyph, tex.strip('$') if tex.startswith('$') else tex)
    span = ''.join(c for c in span if ord(c) < 128)

    opened = span.count('{') - span.count('}')
    if opened > 0:
        span += '}' * opened
    elif opened < 0:
        # Dropping from the right keeps the expression's leading structure.
        for _ in range(-opened):
            span = ''.join(span.rsplit('}', 1))
    return span


def esc(text):
    """Escape prose while leaving math spans alone.

    The coded error descriptions are prose written by a model and frequently
    contain a bare command such as `x=1+\\sqrt3` outside any math span, which
    stops pdflatex dead. Outside math nothing is intended as markup, so the
    backslash is neutralised first — before the escapes that introduce
    backslashes of our own.

    Math spans are passed through, but repaired first: they come from a lossy
    extraction and a single unbalanced brace anywhere in the corpus fails the
    entire document rather than the one question that carries it.
    """
    out = []
    text = _uncontrol(text)
    for i, part in enumerate(re.split(r'(\$\$.*?\$\$|\$[^$\n]*\$)', text, flags=re.S)):
        if i % 2:
            out.append(_fix_math(part))
            continue
        part = part.replace('\\', '\x00')
        for ch, rep in SPECIALS.items():
            part = part.replace(ch, rep)
        part = (part.replace('~', r'\textasciitilde ')
                    .replace('^', r'\textasciicircum ')
                    .replace('{', r'\{').replace('}', r'\}')
                    .replace('\x00', r'\textbackslash '))
        for glyph, tex in UNI.items():
            part = part.replace(glyph, tex)
        part = ''.join(c for c in part if ord(c) < 128)
        out.append(part)
    return ''.join(out)


def question(qid):
    q = DB[qid]
    fixed = LATEX.get(qid)
    if fixed:
        return fixed['text'], fixed['options']
    return display_text(q['text'], q['options']), display_options(q['options'])


def tags_for(qid):
    c = CODED.get(qid) or {}
    return {o['option']: (o.get('error') or '').strip()
            for o in c.get('options', []) if not o.get('sound')}


PRE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=18mm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage[hidelinks]{hyperref}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

\newcommand{\GraphOptions}[4]{%
  \begin{center}
    \begin{tabular}{cc}
      \textbf{A)} & \textbf{B)} \\
      #1 & #2 \\[10pt]
      \textbf{C)} & \textbf{D)} \\
      #3 & #4
    \end{tabular}
  \end{center}
}

\setlist[enumerate]{leftmargin=6mm}
\pagestyle{plain}
\begin{document}
"""


def build(blocks, title, path, markup=False):
    L = [PRE, r'\section*{' + esc(title) + '}']
    if not markup:
        L.append(r'\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{'
                 r'\small Before you commit an answer, write the list of cases you '
                 r'checked. If you cannot write the list, you have not checked. '
                 r'Questions are extracted from PDFs and may contain errors --- the '
                 r'source and page are given for every one.}}' + '\n\n')
    for name, ids in blocks.items():
        L.append(r'\subsection*{' + esc(name) + '}')
        for n, qid in enumerate(ids, 1):
            if qid not in DB:
                continue
            stem, opts = question(qid)
            q = DB[qid]
            # Built from already-escaped pieces: esc() escapes braces, so
            # passing our own markup through it would print it literally.
            src = (esc(q['publisher']) + r' \textbf{Q' + esc(str(q['question_number']))
                   + r'}, p' + esc(str(q['pdf_page'])))
            L.append(r'\noindent\textbf{' + str(n) + r'.} ' + esc(stem) + r'\\[2pt]')
            L.append(r'{\footnotesize\itshape ' + src + r'}')
            
            tikz_code = get_tikz_options(qid, stem)
            if tikz_code:
                L.append(tikz_code)
            else:
                L.append(r'\begin{enumerate}[label=\Alph*)]')
                for k in sorted(opts):
                    L.append(r'\item ' + esc(opts[k]))
                L.append(r'\end{enumerate}')
            if markup:
                st = q.get('answer_status') or 'unknown'
                L.append(r'\noindent\textbf{Answer: ' + esc(str(q.get('answer') or '?')) +
                         r'} {\footnotesize(' + esc(st) + r')}\\')
                for opt, err in sorted(tags_for(qid).items()):
                    if err:
                        L.append(r'{\footnotesize\textbf{' + opt + r'} ' + esc(err) + r'}\\')
            L.append(r'\vspace{4mm}')
    L.append(r'\end{document}')
    tex = Path(path).with_suffix('.tex')
    tex.write_text('\n'.join(L))
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                        '-output-directory', str(tex.parent), str(tex)],
                       capture_output=True, text=True)
    if not Path(path).exists():
        print(r.stdout[-2500:])
        raise SystemExit(f'pdflatex failed for {path}')
    return path


if __name__ == '__main__':
    spec = json.loads(Path(sys.argv[1]).read_text())
    out = sys.argv[2]
    build(spec['blocks'], spec['title'], out + '.pdf')
    build(spec['blocks'], spec['title'] + ' — mark-up', out + '_markup.pdf', markup=True)
    print('built', out + '.pdf', 'and', out + '_markup.pdf')
