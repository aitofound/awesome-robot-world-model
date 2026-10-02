# 11. Evaluation: From Prediction Metrics to Closed-Loop Utility

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Report model behavior, policy effect, deployment behavior and evidence boundary. Model quality, policy utility and reliability are separate axes.

## Reading questions

- Does the model preserve task-relevant consequences?
- Does it improve the consumer under matched budgets?
- Is feedback useful under induced policy queries?

## Interpretation boundary

Ranking correlation is not absolute calibration. Model-real disagreement alone does not diagnose model exploitation.

## Selected annotations

- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DreamerV3](../methods.md#paper-hafner2023dreamerv3)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [TD-MPC2](../methods.md#paper-hansen2024tdmpc2)
- [PointWorld](../methods.md#paper-pointworld2026)
- [WorldPlanner](../methods.md#paper-worldplanner2025)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [RoboDreamer](../methods.md#paper-robodreamer2024)
- [Robotic World Model (RWM)](../methods.md#paper-li2025roboticworldmodel)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [WorldArena](../methods.md#paper-shang2026worldarena)
- [EWMBench](../methods.md#paper-yue2025ewmbench)
- [World-in-World](../methods.md#paper-worldinworld2025)
- [OpenVLA](../methods.md#paper-openvla2024)
- [pi0](../methods.md#paper-pi0)

## References by argument (103 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-061"></a>

### Model Quality

| Year | Work | Primary entry |
|---|---|---|
| 2018 | [Towards Accurate Generative Models of Video: A New Metric &amp; Challenges](../catalog.md#paper-unterthiner2018fvd) | [Paper](<https://arxiv.org/abs/1812.01717>) |
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2020 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](../catalog.md#paper-grimm2020value) | Source metadata only |
| 2020 | [Mastering Atari, Go, chess and shogi by planning with a learned model](../catalog.md#paper-schrittwieser2020muzero) | [Paper](<https://doi.org/10.1038/s41586-020-03051-4>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

<a id="argument-062"></a>

### Policy Utility

| Year | Work | Primary entry |
|---|---|---|
| 2018 | [Deep Reinforcement Learning that Matters](../catalog.md#paper-henderson2018deep) | [Paper](<https://doi.org/10.1609/aaai.v32i1.11694>) |
| 2021 | [Deep Reinforcement Learning at the Edge of the Statistical Precipice](../catalog.md#paper-agarwal2021precipice) | Source metadata only |
| 2024 | [Empirical Design in Reinforcement Learning](../catalog.md#paper-patterson2024empirical) | Source metadata only |
| 2024 | [Robot Learning as an Empirical Science: Best Practices for Policy Evaluation](../catalog.md#paper-kressgazit2024empirical) | [Paper](<https://arxiv.org/abs/2409.09491>) |
| 2024 | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../catalog.md#paper-hansen2024tdmpc2) | [Paper](<https://arxiv.org/abs/2310.16828>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Robohorizon: An llm-assisted multi-view world model for long-horizon robotic manipulation](../catalog.md#paper-robohorizon2025) | [Paper](<https://arxiv.org/abs/2501.06605>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2020 | [Objective Mismatch in Model-based Reinforcement Learning](../catalog.md#paper-lambert2020objective) | Source metadata only |
| 2024 | [A Unified View on Solving Objective Mismatch in Model-Based Reinforcement Learning](../catalog.md#paper-wei2024unified) | Source metadata only |
| 2017 | [Value-Aware Loss Function for Model-based Reinforcement Learning](../catalog.md#paper-farahmand2017vaml) | Source metadata only |
| 2020 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](../catalog.md#paper-grimm2020value) | Source metadata only |
| 2025 | [WorldGym: World Model as An Environment for Policy Evaluation](../catalog.md#paper-quevedo2025wpe) | [Paper](<https://arxiv.org/abs/2506.00613>) |
| 2025 | [Unpacking failure modes of generative policies: Runtime monitoring of consistency and progress](../catalog.md#paper-agia2025unpacking) | Source metadata only |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2022 | [Autonomous Reinforcement Learning: Formalism and Benchmarking](../catalog.md#paper-sharma2022autonomous) | Source metadata only |
| 2025 | [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../catalog.md#paper-atreya2025roboarena) | [Paper](<https://arxiv.org/abs/2506.18123>) |
| 2025 | [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../catalog.md#paper-zhou2025autoeval) | [Paper](<https://arxiv.org/abs/2503.24278>) |
| 2024 | [Evaluating Real-World Robot Manipulation Policies in Simulation](../catalog.md#paper-li2024simpler) | [Paper](<https://arxiv.org/abs/2405.05941>) |

<a id="argument-063"></a>

### Deployment Reliability

| Year | Work | Primary entry |
|---|---|---|
| 2017 | [A Distributional Perspective on Reinforcement Learning](../catalog.md#paper-bellemare2017distributional) | Source metadata only |
| 2020 | [Worst Cases Policy Gradients](../catalog.md#paper-tang2020worst) | Source metadata only |
| 2018 | [ISO 26262:2018 Road vehicles — Functional safety](../catalog.md#paper-iso26262) | Source metadata only |
| 2022 | [ISO 21448:2022 Road vehicles — Safety of the intended functionality](../catalog.md#paper-iso21448) | Source metadata only |
| 2025 | [ISO 10218-2:2025 Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells](../catalog.md#paper-iso10218part2) | Source metadata only |
| 2016 | [ISO/TS 15066:2016 Robots and robotic devices — Collaborative robots](../catalog.md#paper-isots15066) | Source metadata only |
| 2024 | [Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning](../catalog.md#paper-gu2024dwl) | [Paper](<https://doi.org/10.15607/RSS.2024.XX.058>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2018 | [Artificial Intelligence for Long-Term Robot Autonomy: A Survey](../catalog.md#paper-kunze2018ai) | [Paper](<https://doi.org/10.1109/LRA.2018.2860628>) |
| 2021 | [J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles](../catalog.md#paper-saej3016) | Source metadata only |
| 2023 | [ISO 34503:2023 Road vehicles — Test scenarios for automated driving systems — Specification for operational design domain](../catalog.md#paper-iso34503) | Source metadata only |
| 2024 | [Evaluating Real-World Robot Manipulation Policies in Simulation](../catalog.md#paper-li2024simpler) | [Paper](<https://arxiv.org/abs/2405.05941>) |
| 2023 | [TWIST: Teacher-Student World Model Distillation for Efficient Sim-to-Real Transfer](../catalog.md#paper-twist2023) | [Paper](<https://arxiv.org/abs/2311.03622>) |
| 2020 | [Learning Quadrupedal Locomotion over Challenging Terrain](../catalog.md#paper-lee2020quadruped) | [Paper](<https://doi.org/10.1126/scirobotics.abc5986>) |
| 2004 | [Trust in Automation: Designing for Appropriate Reliance](../catalog.md#paper-leesee2004trust) | [Paper](<https://doi.org/10.1518/hfes.46.1.50_30392>) |
| 2023 | [Task-Relevant Failure Detection for Trajectory Predictors in Autonomous Vehicles](../catalog.md#paper-farid2023taskrelevant) | Source metadata only |
| 2022 | [Task-Driven Out-of-Distribution Detection with Statistical Guarantees for Robot Learning](../catalog.md#paper-farid2022taskdriven) | Source metadata only |
| 2022 | [Failure Prediction with Statistical Guarantees for Vision-Based Robot Control](../catalog.md#paper-farid2022failure) | Source metadata only |
| 2025 | [Task-Driven Detection of Distribution Shifts with Statistical Guarantees for Robot Learning](../catalog.md#paper-farid2025taskdriven) | [Paper](<https://doi.org/10.1109/TRO.2024.3521963>) |
| 2025 | [Unpacking failure modes of generative policies: Runtime monitoring of consistency and progress](../catalog.md#paper-agia2025unpacking) | Source metadata only |
| 2016 | [Introspective Perception: Learning to Predict Failures in Vision Systems](../catalog.md#paper-daftry2016introspective) | Source metadata only |
| 2020 | [Learning to Optimize Autonomy in Competence-Aware Systems](../catalog.md#paper-basich2020learning) | Source metadata only |
| 2021 | [Waymo Simulated Driving Behavior in Reconstructed Fatal Crashes within an Autonomous Vehicle Operating Domain](../catalog.md#paper-scanlon2021waymo) | [Paper](<https://doi.org/10.1016/j.aap.2021.106454>) |
| 2011 | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../catalog.md#paper-ross2011dagger) | [Paper](<https://proceedings.mlr.press/v15/ross11a.html>) |
| 2019 | [HG-DAgger: Interactive Imitation Learning with Human Experts](../catalog.md#paper-kelly2019hgdagger) | [Paper](<https://doi.org/10.1109/ICRA.2019.8793698>) |
| 2022 | [Robot Reinforcement Learning on the Constraint Manifold](../catalog.md#paper-liu2022atacom) | Source metadata only |
| 2023 | [Closing the loop on runtime monitors with fallback-safe MPC](../catalog.md#paper-sinha2023closing) | Source metadata only |
| 2025 | [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../catalog.md#paper-zhou2025autoeval) | [Paper](<https://arxiv.org/abs/2503.24278>) |
| 2018 | [Safe Reinforcement Learning via Shielding](../catalog.md#paper-alshiekh2018safe) | [Paper](<https://doi.org/10.1609/aaai.v32i1.11797>) |
| 2019 | [Control Barrier Functions: Theory and Applications](../catalog.md#paper-ames2019cbf) | [Paper](<https://doi.org/10.23919/ECC.2019.8796030>) |
| 2019 | [End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks](../catalog.md#paper-cheng2019endtoend) | [Paper](<https://doi.org/10.1609/aaai.v33i01.33013387>) |
| 2001 | [Using Simplicity to Control Complexity](../catalog.md#paper-sha2001simplicity) | Source metadata only |
| 2015 | [Hidden Technical Debt in Machine Learning Systems](../catalog.md#paper-sculley2015hidden) | Source metadata only |
| 2022 | [Defining and Characterizing Reward Gaming](../catalog.md#paper-skalse2022reward) | Source metadata only |
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |

<a id="argument-064"></a>

### A Four-Layer Reporting Protocol

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2024 | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../catalog.md#paper-hansen2024tdmpc2) | [Paper](<https://arxiv.org/abs/2310.16828>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../catalog.md#paper-openxembodiment2023) | [Paper](<https://arxiv.org/abs/2310.08864>) |
| 2024 | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../catalog.md#paper-khazatsky2024droid) | Source metadata only |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |

<a id="argument-065"></a>

### Evaluation by Role

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-066"></a>

### Evaluation by Learning Regime

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](../catalog.md#paper-dexmimicgen) | [Paper](<https://arxiv.org/abs/2410.24185>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2025 | [Robohorizon: An llm-assisted multi-view world model for long-horizon robotic manipulation](../catalog.md#paper-robohorizon2025) | [Paper](<https://arxiv.org/abs/2501.06605>) |
| 2023 | [TWIST: Teacher-Student World Model Distillation for Efficient Sim-to-Real Transfer](../catalog.md#paper-twist2023) | [Paper](<https://arxiv.org/abs/2311.03622>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2025 | [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../catalog.md#paper-zhou2025autoeval) | [Paper](<https://arxiv.org/abs/2503.24278>) |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

<a id="argument-067"></a>

### Evaluating Physical Fidelity: From Plausibility to Control Validity

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2026 | [Physics-IQ Verified](../catalog.md#paper-radsch2026physicsiqverified) | [Paper](<https://arxiv.org/abs/2606.18943>) |
| 2026 | [WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](../catalog.md#paper-shang2026worldarena) | [Paper](<https://arxiv.org/abs/2602.08971>) |
| 2026 | [Causally Debiased Latent Action Model for Embodied Action Conditioned World Models](../catalog.md#paper-wei2026cdlam) | [Paper](<https://arxiv.org/abs/2607.09185>) |
| 2026 | [Masked Visual Actions for Unified World Modeling](../catalog.md#paper-alzayer2026maskedvisual) | [Paper](<https://arxiv.org/abs/2607.19343>) |
| 2026 | [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](../catalog.md#paper-chen2026worldsync) | [Paper](<https://arxiv.org/abs/2608.24885>) |
| 2026 | [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](../catalog.md#paper-zhang2026physisforcing) | [Paper](<https://arxiv.org/abs/2606.28128>) |
| 2026 | [CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL](../catalog.md#paper-ni2026creflow) | [Paper](<https://arxiv.org/abs/2605.14274>) |
| 2026 | [EmboAlign: Aligning Video Generation with Compositional Constraints for Zero-Shot Manipulation](../catalog.md#paper-zhang2026emboalign) | [Paper](<https://arxiv.org/abs/2603.05757>) |
| 2026 | [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](../catalog.md#paper-yu2026howshould) | [Paper](<https://arxiv.org/abs/2606.15032>) |

<a id="argument-068"></a>

### Evidence Standards for Frontier Systems

| Year | Work | Primary entry |
|---|---|---|
| 2021 | [Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)](../catalog.md#paper-pineau2021improving) | [Paper](<https://jmlr.org/papers/v22/20-303.html>) |
| 2026 | [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](../catalog.md#paper-yu2026howshould) | [Paper](<https://arxiv.org/abs/2606.15032>) |

<a id="argument-069"></a>

### Minimum Evaluation Coverage with Runnable Fixtures

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](../catalog.md#paper-robosuite) | [Paper](<https://arxiv.org/abs/2009.12293>) |
| 2024 | [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](../catalog.md#paper-maniskill3) | [Paper](<https://arxiv.org/abs/2410.00425>) |
| 2025 | [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](../catalog.md#paper-chen2025robotwin2) | [Paper](<https://arxiv.org/abs/2506.18088>) |
| 2020 | [RLBench: The Robot Learning Benchmark and Learning Environment](../catalog.md#paper-james2020rlbench) | [Paper](<https://arxiv.org/abs/1909.12271>) |
| 2022 | [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](../catalog.md#paper-mees2022calvin) | [Paper](<https://arxiv.org/abs/2112.03227>) |
| 2026 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](../catalog.md#paper-nasiriany2026robocasa365) | [Paper](<https://arxiv.org/abs/2603.04356>) |
| 2026 | [Memory, Benchmark &amp; Robots: A Benchmark for Solving Complex Tasks with Reinforcement Learning](../catalog.md#paper-cherepanov2026mikasa) | [Paper](<https://arxiv.org/abs/2502.10550>) |
| 2026 | [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](../catalog.md#paper-dai2026robomme) | [Paper](<https://arxiv.org/abs/2603.04639>) |
| 2026 | [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](../catalog.md#paper-lei2026robomemarena) | [Paper](<https://arxiv.org/abs/2605.10921>) |
| 2019 | [Habitat: A platform for embodied ai research](../catalog.md#paper-habitat) | Source metadata only |
| 2017 | [Ai2-thor: An interactive 3d environment for visual ai](../catalog.md#paper-ai2thor) | [Paper](<https://arxiv.org/abs/1712.05474>) |
| 2024 | [HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](../catalog.md#paper-sferrazza2024humanoidbench) | [Paper](<https://doi.org/10.15607/RSS.2024.XX.061>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2026 | [WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](../catalog.md#paper-shang2026worldarena) | [Paper](<https://arxiv.org/abs/2602.08971>) |
| 2024 | [Robot Learning as an Empirical Science: Best Practices for Policy Evaluation](../catalog.md#paper-kressgazit2024empirical) | [Paper](<https://arxiv.org/abs/2409.09491>) |

<a id="argument-070"></a>

### Role-Conditioned Evidence Paths for Closed-Loop Claims

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [Objective Mismatch in Model-based Reinforcement Learning](../catalog.md#paper-lambert2020objective) | Source metadata only |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |

<a id="argument-071"></a>

### Role Ablations under the Query Distribution

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2024 | [Openvla: An open-source vision-language-action model](../catalog.md#paper-openvla2024) | [Paper](<https://arxiv.org/abs/2406.09246>) |
| 2026 | [Pointworld: Scaling 3d world models for in-the-wild robotic manipulation](../catalog.md#paper-pointworld2026) | [Paper](<https://arxiv.org/abs/2601.03782>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models](../catalog.md#paper-worldplanner2025) | [Paper](<https://arxiv.org/abs/2511.03077>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](../catalog.md#paper-robodreamer2024) | [Paper](<https://arxiv.org/abs/2404.12377>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2024 | [TD-MPC2: Scalable, Robust World Models for Continuous Control](../catalog.md#paper-hansen2024tdmpc2) | [Paper](<https://arxiv.org/abs/2310.16828>) |
| 2024 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](../catalog.md#paper-pi0) | [Paper](<https://arxiv.org/abs/2410.24164>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2026 | [Maskwam: Unifying mask prompting and prediction for world-action models](../catalog.md#paper-yu2026maskwam) | [Paper](<https://arxiv.org/abs/2606.13515>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |

<a id="argument-072"></a>

### The Evaluation Crisis: Toward Reproducible Closed-Loop Benchmarks

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2025 | [RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies](../catalog.md#paper-atreya2025roboarena) | [Paper](<https://arxiv.org/abs/2506.18123>) |
| 2025 | [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../catalog.md#paper-zhou2025autoeval) | [Paper](<https://arxiv.org/abs/2503.24278>) |
| 2024 | [Evaluating Real-World Robot Manipulation Policies in Simulation](../catalog.md#paper-li2024simpler) | [Paper](<https://arxiv.org/abs/2405.05941>) |
| 2025 | [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](../catalog.md#paper-yang2025embodiedbench) | [Paper](<https://arxiv.org/abs/2502.09560>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2025 | [WorldScore: A Unified Evaluation Benchmark for World Generation](../catalog.md#paper-duan2025worldscore) | [Paper](<https://arxiv.org/abs/2504.00983>) |
| 2024 | [VBench: Comprehensive Benchmark Suite for Video Generative Models](../catalog.md#paper-huang2024vbench) | [Paper](<https://arxiv.org/abs/2311.17982>) |
| 2025 | [VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness](../catalog.md#paper-zheng2025vbench2) | [Paper](<https://arxiv.org/abs/2503.21755>) |
| 2025 | [EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models](../catalog.md#paper-yue2025ewmbench) | [Paper](<https://arxiv.org/abs/2505.09694>) |

