"""Offline consistency and navigation checks for the Atlas; no scientific certification."""
from __future__ import annotations
import csv
from datetime import datetime
import json
from pathlib import Path
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

import generate

ROOT = Path(__file__).resolve().parents[1]


def valid_url(value):
    if not isinstance(value,str):
        return False
    parsed=urlsplit(value)
    return parsed.scheme in {'https','http'} and bool(parsed.netloc) and not any(c.isspace() for c in value)


def check_data(catalog, atlas, resource_data):
    errors=[]
    papers=catalog['papers']
    ids=[p['id'] for p in papers]
    if len(ids) != len(set(ids)):errors.append('Duplicate canonical paper IDs')
    lookup={p['id']:p for p in papers}
    chapters={c['id'] for c in atlas['chapters']}
    roles={r['id'] for r in atlas['roles']}
    if len(chapters) != len(atlas['chapters']):errors.append('Duplicate chapter IDs')
    if len(roles) != len(atlas['roles']):errors.append('Duplicate role IDs')
    if atlas['companion_to'] != catalog['source']['title']:errors.append('Companion title differs from catalog source')
    aliases={};arxiv={};doi={};anchors={}
    for p in papers:
        key=p['id']
        for field in ['title','authors','publication_type','cited_in','aliases','metadata_status']:
            if not p.get(field):errors.append(f'{key}: missing {field}')
        if key not in p['aliases']:errors.append(f'{key}: canonical key absent from aliases')
        for alias in p['aliases']:
            if not alias or (alias in aliases and aliases[alias] != key):errors.append(f'{key}: duplicate/empty citation alias {alias!r}')
            aliases[alias]=key
        a=generate.anchor(key)
        if a in anchors:errors.append(f'{key}: anchor collision with {anchors[a]}')
        anchors[a]=key
        if set(p['cited_in'])-chapters:errors.append(f'{key}: unknown source chapter')
        if p['paper_url'] and not valid_url(p['paper_url']):errors.append(f'{key}: malformed paper URL')
        if p['arxiv_id']:
            if not re.fullmatch(r'(?:\d{4}\.\d{4,5}|(?:cs|math|physics|stat|q-bio|q-fin|astro-ph|cond-mat|gr-qc|hep-ex|hep-lat|hep-ph|hep-th|math-ph|nlin|nucl-ex|nucl-th|quant-ph)(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?',p['arxiv_id']):errors.append(f'{key}: malformed arXiv ID')
            base=re.sub(r'v\d+$','',p['arxiv_id'])
            if base in arxiv:errors.append(f'{key}: duplicate arXiv identity with {arxiv[base]}')
            arxiv[base]=key
        if p['doi']:
            base=p['doi'].lower()
            if not base.startswith('10.'):errors.append(f'{key}: malformed DOI')
            if base in doi:errors.append(f'{key}: duplicate DOI identity with {doi[base]}')
            doi[base]=key
        status=p['metadata_status']
        if status not in {'source-derived','primary-identity-checked'}:errors.append(f'{key}: unresolved metadata status {status}')
        if status=='primary-identity-checked':
            check=p.get('primary_check') or {}
            if not valid_url(check.get('source')):errors.append(f'{key}: missing primary identity source')
            try:datetime.fromisoformat(check['checked_at'].replace('Z','+00:00'))
            except (KeyError,ValueError):errors.append(f'{key}: missing/invalid primary check time')
            if check.get('title_matches') is False and not check.get('resolution'):errors.append(f'{key}: unresolved primary title mismatch')
    for missing,target in catalog['source']['missing_key_resolutions'].items():
        if missing not in aliases or target not in aliases or aliases[missing] != aliases[target]:errors.append(f'Unresolved source key alias: {missing}')
    kinds={'world-model-use','representation-prior','policy-context','generative-context','benchmark'}
    card_keys=[]
    for c in atlas['curated']:
        key=c['paper'];card_keys.append(key)
        if key not in lookup:errors.append(f'Annotation references unknown paper: {key}');continue
        for field in ['name','roles','kind','interface','consumer_and_change','boundary','annotation_basis','source_chapters']:
            if not c.get(field):errors.append(f'{key}: incomplete annotation field {field}')
        if set(c['roles'])-roles:errors.append(f'{key}: unknown role')
        if c['kind'] not in kinds:errors.append(f'{key}: unknown annotation kind')
        if set(c['source_chapters']) != set(lookup[key]['cited_in']):errors.append(f'{key}: annotation/source chapter drift')
        if not lookup[key]['paper_url']:errors.append(f'{key}: annotated entry lacks a paper link')
    if len(card_keys)!=len(set(card_keys)):errors.append('Duplicate annotated paper')
    resource_names=[]
    for r in resource_data['resources']:
        resource_names.append(r['name'])
        if r['paper'] not in lookup:errors.append(f"{r['name']}: resource paper absent from catalog")
        if not valid_url(r['repository']):errors.append(f"{r['name']}: malformed repository URL")
        if not valid_url(r['primary_check']['source']):errors.append(f"{r['name']}: missing resource source")
        if not r['kind'] or not r['use']:errors.append(f"{r['name']}: incomplete resource description")
    if len(resource_names)!=len(set(resource_names)):errors.append('Duplicate resource name')
    return errors


def markdown_anchors(content):
    found=set(re.findall(r'<a\s+id="([^"]+)"',content))
    occurrences={}
    for line in content.splitlines():
        match=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
        if not match:continue
        heading=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',match.group(1))
        slug=re.sub(r'[^\w\s-]','',heading.lower()).replace(' ','-')
        count=occurrences.get(slug,0);occurrences[slug]=count+1
        found.add(slug+(f'-{count}' if count else ''))
    return found


def check_markdown(root):
    errors=[];checked=0
    files=[root/'README.md',root/'CONTRIBUTING.md',*sorted((root/'docs').rglob('*.md'))]
    contents={p:p.read_text(encoding='utf-8') for p in files}
    targets={p:markdown_anchors(content) for p,content in contents.items()}
    for source,content in contents.items():
        class LocalHTMLLinks(HTMLParser):
            def __init__(self):super().__init__();self.links=[]
            def handle_starttag(self,tag,attrs):
                attrs=dict(attrs)
                for attribute in {'a':['href'],'img':['src'],'source':['srcset']}.get(tag,[]):
                    if attribute in attrs:self.links.append(attrs[attribute])
        parser=LocalHTMLLinks();parser.feed(content)
        for raw in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)',content)+parser.links:
            raw=raw.strip().strip('<>')
            if urlsplit(raw).scheme:continue
            path,_,fragment=raw.partition('#')
            target=(source.parent/unquote(path)).resolve() if path else source.resolve()
            checked+=1
            if not target.is_relative_to(root.resolve()):errors.append(f'{source.relative_to(root)}: link leaves repository: {raw}');continue
            if not target.is_file():errors.append(f'{source.relative_to(root)}: missing target {raw}');continue
            if fragment and target.suffix=='.md' and unquote(fragment) not in targets.get(target,set()):errors.append(f'{source.relative_to(root)}: missing anchor {raw}')
    return errors,checked,len(files)


def check_organization(catalog, atlas, organization, mapping):
    errors=[]
    papers={p['id']:p for p in catalog['papers']}
    aliases={a:p['id'] for p in papers.values() for a in p['aliases']}
    groups={g['id']:g for g in mapping['groups']}
    occurrences={o['id']:o for o in mapping['occurrences']}
    tracks={t['id'] for t in organization['tracks']}
    placements={p['paper']:p for p in organization['placements']}
    if len(groups)!=len(mapping['groups']):errors.append('Duplicate argument group')
    if len(occurrences)!=len(mapping['occurrences']):errors.append('Duplicate citation occurrence')
    if set(placements)!=set(papers) or len(placements)!=len(organization['placements']):errors.append('Reading-route coverage mismatch')
    seen_aliases=set();membership={p:set() for p in papers}
    for o in occurrences.values():
        if o['group'] not in groups:errors.append(f"Unknown citation argument: {o['group']}");continue
        if o['chapter']!=groups[o['group']]['chapter']:errors.append('Occurrence/group chapter drift')
        if o['source'] not in mapping['source_files'] or o['line']<1:errors.append('Missing source locator')
        if any(k not in aliases for k in o['citation_keys']):errors.append('Unresolved occurrence alias');continue
        expected=list(dict.fromkeys(aliases[k] for k in o['citation_keys']))
        if expected!=o['papers']:errors.append('Occurrence identity drift')
        seen_aliases.update(o['citation_keys'])
        for p in o['papers']:membership[p].add(o['chapter'])
    if len(seen_aliases)!=catalog['source']['active_citation_keys']:errors.append('Active source citation-key coverage mismatch')
    for g in groups.values():
        members=[]
        for i in g['occurrences']:
            if i not in occurrences or occurrences[i]['group']!=g['id']:errors.append('Group occurrence drift');continue
            for p in occurrences[i]['papers']:
                if p not in members:members.append(p)
        if members!=g['papers']:errors.append('Ordered group identity drift')
    for p,record in papers.items():
        if membership[p]!=set(record['cited_in']):errors.append(f'{p}: citation/chapter drift')
        placement=placements.get(p)
        if not placement:continue
        if placement['track'] not in tracks:errors.append(f'{p}: unknown reading route')
        if placement['context_group'] not in groups or p not in groups[placement['context_group']]['papers']:errors.append(f'{p}: home context lacks citation evidence')
        expected=[g['id'] for g in mapping['groups'] if p in g['papers']]
        if placement['all_groups']!=expected:errors.append(f'{p}: incomplete argument contexts')
    if atlas['repository_name']!='awesome-robot-world-model':errors.append('Repository name differs from locked name')
    if atlas['title']+': '+atlas['subtitle']!='From Prediction to Control: An Atlas of Robot World Models':errors.append('Full title differs from locked title')
    return errors


def main():
    catalog=generate.load('catalog.json');atlas=generate.load('atlas.json');resources=generate.load('resources.json')
    errors=check_data(catalog,atlas,resources)
    organization=generate.load('organization.json');mapping=generate.load('citation-map.json')
    errors.extend(check_organization(catalog,atlas,organization,mapping))
    for name,content in generate.outputs().items():
        path=ROOT/name
        if not path.exists():errors.append(f'Missing generated file: {name}');continue
        with path.open('r',encoding='utf-8',newline='') as handle:existing=handle.read()
        if existing!=content:errors.append(f'Stale generated file: {name}')
    navigation,links,markdown_files=check_markdown(ROOT)
    errors.extend(navigation)
    expected={p['id'] for p in catalog['papers']}
    with (ROOT/'data/catalog.csv').open(encoding='utf-8-sig',newline='') as handle:csv_rows=list(csv.DictReader(handle))
    if len(csv_rows)!=len(expected) or {r['id'] for r in csv_rows}!=expected:errors.append('CSV coverage mismatch')
    bib_keys=re.findall(r'^@\w+\{([^,]+),',(ROOT/'data/references.bib').read_text(encoding='utf-8'),re.M)
    if len(bib_keys)!=len(expected) or set(bib_keys)!=expected:errors.append('BibTeX coverage mismatch')
    if errors:
        for error in errors:print('FAIL:',error)
        raise SystemExit(1)
    print(json.dumps({'result':'PASS','catalog_records':len(expected),'reading_routes':len(organization['tracks']),'argument_groups':len(mapping['groups']),'citation_occurrences':len(mapping['occurrences']),'annotated_entries':len(atlas['curated']),'resources':len(resources['resources']),'markdown_files':markdown_files,'local_links_checked':links,'primary_identity_checked':sum(p['metadata_status']=='primary-identity-checked' for p in catalog['papers']),'scientific_replication':'NOT_PERFORMED'},indent=2))


if __name__=='__main__':
    main()
