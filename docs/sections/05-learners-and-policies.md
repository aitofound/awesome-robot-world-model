# 5 · Who Changes the Robot: Learners and Policies

[Home](../../README.md) · [← 4 · How Predictions Are Consumed: Five Pathways](04-pathways.md) · [6 · Embodiments: What the World Demands →](06-embodiments.md)

The consumer of a prediction sets two of the three factors in ΔJ: the queries it issues and the sensitivity of its output to errors in the answers. The same world model can therefore help one consumer and mislead another. The section covers the learners that turn model outputs into parameter updates (imitation learning, offline and online reinforcement learning) and the policies and planners that turn them into actions.

This section cites 20 works. A work cited in several subsections appears under each; ⌂ marks the subsection where the README lists it.

<a id="sec-5-1"></a>

## 5.1 Policy-Learning Regimes

*Representative works (Figure 2):* [MimicGen](../catalog.md#paper-mimicgen), [MOPO](../catalog.md#paper-mopo), [MOReL](../catalog.md#paper-morel), [COMBO](../catalog.md#paper-combo), [Dreamer](../catalog.md#paper-hafner2019dreamer)

- **RT-1**: [Robotics Transformer for Real-World Control at Scale](<https://arxiv.org/abs/2212.06817>) · 2022 · [ⓘ](../catalog.md#paper-rt1) ⌂
- **RT-2**: [Vision-language-action models transfer web knowledge to robotic control](<https://arxiv.org/abs/2307.15818>) · arXiv 2023 · [ⓘ](../catalog.md#paper-rt2)
- **OpenVLA**: [An open-source vision-language-action model](<https://arxiv.org/abs/2406.09246>) · arXiv 2024 · [Code](<https://github.com/openvla/openvla>) · [ⓘ](../catalog.md#paper-openvla2024)
- **π0**: [A Vision-Language-Action Flow Model for General Robot Control](<https://arxiv.org/abs/2410.24164>) · arXiv 2024 · [ⓘ](../catalog.md#paper-pi0)
- **GR00T**: [Gr00t n1: An open foundation model for generalist humanoid robots](<https://arxiv.org/abs/2503.14734>) · arXiv 2025 · [ⓘ](../catalog.md#paper-nvidia2025groot)
- **Open X-Embodiment**: [Robotic Learning Datasets and RT-X Models](<https://arxiv.org/abs/2310.08864>) · ICRA 2024 · [Code](<https://github.com/google-deepmind/open_x_embodiment>) · [ⓘ](../catalog.md#paper-openxembodiment2023)
- [Uncertainty-driven Trajectory Truncation for Data Augmentation in Offline Reinforcement Learning](<https://arxiv.org/abs/2304.04660>) · 2023 · [ⓘ](../catalog.md#paper-tatu) ⌂
- **MOPO**: [Model-based Offline Policy Optimization](<https://proceedings.neurips.cc/paper_files/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf>) · NeurIPS 2020 · [ⓘ](../catalog.md#paper-mopo) ⌂
- **MOReL**: [Model-Based Offline Reinforcement Learning](<https://proceedings.neurips.cc/paper_files/paper/2020/file/f7efa4f864ae9b88d43527f4b14f750f-Paper.pdf>) · NeurIPS 2020 · [ⓘ](../catalog.md#paper-morel) ⌂
- **COMBO**: [Conservative Offline Model-Based Policy Optimization](<https://proceedings.neurips.cc/paper_files/paper/2021/file/f29a179746902e331572c483c45e5086-Paper.pdf>) · NeurIPS 2021 · [ⓘ](../catalog.md#paper-combo) ⌂

<a id="sec-5-2"></a>

## 5.2 Policies and Planners

*Representative works (Figure 2):* [OpenVLA](../catalog.md#paper-openvla2024), [π0](../catalog.md#paper-pi0), [GR00T](../catalog.md#paper-nvidia2025groot), MPC and tree search

- **OpenVLA**: [An open-source vision-language-action model](<https://arxiv.org/abs/2406.09246>) · arXiv 2024 · [Code](<https://github.com/openvla/openvla>) · [ⓘ](../catalog.md#paper-openvla2024) ⌂
- **π0**: [A Vision-Language-Action Flow Model for General Robot Control](<https://arxiv.org/abs/2410.24164>) · arXiv 2024 · [ⓘ](../catalog.md#paper-pi0) ⌂
- **GR00T**: [Gr00t n1: An open foundation model for generalist humanoid robots](<https://arxiv.org/abs/2503.14734>) · arXiv 2025 · [ⓘ](../catalog.md#paper-nvidia2025groot) ⌂
- **VLA Review**: [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](<https://arxiv.org/abs/2510.07077>) · 2025 · [ⓘ](../catalog.md#paper-vlareview2025) ⌂
- **RT-2**: [Vision-language-action models transfer web knowledge to robotic control](<https://arxiv.org/abs/2307.15818>) · arXiv 2023 · [ⓘ](../catalog.md#paper-rt2)
- [Towards Safe Robot Foundation Models](<https://arxiv.org/abs/2503.07404>) · 2025 · [ⓘ](../catalog.md#paper-saferobotfoundation2025)
- [π0.5: a Vision-Language-Action Model with Open-World Generalization](<https://arxiv.org/abs/2504.16054>) · arXiv 2025 · [ⓘ](../catalog.md#paper-pi2025pi05) ⌂
- [π\*0.6: a VLA That Learns From Experience](<https://arxiv.org/abs/2511.14759>) · arXiv 2025 · [ⓘ](../catalog.md#paper-pi2025pistar06) ⌂
- [π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](<https://arxiv.org/abs/2604.15483>) · arXiv 2026 · [ⓘ](../catalog.md#paper-pi2026pi07) ⌂
- **GR00T N1.7**: [NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots](<https://huggingface.co/blog/nvidia/gr00t-n1-7>) · 2026 · [ⓘ](../catalog.md#paper-nvidia2026groot17) ⌂
- **DreamZero**: [World Action Models are Zero-shot Policies](<https://arxiv.org/abs/2602.15922>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ye2026dreamzero)
- **PlaNet**: [Learning Latent Dynamics for Planning from Pixels](<https://arxiv.org/abs/1811.04551>) · ICML 2019 · [ⓘ](../catalog.md#paper-hafner2019planet)
- **TD-MPC2**: [Scalable, Robust World Models for Continuous Control](<https://arxiv.org/abs/2310.16828>) · ICLR 2024 · [ⓘ](../catalog.md#paper-hansen2024tdmpc2) ⌂
- **WorldEcho**: [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](<https://arxiv.org/abs/2608.24885>) · 2026 · [ⓘ](../catalog.md#paper-chen2026worldsync)

