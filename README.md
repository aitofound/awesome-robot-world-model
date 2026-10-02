<div align="center">

<p><strong>awesome-robot-world-model</strong></p>
<h1>From Prediction to Control</h1>
<p><strong>An Atlas of Robot World Models</strong></p>

<p>What does a model predict — and how does that prediction change a robot’s decisions?</p>

<p><a href="docs/paper-index.md">Find a paper</a> · <a href="docs/paper-map.md">Follow the survey</a> · <a href="docs/methods.md">Read the annotations</a> · <a href="docs/resources.md">Find a resource</a></p>

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/loop-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/loop-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/loop-dark.svg">
  <img src="assets/loop-light.svg" width="100%" alt="Observe, predict, improve a policy or choose an action, then execute. Feedback can return to different parts of the robot learning loop.">
</picture>

</div>

A companion to **From Prediction to Control: A Survey of Closed-Loop World Models for Robot Learning**. The Atlas follows the paper’s central question: how do predictive models improve robot learning, control and evaluation? Browse by the problem you are solving; use the paper map to recover the original argument.

## Start here

| Your question | Reading route |
|---|---|
| What makes a prediction useful for a robot? | [The Prediction-to-Control Gap](docs/scope-and-taxonomy.md) → [six model roles](docs/roles.md) |
| Which system should I read for my task? | [Annotated entries below](#the-atlas) → [interfaces and evidence boundaries](docs/methods.md) |
| Where is a particular paper or citation key? | [Complete paper index](docs/paper-index.md) · [bibliographic catalog](docs/catalog.md) |
| What can I use to train or evaluate? | [Datasets, environments and implementations](docs/resources.md) → [evaluation worksheet](docs/evaluation.md) |

<details>
<summary><strong>How to follow the argument</strong> · from a predicted future to useful feedback</summary>

<br>

The survey begins with a practical gap: a model can predict plausible futures while providing little help to the robot’s next decision. The Atlas therefore follows the handoffs between components. First identify the information state and the alternative actions the model can query. Then locate the consumer that turns those predictions into an action, learning target, evaluation or intervention. Finally trace real execution back to the next decision or update and ask what evidence supports that connection.

| Handoff | Question and next reading |
|---|---|
| Observation → state | Which task information is retained, hidden or discarded?<br>[Representations](#track-representations) · [Touch](#track-tactile) |
| State + action → consequence | Are alternative executable actions associated with different task-relevant outcomes?<br>[Foundations](#track-foundations) · [Embodiment](#track-embodiment) |
| Consequence → consumer | Does a planner choose an action, a learner update a policy, or an evaluator assess behavior?<br>[Learning and control](#track-learning-control) · [Simulation](#track-simulation) |
| Execution → returned information | Does feedback update context, actions, memory, policy or model parameters?<br>[Interaction](#track-interaction) |
| Claimed use → evidence | Which comparison separates prediction quality, policy effect and deployment reliability?<br>[Evaluation](#track-evaluation) · [Resources](#track-resources) |

These handoffs branch. Dreamer’s imagination can improve a policy during learning; PlaNet’s imagined trajectories can select an action through planning. Generated video can supply demonstrations, filtered behavior-cloning data, RL experience or policy-evaluation observations. The relevant question is which branch is implemented and tested. The sections below unfold those branches with concrete paper comparisons.

[Read the complete argument as a continuous guide →](docs/reading-paths.md)

</details>

## The Atlas

The reading order moves from foundations to prediction, downstream use, physical grounding and returned feedback. Each entry has one home here and can appear in several [functional roles](docs/roles.md). **Predictive use**, **policy context**, **representation prior**, **generative context** and **benchmark** are different entry kinds. Neither citation presence nor the “predictive use” label automatically establishes strict closed-loop qualification. Expand each argument to follow the reading chain, compare mechanisms and identify the evidence needed. The entry table provides quick lookup; its linked method cards retain each interface, consumer and execution boundary.

[01 Foundations](#track-foundations) · [02 Representations](#track-representations) · [03 Policy learning](#track-learning-control) · [04 Foundation priors, simulation](#track-simulation) · [05 Touch](#track-tactile) · [06 Human video](#track-human-data) · [07 Embodiments](#track-embodiment) · [08 Evaluation, reliability](#track-evaluation) · [09 Datasets, environments](#track-resources) · [10 Interaction](#track-interaction) · [11 Open problems](#track-frontiers)

<a id="track-foundations"></a>

### 01 · Foundations and the Prediction-to-Control Gap

Define the model’s downstream use and distinguish predictive quality from decision utility.

<details>
<summary><strong>Unfold the argument</strong> · From a predicted future to a decision that changes</summary>

<br>

**The question.** What has to happen between predicting the world and improving a robot’s behavior?

**Reading chain**

1. **Recover the information state.** Start from observations and action history. A compact latent state is useful when it retains the consequences relevant to the task, even if it cannot reconstruct every visible detail.
2. **Ask a counterfactual question.** Hold the history fixed and change a feasible action. The prediction should change the affected objects, contacts or outcomes while preserving unrelated parts of the scene.
3. **Name the consumer.** Identify the planner, actor learner, demonstration learner, evaluator or monitor that receives the output. Explain which action, target or parameter that consumer changes.
4. **Locate the return path.** Follow execution back to the next decision or learning round. Refreshing observations, correcting an action and refitting dynamics close different parts of the loop.

**Why begin with World Models?**

[World Models](docs/methods.md#paper-ha2018worldmodels) makes the representation–dynamics–controller relationship easy to inspect. Its place here is conceptual: the early control setting explains how a learned state can support behavior, while the robot-specific sensing and deployment requirements arrive later. This gives the reader a vocabulary for asking what the prediction contributes before comparing larger architectures.

**The first useful fork**

Read [PlaNet](docs/methods.md#paper-hafner2019planet) beside [Dreamer](docs/methods.md#paper-hafner2019dreamer). PlaNet uses imagined futures to select actions through planning. Dreamer uses imagined trajectories to train an actor and value model. The two systems illustrate distinct consumers of predictive dynamics, so a single “world-model-based control” label would hide the most useful comparison.

**What would establish usefulness?**

The central test is downstream usefulness under the stated task and budget. Low prediction error or plausible video is relevant only insofar as it preserves the consequences used by the consumer. Keep the [operational criterion](docs/scope-and-taxonomy.md) beside the [six functional roles](docs/roles.md): a role identifies a use, while strict closed-loop qualification also needs action-responsive prediction, implemented coupling and execution evidence.

**Where the argument goes next.** Continue to [representations](#track-representations) to ask what information the model preserves, then to [policy learning and planning](#track-learning-control) to examine the consumer.

**Survey connections:** [01. Introduction](docs/chapters/01-introduction.md) · [03. A Robot Learning Loop View of World Models](docs/chapters/03-foundations.md) · [04. The Optimizable Roles of World Models](docs/chapters/04-roles.md).

</details>

| Entry | Read for |
|---|---|
| [World Models](docs/methods.md#paper-ha2018worldmodels) · 2018<br><sub>Predictive use</sub> | A compact starting point for learned latent environments. |

[Browse all 27 cited works in this route →](docs/paper-index.md#track-foundations)

<a id="track-representations"></a>

### 02 · Representations and predictive mechanics

Choose a state substrate, action interface and rollout mechanism that preserve task-relevant consequences.

<details>
<summary><strong>Unfold the argument</strong> · From a state substrate to a usable predictive interface</summary>

<br>

**The question.** Which representation preserves the action consequences that the next decision needs?

**Reading chain**

1. **Choose the task state.** Compare pixels, visual features, object or point states, contact variables and physical parameters by the information they retain. A visually rich state can still omit the friction or contact event that determines success.
2. **Specify the query.** Write down the conditioning variables and the predicted quantity. Observation-and-goal conditioning, action-chunk conditioning and a query under an alternative control are different interfaces.
3. **Separate substrate from mechanics.** The state representation answers what is modeled. Recurrent dynamics, autoregression, diffusion, flow and physical-time ODEs answer how prediction is computed. A method can combine more than one of these axes.
4. **Connect the representation to a consumer.** Explain how a feature distance, point trajectory or simulated physical state becomes a planning objective or learning signal. Then check the executed controller rather than stopping at the representation benchmark.

**Predictive features versus action grounding**

[DINO-WM](docs/methods.md#paper-zhou2025dinowm) connects pretrained visual features to action-conditioned prediction and planning. [V-JEPA 2](docs/methods.md#paper-assran2025vjepa2) should be read as video pretraining followed by a distinct action-conditioned robot adaptation. [ACT-JEPA](docs/methods.md#paper-actjepa2025) supplies predictive representation and policy-learning context. These papers belong together because they ask how learned features become useful, but the presence of a predictive embedding objective does not make every entry an online action-search system.

**Geometry, physics and temporal queries**

[PointWorld](docs/methods.md#paper-pointworld2026) exposes 3D action consequences to MPPI, while [PhysTwin](docs/methods.md#paper-jiang2025phystwin) reconstructs structured deformable physics from video. [ODEWorld](docs/methods.md#paper-liu2026odeworld) queries observation- and goal-conditioned futures in physical time; its reviewed interface does not accept queried candidate actions. [Causal-JEPA](docs/methods.md#paper-nam2026causaljepa) provides object-aware predictive dependencies, which are not by themselves an identified causal graph. These distinctions prevent an architecture name from substituting for an interface description.

**What would establish usefulness?**

Ask whether the representation preserves task-relevant geometry, occlusion, contact and action sensitivity over the consumer’s horizon. Measure the entire decision pipeline when a planner is used. PointWorld’s reported physical execution remains open loop, so its predictive representation and planning evidence must not be upgraded into a claim of online hardware correction.

**Where the argument goes next.** Use [learning and control](#track-learning-control) to trace the chosen interface into action selection. For hidden contact state, follow [touch and contact](#track-tactile).

**Survey connections:** [05. Representation Substrates and World-Model Mechanics](docs/chapters/05-representations.md) · [06. From Roles to Policy Improvement](docs/chapters/06-learning-regimes.md) · [10. Embodiment and Task Perspective](docs/chapters/10-embodiments.md).

</details>

| Entry | Read for |
|---|---|
| [DINO-WM](docs/methods.md#paper-zhou2025dinowm) · 2025<br><sub>Predictive use</sub> | Predict frozen visual features for goal-directed planning. |
| [V-JEPA 2](docs/methods.md#paper-assran2025vjepa2) · 2025<br><sub>Predictive use</sub> | Separate video pretraining from action-grounded V-JEPA 2-AC. |
| [ACT-JEPA](docs/methods.md#paper-actjepa2025) · 2025<br><sub>Representation prior</sub> | Predictive representations and action-chunk learning. |
| [Causal-JEPA](docs/methods.md#paper-nam2026causaljepa) · 2026<br><sub>Representation prior</sub> | Object-level predictive dependencies; retain identifiability limits. |
| [ODEWorld](docs/methods.md#paper-liu2026odeworld) · 2026<br><sub>Generative context</sub> | Continuous latent prediction conditioned on observation and goal. |
| [PointWorld](docs/methods.md#paper-pointworld2026) · 2026<br><sub>Predictive use</sub> | Scene point-flow prediction and MPPI; hardware execution is open-loop. |
| [PhysTwin](docs/methods.md#paper-jiang2025phystwin) · 2025<br><sub>Predictive use</sub> | Build deformable physical twins from sparse videos. |

[Browse all 73 cited works in this route →](docs/paper-index.md#track-representations)

<a id="track-learning-control"></a>

### 03 · Policy learning and planning

Separate actor learning through imagination from action selection through search or control.

<details>
<summary><strong>Unfold the argument</strong> · Two consumers: improve a policy or select the next action</summary>

<br>

**The question.** Does the model change policy parameters during learning, or action choices during execution?

**Reading chain**

1. **Identify the learning signal.** Determine whether predictions supply imagined transitions, demonstrations, rewards, value targets or a planning cost. The same transition model can support several learning regimes.
2. **Trace the update.** For an imagination learner, follow generated trajectories into actor and value updates. For a planner, follow candidate actions into predicted consequences, scoring and selection.
3. **Inspect deployment separately.** Check whether the deployed policy calls the model, whether a planner replans after new observations, and whether an action chunk is executed in full. Training-time model use does not specify deployment-time computation.
4. **Close the appropriate loop.** Record real data collection, model fitting, policy fitting and action correction as separate events. Their update rates and their dependence on fresh physical experience can differ.

**PlaNet, Dreamer and the physical learning loop**

[PlaNet](docs/methods.md#paper-hafner2019planet) is the planning reference: latent rollouts guide action selection. [Dreamer](docs/methods.md#paper-hafner2019dreamer), [DreamerV2](docs/methods.md#paper-hafner2021dreamerv2) and [DreamerV3](docs/methods.md#paper-hafner2023dreamerv3) form an imagined policy-learning route. [DayDreamer](docs/methods.md#paper-wu2022daydreamer) brings that discussion to physical data collection and learning. Reading them together reveals where robot experience enters the learner, rather than implying that every deployed actor executes a rollout planner.

**Search, value and executable motion**

[TD-MPC2](docs/methods.md#paper-hansen2024tdmpc2) combines latent prediction and value estimates with model-predictive action selection. [WorldPlanner](docs/methods.md#paper-worldplanner2025) connects global tree search to local MPC. [Large Video Planner](docs/methods.md#paper-chen2025largevideoplanner) instead turns visual plans into executable motion through retargeting, followed by open-loop execution in the reviewed evidence. [RoboDreamer](docs/methods.md#paper-robodreamer2024) illustrates compositional task imagination. These interfaces should be compared at the handoff from prediction to an executable decision.

**What would establish usefulness?**

Match real interaction, policy capacity and compute when assessing policy improvement. For planning, report candidate count, horizon, scoring, replanning cadence and full latency. For imagination learning, separate real and synthetic transitions and inspect performance under the learned policy’s query distribution. A success rate without these conditions does not establish which consumer benefited.

**Where the argument goes next.** Follow [neural simulation](#track-simulation) when generated experience becomes reusable training data. Follow [interaction](#track-interaction) when real deployment changes the next learning round.

**Survey connections:** [04. The Optimizable Roles of World Models](docs/chapters/04-roles.md) · [06. From Roles to Policy Improvement](docs/chapters/06-learning-regimes.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

| Entry | Read for |
|---|---|
| [PlaNet](docs/methods.md#paper-hafner2019planet) · 2019<br><sub>Predictive use</sub> | Plan candidate actions with latent dynamics and CEM. |
| [Dreamer](docs/methods.md#paper-hafner2019dreamer) · 2020<br><sub>Predictive use</sub> | Learn an actor and value model through latent imagination. |
| [DreamerV2](docs/methods.md#paper-hafner2021dreamerv2) · 2021<br><sub>Predictive use</sub> | Discrete latent dynamics for imagined policy learning. |
| [DreamerV3](docs/methods.md#paper-hafner2023dreamerv3) · 2023<br><sub>Predictive use</sub> | A shared world-model agent configuration across domains. |
| [Dreamer4](docs/methods.md#paper-hafner2025dreamer4) · 2025<br><sub>Predictive use</sub> | Scale agent training inside learned worlds. |
| [DayDreamer](docs/methods.md#paper-wu2022daydreamer) · 2022<br><sub>Predictive use</sub> | Connect latent imagination to physical robot learning. |
| [TD-MPC2](docs/methods.md#paper-hansen2024tdmpc2) · 2024<br><sub>Predictive use</sub> | Combine latent planning with scalable continuous control. |
| [WorldPlanner](docs/methods.md#paper-worldplanner2025) · 2025<br><sub>Predictive use</sub> | Action-conditioned visual prediction for MCTS and MPC. |
| [Large Video Planner](docs/methods.md#paper-chen2025largevideoplanner) · 2025<br><sub>Predictive use</sub> | Video prediction for long-horizon plans; retain execution limits. |

[Browse all 40 cited works in this route →](docs/paper-index.md#track-learning-control)

<a id="track-simulation"></a>

### 04 · Foundation priors, simulation and generated experience

Distinguish general priors, interactive neural environments and pipelines that generate training data.

<details>
<summary><strong>Unfold the argument</strong> · From a pretrained prior to interaction, supervision or evaluation</summary>

<br>

**The question.** What makes generated experience usable by a robot policy, and which learning rule consumes it?

**Reading chain**

1. **Adapt the prior.** Start from the pretrained representation or video prior, then locate robot action grounding, observation compatibility and task conditioning. A broad visual prior is not yet an executable robot environment.
2. **Define the experience interface.** For interaction, a policy or human chooses an action and receives the predicted next observation before choosing again. Initial contexts, resets and the actor’s required modalities are part of that interface.
3. **Choose a downstream branch.** Demonstration collection, filtered supervised learning, imagined policy optimization and policy evaluation consume experience differently. Rewards and termination may come from external modules rather than the transition predictor.
4. **Return to independent physical evidence.** Train or assess the consumer, then check its physical outcomes. If new real rollouts refit the model, show that additional return path explicitly; it is not a mandatory component of every neural simulator.

**Three ways to learn from generated experience**

[IWS](docs/methods.md#paper-interactiveworldsim2026) turns simulator interaction into demonstration-based learning, while [Hi-WM](docs/methods.md#paper-li2026hiwm) uses rollback and branching for targeted human correction. [GE-Sim 2.0](docs/methods.md#paper-qiu2026gesim2) filters generated rollouts for behavior-cloning updates. [DreamGen](docs/methods.md#paper-jang2025dreamgen) recovers pseudo-actions so generated video can supply demonstrations. [RWM](docs/methods.md#paper-li2025roboticworldmodel), [WoVR](docs/methods.md#paper-nsim-wovr) and [WorldGymnast](docs/methods.md#paper-worldgymnast2026) belong on the policy-optimization branch. The presence of synthetic trajectories cannot decide which branch a paper implements.

**Where foundation priors and evaluators fit**

[Cosmos](docs/methods.md#paper-nvidia2025cosmos) and [Genie](docs/methods.md#paper-bruce2024genie) provide generative context. [DreamDojo](docs/methods.md#paper-gao2026dreamdojo) moves from human-video interaction priors toward robot grounding; [GeniWorld](docs/methods.md#paper-gu2026geniworld) grounds conditions through rendered robot actions. [RoboWorld](docs/methods.md#paper-nsim-roboworld) and [WorldEval](docs/methods.md#paper-li2025worldeval) ask whether predicted outcomes can evaluate policies. Evaluation can be useful without a policy update, so its evidence should be read separately from training gains.

**What would establish usefulness?**

For generated demonstrations, include adaptation, generation, filtering, labeling and rejected samples in the cost. For policy optimization, test independent physical performance and the actions favored by the learned policy. For evaluation, measure held-out policy ranking and absolute outcome calibration separately. Matching the final training-set size, as in an IWS comparison, does not by itself match the cost of constructing the world model.

**Where the argument goes next.** Use [resources](#track-resources) to check whether a released artifact exposes the required interface. Continue to [evaluation](#track-evaluation) for the evidence contract or [interaction](#track-interaction) for real–synthetic updates.

**Survey connections:** [07. Foundation-Driven World Models and Robot Priors](docs/chapters/07-foundation-priors.md) · [06. From Roles to Policy Improvement](docs/chapters/06-learning-regimes.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

| Entry | Read for |
|---|---|
| [RoboDreamer](docs/methods.md#paper-robodreamer2024) · 2024<br><sub>Predictive use</sub> | Instruction-conditioned, compositional imagined futures. |
| [Robotic World Model (RWM)](docs/methods.md#paper-li2025roboticworldmodel) · 2025<br><sub>Predictive use</sub> | A learned neural simulator for policy optimization. |
| [Interactive World Simulator (IWS)](docs/methods.md#paper-interactiveworldsim2026) · 2026<br><sub>Predictive use</sub> | Interactive demonstration generation and policy evaluation. |
| [Hi-WM](docs/methods.md#paper-li2026hiwm) · 2026<br><sub>Predictive use</sub> | Human correction through simulator rollback and branching. |
| [GE-Sim 2.0](docs/methods.md#paper-qiu2026gesim2) · 2026<br><sub>Predictive use</sub> | Filter generated rollouts for supervised policy updates. |
| [GeniWorld](docs/methods.md#paper-gu2026geniworld) · 2026<br><sub>Predictive use</sub> | Ground interactive video prediction in rendered robot actions. |
| [DreamGen](docs/methods.md#paper-jang2025dreamgen) · 2025<br><sub>Predictive use</sub> | Recover synthetic robot trajectories from generated videos. |
| [DreamDojo](docs/methods.md#paper-gao2026dreamdojo) · 2026<br><sub>Predictive use</sub> | Human-video interaction priors followed by robot grounding. |
| [WoVR](docs/methods.md#paper-nsim-wovr) · 2026<br><sub>Predictive use</sub> | Use action-conditioned simulation to post-train VLA policies. |
| [Cosmos](docs/methods.md#paper-nvidia2025cosmos) · 2025<br><sub>Generative context</sub> | Pretrained world-model components and generative priors. |
| [Cosmos 3](docs/methods.md#paper-nvidia2026cosmos3) · 2026<br><sub>Generative context</sub> | Shared multimodal understanding, prediction and action interfaces. |
| [Genie](docs/methods.md#paper-bruce2024genie) · 2024<br><sub>Generative context</sub> | Latent-action interactive environments from passive video. |
| [Gen2Act](docs/methods.md#paper-bharadhwaj2025gen2act) · 2025<br><sub>Predictive use</sub> | Condition robot behavior on generated human task motion. |
| [Dreamitate](docs/methods.md#paper-liang2025dreamitate) · 2025<br><sub>Predictive use</sub> | Convert generated task motion into robot behavior. |
| [OpenVLA](docs/methods.md#paper-openvla2024) · 2024<br><sub>Policy context</sub> | An open VLA action prior and policy baseline. |
| [pi0](docs/methods.md#paper-pi0) · 2024<br><sub>Policy context</sub> | A foundation policy with flow-matching action generation. |
| [GR00T N1.7](docs/methods.md#paper-nvidia2026groot17) · 2026<br><sub>Policy context</sub> | A reasoning VLA with an action-cascade interface. |

[Browse all 77 cited works in this route →](docs/paper-index.md#track-simulation)

<a id="track-tactile"></a>

### 05 · Touch and contact

Connect hidden contact state to predictive control, corrective action and multisensory learning.

<details>
<summary><strong>Unfold the argument</strong> · From hidden contact to prediction, correction and retained competence</summary>

<br>

**The question.** What does touch reveal that vision misses, and how does that information change control?

**Reading chain**

1. **Recover local interaction state.** Contact, slip, compliance and occluded deformation can remain ambiguous in camera observations. Tactile or force history supplies evidence about the local interaction rather than just another visual view.
2. **Predict a contact consequence.** Condition on the robot’s action and predict tactile images, latent contact state or deformation. Distinguish predicting the future from supplying current touch directly to an action policy.
3. **Deliver the prediction in time.** A planner, compliance controller or corrective module must consume the forecast before the relevant failure. State the contact horizon and the rate of correction, not only the video-generation rate.
4. **Transfer and retain.** When visual priors initialize touch modeling, identify the shared encoder and the modality-specific adaptation. Test both the new contact behavior and the predictive or control competence retained from earlier modalities.

**Prediction, planning and correction**

[Manipulation by Feel](docs/methods.md#paper-tian2019manipulation) uses predicted tactile images as a servoing objective. [RoboPack](docs/methods.md#paper-ai2024robopack) uses vision and touch to infer physical state for planning, while [VIRDO++](docs/methods.md#paper-wi2022virdopp) models deformable state. [Visuo-Tactile World Models](docs/methods.md#paper-visuotactilewm2026) and [OmniVTA](docs/methods.md#paper-omnivta2026) connect contact prediction to different consumers: the former retains an open-loop physical planning boundary, while the latter includes execution-time corrective feedback. This is why “uses touch” is too broad a grouping by itself.

**A sensing prior is not the predictive loop**

[Sparsh](docs/methods.md#paper-higuera2024sparsh) and [AnyTouch](docs/methods.md#paper-feng2025anytouch) provide reusable tactile representations. [OmniVTLA](docs/methods.md#paper-cheng2025omnivtla) supplies touch-conditioned policy context and is distinct from OmniVTA. [DexTacWAM](docs/methods.md#paper-yuan2026dextacwam), [VTAM](docs/methods.md#paper-yuan2026vtam), [Dream-Tac](docs/methods.md#paper-lou2026dreamtac) and [Tactile-WAM](docs/methods.md#paper-wu2026tactilewam) motivate a further comparison: where visual priors are reused, how touch affects prediction and action, and which pathways are allowed to adapt. [MuSe](docs/methods.md#paper-clark2026muse) adds the retention question when sensing expands.

**What would establish usefulness?**

Compare predictive touch with direct tactile conditioning under matched sensors, data and policy capacity. Check contact-sensitive errors, downstream control and full decision latency. A separated or aligned latent space alone cannot establish utility. Vision-to-touch retention should be measured on earlier behavior as well as the newly acquired sensing task, within the actual sensor and robot scope.

**Where the argument goes next.** Follow [human data](#track-human-data) for the asymmetry between abundant video and scarce robot contact data. Follow [interaction](#track-interaction) for modality expansion, replay and retained behavior.

**Survey connections:** [08. Tactile and Contact World Models](docs/chapters/08-tactile-contact.md) · [05. Representation Substrates and World-Model Mechanics](docs/chapters/05-representations.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

| Entry | Read for |
|---|---|
| [Manipulation by Feel](docs/methods.md#paper-tian2019manipulation) · 2019<br><sub>Predictive use</sub> | Predict tactile images to servo toward a contact goal. |
| [RoboPack](docs/methods.md#paper-ai2024robopack) · 2024<br><sub>Predictive use</sub> | Infer physical state from vision and touch for planning. |
| [VIRDO++](docs/methods.md#paper-wi2022virdopp) · 2022<br><sub>Predictive use</sub> | Predict deformable state from vision, contact and force. |
| [ContactWorld](docs/methods.md#paper-zhang2026contactworld) · 2026<br><sub>Predictive use</sub> | Study which visual-tactile representations help prediction. |
| [OmniVTA](docs/methods.md#paper-omnivta2026) · 2026<br><sub>Predictive use</sub> | Use tactile forecasts and feedback for execution-time correction. |
| [Visuo-Tactile World Models](docs/methods.md#paper-visuotactilewm2026) · 2026<br><sub>Predictive use</sub> | Visual-tactile latent dynamics and open-loop physical planning. |
| [DexTacWAM](docs/methods.md#paper-yuan2026dextacwam) · 2026<br><sub>Predictive use</sub> | Transfer video priors into dexterous tactile world-action modeling. |
| [VTAM](docs/methods.md#paper-yuan2026vtam) · 2026<br><sub>Predictive use</sub> | Joint video, tactile and action modeling. |
| [VT-WAM](docs/methods.md#paper-tian2026vtwam) · 2026<br><sub>Predictive use</sub> | Route contact information into world-action prediction. |
| [Dream-Tac](docs/methods.md#paper-lou2026dreamtac) · 2026<br><sub>Predictive use</sub> | Joint future vision, touch and action with contact-aware fusion. |
| [Tactile-WAM](docs/methods.md#paper-wu2026tactilewam) · 2026<br><sub>Predictive use</sub> | Asymmetric tactile attention for world-action modeling. |
| [Sparsh](docs/methods.md#paper-higuera2024sparsh) · 2024<br><sub>Representation prior</sub> | Reusable self-supervised tactile features. |
| [AnyTouch](docs/methods.md#paper-feng2025anytouch) · 2025<br><sub>Representation prior</sub> | Static and dynamic tactile representations across sensors. |
| [OmniVTLA](docs/methods.md#paper-cheng2025omnivtla) · 2025<br><sub>Policy context</sub> | Tactile-conditioned VLA policy context, distinct from OmniVTA. |
| [MuSe](docs/methods.md#paper-clark2026muse) · 2026<br><sub>Policy context</sub> | Add force sensing while testing retention of earlier behavior. |

[Browse all 59 cited works in this route →](docs/paper-index.md#track-tactile)

<a id="track-human-data"></a>

### 06 · Human video and embodiment grounding

Separate passive priors, action proxies, paired supervision and deployment-time human context.

<details>
<summary><strong>Unfold the argument</strong> · From observed human motion to robot-grounded supervision</summary>

<br>

**The question.** Which part of human experience transfers, and where do executable robot actions come from?

**Reading chain**

1. **Identify the role of the video.** Human video may supply representation pretraining, motion proxies, predictive supervision, generated task motion or context at deployment. These roles require different correspondences to robot experience.
2. **Expose the transfer gaps.** Track sensing/viewpoint, kinematics, contact dynamics and action labels separately. Matching an image or hand trajectory does not resolve all four gaps.
3. **Ground the robot interface.** Locate paired robot data, retargeting, action proxies or another stated mapping into executable controls. Ask which information is learned from the human source and which is supplied by robot supervision.
4. **Distinguish context from adaptation.** A frozen model can condition on a demonstration without changing weights. Fast-weight adaptation before rollout changes a different object and does not automatically imply updates during physical execution.

**Generated motion and predictive transfer**

[Gen2Act](docs/methods.md#paper-bharadhwaj2025gen2act) and [Dreamitate](docs/methods.md#paper-liang2025dreamitate) connect generated task motion to robot behavior. [DreamDojo](docs/methods.md#paper-gao2026dreamdojo) learns interaction priors from human video before robot grounding. [EgoWAM](docs/methods.md#paper-egowam2026) compares predictive targets using human and robot data, while [AnyWorld](docs/methods.md#paper-chen2026anyworld) separates motion, camera and embodiment conditions. Read the conversion step in each pipeline rather than treating passive human video as already labeled robot interaction.

**Two deployment interfaces, plus a sensing contrast**

[Zero-WAM](docs/methods.md#paper-zhou2026zerowam) supplies human video as context to frozen weights. [WAM-TTT](docs/methods.md#paper-feng2026wamttt) adapts fast weights before execution and holds them fixed during rollout in the reviewed account. [TactAlign](docs/methods.md#paper-tactalign2026) tests human–robot touch alignment and policy transfer, which does not by itself validate transferred predictive dynamics. [EgoZero](docs/methods.md#paper-egozero2025) supplies an adjacent route from wearable observations to robot-grounded learning signals.

**What would establish usefulness?**

Disentangle the gain from human data, robot fine-tuning and the grounding mechanism. Test held-out tasks or embodiments under the reported adaptation protocol and identify what stays frozen. If a method reports task progress rather than success, preserve that distinction. For contact transfer, a sensing or policy result needs separate evidence before supporting a claim about predictive robot dynamics.

**Where the argument goes next.** Continue to [embodiment](#track-embodiment) for action semantics and physical feasibility, or [simulation](#track-simulation) when human priors generate experience for policy learning.

**Survey connections:** [09. Human and Egocentric Data as a World-Model Source](docs/chapters/09-human-egocentric.md) · [07. Foundation-Driven World Models and Robot Priors](docs/chapters/07-foundation-priors.md) · [08. Tactile and Contact World Models](docs/chapters/08-tactile-contact.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

| Entry | Read for |
|---|---|
| [EgoWAM](docs/methods.md#paper-egowam2026) · 2026<br><sub>Predictive use</sub> | Compare predictive targets using human and robot data. |
| [AnyWorld](docs/methods.md#paper-chen2026anyworld) · 2026<br><sub>Predictive use</sub> | Factor human motion, camera and embodiment conditions. |
| [Zero-WAM](docs/methods.md#paper-zhou2026zerowam) · 2026<br><sub>Predictive use</sub> | Condition frozen world-action models on human demonstrations. |
| [TactAlign](docs/methods.md#paper-tactalign2026) · 2026<br><sub>Policy context</sub> | Align human and robot touch for policy transfer. |
| [EgoZero](docs/methods.md#paper-egozero2025) · 2025<br><sub>Policy context</sub> | Extract robot-grounded learning signals from smart glasses. |

[Browse all 29 cited works in this route →](docs/paper-index.md#track-human-data)

<a id="track-embodiment"></a>

### 07 · Embodiments and task interfaces

Read manipulation, navigation, locomotion and driving through their action units and feedback requirements.

<details>
<summary><strong>Unfold the argument</strong> · From a shared model to the constraints of a particular robot</summary>

<br>

**The question.** Which assumptions change when the same predictive idea moves between manipulation, navigation, locomotion and driving?

**Reading chain**

1. **Specify the controlled quantity.** Record joint commands, end-effector targets, action chunks or higher-level motion commands, together with controller rate and actuation limits. An action token has no portable physical meaning without this mapping.
2. **Determine the necessary history.** Manipulation needs contact and object state, navigation needs persistent spatial belief, locomotion needs balance and morphology, and driving needs interaction with other traffic. Choose memory and prediction targets for the task.
3. **Check the prediction-to-controller handoff.** Explain how model outputs become feasible commands. A generated plan, retargeted trajectory and online corrective controller provide different execution interfaces.
4. **Record assistance and physical feedback.** Locate human corrections, resets, safety interventions and the next observation. A command-conditioned locomotion policy is not automatically an autonomous navigation system.

**The embodiment layer changes the meaning of a result**

[PointWorld](docs/methods.md#paper-pointworld2026) and [Large Video Planner](docs/methods.md#paper-chen2025largevideoplanner) illustrate why predictive planning and physical execution must be separated: the reviewed hardware evidence is open loop. [DayDreamer](docs/methods.md#paper-wu2022daydreamer) provides a different perspective on learned dynamics and physical data collection. These examples motivate the [embodiment chapter](docs/chapters/10-embodiments.md), where action units, observation history and feedback determine whether a comparison is transferable.

**Policies are consumers and baselines**

[OpenVLA](docs/methods.md#paper-openvla2024), [pi0](docs/methods.md#paper-pi0) and [GR00T N1.7](docs/methods.md#paper-nvidia2026groot17) provide policy context. Their action interfaces can consume generated supervision or be evaluated in a learned environment, but action prediction alone is not consequence prediction under alternative actions. Read these policies alongside the relevant world-model consumer rather than assigning them the same model category.

**What would establish usefulness?**

Compare within a stated robot, controller, sensor suite, task distribution and intervention policy. Report full control latency and assistance rather than inference speed alone. For cross-robot transfer, identify what is shared and what is recalibrated or relearned. A stronger result on one embodiment does not establish a general ranking across different action spaces and physical constraints.

**Where the argument goes next.** Use [evaluation](#track-evaluation) to choose the matching evidence. If human assistance changes later behavior, follow [interaction](#track-interaction) to identify the retained update.

**Survey connections:** [10. Embodiment and Task Perspective](docs/chapters/10-embodiments.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) · [04. The Optimizable Roles of World Models](docs/chapters/04-roles.md).

</details>

[Browse all 59 cited works in this route →](docs/paper-index.md#track-embodiment)

<a id="track-evaluation"></a>

### 08 · Evaluation, reliability and safety

Assess model quality, policy utility and deployment reliability with use-specific evidence.

<details>
<summary><strong>Unfold the argument</strong> · From prediction quality to utility, reliability and attribution</summary>

<br>

**The question.** Which reported measurement answers the claim the system actually makes?

**Reading chain**

1. **Test model behavior.** Measure task-relevant prediction, action sensitivity, temporal consistency and contact or geometry validity. Specify the conditioning actions and the query distribution.
2. **Test the consumer.** Ask whether the planner, learner or evaluator improves under a matched budget. A better-looking video and a better-performing robot are separate observations.
3. **Test deployment behavior.** Record latency, failures, recoveries, assistance, retention and shifted physical conditions. Include the monitor and fallback that influence which trajectories are observed.
4. **State the evidence boundary.** Keep paper version, platforms, policy families, tasks, uncertainty and total cost beside the claim. Use an evaluation protocol that could distinguish the proposed source of the improvement.

**Benchmarks answer different questions**

[EWMBench](docs/methods.md#paper-yue2025ewmbench) examines aspects of generated scene and motion quality. [WorldArena](docs/methods.md#paper-shang2026worldarena) considers perceptual and functional world-model utility, while [World-in-World](docs/methods.md#paper-worldinworld2025) provides a closed-loop assessment context. These are complementary entry points rather than a single interchangeable leaderboard. Start from the claim—prediction, action consequence or downstream utility—then select the protocol.

**Ranking, monitoring and safety require different evidence**

[RoboWorld](docs/methods.md#paper-nsim-roboworld) and [WorldEval](docs/methods.md#paper-li2025worldeval) illustrate learned policy evaluation. Ranking agreement does not establish calibrated success probabilities. [Model-Based Runtime Monitoring](docs/methods.md#paper-liu2024runtime) concerns prospective failure detection, while [SafeDreamer](docs/methods.md#paper-huang2024safedreamer) introduces constraint-related prediction and control. A low observed failure rate may reflect the controller, monitor, fallback or human intervention, so model-specific attribution requires an appropriate comparison.

**What would establish usefulness?**

Use the [evaluation worksheet](docs/evaluation.md) to record the predicted quantity, consumer, changed object and feedback before choosing metrics. Preserve intervention-induced censoring: when assistance changes a trajectory, the outcome without assistance is unobserved. Model-to-real disagreement is a reason to investigate, not by itself proof of deliberate model exploitation. Proposed utility curves and reliability margins need measured data and a declared uncertainty procedure.

**Where the argument goes next.** Select the supporting [resources](#track-resources), then follow [interaction](#track-interaction) to connect failures to the next update rather than reporting them only as a final score.

**Survey connections:** [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) · [15. Open Challenges and Future Directions](docs/chapters/15-research-agenda.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

| Entry | Read for |
|---|---|
| [RoboWorld](docs/methods.md#paper-nsim-roboworld) · 2026<br><sub>Predictive use</sub> | Compare policies in neural simulation; correlation is not calibration. |
| [WorldEval](docs/methods.md#paper-li2025worldeval) · 2025<br><sub>Predictive use</sub> | Use predicted consequences to evaluate robot policies. |
| [Model-Based Runtime Monitoring](docs/methods.md#paper-liu2024runtime) · 2024<br><sub>Predictive use</sub> | Predict near-term failures to support deployment monitoring. |
| [Sirius-Fleet](docs/methods.md#paper-liu2025siriusfleet) · 2025<br><sub>Predictive use</sub> | Allocate fleet supervision using prospective anomaly prediction. |
| [WorldArena](docs/methods.md#paper-shang2026worldarena) · 2026<br><sub>Benchmark</sub> | Evaluate perception and functional world-model utility. |
| [EWMBench](docs/methods.md#paper-yue2025ewmbench) · 2025<br><sub>Benchmark</sub> | Diagnose scene, motion and semantic generation quality. |
| [World-in-World](docs/methods.md#paper-worldinworld2025) · 2026<br><sub>Benchmark</sub> | Study world-model assessment in a closed-loop setting. |
| [SafeDreamer](docs/methods.md#paper-huang2024safedreamer) · 2024<br><sub>Predictive use</sub> | Use predicted costs in constrained policy learning. |

[Browse all 105 cited works in this route →](docs/paper-index.md#track-evaluation)

<a id="track-resources"></a>

### 09 · Datasets, environments and benchmarks

Find the data, tools and evaluation fixtures that support a particular interface.

<details>
<summary><strong>Unfold the argument</strong> · From a research question to the artifact that can test it</summary>

<br>

**The question.** Does a dataset, simulator or harness expose the interface required by the intended experiment?

**Reading chain**

1. **Define the intended use.** Choose model fitting, alternative-action decisions, policy learning or deployment assessment before choosing a resource. Each use imposes a different data and execution contract.
2. **Inspect the available signals.** Check actions, timestamps, observations, robot and controller metadata, rewards, task labels and intervention records. Missing correspondence can prevent a log from supporting the intended prediction query.
3. **Inspect interaction capabilities.** For branching decisions or imagined policy learning, examine initial states, resets, executable action queries and returned observations. Static trajectories do not supply all of these capabilities.
4. **Construct the full evidence loop.** Combine the artifact with a consumer and an evaluation protocol. Preserve collection, adaptation, filtering and physical validation costs instead of treating a repository URL as an experimental result.

**Four interfaces, not four maturity levels**

The survey separates Model, Decision, Learning and Deployment capabilities. They are non-nested: a trajectory dataset can fit a predictor without enabling branching control, while a policy-evaluation harness can compare outcomes without exposing a policy optimizer. The [resource chapter](docs/chapters/12-resources.md) and [upstream resource guide](docs/resources.md) should therefore be read as interface choices rather than a ranking of artifact prestige.

**Match the artifact to the method’s claim**

A [DINO-WM](docs/methods.md#paper-zhou2025dinowm)-style planning question needs compatible visual states and action consequences. An [IWS](docs/methods.md#paper-interactiveworldsim2026)-style demonstration route needs an interactive collection interface and usable supervision. A [RoboWorld](docs/methods.md#paper-nsim-roboworld)-style evaluation question needs independent outcomes on policies beyond those used to construct the evaluator. These examples explain why selecting an artifact is downstream of defining the consumer.

**What would establish usefulness?**

Read the actual released interface, version and metadata, and distinguish a paper description from an executable artifact. The linked resources here are entry points whose identities were checked, not installations or reproduced experiments. To evaluate a release, verify that its inputs, outputs and reset or labeling behavior support the chosen claim, then connect it to an appropriate physical or independently grounded outcome.

**Where the argument goes next.** Return to [evaluation](#track-evaluation) with the chosen interface. Use [interaction](#track-interaction) if failures or deployment traces will become new data.

**Survey connections:** [12. Resources: Datasets, Simulators, Benchmarks, and Frameworks](docs/chapters/12-resources.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) · [A. Extended Survey Protocols](docs/chapters/a-review-protocol.md).

</details>

[Browse all 25 cited works in this route →](docs/paper-index.md#track-resources)

<a id="track-interaction"></a>

### 10 · Interaction and continual improvement

Track what feedback updates: context, actions, policy, model parameters or memory.

<details>
<summary><strong>Unfold the argument</strong> · From execution feedback to a named update and retained behavior</summary>

<br>

**The question.** What changes after interaction, and which part of that change persists?

**Reading chain**

1. **Acquire experience with provenance.** Record the collection policy, executed actions, observations, predicted outcomes, failures and interventions. Real transitions, human corrections and synthetic alternatives provide different kinds of supervision.
2. **Route each signal to its learner.** A failed action can provide valid dynamics supervision while being a poor behavior-cloning target. Corrective labels, rewards and counterfactual transitions must be sent to the appropriate policy, value or model update.
3. **Name the update destination and timing.** Distinguish observation context, action correction, policy memory, physical parameters, model weights and policy weights. Before-rollout adaptation, between-round refitting and during-execution updates are different protocols.
4. **Test retained competence.** After the new update, evaluate both the new condition and earlier behavior. Replay selection and modality-specific plasticity affect what the next learning round retains.

**Different meanings of policy improvement**

[VLAW](docs/methods.md#paper-vlaw2026) grounds the world model with real rollouts before using selected experience for policy training. [WorldSample](docs/methods.md#paper-xue2026worldsample) routes real and counterfactual transitions into critic and policy learning with a synthetic-data schedule. [VLA-RFT](docs/methods.md#paper-vlarft2025) uses policy GRPO with feedback from a frozen world simulator. [WAM-RL](docs/methods.md#paper-wamrl2026) separates actor RL from world-model video fine-tuning. An outer-loop diagram should retain those separate objectives and frozen components rather than drawing one undifferentiated update arrow.

**Correction, context and retention**

[Sirius-Fleet](docs/methods.md#paper-liu2025siriusfleet) connects prospective prediction to allocating human supervision, and [Hi-WM](docs/methods.md#paper-li2026hiwm) turns imagined failure states into corrective experience. [Zero-WAM](docs/methods.md#paper-zhou2026zerowam) changes context rather than model weights; [WAM-TTT](docs/methods.md#paper-feng2026wamttt) changes fast weights before rollout. [REGEN](docs/methods.md#paper-govind2026regen) uses generated replay for continual imitation, while [Planning with Online World Models](docs/methods.md#paper-liu2025onlinewm) examines predictive refitting for planning. Their shared question is where experience is stored and how that storage affects the next decision.

**What would establish usefulness?**

Write separate model and policy objectives, update cadence, frozen components and the provenance of each transition. Measure new-task improvement together with old-task retention, including interventions and curation costs. The predictive fidelity of recorded actions does not automatically validate altered-action counterfactuals used to train the policy. An observed failure identifies an outcome; its suspected cause still needs a discriminating comparison.

**Where the argument goes next.** Follow [open problems](#track-frontiers) for query shift, persistent memory and long-run retention. Return to [evaluation](#track-evaluation) to design the comparison for a claimed update.

**Survey connections:** [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md) · [06. From Roles to Policy Improvement](docs/chapters/06-learning-regimes.md) · [09. Human and Egocentric Data as a World-Model Source](docs/chapters/09-human-egocentric.md) · [08. Tactile and Contact World Models](docs/chapters/08-tactile-contact.md).

</details>

| Entry | Read for |
|---|---|
| [VLA-RFT](docs/methods.md#paper-vlarft2025) · 2025<br><sub>Predictive use</sub> | Policy GRPO with rewards from a frozen world simulator. |
| [World-Gymnast](docs/methods.md#paper-worldgymnast2026) · 2026<br><sub>Predictive use</sub> | Use learned-world interaction for robot policy learning. |
| [WAM-TTT](docs/methods.md#paper-feng2026wamttt) · 2026<br><sub>Predictive use</sub> | Adapt fast weights from human video before execution. |
| [VLAW](docs/methods.md#paper-vlaw2026) · 2026<br><sub>Predictive use</sub> | Refit the world model with real rollouts, then train on selected data. |
| [WorldSample](docs/methods.md#paper-xue2026worldsample) · 2026<br><sub>Predictive use</sub> | Route real and counterfactual transitions into critic and policy learning. |
| [WAM-RL](docs/methods.md#paper-wamrl2026) · 2026<br><sub>Predictive use</sub> | Actor RL and world-model video fine-tuning use separate objectives. |
| [REGEN](docs/methods.md#paper-govind2026regen) · 2026<br><sub>Predictive use</sub> | Generate replay for continual world-action imitation learning. |
| [Planning with Online World Models](docs/methods.md#paper-liu2025onlinewm) · 2025<br><sub>Predictive use</sub> | Refit predictive models for planning across changing environments. |

[Browse all 76 cited works in this route →](docs/paper-index.md#track-interaction)

<a id="track-frontiers"></a>

### 11 · Open problems and frontier directions

Follow unresolved questions in efficiency, streaming, memory, causality and accountable systems.

<details>
<summary><strong>Unfold the argument</strong> · From an unresolved interface gap to a testable research direction</summary>

<br>

**The question.** What observation would show that a proposed world-model improvement helps the robot for the claimed reason?

**Reading chain**

1. **Locate the missing link.** Identify whether the problem is action grounding, hidden state, contact transfer, rollout drift, decision latency, policy-induced queries, evaluation calibration or retained experience. A larger model is an intervention only after that link is specified.
2. **Propose a concrete change.** Change a query interface, representation, learning objective, memory or feedback destination. Explain how the change is expected to reach the consumer rather than assuming predictive improvement becomes utility.
3. **Choose a resolving comparison.** Match the consumer, data and total budget while varying the proposed mechanism. Use feasible off-expert actions, shifted conditions or held-out policy families where those are needed to test the explanation.
4. **Bound the conclusion.** Record the robot, task, model version, uncertainty and cost. A controlled result can establish a particular benefit without resolving every transfer, reliability or continual-learning question.

**Three connected directions**

Representation work such as [DINO-WM](docs/methods.md#paper-zhou2025dinowm) and [V-JEPA 2](docs/methods.md#paper-assran2025vjepa2) raises the question of which predictive features preserve action consequences. Contact systems such as [DexTacWAM](docs/methods.md#paper-yuan2026dextacwam) and [MuSe](docs/methods.md#paper-clark2026muse) raise the question of acquiring new sensory dynamics while retaining earlier competence. [WorldSample](docs/methods.md#paper-xue2026worldsample), [REGEN](docs/methods.md#paper-govind2026regen) and online-model planning raise the question of how the policy’s evolving experience changes prediction and learning. These directions connect through the consumer and returned feedback, rather than through a single architecture family.

**Make frontier evidence readable**

The [frontier atlas](docs/chapters/13-frontier-atlas.md) locates emerging systems by mechanism and reported evidence; the [research agenda](docs/chapters/15-research-agenda.md) turns unresolved boundaries into questions. Read them together. Frozen-model adaptation, open-loop execution, policy context and artifact availability should remain visible when interpreting a new paper. A new interface or release can motivate research without supplying a replicated cross-paper superiority claim.

**What would establish usefulness?**

Use the [evaluation guide](docs/evaluation.md) to turn a direction into measurable model behavior, policy effect and deployment behavior. Utility curves, optimism-gap analyses and reliability margins in the survey are proposed analytical constructs whose interpretation depends on actual measurements and a declared protocol. The useful endpoint of the reading chain is a comparison that could change the conclusion, not merely a longer list of new methods.

**Where the argument goes next.** Return to [foundations](#track-foundations) to state the consumer and to [resources](#track-resources) to identify the artifact needed for the proposed test.

**Survey connections:** [13. Frontier Evidence Atlas: 2024–2026](docs/chapters/13-frontier-atlas.md) · [15. Open Challenges and Future Directions](docs/chapters/15-research-agenda.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) · [14. From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md).

</details>

[Browse all 30 cited works in this route →](docs/paper-index.md#track-frontiers)

## Follow the paper

The complete paper map links every citation-bearing argument group. It preserves multiple uses of the same work, while the main index uses the clearer reading routes above.

[Open the paper map →](docs/paper-map.md)

<details>
<summary><strong>All paper sections</strong></summary>

| Section | Guide |
|---|---|
| 01 | [Introduction](docs/chapters/01-introduction.md) |
| 02 | [Positioning Among Existing Surveys](docs/chapters/02-related-surveys.md) |
| 03 | [A Robot Learning Loop View of World Models](docs/chapters/03-foundations.md) |
| 04 | [The Optimizable Roles of World Models](docs/chapters/04-roles.md) |
| 05 | [Representation Substrates and World-Model Mechanics](docs/chapters/05-representations.md) |
| 06 | [From Roles to Policy Improvement](docs/chapters/06-learning-regimes.md) |
| 07 | [Foundation-Driven World Models and Robot Priors](docs/chapters/07-foundation-priors.md) |
| 08 | [Tactile and Contact World Models](docs/chapters/08-tactile-contact.md) |
| 09 | [Human and Egocentric Data as a World-Model Source](docs/chapters/09-human-egocentric.md) |
| 10 | [Embodiment and Task Perspective](docs/chapters/10-embodiments.md) |
| 11 | [Evaluation: From Prediction Metrics to Closed-Loop Utility](docs/chapters/11-evaluation.md) |
| 12 | [Resources: Datasets, Simulators, Benchmarks, and Frameworks](docs/chapters/12-resources.md) |
| 13 | [Frontier Evidence Atlas: 2024–2026](docs/chapters/13-frontier-atlas.md) |
| 14 | [From Interaction to Model Improvement](docs/chapters/14-interaction-learning.md) |
| 15 | [Open Challenges and Future Directions](docs/chapters/15-research-agenda.md) |
| 16 | [Conclusion](docs/chapters/16-conclusion.md) |
| A | [Extended Survey Protocols](docs/chapters/a-review-protocol.md) |

</details>

## Read the evidence with the interface

Latent imagination can train an actor without deployment-time planning. Video generation can supply demonstrations without online RL. A planner can select a trajectory that is later executed open-loop. Tactile feedback can correct an action without updating model weights. The [method cards](docs/methods.md) keep these distinctions visible.

[Scope and taxonomy](docs/scope-and-taxonomy.md) · [Reading paths](docs/reading-paths.md) · [Evaluation](docs/evaluation.md)

## Contribute

Correct an identity, clarify a mechanism or add a resource cited by the companion survey. Keep the predictive interface, downstream consumer and evidence boundary together. See [contributing](CONTRIBUTING.md).

[Catalog JSON](data/catalog.json) · [Reading-route JSON](data/organization.json) · [Citation map](data/citation-map.json) · [CSV](data/catalog.csv) · [BibTeX](data/references.bib)

<details>
<summary><strong>Snapshot, verification and design references</strong></summary>

Manuscript snapshot: **2026-10-01**. Organization and presentation reviewed: **2026-10-02**. The catalog includes contextual literature. Primary bibliographic checks do not constitute scientific replication; some source records lack an extracted paper URL.

[Verification coverage](docs/provenance.md) · [Five layout references and Apple guidance](docs/design-notes.md)

Linked papers, datasets and code retain their authorship and upstream licenses. No full papers or private manuscript paragraphs are redistributed.

</details>
