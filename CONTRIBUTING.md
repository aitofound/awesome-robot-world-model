# Contributing to the Atlas

The Atlas is a companion to a specific manuscript snapshot. Maintain its scope, terminology and citation traceability when adding or correcting material.

## Authoritative inputs

| File | Purpose |
|---|---|
| `data/catalog.json` | Bibliographic records, canonical keys, aliases, chapter membership and identity-check provenance |
| `data/atlas.json` | Brand title, exact paper-section navigation, role definitions and reviewed method annotations |
| `data/resources.json` | Upstream artifacts, type, use, source check and maintenance notes |
| `data/organization.json` | Reviewed logical reading routes and one home placement per cited work |
| `data/citation-map.json` | All original argument groups, citation occurrences and source-relative locators |

`README.md`, the catalog, role views, method cards, chapter guides, resource page, provenance page, CSV and BibTeX are generated. Edit their inputs and regenerate them. The scope, reading-path and evaluation documents are maintained prose.

## Add a paper or annotation

1. Confirm the work is cited in the corresponding active manuscript snapshot. Update the snapshot and citation accounting when the paper changes; do not silently expand a companion catalog into unrelated literature.
2. Reuse an existing canonical record when its DOI, arXiv identity or known title variant matches. Preserve every old citation alias. Check title differences instead of merging merely similar names.
3. Record actual source and access coverage. `source-derived` means metadata inherited from the manuscript. `primary-identity-checked` requires a recorded primary metadata source and check time. It does not mean that the science was independently validated.
4. For an annotation, describe the predictive interface, downstream consumer and changed object, plus the decisive evidence boundary. Use an explicit entry kind. Do not assign strict closed-loop qualification solely from a name or architecture.
5. Link an official resource only after checking its identity. State whether it is a dataset, environment, implementation, policy context or representation prior. Keep link retrieval separate from package execution and reproduction.

An annotation has the following shape:

```json
{
  "paper": "existing-canonical-key",
  "name": "System name",
  "roles": ["prediction", "planning"],
  "kind": "world-model-use",
  "interface": "Conditioning and predicted quantity.",
  "consumer_and_change": "Consumer, changed action or learner, and feedback destination.",
  "boundary": "Tested scope and the distinction needed to interpret the claim.",
  "annotation_basis": "manuscript-synthesis",
  "source_chapters": ["representations"]
}
```

Keep frozen-model learning, context conditioning, action correction and neural weight adaptation distinct. Do not infer a causal graph from a causal-sounding name, or online feedback from physical open-loop execution. Keep related names such as OmniVTA and OmniVTLA separate.

Choose a readable home placement based on the work’s actual purpose in the survey. A dataset mentioned in an imitation-learning paragraph can belong in the resource route. A safety reference introduced as a future direction can belong in the evaluation route. Preserve all original argument contexts even when the browsing order changes. The citation map must match the active source snapshot; the public repository does not contain the private manuscript. `tools/layout.py` contains reviewed short introductions for the annotated entries.

## Generate and check

Python 3.10 or newer is sufficient. The local generation and validation scripts use the standard library and make no network calls.

```bash
python tools/generate.py
python tools/validate.py
python tools/generate.py --check
```

Validation checks record uniqueness, citation aliases, chapter and role references, required annotation fields, metadata provenance, resource identities, CSV/BibTeX coverage, local Markdown targets and generated-file consistency. It does not run robot software or certify empirical claims.

## Attribution and corrections

Write original annotations and link to the primary work. External papers and software retain their upstream rights and licenses. Do not upload full papers, unpublished manuscript files, dataset copies or private task records as part of ordinary catalog maintenance.

For a correction, keep the source title or earlier interpretation where it is needed to explain a version difference. Never replace a missing URL, venue, result or artifact with a guess. There is no pooled performance leaderboard in this repository.
