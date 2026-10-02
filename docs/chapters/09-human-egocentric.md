# 09. Human and Egocentric Data as a World-Model Source

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Human video can support representation priors, motion/action proxies, predictive world-action objectives or deployment context. Each route faces different grounding requirements.

## Reading questions

- Which visual/sensing gap is addressed?
- Which kinematic and contact gaps remain?
- How are robot action labels obtained?

## Interpretation boundary

Human motion is not robot experience without grounding. Context conditioning and fast weight updates must be separated.

## Selected annotations

- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [DreamDojo](../methods.md#paper-gao2026dreamdojo)
- [World-Gymnast](../methods.md#paper-worldgymnast2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [EgoWAM](../methods.md#paper-egowam2026)
- [AnyWorld](../methods.md#paper-chen2026anyworld)
- [Zero-WAM](../methods.md#paper-zhou2026zerowam)
- [TactAlign](../methods.md#paper-tactalign2026)
- [EgoZero](../methods.md#paper-egozero2025)
- [VLAW](../methods.md#paper-vlaw2026)

## References by argument (35 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-049"></a>

### Human Video as a Scalable World-Model Source

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems](../catalog.md#paper-bu2025agibot) | [Paper](<https://arxiv.org/abs/2503.06669>) |
| 2022 | [Ego4D: Around the World in 3,000 Hours of Egocentric Video](../catalog.md#paper-grauman-2022-cvpr) | Source metadata only |
| 2026 | [Egodex: Learning dexterous manipulation from large-scale egocentric video](../catalog.md#paper-hoque2026egodex) | Source metadata only |
| 2026 | [Egoscale: Scaling dexterous manipulation with diverse egocentric human data](../catalog.md#paper-zheng2026egoscale) | [Paper](<https://arxiv.org/abs/2602.16710>) |
| 2026 | [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](../catalog.md#paper-ma2026humanscale) | [Paper](<https://arxiv.org/abs/2606.20521>) |

<a id="argument-050"></a>

### The Embodiment Gap: Why Human Video Is Not Robot Experience

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](../catalog.md#paper-egoexo4d2023) | [Paper](<https://arxiv.org/abs/2311.18259>) |
| 2025 | [H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos](../catalog.md#paper-h2r2025) | [Paper](<https://arxiv.org/abs/2505.11920>) |
| 2026 | [Egodex: Learning dexterous manipulation from large-scale egocentric video](../catalog.md#paper-hoque2026egodex) | Source metadata only |
| 2024 | [Learning from Massive Human Videos for Universal Humanoid Pose Control](../catalog.md#paper-humanoidx2024) | [Paper](<https://arxiv.org/abs/2412.14172>) |
| 2025 | [EgoZero: Robot Learning from Smart Glasses](../catalog.md#paper-egozero2025) | [Paper](<https://arxiv.org/abs/2505.20290>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](../catalog.md#paper-clap2026) | [Paper](<https://arxiv.org/abs/2608.27406>) |
| 2024 | [EgoMimic: Scaling Imitation Learning via Egocentric Video](../catalog.md#paper-egomimic2024) | [Paper](<https://arxiv.org/abs/2410.24221>) |
| 2026 | [HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos](../catalog.md#paper-humanego2026) | [Paper](<https://arxiv.org/abs/2605.24934>) |
| 2025 | [EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](../catalog.md#paper-egobridge2025) | [Paper](<https://arxiv.org/abs/2509.19626>) |

<a id="argument-051"></a>

### From Human Video to Robot Learning Signals

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](../catalog.md#paper-mimicplay2023) | [Paper](<https://arxiv.org/abs/2302.12422>) |
| 2024 | [EgoMimic: Scaling Imitation Learning via Egocentric Video](../catalog.md#paper-egomimic2024) | [Paper](<https://arxiv.org/abs/2410.24221>) |
| 2025 | [EMMA: Scaling Mobile Manipulation via Egocentric Human Data](../catalog.md#paper-emma2025) | [Paper](<https://arxiv.org/abs/2509.04443>) |
| 2026 | [Egodex: Learning dexterous manipulation from large-scale egocentric video](../catalog.md#paper-hoque2026egodex) | Source metadata only |
| 2025 | [Scalable vision-language-action model pretraining for robotic manipulation with real-life human activity videos](../catalog.md#paper-li2025scalable) | [Paper](<https://arxiv.org/abs/2510.21571>) |
| 2025 | [EgoZero: Robot Learning from Smart Glasses](../catalog.md#paper-egozero2025) | [Paper](<https://arxiv.org/abs/2505.20290>) |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2026 | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../catalog.md#paper-gao2026dreamdojo) | [Paper](<https://arxiv.org/abs/2602.06949>) |
| 2026 | [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](../catalog.md#paper-egowam2026) | [Paper](<https://arxiv.org/abs/2607.08436>) |
| 2026 | [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../catalog.md#paper-zhou2026zerowam) | [Paper](<https://arxiv.org/abs/2608.26103>) |

<a id="argument-052"></a>

### Cross-Embodiment Alignment: From Human Motion to Robot-Controllable Representations

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos](../catalog.md#paper-h2r2025) | [Paper](<https://arxiv.org/abs/2505.11920>) |
| 2026 | [LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment](../catalog.md#paper-lidea2026) | [Paper](<https://arxiv.org/abs/2604.10677>) |
| 2026 | [EgoExo-WM: Unlocking Exo Video for Ego World Models](../catalog.md#paper-egoexowm2026) | [Paper](<https://arxiv.org/abs/2605.15477>) |
| 2025 | [RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning](../catalog.md#paper-robowheel2025) | [Paper](<https://arxiv.org/abs/2512.02729>) |
| 2026 | [HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos](../catalog.md#paper-humanego2026) | [Paper](<https://arxiv.org/abs/2605.24934>) |
| 2022 | [XIRL: Cross-embodiment Inverse Reinforcement Learning](../catalog.md#paper-xirl2022) | [Paper](<https://arxiv.org/abs/2106.03911>) |
| 2023 | [XSkill: Cross Embodiment Skill Discovery](../catalog.md#paper-xskill2023) | [Paper](<https://arxiv.org/abs/2307.09955>) |
| 2025 | [EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data](../catalog.md#paper-egobridge2025) | [Paper](<https://arxiv.org/abs/2509.19626>) |
| 2026 | [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](../catalog.md#paper-tactalign2026) | [Paper](<https://arxiv.org/abs/2602.13579>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |

<a id="argument-053"></a>

### From Human Data to Synthetic Data Flywheels

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Scalable vision-language-action model pretraining for robotic manipulation with real-life human activity videos](../catalog.md#paper-li2025scalable) | [Paper](<https://arxiv.org/abs/2510.21571>) |
| 2026 | [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](../catalog.md#paper-wang2026ego2robot) | [Paper](<https://arxiv.org/abs/2608.02580>) |
| 2025 | [H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos](../catalog.md#paper-h2r2025) | [Paper](<https://arxiv.org/abs/2505.11920>) |
| 2025 | [Phantom: Training Robots Without Robots Using Only Human Videos](../catalog.md#paper-lepert2025phantomtrainingrobots) | Source metadata only |
| 2026 | [Masquerade: Learning from In-the-wild Human Videos using Data-Editing](../catalog.md#paper-lepert2025masquerade) | Source metadata only |
| 2026 | [HandEdit: A Unified Benchmark for Egocentric Human-to-Robot Dexterous Hand Image Editing](../catalog.md#paper-handedit2026) | [Paper](<https://arxiv.org/abs/2608.12122>) |
| 2026 | [AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization](../catalog.md#paper-chen2026anyworld) | [Paper](<https://arxiv.org/abs/2608.29242>) |
| 2025 | [Robot learning on the job: Human-in-the-loop autonomy and learning during deployment](../catalog.md#paper-sirius2022) | [Paper](<https://doi.org/10.15607/RSS.2023.XIX.005>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [World-gymnast: Training robots with reinforcement learning in a world model](../catalog.md#paper-worldgymnast2026) | [Paper](<https://arxiv.org/abs/2602.02454>) |

