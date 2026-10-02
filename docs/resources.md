# Datasets, benchmarks and implementations

[Home](../README.md) · [Paper section 12](chapters/12-resources.md)

These are upstream artifact entry points linked to works cited by the survey. The README endpoints were retrieved and their identity sections inspected. Packages, datasets, weights and robot experiments were not installed or run. A repository link is not a reproduction result.

Model, Decision, Learning and Deployment are separate interface capabilities. Establish each from the artifact and chosen protocol rather than assigning a single maturity score.

## robosuite

**Type:** `benchmark`. [Repository](https://github.com/ARISE-Initiative/robosuite) · [Cited paper](catalog.md#paper-robosuite).

Manipulation environments and controller interfaces; useful for isolating model and planning effects.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/ARISE-Initiative/robosuite/master/README.md), 2026-10-01. No runtime validation.

## ManiSkill

**Type:** `benchmark`. [Repository](https://github.com/haosulab/ManiSkill) · [Cited paper](catalog.md#paper-maniskill3).

Parallel robotics simulation and rendering; report tasks, controllers and randomization.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/haosulab/ManiSkill/main/README.md), 2026-10-01. No runtime validation.

## RoboTwin

**Type:** `benchmark`. [Repository](https://github.com/RoboTwin-Platform/RoboTwin) · [Cited paper](catalog.md#paper-chen2025robotwin2).

Bimanual tasks and data generation; separate task variation from execution robustness.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/README.md), 2026-10-01. No runtime validation.

## CALVIN

**Type:** `benchmark`. [Repository](https://github.com/mees/calvin) · [Cited paper](catalog.md#paper-mees2022calvin).

Language-conditioned long-horizon manipulation; report chain length and reset assumptions.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/mees/calvin/main/README.md), 2026-10-01. No runtime validation.

## RLBench

**Type:** `benchmark`. [Repository](https://github.com/stepjam/RLBench) · [Cited paper](catalog.md#paper-james2020rlbench).

Robot manipulation task suite; preserve observation, action and success-test settings.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/stepjam/RLBench/master/README.md), 2026-10-01. No runtime validation.

## Habitat

**Type:** `benchmark`. [Repository](https://github.com/facebookresearch/habitat-lab) · [Cited paper](catalog.md#paper-habitat).

Embodied navigation and interaction; useful for persistent spatial belief and partial observability.

**Maintenance:** Upstream README states that Meta internal teams no longer actively develop or maintain habitat-lab beyond v0.3.4; inspected 2026-10-01.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/facebookresearch/habitat-lab/main/README.md), 2026-10-01. No runtime validation.

## AI2-THOR

**Type:** `benchmark`. [Repository](https://github.com/allenai/ai2thor) · [Cited paper](catalog.md#paper-ai2thor).

Interactive indoor environments; a simulator resource rather than a learned world model.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/allenai/ai2thor/main/README.md), 2026-10-01. No runtime validation.

## HumanoidBench

**Type:** `benchmark`. [Repository](https://github.com/carlosferrazza/humanoid-bench) · [Cited paper](catalog.md#paper-sferrazza2024humanoidbench).

Whole-body locomotion and manipulation; useful for balance and embodiment constraints.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/carlosferrazza/humanoid-bench/main/README.md), 2026-10-01. No runtime validation.

## RoboCasa

**Type:** `benchmark`. [Repository](https://github.com/robocasa/robocasa) · [Cited paper](catalog.md#paper-nasiriany2026robocasa365).

Kitchen manipulation scenes and task variation; pin the release matching the cited benchmark.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/robocasa/robocasa/main/README.md), 2026-10-01. No runtime validation.

## Open X-Embodiment

**Type:** `dataset`. [Repository](https://github.com/google-deepmind/open_x_embodiment) · [Cited paper](catalog.md#paper-openxembodiment2023).

Cross-robot demonstration data; action schemas and embodiment metadata require alignment.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/google-deepmind/open_x_embodiment/main/README.md), 2026-10-01. No runtime validation.

## BridgeData V2

**Type:** `dataset`. [Repository](https://github.com/rail-berkeley/bridge_data_v2) · [Cited paper](catalog.md#paper-bridgedatav2).

Robot manipulation trajectories; static data do not provide interactive deployment tests.

[Dataset project](https://rail-berkeley.github.io/bridgedata/). The linked GitHub repository contains training implementations; the dataset is linked from its project page.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/rail-berkeley/bridge_data_v2/main/README.md), 2026-10-01. No runtime validation.

## MimicGen

**Type:** `data-generation`. [Repository](https://github.com/NVlabs/mimicgen) · [Cited paper](catalog.md#paper-mimicgen).

Demonstration-based data generation; distinguish environment-generated data from learned neural simulation.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/NVlabs/mimicgen/main/README.md), 2026-10-01. No runtime validation.

## DexMimicGen

**Type:** `data-generation`. [Repository](https://github.com/NVlabs/dexmimicgen) · [Cited paper](catalog.md#paper-dexmimicgen).

Bimanual dexterous demonstration generation; document task-specific validity checks.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/NVlabs/dexmimicgen/main/README.md), 2026-10-01. No runtime validation.

## DreamGen / GR00T Dreams

**Type:** `method-code`. [Repository](https://github.com/NVIDIA/GR00T-dreams) · [Cited paper](catalog.md#paper-jang2025dreamgen).

Video-generated behavior and pseudo-action recovery support policy training; data generation is distinct from online RL.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/NVIDIA/GR00T-dreams/main/README.md), 2026-10-01. No runtime validation.

## DreamerV3

**Type:** `method-code`. [Repository](https://github.com/danijar/dreamerv3) · [Cited paper](catalog.md#paper-hafner2023dreamerv3).

Latent imagination for actor learning; policy deployment need not run an explicit planner.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/danijar/dreamerv3/main/README.md), 2026-10-01. No runtime validation.

## DayDreamer

**Type:** `method-code`. [Repository](https://github.com/danijar/daydreamer) · [Cited paper](catalog.md#paper-wu2022daydreamer).

Physical robot world-model learning; hardware and task setup remain part of reproduction.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/danijar/daydreamer/main/README.md), 2026-10-01. No runtime validation.

## DINO-WM

**Type:** `method-code`. [Repository](https://github.com/gaoyuezhou/dino_wm) · [Cited paper](catalog.md#paper-zhou2025dinowm).

Predictive dynamics on pretrained visual features for planning; distinguish feature pretraining from action-grounded dynamics.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/gaoyuezhou/dino_wm/main/README.md), 2026-10-01. No runtime validation.

## V-JEPA 2

**Type:** `method-code`. [Repository](https://github.com/facebookresearch/vjepa2) · [Cited paper](catalog.md#paper-assran2025vjepa2).

Video predictive features and action-conditioned adaptation; inspect the planning interface used by a particular experiment.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md), 2026-10-01. No runtime validation.

## SafeDreamer

**Type:** `method-code`. [Repository](https://github.com/PKU-Alignment/SafeDreamer) · [Cited paper](catalog.md#paper-huang2024safedreamer).

World-model-based safety-constrained learning; constraint satisfaction is protocol-specific.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/PKU-Alignment/SafeDreamer/main/README.md), 2026-10-01. No runtime validation.

## OpenVLA

**Type:** `policy-context`. [Repository](https://github.com/openvla/openvla) · [Cited paper](catalog.md#paper-openvla2024).

Foundation policy code used as context or a downstream consumer; VLA status alone does not qualify it as a world model.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/openvla/openvla/main/README.md), 2026-10-01. No runtime validation.

## Sparsh

**Type:** `representation`. [Repository](https://github.com/facebookresearch/sparsh) · [Cited paper](catalog.md#paper-higuera2024sparsh).

Tactile representation learning; useful as a sensor prior, with predictive control evaluated separately.

**Link provenance:** [retrieved upstream README](https://raw.githubusercontent.com/facebookresearch/sparsh/main/README.md), 2026-10-01. No runtime validation.
