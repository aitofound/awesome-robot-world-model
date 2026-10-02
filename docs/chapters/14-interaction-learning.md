# 14. From Interaction to Model Improvement

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Organize the outer loop as acquisition, update target, retention, failure curation and fleet sharing. Record whether feedback changes context, policy, physical parameters, neural dynamics or memory.

## Reading questions

- What data are acquired and under which policy?
- Which learner receives each supervision signal?
- What old-task behavior is retained?

## Interpretation boundary

A failed transition can teach dynamics while being an invalid behavior-cloning target. Actor RL and world-model SFT are different updates.

## Selected annotations

- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DreamerV3](../methods.md#paper-hafner2023dreamerv3)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [V-JEPA 2](../methods.md#paper-assran2025vjepa2)
- [Hi-WM](../methods.md#paper-li2026hiwm)
- [GE-Sim 2.0](../methods.md#paper-qiu2026gesim2)
- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [MuSe](../methods.md#paper-clark2026muse)
- [Zero-WAM](../methods.md#paper-zhou2026zerowam)
- [WAM-TTT](../methods.md#paper-feng2026wamttt)
- [VLAW](../methods.md#paper-vlaw2026)
- [WorldSample](../methods.md#paper-xue2026worldsample)
- [Sirius-Fleet](../methods.md#paper-liu2025siriusfleet)
- [REGEN](../methods.md#paper-govind2026regen)
- [Planning with Online World Models](../methods.md#paper-liu2025onlinewm)
- [World-in-World](../methods.md#paper-worldinworld2025)

## References by argument (99 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-088"></a>

### Formulation and Architecture of the Outer Loop

| Year | Work | Primary entry |
|---|---|---|
| 1991 | [Dyna, an Integrated Architecture for Learning, Planning, and Reacting](../catalog.md#paper-sutton1991dyna) | Source metadata only |
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2019 | [Deep Dynamics Models for Learning Dexterous Manipulation](../catalog.md#paper-nagabandi2019pddm) | [Paper](<https://arxiv.org/abs/1909.11652>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2018 | [Augmenting Physical Simulators with Stochastic Neural Networks: Case Study of Planar Pushing and Bouncing](../catalog.md#paper-ajay2018residual) | [Paper](<https://arxiv.org/abs/1808.03246>) |
| 2025 | [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](../catalog.md#paper-he2025asap) | [Paper](<https://arxiv.org/abs/2502.01143>) |
| 2019 | [Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience](../catalog.md#paper-chebotar2019simopt) | [Paper](<https://arxiv.org/abs/1810.05687>) |
| 2020 | [TossingBot: Learning to Throw Arbitrary Objects with Residual Physics](../catalog.md#paper-zeng2019tossingbot) | [Paper](<https://arxiv.org/abs/1903.11239>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |
| 2026 | [Robot Self-Improvement via Human-Video Dynamics Models](../catalog.md#paper-dgac2026) | [Paper](<https://arxiv.org/abs/2606.21406>) |
| 2023 | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](../catalog.md#paper-bousmalis2023robocat) | [Paper](<https://arxiv.org/abs/2306.11706>) |
| 2025 | [EvoVLA: Self-Evolving Vision-Language-Action Model](../catalog.md#paper-liu2025evovla) | [Paper](<https://arxiv.org/abs/2511.16166>) |
| 2025 | [π^\*_0.6: a VLA That Learns From Experience](../catalog.md#paper-pi2025pistar06) | [Paper](<https://arxiv.org/abs/2511.14759>) |
| 2025 | [Robot learning on the job: Human-in-the-loop autonomy and learning during deployment](../catalog.md#paper-sirius2022) | [Paper](<https://doi.org/10.15607/RSS.2023.XIX.005>) |
| 2025 | [Multi-Task Interactive Robot Fleet Learning with Visual World Models](../catalog.md#paper-liu2025siriusfleet) | [Paper](<https://proceedings.mlr.press/v270/liu25g.html>) |
| 2026 | [Self-Evolving World Models for LLM Agent Planning](../catalog.md#paper-zhang2026worldevolver) | [Paper](<https://arxiv.org/abs/2606.30639>) |
| 2017 | [Value-Aware Loss Function for Model-based Reinforcement Learning](../catalog.md#paper-farahmand2017vaml) | Source metadata only |
| 2020 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](../catalog.md#paper-grimm2020value) | Source metadata only |
| 2020 | [Objective Mismatch in Model-based Reinforcement Learning](../catalog.md#paper-lambert2020objective) | Source metadata only |
| 2026 | [Safety, Security, and Cognitive Risks in World Models](../catalog.md#paper-worldmodelrisks2026) | [Paper](<https://arxiv.org/abs/2604.01346>) |

<a id="argument-089"></a>

### Autonomous Exploration and Active Interaction

| Year | Work | Primary entry |
|---|---|---|
| 2017 | [Curiosity-driven Exploration by Self-supervised Prediction](../catalog.md#paper-pathak2017icm) | [Paper](<https://arxiv.org/abs/1705.05363>) |
| 2019 | [Exploration by Random Network Distillation](../catalog.md#paper-burda2018rnd) | [Paper](<https://arxiv.org/abs/1810.12894>) |
| 2019 | [Self-Supervised Exploration via Disagreement](../catalog.md#paper-pathak2019disagreement) | [Paper](<https://arxiv.org/abs/1906.04161>) |
| 2020 | [Planning to Explore via Self-Supervised World Models](../catalog.md#paper-sekar2020plan2explore) | [Paper](<https://arxiv.org/abs/2005.05960>) |
| 2021 | [Discovering and Achieving Goals via World Models](../catalog.md#paper-mendonca2021lexa) | [Paper](<https://arxiv.org/abs/2110.09514>) |
| 2022 | [Curious Exploration via Structured World Models Yields Zero-Shot Object Manipulation](../catalog.md#paper-sancaktar2022ceeus) | [Paper](<https://arxiv.org/abs/2206.11403>) |
| 2019 | [Active Learning of Dynamics for Data-Driven Control Using Koopman Operators](../catalog.md#paper-abraham2019active) | [Paper](<https://doi.org/10.1109/TRO.2019.2923880>) |
| 2020 | [Reward-Free Exploration for Reinforcement Learning](../catalog.md#paper-jin2020rewardfree) | [Paper](<https://proceedings.mlr.press/v119/jin20d.html>) |
| 2022 | [Deciding What to Model: Value-Equivalent Sampling for Reinforcement Learning](../catalog.md#paper-arumugam2022deciding) | [Paper](<https://arxiv.org/abs/2206.02072>) |
| 2022 | [Between Rate-Distortion Theory &amp; Value Equivalence in Model-Based Reinforcement Learning](../catalog.md#paper-arumugam2022ratedistortion) | [Paper](<https://arxiv.org/abs/2206.02025>) |
| 2018 | [Leave no Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning](../catalog.md#paper-eysenbach2018leavenotrace) | [Paper](<https://arxiv.org/abs/1711.06782>) |
| 2021 | [Reset-Free Reinforcement Learning via Multi-Task Learning: Learning Dexterous Manipulation Behaviors without Human Intervention](../catalog.md#paper-gupta2021resetfree) | [Paper](<https://arxiv.org/abs/2104.11203>) |
| 2022 | [Autonomous Reinforcement Learning: Formalism and Benchmarking](../catalog.md#paper-sharma2022autonomous) | Source metadata only |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2023 | [ALAN: Autonomously Exploring Robotic Agents in the Real World](../catalog.md#paper-mendonca2023alan) | [Paper](<https://arxiv.org/abs/2302.06604>) |
| 2023 | [Structured World Models from Human Videos](../catalog.md#paper-mendonca2023swim) | [Paper](<https://arxiv.org/abs/2308.10901>) |
| 2026 | [PlayWorld: Learning Robot World Models from Autonomous Play](../catalog.md#paper-yin2026playworld) | [Paper](<https://arxiv.org/abs/2603.09030>) |

<a id="argument-090"></a>

### Continual Learning and Online Model Updating

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation](../catalog.md#paper-zhao2026ttswam) | [Paper](<https://arxiv.org/abs/2607.17454>) |
| 2026 | [Stream-T1: Test-Time Scaling for Streaming Video Generation](../catalog.md#paper-tu2026streamt1) | [Paper](<https://arxiv.org/abs/2605.04461>) |
| 2011 | [PILCO: A Model-Based and Data-Efficient Approach to Policy Search](../catalog.md#paper-deisenroth2011pilco) | Source metadata only |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2019 | [Learning to Adapt in Dynamic, Real-World Environments Through Meta-Reinforcement Learning](../catalog.md#paper-nagabandi2019adapt) | [Paper](<https://arxiv.org/abs/1803.11347>) |
| 2019 | [Deep Online Learning via Meta-Learning: Continual Adaptation for Model-Based RL](../catalog.md#paper-nagabandi2019mole) | [Paper](<https://arxiv.org/abs/1812.07671>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2023 | [Structured World Models from Human Videos](../catalog.md#paper-mendonca2023swim) | [Paper](<https://arxiv.org/abs/2308.10901>) |
| 2019 | [Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience](../catalog.md#paper-chebotar2019simopt) | [Paper](<https://arxiv.org/abs/1810.05687>) |
| 2024 | [AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation](../catalog.md#paper-zhang2024adaptigraph) | [Paper](<https://arxiv.org/abs/2407.07889>) |
| 2020 | [Context-aware Dynamics Model for Generalization in Model-Based Reinforcement Learning](../catalog.md#paper-lee2020cadm) | [Paper](<https://arxiv.org/abs/2005.06800>) |
| 2024 | [Dynamics as Prompts: In-Context Learning for Sim-to-Real System Identifications](../catalog.md#paper-zhang2024dynprompt) | [Paper](<https://arxiv.org/abs/2410.20357>) |
| 2025 | [s1: Simple test-time scaling](../catalog.md#paper-muennighoff2025s1) | [Paper](<https://arxiv.org/abs/2501.19393>) |
| 2022 | [A Generalist Agent](../catalog.md#paper-reed2022gato) | [Paper](<https://arxiv.org/abs/2205.06175>) |
| 2023 | [In-context Reinforcement Learning with Algorithm Distillation](../catalog.md#paper-laskin2023distillation) | Source metadata only |
| 2023 | [Human-Timescale Adaptation in an Open-Ended Task Space](../catalog.md#paper-bauer2023ada) | Source metadata only |
| 2024 | [In-Context Imitation Learning via Next-Token Prediction](../catalog.md#paper-fu2024icrt) | [Paper](<https://arxiv.org/abs/2408.15980>) |
| 2024 | [Instant Policy: In-Context Imitation Learning via Graph Diffusion](../catalog.md#paper-vosylius2024instantpolicy) | [Paper](<https://arxiv.org/abs/2411.12633>) |
| 2026 | [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../catalog.md#paper-zhou2026zerowam) | [Paper](<https://arxiv.org/abs/2608.26103>) |
| 2026 | [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](../catalog.md#paper-feng2026wamttt) | [Paper](<https://arxiv.org/abs/2607.06988>) |
| 2024 | [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](../catalog.md#paper-sun2024ttt) | [Paper](<https://arxiv.org/abs/2407.04620>) |
| 2026 | [RoboTTT: Context Scaling for Robot Policies](../catalog.md#paper-jiang2026robottt) | [Paper](<https://arxiv.org/abs/2607.15275>) |
| 2026 | [In-Context World Modeling for Robotic Control](../catalog.md#paper-icwm2026) | [Paper](<https://arxiv.org/abs/2606.26025>) |
| 2025 | [LocoFormer: Generalist Locomotion via Long-context Adaptation](../catalog.md#paper-locoformer2025) | Source metadata only |
| 2025 | [Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning](../catalog.md#paper-sgft2025) | Source metadata only |
| 2026 | [xTED: Cross-Domain Adaptation via Diffusion-Based Trajectory Editing](../catalog.md#paper-xted2026) | [Paper](<https://doi.org/10.65109/BENP4894>) |
| 2025 | [Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids](../catalog.md#paper-rtr2025) | Source metadata only |
| 2026 | [On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning](../catalog.md#paper-ontheflyvla2026) | [Paper](<https://doi.org/10.18653/v1/2026.acl-long.1863>) |
| 2026 | [Zeva: In-Context Causal Learning for Generalizable Embodied Manipulation](../catalog.md#paper-chen2026zeva) | [Paper](<https://arxiv.org/abs/2608.30880>) |
| 2026 | [Self-Evolving World Models for LLM Agent Planning](../catalog.md#paper-zhang2026worldevolver) | [Paper](<https://arxiv.org/abs/2606.30639>) |
| 2026 | [Zetta: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](../catalog.md#paper-ding2026zetta) | [Paper](<https://arxiv.org/abs/2608.16590>) |
| 2026 | [Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training](../catalog.md#paper-li2026hiwm) | [Paper](<https://arxiv.org/abs/2604.21741>) |
| 2022 | [Continual Predictive Learning from Videos](../catalog.md#paper-chen2022cpl) | [Paper](<https://arxiv.org/abs/2204.05624>) |
| 2025 | [Continual Reinforcement Learning by Planning with Online World Models](../catalog.md#paper-liu2025onlinewm) | [Paper](<https://arxiv.org/abs/2507.09177>) |
| 2026 | [World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays](../catalog.md#paper-govind2026regen) | [Paper](<https://arxiv.org/abs/2606.27374>) |
| 2026 | [Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force](../catalog.md#paper-clark2026muse) | [Paper](<https://arxiv.org/abs/2606.30988>) |

<a id="argument-091"></a>

### Failure Mining and Experience Curation

| Year | Work | Primary entry |
|---|---|---|
| 2016 | [Prioritized Experience Replay](../catalog.md#paper-schaul2015per) | [Paper](<https://arxiv.org/abs/1511.05952>) |
| 2023 | [Curious Replay for Model-based Adaptation](../catalog.md#paper-kauvar2023curious) | [Paper](<https://arxiv.org/abs/2306.15934>) |
| 2026 | [Robot Self-Improvement via Human-Video Dynamics Models](../catalog.md#paper-dgac2026) | [Paper](<https://arxiv.org/abs/2606.21406>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |
| 2026 | [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](../catalog.md#paper-qiu2026gesim2) | [Paper](<https://arxiv.org/abs/2605.27491>) |
| 2026 | [RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](../catalog.md#paper-robocurate2026) | [Paper](<https://arxiv.org/abs/2602.18742>) |
| 2025 | [Robot Data Curation with Mutual Information Estimators](../catalog.md#paper-hejna2025deminf) | [Paper](<https://arxiv.org/abs/2502.08623>) |
| 2011 | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../catalog.md#paper-ross2011dagger) | [Paper](<https://proceedings.mlr.press/v15/ross11a.html>) |
| 2025 | [Robot learning on the job: Human-in-the-loop autonomy and learning during deployment](../catalog.md#paper-sirius2022) | [Paper](<https://doi.org/10.15607/RSS.2023.XIX.005>) |
| 2022 | [ThriftyDAgger: Budget-Aware Novelty and Risk Gating for Interactive Imitation Learning](../catalog.md#paper-hoque2022thrifty) | [Paper](<https://proceedings.mlr.press/v164/hoque22a.html>) |
| 2023 | [Reflect: Summarizing robot experiences for failure explanation and correction](../catalog.md#paper-liu2023reflect) | [Paper](<https://arxiv.org/abs/2306.15724>) |
| 2024 | [Aha: A vision-language-model for detecting and reasoning over failures in robotic manipulation](../catalog.md#paper-duan2024aha) | [Paper](<https://arxiv.org/abs/2410.00371>) |
| 2025 | [A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning](../catalog.md#paper-vlac2025) | [Paper](<https://arxiv.org/abs/2509.15937>) |
| 2025 | [ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations](../catalog.md#paper-rewind2025) | [Paper](<https://arxiv.org/abs/2505.10911>) |
| 2024 | [Eureka: Human-Level Reward Design via Coding Large Language Models](../catalog.md#paper-ma2023eureka) | [Paper](<https://arxiv.org/abs/2310.12931>) |
| 2024 | [AI models collapse when trained on recursively generated data](../catalog.md#paper-shumailov2024collapse) | [Paper](<https://doi.org/10.1038/s41586-024-07566-y>) |
| 2024 | [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](../catalog.md#paper-gerstgrasser2024collapse) | [Paper](<https://arxiv.org/abs/2404.01413>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

<a id="argument-092"></a>

### Fleet Learning and Scaled Deployment

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [RoboNet: Large-Scale Multi-Robot Learning](../catalog.md#paper-robonet) | [Paper](<https://arxiv.org/abs/1910.11215>) |
| 2025 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../catalog.md#paper-assran2025vjepa2) | [Paper](<https://arxiv.org/abs/2506.09985>) |
| 2024 | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](../catalog.md#paper-khazatsky2024droid) | Source metadata only |
| 2025 | [Data Scaling Laws in Imitation Learning for Robotic Manipulation](../catalog.md#paper-lin2024datascaling) | [Paper](<https://arxiv.org/abs/2410.18647>) |
| 2026 | [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../catalog.md#paper-zhou2026zerowam) | [Paper](<https://arxiv.org/abs/2608.26103>) |
| 2024 | [Learning Interactive Real-World Simulators](../catalog.md#paper-yang2024unisim) | [Paper](<https://arxiv.org/abs/2310.06114>) |
| 2026 | [Ctrl-world: A controllable generative world model for robot manipulation](../catalog.md#paper-guo2026ctrl) | Source metadata only |
| 2025 | [Multi-Task Interactive Robot Fleet Learning with Visual World Models](../catalog.md#paper-liu2025siriusfleet) | [Paper](<https://proceedings.mlr.press/v270/liu25g.html>) |
| 2018 | [QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation](../catalog.md#paper-kalashnikov2018qtopt) | [Paper](<https://arxiv.org/abs/1806.10293>) |
| 2024 | [Robot Fleet Learning via Policy Merging](../catalog.md#paper-wang2023fleetmerge) | [Paper](<https://arxiv.org/abs/2310.01362>) |
| 2022 | [Fleet-DAgger: Interactive Robot Fleet Learning with Scalable Human Supervision](../catalog.md#paper-hoque2022fleetdagger) | [Paper](<https://arxiv.org/abs/2206.14349>) |
| 2024 | [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](../catalog.md#paper-ahn2024autort) | [Paper](<https://arxiv.org/abs/2401.12963>) |
| 2025 | [Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems](../catalog.md#paper-bu2025agibot) | [Paper](<https://arxiv.org/abs/2503.06669>) |
| 2023 | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](../catalog.md#paper-bousmalis2023robocat) | [Paper](<https://arxiv.org/abs/2306.11706>) |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2022 | [Failure Prediction with Statistical Guarantees for Vision-Based Robot Control](../catalog.md#paper-farid2022failure) | Source metadata only |
| 2023 | [Closing the loop on runtime monitors with fallback-safe MPC](../catalog.md#paper-sinha2023closing) | Source metadata only |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

