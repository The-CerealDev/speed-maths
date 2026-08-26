"""Build the archive site from the sheets on disk.

One scan produces every page. `index.html` is the current design and
`classic.html` is the original two-column card grid, both rendered from the same
data so neither can drift from the repo or from each other while the layout is
still being decided.

Sheet metadata comes out of the `.tex` itself via `\\SpeedMeta` rather than a
manifest kept alongside it. A manifest is a second place to forget: a sheet
whose topic lives in its own source cannot disagree with the site, and a
contributor writing a sheet fills its topic in without being told to.

Counts are always derived, never stored, for the same reason.
"""
import json
import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# slug -> (display name, one-line description, status)
# Order is the order pillars appear in the nav and on the page.
#
# status 'draft' keeps a pillar off the site while its sheets are still being
# reviewed. The sheets stay in the repo and in sheets.json, so nothing is lost
# and the build reports what is being held back — but the archive only lists
# what a reader can trust blind, which is the promise the whole site makes.
# Move a pillar to 'live' when its sheets have passed review.
PILLARS = {
    'algebra':       ('Algebra', 'Polynomials, inequalities, and functional equations.', 'live'),
    'combinatorics': ('Combinatorics', 'Counting, probability, and discrete structures.', 'live'),
    'number-theory': ('Number Theory', 'Divisibility, modular arithmetic, and primes.', 'live'),
    'logic':         ('Logic', 'Conditionals, proof techniques, and counterexamples.', 'live'),
    'sequences':     ('Sequences', 'Recurrences, series, and limiting behaviour.', 'live'),
    'calculus':      ('Calculus', 'Differentiation, integration, and rates of change.', 'draft'),
    'graphs':        ('Graphs', 'Curve sketching, transformations, and asymptotics.', 'draft'),
}

TEMPLATES = [
    ('template-archive.html', 'index.html'),
    ('template.html', 'classic.html'),
]

META_RE = re.compile(r'\\SpeedMeta\s*\{', re.S)


def _braced(text, start):
    """Read one balanced {...} group beginning at `start`, which must be '{'.

    LaTeX arguments nest, so a plain non-greedy regex takes the wrong closing
    brace the moment a topic contains one. Counting depth is the only thing that
    survives `{\\LaTeX}` inside a title.
    """
    depth, i = 0, start
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return '', start


def read_meta(tex_path):
    """Topic and tool list for one sheet, or empty strings if not annotated."""
    if not os.path.exists(tex_path):
        return '', []
    src = open(tex_path, encoding='utf-8', errors='ignore').read()
    m = META_RE.search(src)
    if not m:
        return '', []
    topic, nxt = _braced(src, m.end() - 1)
    tools_raw, _ = _braced(src, src.index('{', nxt))
    tools = [t.strip() for t in tools_raw.split(',') if t.strip()]
    return _detex(topic), [_detex(t) for t in tools]


def _detex(s):
    """LaTeX source to display text.

    Dashes are converted before macros are stripped: `--` and `---` are LaTeX's
    en and em dash, and leaving them alone puts a literal "AM--GM" on the page.
    """
    s = re.sub(r'\\[a-zA-Z]+\s*', '', s)
    s = s.replace('---', '\u2014').replace('--', '\u2013')
    return s.replace('\\', '').replace('{', '').replace('}', '').strip()


ITEMIZE_RE = re.compile(r'\\begin\{itemize\}.*?\\end\{itemize\}', re.S)


def count_questions(tex_path):
    r"""Questions on a sheet: the \item entries that are questions.

    Sections A-D are four `enumerate` environments and one question is one
    \item inside them. Multiple-choice options are an `itemize` nested within a
    question, and those \items are not questions — counting raw reports 126 for
    a 33-question calculus sheet, because that sheet has 23 option lists.

    Nested itemize blocks are stripped innermost-first until the source stops
    changing, so a sheet that puts options inside options still counts right.
    """
    if not os.path.exists(tex_path):
        return 0
    src = open(tex_path, encoding='utf-8', errors='ignore').read()
    prev = None
    while prev != src:
        prev, src = src, ITEMIZE_RE.sub('', src)
    return len(re.findall(r'\\item\b', src))


def scan():
    """Every pillar with its sheets. Pillars with no PDFs are kept, empty."""
    data = []
    for slug, meta in PILLARS.items():
        name, desc, status = meta[0], meta[1], meta[2]
        sheets_dir = os.path.join(ROOT_DIR, slug, 'sheets')
        answers_dir = os.path.join(ROOT_DIR, slug, 'answers')
        sheets = []
        if os.path.isdir(sheets_dir):
            for f in sorted(os.listdir(sheets_dir)):
                if not f.endswith('.pdf'):
                    continue
                num = re.search(r'\d+', f)
                if not num:
                    continue
                n = num.group(0)
                tex = os.path.join(sheets_dir, f'sheet{n}.tex')
                topic, tools = read_meta(tex)
                ans = f'ans{n}.pdf'
                sheets.append({
                    'n': n,
                    'topic': topic,
                    'tools': tools,
                    'questions': count_questions(tex),
                    'pdf': f'{slug}/sheets/{f}',
                    'answers': (f'{slug}/answers/{ans}'
                                if os.path.exists(os.path.join(answers_dir, ans))
                                else None),
                })
        data.append({'slug': slug, 'name': name, 'desc': desc,
                     'status': status, 'sheets': sheets})
    return data


def published(data):
    """What the site may list: live pillars only, drafts held back."""
    return [p for p in data if p['status'] == 'live']


# ── rendering ────────────────────────────────────────────────────────────────

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def render_rows(pillar):
    """Sheet rows for the current design: number, topic, new-tool tags, links."""
    out = []
    for s in pillar['sheets']:
        title = esc(s['topic']) if s['topic'] else f"Sheet {s['n']}"
        if s['tools']:
            tags = ('<span class="tools-label">Methods:</span>'
                    + ''.join(f'<span class="tool">{esc(t)}</span>' for t in s['tools']))
            tools_html = f'<span class="tools">{tags}</span>'
        else:
            tools_html = ''
        qs = (f'<span class="qcount">{s["questions"]} questions</span>'
              if s['questions'] else '')
        ans = (f'<a href="{s["answers"]}" class="pdf-link ans" target="_blank">Answers</a>'
               if s['answers'] else '')
        out.append(f'''
          <li class="sheet-row">
            <span class="sheet-num">{s['n']}</span>
            <span class="sheet-body">
              <span class="sheet-name">{title}</span>
              {tools_html}
            </span>
            {qs}
            <span class="links">
              <a href="{s['pdf']}" class="pdf-link" target="_blank">Questions</a>
              {ans}
            </span>
          </li>''')
    return '\n'.join(out)


def render_archive(template, data):
    nav, sections = [], []
    for p in data:
        n = len(p['sheets'])
        cnt = f'<span class="count">{n}</span>' if n else ''
        nav.append(f'<a href="#{p["slug"]}">{esc(p["name"])}{cnt}</a>')
        if not n:
            body = ('<div class="coming-soon">Under construction. '
                    '<a href="https://github.com/The-CerealDev/speed-maths">Contribute a sheet</a>'
                    '</div>')
            stats = ''
        else:
            body = f'<ul class="sheet-list">{render_rows(p)}</ul>'
            qs = sum(s['questions'] for s in p['sheets'])
            stats = (f'<span class="stats"><b>{n}</b> sheets'
                     + (f' &middot; <b>{qs}</b> questions' if qs else '') + '</span>')
        sections.append(f'''
      <section class="pillar" id="{p['slug']}">
        <div class="pillar-head">
          <div>
            <h2>{esc(p['name'])}</h2>
            <p class="pillar-desc">{esc(p['desc'])}</p>
          </div>
          {stats}
        </div>
        {body}
      </section>''')
    return (template
            .replace('<!-- NAV -->', '\n'.join(nav))
            .replace('<!-- PILLARS -->', '\n'.join(sections)))


def render_classic(template, data):
    """The original: one card per pillar, placeholders named per pillar.

    Deliberately ignores `\\SpeedMeta` and always labels a row "Sheet NN". This
    view exists to be compared against the new one, so it has to keep rendering
    what it rendered before — feeding it the new metadata would make the two
    views differ by more than their layout and answer the wrong question.
    """
    html = template
    for p in data:
        ph = f"<!-- PILLAR_{p['slug'].upper().replace('-', '_')} -->"
        if not p['sheets']:
            block = ('<div class="coming-soon">Currently under construction. '
                     'Want to contribute? <a href="https://github.com/The-CerealDev/'
                     'speed-maths">View GitHub repo</a></div>')
        else:
            items = []
            for s in p['sheets']:
                name = f"Sheet {s['n']}"
                ans = (f'<a href="{s["answers"]}" class="pdf-link ans" '
                       f'target="_blank">Answers</a>' if s['answers'] else '')
                items.append(f'''
                    <li>
                        <span class="sheet-name">{name}</span>
                        <div class="links">
                            <a href="{s['pdf']}" class="pdf-link" target="_blank">Questions</a>
                            {ans}
                        </div>
                    </li>''')
            block = '<ul class="sheet-list">' + '\n'.join(items) + '</ul>'
        html = html.replace(ph, block)
    return html


def build():
    data = scan()
    for tpl_name, out_name in TEMPLATES:
        tpl_path = os.path.join(ROOT_DIR, tpl_name)
        if not os.path.exists(tpl_path):
            print(f'  skip {out_name}: no {tpl_name}')
            continue
        tpl = open(tpl_path, encoding='utf-8').read()
        render = render_archive if 'PILLARS' in tpl else render_classic
        open(os.path.join(ROOT_DIR, out_name), 'w', encoding='utf-8').write(
            render(tpl, published(data)))
        print(f'  {out_name}')

    # Emitted for the site's client-side search, and it doubles as the answer to
    # "what is actually in this repo" for anything else that wants to know.
    with open(os.path.join(ROOT_DIR, 'sheets.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print('  sheets.json')

    # Emit robots.txt and sitemap.xml for search engine indexing.
    with open(os.path.join(ROOT_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: https://speedmaths.co.uk/sitemap.xml\n')
    print('  robots.txt')

    live = published(data)
    sitemap_urls = [
        ('https://speedmaths.co.uk/', 'weekly', '1.0'),
        ('https://speedmaths.co.uk/classic.html', 'monthly', '0.5'),
    ]
    for p in live:
        for s in p['sheets']:
            if s.get('pdf'):
                sitemap_urls.append((f"https://speedmaths.co.uk/{s['pdf']}", 'monthly', '0.8'))
            if s.get('answers'):
                sitemap_urls.append((f"https://speedmaths.co.uk/{s['answers']}", 'monthly', '0.8'))

    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, prio in sitemap_urls:
        sitemap_lines.append(f'  <url>\n    <loc>{loc}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>')
    sitemap_lines.append('</urlset>\n')

    with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap_lines))
    print('  sitemap.xml')
    total = sum(len(p['sheets']) for p in live)
    annotated = sum(1 for p in live for s in p['sheets'] if s['topic'])
    print(f'{total} sheets published across {len(live)} pillars; '
          f'{annotated} annotated with \\SpeedMeta, {total - annotated} without')

    held = [p for p in data if p['status'] != 'live' and p['sheets']]
    for p in held:
        print(f'  held back ({p["status"]}): {p["name"]} — '
              f'{len(p["sheets"])} sheets not listed on the site')

    odd = [(p['name'], s['n'], s['questions']) for p in data for s in p['sheets']
           if s['questions'] and s['questions'] != 33]
    for name, n, q in odd:
        print(f'  note: {name} sheet{n} has {q} questions, not the standard 33')


if __name__ == '__main__':
    build()
