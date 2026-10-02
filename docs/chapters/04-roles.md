# 04. The Optimizable Roles of World Models

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

The six roles organize uses before architectures. A single system can serve several roles, and the same model can change roles when its consumer changes.

## Reading questions

- What is the prediction objective?
- What is the downstream use?
- What object is changed by that use?

## Interpretation boundary

Roles describe interfaces and uses; they are neither disjoint model families nor maturity levels.

## Selected annotations

- [PlaNet](../methods.md#paper-hafner2019planet)
- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DINO-WM](../methods.md#paper-zhou2025dinowm)
- [PointWorld](../methods.md#paper-pointworld2026)
- [WorldPlanner](../methods.md#paper-worldplanner2025)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [RoboDreamer](../methods.md#paper-robodreamer2024)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [Gen2Act](../methods.md#paper-bharadhwaj2025gen2act)
- [Dreamitate](../methods.md#paper-liang2025dreamitate)
- [Model-Based Runtime Monitoring](../methods.md#paper-liu2024runtime)
- [SafeDreamer](../methods.md#paper-huang2024safedreamer)
- [OpenVLA](../methods.md#paper-openvla2024)
- [pi0](../methods.md#paper-pi0)

## References by argument (54 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-010"></a>

### A Common Template for Role Analysis

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2025 | [Unified Video Action Model](../catalog.md#paper-li2025uva) | [Paper](<https://arxiv.org/abs/2503.00200>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [DINO-WM: World Models on Pre-trained Visual Features Enable Zero-Shot Planning](../catalog.md#paper-zhou2025dinowm) | [Paper](<https://arxiv.org/abs/2411.04983>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2024 | [Model-Based Runtime Monitoring with Interactive Imitation Learning](../catalog.md#paper-liu2024runtime) | [Paper](<https://arxiv.org/abs/2310.17552>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |

<a id="argument-011"></a>

### Representation: what state should the policy act on?

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [DINO-WM: World Models on Pre-trained Visual Features Enable Zero-Shot Planning](../catalog.md#paper-zhou2025dinowm) | [Paper](<https://arxiv.org/abs/2411.04983>) |
| 2026 | [What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](../catalog.md#paper-terver2026jepawm) | [Paper](<https://arxiv.org/abs/2512.24497>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-012"></a>

### Prediction and imagination: what futures can be queried?

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2019 | [Learning Latent Dynamics for Planning from Pixels](../catalog.md#paper-hafner2019planet) | [Paper](<https://arxiv.org/abs/1811.04551>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |

<a id="argument-013"></a>

### Simulation &amp; Data Generation: how can models provide experience?

| Year | Work | Primary entry |
|---|---|---|
| 2012 | [MuJoCo: A Physics Engine for Model-Based Control](../catalog.md#paper-todorov2012mujoco) | [Paper](<https://doi.org/10.1109/IROS.2012.6386109>) |
| 2021 | [Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning](../catalog.md#paper-makoviychuk2021isaacgym) | [Paper](<https://arxiv.org/abs/2108.10470>) |
| 2017 | [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](../catalog.md#paper-tobin2017domain) | [Paper](<https://doi.org/10.1109/IROS.2017.8202133>) |
| 2019 | [Solving Rubik's Cube with a Robot Hand](../catalog.md#paper-openai2019rubiks) | [Paper](<https://arxiv.org/abs/1910.07113>) |
| 2024 | [Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation](../catalog.md#paper-torne2024rialto) | [Paper](<https://doi.org/10.15607/RSS.2024.XX.015>) |
| 2025 | [X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real](../catalog.md#paper-dan2025xsim) | Source metadata only |
| 2025 | [Visual Imitation Enables Contextual Humanoid Control](../catalog.md#paper-allshire2025videomimic) | Source metadata only |
| 2026 | [CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives](../catalog.md#paper-wang2026crisp) | Source metadata only |
| 2026 | [REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image](../catalog.md#paper-ma2026rest3d) | [Paper](<https://arxiv.org/abs/2605.30338>) |
| 2026 | [EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents](../catalog.md#paper-wang2026embodmocap) | Source metadata only |
| 2026 | [HIL: Hybrid Imitation Learning for Dynamic Athletic Control](../catalog.md#paper-wang2026hil) | Source metadata only |
| 2026 | [Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework](../catalog.md#paper-wang2026generalizing) | Source metadata only |
| 2026 | [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](../catalog.md#paper-ranawaka2026simfoundry) | [Paper](<https://arxiv.org/abs/2606.28276>) |
| 2025 | [VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](../catalog.md#paper-zhu2025vrrobo) | [Paper](<https://doi.org/10.1109/LRA.2025.3575648>) |
| 2025 | [Splatting Physical Scenes: End-to-End Real-to-Sim from Imperfect Robot Data](../catalog.md#paper-moran2025splatting) | [Paper](<https://arxiv.org/abs/2506.04120>) |
| 2025 | [GaussGym: An Open-Source Real-to-Sim Framework for Learning Locomotion from Pixels](../catalog.md#paper-escontrela2025gaussgym) | [Paper](<https://arxiv.org/abs/2510.15352>) |
| 2025 | [MonoFusion: Sparse-View 4D Reconstruction via Monocular Fusion](../catalog.md#paper-wang2025monofusion) | Source metadata only |
| 2025 | [Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation](../catalog.md#paper-xie2025vid2sim) | Source metadata only |
| 2025 | [Dreamitate: Real-World Visuomotor Policy Learning via Video Generation](../catalog.md#paper-liang2025dreamitate) | [Paper](<https://arxiv.org/abs/2406.16862>) |
| 2025 | [Gen2Act: Human Video Generation in Novel Scenarios Enables Generalizable Robot Manipulation](../catalog.md#paper-bharadhwaj2025gen2act) | [Paper](<https://arxiv.org/abs/2409.16283>) |
| 2025 | [Robotic Manipulation by Imitating Generated Videos Without Physical Demonstrations](../catalog.md#paper-patel2025rigvid) | [Paper](<https://arxiv.org/abs/2507.00990>) |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2026 | [Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow](../catalog.md#paper-dharmarajan2026dream2flow) | Source metadata only |
| 2025 | [Robot Learning from a Physical World Model](../catalog.md#paper-mao2025physworld) | [Paper](<https://arxiv.org/abs/2511.07416>) |
| 2026 | [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](../catalog.md#paper-xie2026grail) | [Paper](<https://arxiv.org/abs/2606.05160>) |
| ? | [Counterfactual Video Generation for Humanoid Loco-Manipulation](../catalog.md#paper-wang2026counterfactual) | Source metadata only |

<a id="argument-014"></a>

### Planning and search: which action to execute now?

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2025 | [Robohorizon: An llm-assisted multi-view world model for long-horizon robotic manipulation](../catalog.md#paper-robohorizon2025) | [Paper](<https://arxiv.org/abs/2501.06605>) |

<a id="argument-015"></a>

### Evaluation, reward, and safety: what to reinforce or reject?

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2017 | [Deep Reinforcement Learning from Human Preferences](../catalog.md#paper-christiano2017preferences) | [Paper](<https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2024 | [Safedreamer: Safe reinforcement learning with world models](../catalog.md#paper-huang2024safedreamer) | [Paper](<https://arxiv.org/abs/2307.07176>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |

<a id="argument-016"></a>

### Adaptation and Monitoring: how Should the Robot Respond to Deployment Feedback?

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation](../catalog.md#paper-zang2026tacforesight) | [Paper](<https://arxiv.org/abs/2606.11184>) |
| 2026 | [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](../catalog.md#paper-zhou2026touchworld) | [Paper](<https://arxiv.org/abs/2607.07287>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2019 | [HG-DAgger: Interactive Imitation Learning with Human Experts](../catalog.md#paper-kelly2019hgdagger) | [Paper](<https://doi.org/10.1109/ICRA.2019.8793698>) |
| 2022 | [ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning](../catalog.md#paper-hoque2022thrifty) | [Paper](<https://proceedings.mlr.press/v164/hoque22a.html>) |
| 2024 | [Model-Based Runtime Monitoring with Interactive Imitation Learning](../catalog.md#paper-liu2024runtime) | [Paper](<https://arxiv.org/abs/2310.17552>) |

<a id="argument-017"></a>

### System Design Patterns

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2025 | [Unified Video Action Model](../catalog.md#paper-li2025uva) | [Paper](<https://arxiv.org/abs/2503.00200>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2024 | [Model-Based Runtime Monitoring with Interactive Imitation Learning](../catalog.md#paper-liu2024runtime) | [Paper](<https://arxiv.org/abs/2310.17552>) |

