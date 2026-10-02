# 12. Resources: Datasets, Simulators, Benchmarks, and Frameworks

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Distinguish datasets, interactive engines, benchmark suites, harnesses and checkpoints. Check which interface an artifact actually provides.

## Reading questions

- Can it support model fitting?
- Can it branch decisions or learning trajectories?
- Can it assess physical deployment and interventions?

## Interpretation boundary

Model, Decision, Learning and Deployment capabilities are non-nested. Static logs and a paper alone are not deployment resources.

## Selected annotations

- [PointWorld](../methods.md#paper-pointworld2026)
- [Robotic World Model (RWM)](../methods.md#paper-li2025roboticworldmodel)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [Hi-WM](../methods.md#paper-li2026hiwm)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [Cosmos](../methods.md#paper-nvidia2025cosmos)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [World-in-World](../methods.md#paper-worldinworld2025)
- [OpenVLA](../methods.md#paper-openvla2024)
- [pi0](../methods.md#paper-pi0)

## References by argument (54 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-073"></a>

### Section opening

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [RoboNet: Large-Scale Multi-Robot Learning](../catalog.md#paper-robonet) | [Paper](<https://arxiv.org/abs/1910.11215>) |
| 2022 | [RT-1: Robotics Transformer for Real-World Control at Scale](../catalog.md#paper-rt1) | [Paper](<https://arxiv.org/abs/2212.06817>) |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2023 | [Bridgedata v2: A dataset for robot learning at scale](../catalog.md#paper-bridgedatav2) | Source metadata only |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2020 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](../catalog.md#paper-robosuite) | [Paper](<https://arxiv.org/abs/2009.12293>) |
| 2020 | [Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](../catalog.md#paper-metaworld) | [Paper](<https://meta-world.github.io/>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../catalog.md#paper-dexmimicgen) | [Paper](<https://arxiv.org/abs/2410.24185>) |
| 2019 | [Habitat: A platform for embodied ai research](../catalog.md#paper-habitat) | Source metadata only |
| 2017 | [Ai2-thor: An interactive 3d environment for visual ai](../catalog.md#paper-ai2thor) | [Paper](<https://arxiv.org/abs/1712.05474>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Robohorizon: An llm-assisted multi-view world model for long-horizon robotic manipulation](../catalog.md#paper-robohorizon2025) | [Paper](<https://arxiv.org/abs/2501.06605>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

<a id="argument-074"></a>

### Frontier Resource Cards › Large Robot Datasets: From Behavior Logs to World-Model Training Data

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [RoboNet: Large-Scale Multi-Robot Learning](../catalog.md#paper-robonet) | [Paper](<https://arxiv.org/abs/1910.11215>) |
| 2023 | [Bridgedata v2: A dataset for robot learning at scale](../catalog.md#paper-bridgedatav2) | Source metadata only |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2022 | [RT-1: Robotics Transformer for Real-World Control at Scale](../catalog.md#paper-rt1) | [Paper](<https://arxiv.org/abs/2212.06817>) |
| 2023 | [Rt-2: Vision-language-action models transfer web knowledge to robotic control](../catalog.md#paper-rt2) | [Paper](<https://arxiv.org/abs/2307.15818>) |

<a id="argument-075"></a>

### Frontier Resource Cards › Foundation Policy Resources: Open VLAs as Baselines and Priors

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |

<a id="argument-076"></a>

### Frontier Resource Cards › Physics Simulators and GPU-Parallel Benchmarks

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2020 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](../catalog.md#paper-robosuite) | [Paper](<https://arxiv.org/abs/2009.12293>) |
| 2020 | [Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](../catalog.md#paper-metaworld) | [Paper](<https://meta-world.github.io/>) |
| 2019 | [Habitat: A platform for embodied ai research](../catalog.md#paper-habitat) | Source metadata only |
| 2017 | [Ai2-thor: An interactive 3d environment for visual ai](../catalog.md#paper-ai2thor) | [Paper](<https://arxiv.org/abs/1712.05474>) |
| 2023 | [TWIST: Teacher-Student World Model Distillation for Efficient Sim-to-Real Transfer](../catalog.md#paper-twist2023) | [Paper](<https://arxiv.org/abs/2311.03622>) |

<a id="argument-077"></a>

### Frontier Resource Cards › Learned Simulators and World Foundation Models

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2026 | [ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](../catalog.md#paper-abotphysworld2026) | [Paper](<https://arxiv.org/abs/2603.23376>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2026 | [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](../catalog.md#paper-huang2026solarwm) | [Paper](<https://arxiv.org/abs/2609.02886>) |

<a id="argument-078"></a>

### Frontier Resource Cards › Synthetic Demonstration Engines

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../catalog.md#paper-dexmimicgen) | [Paper](<https://arxiv.org/abs/2410.24185>) |

<a id="argument-079"></a>

### Frontier Resource Cards › Closed-Loop Benchmarks and Evaluation Harnesses

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2020 | [Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](../catalog.md#paper-metaworld) | [Paper](<https://meta-world.github.io/>) |
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |

<a id="argument-080"></a>

### Frontier Resource Cards › Visuo-Tactile and Contact Resources

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-081"></a>

### Frontier Resource Cards › Safety, Monitoring, and Failure Resources

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |

<a id="argument-082"></a>

### Resource Gaps for 2026-Ready Robot World Models

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2024 | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../catalog.md#paper-khazatsky2024droid) | Source metadata only |
| 2024 | [Robomind: Benchmark on multi-embodiment intelligence normative data for robot manipulation](../catalog.md#paper-wu2024robomind) | [Paper](<https://arxiv.org/abs/2412.13877>) |
| 2025 | [Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems](../catalog.md#paper-bu2025agibot) | [Paper](<https://arxiv.org/abs/2503.06669>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2026 | [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](../catalog.md#paper-clap2026) | [Paper](<https://arxiv.org/abs/2608.27406>) |
| 2023 | [Reflect: Summarizing robot experiences for failure explanation and correction](../catalog.md#paper-liu2023reflect) | [Paper](<https://arxiv.org/abs/2306.15724>) |
| 2024 | [Aha: A vision-language-model for detecting and reasoning over failures in robotic manipulation](../catalog.md#paper-duan2024aha) | [Paper](<https://arxiv.org/abs/2410.00371>) |
| 2026 | [Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols](../catalog.md#paper-vifailback2026) | [Paper](<https://arxiv.org/abs/2512.02787>) |
| 2019 | [RoboNet: Large-Scale Multi-Robot Learning](../catalog.md#paper-robonet) | [Paper](<https://arxiv.org/abs/1910.11215>) |
| 2024 | [Scaling Cross-Embodied Learning: One Policy for Manipulation, Navigation, Locomotion and Aviation](../catalog.md#paper-crossformer2024) | [Paper](<https://arxiv.org/abs/2408.11812>) |
| 2026 | [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../catalog.md#paper-lee2026space) | [Paper](<https://arxiv.org/abs/2606.24049>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2025 | [Manifeel: Benchmarking and understanding visuotactile manipulation policy learning](../catalog.md#paper-luu2025manifeel) | [Paper](<https://arxiv.org/abs/2505.18472>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [T-Rex: Tactile-reactive dexterous manipulation](../catalog.md#paper-niu2026t) | [Paper](<https://arxiv.org/abs/2606.17055>) |
| 2026 | [Ftp-1: A generalist foundation tactile policy across tactile sensors for contact-rich manipulation](../catalog.md#paper-yuan2026ftp) | [Paper](<https://arxiv.org/abs/2606.13102>) |
| 2026 | [PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](../catalog.md#paper-yu2026prism) | [Paper](<https://arxiv.org/abs/2608.17962>) |
| 2024 | [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](../catalog.md#paper-luo2024hilserl) | [Paper](<https://arxiv.org/abs/2410.21845>) |
| 2024 | [Intervengen: Interventional data generation for robust and data-efficient robot imitation learning](../catalog.md#paper-hoque2024intervengen) | Source metadata only |
| 2026 | [Visual Verification Enables Inference-Time Steering and Autonomous Policy Improvement](../catalog.md#paper-visualverification2026) | [Paper](<https://arxiv.org/abs/2606.18247>) |
| 2026 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](../catalog.md#paper-ups2026) | [Paper](<https://arxiv.org/abs/2602.22474>) |

<a id="argument-083"></a>

### What Resources Should Enable: Four Capability Dimensions

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [RoboNet: Large-Scale Multi-Robot Learning](../catalog.md#paper-robonet) | [Paper](<https://arxiv.org/abs/1910.11215>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2026 | [VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models](../catalog.md#paper-huang2026vlareplica) | [Paper](<https://arxiv.org/abs/2605.20774>) |
| 2026 | [RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](../catalog.md#paper-chen2026robodojo) | [Paper](<https://arxiv.org/abs/2607.04434>) |
| 2026 | [Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](../catalog.md#paper-li2026hiwm) | [Paper](<https://arxiv.org/abs/2604.21741>) |

<a id="argument-084"></a>

### Evaluation Axes

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2023 | [Bridgedata v2: A dataset for robot learning at scale](../catalog.md#paper-bridgedatav2) | Source metadata only |
| 2024 | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../catalog.md#paper-khazatsky2024droid) | Source metadata only |
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2020 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](../catalog.md#paper-robosuite) | [Paper](<https://arxiv.org/abs/2009.12293>) |
| 2019 | [Habitat: A platform for embodied ai research](../catalog.md#paper-habitat) | Source metadata only |
| 2024 | [Evaluating Real-World Robot Manipulation Policies in Simulation](../catalog.md#paper-li2024simpler) | [Paper](<https://arxiv.org/abs/2405.05941>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |

