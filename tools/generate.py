"""Generate the manuscript companion from reviewed JSON inputs (standard library only)."""
from __future__ import annotations
import argparse
import csv
import html
import io
import json
from pathlib import Path
import re
import layout

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def anchor(key):
    return 'paper-' + re.sub(r'[^a-z0-9-]', '-', key.lower())


def text(value):
    value = html.escape(str(value or ''), quote=False)
    return re.sub(r'([\[\]*|`])', r'\\\1', value).replace('\n', ' ')


def paper_link(paper):
    return f"[Paper](<{paper['paper_url']}>)" if paper['paper_url'] else 'Source metadata only'


def chapter_path(chapter):
    return f"docs/chapters/{chapter['number'].lower()}-{chapter['id']}.md"


def card_link(key, label, prefix=''):
    return f'[{text(label)}]({prefix}methods.md#{anchor(key)})'


def outputs():
    atlas, catalog, resources = load('atlas.json'), load('catalog.json'), load('resources.json')['resources']
    organization, mapping = load('organization.json'), load('citation-map.json')
    papers = catalog['papers']
    lookup = {p['id']: p for p in papers}
    cards = atlas['curated']
    chapters = atlas['chapters']
    chapter_lookup = {c['id']: c for c in chapters}
    primary = sum(p['metadata_status'] == 'primary-identity-checked' for p in papers)
    arxiv = sum(bool(p['arxiv_id']) and bool(p['primary_check']) for p in papers)
    unresolved = sum(not p['paper_url'] for p in papers)
    result = {}
    methods = ['# Annotated methods and context', '', '[Home](../README.md) · [Role views](roles.md) · [Full catalog](catalog.md)', '',
               'Annotations are original syntheses of the companion survey. `world-model-use` identifies a discussed predictive use, not an automatic certificate of strict closed-loop qualification. '
               'Other kinds explicitly retain representation priors, policy context, general generation and benchmark literature.', '',
               'Read the interface, consumer and boundary together. Paper metadata checks do not independently verify these mechanism annotations.', '']
    for c in cards:
        p = lookup[c['paper']]
        methods += [f'<a id="{anchor(p["id"])}"></a>', '', f"## {c['name']}", '',
                    f"**{text(p['title'])}** ({p['year'] or 'year unknown'}). {paper_link(p)} · [Catalog record](catalog.md#{anchor(p['id'])})", '',
                    f"**Kind:** `{c['kind']}`. **Roles:** " + ', '.join(f"[{next(r['title'] for r in atlas['roles'] if r['id']==role)}](roles.md#role-{role})" for role in c['roles']) + '.', '',
                    f"**Predictive interface.** {c['interface']}", '',
                    f"**Consumer and changed object.** {c['consumer_and_change']}", '',
                    f"**Evidence boundary.** {c['boundary']}", '',
                    '**Cited in:** ' + ', '.join(f"[{chapter_lookup[i]['number']}](chapters/{Path(chapter_path(chapter_lookup[i])).name})" for i in c['source_chapters']) + '.', '']
        contexts = [g for g in mapping['groups'] if p['id'] in g['papers']]
        methods += ['**Argument contexts:** ' + ' · '.join(f"[{text(' › '.join(g['heading_path']) or chapter_lookup[g['chapter']]['title'])}](chapters/{Path(chapter_path(chapter_lookup[g['chapter']])).name}#{g['id']})" for g in contexts) + '.', '']
        available = [r for r in resources if r['paper'] == p['id']]
        if available:
            methods += ['**Upstream resource:** ' + ', '.join(f"[{r['name']}]({r['repository']})" for r in available) + '.', '']
    result['docs/methods.md'] = '\n'.join(methods)

    role_doc = ['# Browse by functional role', '', '[Home](../README.md) · [Scope and taxonomy](scope-and-taxonomy.md)', '',
                'A system can appear in several roles. The entry kind and evidence boundary qualify each placement.', '']
    for r in atlas['roles']:
        role_doc += [f'<a id="role-{r["id"]}"></a>', '', f"## {r['title']}", '', r['definition'], '',
                     '| Entry | Kind | Consumer and change |', '|---|---|---|']
        for c in cards:
            if r['id'] in c['roles']:
                role_doc.append(f"| {card_link(c['paper'], c['name'])} | `{c['kind']}` | {text(c['consumer_and_change'])} |")
        role_doc += ['']
    result['docs/roles.md'] = '\n'.join(role_doc)

    cat_doc = ['# Complete manuscript citation catalog', '', '[Home](../README.md) · [Annotated methods](methods.md) · [Machine-readable JSON](../data/catalog.json)', '',
               'This is the deduplicated active-manuscript reference index, including contextual literature. '
               'A primary identity check compares bibliographic metadata; it is not an independent reading or replication of the scientific work. '
               'Publication years and venues otherwise follow the manuscript. Missing URLs remain explicit.', '']
    previous_year = object()
    for p in papers:
        if p['year'] != previous_year:
            cat_doc += [f"## {p['year'] or 'Year unknown'}", '']
            previous_year = p['year']
        authors = p['authors'][:6]
        author_text = '; '.join(authors) + ('; et al. (full list in JSON)' if len(p['authors']) > 6 else '')
        cat_doc += [f'<a id="{anchor(p["id"])}"></a>', '', f"### {text(p['title'])}", '',
                    f"{text(author_text)}. **{p['year'] or 'Year unknown'}**. {text(p['venue'] or 'Venue not supplied in source')}. {paper_link(p)}.", '',
                    f"**Metadata:** `{p['metadata_status']}`. **Citation keys:** " + ', '.join('`'+k+'`' for k in p['aliases']) + '.', '',
                    '**Paper sections:** ' + ', '.join(f"[{chapter_lookup[i]['number']}](chapters/{Path(chapter_path(chapter_lookup[i])).name})" for i in p['cited_in']) + '.', '']
        cat_doc += [f"[Reading-route placement](paper-index.md#entry-{p['id']}) · [Argument map](paper-map.md).", '']
        if p.get('manuscript_title') and p['manuscript_title'] != p['title']:
            cat_doc += [f"**Manuscript title retained for traceability:** {text(p['manuscript_title'])}.", '']
        if p.get('metadata_note'):
            cat_doc += [f"**Source note:** {p['metadata_note']}", '']
        if p['primary_check']:
            check = p['primary_check']
            cat_doc += [f"**Identity source:** [primary metadata]({check['source']}), checked {check['checked_at'][:10]}.", '']
            if check.get('resolution'):
                cat_doc += [f"**Version note:** {check['resolution']}", '']
    result['docs/catalog.md'] = '\n'.join(cat_doc)

    for c in chapters:
        selected = [e for e in cards if c['id'] in e['source_chapters']]
        groups = [g for g in mapping['groups'] if g['chapter']==c['id']]
        refs = list(dict.fromkeys(key for g in groups for key in g['papers']))
        page = [f"# {c['number']}. {c['title']}", '', '[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)', '',
                c['summary'], '', '## Reading questions', '']
        page += ['- '+q for q in c['questions']]
        page += ['', '## Interpretation boundary', '', c['boundary'], '', '## Selected annotations', '']
        page += ['- '+card_link(e['paper'],e['name'],'../') for e in selected] if selected else ['This section states the survey’s argument; follow the neighboring method guides for concrete systems.']
        page += ['', f'## References by argument ({len(refs)} distinct works)', '',
                 'The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. '
                 'For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.', '']
        if not groups:page += ['This section has no active citations.', '']
        for g in groups:
            page += [f'<a id="{g["id"]}"></a>', '', '### '+text(' › '.join(g['heading_path']) or 'Section opening'), '',
                     '| Year | Work | Primary entry |', '|---|---|---|']
            for key in g['papers']:
                p=lookup[key]
                page += [f"| {p['year'] or '?'} | [{text(p['title'])}](../catalog.md#{anchor(p['id'])}) | {paper_link(p)} |"]
            page+=['']
        result[chapter_path(c)] = '\n'.join(page)+ '\n'

    resource_doc = ['# Datasets, benchmarks and implementations', '', '[Home](../README.md) · [Paper section 12](chapters/12-resources.md)', '',
                    'These are upstream artifact entry points linked to works cited by the survey. The README endpoints were retrieved and their identity sections inspected. '
                    'Packages, datasets, weights and robot experiments were not installed or run. A repository link is not a reproduction result.', '',
                    'Model, Decision, Learning and Deployment are separate interface capabilities. Establish each from the artifact and chosen protocol rather than assigning a single maturity score.', '']
    for r in resources:
        p = lookup[r['paper']]
        resource_doc += [f"## {r['name']}", '', f"**Type:** `{r['kind']}`. [Repository]({r['repository']}) · [Cited paper](catalog.md#{anchor(p['id'])}).", '', r['use'], '']
        if r.get('project_url'):
            resource_doc += [f"[Dataset project]({r['project_url']}). {r.get('artifact_note','')}", '']
        if r.get('maintenance_note'):
            resource_doc += [f"**Maintenance:** {r['maintenance_note']}", '']
        resource_doc += [f"**Link provenance:** [retrieved upstream README]({r['primary_check']['source']}), {r['primary_check']['checked_at'][:10]}. No runtime validation.", '']
    result['docs/resources.md'] = '\n'.join(resource_doc)

    provenance = ['# Provenance and verification coverage', '', '[Home](../README.md)', '',
                  '## Manuscript authority', '',
                  f"The companion tracks **{catalog['source']['title']}**, source snapshot **{catalog['source']['manuscript_version']}**, dated **{atlas['snapshot']}**. "
                  'The active main file, all included chapter bodies, appendix, table and figure sources were read. The two embedded graphics were inspected visually. '
                  'Unused attic material and commented passages are outside this snapshot. Independent unmerged chapter edits were not substituted for the ZIP.', '',
                  '## Citation processing', '',
                  f"The active source has {catalog['source']['active_citation_keys']} nonempty citation keys. Empty trailing tokens were excluded. Duplicate identities were consolidated into {len(papers)} records while preserving every cited alias and chapter membership.", '',
                  '| Missing source key | Resolved bibliography key |', '|---|---|']
    provenance += [f'| `{k}` | `{v}` |' for k,v in catalog['source']['missing_key_resolutions'].items()]
    provenance += ['', 'The resolutions follow the system identity in the surrounding manuscript text. The CSV and BibTeX use canonical keys; the JSON retains aliases. The generated BibTeX is a normalized catalog export, not a replacement for the manuscript’s original bibliography file.', '',
                   '## Independent checks', '',
                   f'- **{arxiv} arXiv records:** identifiers and titles were compared with the official Atom API; the returned version and check time are recorded per work.',
                   '- **Published-title variant:** the Shumailov et al. Nature title was checked through its DOI record in Crossref; the linked arXiv work has an earlier title.',
                   '- **Title variants:** ABot-PhysWorld, ContactWorld and ACT-JEPA retain the current primary title and the manuscript title. The malformed Open X-Embodiment title was corrected against the primary record.',
                   '- **Official article:** GR00T N1.7’s title was checked on its NVIDIA article hosted by Hugging Face.',
                   f'- **{len(resources)} resource entries:** upstream README endpoints retrieved, identity sections inspected, no package execution.', '',
                   f"Total metadata marked `primary-identity-checked`: **{primary} works**. Other records remain `source-derived`. **{unresolved} records lack an extracted paper URL**. Titles with unresolved source encoding problems carry a per-record note.", '',
                   '## What these checks establish', '',
                   f'The checks support bibliographic identity, source coverage and navigable links. The {len(cards)} method annotations are editorial syntheses of the fully read manuscript. '
                   'They do not claim independent full-text reading of all 600 cited papers, replication of numerical results, execution of released code or validation on robot hardware. '
                   'No cross-paper leaderboard or unqualified closed-loop ranking is inferred.', '',
                   'The catalog separates publication type, source venue, identity status and chapter membership. Policy context and general predictive priors retain their own labels. '
                   'If a scientific interpretation changes, update its annotation and retain the source/version explanation.', '']
    provenance += ['## Second organization audit', '',
                   f"Organization reviewed on **{organization['reviewed_at']}** using ZYR. The existing complete active-manuscript reading was reused. "
                   f"A second pass inspected all **{len(mapping['groups'])}** citation-bearing argument groups, context witnesses for all **{len(cards)}** annotated entries, "
                   f"and proposed identity/context placements for all **{len(papers)}** works. Targeted body passages were reread where diagram witnesses were too general.", '',
                   'The final reading routes were revised editorially after that inspection. They prioritize understandable scientific uses and do not mechanically reproduce first citation order. '
                   'The [paper map](paper-map.md) and [citation-map JSON](../data/citation-map.json) retain every original placement and source-relative locator. '
                   'Private citation-bearing manuscript paragraphs are not published.', '',
                   'This second pass verifies organization against the manuscript. It does not claim a second full reading of every manuscript paragraph, '
                   'independent full-text verification of all external papers or reproduction of their results.', '']
    result['docs/provenance.md'] = '\n'.join(provenance)

    stream=io.StringIO(newline='')
    writer=csv.writer(stream,lineterminator='\n')
    writer.writerow(['id','title','authors','year','venue','paper_url','arxiv_id','doi','paper_sections','citation_aliases','metadata_status'])
    for p in papers:
        row=[p['id'],p['title'],'; '.join(p['authors']),p['year'],p['venue'],p['paper_url'],p['arxiv_id'],p['doi'],'; '.join(p['cited_in']),'; '.join(p['aliases']),p['metadata_status']]
        writer.writerow([("'"+str(v) if str(v or '').startswith(('=','+','-','@')) else v) for v in row])
    result['data/catalog.csv']='\ufeff'+stream.getvalue()
    bib=[]
    for p in papers:
        fields={'title':p['title'],'author':' and '.join(p['authors']),'year':p['year'],'url':p['paper_url'],'doi':p['doi'],'eprint':p['arxiv_id']}
        if p['arxiv_id']:fields['archivePrefix']='arXiv'
        entry_type=p['publication_type']
        if p['venue']:fields['journal' if entry_type=='article' else 'booktitle' if entry_type=='inproceedings' else 'note']=p['venue']
        body=',\n'.join('  '+key+' = {'+str(value).replace('\\','\\textbackslash{}')+'}' for key,value in fields.items() if value)
        bib.append(f"@{entry_type}{{{p['id']},\n{body}\n}}\n")
    result['data/references.bib']='% Normalized Atlas export. Citation aliases are retained in catalog.json.\n\n'+'\n'.join(bib)
    result.update(layout.build(atlas, catalog, resources, organization, mapping))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Check generated files without writing them')
    args=parser.parse_args()
    pending=[]
    generated=outputs()
    for name,content in generated.items():
        path=ROOT/name
        existing=None
        if path.exists():
            with path.open('r',encoding='utf-8',newline='') as handle:existing=handle.read()
        if existing != content:
            pending.append(name)
            if not args.check:
                path.parent.mkdir(parents=True,exist_ok=True)
                with path.open('w',encoding='utf-8',newline='') as handle:handle.write(content)
    if args.check and pending:
        raise SystemExit('Generated files are stale: '+', '.join(pending))
    print(f"{'Checked' if args.check else 'Generated'} {len(generated)} files; {'stale' if args.check else 'updated'}: {len(pending)}")


if __name__=='__main__':
    main()
