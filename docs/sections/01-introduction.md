# 1 · Introduction

[Home](../../README.md) · [2 · From Prediction to Control →](02-prediction-to-control.md)

World models now supply robot systems with representations, training experience, action choices and assessments of behavior. The introduction states the position of the survey, that the quality of a world model is relative to the component that consumes its predictions, compares it with earlier world-model and world-action-model surveys, and fixes the scope.

This section cites 24 works. A work cited in several subsections appears under each; ⌂ marks the subsection where the README lists it.

## Section opening

- **DayDreamer**: [World Models for Physical Robot Learning](<https://arxiv.org/abs/2206.14176>) · CoRL 2022 · [Code](<https://github.com/danijar/daydreamer>) · [ⓘ](../catalog.md#paper-wu2022daydreamer)
- **Cosmos 3**: [Omnimodal World Models for Physical AI](<https://arxiv.org/abs/2606.02800>) · arXiv 2026 · [ⓘ](../catalog.md#paper-nvidia2026cosmos3)
- The Value Equivalence Principle for Model-Based Reinforcement Learning · NeurIPS 2020 · [ⓘ](../catalog.md#paper-grimm2020value)
- Value-Aware Loss Function for Model-based Reinforcement Learning · AISTATS 2017 · [ⓘ](../catalog.md#paper-farahmand2017vaml)
- **MuZero**: [Mastering Atari, Go, chess and shogi by planning with a learned model](<https://doi.org/10.1038/s41586-020-03051-4>) · Nature 2020 · [ⓘ](../catalog.md#paper-schrittwieser2020muzero)
- **RoboPack**: [Learning Tactile-Informed Dynamics Models for Dense Packing](<https://arxiv.org/abs/2407.01418>) · RSS 2024 · [ⓘ](../catalog.md#paper-ai2024robopack)
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- **WorldPlanner**: [Monte carlo tree search and mpc with action-conditioned visual world models](<https://arxiv.org/abs/2511.03077>) · arXiv 2025 · [ⓘ](../catalog.md#paper-worldplanner2025)
- **Flex-π**: [A Multi-Stream World-Action Model with Compute Flexibility](<https://arxiv.org/abs/2608.10860>) · 2026 · [ⓘ](../catalog.md#paper-yan2026flexpi)
- [Survey of Model-Based Reinforcement Learning: Applications on Robotics](<https://doi.org/10.1007/s10846-017-0468-y>) · Journal of Intelligent &amp; Robotic Systems 2017 · [ⓘ](../catalog.md#paper-polydoros2017mbrlrobotics) ⌂
- [Model-based Reinforcement Learning: A Survey](<https://arxiv.org/abs/2006.16712>) · Foundations and Trends in Machine Learning 2023 · [ⓘ](../catalog.md#paper-moerland2023modelbasedrl) ⌂
- [Robotic world models – conceptualization, review, and engineering best practices](<https://doi.org/10.3389/frobt.2023.1253049>) · Frontiers in Robotics and AI 2023 · [ⓘ](../catalog.md#paper-sakagami2023roboticworldmodels) ⌂
- [Foundation models in robotics: Applications, challenges, and the future](<https://doi.org/10.1177/02783649241281508>) · The International Journal of Robotics Research 2025 · [ⓘ](../catalog.md#paper-firoozi2025foundation)
- [Towards General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis](<https://robotics-fm-survey.github.io/>) · 2024 · [ⓘ](../catalog.md#paper-hu2024generalpurpose) ⌂
- **VLA Review**: [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](<https://arxiv.org/abs/2510.07077>) · 2025 · [ⓘ](../catalog.md#paper-vlareview2025)
- [Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI](<https://arxiv.org/abs/2407.06886>) · 2024 · [ⓘ](../catalog.md#paper-liu2024embodiedai) ⌂
- [Understanding World or Predicting Future? A Comprehensive Survey of World Models](<https://arxiv.org/abs/2411.14499>) · ACM Computing Surveys 2025 · [ⓘ](../catalog.md#paper-ding2024understandingworld) ⌂
- [A Definition and Roadmap for World Models](<https://arxiv.org/abs/2607.06401>) · 2026 · [ⓘ](../catalog.md#paper-shanghailab2026definitionroadmap) ⌂
- [World Model for Robot Learning: A Comprehensive Survey](<https://arxiv.org/abs/2605.00080>) · 2026 · [ⓘ](../catalog.md#paper-hou2026worldmodelrobotlearning) ⌂
- [A Step Toward World Models: A Survey on Robotic Manipulation](<https://arxiv.org/abs/2511.02097>) · 2025 · [ⓘ](../catalog.md#paper-zhang2025manipulationworldmodels) ⌂
- [A Review of Learning-Based Dynamics Models for Robotic Manipulation](<https://doi.org/10.1126/scirobotics.adt1497>) · Science Robotics 2025 · [ⓘ](../catalog.md#paper-ai2025learningdynamicsmanipulation) ⌂
- [A Comprehensive Survey on World Models for Embodied AI](<https://arxiv.org/abs/2510.16732>) · 2025 · [ⓘ](../catalog.md#paper-li2025embodiedworldmodels) ⌂
- [World Action Models: The Next Frontier in Embodied AI](<https://arxiv.org/abs/2605.12090>) · 2026 · [ⓘ](../catalog.md#paper-wang2026wamnextfrontier) ⌂
- [World Action Models: A Survey](<https://arxiv.org/abs/2606.20781>) · arXiv 2026 · [ⓘ](../catalog.md#paper-shen2026wamsurvey) ⌂

