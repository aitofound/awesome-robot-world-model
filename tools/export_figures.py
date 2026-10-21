"""Export manuscript TikZ figures to assets/figures/*.svg and *.png.

Requires pdflatex and pdftocairo (poppler). The manuscript tree is copied to a temporary
directory; one pdflatex pass over main.tex provides the section numbers drawn inside figures.

    python tools/export_figures.py --paper ../paper [--only structure,loop]
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FIGURES = {
    'structure': 'sections/s01_intro/taxonomy_figure',
    'loop': 'sections/s02_foundations/loop_figure',
    'dials': 'sections/s03_model/route_dials',
    'pathway-timing': 'sections/s04_pathways/pathway_timing',
    'evidence-map': 'sections/s04_pathways/evidence_map',
    'embodiment-requirements': 'sections/s06_embodiment/domain_requirements',
    'pathway-tests': 'sections/s07_evaluation/pathway_tests',
    'outer-loop': 'sections/s08_outer_loop/interaction_loop',
    'takeaways': 'sections/s10_conclusion/takeaways',
}


def run(*cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(f"{cmd[0]} failed in {cwd}:\n{result.stdout[-3000:]}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--paper', required=True, type=Path)
    parser.add_argument('--only', help='Comma-separated figure names')
    parser.add_argument('--dpi', type=int, default=200)
    args = parser.parse_args()
    names = args.only.split(',') if args.only else list(FIGURES)
    out = ROOT / 'assets' / 'figures'
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / 'paper'
        shutil.copytree(args.paper, work, ignore=shutil.ignore_patterns('.git', '*.pdf'))
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-draftmode', 'main.tex'], cwd=work, capture_output=True)
        labels = [l for l in (work / 'main.aux').read_text(encoding='utf-8', errors='replace').splitlines() if l.startswith('\\newlabel{')]
        (work / 'export_labels.tex').write_text('\\makeatletter\n' + '\n'.join(labels) + '\n\\makeatother\n', encoding='utf-8')
        main = (work / 'main.tex').read_text(encoding='utf-8')
        preamble = main[:main.index('\\begin{document}')]
        for name in names:
            body = ('\\usepackage[active,tightpage]{preview}\n\\setlength\\PreviewBorder{6pt}\n'
                    '\\input{export_labels.tex}\n\\begin{document}\n\\pagestyle{empty}\n'
                    f'\\begin{{preview}}\\input{{{FIGURES[name]}}}\\end{{preview}}\n\\end{{document}}\n')
            (work / f'fig-{name}.tex').write_text(preamble + body, encoding='utf-8')
            run('pdflatex', '-interaction=nonstopmode', f'fig-{name}.tex', cwd=work)
            run('pdftocairo', '-svg', f'fig-{name}.pdf', str(out / f'{name}.svg'), cwd=work)
            svg = out / f'{name}.svg'
            # An opaque page keeps the figure legible under GitHub's dark theme.
            source = svg.read_text(encoding='utf-8')
            if '</defs>' not in source:
                raise SystemExit(f'{svg.name}: no </defs> element to place the background after')
            svg.write_text(source.replace('</defs>', '</defs>\n<rect width="100%" height="100%" fill="#ffffff"/>', 1), encoding='utf-8')
            run('pdftocairo', '-png', '-singlefile', '-r', str(args.dpi), f'fig-{name}.pdf', str(out / name), cwd=work)
            print('exported', name)


if __name__ == '__main__':
    main()
