# 08. Tactile and Contact World Models

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

Contact introduces hidden state, rate constraints and sensor-dependent representations. Separate predictive tactile control, world-action modeling, reactive policies and reusable sensing priors.

## Reading questions

- Does tactile prediction change an action or learning target?
- Is the contact loop executed online?
- Which sensing transfer and retention tests are reported?

## Interpretation boundary

Predictive touch and direct tactile conditioning are different mechanisms. Keep OmniVTA and OmniVTLA distinct.

## Selected annotations

- [Dreamer](../methods.md#paper-hafner2019dreamer)
- [DayDreamer](../methods.md#paper-wu2022daydreamer)
- [Large Video Planner](../methods.md#paper-chen2025largevideoplanner)
- [Manipulation by Feel](../methods.md#paper-tian2019manipulation)
- [RoboPack](../methods.md#paper-ai2024robopack)
- [VIRDO++](../methods.md#paper-wi2022virdopp)
- [ContactWorld](../methods.md#paper-zhang2026contactworld)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [DexTacWAM](../methods.md#paper-yuan2026dextacwam)
- [VTAM](../methods.md#paper-yuan2026vtam)
- [VT-WAM](../methods.md#paper-tian2026vtwam)
- [Dream-Tac](../methods.md#paper-lou2026dreamtac)
- [Tactile-WAM](../methods.md#paper-wu2026tactilewam)
- [Sparsh](../methods.md#paper-higuera2024sparsh)
- [AnyTouch](../methods.md#paper-feng2025anytouch)
- [OmniVTLA](../methods.md#paper-cheng2025omnivtla)
- [MuSe](../methods.md#paper-clark2026muse)

## References by argument (55 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-043"></a>

### Why Vision-Only World Models Fail at Contact

| Year | Work | Primary entry |
|---|---|---|
| 1996 | [An implicit time-stepping method for rigid body dynamics with inelastic collisions and Coulomb friction](../catalog.md#paper-stewart1996implicit) | [Paper](<https://doi.org/10.1002/(SICI)1097-0207(19960815)39:15<2673::AID-NME972>3.0.CO;2-I>) |
| 2020 | [Dream to Control: Learning Behaviors by Latent Imagination](../catalog.md#paper-hafner2019dreamer) | [Paper](<https://arxiv.org/abs/1912.01603>) |
| 2022 | [DayDreamer: World Models for Physical Robot Learning](../catalog.md#paper-wu2022daydreamer) | [Paper](<https://arxiv.org/abs/2206.14176>) |
| 2024 | [Diffusion for World Modeling: Visual Details Matter in Atari](../catalog.md#paper-alonso2024diamond) | [Paper](<https://arxiv.org/abs/2405.12399>) |
| 2025 | [Large video planner enables generalizable robot control](../catalog.md#paper-chen2025largevideoplanner) | [Paper](<https://arxiv.org/abs/2512.15840>) |
| 2026 | [Do Generative Video Models Understand Physical Principles?](../catalog.md#paper-motamed2026physicsiq) | [Paper](<https://arxiv.org/abs/2501.09038>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination](../catalog.md#paper-li2026efficientwam) | [Paper](<https://arxiv.org/abs/2606.10040>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 1982 | [Quasi-Static Assembly of Compliantly Supported Rigid Parts](../catalog.md#paper-whitney1982quasi) | [Paper](<https://doi.org/10.1115/1.3139682>) |
| 2023 | [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../catalog.md#paper-chi2023diffusionpolicy) | Source metadata only |
| 2023 | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../catalog.md#paper-zhao2023act) | Source metadata only |
| 1985 | [Impedance Control: An Approach to Manipulation: Part I—Theory](../catalog.md#paper-hogan1985impedance) | [Paper](<https://doi.org/10.1115/1.3140702>) |
| 2017 | [GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force](../catalog.md#paper-yuan2017gelsight) | Source metadata only |
| 2020 | [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../catalog.md#paper-lambeta2020digit) | [Paper](<https://arxiv.org/abs/2005.14679>) |
| 2024 | [AnySkin: Plug-and-play Skin Sensing for Robotic Touch](../catalog.md#paper-bhirangi2024anyskin) | [Paper](<https://arxiv.org/abs/2409.08276>) |

<a id="argument-044"></a>

### Tactile Sensing and Representation Foundations

| Year | Work | Primary entry |
|---|---|---|
| 2017 | [GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force](../catalog.md#paper-yuan2017gelsight) | Source metadata only |
| 2020 | [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../catalog.md#paper-lambeta2020digit) | [Paper](<https://arxiv.org/abs/2005.14679>) |
| 2024 | [Digitizing Touch with an Artificial Multimodal Fingertip](../catalog.md#paper-lambeta2024digit360) | [Paper](<https://arxiv.org/abs/2411.02479>) |
| 2008 | [Biomimetic Tactile Sensor Array](../catalog.md#paper-wettels2008biotac) | Source metadata only |
| 2021 | [ReSkin: Versatile, Replaceable, Lasting Tactile Skins](../catalog.md#paper-bhirangi2021reskin) | [Paper](<https://arxiv.org/abs/2111.00071>) |
| 2024 | [AnySkin: Plug-and-play Skin Sensing for Robotic Touch](../catalog.md#paper-bhirangi2024anyskin) | [Paper](<https://arxiv.org/abs/2409.08276>) |
| 2026 | [FlexiTac: A Low-Cost, Open-Source, Scalable Tactile Sensing Solution for Robotic Systems](../catalog.md#paper-huang2026flexitac) | [Paper](<https://arxiv.org/abs/2604.28156>) |
| 2024 | [Sparsh: Self-supervised Touch Representations for Vision-based Tactile Sensing](../catalog.md#paper-higuera2024sparsh) | [Paper](<https://arxiv.org/abs/2410.24090>) |
| 2025 | [AnyTouch: Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors](../catalog.md#paper-feng2025anytouch) | [Paper](<https://arxiv.org/abs/2502.12191>) |
| 2024 | [Octopi: Object Property Reasoning with Large Tactile-Language Models](../catalog.md#paper-yu2024octopi) | [Paper](<https://arxiv.org/abs/2405.02794>) |

<a id="argument-045"></a>

### Tactile World Models for Model-Based Control and Planning

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Learning Physical Interaction: A Survey of Tactile- and Force-aware Robot Learning](../catalog.md#paper-shan2026learningphysicalinteractionsurvey) | [Paper](<https://arxiv.org/abs/2608.07558>) |
| 2019 | [Manipulation by Feel: Touch-Based Control with Deep Predictive Models](../catalog.md#paper-tian2019manipulation) | [Paper](<https://arxiv.org/abs/1903.04128>) |
| 2024 | [LeTac-MPC: Learning Model Predictive Control for Tactile-reactive Grasping](../catalog.md#paper-xu2024letacmpc) | [Paper](<https://arxiv.org/abs/2403.04934>) |
| 2024 | [RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing](../catalog.md#paper-ai2024robopack) | [Paper](<https://arxiv.org/abs/2407.01418>) |
| 2022 | [VIRDO: Visio-tactile Implicit Representations of Deformable Objects](../catalog.md#paper-wi2022virdo) | [Paper](<https://arxiv.org/abs/2202.00868>) |
| 2022 | [VIRDO++: Real-World, Visuo-tactile Dynamics and Perception of Deformable Objects](../catalog.md#paper-wi2022virdopp) | [Paper](<https://arxiv.org/abs/2210.03701>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |

<a id="argument-046"></a>

### From Tactile Representation to Policy Learning

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [OmniVTLA: Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing](../catalog.md#paper-cheng2025omnivtla) | [Paper](<https://arxiv.org/abs/2508.08706>) |
| 2025 | [Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization](../catalog.md#paper-huang2025tactilevla) | [Paper](<https://arxiv.org/abs/2507.09160>) |
| 2025 | [ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation](../catalog.md#paper-heng2025vitacformer) | [Paper](<https://arxiv.org/abs/2506.15953>) |
| 2026 | [Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](../catalog.md#paper-lou2026dreamtac) | [Paper](<https://arxiv.org/abs/2606.08737>) |
| 2025 | [Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper](../catalog.md#paper-zhu2025touchwild) | Source metadata only |
| 2024 | [3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](../catalog.md#paper-huang2024vitac) | Source metadata only |
| 2025 | [VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning](../catalog.md#paper-huang2025vtrefine) | Source metadata only |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation](../catalog.md#paper-huang2026vitacworld) | [Paper](<https://arxiv.org/abs/2607.22530>) |
| 2026 | [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](../catalog.md#paper-zhou2026touchworld) | [Paper](<https://arxiv.org/abs/2607.07287>) |
| 2026 | [ContactWorld: What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation](../catalog.md#paper-zhang2026contactworld) | [Paper](<https://arxiv.org/abs/2606.13877>) |

<a id="argument-047"></a>

### Predictive Contact and Fast Tactile Correction

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation](../catalog.md#paper-zang2026tacforesight) | [Paper](<https://arxiv.org/abs/2606.11184>) |
| 2026 | [Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding](../catalog.md#paper-xu2026cgp) | [Paper](<https://arxiv.org/abs/2603.05687>) |
| 2024 | [Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control](../catalog.md#paper-hou2024adaptive) | [Paper](<https://arxiv.org/abs/2410.09309>) |
| 2025 | [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../catalog.md#paper-xue2025reactive) | [Paper](<https://arxiv.org/abs/2503.02881>) |
| 2025 | [TacDiffusion: Force-domain Diffusion Policy for Precise Tactile Manipulation](../catalog.md#paper-wu2025tacdiffusion) | [Paper](<https://arxiv.org/abs/2409.11047>) |

<a id="argument-048"></a>

### Scaling Tactile World Models through Vision-to-Touch Transfer

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](../catalog.md#paper-egoexo4d2023) | [Paper](<https://arxiv.org/abs/2311.18259>) |
| 2026 | [Egodex: Learning dexterous manipulation from large-scale egocentric video](../catalog.md#paper-hoque2026egodex) | Source metadata only |
| 2026 | [EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](../catalog.md#paper-egoverse2026) | [Paper](<https://arxiv.org/abs/2604.07607>) |
| 2019 | [Learning the Signatures of the Human Grasp Using a Scalable Tactile Glove](../catalog.md#paper-sundaram2019stag) | Source metadata only |
| 2021 | [Learning Human–Environment Interactions Using Conformal Tactile Textiles](../catalog.md#paper-luo2021tactiletextiles) | Source metadata only |
| 2026 | [VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs](../catalog.md#paper-yuan2026vtam) | [Paper](<https://arxiv.org/abs/2603.23481>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2026 | [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](../catalog.md#paper-tian2026vtwam) | [Paper](<https://arxiv.org/abs/2607.02503>) |
| 2026 | [Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](../catalog.md#paper-lou2026dreamtac) | [Paper](<https://arxiv.org/abs/2606.08737>) |
| 2026 | [Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention](../catalog.md#paper-wu2026tactilewam) | [Paper](<https://arxiv.org/abs/2606.26663>) |
| 2026 | [Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force](../catalog.md#paper-clark2026muse) | [Paper](<https://arxiv.org/abs/2606.30988>) |
| 2026 | [DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](../catalog.md#paper-yuan2026dextacwam) | [Paper](<https://arxiv.org/abs/2609.24976>) |
| 2017 | [GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force](../catalog.md#paper-yuan2017gelsight) | Source metadata only |
| 2020 | [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](../catalog.md#paper-lambeta2020digit) | [Paper](<https://arxiv.org/abs/2005.14679>) |

