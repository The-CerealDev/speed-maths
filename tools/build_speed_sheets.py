"""Build the Speed Sheet edition of every published sheet.

A Speed Sheet is the answers file compiled a second way: working space under
each question, the answer hidden upside down in the margin, and that answer
linking to its worked solution in the published answers PDF. There is no second
`.tex` per sheet. The answers file already holds every question and every
checked answer, so a copy would be one more place for the two to disagree; the
build instead feeds `ansNN.tex` a prelude that loads `shared/speed.tex`, which
overrides how the answer macros render.

The links point at hyperref's `Item.N` destinations, which already exist in
every answers PDF. They are only right while the Nth `\\ans` sits under the
Nth numbered item, so `answer_item_numbers` exists to guard exactly that.
"""
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SITE = 'https://speedmaths.co.uk'
ROOT = Path(__file__).resolve().parent.parent
SPEED_TEX = ROOT / 'shared' / 'speed.tex'
ANSWERS_PHRASE = r'Answers \& Investigations'

_TOKEN_RE = re.compile(r'\\begin\{(\w+)\}|\\end\{(\w+)\}|\\item(\[)?|\\ans\{')
_COMMENT_RE = re.compile(r'(?<!\\)%.*')


def answer_item_numbers(tex: str) -> list[int]:
    """For each `\\ans` in order, how many numbered list items come before it.

    Only an `\\item` directly inside an `enumerate`, without a `[...]` label,
    steps LaTeX's counter and gets an `Item.N` anchor; MCQ options live in
    `itemize` and labelled sub-parts take `[...]`, so neither counts.
    """
    stack, count, out = [], 0, []
    for m in _TOKEN_RE.finditer(_COMMENT_RE.sub('', tex)):
        begin, end, labelled = m.group(1), m.group(2), m.group(3)
        if begin:
            stack.append(begin)
        elif end:
            if stack and stack[-1] == end:
                stack.pop()
        elif m.group(0).startswith('\\item'):
            if stack and stack[-1] == 'enumerate' and not labelled:
                count += 1
        else:
            out.append(count)
    return out


def speed_title(tex: str) -> str:
    """The answers title with its 'Answers & Investigations' suffix swapped."""
    m = re.search(r'\\SpeedTitleBlock\{((?:[^{}]|\{[^{}]*\})*)\}', tex)
    if not m or ANSWERS_PHRASE not in m.group(1):
        raise ValueError(f'expected a \\SpeedTitleBlock containing {ANSWERS_PHRASE!r}')
    return m.group(1).replace(ANSWERS_PHRASE, 'Speed Sheet')


@dataclass(frozen=True)
class SpeedJob:
    pillar: str
    n: str
    answers_tex: Path
    out_pdf: Path
    url: str
    title: str


def jobs(root: Path, pillars: Iterable[str]) -> list[SpeedJob]:
    """One job per answers file that has a matching question sheet."""
    out = []
    for pillar in pillars:
        for tex in sorted((root / pillar / 'answers').glob('ans*.tex')):
            n = re.fullmatch(r'ans(\d+)\.tex', tex.name)
            if not n or not (root / pillar / 'sheets' / f'sheet{n[1]}.tex').exists():
                continue
            out.append(SpeedJob(
                pillar=pillar,
                n=n[1],
                answers_tex=tex,
                out_pdf=root / pillar / 'sheets' / f'sheet{n[1]}-speed.pdf',
                url=f'{SITE}/{pillar}/answers/ans{n[1]}.pdf',
                title=speed_title(tex.read_text(encoding='utf-8')),
            ))
    return out


def build(job: SpeedJob, out_dir: Path | None = None) -> Path:
    """Compile one Speed Sheet; returns the PDF path. Raises RuntimeError if it fails.

    pdflatex runs from the answers directory because the answers files reach
    the preamble by a path relative to themselves.
    """
    out_dir = Path(out_dir or job.out_pdf.parent).resolve()
    name = job.out_pdf.stem
    prelude = (rf'\def\SpeedAnsURL{{{job.url}}}'
               rf'\def\SpeedSheetTitle{{{job.title}}}'
               rf'\AtBeginDocument{{\input{{{SPEED_TEX.with_suffix("")}}}}}'
               rf'\input{{{job.answers_tex.name}}}')
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
           f'-jobname={name}', f'-output-directory={out_dir}', prelude]
    for _ in range(2):
        run = subprocess.run(cmd, cwd=job.answers_tex.parent, capture_output=True, text=True)
        if run.returncode != 0:
            log = out_dir / f'{name}.log'
            tail = log.read_text(errors='replace')[-2000:] if log.exists() else run.stdout[-2000:]
            raise RuntimeError(f'{job.answers_tex} failed as a Speed Sheet:\n{tail}')
    for ext in ('.aux', '.log', '.out'):
        (out_dir / f'{name}{ext}').unlink(missing_ok=True)
    return out_dir / f'{name}.pdf'


def _live_pillars():
    sys.path.insert(0, str(ROOT))
    from tools.build_website import PILLARS
    return [slug for slug, meta in PILLARS.items() if meta[2] == 'live']


def main(argv: list[str]) -> int:
    files = [Path(a).resolve() for a in argv]
    todo = [j for j in jobs(ROOT, _live_pillars())
            if not files or j.answers_tex.resolve() in files]
    for job in todo:
        print(build(job).relative_to(ROOT))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
