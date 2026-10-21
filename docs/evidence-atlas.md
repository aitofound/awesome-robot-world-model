# Evidence atlas

[Home](../README.md) · [Reading map](reading-map.md)

Representative frontier evidence atlas. P and S denote primary and secondary fields. Citations identify the works; locators specify the source version where needed. Source labels describe the consulted documents rather than later publication status. Each claim should be read together with its locator and limit; evidence level is not a ranking of model quality.

*Source: Supplementary Material S2, 27 records.*

## Evidence levels

- **E0**: an unverified lead.
- **E1**: inspectable descriptive or synthesis evidence.
- **E2**: a controlled empirical comparison.
- **E3**: empirical evaluation of an implemented feedback-coupled system.
- **E4**: evidence extended across independent evaluations or multiple sites, with the form of validation stated.

P denotes the primary pathway relevant to the claim of a row and S a secondary one. A record whose evidence stops at the model, such as open-loop generation or replay, is labeled model only. A policy baseline, benchmark or explicit constraint layer without a demonstrated world-model component is labeled a comparator.

E3 can concern simulated or physical execution and does not, by itself, isolate the contribution of a world model. The labels summarize the evidence attached to a claim; they define no ranking of model quality.

## Records

| Work | Pathway (P / S) | Loop location | Level | Scope |
|---|---|---|---|---|
| [OpenVLA](#paper-openvla2024) | Comparator (policy) / – | Learning | E3 | Real-robot closed loop |
| [RoboDreamer](#paper-robodreamer2024) | Decisions / – | Decision | E3 | Simulation closed loop |
| [DexMimicGen](#paper-dexmimicgen) | Experience / – | Learning | E3 | Real-robot closed loop |
| [Robotic World Model](#paper-li2025roboticworldmodel) | Experience / – | Learning | E3 | Real-robot closed loop |
| [WorldPlanner](#paper-worldplanner2025) | Decisions / – | Decision | E3 | Real-robot closed loop |
| [WorldEval](#paper-worldeval2025) | Scores / – | Decision | E2 | Paired simulated / real policy evaluation |
| [Towards Safe Robot Foundation Models](#paper-saferobotfoundation2025) | Comparator (safety layer) / – | Deployment | E3 | Real-robot closed loop |
| [World-in-World](#paper-worldinworld2025) | Comparator (benchmark) / – | Decision | E3 | Simulation closed loop |
| [Interactive World Simulator](#paper-interactiveworldsim2026) | Experience / Scores | Learning | E3 | Real-robot closed loop |
| [SimFoundry](#paper-ranawaka2026simfoundry) | Experience / – | Learning | E3 | Author-run real-robot closed loop |
| [PointWorld](#paper-pointworld2026) | Decisions / – | Decision | E2 | Open-loop real-robot execution |
| [TrAct](#paper-cao2026tract) | Decisions / – | Decision | E3 | Real-robot closed loop |
| [Hydra-0](#paper-hydra02026) | Model only / Scores | Model | E2 | Open-loop replay |
| [Masked Visual Actions](#paper-alzayer2026maskedvisual) | Decisions / – | Decision | E2 | Offline downstream evaluation |
| [Cosmos 3](#paper-nvidia2026cosmos3) | Model only / – | Model | E2 | Offline downstream evaluation |
| [V-JEPA 2](#paper-assran2025vjepa2) | Decisions / – | Decision | E3 | Multi-site / field evaluation |
| [DreamGen](#paper-jang2025dreamgen) | Experience / – | Learning | E3 | Real-robot closed loop |
| [DreamZero](#paper-ye2026dreamzero) | Decisions / – | Decision | E3 | Real-robot closed loop |
| [Flex-π](#paper-yan2026flexpi) | Decisions / – | Decision | E3 | Author-run real-robot closed loop |
| [EgoWAM](#paper-egowam2026) | Features / – | Learning | E3 | Real-robot closed loop |
| [Puffin-World](#paper-liao2026puffinworld) | Model only / – | Model | E2 | Open-loop generation |
| [SolarWM](#paper-huang2026solarwm) | Model only / – | Model | E1 | Open-loop generation |
| [PERSIST](#paper-garcin2026persist) | Model only / – | Model | E2 | Open-loop generation |
| [VLAW](#paper-vlaw2026) | Experience / – | Learning | E3 | Real-robot closed loop |
| [VLA-RFT](#paper-vlarft2025) | Experience / Scores | Learning | E3 | Simulation closed loop |
| [VT-WAM](#paper-tian2026vtwam) | Decisions / – | Decision | E3 | Real-robot closed loop |
| [RoboArena](#paper-atreya2025roboarena) | Comparator (benchmark) / – | Deployment | E4 | Multi-site / field evaluation |

<a id="paper-openvla2024"></a>

### OpenVLA

**OpenVLA**: [An open-source vision-language-action model](<https://arxiv.org/abs/2406.09246>) · arXiv 2024 · [Code](<https://github.com/openvla/openvla>) · [ⓘ](catalog.md#paper-openvla2024)

- **Pathway:** P: Comparator (policy); S: –; loop location: Learning.
- **Regime / mechanism:** P: Imitation learning; S: Cross-embodiment transfer.
- **Source / object:** Preprint version; Model.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** OpenVLA provides an open 7B VLA baseline trained on the Open X-Embodiment mixture and reports higher author-run success than RT-2-X.
- **Source locator (cited work):** arXiv v3, Tables 4–6; Appendix D.1, Table 9.
- **Limit:** Action-policy evidence; no explicit dynamics or consequence model.

<a id="paper-robodreamer2024"></a>

### RoboDreamer

**RoboDreamer**: [Learning Compositional World Models for Robot Imagination](<https://arxiv.org/abs/2404.12377>) · 2024 · [ⓘ](catalog.md#paper-robodreamer2024)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; compositional conditioning.
- **Source / object:** Preprint version; Model.
- **Level / scope:** E3; Simulation closed loop.
- **Claim:** RoboDreamer generates compositional video plans for unseen instructions and periodically replans during RLBench execution.
- **Source locator (cited work):** arXiv v1, Secs. 2.2, 4.1–4.2; Table 3.
- **Limit:** Robot execution is evaluated in simulation; real-robot datasets support video-generation evaluation, not physical closed-loop deployment.

<a id="paper-dexmimicgen"></a>

### DexMimicGen

**DexMimicGen**: [Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](<https://arxiv.org/abs/2410.24185>) · 2024 · [Code](<https://github.com/NVlabs/dexmimicgen>) · [ⓘ](catalog.md#paper-dexmimicgen)

- **Pathway:** P: Experience; S: –; loop location: Learning.
- **Regime / mechanism:** P: Imitation learning; S: Synthetic demonstrations; sim-to-real transfer.
- **Source / object:** Preprint version; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** DexMimicGen extends object-centric demonstration transformation to bimanual and dexterous manipulation.
- **Source locator (cited work):** arXiv v2, Sec. IV; Sec. VI-D; Fig. 6.
- **Limit:** Assumes observable reference-object poses before contact and may inherit simulator or source-strategy bias.

<a id="paper-li2025roboticworldmodel"></a>

### Robotic World Model

**RWM**: [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](<https://arxiv.org/abs/2501.10100>) · 2025 · [ⓘ](catalog.md#paper-li2025roboticworldmodel)

- **Pathway:** P: Experience; S: –; loop location: Learning.
- **Regime / mechanism:** P: Online model-based RL; S: Sim-to-real transfer; supervised model fitting.
- **Source / object:** Preprint; Model.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** RWM combines dual-autoregressive dynamics learning with MBPO-PPO and deploys the resulting policies zero-shot on ANYmal D and Unitree G1.
- **Source locator (cited work):** arXiv v5, Sec. 4.4; Fig. 5; Table 1; hardware results in Fig. 1.
- **Limit:** Velocity-tracking evidence; not a general manipulation result.

<a id="paper-worldplanner2025"></a>

### WorldPlanner

**WorldPlanner**: [Monte carlo tree search and mpc with action-conditioned visual world models](<https://arxiv.org/abs/2511.03077>) · arXiv 2025 · [ⓘ](catalog.md#paper-worldplanner2025)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Planning-time control; S: MCTS / MPC; supervised model fitting.
- **Source / object:** Preprint; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** WorldPlanner combines an action-conditioned visual model, diffusion action sampler, reward model, and MCTS planning followed by MPC tracking.
- **Source locator (cited work):** arXiv v1, Secs. III-E–III-F, IV-F; Fig. 1.
- **Limit:** Bounded by the play-data distribution, tested horizons, latency, and possible model exploitation.

<a id="paper-worldeval2025"></a>

### WorldEval

**WorldEval**: [World Model as Real-World Robot Policies Evaluator](<https://arxiv.org/abs/2505.19017>) · arXiv 2025 · [ⓘ](catalog.md#paper-worldeval2025)

- **Pathway:** P: Scores; S: –; loop location: Decision.
- **Regime / mechanism:** P: Evaluation protocol; S: Policy ranking; supervised model fitting.
- **Source / object:** Preprint; Method.
- **Level / scope:** E2; Paired simulated / real policy evaluation.
- **Claim:** WorldEval conditions video generation on Policy2Vec embeddings and compares generated-video policy rankings with paired real outcomes.
- **Source locator (cited work):** Secs. 3.2–3.3, 4.1–4.3; Tables 1–2.
- **Limit:** Paired ranking evidence; no demonstrated gain from using the evaluator to select or update a deployed policy.

<a id="paper-saferobotfoundation2025"></a>

### Towards Safe Robot Foundation Models

[Towards Safe Robot Foundation Models](<https://arxiv.org/abs/2503.07404>) · 2025 · [ⓘ](catalog.md#paper-saferobotfoundation2025)

- **Pathway:** P: Comparator (safety layer); S: –; loop location: Deployment.
- **Regime / mechanism:** P: Imitation learning; S: Execution constraints; closed-loop evaluation.
- **Source / object:** Preprint; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** An ATACOM-based post-policy layer constrains generalist-policy actions and prevents collisions in an air-hockey evaluation.
- **Source locator (cited work):** Secs. II–III; Figs. 1–2.
- **Limit:** Physical air-hockey evidence under specified dynamics and constraints; no learned world-model contribution is isolated.

<a id="paper-worldinworld2025"></a>

### World-in-World

**World-in-World**: [World models in a closed-loop world](<https://arxiv.org/abs/2510.18135>) · ICLR 2026 · [ⓘ](catalog.md#paper-worldinworld2025)

- **Pathway:** P: Comparator (benchmark); S: –; loop location: Decision.
- **Regime / mechanism:** P: Evaluation protocol; S: Closed-loop planning; MCTS.
- **Source / object:** Peer-reviewed paper; Benchmark.
- **Level / scope:** E3; Simulation closed loop.
- **Claim:** World-in-World evaluates generative models through four closed-loop embodied tasks and separates decision utility from visual quality.
- **Source locator (cited work):** Fig. 1; main tables; controllability, post-training, and inference-compute ablations.
- **Limit:** Closed-loop benchmark environments rather than real-robot deployment.

<a id="paper-interactiveworldsim2026"></a>

### Interactive World Simulator

**IWS**: [Interactive World Simulator for Robot Policy Training and Evaluation](<https://arxiv.org/abs/2603.08546>) · 2026 · [ⓘ](catalog.md#paper-interactiveworldsim2026)

- **Pathway:** P: Experience; S: Scores; loop location: Learning.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; downstream data generation / evaluation.
- **Source / object:** Preprint version; Simulator.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** Interactive World Simulator reports stable interaction beyond 10 minutes at 15 FPS and relates generated-data and simulated-ranking results to real policies.
- **Source locator (cited work):** arXiv v1, Secs. IV-B–IV-D; Figs. 4–7.
- **Limit:** Author-run tasks and hardware; correlation may not transfer to novel sensors, policies, or contacts.

<a id="paper-ranawaka2026simfoundry"></a>

### SimFoundry

**SimFoundry**: [Modular and Automated Scene Generation for Policy Learning and Evaluation](<https://arxiv.org/abs/2606.28276>) · 2026 · [ⓘ](catalog.md#paper-ranawaka2026simfoundry)

- **Pathway:** P: Experience; S: –; loop location: Learning.
- **Regime / mechanism:** P: Imitation learning; S: Synthetic demonstrations; sim-to-real evaluation.
- **Source / object:** Preprint; System.
- **Level / scope:** E3; Author-run real-robot closed loop.
- **Claim:** Reconstructed twins and generated cousins support policy training and evaluation. Simulated versus physical success yields mean Pearson r=0.911 and MMRV =0.018 across seven tasks and five policy types.
- **Source locator (cited work):** arXiv v4, Secs. 4, 5.1–5.2; Appendix B (FAQ); Table G.1.
- **Limit:** Experiments include minutes of manual scene tuning; agreement covers the evaluated task–policy pairs, without establishing absolute calibration.

<a id="paper-pointworld2026"></a>

### PointWorld

**PointWorld**: [Scaling 3d world models for in-the-wild robotic manipulation](<https://arxiv.org/abs/2601.03782>) · arXiv 2026 · [ⓘ](catalog.md#paper-pointworld2026)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Planning-time control; S: Trajectory optimization; supervised model fitting.
- **Source / object:** Preprint version; Model.
- **Level / scope:** E2; Open-loop real-robot execution.
- **Claim:** PointWorld predicts full-scene 3D point flow and uses MPPI to optimize Franka trajectories without task-specific demonstrations or post-training.
- **Source locator (cited work):** arXiv v1, Secs. 3.2, 5.4; Appendix A.6.1–A.6.3.
- **Limit:** Eight tasks, ten initial configurations each; manually specified spatial goals. Experiments do not replan online; model inference time excludes the full planning cost.

<a id="paper-cao2026tract"></a>

### TrAct

**TrAct**: [Bridging Robot Control and Visual Prediction with Visual Tracks](<https://arxiv.org/abs/2608.24101>) · 2026 · [ⓘ](catalog.md#paper-cao2026tract)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Planning-time control; S: Candidate selection; imitation learning.
- **Source / object:** Preprint; System.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** Track-conditioned candidate selection reaches 76% success on Franka, versus 66% for action-conditioned selection with the same action–track proposal policy.
- **Source locator (cited work):** arXiv v3, Secs. 3.3, 5.4; Table 4; Appendix A, Algorithm 1.
- **Limit:** Five tasks under two backgrounds, with ten trials per condition; author-run hardware evaluation.

<a id="paper-hydra02026"></a>

### Hydra-0

**Hydra-0**: [Action Flow for Generalist World Modeling and Control](<https://arxiv.org/abs/2608.18077>) · 2026 · [ⓘ](catalog.md#paper-hydra02026)

- **Pathway:** P: Model only; S: Scores; loop location: Model.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; recorded replay.
- **Source / object:** Preprint; Model.
- **Level / scope:** E2; Open-loop replay.
- **Claim:** Action-flow conditioning preserves recorded-trajectory outcomes in RoboLab video replay; desired object flow also conditions inverse motion prediction.
- **Source locator (cited work):** Secs. 2.4, 4.5–4.6; Table 2; Figs. 7–9.
- **Limit:** Quantitative evaluation fixes recorded motion before generation; real inverse execution is a qualitative example.

<a id="paper-alzayer2026maskedvisual"></a>

### Masked Visual Actions

**Masked Visual Actions**: [Masked Visual Actions for Unified World Modeling](<https://arxiv.org/abs/2607.19343>) · arXiv 2026 · [ⓘ](catalog.md#paper-alzayer2026maskedvisual)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Planning-time control; S: Candidate selection; supervised model fitting.
- **Source / object:** Preprint; Method.
- **Level / scope:** E2; Offline downstream evaluation.
- **Claim:** Masked visual actions support RoboCasa candidate selection and inverse action extraction; physical-data tests compare predicted progress with recorded demonstrations.
- **Source locator (cited work):** Sec. 5.2; Figs. 8–11.
- **Limit:** Planning and inverse-policy tests use RoboCasa; physical evidence replays recorded demonstrations and retains optimistic progress bias.

<a id="paper-nvidia2026cosmos3"></a>

### Cosmos 3

**Cosmos 3**: [Omnimodal World Models for Physical AI](<https://arxiv.org/abs/2606.02800>) · arXiv 2026 · [ⓘ](catalog.md#paper-nvidia2026cosmos3)

- **Pathway:** P: Model only; S: –; loop location: Model.
- **Regime / mechanism:** P: Model fitting; S: Self-supervised pretraining; supervised prediction.
- **Source / object:** Technical report; Model.
- **Level / scope:** E2; Offline downstream evaluation.
- **Claim:** Cosmos 3 describes one mixture-of-transformers family for language, image, video, audio, and action input–output configurations.
- **Source locator (cited work):** Technical-report abstract; architecture figure; modality and WAM evaluation sections.
- **Limit:** Broad technical-report evidence; robot claims remain model- and task-specific.

<a id="paper-assran2025vjepa2"></a>

### V-JEPA 2

**V-JEPA 2-AC**: [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](<https://arxiv.org/abs/2506.09985>) · arXiv 2025 · [Code](<https://github.com/facebookresearch/vjepa2>) · [ⓘ](catalog.md#paper-assran2025vjepa2)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Planning-time control; S: MPC; self-supervised pretraining.
- **Source / object:** Preprint; Model.
- **Level / scope:** E3; Multi-site / field evaluation.
- **Claim:** V-JEPA 2 post-trains an action-conditioned latent model on under 62 hours of DROID video and deploys image-goal planning in two labs.
- **Source locator (cited work):** Fig. 1; V-JEPA 2-AC section; two-lab result tables.
- **Limit:** Franka image-goal evaluation; not general action prediction or arbitrary embodiment transfer.

<a id="paper-jang2025dreamgen"></a>

### DreamGen

**DreamGen**: [Unlocking Generalization in Robot Learning through Video World Models](<https://arxiv.org/abs/2505.12705>) · CoRL 2025 · [Code](<https://github.com/NVIDIA/GR00T-dreams>) · [ⓘ](catalog.md#paper-jang2025dreamgen)

- **Pathway:** P: Experience; S: –; loop location: Learning.
- **Regime / mechanism:** P: Imitation learning; S: Synthetic demonstrations; embodiment transfer.
- **Source / object:** Peer-reviewed paper; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** DreamGen generates video trajectories and recovers pseudo-actions, reporting 22 new humanoid behaviors from one teleoperated task.
- **Source locator (cited work):** arXiv v1, Secs. 2–4; behavior-generalization results in Sec. 3.2.
- **Limit:** Selected GR1 tasks and environments; video fidelity alone is not the downstream claim.

<a id="paper-ye2026dreamzero"></a>

### DreamZero

**DreamZero**: [World Action Models are Zero-shot Policies](<https://arxiv.org/abs/2602.15922>) · arXiv 2026 · [ⓘ](catalog.md#paper-ye2026dreamzero)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Imitation learning; S: Joint video/action modeling; embodiment transfer.
- **Source / object:** Preprint; Model.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** DreamZero jointly predicts video and actions with a 14B WAM, reporting more than 2× generalization gains and 7 Hz closed-loop execution.
- **Source locator (cited work):** Abstract; unseen-task and environment tables; latency table; cross-embodiment experiments.
- **Limit:** Author-reported robots, tasks, baselines, and data budgets; not universal zero-shot control.

<a id="paper-yan2026flexpi"></a>

### Flex-π

**Flex-π**: [A Multi-Stream World-Action Model with Compute Flexibility](<https://arxiv.org/abs/2608.10860>) · 2026 · [ⓘ](catalog.md#paper-yan2026flexpi)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Imitation learning; S: Joint predictive training; action-only/joint inference.
- **Source / object:** Preprint; Model.
- **Level / scope:** E3; Author-run real-robot closed loop.
- **Claim:** Each task's fine-tuned checkpoint supports action-only or full-joint generation on bimanual YAM, refreshing observations between action chunks. Joint generation improves the reported average partial-credit completion score at additional compute cost.
- **Source locator (cited work):** arXiv v3, Secs. 3.2, 4.2, 4.5; Appendices C, F.2, G.1.
- **Limit:** Five tasks; 20 trials per task except Sort Utensils (10). Results depend on inference mode and task protocol; baseline task coverage differs.

<a id="paper-egowam2026"></a>

### EgoWAM

**EgoWAM**: [World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](<https://arxiv.org/abs/2607.08436>) · arXiv 2026 · [ⓘ](catalog.md#paper-egowam2026)

- **Pathway:** P: Features; S: –; loop location: Learning.
- **Regime / mechanism:** P: Imitation learning; S: Human–robot co-training; predictive supervision.
- **Source / object:** Preprint; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** EgoWAM compares pixel, DINO, and 3D-motion-flow prediction targets under a matched human–robot co-training pipeline.
- **Source locator (cited work):** Secs. 3.2, 4.3; Fig. 1; matched target and bimanual task comparisons.
- **Limit:** Three-task study; the world head supplies training supervision and is removed at inference.

<a id="paper-liao2026puffinworld"></a>

### Puffin-World

**Puffin-World**: [Scaling a Unified Multimodal Model with Native 3D World States](<https://arxiv.org/abs/2609.04196>) · 2026 · [ⓘ](catalog.md#paper-liao2026puffinworld)

- **Pathway:** P: Model only; S: –; loop location: Model.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; multi-task training.
- **Source / object:** Preprint; Model.
- **Level / scope:** E2; Open-loop generation.
- **Claim:** Predicts camera orientation and jointly generates RGB-D views for 3D reconstruction, with controlled camera and geometry benchmarks.
- **Source locator (cited work):** Secs. 3.1–3.2, 5.2–5.6.
- **Limit:** Camera-view generation and reconstruction; the self-calibration loop adjusts generated views, not a physical robot. No robot-policy or contact-force evaluation.

<a id="paper-huang2026solarwm"></a>

### SolarWM

**SolarWM**: [Open Data and Scalable Training for Long-Horizon Video World Models](<https://arxiv.org/abs/2609.02886>) · 2026 · [ⓘ](catalog.md#paper-huang2026solarwm)

- **Pathway:** P: Model only; S: –; loop location: Model.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; distillation.
- **Source / object:** Preprint; System.
- **Level / scope:** E1; Open-loop generation.
- **Claim:** Unifies data preparation and backbone adaptation; its 5B causal student demonstrates a 60-minute camera-conditioned rollout after five-second-sequence training.
- **Source locator (cited work):** Secs. 4–7; Fig. 11.
- **Limit:** Long-horizon evidence is qualitative, with prescribed cameras and fixed prompts; no measured robot-policy gains.

<a id="paper-garcin2026persist"></a>

### PERSIST

**PERSIST**: [Beyond Pixel Histories: World Models with Persistent 3D State](<https://arxiv.org/abs/2603.03482>) · arXiv 2026 · [ⓘ](catalog.md#paper-garcin2026persist)

- **Pathway:** P: Model only; S: –; loop location: Model.
- **Regime / mechanism:** P: Model fitting; S: Supervised prediction; persistent scene state.
- **Source / object:** Preprint version; Model.
- **Level / scope:** E2; Open-loop generation.
- **Claim:** PERSIST maintains a latent 3D scene state to improve spatial memory and long-horizon consistency over pixel-history baselines.
- **Source locator (cited work):** arXiv v2, Secs. 4, 6.1; Tables 1–2; Appendices B–C.
- **Limit:** Generated environments; no downstream robot-policy or contact evidence.

<a id="paper-vlaw2026"></a>

### VLAW

**VLAW**: [Iterative Co-Improvement of Vision-Language-Action Policy and World Model](<https://arxiv.org/abs/2602.12063>) · arXiv 2026 · [ⓘ](catalog.md#paper-vlaw2026)

- **Pathway:** P: Experience; S: –; loop location: Learning.
- **Regime / mechanism:** P: Supervised policy updating; S: Filtered real/synthetic rollouts; policy–model updating.
- **Source / object:** Preprint; Method.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** VLAW alternates real rollouts for model improvement with weighted flow-matching policy updates on successful real and synthetic trajectories.
- **Source locator (cited work):** Sec. 4.2, Eq. (4), Algorithm 1; synthetic-rollout ablation.
- **Limit:** The regularized-RL interpretation does not make the implemented update a policy-gradient method; isolate synthetic-data gains.

<a id="paper-vlarft2025"></a>

### VLA-RFT

**VLA-RFT**: [Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators](<https://arxiv.org/abs/2510.00406>) · arXiv 2025 · [ⓘ](catalog.md#paper-vlarft2025)

- **Pathway:** P: Experience; S: Scores; loop location: Learning.
- **Regime / mechanism:** P: Offline model-based RL; S: GRPO fine-tuning; synthetic rollouts.
- **Source / object:** Preprint; Method.
- **Level / scope:** E3; Simulation closed loop.
- **Claim:** VLA-RFT fine-tunes a VLA through action-conditioned learned-simulator rollouts with trajectory rewards computed from predicted states.
- **Source locator (cited work):** Sec. 3.3, Eq. (13); Secs. 4.1–4.3; Tables 2–3.
- **Limit:** Simulation evidence; reward verification here does not establish real-outcome validity or immunity to simulator exploitation.

<a id="paper-tian2026vtwam"></a>

### VT-WAM

**VT-WAM**: [Visual-Tactile World Action Model for Contact-Rich Manipulation](<https://arxiv.org/abs/2607.02503>) · arXiv 2026 · [ⓘ](catalog.md#paper-tian2026vtwam)

- **Pathway:** P: Decisions; S: –; loop location: Decision.
- **Regime / mechanism:** P: Imitation learning; S: Joint tactile/video/action prediction.
- **Source / object:** Preprint; Model.
- **Level / scope:** E3; Real-robot closed loop.
- **Claim:** VT-WAM jointly predicts future vision, tactile deformation, and actions, reporting 71.67% average success across six real tasks.
- **Source locator (cited work):** arXiv v1, Fig. 2; Secs. IV-C–IV-D, Tables I–III.
- **Limit:** Author-run hardware and sensors; cross-sensor and cross-object transfer remain bounded.

<a id="paper-atreya2025roboarena"></a>

### RoboArena

**RoboArena**: [Distributed Real-World Evaluation of Generalist Robot Policies](<https://arxiv.org/abs/2506.18123>) · arXiv 2025 · [ⓘ](catalog.md#paper-atreya2025roboarena)

- **Pathway:** P: Comparator (benchmark); S: –; loop location: Deployment.
- **Regime / mechanism:** P: Evaluation protocol; S: Distributed real-robot comparison.
- **Source / object:** Preprint version; Benchmark.
- **Level / scope:** E4; Multi-site / field evaluation.
- **Claim:** RoboArena aggregates distributed, pairwise double-blind real-robot comparisons over a DROID evaluator network.
- **Source locator (cited work):** Fig. 1; distributed protocol; ranking and reliability tables.
- **Limit:** Coverage depends on participating sites, policies, resets, and tasks; the ranking is not universal capability.
