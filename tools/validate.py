"""Offline consistency and navigation checks for the companion repository; no scientific certification."""
from __future__ import annotations
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import generate

ROOT = Path(__file__).resolve().parents[1]
ARXIV = re.compile(r'(?:\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?')


def valid_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    # Raw < and > occur in DOIs; generate.url() encodes them. Whitespace marks a corrupted record.
    return parsed.scheme in {'https', 'http'} and bool(parsed.netloc) and not any(c.isspace() for c in value)


def check_catalog(s):
    errors, aliases, arxiv, doi, anchors = [], {}, {}, {}, {}
    ids = [p['id'] for p in s.catalog['papers']]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate canonical paper IDs')
    for p in s.catalog['papers']:
        key = p['id']
        for field in ['title', 'authors', 'publication_type', 'cited_in', 'aliases', 'metadata_status']:
            if not p.get(field):
                errors.append(f'{key}: missing {field}')
        if p['aliases'][:1] != [key]:
            errors.append(f'{key}: canonical key must be the first alias')
        for a in p['aliases']:
            if a in aliases and aliases[a] != key:
                errors.append(f'{key}: alias {a!r} also belongs to {aliases[a]}')
            aliases[a] = key
        a = generate.anchor(key)
        if a in anchors:
            errors.append(f'{key}: anchor collides with {anchors[a]}')
        anchors[a] = key
        if set(p['cited_in']) - set(s.units):
            errors.append(f'{key}: cited_in names an unknown heading')
        if p['paper_url'] and not valid_url(p['paper_url']):
            errors.append(f'{key}: malformed paper URL')
        for field, seen, pattern in [('arxiv_id', arxiv, ARXIV), ('doi', doi, re.compile(r'10\.\d{4,9}/\S+'))]:
            value = p.get(field)
            if not value:
                continue
            if not pattern.fullmatch(value):
                errors.append(f'{key}: malformed {field} {value!r}')
            base = re.sub(r'v\d+$', '', value).lower()
            if base in seen:
                errors.append(f'{key}: {field} duplicates {seen[base]}')
            seen[base] = key
        if p['metadata_status'] not in {'source-derived', 'primary-identity-checked'}:
            errors.append(f'{key}: unknown metadata status')
        if p['metadata_status'] == 'primary-identity-checked':
            check = p.get('primary_check') or {}
            if not valid_url(check.get('source')):
                errors.append(f'{key}: primary check lacks a source')
            try:
                datetime.fromisoformat(check.get('checked_at', ''))
            except ValueError:
                errors.append(f'{key}: primary check lacks a timestamp')
    return errors


def check_mapping(s):
    errors = []
    cited = {p for g in s.groups for p in g['papers']}
    if cited != set(s.papers):
        errors.append(f'Citation map and catalog disagree on {len(cited ^ set(s.papers))} works')
    for g in s.groups:
        if len(g['papers']) != len(g['citations']):
            errors.append(f"{g['id']}: papers and citation counts differ in length")
        for unit in [g['section'], g['subsection'], g['subsubsection']]:
            if unit and unit not in s.units:
                errors.append(f"{g['id']}: unknown heading {unit}")
        for p in g['papers']:
            if (g['subsection'] or g['section']) not in s.papers[p]['cited_in']:
                errors.append(f"{p}: cited in {g['subsection'] or g['section']} but cited_in omits it")
    for p, home in s.homes.items():
        if home not in s.papers[p]['cited_in']:
            errors.append(f'{p}: home {home} is not a heading that cites it')
        if home == 'sec:intro' and len(s.papers[p]['cited_in']) > 1 and any(
                s.units[u]['section']['number'] in generate.MAIN_RANGE for u in s.papers[p]['cited_in']):
            errors.append(f'{p}: home is the introduction although Sections 2-8 cite it')
    for key, unit in s.companion['home_overrides'].items():
        if key not in s.papers or unit not in s.papers[key]['cited_in']:
            errors.append(f'home override {key} -> {unit} is not a citing heading')
    return errors


def check_companion(s):
    errors = []
    c = s.companion
    if c['companion_to'] != s.catalog['source']['title']:
        errors.append('companion_to differs from the catalog source title')
    outline_ids = {sec['id'] for sec in s.mapping['outline']}
    for sid, meta in c['sections'].items():
        if sid not in outline_ids:
            errors.append(f'section {sid} is absent from the manuscript outline')
        if not meta.get('summary') or not meta.get('slug'):
            errors.append(f'section {sid}: missing summary or slug')
        if meta.get('figure') and meta['figure'] not in c['figures']:
            errors.append(f"section {sid}: unknown figure {meta['figure']}")
    for name in c['figures']:
        for ext in ['svg', 'png']:
            if not (ROOT / 'assets' / 'figures' / f'{name}.{ext}').is_file():
                errors.append(f'figure {name}.{ext} is missing; run tools/export_figures.py')
        svg = ROOT / 'assets' / 'figures' / f'{name}.svg'
        if svg.is_file() and '<rect width="100%" height="100%" fill="#ffffff"/>' not in svg.read_text(encoding='utf-8'):
            errors.append(f'figure {name}.svg lacks the white background; re-run tools/export_figures.py')
    for item in c['dials'] + c['pathways']:
        if item['subsection'] not in s.units:
            errors.append(f"{item.get('id') or item['name']}: unknown subsection {item['subsection']}")
    for t in c['tree']:
        if t['subsection'] not in s.units:
            errors.append(f"Figure 2 leaf under unknown heading {t['subsection']}")
        for item in t['leaf']:
            if item['paper'] and item['paper'] not in s.papers:
                errors.append(f"Figure 2 item {item['name']!r} names uncited key {item['paper']}")
    for key in c['names']:
        if key not in s.papers:
            errors.append(f'display name for uncited key {key}')
    for table in ['evidence_atlas', 'resources', 'reading_map']:
        for row in s.manuscript[table]['rows']:
            for k in row['papers']:
                if s.alias.get(k, k) not in s.papers:
                    errors.append(f'{table}: {row["name"]} cites unknown key {k}')
    names = [r['name'] for r in s.code]
    if len(names) != len(set(names)):
        errors.append('Duplicate code repository name')
    for r in s.code:
        if r['paper'] not in s.papers:
            errors.append(f"{r['name']}: repository paper absent from catalog")
        if not valid_url(r['repository']) or not valid_url((r.get('primary_check') or {}).get('source')):
            errors.append(f"{r['name']}: repository or check source malformed")
    return errors


def figure2_notes(s):
    """Figure 2 items whose key is not cited under the subsection that lists them (reported, not errors)."""
    notes = []
    for t in s.companion['tree']:
        for item in t['leaf']:
            if item['paper'] and t['subsection'] not in s.papers[item['paper']]['cited_in']:
                notes.append(f"{item['name']} ({item['paper']}) listed under {s.unit_label(t['subsection'])}")
    return notes


def markdown_anchors(content):
    found = set(re.findall(r'<a\s+id="([^"]+)"', content))
    occurrences = {}
    for line in content.splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match.group(1))
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        count = occurrences.get(slug, 0)
        occurrences[slug] = count + 1
        found.add(slug + (f'-{count}' if count else ''))
    return found


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attribute in {'a': ['href'], 'img': ['src'], 'source': ['srcset']}.get(tag, []):
            if attribute in attrs:
                self.links.append(attrs[attribute])


def check_markdown(root):
    errors, checked = [], 0
    files = [root / 'README.md', root / 'CONTRIBUTING.md', *sorted((root / 'docs').rglob('*.md'))]
    contents = {p: p.read_text(encoding='utf-8') for p in files}
    targets = {p: markdown_anchors(content) for p, content in contents.items()}
    for source, content in contents.items():
        parser = LocalLinks()
        parser.feed(content)
        for raw in re.findall(r'\]\(([^)\n]+)\)', content) + parser.links:
            raw = raw.strip().strip('<>')
            if urlsplit(raw).scheme:
                continue
            path, _, fragment = raw.partition('#')
            target = (source.parent / unquote(path)).resolve() if path else source.resolve()
            checked += 1
            if not target.is_relative_to(root.resolve()):
                errors.append(f'{source.relative_to(root)}: link leaves repository: {raw}')
            elif not target.is_file():
                errors.append(f'{source.relative_to(root)}: missing target {raw}')
            elif fragment and target.suffix == '.md' and unquote(fragment) not in targets.get(target, set()):
                errors.append(f'{source.relative_to(root)}: missing anchor {raw}')
    return errors, checked, len(files)


def main():
    s = generate.Survey()
    errors = check_catalog(s) + check_mapping(s) + check_companion(s)
    link_errors, links, files = check_markdown(ROOT)
    errors += link_errors
    for note in figure2_notes(s):
        print('note: Figure 2 lists', note)
    if errors:
        print('\n'.join(errors[:80]))
        sys.exit(f'{len(errors)} validation errors')
    print(f"Validated {len(s.papers)} works, {len(s.groups)} citation groups, {len(s.code)} code repositories, "
          f"{links} local links in {files} Markdown files.")


if __name__ == '__main__':
    main()
