"""GitHub-native reading routes and compact indices from reviewed manuscript inputs."""
from collections import defaultdict
import html
import re


def anchor(key):
    return 'paper-' + re.sub(r'[^a-z0-9-]', '-', key.lower())


def text(value):
    return re.sub(r'([\[\]*|`])', r'\\\1', html.escape(str(value), quote=False)).replace('\n', ' ')


def chapter_path(c):
    return f"docs/chapters/{c['number'].lower()}-{c['id']}.md"


BRIEFS = {
    'ha2018worldmodels':'A compact starting point for learned latent environments.',
    'hafner2019planet':'Plan candidate actions with latent dynamics and CEM.',
    'hafner2019dreamer':'Learn an actor and value model through latent imagination.',
    'hafner2021dreamerv2':'Discrete latent dynamics for imagined policy learning.',
    'hafner2023dreamerv3':'A shared world-model agent configuration across domains.',
    'hafner2025dreamer4':'Scale agent training inside learned worlds.',
    'wu2022daydreamer':'Connect latent imagination to physical robot learning.',
    'hansen2024tdmpc2':'Combine latent planning with scalable continuous control.',
    'zhou2025dinowm':'Predict frozen visual features for goal-directed planning.',
    'assran2025vjepa2':'Separate video pretraining from action-grounded V-JEPA 2-AC.',
    'actjepa2025':'Predictive representations and action-chunk learning.',
    'nam2026causaljepa':'Object-level predictive dependencies; retain identifiability limits.',
    'liu2026odeworld':'Continuous latent prediction conditioned on observation and goal.',
    'pointworld2026':'Scene point-flow prediction and MPPI; hardware execution is open-loop.',
    'jiang2025phystwin':'Build deformable physical twins from sparse videos.',
    'worldplanner2025':'Action-conditioned visual prediction for MCTS and MPC.',
    'chen2025largevideoplanner':'Video prediction for long-horizon plans; retain execution limits.',
    'robodreamer2024':'Instruction-conditioned, compositional imagined futures.',
    'li2025roboticworldmodel':'A learned neural simulator for policy optimization.',
    'interactiveworldsim2026':'Interactive demonstration generation and policy evaluation.',
    'li2026hiwm':'Human correction through simulator rollback and branching.',
    'qiu2026gesim2':'Filter generated rollouts for supervised policy updates.',
    'gu2026geniworld':'Ground interactive video prediction in rendered robot actions.',
    'jang2025dreamgen':'Recover synthetic robot trajectories from generated videos.',
    'gao2026dreamdojo':'Human-video interaction priors followed by robot grounding.',
    'nsim_wovr':'Use action-conditioned simulation to post-train VLA policies.',
    'nsim_roboworld':'Compare policies in neural simulation; correlation is not calibration.',
    'li2025worldeval':'Use predicted consequences to evaluate robot policies.',
    'vlarft2025':'Policy GRPO with rewards from a frozen world simulator.',
    'worldgymnast2026':'Use learned-world interaction for robot policy learning.',
    'nvidia2025cosmos':'Pretrained world-model components and generative priors.',
    'nvidia2026cosmos3':'Shared multimodal understanding, prediction and action interfaces.',
    'bruce2024genie':'Latent-action interactive environments from passive video.',
    'tian2019manipulation':'Predict tactile images to servo toward a contact goal.',
    'ai2024robopack':'Infer physical state from vision and touch for planning.',
    'wi2022virdopp':'Predict deformable state from vision, contact and force.',
    'zhang2026contactworld':'Study which visual-tactile representations help prediction.',
    'omnivta2026':'Use tactile forecasts and feedback for execution-time correction.',
    'visuotactilewm2026':'Visual-tactile latent dynamics and open-loop physical planning.',
    'yuan2026dextacwam':'Transfer video priors into dexterous tactile world-action modeling.',
    'yuan2026vtam':'Joint video, tactile and action modeling.',
    'tian2026vtwam':'Route contact information into world-action prediction.',
    'lou2026dreamtac':'Joint future vision, touch and action with contact-aware fusion.',
    'wu2026tactilewam':'Asymmetric tactile attention for world-action modeling.',
    'higuera2024sparsh':'Reusable self-supervised tactile features.',
    'feng2025anytouch':'Static and dynamic tactile representations across sensors.',
    'cheng2025omnivtla':'Tactile-conditioned VLA policy context, distinct from OmniVTA.',
    'clark2026muse':'Add force sensing while testing retention of earlier behavior.',
    'bharadhwaj2025gen2act':'Condition robot behavior on generated human task motion.',
    'liang2025dreamitate':'Convert generated task motion into robot behavior.',
    'egowam2026':'Compare predictive targets using human and robot data.',
    'chen2026anyworld':'Factor human motion, camera and embodiment conditions.',
    'zhou2026zerowam':'Condition frozen world-action models on human demonstrations.',
    'feng2026wamttt':'Adapt fast weights from human video before execution.',
    'tactalign2026':'Align human and robot touch for policy transfer.',
    'egozero2025':'Extract robot-grounded learning signals from smart glasses.',
    'vlaw2026':'Refit the world model with real rollouts, then train on selected data.',
    'xue2026worldsample':'Route real and counterfactual transitions into critic and policy learning.',
    'wamrl2026':'Actor RL and world-model video fine-tuning use separate objectives.',
    'liu2024runtime':'Predict near-term failures to support deployment monitoring.',
    'liu2025siriusfleet':'Allocate fleet supervision using prospective anomaly prediction.',
    'govind2026regen':'Generate replay for continual world-action imitation learning.',
    'liu2025onlinewm':'Refit predictive models for planning across changing environments.',
    'shang2026worldarena':'Evaluate perception and functional world-model utility.',
    'yue2025ewmbench':'Diagnose scene, motion and semantic generation quality.',
    'worldinworld2025':'Study world-model assessment in a closed-loop setting.',
    'huang2024safedreamer':'Use predicted costs in constrained policy learning.',
    'openvla2024':'An open VLA action prior and policy baseline.',
    'pi0':'A foundation policy with flow-matching action generation.',
    'nvidia2026groot17':'A reasoning VLA with an action-cascade interface.',
}
KIND = {'world-model-use':'Predictive use','representation-prior':'Representation prior','policy-context':'Policy context','generative-context':'Generative context','benchmark':'Benchmark'}


def argument_blocks(track, chapters, in_docs=False):
    """Render one reviewed argument for both the expandable home and open guide."""
    logic=track['logic']
    def relative(value):
        return value.replace('](docs/', '](') if in_docs else value
    blocks=['**The question.** '+relative(logic['question']), '', '**Reading chain**', '']
    for number,(title,explanation) in enumerate(logic['steps'],1):
        blocks += [f'{number}. **{title}.** {relative(explanation)}']
    blocks += ['']
    for title,explanation in logic['comparisons']:
        blocks += [f'**{title}**', '', relative(explanation), '']
    blocks += ['**What would establish usefulness?**', '', relative(logic['evidence']), '',
               '**Where the argument goes next.** '+relative(logic['next']), '']
    source_links=[]
    for key in logic['source_chapters']:
        chapter=chapters[key]
        path=chapter_path(chapter)
        source_links.append(f"[{chapter['number']}. {chapter['title']}]({path.removeprefix('docs/') if in_docs else path})")
    blocks += ['**Survey connections:** '+ ' · '.join(source_links)+'.', '']
    return blocks


def build(atlas, catalog, resources, organization, mapping):
    papers={p['id']:p for p in catalog['papers']}
    cards={c['paper']:c for c in atlas['curated']}
    chapters={c['id']:c for c in atlas['chapters']}
    groups={g['id']:g for g in mapping['groups']}
    placements={p['paper']:p for p in organization['placements']}
    tracks=organization['tracks']
    assert set(BRIEFS)==set(cards), 'Every curated entry needs a reviewed compact introduction'
    home=['<div align="center">','', '<p><strong>awesome-robot-world-model</strong></p>',
          '<h1>From Prediction to Control</h1>', '<p><strong>An Atlas of Robot World Models</strong></p>', '',
          '<p>What does a model predict — and how does that prediction change a robot’s decisions?</p>', '',
          '<p><a href="docs/paper-index.md">Find a paper</a> · <a href="docs/paper-map.md">Follow the survey</a> · <a href="docs/methods.md">Read the annotations</a> · <a href="docs/resources.md">Find a resource</a></p>', '',
          '<picture>',
          '  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/loop-mobile-dark.svg">',
          '  <source media="(max-width: 600px)" srcset="assets/loop-mobile-light.svg">',
          '  <source media="(prefers-color-scheme: dark)" srcset="assets/loop-dark.svg">',
          '  <img src="assets/loop-light.svg" width="100%" alt="Observe, predict, improve a policy or choose an action, then execute. Feedback can return to different parts of the robot learning loop.">',
          '</picture>', '',
          '</div>', '',
          'A companion to **'+atlas['companion_to']+'**. The Atlas follows the paper’s central question: '
          'how do predictive models improve robot learning, control and evaluation? Browse by the problem you are solving; use the paper map to recover the original argument.', '',
          '## Start here', '',
          '| Your question | Reading route |', '|---|---|',
          '| What makes a prediction useful for a robot? | [The Prediction-to-Control Gap](docs/scope-and-taxonomy.md) → [six model roles](docs/roles.md) |',
          '| Which system should I read for my task? | [Annotated entries below](#the-atlas) → [interfaces and evidence boundaries](docs/methods.md) |',
          '| Where is a particular paper or citation key? | [Complete paper index](docs/paper-index.md) · [bibliographic catalog](docs/catalog.md) |',
          '| What can I use to train or evaluate? | [Datasets, environments and implementations](docs/resources.md) → [evaluation worksheet](docs/evaluation.md) |', '',
          '<details>', '<summary><strong>How to follow the argument</strong> · from a predicted future to useful feedback</summary>', '', '<br>', '',
          'The survey begins with a practical gap: a model can predict plausible futures while providing little help to the robot’s next decision. '
          'The Atlas therefore follows the handoffs between components. First identify the information state and the alternative actions the model can query. '
          'Then locate the consumer that turns those predictions into an action, learning target, evaluation or intervention. '
          'Finally trace real execution back to the next decision or update and ask what evidence supports that connection.', '',
          '| Handoff | Question and next reading |', '|---|---|',
          '| Observation → state | Which task information is retained, hidden or discarded?<br>[Representations](#track-representations) · [Touch](#track-tactile) |',
          '| State + action → consequence | Are alternative executable actions associated with different task-relevant outcomes?<br>[Foundations](#track-foundations) · [Embodiment](#track-embodiment) |',
          '| Consequence → consumer | Does a planner choose an action, a learner update a policy, or an evaluator assess behavior?<br>[Learning and control](#track-learning-control) · [Simulation](#track-simulation) |',
          '| Execution → returned information | Does feedback update context, actions, memory, policy or model parameters?<br>[Interaction](#track-interaction) |',
          '| Claimed use → evidence | Which comparison separates prediction quality, policy effect and deployment reliability?<br>[Evaluation](#track-evaluation) · [Resources](#track-resources) |', '',
          'These handoffs branch. Dreamer’s imagination can improve a policy during learning; PlaNet’s imagined trajectories can select an action through planning. '
          'Generated video can supply demonstrations, filtered behavior-cloning data, RL experience or policy-evaluation observations. '
          'The relevant question is which branch is implemented and tested. The sections below unfold those branches with concrete paper comparisons.', '',
          '[Read the complete argument as a continuous guide →](docs/reading-paths.md)', '', '</details>', '',
          '## The Atlas', '',
          'The reading order moves from foundations to prediction, downstream use, physical grounding and returned feedback. '
          'Each entry has one home here and can appear in several [functional roles](docs/roles.md). '
          '**Predictive use**, **policy context**, **representation prior**, **generative context** and **benchmark** are different entry kinds. '
          'Neither citation presence nor the “predictive use” label automatically establishes strict closed-loop qualification. '
          'Expand each argument to follow the reading chain, compare mechanisms and identify the evidence needed. '
          'The entry table provides quick lookup; its linked method cards retain each interface, consumer and execution boundary.', '',
          ' · '.join(f"[{i+1:02d} {t['title'].split(' and ')[0]}](#track-{t['id']})" for i,t in enumerate(tracks)), '']
    for i,t in enumerate(tracks):
        home += [f'<a id="track-{t["id"]}"></a>', '', f"### {i+1:02d} · {t['title']}", '', t['purpose'], '']
        home += ['<details>', f"<summary><strong>Unfold the argument</strong> · {html.escape(t['logic']['summary'])}</summary>", '', '<br>', '']
        home += argument_blocks(t,chapters)
        home += ['</details>', '']
        selected=[c for c in atlas['curated'] if placements[c['paper']]['track']==t['id']]
        if selected:
            home += ['| Entry | Read for |', '|---|---|']
            for c in selected:
                p=papers[c['paper']]
                home.append(f"| [{text(c['name'])}](docs/methods.md#{anchor(c['paper'])}) · {p['year'] or '?'}<br><sub>{KIND[c['kind']]}</sub> | {BRIEFS[c['paper']]} |")
            home+=['']
        n=sum(p['track']==t['id'] for p in placements.values())
        home += [f"[Browse all {n} cited works in this route →](docs/paper-index.md#track-{t['id']})", '']
    home += ['## Follow the paper', '',
             'The complete paper map links every citation-bearing argument group. It preserves multiple uses of the same work, '
             'while the main index uses the clearer reading routes above.', '',
             '[Open the paper map →](docs/paper-map.md)', '', '<details>', '<summary><strong>All paper sections</strong></summary>', '',
             '| Section | Guide |', '|---|---|']
    home += [f"| {c['number']} | [{c['title']}]({chapter_path(c)}) |" for c in atlas['chapters']]
    home += ['', '</details>', '', '## Read the evidence with the interface', '',
             'Latent imagination can train an actor without deployment-time planning. Video generation can supply demonstrations without online RL. '
             'A planner can select a trajectory that is later executed open-loop. Tactile feedback can correct an action without updating model weights. '
             'The [method cards](docs/methods.md) keep these distinctions visible.', '',
             '[Scope and taxonomy](docs/scope-and-taxonomy.md) · [Reading paths](docs/reading-paths.md) · [Evaluation](docs/evaluation.md)', '',
             '## Contribute', '',
             'Correct an identity, clarify a mechanism or add a resource cited by the companion survey. '
             'Keep the predictive interface, downstream consumer and evidence boundary together. See [contributing](CONTRIBUTING.md).', '',
             '[Catalog JSON](data/catalog.json) · [Reading-route JSON](data/organization.json) · [Citation map](data/citation-map.json) · [CSV](data/catalog.csv) · [BibTeX](data/references.bib)', '',
             '<details>', '<summary><strong>Snapshot, verification and design references</strong></summary>', '',
             f"Manuscript snapshot: **{atlas['snapshot']}**. Organization and presentation reviewed: **{organization['reviewed_at']}**. "
             'The catalog includes contextual literature. Primary bibliographic checks do not constitute scientific replication; some source records lack an extracted paper URL.', '',
             '[Verification coverage](docs/provenance.md) · [Five layout references and Apple guidance](docs/design-notes.md)', '',
             'Linked papers, datasets and code retain their authorship and upstream licenses. No full papers or private manuscript paragraphs are redistributed.', '', '</details>', '']
    result={'README.md':'\n'.join(home)}
    guide=['# From prediction to control: the reading argument', '',
           '[Home](../README.md) · [Method cards](methods.md) · [Source argument map](paper-map.md)', '',
           'This guide explains why the Atlas moves from foundations and representations to downstream use, physical grounding, evaluation and returned experience. '
           'The sequences below are comparative reading suggestions grounded in the companion survey. They are not a genealogy of methods or a performance ranking.', '',
           'Read a system through five connected questions: what information is available, what consequence is predicted, which consumer uses it, '
           'what execution feedback changes, and which evidence supports the claimed benefit. '
           'When following a method link, keep its interface, changed object and reported execution boundary together.', '',
           ' · '.join(f"[{i+1:02d} {t['title']}](#track-{t['id']})" for i,t in enumerate(tracks)), '']
    for i,t in enumerate(tracks):
        guide += [f'<a id="track-{t["id"]}"></a>', '', f"## {i+1:02d}. {t['title']}", '', t['purpose'], '']
        guide += argument_blocks(t,chapters,in_docs=True)
        guide += [f"[Browse this route’s cited works →](paper-index.md#track-{t['id']})", '']
    result['docs/reading-paths.md']='\n'.join(guide)
    index=['# Find a paper', '', '[Home](../README.md) · [Paper map](paper-map.md) · [Bibliographic records](catalog.md)', '',
           f"All **{len(papers)}** deduplicated works cited in the manuscript, organized into **{len(tracks)}** reading routes. "
           'Use your browser’s Find command for a title, system name or canonical key. Citation aliases are searchable in the bibliographic catalog and JSON. '
           'Routes are editorial navigation, not strict inclusion judgments. A work appears once here; its catalog and chapter links preserve all uses.', '',
           ' · '.join(f"[{t['title']}](#track-{t['id']})" for t in tracks), '']
    for t in tracks:
        entries=[p for p in organization['placements'] if p['track']==t['id']]
        index += [f'<a id="track-{t["id"]}"></a>', '', f"## {t['title']} ({len(entries)})", '', t['purpose'], '',
                  '| Year | Work and cited argument |', '|---|---|']
        # Reading routes govern the order; neighboring source arguments supply a stable secondary order.
        for placement in sorted(entries,key=lambda x:(int(x['context_group'].split('-')[-1]),groups[x['context_group']]['papers'].index(x['paper']))):
            p=papers[placement['paper']];g=groups[placement['context_group']];c=chapters[g['chapter']]
            name=cards[p['id']]['name']+' — ' if p['id'] in cards else ''
            title=name+p['title']
            index += [f"| {p['year'] or '?'} | <a id=\"entry-{p['id']}\"></a>[{text(title)}](catalog.md#{anchor(p['id'])})<br><sub><code>{p['id']}</code> · [Cited argument](chapters/{chapter_path(c).split('/')[-1]}#{g['id']})</sub> |"]
        index+=['']
    result['docs/paper-index.md']='\n'.join(index)
    paper_map=['# Follow the survey’s argument', '', '[Home](../README.md) · [Find a paper by topic](paper-index.md)', '',
               'Start with the gap between prediction and decision utility, then identify the modeled state, predictive interface, downstream use and returned feedback. '
               'This map follows the paper’s chapters and citation-bearing subsections. It complements the more flexible reading routes in the main index.', '',
               f"**{len(mapping['groups'])} argument groups · {len(mapping['occurrences'])} citation commands · {len(papers)} deduplicated works**", '']
    for c in atlas['chapters']:
        paper_map += [f"## {c['number']}. {c['title']}", '', c['summary'], '']
        gs=[g for g in mapping['groups'] if g['chapter']==c['id']]
        for g in gs:
            label=' › '.join(g['heading_path']) or 'Section opening'
            paper_map += [f"- [{text(label)}](chapters/{chapter_path(c).split('/')[-1]}#{g['id']}) — {len(g['papers'])} works"]
        if not gs:paper_map+=['This section closes the argument and has no active citations.']
        paper_map+=['']
    result['docs/paper-map.md']='\n'.join(paper_map)
    return result
