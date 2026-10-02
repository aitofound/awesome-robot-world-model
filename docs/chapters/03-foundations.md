# 03. A Robot Learning Loop View of World Models

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Read models through observation, action, predicted consequence, downstream consumer and returned execution feedback. Separate learning-time and execution-time loops.

## Reading questions

- Can the predictor be queried under alternative actions?
- Is the coupling to a learner or controller implemented?
- Where does execution feedback enter?

## Interpretation boundary

Context refresh, action correction, policy learning and world-model weight updates are different forms of feedback.

## Selected annotations

- [World Models](../methods.md#paper-ha2018worldmodels)
- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DreamerV3](../methods.md#paper-hafner2023dreamerv3)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [Robotic World Model (RWM)](../methods.md#paper-li2025roboticworldmodel)
- [Cosmos](../methods.md#paper-nvidia2025cosmos)
- [EgoWAM](../methods.md#paper-egowam2026)
- [World-in-World](../methods.md#paper-worldinworld2025)

## References by argument (17 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-007"></a>

### Section opening

| Year | Work | Primary entry |
|---|---|---|
| 2018 | [World Models](../catalog.md#paper-ha2018worldmodels) | [Paper](<https://arxiv.org/abs/1803.10122>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2023 | [Robotic world models – conceptualization, review, and engineering best practices](../catalog.md#paper-sakagami2023roboticworldmodels) | [Paper](<https://doi.org/10.3389/frobt.2023.1253049>) |
| 2025 | [Foundation models in robotics: Applications, challenges, and the future](../catalog.md#paper-firoozi2025foundation) | [Paper](<https://doi.org/10.1177/02783649241281508>) |
| 2024 | [Towards General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis](../catalog.md#paper-hu2024generalpurpose) | [Paper](<https://robotics-fm-survey.github.io/>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |

<a id="argument-008"></a>

### Open-Loop Prediction vs. Closed-Loop Utility

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [Mastering Diverse Domains through World Models](../catalog.md#paper-hafner2023dreamerv3) | [Paper](<https://arxiv.org/abs/2301.04104>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2025 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../catalog.md#paper-li2025roboticworldmodel) | [Paper](<https://arxiv.org/abs/2501.10100>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |

<a id="argument-009"></a>

### Positioning Against Existing Paradigms

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2026 | [WALL-WM: Carving World Action Modeling at the Event Joints](../catalog.md#paper-xsquare2026wallwm) | [Paper](<https://arxiv.org/abs/2606.01955>) |
| 2025 | [Unified Video Action Model](../catalog.md#paper-li2025uva) | [Paper](<https://arxiv.org/abs/2503.00200>) |
| 2026 | [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](../catalog.md#paper-egowam2026) | [Paper](<https://arxiv.org/abs/2607.08436>) |
| 2026 | [World Action Models: A Survey](../catalog.md#paper-shen2026wamsurvey) | [Paper](<https://arxiv.org/abs/2606.20781>) |
| 2026 | [World Action Models: The Next Frontier in Embodied AI](../catalog.md#paper-wang2026wamnextfrontier) | [Paper](<https://arxiv.org/abs/2605.12090>) |

