"""Synchronize the manuscript-derived data with a manuscript source tree (standard library only).

Reads main.tex and supplement.tex in input order and rewrites three files:
  data/citation-map.json  section outline and the works cited under each heading
  data/manuscript.json    verbatim tables (evidence atlas, resources, reading map, glossary, checklist)
  data/catalog.json       membership fields; reviewed identity checks and metadata are kept
New citation keys are filled from the manuscript bibliography and marked source-derived.
The input is the manuscript's LaTeX source with its references.bib (the Overleaf checkout).

    python tools/extract.py --paper ../paper [--revision arXiv-v1] [--aux BUILD_DIR] [--dry-run]
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import date
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = [('main', 'main.tex'), ('supplement', 'supplement.tex')]
LEVELS = ['section', 'subsection', 'subsubsection']
TOKEN = re.compile(r'\\(?:(section|subsection|subsubsection)(\*?)\s*(?:\[[^\]]*\])?\s*\{|label\{([^}]*)\}|(appendix)\b'
                   r'|(?:no)?cite[a-zA-Z]*\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}|begin\{(equation)\})')
REFS = {}  # label -> printed reference, filled while parsing; used by detex
TABLES = {  # manuscript.json field: (document, table label)
    'evidence_atlas': ('supplement', 'tab:frontier-atlas'),
    'resources': ('supplement', 'tab:resources'),
    'reading_map': ('supplement', 'tab:atlas-cluster-mapping'),
    'glossary': ('main', 'tab:glossary'),
    'reporting_checklist': ('main', 'tab:min-reporting-checklist'),
}


def strip_comments(source):
    return '\n'.join(re.sub(r'(?<!\\)%.*', '', line) for line in source.split('\n'))


def expand(path, paper, seen=()):
    """Return the source of a file with \\input and \\include expanded in place."""
    if path in seen:
        raise SystemExit(f'Cyclic \\input: {path}')
    text = strip_comments(path.read_text(encoding='utf-8'))

    def replace(match):
        target = paper / match.group(2)
        if target.suffix != '.tex':
            target = target.with_name(target.name + '.tex')
        return expand(target, paper, seen + (path,)) if target.exists() else ''
    return re.sub(r'\\(input|include)\{([^}]*)\}', replace, text)


def balanced(text, start):
    """Return (content, end) of the brace group whose opening brace precedes start."""
    depth, i = 1, start
    while depth:
        if text[i - 1] != '\\':
            depth += {'{': 1, '}': -1}.get(text[i], 0)
        i += 1
    return text[start:i - 1], i


def split_top(text, sep):
    """Split on sep at brace depth zero, ignoring escaped separators."""
    parts, depth, start, i = [], 0, 0, 0
    while i < len(text):
        ch = text[i]
        if ch in '{}' and text[i - 1:i] != '\\':
            depth += 1 if ch == '{' else -1
        elif depth == 0 and text.startswith(sep, i) and text[i - 1:i] != '\\':
            parts.append(text[start:i])
            start = i = i + len(sep)
            continue
        i += 1
    return parts + [text[start:]]


GREEK = {'pi': 'π', 'omega': 'ω', 'times': '×', 'phi': 'φ', 'theta': 'θ', 'Delta': 'Δ', 'varepsilon': 'ε', 'to': '→', 'leftrightarrow': '↔'}


def math(segment):
    """Plain-text rendering of inline math; subscripts stay as _{...} for the page generator."""
    segment = re.sub(r'\\partial\s*', '∂', segment.replace('\\mid', '|').replace('\\,', ' ').replace('\\;', ' '))
    segment = re.sub(r'\\(?:mathcal|mathrm|mathbf|text)\{([^{}]*)\}', r'\1', segment)
    segment = re.sub(r'\\hat\s*\{?\\?([A-Za-z])\}?', lambda m: GREEK.get(m.group(1), m.group(1)) + '\u0302', segment)
    segment = re.sub(r'\\([A-Za-z]+)', lambda m: GREEK.get(m.group(1), m.group(0)), segment)
    segment = re.sub(r'_([A-Za-z0-9θφ])', r'_{\1}', segment)
    segment = re.sub(r'_\{([^{}]*)\}', lambda m: '\x00' + m.group(1) + '\x01', segment)
    return re.sub(r'Δ\s+', 'Δ', segment).replace('{', '').replace('}', '')


def detex(value):
    value = re.sub(r'~?\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{[^}]*\}', '', value or '')
    value = re.sub(r'\\supp\{([^}]*)\}', r'Supplementary Material S\1', value)
    value = re.sub(r'\\(?:Cref|cref|ref)\{([^}]*)\}', lambda m: ', '.join(REFS.get(k.strip(), '') for k in m.group(1).split(',')), value)
    value = value.replace('\\slashsep', ' / ').replace('\\newline', ' ')
    value = value.replace('\\mid', '|')
    value = re.sub(r'\\([A-Za-z]+)', lambda m: GREEK.get(m.group(1), m.group(0)), value)
    value = re.sub(r'\\(?:emph|textit|textbf|textsc|texttt|mathrm|mathcal|mathbf|text|textcolor\{[^}]*\})\{([^{}]*)\}', r'\1', value)
    value = re.sub(r'\$\^\{?([^}$]*)\}?\$', r'^\1', value)
    value = re.sub(r'\$π_\{?0\}?\$|π_\{?0\}?', 'π0', value)
    value = re.sub(r'\$([^$]*)\$', lambda m: math(m.group(1)), value)
    value = value.replace('$', '').replace('\\&', '&').replace('\\%', '%').replace('\\_', '_').replace('~', ' ')
    value = value.replace('---', '—').replace('--', '–').replace('``', '“').replace("''", '”').replace("\\'e", 'é').replace("\\'{e}", 'é')
    value = re.sub(r'\\[a-zA-Z]+\*?\s*', '', value)
    value = ' '.join(value.replace('{', '').replace('}', '').replace('\\', '').split())
    return value.replace('\x00', '_{').replace('\x01', '}')


def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')


def document_text(doc, paper):
    text = expand(paper / dict(DOCUMENTS)[doc], paper)
    return text[text.index('\\begin{document}'):]


def parse_document(doc, paper):
    """Return the heading outline and the citation groups of one document in reading order."""
    text = document_text(doc, paper)
    numbers, appendix, current = [0, 0, 0], False, [None, None, None]
    pending, pending_end, outline, groups, equations = None, 0, [], {}, 0
    prefix = 'S' if doc == 'supplement' else ''
    pos = 0
    while (m := TOKEN.search(text, pos)):
        pos = m.end()
        level, star, label, is_appendix, keys, equation = m.groups()
        if equation:
            equations += 1
        elif is_appendix:
            appendix, numbers = True, [0, 0, 0]
        elif level:
            title, pos = balanced(text, m.end())
            depth = LEVELS.index(level)
            number = None
            if not star:
                numbers[depth] += 1
                numbers[depth + 1:] = [0] * (2 - depth)
                head = chr(64 + numbers[0]) if appendix else f'{prefix}{numbers[0]}'
                number = '.'.join([head] + [str(n) for n in numbers[1:depth + 1]])
            node = {'id': None, 'labels': [], 'number': number, 'title': detex(title), 'children': []}
            if depth == 0:
                node.update(document=doc, appendix=appendix)
                outline.append(node)
            elif current[depth - 1] is not None:
                current[depth - 1]['children'].append(node)
            current[depth:] = [node] + [None] * (2 - depth)
            pending, pending_end = node, pos
        elif label is not None:
            unit = next((n for n in reversed(current) if n is not None), None)
            if label.startswith('eq:') and doc == 'main':
                REFS[label] = f'Eq. ({equations})'
            elif unit and unit['number'] and not label.startswith(('fig:', 'tab:', 'eq:')):
                REFS.setdefault(label, ('Appendix ' if unit_is_appendix(outline) else 'Section ') + unit['number'])
            if pending and not text[pending_end:m.start()].strip():
                pending['id'] = pending['id'] or label
                pending['labels'].append(label)
                pending_end = m.end()
            else:
                pending = None
        elif keys is not None and current[0]:
            pending = None
            unit = next(n for n in reversed(current) if n is not None)
            group = groups.setdefault(id(unit), {'unit': unit, 'path': [n for n in current if n], 'papers': []})
            group['papers'] += [k.strip() for k in keys.split(',') if k.strip() and k.strip() != '*']

    def assign(node, parent_id):
        node['id'] = node['id'] or (parent_id + '/' if parent_id else 'sec:') + slug(node['title'])
        for child in node['children']:
            assign(child, node['id'])
    for node in outline:
        assign(node, None)

    def simplify(node, depth=0):
        out = {k: node[k] for k in ['id', 'number', 'title']}
        if len(node['labels']) > 1:
            out['labels'] = node['labels']
        if depth == 0:
            out.update(document=node['document'], appendix=node['appendix'])
        if node['children']:
            out['subsections' if depth == 0 else 'subsubsections'] = [simplify(c, depth + 1) for c in node['children']]
        return out
    result = []
    for g in groups.values():
        path = g['path']
        result.append({'document': doc, 'section': path[0]['id'], 'subsection': path[1]['id'] if len(path) > 1 else None,
                       'subsubsection': path[2]['id'] if len(path) > 2 else None, 'papers': g['papers']})
    return [simplify(n) for n in outline], result


def unit_is_appendix(outline):
    return bool(outline) and outline[-1].get('appendix') and outline[-1].get('document') == 'main'


def table_rows(text, label):
    """Return (caption, header, rows) of the tabular environment that carries label; cells keep their TeX."""
    at = text.index('\\label{' + label + '}')
    caption_at = text.rfind('\\caption{', 0, at + 1) if text.rfind('\\caption{', 0, at + 1) > text.rfind('\\begin{table', 0, at) else text.find('\\caption{', at - 2000)
    caption = detex(balanced(text, caption_at + len('\\caption{'))[0])
    start = text.index('\\toprule', at)
    header_end = text.index('\\midrule', start)
    header = [detex(c) for c in split_top(text[start + len('\\toprule'):header_end].strip().rstrip('\\').strip(), '&')]
    body_start = text.index('\\endhead', at) + len('\\endhead') if '\\endhead' in text[at:text.index('\\bottomrule', at)] else header_end + len('\\midrule')
    body = text[body_start:text.index('\\bottomrule', at)]
    rows = []
    for raw in split_top(body, '\\\\'):
        raw = re.sub(r'^\s*(?:\\addlinespace(?:\[[^\]]*\])?|\\midrule)\s*', '', raw)
        cells = [c.strip() for c in split_top(raw, '&')]
        if len(cells) == len(header):
            rows.append(cells)
    return caption, header, rows


def cited(cell):
    return [k.strip() for g in re.findall(r'\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}', cell) for k in g.split(',')]


def first_name(cell):
    return detex(re.split(r'\\newline|~?\\cite', cell)[0])


def parse_tables(paper):
    texts = {doc: document_text(doc, paper) for doc, _ in DOCUMENTS}
    out = {}
    for field, (doc, label) in TABLES.items():
        caption, header, rows = table_rows(texts[doc], label)
        entry = {'label': label, 'document': doc, 'caption': caption, 'columns': header, 'rows': []}
        for cells in rows:
            if field == 'evidence_atlas':
                parts = [re.split(r'\\newline', c) for c in cells]

                def tagged(items, tag):
                    value = next((detex(x)[len(tag):].strip() for x in items if detex(x).startswith(tag)), '')
                    return None if value in {'', '–', '-'} else value
                claim = {}
                for piece in parts[5]:
                    if (m := re.match(r'\s*\\textit\{([^}]*)\}\s*(.*)', piece, re.S)):
                        claim[detex(m.group(1)).rstrip(':').strip().lower()] = detex(m.group(2))
                row = {'name': first_name(cells[0]), 'papers': cited(cells[0]),
                       'pathway': tagged(parts[1], 'P:'), 'secondary_pathway': tagged(parts[1], 'S:'), 'loop_location': detex(parts[1][-1]),
                       'regime': tagged(parts[2], 'P:'), 'mechanism': tagged(parts[2], 'S:'),
                       'source': detex(parts[3][0]), 'object': detex(parts[3][-1]), 'level': detex(parts[4][0]),
                       'scope': detex(' '.join(parts[4][1:])), 'claim': claim.get('claim'),
                       'locator': claim.get('source locator (cited work)'), 'limit': claim.get('limit')}
                missing = [k for k, v in row.items() if v in (None, '', []) and k not in {'secondary_pathway', 'mechanism'}]
                if missing:
                    raise SystemExit(f"{label}: row {row['name']!r} lacks {missing}")
            else:
                row = {'name': first_name(cells[0]), 'papers': cited(cells[0]), 'cells': [detex(c) for c in cells[1:]]}
                if field in {'glossary', 'reporting_checklist'}:
                    row.pop('papers')
            entry['rows'].append(row)
        out[field] = entry
    return out


def parse_bib(path):
    entries, text = {}, strip_comments(path.read_text(encoding='utf-8'))
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        if m.group(1).lower() in {'comment', 'string', 'preamble'}:
            continue
        body, _ = balanced(text, m.start() + m.group(0).index('{') + 1)
        body = body[body.index(',') + 1:]
        fields = {}
        for f in re.finditer(r'(\w+)\s*=\s*', body):
            start = f.end()
            if body[start] == '{':
                value, _ = balanced(body, start + 1)
            elif body[start] == '"':
                value = body[start + 1:body.index('"', start + 1)]
            else:
                value = re.match(r'[^,\n]*', body[start:]).group(0)
            fields.setdefault(f.group(1).lower(), value.strip())
        entries[m.group(2)] = {'type': m.group(1).lower(), **fields}
    return entries


def bib_record(key, entry):
    authors = [detex(a) for a in re.split(r'\s+and\s+', entry.get('author', '')) if a.strip()]
    arxiv = re.search(r'(\d{4}\.\d{4,5})', ' '.join(entry.get(f, '') for f in ['eprint', 'url', 'journal']))
    year = re.search(r'\d{4}', entry.get('year', ''))
    return {'id': key, 'aliases': [key], 'title': detex(entry.get('title', key)), 'authors': authors or ['Unknown'],
            'year': int(year.group(0)) if year else None,
            'venue': detex(entry.get('journal') or entry.get('booktitle') or '') or None,
            'publication_type': entry.get('type', 'misc'),
            'paper_url': entry.get('url') or (f'https://arxiv.org/abs/{arxiv.group(1)}' if arxiv else None),
            'arxiv_id': arxiv.group(1) if arxiv else None, 'doi': entry.get('doi') or None,
            'cited_in': [], 'metadata_status': 'source-derived', 'primary_check': None}


def norm_title(value):
    return re.sub(r'[^a-z0-9]', '', detex(value or '').lower())


def revision_of(paper):
    try:
        head = subprocess.run(['git', '-C', str(paper), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, check=True)
        return 'manuscript@' + head.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return 'manuscript'


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--paper', required=True, type=Path, help='Manuscript source directory containing main.tex')
    parser.add_argument('--revision', help='Label for the manuscript version (default: git hash of --paper)')
    parser.add_argument('--dry-run', action='store_true', help='Print the report without writing data files')
    parser.add_argument('--aux', type=Path, help='Build directory with main.aux and supplement.aux; the extracted keys must equal their \\citation keys')
    args = parser.parse_args()
    paper = args.paper.resolve()
    bib = parse_bib(paper / 'references.bib') if (paper / 'references.bib').exists() else {}
    if not bib:
        print('warning: references.bib not found; new keys get placeholder metadata')
    catalog = json.loads((ROOT / 'data' / 'catalog.json').read_text(encoding='utf-8'))
    records = {p['id']: p for p in catalog['papers']}
    alias = {a: p['id'] for p in catalog['papers'] for a in p['aliases']}
    by_title = {norm_title(p['title']): p['id'] for p in catalog['papers']}
    by_arxiv = {p['arxiv_id']: p['id'] for p in catalog['papers'] if p.get('arxiv_id')}

    outline, groups = [], []
    for doc, _ in DOCUMENTS:
        sections, doc_groups = parse_document(doc, paper)
        outline += sections
        groups += doc_groups
    keys = list(dict.fromkeys(k for g in groups for k in g['papers']))
    if args.aux:
        for doc, _ in DOCUMENTS:
            aux = (args.aux / f'{doc}.aux').read_text(encoding='utf-8', errors='replace')
            expected = {k.strip() for m in re.finditer(r'\\citation\{([^}]*)\}', aux) for k in m.group(1).split(',') if k.strip()}
            found = {k for g in groups if g['document'] == doc for k in g['papers']}
            if expected != found:
                raise SystemExit(f'{doc}: extracted keys differ from {doc}.aux: missing {sorted(expected - found)[:10]}, extra {sorted(found - expected)[:10]}')
            print(f'{doc}: {len(found)} keys match {doc}.aux')
    report = {'renamed': [], 'added': [], 'missing_from_bib': [k for k in keys if k not in bib]}

    canonical = {}
    for key in keys:
        if key in alias:
            canonical[key] = alias[key]
            continue
        record = bib_record(key, bib.get(key, {}))
        match = by_arxiv.get(record['arxiv_id']) or by_title.get(norm_title(record['title']))
        if match:
            records[match]['aliases'].append(key)
            canonical[key] = match
        else:
            records[key] = record
            canonical[key] = key
            report['added'].append(key)
    # A record takes the key the manuscript now cites; earlier keys remain aliases.
    for rid in list(records):
        now = [a for a in records[rid]['aliases'] if a in canonical]
        if rid not in canonical and len(now) == 1:
            rec = records.pop(rid)
            rec['id'] = now[0]
            rec['aliases'] = [now[0]] + [a for a in rec['aliases'] if a != now[0]]
            records[now[0]] = rec
            report['renamed'].append(f'{rid} -> {now[0]}')
            for k, v in canonical.items():
                if v == rid:
                    canonical[k] = now[0]

    membership = defaultdict(list)
    for n, g in enumerate(groups, 1):
        counts = defaultdict(int)
        for k in g['papers']:
            counts[canonical[k]] += 1
        g['id'] = f'group-{n:03d}'
        g['papers'] = list(counts)
        g['citations'] = [counts[p] for p in g['papers']]
        unit = g['subsection'] or g['section']
        for p in g['papers']:
            if unit not in membership[p]:
                membership[p].append(unit)

    report['dropped'] = sorted(k for k in records if k not in membership)
    report['title_differs'] = [k for k in membership if k in bib and norm_title(bib[k].get('title')) not in
                               {norm_title(records[k]['title']), norm_title(records[k].get('manuscript_title'))}]
    papers = []
    for key, rec in records.items():
        rec['aliases'] = [key] + [a for a in rec['aliases'] if a != key]
        if key in membership:
            rec['cited_in'] = membership[key]
            rec.pop('home', None)
            papers.append(rec)
    papers.sort(key=lambda p: (-(p['year'] or 0), p['title'].lower()))
    revision = args.revision or revision_of(paper)
    supplement_units = {g['subsection'] or g['section'] for g in groups if g['document'] == 'supplement'}
    main_units = {g['subsection'] or g['section'] for g in groups if g['document'] == 'main'}
    supplement_only = sum(not (set(p['cited_in']) & main_units) for p in papers)

    catalog.update(schema_version=2, papers=papers,
                   source={'title': catalog['source']['title'], 'revision': revision, 'snapshot': date.today().isoformat(),
                           'citation_keys': len(keys), 'works': len(papers),
                           'notes': ['Membership records citation presence in the manuscript, not closed-loop qualification.',
                                     'A primary identity check covers bibliographic metadata only.']})
    mapping = {'schema_version': 2, 'revision': revision, 'outline': outline, 'groups': groups}
    manuscript = {'schema_version': 1, 'revision': revision, **parse_tables(paper)}

    print(f"{len(keys)} citation keys -> {len(papers)} works in {len(groups)} groups ({supplement_only} supplement-only); "
          + ', '.join(f"{k}: {len(v['rows'])} rows" for k, v in manuscript.items() if isinstance(v, dict)))
    for label, items in report.items():
        print(f"{label}: {len(items)}" + (': ' + ', '.join(items) if items else ''))
    # Keep the earlier snapshot date when nothing else changed, so a rerun on the same manuscript is a no-op.
    previous = json.loads((ROOT / 'data' / 'catalog.json').read_text(encoding='utf-8'))
    if previous.get('source', {}).get('snapshot') and {**previous, 'source': {**previous['source'], 'snapshot': None}} == \
            {**catalog, 'source': {**catalog['source'], 'snapshot': None}}:
        catalog['source']['snapshot'] = previous['source']['snapshot']
    if not args.dry_run:
        for name, data in [('catalog.json', catalog), ('citation-map.json', mapping), ('manuscript.json', manuscript)]:
            (ROOT / 'data' / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
