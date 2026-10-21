"""Generate the README, docs pages and exports from data/*.json (standard library only)."""
from __future__ import annotations
import argparse
from collections import defaultdict
import csv
import html
import io
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN_RANGE = {f'{n}' for n in range(2, 9)}  # Sections 2-8 carry the survey's detailed discussion


def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def anchor(key):
    return 'paper-' + re.sub(r'[^a-z0-9-]', '-', key.lower())


def unit_anchor(number):
    return 'sec-' + number.lower().replace('.', '-')


VENUES = [  # (pattern, short name) for venues written out in full in the manuscript bibliography
    (r'^arxiv', 'arXiv'), (r'neural information processing systems|neurips', 'NeurIPS'), (r'international conference on machine learning', 'ICML'),
    (r'international conference on learning representations', 'ICLR'), (r'conference on robot learning', 'CoRL'),
    (r'robotics: science and systems', 'RSS'), (r'computer vision and pattern recognition', 'CVPR'),
    (r'international conference on computer vision', 'ICCV'), (r'european conference on computer vision', 'ECCV'),
    (r'international conference on robotics and automation', 'ICRA'), (r'intelligent robots and systems', 'IROS'),
    (r'transactions on machine learning research', 'TMLR'), (r'robotics and automation letters', 'RA-L'),
    (r'autonomous agents and multiagent systems', 'AAMAS'), (r'association for the advancement of artificial intelligence|aaai conference', 'AAAI'), (r'science robotics', 'Science Robotics'),
]


def short_venue(venue):
    if not venue:
        return ''
    for pattern, name in VENUES:
        if re.search(pattern, venue, re.I):
            return name
    acronym = re.search(r'\(([A-Z][A-Za-z\-]{1,9})\)', venue)
    return acronym.group(1) if acronym else re.sub(r'^(?:19|20)\d\d\s+|\s+(?:19|20)\d\d$', '', venue)


def display_title(title):
    """Render TeX-style subscripts in system names, e.g. π_0.5 as π0.5 and π^*_0.6 as π*0.6."""
    return re.sub(r'([πτ])(\^\*)?_\{?([0-9.]*)\}?', lambda m: m.group(1) + ('*' if m.group(2) else '') + m.group(3), title)


def plural(n, word):
    return f"{n} {word}{'' if n == 1 else 's'}"


def text(value):
    value = html.escape(str(value or ''), quote=False)
    value = re.sub(r'([\[\]*|`_])', r'\\\1', value).replace('\n', ' ')
    return re.sub(r'\\_\{([^}]*)\}', r'<sub>\1</sub>', value)


def url(value):
    """A link destination that CommonMark accepts inside angle brackets."""
    return value.replace(' ', '%20').replace('<', '%3C').replace('>', '%3E')


class Survey:
    """Indexes the manuscript outline, citation groups and catalog."""

    def __init__(self):
        self.companion, self.catalog, self.mapping = load('companion.json'), load('catalog.json'), load('citation-map.json')
        self.manuscript, self.code = load('manuscript.json'), load('resources.json')['resources']
        self.papers = {p['id']: p for p in self.catalog['papers']}
        self.alias = {a: p['id'] for p in self.catalog['papers'] for a in p['aliases']}
        self.sections = [s for s in self.mapping['outline'] if s['id'] in self.companion['sections']]
        self.units = {}
        for s in self.mapping['outline']:
            self.units[s['id']] = {'section': s, 'node': s}
            for sub in s.get('subsections', []):
                self.units[sub['id']] = {'section': s, 'node': sub}
                for leaf in sub.get('subsubsections', []):
                    self.units[leaf['id']] = {'section': s, 'node': leaf, 'parent': sub}
        self.label = {l: node['id'] for s in self.mapping['outline'] for node in [s, *s.get('subsections', [])] for l in node.get('labels', [])}
        for t in self.companion['tree']:
            t['subsection'] = self.label.get(t['subsection'], t['subsection'])
        self.groups = self.mapping['groups']
        self.code_by_paper = defaultdict(list)
        for r in self.code:
            self.code_by_paper[r['paper']].append(r)
        self.tree = {t['subsection']: t['leaf'] for t in self.companion['tree']}
        self.homes = self.compute_homes()

    # A work's home is the subsection that discusses it; the README lists each work there once.
    def compute_homes(self):
        votes = defaultdict(lambda: defaultdict(lambda: [0, 10**6, 10**6]))
        for rank, g in enumerate(self.groups):
            unit = g['subsection'] or g['section']
            for paper, n in zip(g['papers'], g['citations']):
                v = votes[paper][unit]
                v[0] += n
                v[1] = min(v[1], len(g['papers']))
                v[2] = min(v[2], rank)
        tree_units = defaultdict(list)
        for order, t in enumerate(self.companion['tree']):
            for item in t['leaf']:
                if item['paper']:
                    tree_units[item['paper']].append((order, t['subsection']))
        homes = {}
        for paper, units in votes.items():
            if paper in self.companion['home_overrides']:
                homes[paper] = self.companion['home_overrides'][paper]
                continue
            listed = [u for _, u in sorted(tree_units.get(paper, [])) if u in units]
            if listed:
                homes[paper] = max(listed, key=lambda u: (units[u][0], -listed.index(u)))
                continue
            def tier(unit):
                s = self.units[unit]['section']
                if s['document'] == 'supplement':
                    return 2
                return 0 if s['number'] in MAIN_RANGE else 1
            best = min(tier(u) for u in units)
            pool = [u for u in units if tier(u) == best]
            homes[paper] = min(pool, key=lambda u: (-units[u][0], units[u][1], units[u][2]))
        return homes

    def page(self, section, prefix=''):
        meta = self.companion['sections'][section['id']]
        num = section['number'].lower()
        return f"{prefix}docs/sections/{num.zfill(2) if num.isdigit() else num}-{meta['slug']}.md"

    def unit_link(self, unit, prefix=''):
        info = self.units[unit]
        node = info.get('parent') or info['node']
        target = self.page(info['section'], prefix)
        return target if node is info['section'] else f"{target}#{unit_anchor(node['number'])}"

    def unit_label(self, unit):
        node = self.units[unit]['node']
        return f"{node['number']} {node['title']}" if node['number'] else node['title']

    def name(self, key):
        name = self.companion['names'].get(key)
        return display_title(name) if name else None

    def entry(self, key, catalog_prefix=None, code=True):
        """One Markdown line for a work: name, title link, venue and year, code."""
        p = self.papers[key]
        name, title = self.name(key), display_title(p['title'])
        if name and re.sub(r'\W', '', name.lower()) == re.sub(r'\W', '', title.lower()):
            name = None
        prefix = re.match(r'(?i:' + re.escape(name) + r')(?:\s*:\s*|\s+[-–]\s+)', title) if name else None
        if prefix and re.match(r'[A-Z0-9]', title[prefix.end():]):
            title = title[prefix.end():]
        elif prefix:
            name = None  # the title already opens with the name
        linked = f"[{text(title)}](<{url(p['paper_url'])}>)" if p['paper_url'] else text(title)
        parts = [f"**{text(name)}**: {linked}" if name else linked]
        venue = ' '.join(x for x in [text(short_venue(p['venue'])), str(p['year'] or '')] if x)
        if venue:
            parts.append(venue)
        for r in self.code_by_paper.get(key, []) if code else []:
            parts.append(f"[Code](<{url(r['repository'])}>)")
        if catalog_prefix is not None:
            parts.append(f"[ⓘ]({catalog_prefix}catalog.md#{anchor(key)})")
        return ' · '.join(parts)

    def leaf_text(self, unit, catalog_prefix):
        items = []
        for item in self.tree.get(unit, []):
            if item['paper'] and item['paper'] in self.papers:
                items.append(f"[{text(item['name'])}]({catalog_prefix}catalog.md#{anchor(item['paper'])})")
            else:
                items.append(text(item['name']))
        return ', '.join(items)


def figure(s, name, prefix):
    meta = s.companion['figures'][name]
    return f"[![{meta['alt']}]({prefix}assets/figures/{name}.svg)]({prefix}assets/figures/{name}.svg)"


def readme(s):
    c = s.companion
    papers_by_home = defaultdict(list)
    for key in s.papers:
        papers_by_home[s.homes[key]].append(key)
    out = ['<a id="top"></a>', '', '<div align="center">', '',
           f'<img src="assets/awesome-rwm.png" width="200" alt="{c["title"]} logo">', '',
           f'<h1>{c["title"]}</h1>', '',
           f'<p>Companion repository to the survey<br><b>{c["companion_to"]}</b></p>', '']
    links = [f'<a href="{url}"><b>{label}</b></a>' for label, url in [('📄 Paper', c['paper_links'].get('arxiv') or c['paper_links'].get('pdf'))] if url]
    links += ['<a href="#papers"><b>📚 Papers by section</b></a>', '<a href="docs/evidence-atlas.md"><b>🔬 Evidence atlas</b></a>',
              '<a href="docs/resources.md"><b>🧰 Resources</b></a>', '<a href="docs/catalog.md"><b>🔎 Catalog</b></a>']
    out += ['<p>' + ' &nbsp;·&nbsp; '.join(links) + '</p>', '', '</div>', '']
    out += [' '.join(c['summary']), '']

    out += ['## 🗺️ How the survey is organized', '', figure(s, 'structure', ''), '',
            '*Figure 1 of the survey, read clockwise.* '
            'The model (§3) is specified by four design dials; its predictions reach the robot through five pathways (§4) '
            'that feed either policy learning or action selection (§5). The real world sets the requirements (§6) and is the only place '
            'where utility is measured (§7). Deployment data travel back along the outer loop to refit the model (§8).', '']

    out += ['## 🎛️ Four design dials', '', '| Dial | Question | Spectrum | Trade-off |', '|---|---|---|---|']
    for d in c['dials']:
        out.append(f"| [**{d['id']}**]({s.unit_link(d['subsection'])}) | {d['question']} | {d['ends'][0]} ↔ {d['ends'][1]} | {d['tradeoff'][0]} ↔ {d['tradeoff'][1]} |")
    out += ['', '<details>', '<summary><b>Technical routes as dial settings</b> (Figure 4)</summary>', '', figure(s, 'dials', ''), '', '</details>', '']

    out += ['## 🔀 Five pathways', '', '| | Pathway | The model hands over | At learning time | At acting time | Typical failure |', '|---|---|---|---|---|---|']
    for p in c['pathways']:
        out.append(f"| {p['number']} | [**{p['name']}**]({s.unit_link(p['subsection'])}) | {p['hands_over']} | {p['learning_time'] or ''} | {p['acting_time'] or ''} | {p['typical_failure']} |")
    out += ['', 'Any use that changes model or policy parameters from deployment data belongs to the outer loop (§8).', '',
            '<details>', '<summary><b>Evidence map: pathway against prediction space</b> (Figure 9)</summary>', '', figure(s, 'evidence-map', ''), '', '</details>', '']

    out += ['<a id="papers"></a>', '', '## 📚 Papers by section', '',
            f"The {len(s.papers)} works cited in the survey, each listed once under the subsection that discusses it. "
            '★ marks the representative works that Figure 2 names for a subsection. '
            'Each section page lists every citation in the order of the text.', '']
    for sec in s.sections:
        meta = c['sections'][sec['id']]
        if sec['document'] == 'supplement':
            continue
        out += [f"### {meta.get('emoji', '')} {sec['number']} · {text(sec['title'])}".replace('###  ', '### '), '',
                f"{meta['summary'][0]} [Section page →]({s.page(sec)})", '']
        out += unit_lists(s, sec, papers_by_home)
    out += ['### 📎 Supplementary Material', '']
    for sec in s.sections:
        if sec['document'] == 'supplement':
            out += [f"**{sec['number']} · [{text(sec['title'])}]({s.page(sec)})**. {c['sections'][sec['id']]['summary'][0]}", '']
            out += unit_lists(s, sec, papers_by_home)

    out += ['## 🧭 Seven takeaways', '', figure(s, 'takeaways', ''), '']
    out += ['## 🧰 Companion tables and data', '',
            f"- [Evidence atlas](docs/evidence-atlas.md): {len(s.manuscript['evidence_atlas']['rows'])} claim-level records with pathway, evidence level and limits (Supplementary S2).",
            f"- [Reading map](docs/reading-map.md): {len(s.manuscript['reading_map']['rows'])} entries by primary and secondary cluster (Supplementary S3).",
            f"- [Resources](docs/resources.md): {len(s.manuscript['resources']['rows'])} datasets, simulators, models and benchmarks (Supplementary S1), with code repositories.",
            '- [Glossary](docs/glossary.md) of loop terms and the [minimum reporting checklist](docs/reporting-checklist.md) (Appendix A).',
            '- [Catalog](docs/catalog.md) of all cited works with citation keys. Machine-readable: '
            '[catalog.json](data/catalog.json), [citation-map.json](data/citation-map.json), [manuscript.json](data/manuscript.json), '
            '[CSV](data/catalog.csv), [BibTeX](data/references.bib).', '']
    if c.get('citation'):
        out += ['## 📝 Citation', '', '```bibtex', c['citation'].strip(), '```', '']
    out += ['## 🤝 Contributing', '',
            'This repository follows the survey. Corrections to bibliographic records, paper links and code repositories are welcome; '
            'see [CONTRIBUTING.md](CONTRIBUTING.md). Works that the survey does not cite enter with a revision of the survey.', '',
            '## 📄 License', '',
            'Text, data and figures in this repository are licensed under [CC BY 4.0](LICENSE); the code in `tools/` is under the [MIT License](tools/LICENSE). '
            'Linked papers, datasets and code keep their own licenses.', '',
            f"<sub>Synchronized with the manuscript on {s.catalog['source']['snapshot']}.</sub>", '', '[↑ Back to top](#top)', '']
    return '\n'.join(out)


def unit_lists(s, sec, papers_by_home):
    out = []
    units = [(sec['id'], sec['title'] if not sec.get('subsections') else 'Section opening')] + [(sub['id'], None) for sub in sec.get('subsections', [])]
    for unit, label in units:
        keys = papers_by_home.get(unit, [])
        leaves = s.tree.get(unit, [])
        featured = [i['paper'] for i in leaves if i['paper'] in s.papers]
        if not keys and not featured:
            continue
        if not keys:
            out += [f"**{text(label or s.unit_label(unit))}** · Figure 2: " + ', '.join(
                f"[{text(s.name(k) or s.papers[k]['title'])}]({s.unit_link(s.homes[k])}) ({s.unit_label(s.homes[k]).split(' ')[0]})" for k in featured) + '.', '']
            continue
        order = {k: i for i, k in enumerate(k for g in s.groups if (g['subsection'] or g['section']) == unit for k in g['papers'])}
        keys = sorted(keys, key=lambda k: (k not in featured, featured.index(k) if k in featured else order.get(k, 10**6)))
        summary = f"<b>{text(label or s.unit_label(unit))}</b>"
        if leaves:
            summary += ' · ' + html.escape(', '.join(i['name'] for i in leaves))
        summary += ' · ' + plural(len(keys), 'work')
        out += ['<details>', f'<summary>{summary}</summary>', '']
        out += ['- ' + s.entry(k) + (' ★' if k in featured else '') for k in keys]
        elsewhere = [k for k in featured if k not in keys]
        if elsewhere:
            out += ['', '★ Also representative here (Figure 2): ' + ', '.join(
                f"[{text(s.name(k) or s.papers[k]['title'])}]({s.unit_link(s.homes[k])}) ({s.unit_label(s.homes[k]).split(' ')[0]})" for k in elsewhere) + '.']
        out += ['', '</details>', '']
    return out


def section_page(s, index):
    sec = s.sections[index]
    meta = s.companion['sections'][sec['id']]
    nav = ['[Home](../../README.md)']
    if index:
        prev = s.sections[index - 1]
        nav.append(f"[← {prev['number']} · {text(prev['title'])}]({Path(s.page(prev)).name})")
    if index + 1 < len(s.sections):
        nxt = s.sections[index + 1]
        nav.append(f"[{nxt['number']} · {text(nxt['title'])} →]({Path(s.page(nxt)).name})")
    out = [f"# {sec['number']} · {text(sec['title'])}", '', ' · '.join(nav), '']
    out += [' '.join(meta['summary']), '']
    if meta.get('figure'):
        out += [figure(s, meta['figure'], '../../'), '']
    if meta.get('tables'):
        titles = {'glossary': 'Glossary of loop terms', 'reporting-checklist': 'Minimum reporting checklist', 'resources': 'Resource catalogue',
                  'evidence-atlas': 'Evidence atlas', 'reading-map': 'Reading map'}
        out += ['Tables of this section: ' + ', '.join(f"[{titles[t]}](../{t}.md)" for t in meta['tables']) + '.', '']
    groups = [g for g in s.groups if g['section'] == sec['id']]
    total = len({k for g in groups for k in g['papers']})
    if total:
        out += [f"This section cites {plural(total, 'work')}. A work cited in several subsections appears under each; ⌂ marks the subsection where the README lists it.", '']
    blocks = [(None, sec)] + [(sub, sub) for sub in sec.get('subsections', [])]
    for sub, node in blocks:
        unit = node['id']
        unit_groups = [g for g in groups if (g['subsection'] or g['section']) == unit]
        if sub is not None:
            heading = f"{sub['number']} {sub['title']}" if sub['number'] else sub['title']
            out += [f'<a id="{unit_anchor(sub["number"])}"></a>' if sub['number'] else '', '', f"## {text(heading)}", '']
            if s.tree.get(unit):
                out += [f"*Representative works (Figure 2):* {s.leaf_text(unit, '../')}", '']
        elif not unit_groups:
            continue
        else:
            out += ['## Section opening', '']
        if not unit_groups and total:
            out += ['No citations.', '']
        for g in unit_groups:
            if g['subsubsection']:
                leaf = s.units[g['subsubsection']]['node']
                out += [f"### {text((leaf['number'] + ' ') if leaf['number'] else '')}{text(leaf['title'])}", '']
            out += ['- ' + s.entry(k, '../') + (' ⌂' if s.homes[k] == unit else '') for k in g['papers']] + ['']
    return '\n'.join(line for i, line in enumerate(out) if not (line == '' and i and out[i - 1] == '')) + '\n'


def table_page(title, intro, columns, rows, source):
    out = [f'# {title}', '', '[Home](../README.md)', '', intro, '', f'*Source: {source}.*', '',
           '| ' + ' | '.join(columns) + ' |', '|' + '---|' * len(columns)]
    out += ['| ' + ' | '.join(r) + ' |' for r in rows]
    return '\n'.join(out) + '\n'


def evidence_page(s):
    table, levels = s.manuscript['evidence_atlas'], s.companion['evidence_levels']
    out = ['# Evidence atlas', '', '[Home](../README.md) · [Reading map](reading-map.md)', '',
           f"{table['caption']}", '', f"*Source: Supplementary Material S2, {len(table['rows'])} records.*", '',
           '## Evidence levels', '']
    out += [f"- **{l['level']}**: {l['meaning']}." for l in levels['levels']] + ['']
    for note in levels['notes']:
        out += [note, '']
    out += ['## Records', '', '| Work | Pathway (P / S) | Loop location | Level | Scope |', '|---|---|---|---|---|']
    for r in table['rows']:
        key = s.alias.get(r['papers'][0], r['papers'][0])
        out.append(f"| [{text(r['name'])}](#{anchor(key)}) | {text(r['pathway'])} / {text(r['secondary_pathway'] or '–')} | "
                   f"{text(r['loop_location'])} | {r['level']} | {text(r['scope'])} |")
    out.append('')
    for r in table['rows']:
        key = s.alias.get(r['papers'][0], r['papers'][0])
        out += [f'<a id="{anchor(key)}"></a>', '', f"### {text(r['name'])}", '', s.entry(key, ''), '',
                f"- **Pathway:** P: {text(r['pathway'])}; S: {text(r['secondary_pathway'] or '–')}; loop location: {text(r['loop_location'])}.",
                f"- **Regime / mechanism:** P: {text(r['regime'])}; S: {text(r['mechanism'] or '–')}.",
                f"- **Source / object:** {text(r['source'])}; {text(r['object'])}.",
                f"- **Level / scope:** {r['level']}; {text(r['scope'])}.",
                f"- **Claim:** {text(r['claim'])}",
                f"- **Source locator (cited work):** {text(r['locator'])}",
                f"- **Limit:** {text(r['limit'])}", '']
    return '\n'.join(out)


def resources_page(s):
    table = s.manuscript['resources']
    listed = set()
    rows = []
    for r in table['rows']:
        keys = [s.alias.get(k, k) for k in r['papers']]
        listed.update(keys)
        code = ' '.join(f"[Code](<{url(c['repository'])}>)" for k in keys for c in s.code_by_paper.get(k, []))
        paper = ' '.join(f"[Paper](<{url(s.papers[k]['paper_url'])}>)" for k in keys if s.papers[k]['paper_url'])
        rows.append([f"**{text(r['name'])}**"] + [text(x) for x in r['cells']] + [' '.join(x for x in [paper, code] if x)])
    out = table_page('Resources', table['caption'], table['columns'] + ['Links'], rows, 'Supplementary Material S1').split('\n')
    extra = [c for c in s.code if c['paper'] not in listed]
    out += ['## Further code repositories', '', 'Official repositories of other works cited in the survey.', '',
            '| Repository | Work | Kind |', '|---|---|---|']
    out += [f"| [{text(c['name'])}](<{url(c['repository'])}>) | {s.entry(c['paper'], '', code=False)} | `{c['kind']}` |" for c in extra]
    notes = [c for c in s.code if c.get('maintenance_note') or c.get('artifact_note')]
    if notes:
        out += ['', '**Notes.** ' + ' '.join(f"{c['name']}: {c.get('maintenance_note') or c.get('artifact_note')}" for c in notes)]
    out += ['', 'Each repository link was checked against the upstream README; see the `primary_check` field in [resources.json](../data/resources.json). '
            'Packages were not installed or run.', '']
    return '\n'.join(out)


def catalog_page(s):
    out = ['# Catalog of cited works', '', '[Home](../README.md) · [catalog.json](../data/catalog.json) · [BibTeX](../data/references.bib)', '',
           f"All {len(s.papers)} works cited in the survey and its supplementary material, newest first. "
           '`source-derived` metadata comes from the manuscript bibliography; `primary-identity-checked` records were compared with a primary source, '
           'which checks bibliographic identity only.', '']
    year = object()
    for p in s.catalog['papers']:
        if p['year'] != year:
            year = p['year']
            out += [f"## {year or 'Year unknown'}", '']
        authors = ('; '.join(p['authors'][:6]) + ('; et al' if len(p['authors']) > 6 else '')).rstrip('.')
        cited = ', '.join(f"[{text(s.unit_label(u))}](../{s.unit_link(u)})" for u in p['cited_in'])
        out += [f'<a id="{anchor(p["id"])}"></a>', '', f"### {text(display_title(p['title']))}", '',
                f"{text(authors)}. {text(p['venue']) + '. ' if p['venue'] else ''}{p['year'] or ''}. "
                + (f"[Paper](<{url(p['paper_url'])}>)" if p['paper_url'] else 'No paper link recorded') + '.', '',
                f"**Cited in:** {cited}. **Keys:** " + ', '.join(f'`{k}`' for k in p['aliases'])
                + f". **Metadata:** `{p['metadata_status']}`" + (f", checked {p['primary_check']['checked_at'][:10]}" if p.get('primary_check') else '') + '.', '']
    return '\n'.join(out)


def exports(s):
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['id', 'title', 'authors', 'year', 'venue', 'paper_url', 'arxiv_id', 'doi', 'cited_in', 'home', 'citation_aliases', 'metadata_status'])
    for p in s.catalog['papers']:
        row = [p['id'], p['title'], '; '.join(p['authors']), p['year'], p['venue'], p['paper_url'], p['arxiv_id'], p['doi'],
               '; '.join(p['cited_in']), s.homes[p['id']], '; '.join(p['aliases']), p['metadata_status']]
        writer.writerow([("'" + str(v) if str(v or '').startswith(('=', '+', '-', '@')) else v) for v in row])
    bib = []
    for p in s.catalog['papers']:
        fields = {'title': p['title'], 'author': ' and '.join(p['authors']), 'year': p['year'], 'url': p['paper_url'], 'doi': p['doi'], 'eprint': p['arxiv_id']}
        if p['arxiv_id']:
            fields['archivePrefix'] = 'arXiv'
        kind = p['publication_type']
        if p['venue']:
            fields['journal' if kind == 'article' else 'booktitle' if kind == 'inproceedings' else 'note'] = p['venue']
        body = ',\n'.join('  ' + k + ' = {' + str(v).replace('\\', '\\textbackslash{}') + '}' for k, v in fields.items() if v)
        bib.append(f"@{kind}{{{p['id']},\n{body}\n}}\n")
    return {'data/catalog.csv': '﻿' + stream.getvalue(),
            'data/references.bib': '% Export of the works cited in the survey. Earlier citation keys are listed in catalog.json.\n\n' + '\n'.join(bib)}


def outputs():
    s = Survey()
    result = {'README.md': readme(s)}
    for i in range(len(s.sections)):
        result[s.page(s.sections[i])] = section_page(s, i)
    result['docs/evidence-atlas.md'] = evidence_page(s)
    result['docs/resources.md'] = resources_page(s)
    m = s.manuscript
    result['docs/reading-map.md'] = table_page(
        'Reading map', m['reading_map']['caption'], m['reading_map']['columns'],
        [[s.entry(s.alias.get(r['papers'][0], r['papers'][0]), '') if len(r['papers']) == 1 else
          f"**{text(r['name'])}**: " + ', '.join(s.entry(s.alias.get(k, k), '') for k in r['papers'])] + [text(x) for x in r['cells']]
         for r in m['reading_map']['rows']], 'Supplementary Material S3')
    result['docs/glossary.md'] = table_page('Glossary of loop terms', m['glossary']['caption'], m['glossary']['columns'],
                                            [[f"**{text(r['name'])}**"] + [text(x) for x in r['cells']] for r in m['glossary']['rows']], 'Appendix A.4')
    result['docs/reporting-checklist.md'] = table_page('Minimum reporting checklist', m['reporting_checklist']['caption'], m['reporting_checklist']['columns'],
                                                       [[f"**{text(r['name'])}**"] + [text(x) for x in r['cells']] for r in m['reporting_checklist']['rows']], 'Appendix A.3')
    result['docs/catalog.md'] = catalog_page(s)
    result.update(exports(s))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated files without writing them')
    args = parser.parse_args()
    generated, pending = outputs(), []
    for name, content in generated.items():
        path = ROOT / name
        existing = path.read_text(encoding='utf-8') if path.exists() else None
        if existing != content:
            pending.append(name)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open('w', encoding='utf-8', newline='') as handle:
                    handle.write(content)
    stale = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'docs').rglob('*.md') if str(p.relative_to(ROOT)) not in generated)
    if args.check and (pending or stale):
        raise SystemExit('Generated files are stale: ' + ', '.join(pending + stale))
    print(f"{'Checked' if args.check else 'Generated'} {len(generated)} files; {'stale' if args.check else 'updated'}: {len(pending)}"
          + (f"; not generated: {', '.join(stale)}" if stale else ''))


if __name__ == '__main__':
    main()
