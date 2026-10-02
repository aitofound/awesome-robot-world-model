# From prediction to control: the reading argument

[Home](../README.md) · [Method cards](methods.md) · [Source argument map](paper-map.md)

This guide explains why the Atlas moves from foundations and representations to downstream use, physical grounding, evaluation and returned experience. The sequences below are comparative reading suggestions grounded in the companion survey. They are not a genealogy of methods or a performance ranking.

Read a system through five connected questions: what information is available, what consequence is predicted, which consumer uses it, what execution feedback changes, and which evidence supports the claimed benefit. When following a method link, keep its interface, changed object and reported execution boundary together.

[01 Foundations and the Prediction-to-Control Gap](#track-foundations) · [02 Representations and predictive mechanics](#track-representations) · [03 Policy learning and planning](#track-learning-control) · [04 Foundation priors, simulation and generated experience](#track-simulation) · [05 Touch and contact](#track-tactile) · [06 Human video and embodiment grounding](#track-human-data) · [07 Embodiments and task interfaces](#track-embodiment) · [08 Evaluation, reliability and safety](#track-evaluation) · [09 Datasets, environments and benchmarks](#track-resources) · [10 Interaction and continual improvement](#track-interaction) · [11 Open problems and frontier directions](#track-frontiers)

<a id="track-foundations"></a>

## 01. Foundations and the Prediction-to-Control Gap

Define the model’s downstream use and distinguish predictive quality from decision utility.

**The question.** What has to happen between predicting the world and improving a robot’s behavior?

**Reading chain**

1. **Recover the information state.** Start from observations and action history. A compact latent state is useful when it retains the consequences relevant to the task, even if it cannot reconstruct every visible detail.
2. **Ask a counterfactual question.** Hold the history fixed and change a feasible action. The prediction should change the affected objects, contacts or outcomes while preserving unrelated parts of the scene.
3. **Name the consumer.** Identify the planner, actor learner, demonstration learner, evaluator or monitor that receives the output. Explain which action, target or parameter that consumer changes.
4. **Locate the return path.** Follow execution back to the next decision or learning round. Refreshing observations, correcting an action and refitting dynamics close different parts of the loop.

**Why begin with World Models?**

[World Models](methods.md#paper-ha2018worldmodels) makes the representation–dynamics–controller relationship easy to inspect. Its place here is conceptual: the early control setting explains how a learned state can support behavior, while the robot-specific sensing and deployment requirements arrive later. This gives the reader a vocabulary for asking what the prediction contributes before comparing larger architectures.

**The first useful fork**

Read [PlaNet](methods.md#paper-hafner2019planet) beside [Dreamer](methods.md#paper-hafner2019dreamer). PlaNet uses imagined futures to select actions through planning. Dreamer uses imagined trajectories to train an actor and value model. The two systems illustrate distinct consumers of predictive dynamics, so a single “world-model-based control” label would hide the most useful comparison.

**What would establish usefulness?**

The central test is downstream usefulness under the stated task and budget. Low prediction error or plausible video is relevant only insofar as it preserves the consequences used by the consumer. Keep the [operational criterion](scope-and-taxonomy.md) beside the [six functional roles](roles.md): a role identifies a use, while strict closed-loop qualification also needs action-responsive prediction, implemented coupling and execution evidence.

**Where the argument goes next.** Continue to [representations](#track-representations) to ask what information the model preserves, then to [policy learning and planning](#track-learning-control) to examine the consumer.

**Survey connections:** [01. Introduction](chapters/01-introduction.md) · [03. A Robot Learning Loop View of World Models](chapters/03-foundations.md) · [04. The Optimizable Roles of World Models](chapters/04-roles.md).

[Browse this route’s cited works →](paper-index.md#track-foundations)

<a id="track-representations"></a>

## 02. Representations and predictive mechanics

Choose a state substrate, action interface and rollout mechanism that preserve task-relevant consequences.

**The question.** Which representation preserves the action consequences that the next decision needs?

**Reading chain**

1. **Choose the task state.** Compare pixels, visual features, object or point states, contact variables and physical parameters by the information they retain. A visually rich state can still omit the friction or contact event that determines success.
2. **Specify the query.** Write down the conditioning variables and the predicted quantity. Observation-and-goal conditioning, action-chunk conditioning and a query under an alternative control are different interfaces.
3. **Separate substrate from mechanics.** The state representation answers what is modeled. Recurrent dynamics, autoregression, diffusion, flow and physical-time ODEs answer how prediction is computed. A method can combine more than one of these axes.
4. **Connect the representation to a consumer.** Explain how a feature distance, point trajectory or simulated physical state becomes a planning objective or learning signal. Then check the executed controller rather than stopping at the representation benchmark.

**Predictive features versus action grounding**

[DINO-WM](methods.md#paper-zhou2025dinowm) connects pretrained visual features to action-conditioned prediction and planning. [V-JEPA 2](methods.md#paper-assran2025vjepa2) should be read as video pretraining followed by a distinct action-conditioned robot adaptation. [ACT-JEPA](methods.md#paper-actjepa2025) supplies predictive representation and policy-learning context. These papers belong together because they ask how learned features become useful, but the presence of a predictive embedding objective does not make every entry an online action-search system.

**Geometry, physics and temporal queries**

[PointWorld](methods.md#paper-pointworld2026) exposes 3D action consequences to MPPI, while [PhysTwin](methods.md#paper-jiang2025phystwin) reconstructs structured deformable physics from video. [ODEWorld](methods.md#paper-liu2026odeworld) queries observation- and goal-conditioned futures in physical time; its reviewed interface does not accept queried candidate actions. [Causal-JEPA](methods.md#paper-nam2026causaljepa) provides object-aware predictive dependencies, which are not by themselves an identified causal graph. These distinctions prevent an architecture name from substituting for an interface description.

**What would establish usefulness?**

Ask whether the representation preserves task-relevant geometry, occlusion, contact and action sensitivity over the consumer’s horizon. Measure the entire decision pipeline when a planner is used. PointWorld’s reported physical execution remains open loop, so its predictive representation and planning evidence must not be upgraded into a claim of online hardware correction.

**Where the argument goes next.** Use [learning and control](#track-learning-control) to trace the chosen interface into action selection. For hidden contact state, follow [touch and contact](#track-tactile).

**Survey connections:** [05. Representation Substrates and World-Model Mechanics](chapters/05-representations.md) · [06. From Roles to Policy Improvement](chapters/06-learning-regimes.md) · [10. Embodiment and Task Perspective](chapters/10-embodiments.md).

[Browse this route’s cited works →](paper-index.md#track-representations)

<a id="track-learning-control"></a>

## 03. Policy learning and planning

Separate actor learning through imagination from action selection through search or control.

**The question.** Does the model change policy parameters during learning, or action choices during execution?

**Reading chain**

1. **Identify the learning signal.** Determine whether predictions supply imagined transitions, demonstrations, rewards, value targets or a planning cost. The same transition model can support several learning regimes.
2. **Trace the update.** For an imagination learner, follow generated trajectories into actor and value updates. For a planner, follow candidate actions into predicted consequences, scoring and selection.
3. **Inspect deployment separately.** Check whether the deployed policy calls the model, whether a planner replans after new observations, and whether an action chunk is executed in full. Training-time model use does not specify deployment-time computation.
4. **Close the appropriate loop.** Record real data collection, model fitting, policy fitting and action correction as separate events. Their update rates and their dependence on fresh physical experience can differ.

**PlaNet, Dreamer and the physical learning loop**

[PlaNet](methods.md#paper-hafner2019planet) is the planning reference: latent rollouts guide action selection. [Dreamer](methods.md#paper-hafner2019dreamer), [DreamerV2](methods.md#paper-hafner2021dreamerv2) and [DreamerV3](methods.md#paper-hafner2023dreamerv3) form an imagined policy-learning route. [DayDreamer](methods.md#paper-wu2022daydreamer) brings that discussion to physical data collection and learning. Reading them together reveals where robot experience enters the learner, rather than implying that every deployed actor executes a rollout planner.

**Search, value and executable motion**

[TD-MPC2](methods.md#paper-hansen2024tdmpc2) combines latent prediction and value estimates with model-predictive action selection. [WorldPlanner](methods.md#paper-worldplanner2025) connects global tree search to local MPC. [Large Video Planner](methods.md#paper-chen2025largevideoplanner) instead turns visual plans into executable motion through retargeting, followed by open-loop execution in the reviewed evidence. [RoboDreamer](methods.md#paper-robodreamer2024) illustrates compositional task imagination. These interfaces should be compared at the handoff from prediction to an executable decision.

**What would establish usefulness?**

Match real interaction, policy capacity and compute when assessing policy improvement. For planning, report candidate count, horizon, scoring, replanning cadence and full latency. For imagination learning, separate real and synthetic transitions and inspect performance under the learned policy’s query distribution. A success rate without these conditions does not establish which consumer benefited.

**Where the argument goes next.** Follow [neural simulation](#track-simulation) when generated experience becomes reusable training data. Follow [interaction](#track-interaction) when real deployment changes the next learning round.

**Survey connections:** [04. The Optimizable Roles of World Models](chapters/04-roles.md) · [06. From Roles to Policy Improvement](chapters/06-learning-regimes.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-learning-control)

<a id="track-simulation"></a>

## 04. Foundation priors, simulation and generated experience

Distinguish general priors, interactive neural environments and pipelines that generate training data.

**The question.** What makes generated experience usable by a robot policy, and which learning rule consumes it?

**Reading chain**

1. **Adapt the prior.** Start from the pretrained representation or video prior, then locate robot action grounding, observation compatibility and task conditioning. A broad visual prior is not yet an executable robot environment.
2. **Define the experience interface.** For interaction, a policy or human chooses an action and receives the predicted next observation before choosing again. Initial contexts, resets and the actor’s required modalities are part of that interface.
3. **Choose a downstream branch.** Demonstration collection, filtered supervised learning, imagined policy optimization and policy evaluation consume experience differently. Rewards and termination may come from external modules rather than the transition predictor.
4. **Return to independent physical evidence.** Train or assess the consumer, then check its physical outcomes. If new real rollouts refit the model, show that additional return path explicitly; it is not a mandatory component of every neural simulator.

**Three ways to learn from generated experience**

[IWS](methods.md#paper-interactiveworldsim2026) turns simulator interaction into demonstration-based learning, while [Hi-WM](methods.md#paper-li2026hiwm) uses rollback and branching for targeted human correction. [GE-Sim 2.0](methods.md#paper-qiu2026gesim2) filters generated rollouts for behavior-cloning updates. [DreamGen](methods.md#paper-jang2025dreamgen) recovers pseudo-actions so generated video can supply demonstrations. [RWM](methods.md#paper-li2025roboticworldmodel), [WoVR](methods.md#paper-nsim-wovr) and [WorldGymnast](methods.md#paper-worldgymnast2026) belong on the policy-optimization branch. The presence of synthetic trajectories cannot decide which branch a paper implements.

**Where foundation priors and evaluators fit**

[Cosmos](methods.md#paper-nvidia2025cosmos) and [Genie](methods.md#paper-bruce2024genie) provide generative context. [DreamDojo](methods.md#paper-gao2026dreamdojo) moves from human-video interaction priors toward robot grounding; [GeniWorld](methods.md#paper-gu2026geniworld) grounds conditions through rendered robot actions. [RoboWorld](methods.md#paper-nsim-roboworld) and [WorldEval](methods.md#paper-li2025worldeval) ask whether predicted outcomes can evaluate policies. Evaluation can be useful without a policy update, so its evidence should be read separately from training gains.

**What would establish usefulness?**

For generated demonstrations, include adaptation, generation, filtering, labeling and rejected samples in the cost. For policy optimization, test independent physical performance and the actions favored by the learned policy. For evaluation, measure held-out policy ranking and absolute outcome calibration separately. Matching the final training-set size, as in an IWS comparison, does not by itself match the cost of constructing the world model.

**Where the argument goes next.** Use [resources](#track-resources) to check whether a released artifact exposes the required interface. Continue to [evaluation](#track-evaluation) for the evidence contract or [interaction](#track-interaction) for real–synthetic updates.

**Survey connections:** [07. Foundation-Driven World Models and Robot Priors](chapters/07-foundation-priors.md) · [06. From Roles to Policy Improvement](chapters/06-learning-regimes.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](chapters/11-evaluation.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-simulation)

<a id="track-tactile"></a>

## 05. Touch and contact

Connect hidden contact state to predictive control, corrective action and multisensory learning.

**The question.** What does touch reveal that vision misses, and how does that information change control?

**Reading chain**

1. **Recover local interaction state.** Contact, slip, compliance and occluded deformation can remain ambiguous in camera observations. Tactile or force history supplies evidence about the local interaction rather than just another visual view.
2. **Predict a contact consequence.** Condition on the robot’s action and predict tactile images, latent contact state or deformation. Distinguish predicting the future from supplying current touch directly to an action policy.
3. **Deliver the prediction in time.** A planner, compliance controller or corrective module must consume the forecast before the relevant failure. State the contact horizon and the rate of correction, not only the video-generation rate.
4. **Transfer and retain.** When visual priors initialize touch modeling, identify the shared encoder and the modality-specific adaptation. Test both the new contact behavior and the predictive or control competence retained from earlier modalities.

**Prediction, planning and correction**

[Manipulation by Feel](methods.md#paper-tian2019manipulation) uses predicted tactile images as a servoing objective. [RoboPack](methods.md#paper-ai2024robopack) uses vision and touch to infer physical state for planning, while [VIRDO++](methods.md#paper-wi2022virdopp) models deformable state. [Visuo-Tactile World Models](methods.md#paper-visuotactilewm2026) and [OmniVTA](methods.md#paper-omnivta2026) connect contact prediction to different consumers: the former retains an open-loop physical planning boundary, while the latter includes execution-time corrective feedback. This is why “uses touch” is too broad a grouping by itself.

**A sensing prior is not the predictive loop**

[Sparsh](methods.md#paper-higuera2024sparsh) and [AnyTouch](methods.md#paper-feng2025anytouch) provide reusable tactile representations. [OmniVTLA](methods.md#paper-cheng2025omnivtla) supplies touch-conditioned policy context and is distinct from OmniVTA. [DexTacWAM](methods.md#paper-yuan2026dextacwam), [VTAM](methods.md#paper-yuan2026vtam), [Dream-Tac](methods.md#paper-lou2026dreamtac) and [Tactile-WAM](methods.md#paper-wu2026tactilewam) motivate a further comparison: where visual priors are reused, how touch affects prediction and action, and which pathways are allowed to adapt. [MuSe](methods.md#paper-clark2026muse) adds the retention question when sensing expands.

**What would establish usefulness?**

Compare predictive touch with direct tactile conditioning under matched sensors, data and policy capacity. Check contact-sensitive errors, downstream control and full decision latency. A separated or aligned latent space alone cannot establish utility. Vision-to-touch retention should be measured on earlier behavior as well as the newly acquired sensing task, within the actual sensor and robot scope.

**Where the argument goes next.** Follow [human data](#track-human-data) for the asymmetry between abundant video and scarce robot contact data. Follow [interaction](#track-interaction) for modality expansion, replay and retained behavior.

**Survey connections:** [08. Tactile and Contact World Models](chapters/08-tactile-contact.md) · [05. Representation Substrates and World-Model Mechanics](chapters/05-representations.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-tactile)

<a id="track-human-data"></a>

## 06. Human video and embodiment grounding

Separate passive priors, action proxies, paired supervision and deployment-time human context.

**The question.** Which part of human experience transfers, and where do executable robot actions come from?

**Reading chain**

1. **Identify the role of the video.** Human video may supply representation pretraining, motion proxies, predictive supervision, generated task motion or context at deployment. These roles require different correspondences to robot experience.
2. **Expose the transfer gaps.** Track sensing/viewpoint, kinematics, contact dynamics and action labels separately. Matching an image or hand trajectory does not resolve all four gaps.
3. **Ground the robot interface.** Locate paired robot data, retargeting, action proxies or another stated mapping into executable controls. Ask which information is learned from the human source and which is supplied by robot supervision.
4. **Distinguish context from adaptation.** A frozen model can condition on a demonstration without changing weights. Fast-weight adaptation before rollout changes a different object and does not automatically imply updates during physical execution.

**Generated motion and predictive transfer**

[Gen2Act](methods.md#paper-bharadhwaj2025gen2act) and [Dreamitate](methods.md#paper-liang2025dreamitate) connect generated task motion to robot behavior. [DreamDojo](methods.md#paper-gao2026dreamdojo) learns interaction priors from human video before robot grounding. [EgoWAM](methods.md#paper-egowam2026) compares predictive targets using human and robot data, while [AnyWorld](methods.md#paper-chen2026anyworld) separates motion, camera and embodiment conditions. Read the conversion step in each pipeline rather than treating passive human video as already labeled robot interaction.

**Two deployment interfaces, plus a sensing contrast**

[Zero-WAM](methods.md#paper-zhou2026zerowam) supplies human video as context to frozen weights. [WAM-TTT](methods.md#paper-feng2026wamttt) adapts fast weights before execution and holds them fixed during rollout in the reviewed account. [TactAlign](methods.md#paper-tactalign2026) tests human–robot touch alignment and policy transfer, which does not by itself validate transferred predictive dynamics. [EgoZero](methods.md#paper-egozero2025) supplies an adjacent route from wearable observations to robot-grounded learning signals.

**What would establish usefulness?**

Disentangle the gain from human data, robot fine-tuning and the grounding mechanism. Test held-out tasks or embodiments under the reported adaptation protocol and identify what stays frozen. If a method reports task progress rather than success, preserve that distinction. For contact transfer, a sensing or policy result needs separate evidence before supporting a claim about predictive robot dynamics.

**Where the argument goes next.** Continue to [embodiment](#track-embodiment) for action semantics and physical feasibility, or [simulation](#track-simulation) when human priors generate experience for policy learning.

**Survey connections:** [09. Human and Egocentric Data as a World-Model Source](chapters/09-human-egocentric.md) · [07. Foundation-Driven World Models and Robot Priors](chapters/07-foundation-priors.md) · [08. Tactile and Contact World Models](chapters/08-tactile-contact.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-human-data)

<a id="track-embodiment"></a>

## 07. Embodiments and task interfaces

Read manipulation, navigation, locomotion and driving through their action units and feedback requirements.

**The question.** Which assumptions change when the same predictive idea moves between manipulation, navigation, locomotion and driving?

**Reading chain**

1. **Specify the controlled quantity.** Record joint commands, end-effector targets, action chunks or higher-level motion commands, together with controller rate and actuation limits. An action token has no portable physical meaning without this mapping.
2. **Determine the necessary history.** Manipulation needs contact and object state, navigation needs persistent spatial belief, locomotion needs balance and morphology, and driving needs interaction with other traffic. Choose memory and prediction targets for the task.
3. **Check the prediction-to-controller handoff.** Explain how model outputs become feasible commands. A generated plan, retargeted trajectory and online corrective controller provide different execution interfaces.
4. **Record assistance and physical feedback.** Locate human corrections, resets, safety interventions and the next observation. A command-conditioned locomotion policy is not automatically an autonomous navigation system.

**The embodiment layer changes the meaning of a result**

[PointWorld](methods.md#paper-pointworld2026) and [Large Video Planner](methods.md#paper-chen2025largevideoplanner) illustrate why predictive planning and physical execution must be separated: the reviewed hardware evidence is open loop. [DayDreamer](methods.md#paper-wu2022daydreamer) provides a different perspective on learned dynamics and physical data collection. These examples motivate the [embodiment chapter](chapters/10-embodiments.md), where action units, observation history and feedback determine whether a comparison is transferable.

**Policies are consumers and baselines**

[OpenVLA](methods.md#paper-openvla2024), [pi0](methods.md#paper-pi0) and [GR00T N1.7](methods.md#paper-nvidia2026groot17) provide policy context. Their action interfaces can consume generated supervision or be evaluated in a learned environment, but action prediction alone is not consequence prediction under alternative actions. Read these policies alongside the relevant world-model consumer rather than assigning them the same model category.

**What would establish usefulness?**

Compare within a stated robot, controller, sensor suite, task distribution and intervention policy. Report full control latency and assistance rather than inference speed alone. For cross-robot transfer, identify what is shared and what is recalibrated or relearned. A stronger result on one embodiment does not establish a general ranking across different action spaces and physical constraints.

**Where the argument goes next.** Use [evaluation](#track-evaluation) to choose the matching evidence. If human assistance changes later behavior, follow [interaction](#track-interaction) to identify the retained update.

**Survey connections:** [10. Embodiment and Task Perspective](chapters/10-embodiments.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](chapters/11-evaluation.md) · [04. The Optimizable Roles of World Models](chapters/04-roles.md).

[Browse this route’s cited works →](paper-index.md#track-embodiment)

<a id="track-evaluation"></a>

## 08. Evaluation, reliability and safety

Assess model quality, policy utility and deployment reliability with use-specific evidence.

**The question.** Which reported measurement answers the claim the system actually makes?

**Reading chain**

1. **Test model behavior.** Measure task-relevant prediction, action sensitivity, temporal consistency and contact or geometry validity. Specify the conditioning actions and the query distribution.
2. **Test the consumer.** Ask whether the planner, learner or evaluator improves under a matched budget. A better-looking video and a better-performing robot are separate observations.
3. **Test deployment behavior.** Record latency, failures, recoveries, assistance, retention and shifted physical conditions. Include the monitor and fallback that influence which trajectories are observed.
4. **State the evidence boundary.** Keep paper version, platforms, policy families, tasks, uncertainty and total cost beside the claim. Use an evaluation protocol that could distinguish the proposed source of the improvement.

**Benchmarks answer different questions**

[EWMBench](methods.md#paper-yue2025ewmbench) examines aspects of generated scene and motion quality. [WorldArena](methods.md#paper-shang2026worldarena) considers perceptual and functional world-model utility, while [World-in-World](methods.md#paper-worldinworld2025) provides a closed-loop assessment context. These are complementary entry points rather than a single interchangeable leaderboard. Start from the claim—prediction, action consequence or downstream utility—then select the protocol.

**Ranking, monitoring and safety require different evidence**

[RoboWorld](methods.md#paper-nsim-roboworld) and [WorldEval](methods.md#paper-li2025worldeval) illustrate learned policy evaluation. Ranking agreement does not establish calibrated success probabilities. [Model-Based Runtime Monitoring](methods.md#paper-liu2024runtime) concerns prospective failure detection, while [SafeDreamer](methods.md#paper-huang2024safedreamer) introduces constraint-related prediction and control. A low observed failure rate may reflect the controller, monitor, fallback or human intervention, so model-specific attribution requires an appropriate comparison.

**What would establish usefulness?**

Use the [evaluation worksheet](evaluation.md) to record the predicted quantity, consumer, changed object and feedback before choosing metrics. Preserve intervention-induced censoring: when assistance changes a trajectory, the outcome without assistance is unobserved. Model-to-real disagreement is a reason to investigate, not by itself proof of deliberate model exploitation. Proposed utility curves and reliability margins need measured data and a declared uncertainty procedure.

**Where the argument goes next.** Select the supporting [resources](#track-resources), then follow [interaction](#track-interaction) to connect failures to the next update rather than reporting them only as a final score.

**Survey connections:** [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](chapters/11-evaluation.md) · [15. Open Challenges and Future Directions](chapters/15-research-agenda.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-evaluation)

<a id="track-resources"></a>

## 09. Datasets, environments and benchmarks

Find the data, tools and evaluation fixtures that support a particular interface.

**The question.** Does a dataset, simulator or harness expose the interface required by the intended experiment?

**Reading chain**

1. **Define the intended use.** Choose model fitting, alternative-action decisions, policy learning or deployment assessment before choosing a resource. Each use imposes a different data and execution contract.
2. **Inspect the available signals.** Check actions, timestamps, observations, robot and controller metadata, rewards, task labels and intervention records. Missing correspondence can prevent a log from supporting the intended prediction query.
3. **Inspect interaction capabilities.** For branching decisions or imagined policy learning, examine initial states, resets, executable action queries and returned observations. Static trajectories do not supply all of these capabilities.
4. **Construct the full evidence loop.** Combine the artifact with a consumer and an evaluation protocol. Preserve collection, adaptation, filtering and physical validation costs instead of treating a repository URL as an experimental result.

**Four interfaces, not four maturity levels**

The survey separates Model, Decision, Learning and Deployment capabilities. They are non-nested: a trajectory dataset can fit a predictor without enabling branching control, while a policy-evaluation harness can compare outcomes without exposing a policy optimizer. The [resource chapter](chapters/12-resources.md) and [upstream resource guide](resources.md) should therefore be read as interface choices rather than a ranking of artifact prestige.

**Match the artifact to the method’s claim**

A [DINO-WM](methods.md#paper-zhou2025dinowm)-style planning question needs compatible visual states and action consequences. An [IWS](methods.md#paper-interactiveworldsim2026)-style demonstration route needs an interactive collection interface and usable supervision. A [RoboWorld](methods.md#paper-nsim-roboworld)-style evaluation question needs independent outcomes on policies beyond those used to construct the evaluator. These examples explain why selecting an artifact is downstream of defining the consumer.

**What would establish usefulness?**

Read the actual released interface, version and metadata, and distinguish a paper description from an executable artifact. The linked resources here are entry points whose identities were checked, not installations or reproduced experiments. To evaluate a release, verify that its inputs, outputs and reset or labeling behavior support the chosen claim, then connect it to an appropriate physical or independently grounded outcome.

**Where the argument goes next.** Return to [evaluation](#track-evaluation) with the chosen interface. Use [interaction](#track-interaction) if failures or deployment traces will become new data.

**Survey connections:** [12. Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](chapters/11-evaluation.md) · [A. Extended Survey Protocols](chapters/a-review-protocol.md).

[Browse this route’s cited works →](paper-index.md#track-resources)

<a id="track-interaction"></a>

## 10. Interaction and continual improvement

Track what feedback updates: context, actions, policy, model parameters or memory.

**The question.** What changes after interaction, and which part of that change persists?

**Reading chain**

1. **Acquire experience with provenance.** Record the collection policy, executed actions, observations, predicted outcomes, failures and interventions. Real transitions, human corrections and synthetic alternatives provide different kinds of supervision.
2. **Route each signal to its learner.** A failed action can provide valid dynamics supervision while being a poor behavior-cloning target. Corrective labels, rewards and counterfactual transitions must be sent to the appropriate policy, value or model update.
3. **Name the update destination and timing.** Distinguish observation context, action correction, policy memory, physical parameters, model weights and policy weights. Before-rollout adaptation, between-round refitting and during-execution updates are different protocols.
4. **Test retained competence.** After the new update, evaluate both the new condition and earlier behavior. Replay selection and modality-specific plasticity affect what the next learning round retains.

**Different meanings of policy improvement**

[VLAW](methods.md#paper-vlaw2026) grounds the world model with real rollouts before using selected experience for policy training. [WorldSample](methods.md#paper-xue2026worldsample) routes real and counterfactual transitions into critic and policy learning with a synthetic-data schedule. [VLA-RFT](methods.md#paper-vlarft2025) uses policy GRPO with feedback from a frozen world simulator. [WAM-RL](methods.md#paper-wamrl2026) separates actor RL from world-model video fine-tuning. An outer-loop diagram should retain those separate objectives and frozen components rather than drawing one undifferentiated update arrow.

**Correction, context and retention**

[Sirius-Fleet](methods.md#paper-liu2025siriusfleet) connects prospective prediction to allocating human supervision, and [Hi-WM](methods.md#paper-li2026hiwm) turns imagined failure states into corrective experience. [Zero-WAM](methods.md#paper-zhou2026zerowam) changes context rather than model weights; [WAM-TTT](methods.md#paper-feng2026wamttt) changes fast weights before rollout. [REGEN](methods.md#paper-govind2026regen) uses generated replay for continual imitation, while [Planning with Online World Models](methods.md#paper-liu2025onlinewm) examines predictive refitting for planning. Their shared question is where experience is stored and how that storage affects the next decision.

**What would establish usefulness?**

Write separate model and policy objectives, update cadence, frozen components and the provenance of each transition. Measure new-task improvement together with old-task retention, including interventions and curation costs. The predictive fidelity of recorded actions does not automatically validate altered-action counterfactuals used to train the policy. An observed failure identifies an outcome; its suspected cause still needs a discriminating comparison.

**Where the argument goes next.** Follow [open problems](#track-frontiers) for query shift, persistent memory and long-run retention. Return to [evaluation](#track-evaluation) to design the comparison for a claimed update.

**Survey connections:** [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md) · [06. From Roles to Policy Improvement](chapters/06-learning-regimes.md) · [09. Human and Egocentric Data as a World-Model Source](chapters/09-human-egocentric.md) · [08. Tactile and Contact World Models](chapters/08-tactile-contact.md).

[Browse this route’s cited works →](paper-index.md#track-interaction)

<a id="track-frontiers"></a>

## 11. Open problems and frontier directions

Follow unresolved questions in efficiency, streaming, memory, causality and accountable systems.

**The question.** What observation would show that a proposed world-model improvement helps the robot for the claimed reason?

**Reading chain**

1. **Locate the missing link.** Identify whether the problem is action grounding, hidden state, contact transfer, rollout drift, decision latency, policy-induced queries, evaluation calibration or retained experience. A larger model is an intervention only after that link is specified.
2. **Propose a concrete change.** Change a query interface, representation, learning objective, memory or feedback destination. Explain how the change is expected to reach the consumer rather than assuming predictive improvement becomes utility.
3. **Choose a resolving comparison.** Match the consumer, data and total budget while varying the proposed mechanism. Use feasible off-expert actions, shifted conditions or held-out policy families where those are needed to test the explanation.
4. **Bound the conclusion.** Record the robot, task, model version, uncertainty and cost. A controlled result can establish a particular benefit without resolving every transfer, reliability or continual-learning question.

**Three connected directions**

Representation work such as [DINO-WM](methods.md#paper-zhou2025dinowm) and [V-JEPA 2](methods.md#paper-assran2025vjepa2) raises the question of which predictive features preserve action consequences. Contact systems such as [DexTacWAM](methods.md#paper-yuan2026dextacwam) and [MuSe](methods.md#paper-clark2026muse) raise the question of acquiring new sensory dynamics while retaining earlier competence. [WorldSample](methods.md#paper-xue2026worldsample), [REGEN](methods.md#paper-govind2026regen) and online-model planning raise the question of how the policy’s evolving experience changes prediction and learning. These directions connect through the consumer and returned feedback, rather than through a single architecture family.

**Make frontier evidence readable**

The [frontier atlas](chapters/13-frontier-atlas.md) locates emerging systems by mechanism and reported evidence; the [research agenda](chapters/15-research-agenda.md) turns unresolved boundaries into questions. Read them together. Frozen-model adaptation, open-loop execution, policy context and artifact availability should remain visible when interpreting a new paper. A new interface or release can motivate research without supplying a replicated cross-paper superiority claim.

**What would establish usefulness?**

Use the [evaluation guide](evaluation.md) to turn a direction into measurable model behavior, policy effect and deployment behavior. Utility curves, optimism-gap analyses and reliability margins in the survey are proposed analytical constructs whose interpretation depends on actual measurements and a declared protocol. The useful endpoint of the reading chain is a comparison that could change the conclusion, not merely a longer list of new methods.

**Where the argument goes next.** Return to [foundations](#track-foundations) to state the consumer and to [resources](#track-resources) to identify the artifact needed for the proposed test.

**Survey connections:** [13. Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md) · [15. Open Challenges and Future Directions](chapters/15-research-agenda.md) · [11. Evaluation: From Prediction Metrics to Closed-Loop Utility](chapters/11-evaluation.md) · [14. From Interaction to Model Improvement](chapters/14-interaction-learning.md).

[Browse this route’s cited works →](paper-index.md#track-frontiers)
