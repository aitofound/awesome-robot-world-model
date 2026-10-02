# 06. From Roles to Policy Improvement

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Imitation, offline RL, online model-based RL, planning and transfer consume model information differently. Track real and imagined experience separately.

## Reading questions

- Is generated experience used for supervised learning or RL?
- Is the world model frozen?
- What feedback reaches the policy versus the model?

## Interpretation boundary

Synthetic trajectories alone do not establish online RL or deployment-time adaptation.

## Selected annotations

- [PlaNet](../methods.md#paper-hafner2019planet)
- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DreamerV3](../methods.md#paper-hafner2023dreamerv3)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [TD-MPC2](../methods.md#paper-hansen2024tdmpc2)
- [V-JEPA 2](../methods.md#paper-assran2025vjepa2)
- [ODEWorld](../methods.md#paper-liu2026odeworld)
- [PointWorld](../methods.md#paper-pointworld2026)
- [WorldPlanner](../methods.md#paper-worldplanner2025)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [RoboDreamer](../methods.md#paper-robodreamer2024)
- [Robotic World Model (RWM)](../methods.md#paper-li2025roboticworldmodel)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [VLA-RFT](../methods.md#paper-vlarft2025)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [VLAW](../methods.md#paper-vlaw2026)
- [WAM-RL](../methods.md#paper-wamrl2026)
- [OpenVLA](../methods.md#paper-openvla2024)
- [pi0](../methods.md#paper-pi0)

## References by argument (54 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-026"></a>

### Imitation Learning and Behavior Cloning

| Year | Work | Primary entry |
|---|---|---|
| 2022 | [RT-1: Robotics Transformer for Real-World Control at Scale](../catalog.md#paper-rt1) | [Paper](<https://arxiv.org/abs/2212.06817>) |
| 2023 | [Rt-2: Vision-language-action models transfer web knowledge to robotic control](../catalog.md#paper-rt2) | [Paper](<https://arxiv.org/abs/2307.15818>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../catalog.md#paper-dexmimicgen) | [Paper](<https://arxiv.org/abs/2410.24185>) |
| 2026 | [ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](../catalog.md#paper-liu2026odeworld) | [Paper](<https://arxiv.org/abs/2607.27924>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2026 | [RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL](../catalog.md#paper-roboscape-r) | Source metadata only |

<a id="argument-027"></a>

### Offline Reinforcement Learning

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [Uncertainty-driven Trajectory Truncation for Data Augmentation in Offline Reinforcement Learning](../catalog.md#paper-tatu) | [Paper](<https://arxiv.org/abs/2304.04660>) |
| 2020 | [MOPO: Model-based Offline Policy Optimization](../catalog.md#paper-mopo) | [Paper](<https://proceedings.neurips.cc/paper_files/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf>) |
| 2020 | [MOReL: Model-Based Offline Reinforcement Learning](../catalog.md#paper-morel) | [Paper](<https://proceedings.neurips.cc/paper_files/paper/2020/file/f7efa4f864ae9b88d43527f4b14f750f-Paper.pdf>) |
| 2021 | [COMBO: Conservative Offline Model-Based Policy Optimization](../catalog.md#paper-combo) | [Paper](<https://proceedings.neurips.cc/paper_files/paper/2021/file/f29a179746902e331572c483c45e5086-Paper.pdf>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [DiWA: Diffusion Policy Adaptation with World Models](../catalog.md#paper-diwa) | [Paper](<https://arxiv.org/abs/2508.03645>) |

<a id="argument-028"></a>

### Online Reinforcement Learning

| Year | Work | Primary entry |
|---|---|---|
| 2021 | [Learning Invariant Representations for Reinforcement Learning without Reconstruction](../catalog.md#paper-dbc) | [Paper](<https://arxiv.org/abs/2006.10742>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |

<a id="argument-029"></a>

### Planning-Time Control

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [Learning Latent Dynamics for Planning from Pixels](../catalog.md#paper-hafner2019planet) | [Paper](<https://arxiv.org/abs/1811.04551>) |
| 2024 | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../catalog.md#paper-hansen2024tdmpc2) | [Paper](<https://arxiv.org/abs/2310.16828>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2025 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../catalog.md#paper-assran2025vjepa2) | [Paper](<https://arxiv.org/abs/2506.09985>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2026 | [Masked Visual Actions for Unified World Modeling](../catalog.md#paper-alzayer2026maskedvisual) | [Paper](<https://arxiv.org/abs/2607.19343>) |
| 2026 | [τ_0-WM: A Unified Video-Action World Model for Robotic Manipulation](../catalog.md#paper-zhou2026tau0wm) | [Paper](<https://arxiv.org/abs/2606.01027>) |
| 2026 | [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](../catalog.md#paper-cao2026tract) | [Paper](<https://arxiv.org/abs/2608.24101>) |
| 2026 | [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](../catalog.md#paper-chen2026worldsync) | [Paper](<https://arxiv.org/abs/2608.24885>) |

<a id="argument-030"></a>

### Sim-to-Real and Cross-Embodiment Transfer

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](../catalog.md#paper-zhao2020simtoreal) | [Paper](<https://arxiv.org/abs/2009.13303>) |
| 2023 | [TWIST: Teacher-Student World Model Distillation for Efficient Sim-to-Real Transfer](../catalog.md#paper-twist2023) | [Paper](<https://arxiv.org/abs/2311.03622>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |

<a id="argument-031"></a>

### Robotic Policy Adaptation as a Regime

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [xTED: Cross-Domain Adaptation via Diffusion-Based Trajectory Editing](../catalog.md#paper-xted2026) | [Paper](<https://doi.org/10.65109/BENP4894>) |
| 2022 | [When to Trust Your Simulator: Dynamics-Aware Hybrid Offline-and-Online Reinforcement Learning](../catalog.md#paper-h2o2022) | Source metadata only |
| 2025 | [H2O+: An Improved Framework for Hybrid Offline-and-Online RL with Dynamics Gaps](../catalog.md#paper-h2oplus2025) | [Paper](<https://doi.org/10.1109/ICRA55743.2025.11127503>) |
| 2025 | [Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning](../catalog.md#paper-sgft2025) | Source metadata only |
| 2025 | [LocoFormer: Generalist Locomotion via Long-context Adaptation](../catalog.md#paper-locoformer2025) | Source metadata only |
| 2026 | [In-Context World Modeling for Robotic Control](../catalog.md#paper-icwm2026) | [Paper](<https://arxiv.org/abs/2606.26025>) |
| 2025 | [Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids](../catalog.md#paper-rtr2025) | Source metadata only |
| 2026 | [On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning](../catalog.md#paper-ontheflyvla2026) | [Paper](<https://doi.org/10.18653/v1/2026.acl-long.1863>) |

<a id="argument-032"></a>

### Deployment, Safety, and Human-in-the-Loop Correction

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../catalog.md#paper-dexmimicgen) | [Paper](<https://arxiv.org/abs/2410.24185>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2023 | [Rt-2: Vision-language-action models transfer web knowledge to robotic control](../catalog.md#paper-rt2) | [Paper](<https://arxiv.org/abs/2307.15818>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |

<a id="argument-033"></a>

### Reinforcement Learning with Generative World Models

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Learning Interactive Real-World Simulators](../catalog.md#paper-yang2024unisim) | [Paper](<https://arxiv.org/abs/2310.06114>) |
| 2025 | [VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators](../catalog.md#paper-vlarft2025) | [Paper](<https://arxiv.org/abs/2510.00406>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](../catalog.md#paper-wamrl2026) | [Paper](<https://arxiv.org/abs/2606.17906>) |

