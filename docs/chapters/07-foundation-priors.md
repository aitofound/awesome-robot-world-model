# 07. Foundation-Driven World Models and Robot Priors

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Foundation encoders, VLA proposals, imagination, neural simulation, rewards and constraint layers have distinct interfaces. Neural simulation can supply demonstrations, filtered BC data, policy optimization or evaluation.

## Reading questions

- How are foundation priors adapted to robot actions?
- What generated experience is selected or labeled?
- What independent physical evidence supports utility?

## Interpretation boundary

Include adaptation, judging, resets and rejected samples in cost comparisons. A foundation policy alone is not a world model.

## Selected annotations

- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [PointWorld](../methods.md#paper-pointworld2026)
- [PhysTwin](../methods.md#paper-jiang2025phystwin)
- [WorldPlanner](../methods.md#paper-worldplanner2025)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [RoboDreamer](../methods.md#paper-robodreamer2024)
- [Robotic World Model (RWM)](../methods.md#paper-li2025roboticworldmodel)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [Hi-WM](../methods.md#paper-li2026hiwm)
- [GE-Sim 2.0](../methods.md#paper-qiu2026gesim2)
- [GeniWorld](../methods.md#paper-gu2026geniworld)
- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [DreamDojo](../methods.md#paper-gao2026dreamdojo)
- [WoVR](../methods.md#paper-nsim-wovr)
- [RoboWorld](../methods.md#paper-nsim-roboworld)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [VLA-RFT](../methods.md#paper-vlarft2025)
- [World-Gymnast](../methods.md#paper-worldgymnast2026)
- [Cosmos](../methods.md#paper-nvidia2025cosmos)
- [Cosmos 3](../methods.md#paper-nvidia2026cosmos3)
- [Manipulation by Feel](../methods.md#paper-tian2019manipulation)
- [RoboPack](../methods.md#paper-ai2024robopack)
- [ContactWorld](../methods.md#paper-zhang2026contactworld)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [VT-WAM](../methods.md#paper-tian2026vtwam)
- [Tactile-WAM](../methods.md#paper-wu2026tactilewam)
- [VLAW](../methods.md#paper-vlaw2026)
- [WorldSample](../methods.md#paper-xue2026worldsample)
- [World-in-World](../methods.md#paper-worldinworld2025)
- [SafeDreamer](../methods.md#paper-huang2024safedreamer)
- [OpenVLA](../methods.md#paper-openvla2024)
- [pi0](../methods.md#paper-pi0)
- [GR00T N1.7](../methods.md#paper-nvidia2026groot17)

## References by argument (111 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-034"></a>

### Why Foundation Priors Change World Modeling

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2023 | [Rt-2: Vision-language-action models transfer web knowledge to robotic control](../catalog.md#paper-rt2) | [Paper](<https://arxiv.org/abs/2307.15818>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](../catalog.md#paper-vlareview2025) | [Paper](<https://arxiv.org/abs/2510.07077>) |
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [ForceDelta-VLA: Distilling Force-Conditioned ActionCorrections for Contact-Rich Manipulation](../catalog.md#paper-dong2026forcedelta) | [Paper](<https://arxiv.org/abs/2609.18242>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |

<a id="argument-035"></a>

### Representation Priors: State Abstractions for Control

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Omnidexvlg: Learning dexterous grasp generation from vision language model-guided grasp semantics, taxonomy and functional affordance](../catalog.md#paper-zhang2025omnidexvlg) | [Paper](<https://arxiv.org/abs/2512.03874>) |
| 2022 | [R3m: A universal visual representation for robot manipulation](../catalog.md#paper-nair2022r3m) | [Paper](<https://arxiv.org/abs/2203.12601>) |
| 2023 | [Where are we in the search for an artificial visual cortex for embodied intelligence?](../catalog.md#paper-majumdar2023we) | Source metadata only |
| 2023 | [Rt-2: Vision-language-action models transfer web knowledge to robotic control](../catalog.md#paper-rt2) | [Paper](<https://arxiv.org/abs/2307.15818>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |

<a id="argument-036"></a>

### Open VLA Action Priors

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](../catalog.md#paper-vlareview2025) | [Paper](<https://arxiv.org/abs/2510.07077>) |
| 2025 | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](../catalog.md#paper-pi2025pi05) | [Paper](<https://arxiv.org/abs/2504.16054>) |
| 2025 | [π^\*_0.6: a VLA That Learns From Experience](../catalog.md#paper-pi2025pistar06) | [Paper](<https://arxiv.org/abs/2511.14759>) |
| 2026 | [π_0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../catalog.md#paper-pi2026pi07) | [Paper](<https://arxiv.org/abs/2604.15483>) |
| 2026 | [NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots](../catalog.md#paper-nvidia2026groot17) | [Paper](<https://huggingface.co/blog/nvidia/gr00t-n1-7>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2026 | [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](../catalog.md#paper-cao2026tract) | [Paper](<https://arxiv.org/abs/2608.24101>) |
| 2026 | [Hydra-0: Action Flow for Generalist World Modeling and Control](../catalog.md#paper-hydra02026) | [Paper](<https://arxiv.org/abs/2608.18077>) |
| 2026 | [Masked Visual Actions for Unified World Modeling](../catalog.md#paper-alzayer2026maskedvisual) | [Paper](<https://arxiv.org/abs/2607.19343>) |

<a id="argument-037"></a>

### Imagination and Generative Priors

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [This&amp;That: Language-Gesture Controlled Video Generation for Robot Planning](../catalog.md#paper-wang2025thisandthat) | [Paper](<https://arxiv.org/abs/2407.05530>) |
| 2025 | [TesserAct: Learning 4D Embodied World Models](../catalog.md#paper-zhen2025tesseract) | [Paper](<https://arxiv.org/abs/2504.20995>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-038"></a>

### Neural Simulators as Training Environments

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2026 | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../catalog.md#paper-gao2026dreamdojo) | [Paper](<https://arxiv.org/abs/2602.06949>) |
| 2026 | [GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions](../catalog.md#paper-gu2026geniworld) | [Paper](<https://arxiv.org/abs/2608.06332>) |
| 2026 | [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](../catalog.md#paper-qiu2026gesim2) | [Paper](<https://arxiv.org/abs/2605.27491>) |
| 2026 | [Atlas: A World Model for Spatial Intelligence](../catalog.md#paper-worldlabs2026atlas) | [Paper](<https://www.worldlabs.ai/blog/atlas>) |
| 2026 | [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](../catalog.md#paper-ranawaka2026simfoundry) | [Paper](<https://arxiv.org/abs/2606.28276>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2026 | [Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](../catalog.md#paper-li2026hiwm) | [Paper](<https://arxiv.org/abs/2604.21741>) |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](../catalog.md#paper-nsim-rwmu) | [Paper](<https://arxiv.org/abs/2504.16680>) |
| 2026 | [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](../catalog.md#paper-nsim-wovr) | [Paper](<https://arxiv.org/abs/2602.13977>) |
| 2026 | [RISE: Self-Improving Robot Policy with Compositional World Model](../catalog.md#paper-nsim-rise) | [Paper](<https://arxiv.org/abs/2602.11075>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |
| 2026 | [RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](../catalog.md#paper-nsim-roboworld) | [Paper](<https://arxiv.org/abs/2607.01060>) |
| 2025 | [Evaluating Gemini Robotics Policies in a Veo World Simulator](../catalog.md#paper-nsim-veo) | [Paper](<https://arxiv.org/abs/2512.10675>) |
| 2026 | [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](../catalog.md#paper-chen2026worldsync) | [Paper](<https://arxiv.org/abs/2608.24885>) |
| 2026 | [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](../catalog.md#paper-nsim-memworld) | [Paper](<https://arxiv.org/abs/2606.18960>) |
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2026 | [World-gymnast: Training robots with reinforcement learning in a world model](../catalog.md#paper-worldgymnast2026) | [Paper](<https://arxiv.org/abs/2602.02454>) |
| 2026 | [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](../catalog.md#paper-nsim-wise) | [Paper](<https://arxiv.org/abs/2609.03681>) |

<a id="argument-039"></a>

### Omnimodal World Foundation Models as Interface Consolidation

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Cosmos 3: Omnimodal World Models for Physical AI](../catalog.md#paper-nvidia2026cosmos3) | [Paper](<https://arxiv.org/abs/2606.02800>) |
| 2026 | [WALL-WM: Carving World Action Modeling at the Event Joints](../catalog.md#paper-xsquare2026wallwm) | [Paper](<https://arxiv.org/abs/2606.01955>) |
| 2026 | [RoboOmni: Proactive Robot Manipulation in Omni-modal Context](../catalog.md#paper-wang2026roboomni) | [Paper](<https://arxiv.org/abs/2510.23763>) |
| 2026 | [Atlas: A World Model for Spatial Intelligence](../catalog.md#paper-worldlabs2026atlas) | [Paper](<https://www.worldlabs.ai/blog/atlas>) |
| 2026 | [Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States](../catalog.md#paper-liao2026puffinworld) | [Paper](<https://arxiv.org/abs/2609.04196>) |
| 2026 | [Flex-π: A Multi-Stream World-Action Model with Compute Flexibility](../catalog.md#paper-yan2026flexpi) | [Paper](<https://arxiv.org/abs/2608.10860>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2025 | [Genie 3: A New Frontier for World Models](../catalog.md#paper-deepmind2025genie3) | [Paper](<https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>) |
| 2024 | [Oasis: A Universe in a Transformer](../catalog.md#paper-decart2024oasis) | [Paper](<https://oasis-model.github.io/>) |
| 2026 | [Introducing Oasis 3: First Interactive World Model for Physical AI](../catalog.md#paper-decart2026oasis3) | [Paper](<https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai>) |

<a id="argument-040"></a>

### Critic, Reward, and Value Priors

| Year | Work | Primary entry |
|---|---|---|
| 2022 | [Vip: Towards universal visual reward and representation via value-implicit pre-training](../catalog.md#paper-ma2022vip) | [Paper](<https://arxiv.org/abs/2210.00030>) |
| 2024 | [Vision-language models for robot success detection](../catalog.md#paper-luo2024vision) | Source metadata only |
| 2024 | [Video-language critic: Transferable reward functions for language-conditioned robotics](../catalog.md#paper-alakuijala2024video) | [Paper](<https://arxiv.org/abs/2405.19988>) |
| 2024 | [GRAPE: Generalizing Robot Policy via Preference Alignment](../catalog.md#paper-grape2024) | [Paper](<https://arxiv.org/abs/2411.19309>) |
| 2025 | [ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations](../catalog.md#paper-rewind2025) | [Paper](<https://arxiv.org/abs/2505.10911>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2025 | [VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators](../catalog.md#paper-vlarft2025) | [Paper](<https://arxiv.org/abs/2510.00406>) |

<a id="argument-041"></a>

### Physical, Contact, and Tactile Priors

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Responsible and Generalizable Dexterous Manipulation through Multimodal Perception, Reasoning, and Sim2Real Learning](../catalog.md#paper-zhang2026responsible) | Source metadata only |
| 2025 | [Contactdexnet: Multi-fingered robotic hand grasping in cluttered environments through hand-object contact semantic mapping](../catalog.md#paper-zhang2025contactdexnet) | Source metadata only |
| 2019 | [Manipulation by Feel: Touch-Based Control with Deep Predictive Models](../catalog.md#paper-tian2019manipulation) | [Paper](<https://arxiv.org/abs/1903.04128>) |
| 2024 | [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../catalog.md#paper-ai2024robopack) | [Paper](<https://arxiv.org/abs/2407.01418>) |
| 2025 | [Bioinspired trajectory modulation for effective slip control in robot manipulation](../catalog.md#paper-nazari2025bioinspired) | [Paper](<https://doi.org/10.1038/s42256-025-01062-2>) |
| 2025 | [Towards reliable and damage-less robotic fragile fruit grasping: An enveloping gripper with multimodal strategy inspired by Asian elephant trunk](../catalog.md#paper-wang2025towards) | Source metadata only |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](../catalog.md#paper-ma2026feelworld) | [Paper](<https://arxiv.org/abs/2607.24267>) |
| 2026 | [ContactWorld: What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation](../catalog.md#paper-zhang2026contactworld) | [Paper](<https://arxiv.org/abs/2606.13877>) |
| 2026 | [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](../catalog.md#paper-tian2026vtwam) | [Paper](<https://arxiv.org/abs/2607.02503>) |
| 2026 | [Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention](../catalog.md#paper-wu2026tactilewam) | [Paper](<https://arxiv.org/abs/2606.26663>) |
| 2025 | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../catalog.md#paper-jiang2025phystwin) | [Paper](<https://arxiv.org/abs/2503.17973>) |
| 2025 | [Particle-grid neural dynamics for learning deformable object models from rgb-d videos](../catalog.md#paper-zhang2025particle) | [Paper](<https://arxiv.org/abs/2506.15680>) |
| 2025 | [Contactsdf: Signed distance functions as multi-contact models for dexterous manipulation](../catalog.md#paper-yang2025contactsdf) | Source metadata only |
| 2025 | [Twintrack: Bridging vision and contact physics for real-time tracking of unknown dynamic objects](../catalog.md#paper-yang2025twintrack) | Source metadata only |
| 2024 | [Difftactile: A physics-based differentiable tactile simulator for contact-rich robotic manipulation](../catalog.md#paper-si2024difftactile) | Source metadata only |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [ForceDelta-VLA: Distilling Force-Conditioned ActionCorrections for Contact-Rich Manipulation](../catalog.md#paper-dong2026forcedelta) | [Paper](<https://arxiv.org/abs/2609.18242>) |
| 2024 | [Adaptive Contact-Implicit Model Predictive Control with Online Residual Learning](../catalog.md#paper-huang2024adaptive) | [Paper](<https://arxiv.org/abs/2310.09893>) |
| 2026 | [TACO: TActile World Model as a Self-COrrector for Scalable VLA Post-Training](../catalog.md#paper-liu2026taco) | [Paper](<https://arxiv.org/abs/2607.02840>) |
| 2025 | [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../catalog.md#paper-xue2025reactive) | [Paper](<https://arxiv.org/abs/2503.02881>) |

<a id="argument-042"></a>

### Safety and Constraint Priors

| Year | Work | Primary entry |
|---|---|---|
| 2022 | [Plate: Visually-grounded planning with transformers in procedural tasks](../catalog.md#paper-sun2022plate) | Source metadata only |
| 2021 | [Adversarial inverse reinforcement learning with self-attention dynamics model](../catalog.md#paper-sun2021adversarial) | Source metadata only |
| 2022 | [The politics of autonomous vehicles](../catalog.md#paper-stilgoe2022politics) | Source metadata only |
| 2025 | [Guidelines and Recommendations for ADS Safety Requirements, Assessments and Test Methods to Inform Regulatory Development](../catalog.md#paper-unece2025ads) | [Paper](<https://unece.org/transport/publications/guidelines-and-recommendations-ads-safety-requirements-assessments-and-test>) |
| 2026 | [When physicians and AI work together, who is accountable? How to lay out medical liability](../catalog.md#paper-lam2026physicians) | Source metadata only |
| 2025 | [Mixucb: Enhancing safe exploration in contextual bandits with human oversight](../catalog.md#paper-su2025mixucb) | Source metadata only |
| 2025 | [Foundation models in robotics: Applications, challenges, and the future](../catalog.md#paper-firoozi2025foundation) | [Paper](<https://doi.org/10.1177/02783649241281508>) |
| 2025 | [A survey of reasoning with foundation models: Concepts, methodologies, and outlook](../catalog.md#paper-sun2025survey) | Source metadata only |
| 2023 | [Conformal prediction for uncertainty-aware planning with diffusion dynamics model](../catalog.md#paper-sun2023conformal) | Source metadata only |
| 2025 | [Perry: Policy evaluation with confidence intervals using auxiliary data](../catalog.md#paper-mandyam2025perry) | Source metadata only |
| 2025 | [Don't Let Your Robot be Harmful: Responsible Robotic Manipulation via Safety-as-Policy](../catalog.md#paper-ni2025don) | Source metadata only |
| 2024 | [Safedreamer: Safe reinforcement learning with world models](../catalog.md#paper-huang2024safedreamer) | [Paper](<https://arxiv.org/abs/2307.07176>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2021 | [Learning a decision module by imitating driver's control behaviors](../catalog.md#paper-huang2021learning) | Source metadata only |
| 2021 | [Neuro-symbolic program search for autonomous driving decision module design](../catalog.md#paper-sun2021neuro) | Source metadata only |
| 2024 | [ARCH: Hierarchical hybrid learning for long-horizon contact-rich robotic assembly](../catalog.md#paper-sun2024arch) | Source metadata only |
| 2023 | [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](../catalog.md#paper-mimicplay2023) | [Paper](<https://arxiv.org/abs/2302.12422>) |
| 2024 | [Diffusion-es: Gradient-free planning with diffusion for autonomous and instruction-guided driving](../catalog.md#paper-yang2024diffusion) | Source metadata only |
| 2024 | [Tractable joint prediction and planning over discrete behavior modes for urban driving](../catalog.md#paper-villaflor2024tractable) | Source metadata only |
| 2024 | [A collision-aware cable grasping method in cluttered environment](../catalog.md#paper-zhang2024collision) | Source metadata only |
| 2025 | [ParticleFormer: A 3D Point Cloud World Model for Multi-Object, Multi-Material Robotic Manipulation](../catalog.md#paper-huang2025particleformer) | [Paper](<https://arxiv.org/abs/2506.23126>) |
| 2024 | [World models: The safety perspective](../catalog.md#paper-zeng2024world) | Source metadata only |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |
| 2025 | [Emerging cyber attack risks of medical ai agents](../catalog.md#paper-qiu2025emerging) | [Paper](<https://arxiv.org/abs/2504.03759>) |
| 2026 | [Clawsbench: Evaluating capability and safety of llm productivity agents in simulated workspaces](../catalog.md#paper-li2026clawsbench) | [Paper](<https://arxiv.org/abs/2604.05172>) |
| 2025 | [Responsiblerobotbench: Benchmarking responsible robot manipulation using multi-modal large language models](../catalog.md#paper-zhang2025responsiblerobotbench) | [Paper](<https://arxiv.org/abs/2512.04308>) |

