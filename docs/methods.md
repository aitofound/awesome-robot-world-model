# Annotated methods and context

[Home](../README.md) · [Role views](roles.md) · [Full catalog](catalog.md)

Annotations are original syntheses of the companion survey. `world-model-use` identifies a discussed predictive use, not an automatic certificate of strict closed-loop qualification. Other kinds explicitly retain representation priors, policy context, general generation and benchmark literature.

Read the interface, consumer and boundary together. Paper metadata checks do not independently verify these mechanism annotations.

<a id="paper-ha2018worldmodels"></a>

## World Models

**World Models** (2018). [Paper](<https://arxiv.org/abs/1803.10122>) · [Catalog record](catalog.md#paper-ha2018worldmodels)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** A compressed visual state and recurrent predictive dynamics.

**Consumer and changed object.** A controller consumes the learned state and predictive environment.

**Evidence boundary.** Early non-robot control evidence supplies conceptual background; do not infer general robot deployment.

**Cited in:** [03](chapters/03-foundations.md).

**Argument contexts:** [A Robot Learning Loop View of World Models](chapters/03-foundations.md#argument-007).

<a id="paper-hafner2019planet"></a>

## PlaNet

**Learning Latent Dynamics for Planning from Pixels** (2019). [Paper](<https://arxiv.org/abs/1811.04551>) · [Catalog record](catalog.md#paper-hafner2019planet)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Action-conditioned latent dynamics predict future states and rewards.

**Consumer and changed object.** Online planning selects actions through imagined latent trajectories.

**Evidence boundary.** Separate model fit, planning cost and downstream control performance.

**Cited in:** [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [15](chapters/15-research-agenda.md), [04](chapters/04-roles.md).

**Argument contexts:** [Prediction and imagination: what futures can be queried?](chapters/04-roles.md#argument-012) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Robotics Scaling Laws](chapters/15-research-agenda.md#argument-099).

<a id="paper-hafner2019dreamer"></a>

## Dreamer

**Dream to Control: Learning Behaviors by Latent Imagination** (2020). [Paper](<https://arxiv.org/abs/1912.01603>) · [Catalog record](catalog.md#paper-hafner2019dreamer)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** A latent dynamics model supplies imagined trajectories.

**Consumer and changed object.** Actor and value learning use imagination; the deployed actor can act without an explicit rollout planner.

**Evidence boundary.** Learning-time imagination and execution-time replanning are different interfaces.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [03](chapters/03-foundations.md), [14](chapters/14-interaction-learning.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [A Robot Learning Loop View of World Models](chapters/03-foundations.md#argument-007) · [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Prediction and imagination: what futures can be queried?](chapters/04-roles.md#argument-012) · [Evaluation, reward, and safety: what to reinforce or reject?](chapters/04-roles.md#argument-015) · [System Design Patterns](chapters/04-roles.md#argument-017) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Why Vision-Only World Models Fail at Contact](chapters/08-tactile-contact.md#argument-043) · [Model Quality](chapters/11-evaluation.md#argument-061) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) · [Paper Selection Protocol](chapters/a-review-protocol.md#argument-111).

<a id="paper-hafner2021dreamerv2"></a>

## DreamerV2

**Mastering Atari with Discrete World Models** (2021). [Paper](<https://arxiv.org/abs/2010.02193>) · [Catalog record](catalog.md#paper-hafner2021dreamerv2)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Discrete latent dynamics support imagined behavior learning.

**Consumer and changed object.** Imagination updates the actor and value function.

**Evidence boundary.** Atari evidence is methodological context, not physical robot validation.

**Cited in:** [05](chapters/05-representations.md).

**Argument contexts:** [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024).

<a id="paper-hafner2023dreamerv3"></a>

## DreamerV3

**Mastering Diverse Domains through World Models** (2023). [Paper](<https://arxiv.org/abs/2301.04104>) · [Catalog record](catalog.md#paper-hafner2023dreamerv3)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** A latent world model supports behavior learning across domains.

**Consumer and changed object.** Model-generated trajectories train behavior and value estimates.

**Evidence boundary.** Cross-domain success does not remove embodiment, contact or real-time evaluation requirements.

**Cited in:** [11](chapters/11-evaluation.md), [03](chapters/03-foundations.md), [14](chapters/14-interaction-learning.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md).

**Argument contexts:** [Introduction](chapters/01-introduction.md#argument-001) · [A Robot Learning Loop View of World Models](chapters/03-foundations.md#argument-007) · [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Policy Utility](chapters/11-evaluation.md#argument-062) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088).

**Upstream resource:** [DreamerV3](https://github.com/danijar/dreamerv3).

<a id="paper-hafner2025dreamer4"></a>

## Dreamer4

**Training Agents Inside of Scalable World Models** (2025). [Paper](<https://arxiv.org/abs/2509.24527>) · [Catalog record](catalog.md#paper-hafner2025dreamer4)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Scalable world-model-generated experience for agent training.

**Consumer and changed object.** Policies learn inside a predictive environment.

**Evidence boundary.** Distinguish scalable agent-training evidence from robot-specific action grounding and hardware transfer.

**Cited in:** [13](chapters/13-frontier-atlas.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Memory and Long-Horizon World Models](chapters/15-research-agenda.md#argument-097).

<a id="paper-wu2022daydreamer"></a>

## DayDreamer

**DayDreamer: World Models for Physical Robot Learning** (2022). [Paper](<https://arxiv.org/abs/2206.14176>) · [Catalog record](catalog.md#paper-wu2022daydreamer)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** A learned predictive model uses physical robot interaction data.

**Consumer and changed object.** Imagined experience supports robot policy learning.

**Evidence boundary.** Robot and task conditions bound the results; physical learning does not imply universal embodiment transfer.

**Cited in:** [11](chapters/11-evaluation.md), [03](chapters/03-foundations.md), [14](chapters/14-interaction-learning.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [A](chapters/a-review-protocol.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Introduction](chapters/01-introduction.md#argument-001) · [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Vision-Only World Models Fail at Contact](chapters/08-tactile-contact.md#argument-043) · [Policy Utility](chapters/11-evaluation.md#argument-062) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) · [Autonomous Exploration and Active Interaction](chapters/14-interaction-learning.md#argument-089) · [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090) · [Paper Selection Protocol](chapters/a-review-protocol.md#argument-111).

**Upstream resource:** [DayDreamer](https://github.com/danijar/daydreamer).

<a id="paper-hansen2024tdmpc2"></a>

## TD-MPC2

**TD-MPC2: Scalable, Robust World Models for Continuous Control** (2024). [Paper](<https://arxiv.org/abs/2310.16828>) · [Catalog record](catalog.md#paper-hansen2024tdmpc2)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Latent predictive dynamics and value estimates support continuous control.

**Consumer and changed object.** Model-predictive control selects actions.

**Evidence boundary.** Report action-space, horizon and compute settings rather than comparing raw success across unrelated tasks.

**Cited in:** [11](chapters/11-evaluation.md), [06](chapters/06-learning-regimes.md).

**Argument contexts:** [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Policy Utility](chapters/11-evaluation.md#argument-062) · [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071).

<a id="paper-zhou2025dinowm"></a>

## DINO-WM

**DINO-WM: World Models on Pre-trained Visual Features Enable Zero-Shot Planning** (2025). [Paper](<https://arxiv.org/abs/2411.04983>) · [Catalog record](catalog.md#paper-zhou2025dinowm)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Action-conditioned prediction operates on pretrained visual features.

**Consumer and changed object.** Planning consumes predicted features to select controls.

**Evidence boundary.** Visual feature pretraining alone is not action-grounded dynamics or proof of closed-loop utility.

**Cited in:** [05](chapters/05-representations.md), [04](chapters/04-roles.md).

**Argument contexts:** [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [The Representation Question: What Should a World Model Encode](chapters/05-representations.md#argument-019) · [Latent Representations: Learning Compact Predictive States](chapters/05-representations.md#argument-020).

**Upstream resource:** [DINO-WM](https://github.com/gaoyuezhou/dino_wm).

<a id="paper-assran2025vjepa2"></a>

## V-JEPA 2

**V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** (2025). [Paper](<https://arxiv.org/abs/2506.09985>) · [Catalog record](catalog.md#paper-assran2025vjepa2)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Video predictive representations are adapted for action-conditioned use.

**Consumer and changed object.** A planning consumer connects predictions to robotic decisions.

**Evidence boundary.** Keep generic video pretraining separate from the action-conditioned robot adaptation experiment.

**Cited in:** [13](chapters/13-frontier-atlas.md), [14](chapters/14-interaction-learning.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [The Representation Question: What Should a World Model Encode](chapters/05-representations.md#argument-019) · [Latent Representations: Learning Compact Predictive States](chapters/05-representations.md#argument-020) · [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092) · [The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility](chapters/15-research-agenda.md#argument-093).

**Upstream resource:** [V-JEPA 2](https://github.com/facebookresearch/vjepa2).

<a id="paper-actjepa2025"></a>

## ACT-JEPA

**ACT-JEPA: Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning** (2025). [Paper](<https://arxiv.org/abs/2501.14622>) · [Catalog record](catalog.md#paper-actjepa2025)

**Kind:** `representation-prior`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** A joint-embedding predictive objective learns policy-relevant representations.

**Consumer and changed object.** Representation learning affects downstream policy learning.

**Evidence boundary.** A predictive representation objective does not by itself establish online action search.

**Cited in:** [15](chapters/15-research-agenda.md).

**Argument contexts:** [Inference Efficiency and the Latency Wall](chapters/15-research-agenda.md#argument-095).

<a id="paper-nam2026causaljepa"></a>

## Causal-JEPA

**Causal-JEPA: Learning World Models through Object-Level Latent Masking** (2026). [Paper](<https://arxiv.org/abs/2602.11389>) · [Catalog record](catalog.md#paper-nam2026causaljepa)

**Kind:** `representation-prior`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Object-level latent masking learns predictive dependencies.

**Consumer and changed object.** Downstream uses consume object-aware predictive representations.

**Evidence boundary.** The name does not establish identification of a causal graph or valid causal interventions.

**Cited in:** [05](chapters/05-representations.md).

**Argument contexts:** [Causal Representations](chapters/05-representations.md#argument-023).

<a id="paper-liu2026odeworld"></a>

## ODEWorld

**ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow** (2026). [Paper](<https://arxiv.org/abs/2607.27924>) · [Catalog record](catalog.md#paper-liu2026odeworld)

**Kind:** `generative-context`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Observation- and goal-conditioned prediction uses continuous physical-time flow.

**Consumer and changed object.** The interface predicts futures at physical-time queries.

**Evidence boundary.** The reviewed interface does not accept queried candidate actions; do not label it an action-intervention planner.

**Cited in:** [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md).

**Argument contexts:** [Latent Representations: Learning Compact Predictive States](chapters/05-representations.md#argument-020) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [From Video Generation to Controllable World Models](chapters/05-representations.md#argument-025) · [Imitation Learning and Behavior Cloning](chapters/06-learning-regimes.md#argument-026).

<a id="paper-pointworld2026"></a>

## PointWorld

**Pointworld: Scaling 3d world models for in-the-wild robotic manipulation** (2026). [Paper](<https://arxiv.org/abs/2601.03782>) · [Catalog record](catalog.md#paper-pointworld2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** A 3D point-based world model predicts action consequences.

**Consumer and changed object.** MPPI planning produces robot action sequences.

**Evidence boundary.** The reported physical execution is open loop; model inference time excludes the full planning pipeline.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [12](chapters/12-resources.md), [04](chapters/04-roles.md).

**Argument contexts:** [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [Geometric Representations: Making 3D Structure Explicit](chapters/05-representations.md#argument-021) · [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Representation Priors: State Abstractions for Control](chapters/07-foundation-priors.md#argument-035) · [Embodiment and Task Perspective](chapters/10-embodiments.md#argument-054) · [Manipulation](chapters/10-embodiments.md#argument-055) · [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Resource Cards › Learned Simulators and World Foundation Models](chapters/12-resources.md#argument-077) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087).

<a id="paper-jiang2025phystwin"></a>

## PhysTwin

**PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos** (2025). [Paper](<https://arxiv.org/abs/2503.17973>) · [Catalog record](catalog.md#paper-jiang2025phystwin)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Video observations inform structured deformable-object physics reconstruction.

**Consumer and changed object.** The reconstructed simulation supports interaction reasoning.

**Evidence boundary.** Physics reconstruction and a complete learned robot control loop require separate evidence.

**Cited in:** [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [05](chapters/05-representations.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Physical Representations: Encoding Dynamics and Constraints](chapters/05-representations.md#argument-022) · [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100).

<a id="paper-worldplanner2025"></a>

## WorldPlanner

**Worldplanner: Monte carlo tree search and mpc with action-conditioned visual world models** (2025). [Paper](<https://arxiv.org/abs/2511.03077>) · [Catalog record](catalog.md#paper-worldplanner2025)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Action-conditioned visual prediction supports search over futures.

**Consumer and changed object.** Global Monte Carlo tree search and local MPC choose actions.

**Evidence boundary.** Learned-state PushT comparisons and demonstration baselines should not be treated as a common cross-paper leaderboard.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Prediction and imagination: what futures can be queried?](chapters/04-roles.md#argument-012) · [Planning and search: which action to execute now?](chapters/04-roles.md#argument-014) · [System Design Patterns](chapters/04-roles.md#argument-017) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) · [Embodiment and Task Perspective](chapters/10-embodiments.md#argument-054) · [Manipulation](chapters/10-embodiments.md#argument-055) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-chen2025largevideoplanner"></a>

## Large Video Planner

**Large video planner enables generalizable robot control** (2025). [Paper](<https://arxiv.org/abs/2512.15840>) · [Catalog record](catalog.md#paper-chen2025largevideoplanner)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Generated visual plans are converted into executable robot motion.

**Consumer and changed object.** Retargeting produces actions for physical execution.

**Evidence boundary.** Plan generation and retargeting are followed by open-loop execution; do not infer real-time feedback correction.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [03](chapters/03-foundations.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Planning and search: which action to execute now?](chapters/04-roles.md#argument-014) · [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) · [Why Vision-Only World Models Fail at Contact](chapters/08-tactile-contact.md#argument-043) · [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) · [Role-Conditioned Evidence Paths for Closed-Loop Claims](chapters/11-evaluation.md#argument-070) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-robodreamer2024"></a>

## RoboDreamer

**RoboDreamer: Learning Compositional World Models for Robot Imagination** (2024). [Paper](<https://arxiv.org/abs/2404.12377>) · [Catalog record](catalog.md#paper-robodreamer2024)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Compositional robot imagination predicts visual task futures.

**Consumer and changed object.** Predicted futures provide a task-facing imagination interface.

**Evidence boundary.** Compositional generation must be assessed separately from decision coupling and execution feedback.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [05](chapters/05-representations.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [Prediction and imagination: what futures can be queried?](chapters/04-roles.md#argument-012) · [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-li2025roboticworldmodel"></a>

## Robotic World Model (RWM)

**Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics** (2025). [Paper](<https://arxiv.org/abs/2501.10100>) · [Catalog record](catalog.md#paper-li2025roboticworldmodel)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** A learned neural simulator predicts robot interaction consequences.

**Consumer and changed object.** MBPO-PPO optimizes policies using model-generated experience.

**Evidence boundary.** The studied pipeline uses physics-simulator data and interactions; hardware transfer is not simulator-free training.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [03](chapters/03-foundations.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md).

**Argument contexts:** [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Policy Utility](chapters/11-evaluation.md#argument-062) · [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md#argument-073) · [Frontier Resource Cards › Learned Simulators and World Foundation Models](chapters/12-resources.md#argument-077) · [Resource Gaps for 2026-Ready Robot World Models](chapters/12-resources.md#argument-082) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-interactiveworldsim2026"></a>

## Interactive World Simulator (IWS)

**Interactive World Simulator for Robot Policy Training and Evaluation** (2026). [Paper](<https://arxiv.org/abs/2603.08546>) · [Catalog record](catalog.md#paper-interactiveworldsim2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** An interactive predictive environment supports demonstrations and evaluation.

**Consumer and changed object.** Generated demonstrations train downstream robot policies.

**Evidence boundary.** Equal demonstration-set sizes exclude world-model construction cost and do not establish online RL.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Evaluation, reward, and safety: what to reinforce or reject?](chapters/04-roles.md#argument-015) · [Imitation Learning and Behavior Cloning](chapters/06-learning-regimes.md#argument-026) · [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Manipulation](chapters/10-embodiments.md#argument-055) · [Policy Utility](chapters/11-evaluation.md#argument-062) · [Evaluation by Role](chapters/11-evaluation.md#argument-065) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Resource Cards › Learned Simulators and World Foundation Models](chapters/12-resources.md#argument-077) · [Resource Gaps for 2026-Ready Robot World Models](chapters/12-resources.md#argument-082) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-li2026hiwm"></a>

## Hi-WM

**Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training** (2026). [Paper](<https://arxiv.org/abs/2604.21741>) · [Catalog record](catalog.md#paper-li2026hiwm)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Rollback and branching inside a world model enable targeted human corrections.

**Consumer and changed object.** Corrected trajectories support robot policy post-training.

**Evidence boundary.** The mechanism uses human correction; gains do not establish unattended synthetic data collection.

**Cited in:** [10](chapters/10-embodiments.md), [07](chapters/07-foundation-priors.md), [14](chapters/14-interaction-learning.md), [12](chapters/12-resources.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Human-Robot Interaction &amp; Correctable Autonomy](chapters/10-embodiments.md#argument-060) · [What Resources Should Enable: Four Capability Dimensions](chapters/12-resources.md#argument-083) · [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090).

<a id="paper-qiu2026gesim2"></a>

## GE-Sim 2.0

**GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation** (2026). [Paper](<https://arxiv.org/abs/2605.27491>) · [Catalog record](catalog.md#paper-qiu2026gesim2)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Video prediction is coupled to proprioceptive state and task-feedback modules.

**Consumer and changed object.** Successful-rollout filtering supplies behavior-cloning updates.

**Evidence boundary.** The cited physical improvement is filtered supervised learning, not an online-RL experiment.

**Cited in:** [07](chapters/07-foundation-priors.md), [14](chapters/14-interaction-learning.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Failure Mining and Experience Curation](chapters/14-interaction-learning.md#argument-091) · [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103).

<a id="paper-gu2026geniworld"></a>

## GeniWorld

**GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions** (2026). [Paper](<https://arxiv.org/abs/2608.06332>) · [Catalog record](catalog.md#paper-gu2026geniworld)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Rendered robot motion grounds action-conditioned visual prediction.

**Consumer and changed object.** Synthetic condition augmentation supports policy improvement.

**Evidence boundary.** The reported overall average mixes standard and OOD settings; it is not an OOD-only score.

**Cited in:** [07](chapters/07-foundation-priors.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038).

<a id="paper-jang2025dreamgen"></a>

## DreamGen

**DreamGen: Unlocking Generalization in Robot Learning through Video World Models** (2025). [Paper](<https://arxiv.org/abs/2505.12705>) · [Catalog record](catalog.md#paper-jang2025dreamgen)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Video-generated behavior is paired with recovered pseudo-actions.

**Consumer and changed object.** Synthetic demonstrations supply policy-training supervision.

**Evidence boundary.** Pseudo-action recovery and trajectory validity are essential; video quality alone is not training utility.

**Cited in:** [10](chapters/10-embodiments.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [09](chapters/09-human-egocentric.md), [14](chapters/14-interaction-learning.md), [05](chapters/05-representations.md), [15](chapters/15-research-agenda.md), [04](chapters/04-roles.md).

**Argument contexts:** [Simulation &amp; Data Generation: how can models provide experience?](chapters/04-roles.md#argument-013) · [From Video Generation to Controllable World Models](chapters/05-representations.md#argument-025) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051) · [Humanoid Locomotion &amp; Loco-Manipulation](chapters/10-embodiments.md#argument-057) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100).

**Upstream resource:** [DreamGen / GR00T Dreams](https://github.com/NVIDIA/GR00T-dreams).

<a id="paper-gao2026dreamdojo"></a>

## DreamDojo

**DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos** (2026). [Paper](<https://arxiv.org/abs/2602.06949>) · [Catalog record](catalog.md#paper-gao2026dreamdojo)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Large-scale human video supplies interaction priors adapted to robot controls.

**Consumer and changed object.** Adapted world-model rollouts support robot-facing uses.

**Evidence boundary.** Human-video scale does not resolve the robot action, dynamics and contact gaps without grounding.

**Cited in:** [10](chapters/10-embodiments.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [09](chapters/09-human-egocentric.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051) · [Humanoid Locomotion &amp; Loco-Manipulation](chapters/10-embodiments.md#argument-057) · [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103).

<a id="paper-nsim-wovr"></a>

## WoVR

**WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL** (2026). [Paper](<https://arxiv.org/abs/2602.13977>) · [Catalog record](catalog.md#paper-nsim-wovr)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Action-conditioned rollouts use critical-state initialization and alignment.

**Consumer and changed object.** RL post-trains VLA policies in the predictive simulator.

**Evidence boundary.** Keep manuscript-cited v2 results and per-platform averages separate from other versions and hardware.

**Cited in:** [07](chapters/07-foundation-priors.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038).

<a id="paper-nsim-roboworld"></a>

## RoboWorld

**RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation** (2026). [Paper](<https://arxiv.org/abs/2607.01060>) · [Catalog record](catalog.md#paper-nsim-roboworld)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Neural simulation predicts outcomes for generalist robot policy evaluation.

**Consumer and changed object.** Generated outcomes rank or assess policies.

**Evidence boundary.** High model-to-real correlation is neither absolute calibration nor demonstrated policy-training gain.

**Cited in:** [07](chapters/07-foundation-priors.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038).

<a id="paper-li2025worldeval"></a>

## WorldEval

**WorldEval: World Model as Real-World Robot Policies Evaluator** (2025). [Paper](<https://arxiv.org/abs/2505.19017>) · [Catalog record](catalog.md#paper-li2025worldeval)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Policy-conditioned video prediction is combined with a separate task verifier.

**Consumer and changed object.** Evaluation compares robot policy checkpoints.

**Evidence boundary.** Evaluation evidence does not establish that the same model improves policies through training.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Evaluation, reward, and safety: what to reinforce or reject?](chapters/04-roles.md#argument-015) · [System Design Patterns](chapters/04-roles.md#argument-017) · [Offline Reinforcement Learning](chapters/06-learning-regimes.md#argument-027) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Critic, Reward, and Value Priors](chapters/07-foundation-priors.md#argument-040) · [Evaluation by Role](chapters/11-evaluation.md#argument-065) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Role-Conditioned Evidence Paths for Closed-Loop Claims](chapters/11-evaluation.md#argument-070) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [The Evaluation Crisis: Toward Reproducible Closed-Loop Benchmarks](chapters/11-evaluation.md#argument-072) · [Frontier Resource Cards › Closed-Loop Benchmarks and Evaluation Harnesses](chapters/12-resources.md#argument-079) · [Frontier Resource Cards › Safety, Monitoring, and Failure Resources](chapters/12-resources.md#argument-081) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility](chapters/15-research-agenda.md#argument-093) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100) · [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 1: Role-Specific Leaderboards](chapters/15-research-agenda.md#argument-104) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 2: Query-Distribution Evaluation](chapters/15-research-agenda.md#argument-105) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-vlarft2025"></a>

## VLA-RFT

**VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators** (2025). [Paper](<https://arxiv.org/abs/2510.00406>) · [Catalog record](catalog.md#paper-vlarft2025)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** A world simulator and verified rewards supply policy-learning feedback.

**Consumer and changed object.** GRPO updates the VLA policy while the world model is frozen.

**Evidence boundary.** Policy fine-tuning must not be described as online world-model weight adaptation.

**Cited in:** [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md).

**Argument contexts:** [Reinforcement Learning with Generative World Models](chapters/06-learning-regimes.md#argument-033) · [Critic, Reward, and Value Priors](chapters/07-foundation-priors.md#argument-040) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086).

<a id="paper-worldgymnast2026"></a>

## World-Gymnast

**World-gymnast: Training robots with reinforcement learning in a world model** (2026). [Paper](<https://arxiv.org/abs/2602.02454>) · [Catalog record](catalog.md#paper-worldgymnast2026)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Language tasks and edited scenes expand a predictive training environment.

**Consumer and changed object.** RL updates robot policies using generated task experience.

**Evidence boundary.** Generated tasks must remain executable and independently judgeable; trajectory count is not coverage.

**Cited in:** [07](chapters/07-foundation-priors.md), [09](chapters/09-human-egocentric.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [From Human Data to Synthetic Data Flywheels](chapters/09-human-egocentric.md#argument-053).

<a id="paper-nvidia2025cosmos"></a>

## Cosmos

**Cosmos world foundation model platform for physical ai** (2025). [Paper](<https://arxiv.org/abs/2501.03575>) · [Catalog record](catalog.md#paper-nvidia2025cosmos)

**Kind:** `generative-context`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Pretrained world-model components supply physical-domain generation priors.

**Consumer and changed object.** Robot-specific adaptation can consume these priors.

**Evidence boundary.** A general foundation platform is not, by itself, a demonstrated closed-loop robot system.

**Cited in:** [10](chapters/10-embodiments.md), [07](chapters/07-foundation-priors.md), [03](chapters/03-foundations.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md).

**Argument contexts:** [Introduction](chapters/01-introduction.md#argument-001) · [A Robot Learning Loop View of World Models](chapters/03-foundations.md#argument-007) · [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) · [Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md#argument-073) · [Frontier Resource Cards › Learned Simulators and World Foundation Models](chapters/12-resources.md#argument-077) · [Evaluation Axes](chapters/12-resources.md#argument-084) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Closed-Source Frontier Systems](chapters/15-research-agenda.md#argument-102) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-nvidia2026cosmos3"></a>

## Cosmos 3

**Cosmos 3: Omnimodal World Models for Physical AI** (2026). [Paper](<https://arxiv.org/abs/2606.02800>) · [Catalog record](catalog.md#paper-nvidia2026cosmos3)

**Kind:** `generative-context`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Omnimodal world modeling broadens physical-domain predictive interfaces.

**Consumer and changed object.** Downstream embodied systems can adapt the learned priors.

**Evidence boundary.** Separate broad modality coverage from action grounding and measured robot policy utility.

**Cited in:** [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Introduction](chapters/01-introduction.md#argument-001) · [Omnimodal World Foundation Models as Interface Consolidation](chapters/07-foundation-priors.md#argument-039) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103).

<a id="paper-bruce2024genie"></a>

## Genie

**Genie: Generative Interactive Environments** (2024). [Paper](<https://arxiv.org/abs/2402.15391>) · [Catalog record](catalog.md#paper-bruce2024genie)

**Kind:** `generative-context`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** A learned generative environment supports interactive visual futures.

**Consumer and changed object.** Agents can consume an interactive generated environment.

**Evidence boundary.** Latent interaction interfaces require robot-control grounding before robot deployment claims.

**Cited in:** [05](chapters/05-representations.md).

**Argument contexts:** [From Video Generation to Controllable World Models](chapters/05-representations.md#argument-025).

<a id="paper-tian2019manipulation"></a>

## Manipulation by Feel

**Manipulation by Feel: Touch-Based Control with Deep Predictive Models** (2019). [Paper](<https://arxiv.org/abs/1903.04128>) · [Catalog record](catalog.md#paper-tian2019manipulation)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Tactile observations and actions feed a deep predictive model.

**Consumer and changed object.** Model-predictive control uses touch predictions to choose actions.

**Evidence boundary.** Sensor, contact and manipulation conditions define the control evidence.

**Cited in:** [07](chapters/07-foundation-priors.md), [15](chapters/15-research-agenda.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Tactile World Models for Model-Based Control and Planning](chapters/08-tactile-contact.md#argument-045) · [The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility](chapters/15-research-agenda.md#argument-093).

<a id="paper-ai2024robopack"></a>

## RoboPack

**RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing** (2024). [Paper](<https://arxiv.org/abs/2407.01418>) · [Catalog record](catalog.md#paper-ai2024robopack)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Tactile-informed dynamics encode latent physical interaction state.

**Consumer and changed object.** Predicted contact dynamics support dense-packing decisions.

**Evidence boundary.** The learned physical representation should be judged through the downstream planning task.

**Cited in:** [07](chapters/07-foundation-priors.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Tactile World Models for Model-Based Control and Planning](chapters/08-tactile-contact.md#argument-045).

<a id="paper-wi2022virdopp"></a>

## VIRDO++

**VIRDO++: Real-World, Visuo-tactile Dynamics and Perception of Deformable Objects** (2022). [Paper](<https://arxiv.org/abs/2210.03701>) · [Catalog record](catalog.md#paper-wi2022virdopp)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Visuo-tactile implicit representations capture deformable-object state and dynamics.

**Consumer and changed object.** Predictive perception provides deformable-state estimates.

**Evidence boundary.** Representation and dynamics evidence do not automatically establish a complete robot policy improvement loop.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Tactile World Models for Model-Based Control and Planning](chapters/08-tactile-contact.md#argument-045).

<a id="paper-zhang2026contactworld"></a>

## ContactWorld

**ContactWorld: What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation** (2026). [Paper](<https://arxiv.org/abs/2606.13877>) · [Catalog record](catalog.md#paper-zhang2026contactworld)

**Kind:** `world-model-use`. **Roles:** [Representation](roles.md#role-representation), [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Vision-tactile latent world modeling studies contact-relevant predictive representations.

**Consumer and changed object.** Contact-aware representations support manipulation-facing predictions.

**Evidence boundary.** Compare contact prediction and downstream control separately; a representation study is not a general contact guarantee.

**Cited in:** [07](chapters/07-foundation-priors.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [From Tactile Representation to Policy Learning](chapters/08-tactile-contact.md#argument-046).

<a id="paper-omnivta2026"></a>

## OmniVTA

**OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation** (2026). [Paper](<https://arxiv.org/abs/2603.19201>) · [Catalog record](catalog.md#paper-omnivta2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** A visuo-tactile predictive model is paired with fast tactile feedback.

**Consumer and changed object.** A reflex interface corrects actions during contact-rich manipulation.

**Evidence boundary.** Feedback-driven action correction is distinct from online neural weight updates; OmniVTLA is a different system.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [Adaptation and Monitoring: how Should the Robot Respond to Deployment Feedback?](chapters/04-roles.md#argument-016) · [System Design Patterns](chapters/04-roles.md#argument-017) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) · [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [From Tactile Representation to Policy Learning](chapters/08-tactile-contact.md#argument-046) · [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048) · [Evaluation by Role](chapters/11-evaluation.md#argument-065) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Resource Cards › Visuo-Tactile and Contact Resources](chapters/12-resources.md#argument-080) · [Resource Gaps for 2026-Ready Robot World Models](chapters/12-resources.md#argument-082) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [Physical Interaction World Models: Contact, Force, and Deformation](chapters/15-research-agenda.md#argument-094) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 5: Multimodal Physical Grounding](chapters/15-research-agenda.md#argument-108) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-visuotactilewm2026"></a>

## Visuo-Tactile World Models

**Visuo-Tactile World Models** (2026). [Paper](<https://arxiv.org/abs/2602.06001>) · [Catalog record](catalog.md#paper-visuotactilewm2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning).

**Predictive interface.** Joint visual and tactile prediction informs future interaction estimates.

**Consumer and changed object.** A planning interface produces contact-rich robot actions.

**Evidence boundary.** The reviewed plan execution is open loop; avoid labeling it online corrective control.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [09](chapters/09-human-egocentric.md), [01](chapters/01-introduction.md), [06](chapters/06-learning-regimes.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Two grand challenges](chapters/01-introduction.md#argument-002) · [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) · [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Why Vision-Only World Models Fail at Contact](chapters/08-tactile-contact.md#argument-043) · [Tactile World Models for Model-Based Control and Planning](chapters/08-tactile-contact.md#argument-045) · [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048) · [The Embodiment Gap: Why Human Video Is Not Robot Experience](chapters/09-human-egocentric.md#argument-050) · [Cross-Embodiment Alignment: From Human Motion to Robot-Controllable Representations](chapters/09-human-egocentric.md#argument-052) · [Embodiment and Task Perspective](chapters/10-embodiments.md#argument-054) · [Manipulation](chapters/10-embodiments.md#argument-055) · [Model Quality](chapters/11-evaluation.md#argument-061) · [Evaluation by Role](chapters/11-evaluation.md#argument-065) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Frontier Resource Cards › Visuo-Tactile and Contact Resources](chapters/12-resources.md#argument-080) · [Resource Gaps for 2026-Ready Robot World Models](chapters/12-resources.md#argument-082) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [Physical Interaction World Models: Contact, Force, and Deformation](chapters/15-research-agenda.md#argument-094) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 5: Multimodal Physical Grounding](chapters/15-research-agenda.md#argument-108) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-yuan2026dextacwam"></a>

## DexTacWAM

**DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation** (2026). [Paper](<https://arxiv.org/abs/2609.24976>) · [Catalog record](catalog.md#paper-yuan2026dextacwam)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Visuo-tactile world-action modeling couples predictive touch with dexterous action learning.

**Consumer and changed object.** Predictive tactile supervision influences dexterous manipulation policies.

**Evidence boundary.** Direct tactile conditioning is a comparator, not the same mechanism; evidence remains task- and platform-bounded.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048).

<a id="paper-yuan2026vtam"></a>

## VTAM

**VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs** (2026). [Paper](<https://arxiv.org/abs/2603.23481>) · [Catalog record](catalog.md#paper-yuan2026vtam)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Video, tactile and action modeling connects visual futures to contact information.

**Consumer and changed object.** The joint predictive-action interface supports physical interaction.

**Evidence boundary.** Visual prediction, tactile prediction and policy utility need separate ablations.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048).

<a id="paper-tian2026vtwam"></a>

## VT-WAM

**VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation** (2026). [Paper](<https://arxiv.org/abs/2607.02503>) · [Catalog record](catalog.md#paper-tian2026vtwam)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Visual-tactile world-action modeling learns coupled contact futures and actions.

**Consumer and changed object.** Action generation consumes multimodal predictive information.

**Evidence boundary.** World-action modeling does not by itself demonstrate online corrective planning or sensor transfer.

**Cited in:** [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086).

<a id="paper-lou2026dreamtac"></a>

## Dream-Tac

**Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation** (2026). [Paper](<https://arxiv.org/abs/2606.08737>) · [Catalog record](catalog.md#paper-lou2026dreamtac)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** A unified tactile world-action model represents contact-rich predictive-action relationships.

**Consumer and changed object.** The learned action interface supports manipulation.

**Evidence boundary.** Keep predictive supervision distinct from direct tactile conditioning and real-time deployment evidence.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [From Tactile Representation to Policy Learning](chapters/08-tactile-contact.md#argument-046) · [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048).

<a id="paper-wu2026tactilewam"></a>

## Tactile-WAM

**Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention** (2026). [Paper](<https://arxiv.org/abs/2606.26663>) · [Catalog record](catalog.md#paper-wu2026tactilewam)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Asymmetric attention integrates tactile signals into world-action modeling.

**Consumer and changed object.** Touch-aware predictive-action features influence actions.

**Evidence boundary.** Asymmetric training access and actual deployment sensor access must be reported separately.

**Cited in:** [07](chapters/07-foundation-priors.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) · [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048).

<a id="paper-higuera2024sparsh"></a>

## Sparsh

**Sparsh: Self-supervised Touch Representations for Vision-based Tactile Sensing** (2024). [Paper](<https://arxiv.org/abs/2410.24090>) · [Catalog record](catalog.md#paper-higuera2024sparsh)

**Kind:** `representation-prior`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** Self-supervised learning provides tactile feature representations.

**Consumer and changed object.** Downstream sensing and policy systems consume the features.

**Evidence boundary.** A tactile representation prior is contextual; predictive control requires an additional action-grounded model and consumer.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Tactile Sensing and Representation Foundations](chapters/08-tactile-contact.md#argument-044).

**Upstream resource:** [Sparsh](https://github.com/facebookresearch/sparsh).

<a id="paper-feng2025anytouch"></a>

## AnyTouch

**AnyTouch: Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors** (2025). [Paper](<https://arxiv.org/abs/2502.12191>) · [Catalog record](catalog.md#paper-feng2025anytouch)

**Kind:** `representation-prior`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** Static and dynamic visuo-tactile representation learning spans multiple sensors.

**Consumer and changed object.** Downstream systems reuse tactile features.

**Evidence boundary.** Sensor representation transfer is not proof of transferred robot predictive dynamics.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Tactile Sensing and Representation Foundations](chapters/08-tactile-contact.md#argument-044).

<a id="paper-cheng2025omnivtla"></a>

## OmniVTLA

**OmniVTLA: Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing** (2025). [Paper](<https://arxiv.org/abs/2508.08706>) · [Catalog record](catalog.md#paper-cheng2025omnivtla)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** A vision-tactile-language-action policy consumes semantically aligned tactile sensing.

**Consumer and changed object.** The learned policy predicts actions.

**Evidence boundary.** Keep this policy distinct from the predictive-reflex world-model system OmniVTA.

**Cited in:** [08](chapters/08-tactile-contact.md).

**Argument contexts:** [From Tactile Representation to Policy Learning](chapters/08-tactile-contact.md#argument-046).

<a id="paper-clark2026muse"></a>

## MuSe

**Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force** (2026). [Paper](<https://arxiv.org/abs/2606.30988>) · [Catalog record](catalog.md#paper-clark2026muse)

**Kind:** `policy-context`. **Roles:** [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Force sensing is added to pretrained visuomotor policies through continual learning.

**Consumer and changed object.** Policy adaptation incorporates new sensory information.

**Evidence boundary.** Continual sensory adaptation is related context; validate retention and predictive dynamics separately.

**Cited in:** [14](chapters/14-interaction-learning.md), [08](chapters/08-tactile-contact.md).

**Argument contexts:** [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048) · [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090).

<a id="paper-bharadhwaj2025gen2act"></a>

## Gen2Act

**Gen2Act: Human Video Generation in Novel Scenarios Enables Generalizable Robot Manipulation** (2025). [Paper](<https://arxiv.org/abs/2409.16283>) · [Catalog record](catalog.md#paper-bharadhwaj2025gen2act)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Generated human videos provide novel task scenarios for robot learning.

**Consumer and changed object.** A robot-learning pipeline consumes generated behavior supervision.

**Evidence boundary.** Human motion must be grounded in robot sensing, kinematics and executable actions.

**Cited in:** [10](chapters/10-embodiments.md), [04](chapters/04-roles.md).

**Argument contexts:** [Simulation &amp; Data Generation: how can models provide experience?](chapters/04-roles.md#argument-013) · [Humanoid Locomotion &amp; Loco-Manipulation](chapters/10-embodiments.md#argument-057).

<a id="paper-liang2025dreamitate"></a>

## Dreamitate

**Dreamitate: Real-World Visuomotor Policy Learning via Video Generation** (2025). [Paper](<https://arxiv.org/abs/2406.16862>) · [Catalog record](catalog.md#paper-liang2025dreamitate)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Video generation supplies visuomotor policy-learning experience.

**Consumer and changed object.** Generated supervision updates robot policies.

**Evidence boundary.** Generated demonstrations are a learning-time route, not proof of online model-based planning.

**Cited in:** [10](chapters/10-embodiments.md), [04](chapters/04-roles.md).

**Argument contexts:** [Simulation &amp; Data Generation: how can models provide experience?](chapters/04-roles.md#argument-013) · [Humanoid Locomotion &amp; Loco-Manipulation](chapters/10-embodiments.md#argument-057).

<a id="paper-egowam2026"></a>

## EgoWAM

**EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data** (2026). [Paper](<https://arxiv.org/abs/2607.08436>) · [Catalog record](catalog.md#paper-egowam2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Egocentric human data supply a world-action modeling objective beyond pixels.

**Consumer and changed object.** A predictive-action learner transfers information to robot behavior.

**Evidence boundary.** The visual, kinematic, dynamics/contact and action-label gaps remain distinct evaluation obligations.

**Cited in:** [03](chapters/03-foundations.md), [13](chapters/13-frontier-atlas.md), [09](chapters/09-human-egocentric.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Positioning Against Existing Paradigms](chapters/03-foundations.md#argument-009) · [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility](chapters/15-research-agenda.md#argument-093).

<a id="paper-chen2026anyworld"></a>

## AnyWorld

**AnyWorld: Factorized Egocentric World Models for Cross-Embodiment Generalization** (2026). [Paper](<https://arxiv.org/abs/2608.29242>) · [Catalog record](catalog.md#paper-chen2026anyworld)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation).

**Predictive interface.** Factorized egocentric modeling recomposes observations, instructions and actions.

**Consumer and changed object.** Recomposition supplies missing training combinations for cross-embodiment use.

**Evidence boundary.** Broad recombination is not automatic physical validity or universal embodiment transfer.

**Cited in:** [09](chapters/09-human-egocentric.md).

**Argument contexts:** [From Human Data to Synthetic Data Flywheels](chapters/09-human-egocentric.md#argument-053).

<a id="paper-zhou2026zerowam"></a>

## Zero-WAM

**Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization** (2026). [Paper](<https://arxiv.org/abs/2608.26103>) · [Catalog record](catalog.md#paper-zhou2026zerowam)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction).

**Predictive interface.** Human-video context conditions world-action modeling at test time.

**Consumer and changed object.** Context changes the predictions and generated actions.

**Evidence boundary.** In-context adaptation must not be described as test-time neural weight training.

**Cited in:** [09](chapters/09-human-egocentric.md), [14](chapters/14-interaction-learning.md).

**Argument contexts:** [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051) · [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090) · [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092).

<a id="paper-feng2026wamttt"></a>

## WAM-TTT

**WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time** (2026). [Paper](<https://arxiv.org/abs/2607.06988>) · [Catalog record](catalog.md#paper-feng2026wamttt)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Human play at test time steers a world-action model through adaptation.

**Consumer and changed object.** Test-time learning changes fast model weights.

**Evidence boundary.** Distinguish weight updates from Zero-WAM context conditioning and account for adaptation cost.

**Cited in:** [14](chapters/14-interaction-learning.md).

**Argument contexts:** [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090).

<a id="paper-tactalign2026"></a>

## TactAlign

**TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment** (2026). [Paper](<https://arxiv.org/abs/2602.13579>) · [Catalog record](catalog.md#paper-tactalign2026)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Tactile alignment supports transfer from human interaction to robot policies.

**Consumer and changed object.** The transferred policy uses contact-related information.

**Evidence boundary.** Policy transfer is not evidence that a robot predictive dynamics model transferred.

**Cited in:** [09](chapters/09-human-egocentric.md).

**Argument contexts:** [Cross-Embodiment Alignment: From Human Motion to Robot-Controllable Representations](chapters/09-human-egocentric.md#argument-052).

<a id="paper-egozero2025"></a>

## EgoZero

**EgoZero: Robot Learning from Smart Glasses** (2025). [Paper](<https://arxiv.org/abs/2505.20290>) · [Catalog record](catalog.md#paper-egozero2025)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** Smart-glasses human interaction supplies robot-learning information.

**Consumer and changed object.** The robot policy is trained using grounded human-derived supervision.

**Evidence boundary.** Egocentric video is not an executable robot trajectory until action and embodiment gaps are addressed.

**Cited in:** [09](chapters/09-human-egocentric.md).

**Argument contexts:** [The Embodiment Gap: Why Human Video Is Not Robot Experience](chapters/09-human-egocentric.md#argument-050) · [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051).

<a id="paper-vlaw2026"></a>

## VLAW

**VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model** (2026). [Paper](<https://arxiv.org/abs/2602.12063>) · [Catalog record](catalog.md#paper-vlaw2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Real interaction refines a world model that supplies synthetic policy-training data.

**Consumer and changed object.** Iterative model and policy improvement changes both learners through distinct updates.

**Evidence boundary.** Weighted supervised policy updates with an RL interpretation must not be relabeled PPO or GRPO.

**Cited in:** [10](chapters/10-embodiments.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [09](chapters/09-human-egocentric.md), [14](chapters/14-interaction-learning.md), [06](chapters/06-learning-regimes.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Reinforcement Learning with Generative World Models](chapters/06-learning-regimes.md#argument-033) · [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [From Human Data to Synthetic Data Flywheels](chapters/09-human-egocentric.md#argument-053) · [Embodiment and Task Perspective](chapters/10-embodiments.md#argument-054) · [Manipulation](chapters/10-embodiments.md#argument-055) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) · [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 4: Policy-Model Co-Training](chapters/15-research-agenda.md#argument-107) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109).

<a id="paper-xue2026worldsample"></a>

## WorldSample

**WorldSample: Closed-loop Real-robot RL with World Modelling** (2026). [Paper](<https://arxiv.org/abs/2607.02431>) · [Catalog record](catalog.md#paper-xue2026worldsample)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Counterfactual world-model transitions supplement real robot RL experience.

**Consumer and changed object.** Online policy learning consumes real and selectively generated transitions.

**Evidence boundary.** Report transition provenance, uncertainty scheduling and matched real-interaction budgets.

**Cited in:** [07](chapters/07-foundation-priors.md), [14](chapters/14-interaction-learning.md), [15](chapters/15-research-agenda.md).

**Argument contexts:** [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) · [Failure Mining and Experience Curation](chapters/14-interaction-learning.md#argument-091) · [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100) · [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 4: Policy-Model Co-Training](chapters/15-research-agenda.md#argument-107) · [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109).

<a id="paper-wamrl2026"></a>

## WAM-RL

**WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT** (2026). [Paper](<https://arxiv.org/abs/2606.17906>) · [Catalog record](catalog.md#paper-wamrl2026)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Reconstruction rewards support actor learning while online video supervision updates the world model.

**Consumer and changed object.** Actor RL and world-model video SFT change different parameter sets.

**Evidence boundary.** Do not collapse the separate objectives and KL constraints into a single joint RL loss.

**Cited in:** [06](chapters/06-learning-regimes.md).

**Argument contexts:** [Reinforcement Learning with Generative World Models](chapters/06-learning-regimes.md#argument-033).

<a id="paper-liu2024runtime"></a>

## Model-Based Runtime Monitoring

**Model-Based Runtime Monitoring with Interactive Imitation Learning** (2024). [Paper](<https://arxiv.org/abs/2310.17552>) · [Catalog record](catalog.md#paper-liu2024runtime)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** A predictive model estimates problematic policy outcomes during deployment.

**Consumer and changed object.** A monitor requests human intervention; later interaction supports learning.

**Evidence boundary.** Detection, human decisions and subsequent retraining are separate events.

**Cited in:** [10](chapters/10-embodiments.md), [04](chapters/04-roles.md).

**Argument contexts:** [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Adaptation and Monitoring: how Should the Robot Respond to Deployment Feedback?](chapters/04-roles.md#argument-016) · [System Design Patterns](chapters/04-roles.md#argument-017) · [Human-Robot Interaction &amp; Correctable Autonomy](chapters/10-embodiments.md#argument-060).

<a id="paper-liu2025siriusfleet"></a>

## Sirius-Fleet

**Multi-Task Interactive Robot Fleet Learning with Visual World Models** (2025). [Paper](<https://proceedings.mlr.press/v270/liu25g.html>) · [Catalog record](catalog.md#paper-liu2025siriusfleet)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Visual prediction supports multi-task interactive robot-fleet learning.

**Consumer and changed object.** Monitoring and human assistance influence collection and policy improvement.

**Evidence boundary.** The reviewed predictor is frozen and does not query alternative candidate actions; fleet learning is not online dynamics adaptation.

**Cited in:** [10](chapters/10-embodiments.md), [14](chapters/14-interaction-learning.md).

**Argument contexts:** [Human-Robot Interaction &amp; Correctable Autonomy](chapters/10-embodiments.md#argument-060) · [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) · [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092).

<a id="paper-govind2026regen"></a>

## REGEN

**World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays** (2026). [Paper](<https://arxiv.org/abs/2606.27374>) · [Catalog record](catalog.md#paper-govind2026regen)

**Kind:** `world-model-use`. **Roles:** [Simulation and data generation](roles.md#role-simulation), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Generative replay retains prior task experience during continual imitation learning.

**Consumer and changed object.** Replayed experience supports policy retention as new tasks arrive.

**Evidence boundary.** Replay quality and task retention need empirical checks; generation alone does not guarantee lifelong learning.

**Cited in:** [14](chapters/14-interaction-learning.md).

**Argument contexts:** [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090).

<a id="paper-liu2025onlinewm"></a>

## Planning with Online World Models

**Continual Reinforcement Learning by Planning with Online World Models** (2025). [Paper](<https://arxiv.org/abs/2507.09177>) · [Catalog record](catalog.md#paper-liu2025onlinewm)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning), [Adaptation and monitoring](roles.md#role-adaptation).

**Predictive interface.** Interaction updates a world model used for planning during continual learning.

**Consumer and changed object.** Feedback can change predictive parameters and later decisions.

**Evidence boundary.** Report update cadence, query distribution and old-task retention rather than treating any update as beneficial.

**Cited in:** [14](chapters/14-interaction-learning.md).

**Argument contexts:** [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090).

<a id="paper-shang2026worldarena"></a>

## WorldArena

**WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models** (2026). [Paper](<https://arxiv.org/abs/2602.08971>) · [Catalog record](catalog.md#paper-shang2026worldarena)

**Kind:** `benchmark`. **Roles:** [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** A benchmark examines perceptual quality and embodied functional utility.

**Consumer and changed object.** Evaluation protocols compare model behavior and decision utility.

**Evidence boundary.** The benchmark is an evaluation resource, not a robot world-model method or a universal deployment certificate.

**Cited in:** [11](chapters/11-evaluation.md).

**Argument contexts:** [Evaluating Physical Fidelity: From Plausibility to Control Validity](chapters/11-evaluation.md#argument-067) · [Minimum Evaluation Coverage with Runnable Fixtures](chapters/11-evaluation.md#argument-069).

<a id="paper-yue2025ewmbench"></a>

## EWMBench

**EWMBench: Evaluating Scene, Motion, and Semantic Quality in Embodied World Models** (2025). [Paper](<https://arxiv.org/abs/2505.09694>) · [Catalog record](catalog.md#paper-yue2025ewmbench)

**Kind:** `benchmark`. **Roles:** [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** Evaluation probes scene, motion and semantic quality in embodied world models.

**Consumer and changed object.** Quality tests assess predictive outputs.

**Evidence boundary.** Perceptual and semantic quality do not substitute for downstream policy improvement.

**Cited in:** [11](chapters/11-evaluation.md).

**Argument contexts:** [The Evaluation Crisis: Toward Reproducible Closed-Loop Benchmarks](chapters/11-evaluation.md#argument-072).

<a id="paper-worldinworld2025"></a>

## World-in-World

**World-in-world: World models in a closed-loop world** (2026). [Paper](<https://arxiv.org/abs/2510.18135>) · [Catalog record](catalog.md#paper-worldinworld2025)

**Kind:** `benchmark`. **Roles:** [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** A closed-loop benchmarking interface connects model predictions to agent interaction.

**Consumer and changed object.** Online planning protocols assess generated environments.

**Evidence boundary.** Task scope and action APIs determine applicability; the benchmark name does not establish robot hardware evidence.

**Cited in:** [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [03](chapters/03-foundations.md), [13](chapters/13-frontier-atlas.md), [14](chapters/14-interaction-learning.md), [01](chapters/01-introduction.md), [15](chapters/15-research-agenda.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md).

**Argument contexts:** [Introduction](chapters/01-introduction.md#argument-001) · [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Critic, Reward, and Value Priors](chapters/07-foundation-priors.md#argument-040) · [Model Quality](chapters/11-evaluation.md#argument-061) · [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) · [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) · [Minimum Evaluation Coverage with Runnable Fixtures](chapters/11-evaluation.md#argument-069) · [The Evaluation Crisis: Toward Reproducible Closed-Loop Benchmarks](chapters/11-evaluation.md#argument-072) · [Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md#argument-073) · [Frontier Resource Cards › Closed-Loop Benchmarks and Evaluation Harnesses](chapters/12-resources.md#argument-079) · [What Resources Should Enable: Four Capability Dimensions](chapters/12-resources.md#argument-083) · [Evaluation Axes](chapters/12-resources.md#argument-084) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Failure Mining and Experience Curation](chapters/14-interaction-learning.md#argument-091) · [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092) · [Robotics Scaling Laws](chapters/15-research-agenda.md#argument-099) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-huang2024safedreamer"></a>

## SafeDreamer

**Safedreamer: Safe reinforcement learning with world models** (2024). [Paper](<https://arxiv.org/abs/2307.07176>) · [Catalog record](catalog.md#paper-huang2024safedreamer)

**Kind:** `world-model-use`. **Roles:** [Prediction and imagination](roles.md#role-prediction), [Planning and search](roles.md#role-planning), [Evaluation, reward and safety](roles.md#role-evaluation).

**Predictive interface.** A learned world model supplies predicted trajectories for Lagrangian-based constrained planning.

**Consumer and changed object.** World-model planning consumes task and safety information to choose actions.

**Evidence boundary.** The inspected upstream account reports Safety-Gymnasium experiments; constraint satisfaction is conditional on the tested environment, model and reporting protocol.

**Cited in:** [07](chapters/07-foundation-priors.md), [15](chapters/15-research-agenda.md), [04](chapters/04-roles.md).

**Argument contexts:** [Evaluation, reward, and safety: what to reinforce or reject?](chapters/04-roles.md#argument-015) · [Safety and Constraint Priors](chapters/07-foundation-priors.md#argument-042) · [Safety and Trust Calibration](chapters/15-research-agenda.md#argument-101).

**Upstream resource:** [SafeDreamer](https://github.com/PKU-Alignment/SafeDreamer).

<a id="paper-openvla2024"></a>

## OpenVLA

**Openvla: An open-source vision-language-action model** (2024). [Paper](<https://arxiv.org/abs/2406.09246>) · [Catalog record](catalog.md#paper-openvla2024)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** A foundation vision-language-action policy maps observations and instructions to actions.

**Consumer and changed object.** It supplies a policy baseline or consumer for world-model training and evaluation.

**Evidence boundary.** A VLA policy is not a world model solely because it predicts actions.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) · [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [Imitation Learning and Behavior Cloning](chapters/06-learning-regimes.md#argument-026) · [Sim-to-Real and Cross-Embodiment Transfer](chapters/06-learning-regimes.md#argument-030) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Representation Priors: State Abstractions for Control](chapters/07-foundation-priors.md#argument-035) · [Open VLA Action Priors](chapters/07-foundation-priors.md#argument-036) · [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md#argument-073) · [Frontier Resource Cards › Foundation Policy Resources: Open VLAs as Baselines and Priors](chapters/12-resources.md#argument-075) · [Evaluation Axes](chapters/12-resources.md#argument-084) · [Frontier Evidence Atlas: 2024–2026](chapters/13-frontier-atlas.md#argument-085) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

**Upstream resource:** [OpenVLA](https://github.com/openvla/openvla).

<a id="paper-pi0"></a>

## pi0

**π_0: A Vision-Language-Action Flow Model for General Robot Control** (2024). [Paper](<https://arxiv.org/abs/2410.24164>) · [Catalog record](catalog.md#paper-pi0)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** A flow-based vision-language-action foundation policy generates robot controls.

**Consumer and changed object.** It supplies an action policy or downstream world-model consumer.

**Evidence boundary.** Action generation alone does not satisfy action-intervenable consequence prediction.

**Cited in:** [10](chapters/10-embodiments.md), [11](chapters/11-evaluation.md), [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md), [06](chapters/06-learning-regimes.md), [12](chapters/12-resources.md), [A](chapters/a-review-protocol.md), [04](chapters/04-roles.md).

**Argument contexts:** [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) · [Imitation Learning and Behavior Cloning](chapters/06-learning-regimes.md#argument-026) · [Sim-to-Real and Cross-Embodiment Transfer](chapters/06-learning-regimes.md#argument-030) · [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) · [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) · [Representation Priors: State Abstractions for Control](chapters/07-foundation-priors.md#argument-035) · [Open VLA Action Priors](chapters/07-foundation-priors.md#argument-036) · [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) · [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) · [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) · [Resources: Datasets, Simulators, Benchmarks, and Frameworks](chapters/12-resources.md#argument-073) · [Frontier Resource Cards › Foundation Policy Resources: Open VLAs as Baselines and Priors](chapters/12-resources.md#argument-075) · [Evaluation Axes](chapters/12-resources.md#argument-084) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) · [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) · [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113).

<a id="paper-nvidia2026groot17"></a>

## GR00T N1.7

**NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots** (2026). [Paper](<https://huggingface.co/blog/nvidia/gr00t-n1-7>) · [Catalog record](catalog.md#paper-nvidia2026groot17)

**Kind:** `policy-context`. **Roles:** [Representation](roles.md#role-representation).

**Predictive interface.** A reasoning VLA foundation model provides humanoid-facing action proposals.

**Consumer and changed object.** Downstream embodied systems consume its policy interface.

**Evidence boundary.** Reasoning and generalist policy capabilities do not automatically establish a predictive robot world model.

**Cited in:** [07](chapters/07-foundation-priors.md), [13](chapters/13-frontier-atlas.md).

**Argument contexts:** [Open VLA Action Priors](chapters/07-foundation-priors.md#argument-036) · [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086).
