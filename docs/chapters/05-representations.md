# 05. Representation Substrates and World-Model Mechanics

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Compare pixel/video, predictive latent, 3D/object-centric, structured physics and causal representations. RSSM, autoregression, diffusion, flow and ODE formulations are cross-cutting mechanics.

## Reading questions

- Which state must be preserved for the task?
- Which variables are action-grounded?
- Does a claimed temporal mechanism refer to physical time or computation?

## Interpretation boundary

A causal-sounding objective is not identified causal structure. Continuous-time prediction need not accept queried candidate actions.

## Selected annotations

- [PlaNet](../methods.md#paper-hafner2019planet)
- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DreamerV2](../methods.md#paper-hafner2021dreamerv2)
- [DreamerV3](../methods.md#paper-hafner2023dreamerv3)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [DINO-WM](../methods.md#paper-zhou2025dinowm)
- [V-JEPA 2](../methods.md#paper-assran2025vjepa2)
- [Causal-JEPA](../methods.md#paper-nam2026causaljepa)
- [ODEWorld](../methods.md#paper-liu2026odeworld)
- [PointWorld](../methods.md#paper-pointworld2026)
- [PhysTwin](../methods.md#paper-jiang2025phystwin)
- [WorldPlanner](../methods.md#paper-worldplanner2025)
- [RoboDreamer](../methods.md#paper-robodreamer2024)
- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [Genie](../methods.md#paper-bruce2024genie)

## References by argument (78 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-018"></a>

### Section opening

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Anticipate Before Acting: Future-State-Conditioned Vision-Language Navigation](../catalog.md#paper-zhang2026anticipate) | [Paper](<https://arxiv.org/abs/2607.18042>) |
| 2026 | [FutureNav: Unified World-Action Modeling for Vision-and-Language Navigation](../catalog.md#paper-zhang2026futurenav) | [Paper](<https://arxiv.org/abs/2606.30367>) |

<a id="argument-019"></a>

### The Representation Question: What Should a World Model Encode

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Exploring structural degradation in dense representations for self-supervised learning](../catalog.md#paper-dai2026exploring) | Source metadata only |
| 2022 | [Masked autoencoders are scalable vision learners](../catalog.md#paper-he2022masked) | Source metadata only |
| 2023 | [Dinov2: Learning robust visual features without supervision](../catalog.md#paper-oquab2023dinov2) | [Paper](<https://arxiv.org/abs/2304.07193>) |
| 2022 | [Masked visual pre-training for motor control](../catalog.md#paper-xiao2022masked) | [Paper](<https://arxiv.org/abs/2203.06173>) |
| 2022 | [R3m: A universal visual representation for robot manipulation](../catalog.md#paper-nair2022r3m) | [Paper](<https://arxiv.org/abs/2203.12601>) |
| 2024 | [Revisiting feature prediction for learning visual representations from video](../catalog.md#paper-bardes2024revisiting) | [Paper](<https://arxiv.org/abs/2404.08471>) |
| 2024 | [Not all pairs are equal: Hierarchical learning for average-precision-oriented video retrieval](../catalog.md#paper-liu2024not) | Source metadata only |
| 2025 | [When the future becomes the past: Taming temporal correspondence for self-supervised video representation learning](../catalog.md#paper-liu2025future) | Source metadata only |
| 2023 | [Learning Universal Policies via Text-Guided Video Generation](../catalog.md#paper-du2023unipi) | [Paper](<https://arxiv.org/abs/2302.00111>) |
| 2025 | [DINO-WM: World Models on Pre-trained Visual Features Enable Zero-Shot Planning](../catalog.md#paper-zhou2025dinowm) | [Paper](<https://arxiv.org/abs/2411.04983>) |
| 2025 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../catalog.md#paper-assran2025vjepa2) | [Paper](<https://arxiv.org/abs/2506.09985>) |
| 2019 | [Deepmdp: Learning continuous latent space models for representation learning](../catalog.md#paper-gelada2019deepmdp) | Source metadata only |
| 2020 | [Learning to simulate complex physics with graph networks](../catalog.md#paper-sanchez2020learning) | Source metadata only |
| 2024 | [Physdreamer: Physics-based interaction with 3d objects via video generation](../catalog.md#paper-zhang2024physdreamer) | Source metadata only |

<a id="argument-020"></a>

### Latent Representations: Learning Compact Predictive States

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [DINO-WM: World Models on Pre-trained Visual Features Enable Zero-Shot Planning](../catalog.md#paper-zhou2025dinowm) | [Paper](<https://arxiv.org/abs/2411.04983>) |
| 2025 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../catalog.md#paper-assran2025vjepa2) | [Paper](<https://arxiv.org/abs/2506.09985>) |
| 2025 | [LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics](../catalog.md#paper-balestriero2025lejepa) | [Paper](<https://arxiv.org/abs/2511.08544>) |
| 2026 | [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](../catalog.md#paper-meta2026vjepa21) | [Paper](<https://arxiv.org/abs/2603.14482>) |
| 2026 | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](../catalog.md#paper-maes2026leworldmodel) | [Paper](<https://arxiv.org/abs/2603.19312>) |
| 2026 | [Temporal Straightening for Latent Planning](../catalog.md#paper-wang2026temporalstraightening) | [Paper](<https://arxiv.org/abs/2603.12231>) |
| 2026 | [ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](../catalog.md#paper-liu2026odeworld) | [Paper](<https://arxiv.org/abs/2607.27924>) |
| 2026 | [LeVJEPA: Efficient &amp; Scalable Video Pretraining without the Heuristics](../catalog.md#paper-kuhn2026levjepa) | [Paper](<https://arxiv.org/abs/2608.27395>) |
| 2026 | [What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](../catalog.md#paper-terver2026jepawm) | [Paper](<https://arxiv.org/abs/2512.24497>) |

<a id="argument-021"></a>

### Geometric Representations: Making 3D Structure Explicit

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](../catalog.md#paper-lu2024manigaussian) | [Paper](<https://arxiv.org/abs/2403.08321>) |
| 2025 | [ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model](../catalog.md#paper-yu2025manigaussianpp) | [Paper](<https://arxiv.org/abs/2506.19842>) |
| 2026 | [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](../catalog.md#paper-zhang2026gaussiandream) | [Paper](<https://arxiv.org/abs/2605.20752>) |
| 2025 | [GaussGym: An Open-Source Real-to-Sim Framework for Learning Locomotion from Pixels](../catalog.md#paper-escontrela2025gaussgym) | [Paper](<https://arxiv.org/abs/2510.15352>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2025 | [ParticleFormer: A 3D Point Cloud World Model for Multi-Object, Multi-Material Robotic Manipulation](../catalog.md#paper-huang2025particleformer) | [Paper](<https://arxiv.org/abs/2506.23126>) |
| 2026 | [SyncTwin: Fast Digital Twin Construction and Synchronization for Safe Robotic Manipulation](../catalog.md#paper-huang2026synctwin) | [Paper](<https://arxiv.org/abs/2601.09920>) |
| 2026 | [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](../catalog.md#paper-chen2026agenticreal2sim) | [Paper](<https://arxiv.org/abs/2607.19190>) |
| 2025 | [Object-Centric World Model for Language-Guided Manipulation](../catalog.md#paper-jeong2025objectcentric) | [Paper](<https://arxiv.org/abs/2503.06170>) |
| 2025 | [FOCUS: Object-Centric World Models for Robotic Manipulation](../catalog.md#paper-ferraro2025focus) | Source metadata only |
| 2026 | [Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation](../catalog.md#paper-chen2026goalvla) | [Paper](<https://arxiv.org/abs/2506.23919>) |

<a id="argument-022"></a>

### Physical Representations: Encoding Dynamics and Constraints

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [Learning Particle Dynamics for Manipulating Rigid Bodies, Deformable Objects, and Fluids](../catalog.md#paper-li2019particle) | [Paper](<https://arxiv.org/abs/1810.01566>) |
| 2020 | [Keypoints into the Future: Self-Supervised Correspondence in Model-Based Reinforcement Learning](../catalog.md#paper-manuelli2020keypoints) | [Paper](<https://arxiv.org/abs/2009.05085>) |
| 2020 | [Learning Compositional Koopman Operators for Model-Based Control](../catalog.md#paper-li2020koopman) | [Paper](<https://arxiv.org/abs/1910.08264>) |
| 2023 | [On the Utility of Koopman Operator Theory in Learning Dexterous Manipulation Skills](../catalog.md#paper-han2023koopman) | [Paper](<https://arxiv.org/abs/2303.13446>) |
| 2025 | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../catalog.md#paper-jiang2025phystwin) | [Paper](<https://arxiv.org/abs/2503.17973>) |
| 2024 | [AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation](../catalog.md#paper-zhang2024adaptigraph) | [Paper](<https://arxiv.org/abs/2407.07889>) |
| 2026 | [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](../catalog.md#paper-yin2026physcore) | [Paper](<https://arxiv.org/abs/2607.20653>) |
| 2026 | [Learning to Unfold Cloth: Scaling up World Models to Deformable Object Manipulation](../catalog.md#paper-rome2026unfold) | [Paper](<https://arxiv.org/abs/2602.16675>) |
| 2025 | [Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](../catalog.md#paper-cheng2025graphguidedscenereconstructionimages) | [Paper](<https://arxiv.org/abs/2502.17377>) |
| 2025 | [VGGT4D: Mining Motion Cues in Visual Geometry Transformers for 4D Scene Reconstruction](../catalog.md#paper-hu2025vggt4dminingmotioncues) | [Paper](<https://arxiv.org/abs/2511.19971>) |
| 2024 | [Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation](../catalog.md#paper-torne2024rialto) | [Paper](<https://doi.org/10.15607/RSS.2024.XX.015>) |
| 2024 | [RoboGSim: A Real2Sim2Real Robotic Gaussian Splatting Simulator](../catalog.md#paper-li2024robogsim) | [Paper](<https://arxiv.org/abs/2411.11839>) |

<a id="argument-023"></a>

### Causal Representations

| Year | Work | Primary entry |
|---|---|---|
| 2021 | [Toward Causal Representation Learning](../catalog.md#paper-scholkopf2021causal) | [Paper](<https://arxiv.org/abs/2102.11107>) |
| 2022 | [CITRIS: Causal Identifiability from Temporal Intervened Sequences](../catalog.md#paper-lippe2022citris) | [Paper](<https://proceedings.mlr.press/v162/lippe22a.html>) |
| 2022 | [Weakly supervised causal representation learning](../catalog.md#paper-brehmer2022weakly) | [Paper](<https://doi.org/10.52202/068431-2776>) |
| 2022 | [Causal Dynamics Learning for Task-Independent State Abstraction](../catalog.md#paper-wang2022cdl) | [Paper](<https://arxiv.org/abs/2206.13452>) |
| 2026 | [Causal-JEPA: Learning World Models through Object-Level Latent Masking](../catalog.md#paper-nam2026causaljepa) | [Paper](<https://arxiv.org/abs/2602.11389>) |
| 2020 | [CoPhy: Counterfactual Learning of Physical Dynamics](../catalog.md#paper-baradel2020cophy) | [Paper](<https://arxiv.org/abs/1909.12000>) |

<a id="argument-024"></a>

### Dynamics Mechanisms: How World States Evolve

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [Learning Latent Dynamics for Planning from Pixels](../catalog.md#paper-hafner2019planet) | [Paper](<https://arxiv.org/abs/1811.04551>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2021 | [Mastering Atari with Discrete World Models](../catalog.md#paper-hafner2021dreamerv2) | [Paper](<https://arxiv.org/abs/2010.02193>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2023 | [Masked world models for visual control](../catalog.md#paper-seo2023masked) | Source metadata only |
| 2017 | [Deep visual foresight for planning robot motion](../catalog.md#paper-finn2017deep) | Source metadata only |
| 2022 | [Maskvit: Masked visual pre-training for video prediction](../catalog.md#paper-gupta2022maskvit) | [Paper](<https://arxiv.org/abs/2206.11894>) |
| 2024 | [ivideogpt: Interactive videogpts are scalable world models](../catalog.md#paper-wu2024ivideogpt) | Source metadata only |
| 2023 | [Learning Universal Policies via Text-Guided Video Generation](../catalog.md#paper-du2023unipi) | [Paper](<https://arxiv.org/abs/2302.00111>) |
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2025 | [Irasim: A fine-grained world model for robot manipulation](../catalog.md#paper-zhu2025irasim) | Source metadata only |
| 2026 | [Inference-time enhancement of generative robot policies via predictive world modeling](../catalog.md#paper-qi2026inference) | Source metadata only |
| 2026 | [Ctrl-world: A controllable generative world model for robot manipulation](../catalog.md#paper-guo2026ctrl) | Source metadata only |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2022 | [Flow matching for generative modeling](../catalog.md#paper-lipman2022flow) | [Paper](<https://arxiv.org/abs/2210.02747>) |
| 2022 | [Flow straight and fast: Learning to generate and transfer data with rectified flow](../catalog.md#paper-liu2022flow) | [Paper](<https://arxiv.org/abs/2209.03003>) |
| 2026 | [WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](../catalog.md#paper-jain2026texttt) | [Paper](<https://arxiv.org/abs/2606.13672>) |
| 2026 | [τ_0-WM: A Unified Video-Action World Model for Robotic Manipulation](../catalog.md#paper-zhou2026tau0wm) | [Paper](<https://arxiv.org/abs/2606.01027>) |
| 2026 | [DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation](../catalog.md#paper-shan2026dvg) | [Paper](<https://arxiv.org/abs/2606.32028>) |
| 2026 | [ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](../catalog.md#paper-liu2026odeworld) | [Paper](<https://arxiv.org/abs/2607.27924>) |
| 2026 | [Looped world models](../catalog.md#paper-lu2026loopwm) | [Paper](<https://arxiv.org/abs/2606.18208>) |

<a id="argument-025"></a>

### From Video Generation to Controllable World Models

| Year | Work | Primary entry |
|---|---|---|
| 2024 | [Genie: Generative Interactive Environments](../catalog.md#paper-bruce2024genie) | [Paper](<https://arxiv.org/abs/2402.15391>) |
| 2023 | [GAIA-1: A Generative World Model for Autonomous Driving](../catalog.md#paper-hu2023gaia1) | [Paper](<https://arxiv.org/abs/2309.17080>) |
| 2024 | [Video Generation Models as World Simulators](../catalog.md#paper-brooks2024sora) | [Paper](<https://openai.com/index/video-generation-models-as-world-simulators/>) |
| 2024 | [Learning Interactive Real-World Simulators](../catalog.md#paper-yang2024unisim) | [Paper](<https://arxiv.org/abs/2310.06114>) |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2026 | [ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](../catalog.md#paper-liu2026odeworld) | [Paper](<https://arxiv.org/abs/2607.27924>) |

