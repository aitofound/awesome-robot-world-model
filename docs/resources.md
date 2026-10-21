# Resources

[Home](../README.md)

Catalogue of 21 representative resources and research systems. Experimental use describes the cited system's relevance to robot learning; access conditions depend on the specific release.

*Source: Supplementary Material S1.*

| Resource | Type | Embodiment | Modality | Real / sim | Experimental use | Links |
|---|---|---|---|---|---|---|
| **RoboNet** | dataset | robot arms | video, actions | real | representation learning, video prediction, and action-conditioned modeling | [Paper](<https://arxiv.org/abs/1910.11215>) |
| **RT-1** | dataset / model | mobile manipulator | vision, language, actions | real | policy priors and representations for behavior cloning and scalable robot control | [Paper](<https://arxiv.org/abs/2212.06817>) |
| **Open X-Embodiment** | dataset | many robots | vision, language, actions | real | representation learning and data scaling for cross-robot generalist policies | [Paper](<https://arxiv.org/abs/2310.08864>) [Code](<https://github.com/google-deepmind/open_x_embodiment>) |
| **BridgeData V2** | dataset | manipulation | vision, actions, goals | real | representation learning and data scaling for multi-task imitation and goal-conditioned policies | [Code](<https://github.com/rail-berkeley/bridge_data_v2>) |
| **OpenVLA** | model | robot manipulators | vision, language, actions | real / sim | open VLA baseline for policy priors and representations | [Paper](<https://arxiv.org/abs/2406.09246>) [Code](<https://github.com/openvla/openvla>) |
| **π0** | model | multiple robot platforms | vision, language, actions | real | action priors, representations, and fine-tuning for generalist flow-matching policies | [Paper](<https://arxiv.org/abs/2410.24164>) |
| **GR00T N1** | model | humanoids | vision, language, actions | real / sim | VLA priors and synthetic-data interfaces for humanoid policy training and transfer | [Paper](<https://arxiv.org/abs/2503.14734>) |
| **ManiSkill3** | simulator / benchmark | manipulation | RGB-D, state, actions | sim | GPU-parallel simulation, data generation, and RL evaluation | [Paper](<https://arxiv.org/abs/2410.00425>) [Code](<https://github.com/haosulab/ManiSkill>) |
| **robosuite** | simulator | manipulation | state, vision, actions | sim | simulation and reproducible manipulation-control benchmarking | [Paper](<https://arxiv.org/abs/2009.12293>) [Code](<https://github.com/ARISE-Initiative/robosuite>) |
| **Meta-World** | benchmark | manipulation | state, actions | sim | multi-task and meta-RL evaluation | [Paper](<https://meta-world.github.io/>) |
| **MimicGen** | data generation | manipulation | demos, actions | sim / real | scalable synthetic demonstrations for imitation learning | [Paper](<https://arxiv.org/abs/2310.17596>) [Code](<https://github.com/NVlabs/mimicgen>) |
| **DexMimicGen** | data generation | bimanual dexterity | demos, actions | sim | synthetic demonstrations for bimanual dexterous imitation learning | [Paper](<https://arxiv.org/abs/2410.24185>) [Code](<https://github.com/NVlabs/dexmimicgen>) |
| **Habitat** | simulator | navigation | vision, maps, actions | sim | spatial representation, navigation planning, and mapping | [Code](<https://github.com/facebookresearch/habitat-lab>) |
| **AI2-THOR** | simulator | household agents | vision, actions | sim | spatial representation and planning in interactive household tasks | [Paper](<https://arxiv.org/abs/1712.05474>) [Code](<https://github.com/allenai/ai2thor>) |
| **NVIDIA Cosmos** | platform / model | robots, autonomous vehicles | video | sim / real | world-model adaptation, video curation, tokenization, and synthetic-data generation | [Paper](<https://arxiv.org/abs/2501.03575>) |
| **Robotic World Model** | model | manipulation, locomotion | state, actions, dynamics | sim / real | neural simulation and prediction for imagined policy optimization and robust deployment | [Paper](<https://arxiv.org/abs/2501.10100>) |
| **RoboHorizon** | model / benchmark study | manipulation | multi-view vision, language, actions | sim | planning, reward shaping, and representation learning for long-horizon visual RL | [Paper](<https://arxiv.org/abs/2501.06605>) |
| **VLAC** | critic / model | manipulation | vision, language, actions, rewards | real | policy prior and critic for dense rewards and asynchronous real-world RL | [Paper](<https://arxiv.org/abs/2509.15937>) |
| **World Model Reconstruction** | model / control system | humanoid locomotion | proprioception, terrain state | real | world-state representation and adaptation for robust locomotion | [Paper](<https://arxiv.org/abs/2502.16230>) |
| **Ego-Vision Contact Planning** | model / control system | humanoids | depth, proprioception, contacts | real / sim | predictive MPC and value surrogates for contact-rich planning | [Paper](<https://arxiv.org/abs/2510.11682>) |
| **World-in-World** | benchmark | embodied agents | video, actions, tasks | sim | testing whether world-model rollouts improve embodied decisions | [Paper](<https://arxiv.org/abs/2510.18135>) |

## Further code repositories

Official repositories of other works cited in the survey.

| Repository | Work | Kind |
|---|---|---|
| [RoboTwin](<https://github.com/RoboTwin-Platform/RoboTwin>) | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](<https://arxiv.org/abs/2506.18088>) · 2025 · [ⓘ](catalog.md#paper-chen2025robotwin2) | `benchmark` |
| [CALVIN](<https://github.com/mees/calvin>) | [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](<https://arxiv.org/abs/2112.03227>) · RA-L 2022 · [ⓘ](catalog.md#paper-mees2022calvin) | `benchmark` |
| [RLBench](<https://github.com/stepjam/RLBench>) | [RLBench: The Robot Learning Benchmark and Learning Environment](<https://arxiv.org/abs/1909.12271>) · RA-L 2020 · [ⓘ](catalog.md#paper-james2020rlbench) | `benchmark` |
| [HumanoidBench](<https://github.com/carlosferrazza/humanoid-bench>) | [HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](<https://doi.org/10.15607/RSS.2024.XX.061>) · RSS 2024 · [ⓘ](catalog.md#paper-sferrazza2024humanoidbench) | `benchmark` |
| [RoboCasa](<https://github.com/robocasa/robocasa>) | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](<https://arxiv.org/abs/2603.04356>) · ICLR 2026 · [ⓘ](catalog.md#paper-nasiriany2026robocasa365) | `benchmark` |
| [DreamGen / GR00T Dreams](<https://github.com/NVIDIA/GR00T-dreams>) | **DreamGen**: [Unlocking Generalization in Robot Learning through Video World Models](<https://arxiv.org/abs/2505.12705>) · CoRL 2025 · [ⓘ](catalog.md#paper-jang2025dreamgen) | `method-code` |
| [DreamerV3](<https://github.com/danijar/dreamerv3>) | **DreamerV3**: [Mastering Diverse Domains through World Models](<https://arxiv.org/abs/2301.04104>) · 2023 · [ⓘ](catalog.md#paper-hafner2023dreamerv3) | `method-code` |
| [DayDreamer](<https://github.com/danijar/daydreamer>) | **DayDreamer**: [World Models for Physical Robot Learning](<https://arxiv.org/abs/2206.14176>) · CoRL 2022 · [ⓘ](catalog.md#paper-wu2022daydreamer) | `method-code` |
| [DINO-WM](<https://github.com/gaoyuezhou/dino_wm>) | **DINO-WM**: [World Models on Pre-trained Visual Features Enable Zero-Shot Planning](<https://arxiv.org/abs/2411.04983>) · ICML 2025 · [ⓘ](catalog.md#paper-zhou2025dinowm) | `method-code` |
| [V-JEPA 2](<https://github.com/facebookresearch/vjepa2>) | **V-JEPA 2-AC**: [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](<https://arxiv.org/abs/2506.09985>) · arXiv 2025 · [ⓘ](catalog.md#paper-assran2025vjepa2) | `method-code` |
| [SafeDreamer](<https://github.com/PKU-Alignment/SafeDreamer>) | **SafeDreamer**: [Safe reinforcement learning with world models](<https://arxiv.org/abs/2307.07176>) · ICLR 2024 · [ⓘ](catalog.md#paper-huang2024safedreamer) | `method-code` |
| [Sparsh](<https://github.com/facebookresearch/sparsh>) | **Sparsh**: [Self-supervised Touch Representations for Vision-based Tactile Sensing](<https://arxiv.org/abs/2410.24090>) · CoRL 2024 · [ⓘ](catalog.md#paper-higuera2024sparsh) | `representation` |

**Notes.** Habitat: Upstream README states that Meta internal teams no longer actively develop or maintain habitat-lab beyond v0.3.4; inspected 2026-10-01. BridgeData V2: The linked GitHub repository contains training implementations; the dataset is linked from its project page.

Each repository link was checked against the upstream README; see the `primary_check` field in [resources.json](../data/resources.json). Packages were not installed or run.
