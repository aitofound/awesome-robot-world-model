# Follow the survey’s argument

[Home](../README.md) · [Find a paper by topic](paper-index.md)

Start with the gap between prediction and decision utility, then identify the modeled state, predictive interface, downstream use and returned feedback. This map follows the paper’s chapters and citation-bearing subsections. It complements the more flexible reading routes in the main index.

**113 argument groups · 1102 citation commands · 600 deduplicated works**

## 01. Introduction

The Prediction-to-Control Gap motivates a loop-centered survey. Predictive plausibility matters only through the decision or learning use it enables.

- [Section opening](chapters/01-introduction.md#argument-001) — 7 works
- [Two grand challenges](chapters/01-introduction.md#argument-002) — 6 works
- [The value-equivalence root](chapters/01-introduction.md#argument-003) — 5 works

## 02. Positioning Among Existing Surveys

The survey relates architecture, application and world-model literature to a role-first account of robot learning.

- [Section opening](chapters/02-related-surveys.md#argument-004) — 11 works
- [Relation to Prior World-Model and World-Action-Model Surveys](chapters/02-related-surveys.md#argument-005) — 8 works
- [Survey Scope and Exclusions](chapters/02-related-surveys.md#argument-006) — 16 works

## 03. A Robot Learning Loop View of World Models

Read models through observation, action, predicted consequence, downstream consumer and returned execution feedback. Separate learning-time and execution-time loops.

- [Section opening](chapters/03-foundations.md#argument-007) — 7 works
- [Open-Loop Prediction vs. Closed-Loop Utility](chapters/03-foundations.md#argument-008) — 6 works
- [Positioning Against Existing Paradigms](chapters/03-foundations.md#argument-009) — 6 works

## 04. The Optimizable Roles of World Models

The six roles organize uses before architectures. A single system can serve several roles, and the same model can change roles when its consumer changes.

- [A Common Template for Role Analysis](chapters/04-roles.md#argument-010) — 11 works
- [Representation: what state should the policy act on?](chapters/04-roles.md#argument-011) — 8 works
- [Prediction and imagination: what futures can be queried?](chapters/04-roles.md#argument-012) — 4 works
- [Simulation &amp; Data Generation: how can models provide experience?](chapters/04-roles.md#argument-013) — 26 works
- [Planning and search: which action to execute now?](chapters/04-roles.md#argument-014) — 4 works
- [Evaluation, reward, and safety: what to reinforce or reject?](chapters/04-roles.md#argument-015) — 7 works
- [Adaptation and Monitoring: how Should the Robot Respond to Deployment Feedback?](chapters/04-roles.md#argument-016) — 6 works
- [System Design Patterns](chapters/04-roles.md#argument-017) — 7 works

## 05. Representation Substrates and World-Model Mechanics

Compare pixel/video, predictive latent, 3D/object-centric, structured physics and causal representations. RSSM, autoregression, diffusion, flow and ODE formulations are cross-cutting mechanics.

- [Section opening](chapters/05-representations.md#argument-018) — 2 works
- [The Representation Question: What Should a World Model Encode](chapters/05-representations.md#argument-019) — 14 works
- [Latent Representations: Learning Compact Predictive States](chapters/05-representations.md#argument-020) — 9 works
- [Geometric Representations: Making 3D Structure Explicit](chapters/05-representations.md#argument-021) — 11 works
- [Physical Representations: Encoding Dynamics and Constraints](chapters/05-representations.md#argument-022) — 12 works
- [Causal Representations](chapters/05-representations.md#argument-023) — 6 works
- [Dynamics Mechanisms: How World States Evolve](chapters/05-representations.md#argument-024) — 22 works
- [From Video Generation to Controllable World Models](chapters/05-representations.md#argument-025) — 7 works

## 06. From Roles to Policy Improvement

Imitation, offline RL, online model-based RL, planning and transfer consume model information differently. Track real and imagined experience separately.

- [Imitation Learning and Behavior Cloning](chapters/06-learning-regimes.md#argument-026) — 11 works
- [Offline Reinforcement Learning](chapters/06-learning-regimes.md#argument-027) — 6 works
- [Online Reinforcement Learning](chapters/06-learning-regimes.md#argument-028) — 7 works
- [Planning-Time Control](chapters/06-learning-regimes.md#argument-029) — 11 works
- [Sim-to-Real and Cross-Embodiment Transfer](chapters/06-learning-regimes.md#argument-030) — 7 works
- [Robotic Policy Adaptation as a Regime](chapters/06-learning-regimes.md#argument-031) — 8 works
- [Deployment, Safety, and Human-in-the-Loop Correction](chapters/06-learning-regimes.md#argument-032) — 23 works
- [Reinforcement Learning with Generative World Models](chapters/06-learning-regimes.md#argument-033) — 4 works

## 07. Foundation-Driven World Models and Robot Priors

Foundation encoders, VLA proposals, imagination, neural simulation, rewards and constraint layers have distinct interfaces. Neural simulation can supply demonstrations, filtered BC data, policy optimization or evaluation.

- [Why Foundation Priors Change World Modeling](chapters/07-foundation-priors.md#argument-034) — 21 works
- [Representation Priors: State Abstractions for Control](chapters/07-foundation-priors.md#argument-035) — 7 works
- [Open VLA Action Priors](chapters/07-foundation-priors.md#argument-036) — 12 works
- [Imagination and Generative Priors](chapters/07-foundation-priors.md#argument-037) — 8 works
- [Neural Simulators as Training Environments](chapters/07-foundation-priors.md#argument-038) — 23 works
- [Omnimodal World Foundation Models as Interface Consolidation](chapters/07-foundation-priors.md#argument-039) — 10 works
- [Critic, Reward, and Value Priors](chapters/07-foundation-priors.md#argument-040) — 9 works
- [Physical, Contact, and Tactile Priors](chapters/07-foundation-priors.md#argument-041) — 21 works
- [Safety and Constraint Priors](chapters/07-foundation-priors.md#argument-042) — 26 works

## 08. Tactile and Contact World Models

Contact introduces hidden state, rate constraints and sensor-dependent representations. Separate predictive tactile control, world-action modeling, reactive policies and reusable sensing priors.

- [Why Vision-Only World Models Fail at Contact](chapters/08-tactile-contact.md#argument-043) — 16 works
- [Tactile Sensing and Representation Foundations](chapters/08-tactile-contact.md#argument-044) — 10 works
- [Tactile World Models for Model-Based Control and Planning](chapters/08-tactile-contact.md#argument-045) — 7 works
- [From Tactile Representation to Policy Learning](chapters/08-tactile-contact.md#argument-046) — 11 works
- [Predictive Contact and Fast Tactile Correction](chapters/08-tactile-contact.md#argument-047) — 5 works
- [Scaling Tactile World Models through Vision-to-Touch Transfer](chapters/08-tactile-contact.md#argument-048) — 15 works

## 09. Human and Egocentric Data as a World-Model Source

Human video can support representation priors, motion/action proxies, predictive world-action objectives or deployment context. Each route faces different grounding requirements.

- [Human Video as a Scalable World-Model Source](chapters/09-human-egocentric.md#argument-049) — 5 works
- [The Embodiment Gap: Why Human Video Is Not Robot Experience](chapters/09-human-egocentric.md#argument-050) — 10 works
- [From Human Video to Robot Learning Signals](chapters/09-human-egocentric.md#argument-051) — 10 works
- [Cross-Embodiment Alignment: From Human Motion to Robot-Controllable Representations](chapters/09-human-egocentric.md#argument-052) — 10 works
- [From Human Data to Synthetic Data Flywheels](chapters/09-human-egocentric.md#argument-053) — 10 works

## 10. Embodiment and Task Perspective

Manipulation stresses contact, navigation persistent belief, humanoids balance and morphology, driving traffic and rare events, and cross-robot control action semantics.

- [Section opening](chapters/10-embodiments.md#argument-054) — 26 works
- [Manipulation](chapters/10-embodiments.md#argument-055) — 6 works
- [Navigation &amp; Mobile Robots](chapters/10-embodiments.md#argument-056) — 9 works
- [Humanoid Locomotion &amp; Loco-Manipulation](chapters/10-embodiments.md#argument-057) — 17 works
- [Autonomous Driving World Models](chapters/10-embodiments.md#argument-058) — 13 works
- [Generalist &amp; Cross-Embodiment](chapters/10-embodiments.md#argument-059) — 12 works
- [Human-Robot Interaction &amp; Correctable Autonomy](chapters/10-embodiments.md#argument-060) — 24 works

## 11. Evaluation: From Prediction Metrics to Closed-Loop Utility

Report model behavior, policy effect, deployment behavior and evidence boundary. Model quality, policy utility and reliability are separate axes.

- [Model Quality](chapters/11-evaluation.md#argument-061) — 8 works
- [Policy Utility](chapters/11-evaluation.md#argument-062) — 23 works
- [Deployment Reliability](chapters/11-evaluation.md#argument-063) — 36 works
- [A Four-Layer Reporting Protocol](chapters/11-evaluation.md#argument-064) — 10 works
- [Evaluation by Role](chapters/11-evaluation.md#argument-065) — 4 works
- [Evaluation by Learning Regime](chapters/11-evaluation.md#argument-066) — 16 works
- [Evaluating Physical Fidelity: From Plausibility to Control Validity](chapters/11-evaluation.md#argument-067) — 10 works
- [Evidence Standards for Frontier Systems](chapters/11-evaluation.md#argument-068) — 2 works
- [Minimum Evaluation Coverage with Runnable Fixtures](chapters/11-evaluation.md#argument-069) — 15 works
- [Role-Conditioned Evidence Paths for Closed-Loop Claims](chapters/11-evaluation.md#argument-070) — 4 works
- [Role Ablations under the Query Distribution](chapters/11-evaluation.md#argument-071) — 21 works
- [The Evaluation Crisis: Toward Reproducible Closed-Loop Benchmarks](chapters/11-evaluation.md#argument-072) — 12 works

## 12. Resources: Datasets, Simulators, Benchmarks, and Frameworks

Distinguish datasets, interactive engines, benchmark suites, harnesses and checkpoints. Check which interface an artifact actually provides.

- [Section opening](chapters/12-resources.md#argument-073) — 21 works
- [Frontier Resource Cards › Large Robot Datasets: From Behavior Logs to World-Model Training Data](chapters/12-resources.md#argument-074) — 5 works
- [Frontier Resource Cards › Foundation Policy Resources: Open VLAs as Baselines and Priors](chapters/12-resources.md#argument-075) — 3 works
- [Frontier Resource Cards › Physics Simulators and GPU-Parallel Benchmarks](chapters/12-resources.md#argument-076) — 6 works
- [Frontier Resource Cards › Learned Simulators and World Foundation Models](chapters/12-resources.md#argument-077) — 6 works
- [Frontier Resource Cards › Synthetic Demonstration Engines](chapters/12-resources.md#argument-078) — 2 works
- [Frontier Resource Cards › Closed-Loop Benchmarks and Evaluation Harnesses](chapters/12-resources.md#argument-079) — 5 works
- [Frontier Resource Cards › Visuo-Tactile and Contact Resources](chapters/12-resources.md#argument-080) — 2 works
- [Frontier Resource Cards › Safety, Monitoring, and Failure Resources](chapters/12-resources.md#argument-081) — 3 works
- [Resource Gaps for 2026-Ready Robot World Models](chapters/12-resources.md#argument-082) — 23 works
- [What Resources Should Enable: Four Capability Dimensions](chapters/12-resources.md#argument-083) — 6 works
- [Evaluation Axes](chapters/12-resources.md#argument-084) — 14 works

## 13. Frontier Evidence Atlas: 2024–2026

The frontier atlas locates emerging systems by mechanism, role and bounded evidence. It complements the historical bibliography without creating a pooled leaderboard.

- [Section opening](chapters/13-frontier-atlas.md#argument-085) — 31 works
- [Role Clusters in the Frontier Atlas](chapters/13-frontier-atlas.md#argument-086) — 60 works
- [Near-Term Research Questions from the Atlas](chapters/13-frontier-atlas.md#argument-087) — 12 works

## 14. From Interaction to Model Improvement

Organize the outer loop as acquisition, update target, retention, failure curation and fleet sharing. Record whether feedback changes context, policy, physical parameters, neural dynamics or memory.

- [Formulation and Architecture of the Outer Loop](chapters/14-interaction-learning.md#argument-088) — 23 works
- [Autonomous Exploration and Active Interaction](chapters/14-interaction-learning.md#argument-089) — 17 works
- [Continual Learning and Online Model Updating](chapters/14-interaction-learning.md#argument-090) — 36 works
- [Failure Mining and Experience Curation](chapters/14-interaction-learning.md#argument-091) — 18 works
- [Fleet Learning and Scaled Deployment](chapters/14-interaction-learning.md#argument-092) — 18 works

## 15. Open Challenges and Future Directions

The agenda connects action grounding, multimodal contact, query-distribution shift, latency, memory, calibration and auditability to specific evaluation obligations.

- [The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility](chapters/15-research-agenda.md#argument-093) — 13 works
- [Physical Interaction World Models: Contact, Force, and Deformation](chapters/15-research-agenda.md#argument-094) — 4 works
- [Inference Efficiency and the Latency Wall](chapters/15-research-agenda.md#argument-095) — 11 works
- [Streaming, Full-Duplex, and Self-Evolving World Models](chapters/15-research-agenda.md#argument-096) — 19 works
- [Memory and Long-Horizon World Models](chapters/15-research-agenda.md#argument-097) — 9 works
- [Causal and Counterfactual World Models](chapters/15-research-agenda.md#argument-098) — 5 works
- [Robotics Scaling Laws](chapters/15-research-agenda.md#argument-099) — 5 works
- [Synthetic Data Flywheels](chapters/15-research-agenda.md#argument-100) — 13 works
- [Safety and Trust Calibration](chapters/15-research-agenda.md#argument-101) — 41 works
- [Closed-Source Frontier Systems](chapters/15-research-agenda.md#argument-102) — 11 works
- [Toward World-Model-Centric Robot Learning Systems](chapters/15-research-agenda.md#argument-103) — 9 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 1: Role-Specific Leaderboards](chapters/15-research-agenda.md#argument-104) — 1 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 2: Query-Distribution Evaluation](chapters/15-research-agenda.md#argument-105) — 2 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 3: Failure Libraries as Shared Infrastructure](chapters/15-research-agenda.md#argument-106) — 1 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 4: Policy-Model Co-Training](chapters/15-research-agenda.md#argument-107) — 2 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 5: Multimodal Physical Grounding](chapters/15-research-agenda.md#argument-108) — 2 works
- [A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems](chapters/15-research-agenda.md#argument-109) — 8 works
- [A Closing Thesis](chapters/15-research-agenda.md#argument-110) — 1 works

## 16. Conclusion

The survey returns to a single criterion: whether a predictive interface contributes to better robot decisions and learning under its tested conditions.

This section closes the argument and has no active citations.

## A. Extended Survey Protocols

The appendix supplies role worksheets, reporting fields, reading paths and terminology for consistent curation.

- [Paper Selection Protocol](chapters/a-review-protocol.md#argument-111) — 7 works
- [Evidence-Level Labels](chapters/a-review-protocol.md#argument-112) — 3 works
- [Extended Frontier Comparison Matrix](chapters/a-review-protocol.md#argument-113) — 25 works
