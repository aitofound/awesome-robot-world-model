# Contributing

This repository accompanies the survey *From Prediction to Control: A Survey of Closed-Loop World Models for Robot Learning*. It lists the works the survey cites and follows the sections of the survey.

## What to change

Corrections to a title, author list, year, venue, paper link or code repository are welcome. Edit `data/catalog.json` or `data/resources.json`, record the primary source you checked in the `primary_check` field, and regenerate the pages.

The repository lists only works that the survey cites. A new work enters with a revision of the survey, so please suggest it in an issue.

Editorial text lives in `data/companion.json`: section summaries, the dial and pathway tables, the Figure 2 leaves, display names and home overrides. Each sentence restates the survey; name the section it comes from in the pull request.

## Data files

| File | Content | Written by |
|---|---|---|
| `data/catalog.json` | Bibliographic records, citation keys, the headings that cite each work, identity checks | `extract.py` for membership; maintainers for metadata and checks |
| `data/citation-map.json` | Outline of the survey and the works cited under each heading, in text order | `extract.py` |
| `data/manuscript.json` | Tables taken from the survey: evidence atlas, resource catalogue, reading map, glossary, reporting checklist | `extract.py` |
| `data/companion.json` | Editorial input for the pages | maintainers |
| `data/resources.json` | Official code repositories and the check of each link | maintainers |
| `assets/figures/` | Figures of the survey as SVG and PNG | `export_figures.py` |

`README.md`, `docs/`, `data/catalog.csv` and `data/references.bib` are generated; edit their inputs instead.

## Synchronize with a new manuscript version

```bash
python tools/extract.py --paper ../paper --revision arXiv-v2 --aux <build directory>
python tools/export_figures.py --paper ../paper
python tools/generate.py
python tools/validate.py
```

`extract.py` reads the LaTeX source together with `references.bib`. The Overleaf project contains the bibliography; an arXiv source bundle contains it only if `references.bib` was uploaded with the `.bbl`, so upload both. Without it, new keys receive placeholder metadata. With `--aux`, the script compares the extracted keys with the `\citation` entries of a compiled `main.aux` and `supplement.aux` and stops on any difference. It keeps reviewed metadata and identity checks, fills new keys from the bibliography as `source-derived`, and moves a record to the key the manuscript now cites while keeping earlier keys as aliases. Its report lists renamed, added and dropped keys, and `title_differs` lists records whose title differs from the manuscript bibliography. A dropped work disappears from every page.

`export_figures.py` needs `pdflatex` and `pdftocairo`. It compiles the manuscript once to resolve the section numbers drawn inside the figures.

`validate.py` also prints the Figure 2 items that the subsection listing them does not cite. These are notes for the authors of the survey, not errors.

## Where a work is listed

The README lists each work once, under its home subsection, chosen in this order:

1. a home override in `data/companion.json`;
2. a subsection that cites the work and whose Figure 2 leaf names it, the one with more citations first;
3. the subsection with the most citations of the work. Sections 2 to 8 take precedence over the introduction, open problems, conclusion and appendix, and these over the supplementary material. Ties go to the more specific subsection, then to the earlier one.

Section pages list every citation in the order of the text.

## Checks

```bash
python tools/validate.py
python tools/generate.py --check
```

Validation covers record uniqueness, citation aliases, identifiers, headings, home placement, Figure 2 keys, figure files, and local links and anchors. CI runs both commands. Neither runs robot software or certifies empirical claims; a primary identity check confirms bibliographic metadata only.

All tools use the Python 3.10+ standard library.

## Rights

Linked papers, datasets and code keep their authorship and upstream licenses. The repository does not redistribute papers or manuscript sources.
