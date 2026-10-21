# 3 · What the Model Is: Four Design Dials

[Home](../../README.md) · [← 2 · From Prediction to Control](02-prediction-to-control.md) · [4 · How Predictions Are Consumed: Five Pathways →](04-pathways.md)

A world model is a learned conditional predictor, and four design dials determine it: what it predicts (Y), what it is conditioned on (C), where its knowledge comes from (D) and how it computes a prediction (M). Each dial spans a trade-off between two useful ends, and current technical routes are settings of all four dials at once. Section 3.2 extends the prediction space to contact and touch.

[![Current technical routes as settings of the four design dials, with the pathways each route serves.](../../assets/figures/dials.svg)](../../assets/figures/dials.svg)

This section cites 177 works. A work cited in several subsections appears under each; ⌂ marks the subsection where the README lists it.

<a id="sec-3-1"></a>

## 3.1 Y: What Is Predicted

*Representative works (Figure 2):* [DINO-WM](../catalog.md#paper-zhou2025dinowm), [V-JEPA 2-AC](../catalog.md#paper-assran2025vjepa2), [PointWorld](../catalog.md#paper-pointworld2026), [PhysTwin](../catalog.md#paper-jiang2025phystwin)

- [Mastering Atari, Go, chess and shogi by planning with a learned model](<https://doi.org/10.1038/s41586-020-03051-4>) · Nature 2020 · [ⓘ](../catalog.md#paper-schrittwieser2020muzero)
- **TD-MPC2**: [Scalable, Robust World Models for Continuous Control](<https://arxiv.org/abs/2310.16828>) · ICLR 2024 · [ⓘ](../catalog.md#paper-hansen2024tdmpc2)
- **DINO-WM**: [World Models on Pre-trained Visual Features Enable Zero-Shot Planning](<https://arxiv.org/abs/2411.04983>) · ICML 2025 · [Code](<https://github.com/gaoyuezhou/dino_wm>) · [ⓘ](../catalog.md#paper-zhou2025dinowm) ⌂
- **V-JEPA 2-AC**: [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](<https://arxiv.org/abs/2506.09985>) · arXiv 2025 · [Code](<https://github.com/facebookresearch/vjepa2>) · [ⓘ](../catalog.md#paper-assran2025vjepa2) ⌂
- [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](<https://arxiv.org/abs/2603.19312>) · arXiv 2026 · [ⓘ](../catalog.md#paper-maes2026leworldmodel) ⌂
- [Temporal Straightening for Latent Planning](<https://arxiv.org/abs/2603.12231>) · ICML 2026 · [ⓘ](../catalog.md#paper-wang2026temporalstraightening) ⌂
- [What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?](<https://arxiv.org/abs/2512.24497>) · TMLR 2026 · [ⓘ](../catalog.md#paper-terver2026jepawm) ⌂
- [ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](<https://arxiv.org/abs/2403.08321>) · ECCV 2024 · [ⓘ](../catalog.md#paper-lu2024manigaussian) ⌂
- [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](<https://arxiv.org/abs/2605.20752>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zhang2026gaussiandream) ⌂
- **PointWorld**: [Scaling 3d world models for in-the-wild robotic manipulation](<https://arxiv.org/abs/2601.03782>) · arXiv 2026 · [ⓘ](../catalog.md#paper-pointworld2026)
- [ParticleFormer: A 3D Point Cloud World Model for Multi-Object, Multi-Material Robotic Manipulation](<https://arxiv.org/abs/2506.23126>) · arXiv 2025 · [ⓘ](../catalog.md#paper-huang2025particleformer) ⌂
- [SyncTwin: Fast Digital Twin Construction and Synchronization for Safe Robotic Manipulation](<https://arxiv.org/abs/2601.09920>) · arXiv 2026 · [ⓘ](../catalog.md#paper-huang2026synctwin) ⌂
- [Object-Centric World Model for Language-Guided Manipulation](<https://arxiv.org/abs/2503.06170>) · arXiv 2025 · [ⓘ](../catalog.md#paper-jeong2025objectcentric) ⌂
- FOCUS: Object-Centric World Models for Robotic Manipulation · Frontiers in Neurorobotics 2025 · [ⓘ](../catalog.md#paper-ferraro2025focus) ⌂
- [Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation](<https://arxiv.org/abs/2506.23919>) · ICRA 2026 · [ⓘ](../catalog.md#paper-chen2026goalvla) ⌂
- [Learning Particle Dynamics for Manipulating Rigid Bodies, Deformable Objects, and Fluids](<https://arxiv.org/abs/1810.01566>) · ICLR 2019 · [ⓘ](../catalog.md#paper-li2019particle) ⌂
- [Keypoints into the Future: Self-Supervised Correspondence in Model-Based Reinforcement Learning](<https://arxiv.org/abs/2009.05085>) · CoRL 2020 · [ⓘ](../catalog.md#paper-manuelli2020keypoints) ⌂
- [Learning Compositional Koopman Operators for Model-Based Control](<https://arxiv.org/abs/1910.08264>) · ICLR 2020 · [ⓘ](../catalog.md#paper-li2020koopman) ⌂
- [On the Utility of Koopman Operator Theory in Learning Dexterous Manipulation Skills](<https://arxiv.org/abs/2303.13446>) · CoRL 2023 · [ⓘ](../catalog.md#paper-han2023koopman) ⌂
- **PhysTwin**: [Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](<https://arxiv.org/abs/2503.17973>) · ICCV 2025 · [ⓘ](../catalog.md#paper-jiang2025phystwin) ⌂
- [AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation](<https://arxiv.org/abs/2407.07889>) · arXiv 2024 · [ⓘ](../catalog.md#paper-zhang2024adaptigraph) ⌂
- [PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics](<https://arxiv.org/abs/2607.20653>) · arXiv 2026 · [ⓘ](../catalog.md#paper-yin2026physcore) ⌂
- [Reconciling Reality through Simulation: A Real-To-Sim-to-Real Approach for Robust Manipulation](<https://doi.org/10.15607/RSS.2024.XX.015>) · RSS 2024 · [ⓘ](../catalog.md#paper-torne2024rialto) ⌂
- [RoboGSim: A Real2Sim2Real Robotic Gaussian Splatting Simulator](<https://arxiv.org/abs/2411.11839>) · arXiv 2024 · [ⓘ](../catalog.md#paper-li2024robogsim) ⌂
- [CITRIS: Causal Identifiability from Temporal Intervened Sequences](<https://proceedings.mlr.press/v162/lippe22a.html>) · ICML 2022 · [ⓘ](../catalog.md#paper-lippe2022citris) ⌂
- [Causal Dynamics Learning for Task-Independent State Abstraction](<https://arxiv.org/abs/2206.13452>) · ICML 2022 · [ⓘ](../catalog.md#paper-wang2022cdl) ⌂
- **Causal-JEPA**: [Learning World Models through Object-Level Latent Masking](<https://arxiv.org/abs/2602.11389>) · arXiv 2026 · [ⓘ](../catalog.md#paper-nam2026causaljepa) ⌂
- [CoPhy: Counterfactual Learning of Physical Dynamics](<https://arxiv.org/abs/1909.12000>) · ICLR 2020 · [ⓘ](../catalog.md#paper-baradel2020cophy) ⌂
- [Particle-grid neural dynamics for learning deformable object models from rgb-d videos](<https://arxiv.org/abs/2506.15680>) · arXiv 2025 · [ⓘ](../catalog.md#paper-zhang2025particle) ⌂
- ContactSDF: Signed distance functions as multi-contact models for dexterous manipulation · RA-L 2025 · [ⓘ](../catalog.md#paper-yang2025contactsdf) ⌂
- TwinTrack: Bridging vision and contact physics for real-time tracking of unknown dynamic objects · arXiv 2025 · [ⓘ](../catalog.md#paper-yang2025twintrack) ⌂
- DiffTactile: A physics-based differentiable tactile simulator for contact-rich robotic manipulation · ICLR 2024 · [ⓘ](../catalog.md#paper-si2024difftactile) ⌂

<a id="sec-3-2"></a>

## 3.2 Beyond Vision: Contact and Touch

*Representative works (Figure 2):* [RoboPack](../catalog.md#paper-ai2024robopack), [VT-WM](../catalog.md#paper-visuotactilewm2026), [OmniVTA](../catalog.md#paper-omnivta2026), [VTAM](../catalog.md#paper-yuan2026vtam), [DexTacWAM](../catalog.md#paper-yuan2026dextacwam)

### 3.2.1 Why Vision-Only World Models Fail at Contact

- Responsible and Generalizable Dexterous Manipulation through Multimodal Perception, Reasoning, and Sim2Real Learning · Staats-und Universitätsbibliothek Hamburg Carl von Ossietzky 2026 · [ⓘ](../catalog.md#paper-zhang2026responsible) ⌂
- ContactDexNet: Multi-fingered robotic hand grasping in cluttered environments through hand-object contact semantic mapping · IROS 2025 · [ⓘ](../catalog.md#paper-zhang2025contactdexnet) ⌂
- [An implicit time-stepping method for rigid body dynamics with inelastic collisions and Coulomb friction](<https://doi.org/10.1002/(SICI)1097-0207(19960815)39:15%3C2673::AID-NME972%3E3.0.CO;2-I>) · International Journal for Numerical Methods in Engineering 1996 · [ⓘ](../catalog.md#paper-stewart1996implicit) ⌂
- **Dreamer**: [Dream to Control: Learning Behaviors by Latent Imagination](<https://arxiv.org/abs/1912.01603>) · ICLR 2020 · [ⓘ](../catalog.md#paper-hafner2019dreamer)
- **DayDreamer**: [World Models for Physical Robot Learning](<https://arxiv.org/abs/2206.14176>) · CoRL 2022 · [Code](<https://github.com/danijar/daydreamer>) · [ⓘ](../catalog.md#paper-wu2022daydreamer)
- [Diffusion for World Modeling: Visual Details Matter in Atari](<https://arxiv.org/abs/2405.12399>) · NeurIPS 2024 · [ⓘ](../catalog.md#paper-alonso2024diamond) ⌂
- **LVP**: [Large video planner enables generalizable robot control](<https://arxiv.org/abs/2512.15840>) · arXiv 2025 · [ⓘ](../catalog.md#paper-chen2025largevideoplanner)
- **Physics-IQ**: [Do Generative Video Models Understand Physical Principles?](<https://arxiv.org/abs/2501.09038>) · WACV 2026 · [ⓘ](../catalog.md#paper-motamed2026physicsiq)
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026) ⌂
- [Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination](<https://arxiv.org/abs/2606.10040>) · arXiv 2026 · [ⓘ](../catalog.md#paper-li2026efficientwam) ⌂
- **DreamZero**: [World Action Models are Zero-shot Policies](<https://arxiv.org/abs/2602.15922>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ye2026dreamzero)
- [Quasi-Static Assembly of Compliantly Supported Rigid Parts](<https://doi.org/10.1115/1.3139682>) · Journal of Dynamic Systems, Measurement, and Control 1982 · [ⓘ](../catalog.md#paper-whitney1982quasi) ⌂
- Diffusion Policy: Visuomotor Policy Learning via Action Diffusion · RSS 2023 · [ⓘ](../catalog.md#paper-chi2023diffusionpolicy) ⌂
- Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware · RSS 2023 · [ⓘ](../catalog.md#paper-zhao2023act) ⌂
- [Impedance Control: An Approach to Manipulation: Part I—Theory](<https://doi.org/10.1115/1.3140702>) · Journal of Dynamic Systems, Measurement, and Control 1985 · [ⓘ](../catalog.md#paper-hogan1985impedance) ⌂
- GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force · Sensors 2017 · [ⓘ](../catalog.md#paper-yuan2017gelsight) ⌂
- [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](<https://arxiv.org/abs/2005.14679>) · RA-L 2020 · [ⓘ](../catalog.md#paper-lambeta2020digit) ⌂
- [AnySkin: Plug-and-play Skin Sensing for Robotic Touch](<https://arxiv.org/abs/2409.08276>) · arXiv 2024 · [ⓘ](../catalog.md#paper-bhirangi2024anyskin) ⌂

### 3.2.2 Tactile Sensing and Representation Foundations

- GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force · Sensors 2017 · [ⓘ](../catalog.md#paper-yuan2017gelsight) ⌂
- [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](<https://arxiv.org/abs/2005.14679>) · RA-L 2020 · [ⓘ](../catalog.md#paper-lambeta2020digit) ⌂
- [Digitizing Touch with an Artificial Multimodal Fingertip](<https://arxiv.org/abs/2411.02479>) · arXiv 2024 · [ⓘ](../catalog.md#paper-lambeta2024digit360) ⌂
- Biomimetic Tactile Sensor Array · Advanced Robotics 2008 · [ⓘ](../catalog.md#paper-wettels2008biotac) ⌂
- [ReSkin: Versatile, Replaceable, Lasting Tactile Skins](<https://arxiv.org/abs/2111.00071>) · CoRL 2021 · [ⓘ](../catalog.md#paper-bhirangi2021reskin) ⌂
- [AnySkin: Plug-and-play Skin Sensing for Robotic Touch](<https://arxiv.org/abs/2409.08276>) · arXiv 2024 · [ⓘ](../catalog.md#paper-bhirangi2024anyskin) ⌂
- [FlexiTac: A Low-Cost, Open-Source, Scalable Tactile Sensing Solution for Robotic Systems](<https://arxiv.org/abs/2604.28156>) · arXiv 2026 · [ⓘ](../catalog.md#paper-huang2026flexitac) ⌂
- **Sparsh**: [Self-supervised Touch Representations for Vision-based Tactile Sensing](<https://arxiv.org/abs/2410.24090>) · CoRL 2024 · [Code](<https://github.com/facebookresearch/sparsh>) · [ⓘ](../catalog.md#paper-higuera2024sparsh) ⌂
- **AnyTouch**: [Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors](<https://arxiv.org/abs/2502.12191>) · ICLR 2025 · [ⓘ](../catalog.md#paper-feng2025anytouch) ⌂
- [Octopi: Object Property Reasoning with Large Tactile-Language Models](<https://arxiv.org/abs/2405.02794>) · RSS 2024 · [ⓘ](../catalog.md#paper-yu2024octopi) ⌂

### 3.2.3 Tactile World Models for Model-Based Control and Planning

- [Learning Physical Interaction: A Survey of Tactile- and Force-aware Robot Learning](<https://arxiv.org/abs/2608.07558>) · 2026 · [ⓘ](../catalog.md#paper-shan2026learningphysicalinteractionsurvey) ⌂
- **Manipulation by Feel**: [Touch-Based Control with Deep Predictive Models](<https://arxiv.org/abs/1903.04128>) · ICRA 2019 · [ⓘ](../catalog.md#paper-tian2019manipulation) ⌂
- [LeTac-MPC: Learning Model Predictive Control for Tactile-reactive Grasping](<https://arxiv.org/abs/2403.04934>) · IEEE Transactions on Robotics 2024 · [ⓘ](../catalog.md#paper-xu2024letacmpc) ⌂
- **RoboPack**: [Learning Tactile-Informed Dynamics Models for Dense Packing](<https://arxiv.org/abs/2407.01418>) · RSS 2024 · [ⓘ](../catalog.md#paper-ai2024robopack) ⌂
- [VIRDO: Visio-tactile Implicit Representations of Deformable Objects](<https://arxiv.org/abs/2202.00868>) · ICRA 2022 · [ⓘ](../catalog.md#paper-wi2022virdo) ⌂
- **VIRDO++**: [Real-World, Visuo-tactile Dynamics and Perception of Deformable Objects](<https://arxiv.org/abs/2210.03701>) · CoRL 2022 · [ⓘ](../catalog.md#paper-wi2022virdopp) ⌂
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026) ⌂
- [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](<https://arxiv.org/abs/2607.24267>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ma2026feelworld) ⌂

### 3.2.4 From Tactile Representation to Policy Learning

- **OmniVTLA**: [Vision-Tactile-Language-Action Models with Semantic-Aligned Tactile Sensing](<https://arxiv.org/abs/2508.08706>) · arXiv 2025 · [ⓘ](../catalog.md#paper-cheng2025omnivtla) ⌂
- [Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization](<https://arxiv.org/abs/2507.09160>) · arXiv 2025 · [ⓘ](../catalog.md#paper-huang2025tactilevla) ⌂
- [ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation](<https://arxiv.org/abs/2506.15953>) · 2025 · [ⓘ](../catalog.md#paper-heng2025vitacformer) ⌂
- **Dream-Tac**: [A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](<https://arxiv.org/abs/2606.08737>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lou2026dreamtac) ⌂
- Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper · NeurIPS 2025 · [ⓘ](../catalog.md#paper-zhu2025touchwild) ⌂
- 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing · CoRL 2024 · [ⓘ](../catalog.md#paper-huang2024vitac) ⌂
- VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning · CoRL 2025 · [ⓘ](../catalog.md#paper-huang2025vtrefine) ⌂
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026) ⌂
- [ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation](<https://arxiv.org/abs/2607.22530>) · arXiv 2026 · [ⓘ](../catalog.md#paper-huang2026vitacworld) ⌂
- [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](<https://arxiv.org/abs/2607.07287>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zhou2026touchworld)
- **ContactWorld**: [What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation](<https://arxiv.org/abs/2606.13877>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zhang2026contactworld) ⌂

### 3.2.5 Predictive Contact and Fast Tactile Correction

- **TacForeSight**: [Force-Guided Tactile World Model for Contact-Rich Manipulation](<https://arxiv.org/abs/2606.11184>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zang2026tacforesight)
- [Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding](<https://arxiv.org/abs/2603.05687>) · arXiv 2026 · [ⓘ](../catalog.md#paper-xu2026cgp) ⌂
- [Adaptive Compliance Policy: Learning Approximate Compliance for Diffusion Guided Control](<https://arxiv.org/abs/2410.09309>) · arXiv 2024 · [ⓘ](../catalog.md#paper-hou2024adaptive) ⌂
- [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](<https://arxiv.org/abs/2503.02881>) · RSS 2025 · [ⓘ](../catalog.md#paper-xue2025reactive) ⌂
- [TacDiffusion: Force-domain Diffusion Policy for Precise Tactile Manipulation](<https://arxiv.org/abs/2409.11047>) · ICRA 2025 · [ⓘ](../catalog.md#paper-wu2025tacdiffusion) ⌂
- [Bioinspired trajectory modulation for effective slip control in robot manipulation](<https://doi.org/10.1038/s42256-025-01062-2>) · Nature Machine Intelligence 2025 · [ⓘ](../catalog.md#paper-nazari2025bioinspired) ⌂
- Towards reliable and damage-less robotic fragile fruit grasping: An enveloping gripper with multimodal strategy inspired by Asian elephant trunk · Computers and Electronics in Agriculture 2025 · [ⓘ](../catalog.md#paper-wang2025towards) ⌂
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026) ⌂
- [ForceDelta-VLA: Distilling Force-Conditioned ActionCorrections for Contact-Rich Manipulation](<https://arxiv.org/abs/2609.18242>) · arXiv 2026 · [ⓘ](../catalog.md#paper-dong2026forcedelta) ⌂
- [Adaptive Contact-Implicit Model Predictive Control with Online Residual Learning](<https://arxiv.org/abs/2310.09893>) · ICRA 2024 · [ⓘ](../catalog.md#paper-huang2024adaptive) ⌂
- [TACO: TActile World Model as a Self-COrrector for Scalable VLA Post-Training](<https://arxiv.org/abs/2607.02840>) · arXiv 2026 · [ⓘ](../catalog.md#paper-liu2026taco) ⌂

### 3.2.6 Scaling Tactile World Models through Vision-to-Touch Transfer

- [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](<https://arxiv.org/abs/2311.18259>) · arXiv 2023 · [ⓘ](../catalog.md#paper-egoexo4d2023)
- **EgoDex**: Learning dexterous manipulation from large-scale egocentric video · ICLR 2026 · [ⓘ](../catalog.md#paper-hoque2026egodex)
- [EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](<https://arxiv.org/abs/2604.07607>) · arXiv 2026 · [ⓘ](../catalog.md#paper-egoverse2026) ⌂
- Learning the Signatures of the Human Grasp Using a Scalable Tactile Glove · Nature 2019 · [ⓘ](../catalog.md#paper-sundaram2019stag) ⌂
- Learning Human–Environment Interactions Using Conformal Tactile Textiles · Nature Electronics 2021 · [ⓘ](../catalog.md#paper-luo2021tactiletextiles) ⌂
- **VTAM**: [Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs](<https://arxiv.org/abs/2603.23481>) · arXiv 2026 · [ⓘ](../catalog.md#paper-yuan2026vtam) ⌂
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026) ⌂
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026) ⌂
- **VT-WAM**: [Visual-Tactile World Action Model for Contact-Rich Manipulation](<https://arxiv.org/abs/2607.02503>) · arXiv 2026 · [ⓘ](../catalog.md#paper-tian2026vtwam)
- **Dream-Tac**: [A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](<https://arxiv.org/abs/2606.08737>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lou2026dreamtac) ⌂
- **Tactile-WAM**: [Touch-Aware World Action Model with Tactile Asymmetric Attention](<https://arxiv.org/abs/2606.26663>) · arXiv 2026 · [ⓘ](../catalog.md#paper-wu2026tactilewam) ⌂
- **MuSe**: [Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force](<https://arxiv.org/abs/2606.30988>) · arXiv 2026 · [ⓘ](../catalog.md#paper-clark2026muse)
- **DexTacWAM**: [A Visuo-Tactile World-Action Model for Dexterous Manipulation](<https://arxiv.org/abs/2609.24976>) · arXiv 2026 · [ⓘ](../catalog.md#paper-yuan2026dextacwam) ⌂
- GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force · Sensors 2017 · [ⓘ](../catalog.md#paper-yuan2017gelsight) ⌂
- [DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](<https://arxiv.org/abs/2005.14679>) · RA-L 2020 · [ⓘ](../catalog.md#paper-lambeta2020digit) ⌂

<a id="sec-3-3"></a>

## 3.3 C: Conditioning and the Action Interface

*Representative works (Figure 2):* [UniSim](../catalog.md#paper-yang2024unisim), [RoboDreamer](../catalog.md#paper-robodreamer2024), [UVA](../catalog.md#paper-li2025uva), [DreamZero](../catalog.md#paper-ye2026dreamzero), [Flex-π](../catalog.md#paper-yan2026flexpi)

- **Genie**: [Generative Interactive Environments](<https://arxiv.org/abs/2402.15391>) · ICML 2024 · [ⓘ](../catalog.md#paper-bruce2024genie) ⌂
- **GAIA-1**: [A Generative World Model for Autonomous Driving](<https://arxiv.org/abs/2309.17080>) · arXiv 2023 · [ⓘ](../catalog.md#paper-hu2023gaia1)
- [Video Generation Models as World Simulators](<https://openai.com/index/video-generation-models-as-world-simulators/>) · 2024 · [ⓘ](../catalog.md#paper-brooks2024sora) ⌂
- **UniSim**: [Learning Interactive Real-World Simulators](<https://arxiv.org/abs/2310.06114>) · ICLR 2024 · [ⓘ](../catalog.md#paper-yang2024unisim) ⌂
- **DreamGen**: [Unlocking Generalization in Robot Learning through Video World Models](<https://arxiv.org/abs/2505.12705>) · CoRL 2025 · [Code](<https://github.com/NVIDIA/GR00T-dreams>) · [ⓘ](../catalog.md#paper-jang2025dreamgen)
- **DreamZero**: [World Action Models are Zero-shot Policies](<https://arxiv.org/abs/2602.15922>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ye2026dreamzero) ⌂
- **RoboDreamer**: [Learning Compositional World Models for Robot Imagination](<https://arxiv.org/abs/2404.12377>) · 2024 · [ⓘ](../catalog.md#paper-robodreamer2024) ⌂
- **EgoWAM**: [World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](<https://arxiv.org/abs/2607.08436>) · arXiv 2026 · [ⓘ](../catalog.md#paper-egowam2026)
- **UVA**: [Unified Video Action Model](<https://arxiv.org/abs/2503.00200>) · arXiv 2025 · [ⓘ](../catalog.md#paper-li2025uva) ⌂
- **Physics-IQ**: [Do Generative Video Models Understand Physical Principles?](<https://arxiv.org/abs/2501.09038>) · WACV 2026 · [ⓘ](../catalog.md#paper-motamed2026physicsiq)
- **WorldArena**: [A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](<https://arxiv.org/abs/2602.08971>) · arXiv 2026 · [ⓘ](../catalog.md#paper-shang2026worldarena)
- [Causally Debiased Latent Action Model for Embodied Action Conditioned World Models](<https://arxiv.org/abs/2607.09185>) · arXiv 2026 · [ⓘ](../catalog.md#paper-wei2026cdlam) ⌂
- **Masked Visual Actions**: [Masked Visual Actions for Unified World Modeling](<https://arxiv.org/abs/2607.19343>) · arXiv 2026 · [ⓘ](../catalog.md#paper-alzayer2026maskedvisual) ⌂
- **WorldEcho**: [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](<https://arxiv.org/abs/2608.24885>) · 2026 · [ⓘ](../catalog.md#paper-chen2026worldsync)
- **TrAct**: [Bridging Robot Control and Visual Prediction with Visual Tracks](<https://arxiv.org/abs/2608.24101>) · 2026 · [ⓘ](../catalog.md#paper-cao2026tract)
- **Hydra-0**: [Action Flow for Generalist World Modeling and Control](<https://arxiv.org/abs/2608.18077>) · 2026 · [ⓘ](../catalog.md#paper-hydra02026) ⌂
- **Cosmos 3**: [Omnimodal World Models for Physical AI](<https://arxiv.org/abs/2606.02800>) · arXiv 2026 · [ⓘ](../catalog.md#paper-nvidia2026cosmos3) ⌂
- **WALL-WM**: [Carving World Action Modeling at the Event Joints](<https://arxiv.org/abs/2606.01955>) · arXiv 2026 · [ⓘ](../catalog.md#paper-xsquare2026wallwm) ⌂
- [RoboOmni: Proactive Robot Manipulation in Omni-modal Context](<https://arxiv.org/abs/2510.23763>) · ICLR 2026 · [ⓘ](../catalog.md#paper-wang2026roboomni) ⌂
- [Atlas: A World Model for Spatial Intelligence](<https://www.worldlabs.ai/blog/atlas>) · World Labs Blog 2026 · [ⓘ](../catalog.md#paper-worldlabs2026atlas) ⌂
- **Puffin-World**: [Scaling a Unified Multimodal Model with Native 3D World States](<https://arxiv.org/abs/2609.04196>) · 2026 · [ⓘ](../catalog.md#paper-liao2026puffinworld) ⌂
- **Flex-π**: [A Multi-Stream World-Action Model with Compute Flexibility](<https://arxiv.org/abs/2608.10860>) · 2026 · [ⓘ](../catalog.md#paper-yan2026flexpi) ⌂

<a id="sec-3-4"></a>

## 3.4 D: Knowledge Sources

*Representative works (Figure 2):* [Cosmos](../catalog.md#paper-nvidia2025cosmos), [DreamDojo](../catalog.md#paper-gao2026dreamdojo), [Isaac Gym](../catalog.md#paper-makoviychuk2021isaacgym), [Ego4D](../catalog.md#paper-grauman-2022-cvpr), [EgoDex](../catalog.md#paper-hoque2026egodex)

### 3.4.1 Foundation Priors and Simulation

- [Omnidexvlg: Learning dexterous grasp generation from vision language model-guided grasp semantics, taxonomy and functional affordance](<https://arxiv.org/abs/2512.03874>) · arXiv 2025 · [ⓘ](../catalog.md#paper-zhang2025omnidexvlg) ⌂
- **Cosmos**: [Cosmos world foundation model platform for physical ai](<https://arxiv.org/abs/2501.03575>) · arXiv 2025 · [ⓘ](../catalog.md#paper-nvidia2025cosmos) ⌂
- **DreamDojo**: [A Generalist Robot World Model from Large-Scale Human Videos](<https://arxiv.org/abs/2602.06949>) · arXiv 2026 · [ⓘ](../catalog.md#paper-gao2026dreamdojo) ⌂
- [MuJoCo: A Physics Engine for Model-Based Control](<https://doi.org/10.1109/IROS.2012.6386109>) · IROS 2012 · [ⓘ](../catalog.md#paper-todorov2012mujoco) ⌂
- **Isaac Gym**: [High Performance GPU-Based Physics Simulation for Robot Learning](<https://arxiv.org/abs/2108.10470>) · arXiv 2021 · [ⓘ](../catalog.md#paper-makoviychuk2021isaacgym) ⌂
- [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](<https://doi.org/10.1109/IROS.2017.8202133>) · IROS 2017 · [ⓘ](../catalog.md#paper-tobin2017domain) ⌂
- [Solving Rubik's Cube with a Robot Hand](<https://arxiv.org/abs/1910.07113>) · arXiv 2019 · [ⓘ](../catalog.md#paper-openai2019rubiks) ⌂

### 3.4.2 Human Video: Scalable Priors, Incomplete Robot Experience

- [Agibot world colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems](<https://arxiv.org/abs/2503.06669>) · arXiv 2025 · [ⓘ](../catalog.md#paper-bu2025agibot) ⌂
- **Ego4D**: Around the World in 3,000 Hours of Egocentric Video · CVPR 2022 · [ⓘ](../catalog.md#paper-grauman-2022-cvpr) ⌂
- **EgoDex**: Learning dexterous manipulation from large-scale egocentric video · ICLR 2026 · [ⓘ](../catalog.md#paper-hoque2026egodex) ⌂
- **EgoScale**: [Scaling dexterous manipulation with diverse egocentric human data](<https://arxiv.org/abs/2602.16710>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zheng2026egoscale) ⌂
- [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](<https://arxiv.org/abs/2606.20521>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ma2026humanscale) ⌂
- [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](<https://arxiv.org/abs/2311.18259>) · arXiv 2023 · [ⓘ](../catalog.md#paper-egoexo4d2023) ⌂
- [H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos](<https://arxiv.org/abs/2505.11920>) · arXiv 2025 · [ⓘ](../catalog.md#paper-h2r2025) ⌂
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](<https://arxiv.org/abs/2412.14172>) · arXiv 2024 · [ⓘ](../catalog.md#paper-humanoidx2024) ⌂
- **EgoZero**: [Robot Learning from Smart Glasses](<https://arxiv.org/abs/2505.20290>) · arXiv 2025 · [ⓘ](../catalog.md#paper-egozero2025) ⌂
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- [EgoMimic: Scaling Imitation Learning via Egocentric Video](<https://arxiv.org/abs/2410.24221>) · arXiv 2024 · [ⓘ](../catalog.md#paper-egomimic2024) ⌂
- [HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos](<https://arxiv.org/abs/2605.24934>) · arXiv 2026 · [ⓘ](../catalog.md#paper-humanego2026) ⌂

### 3.4.3 Grounding Human Interaction into Robot-Controllable Signals

- [MimicPlay: Long-Horizon Imitation Learning by Watching Human Play](<https://arxiv.org/abs/2302.12422>) · CoRL 2023 · [ⓘ](../catalog.md#paper-wang2023mimicplay) ⌂
- [EgoMimic: Scaling Imitation Learning via Egocentric Video](<https://arxiv.org/abs/2410.24221>) · arXiv 2024 · [ⓘ](../catalog.md#paper-egomimic2024) ⌂
- [EMMA: Scaling Mobile Manipulation via Egocentric Human Data](<https://arxiv.org/abs/2509.04443>) · arXiv 2025 · [ⓘ](../catalog.md#paper-emma2025) ⌂
- **EgoDex**: Learning dexterous manipulation from large-scale egocentric video · ICLR 2026 · [ⓘ](../catalog.md#paper-hoque2026egodex) ⌂
- [Scalable vision-language-action model pretraining for robotic manipulation with real-life human activity videos](<https://arxiv.org/abs/2510.21571>) · arXiv 2025 · [ⓘ](../catalog.md#paper-li2025scalable) ⌂
- **EgoZero**: [Robot Learning from Smart Glasses](<https://arxiv.org/abs/2505.20290>) · arXiv 2025 · [ⓘ](../catalog.md#paper-egozero2025) ⌂
- **DreamGen**: [Unlocking Generalization in Robot Learning through Video World Models](<https://arxiv.org/abs/2505.12705>) · CoRL 2025 · [Code](<https://github.com/NVIDIA/GR00T-dreams>) · [ⓘ](../catalog.md#paper-jang2025dreamgen)
- **DreamDojo**: [A Generalist Robot World Model from Large-Scale Human Videos](<https://arxiv.org/abs/2602.06949>) · arXiv 2026 · [ⓘ](../catalog.md#paper-gao2026dreamdojo) ⌂
- **EgoWAM**: [World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](<https://arxiv.org/abs/2607.08436>) · arXiv 2026 · [ⓘ](../catalog.md#paper-egowam2026)
- [H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos](<https://arxiv.org/abs/2505.11920>) · arXiv 2025 · [ⓘ](../catalog.md#paper-h2r2025) ⌂
- [LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment](<https://arxiv.org/abs/2604.10677>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lidea2026) ⌂
- [EgoExo-WM: Unlocking Exo Video for Ego World Models](<https://arxiv.org/abs/2605.15477>) · arXiv 2026 · [ⓘ](../catalog.md#paper-egoexowm2026) ⌂
- [RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning](<https://arxiv.org/abs/2512.02729>) · arXiv 2025 · [ⓘ](../catalog.md#paper-robowheel2025) ⌂
- [HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos](<https://arxiv.org/abs/2605.24934>) · arXiv 2026 · [ⓘ](../catalog.md#paper-humanego2026) ⌂
- [XIRL: Cross-embodiment Inverse Reinforcement Learning](<https://arxiv.org/abs/2106.03911>) · CoRL 2022 · [ⓘ](../catalog.md#paper-xirl2022) ⌂
- [XSkill: Cross Embodiment Skill Discovery](<https://arxiv.org/abs/2307.09955>) · CoRL 2023 · [ⓘ](../catalog.md#paper-xskill2023) ⌂
- **EgoBridge**: [Domain Adaptation for Generalizable Imitation from Egocentric Human Data](<https://arxiv.org/abs/2509.19626>) · arXiv 2025 · [ⓘ](../catalog.md#paper-egobridge2025)
- **TactAlign**: [Human-to-Robot Policy Transfer via Tactile Alignment](<https://arxiv.org/abs/2602.13579>) · arXiv 2026 · [ⓘ](../catalog.md#paper-tactalign2026) ⌂
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- **Zero-WAM**: [In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](<https://arxiv.org/abs/2608.26103>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zhou2026zerowam) ⌂

<a id="sec-3-5"></a>

## 3.5 M: Dynamics Mechanisms and Inference Cost

*Representative works (Figure 2):* RSSMs, [iVideoGPT](../catalog.md#paper-wu2024ivideogpt), [UniPi](../catalog.md#paper-du2023unipi), [CausVid](../catalog.md#paper-yin2024causvid), [Self Forcing](../catalog.md#paper-huang2025selfforcing)

- **PlaNet**: [Learning Latent Dynamics for Planning from Pixels](<https://arxiv.org/abs/1811.04551>) · ICML 2019 · [ⓘ](../catalog.md#paper-hafner2019planet)
- **Dreamer**: [Dream to Control: Learning Behaviors by Latent Imagination](<https://arxiv.org/abs/1912.01603>) · ICLR 2020 · [ⓘ](../catalog.md#paper-hafner2019dreamer)
- **DreamerV2**: [Mastering Atari with Discrete World Models](<https://arxiv.org/abs/2010.02193>) · ICLR 2021 · [ⓘ](../catalog.md#paper-hafner2021dreamerv2) ⌂
- **DreamerV3**: [Mastering Diverse Domains through World Models](<https://arxiv.org/abs/2301.04104>) · 2023 · [Code](<https://github.com/danijar/dreamerv3>) · [ⓘ](../catalog.md#paper-hafner2023dreamerv3)
- **DayDreamer**: [World Models for Physical Robot Learning](<https://arxiv.org/abs/2206.14176>) · CoRL 2022 · [Code](<https://github.com/danijar/daydreamer>) · [ⓘ](../catalog.md#paper-wu2022daydreamer)
- Deep visual foresight for planning robot motion · ICRA 2017 · [ⓘ](../catalog.md#paper-finn2017deep) ⌂
- [Maskvit: Masked visual pre-training for video prediction](<https://arxiv.org/abs/2206.11894>) · arXiv 2022 · [ⓘ](../catalog.md#paper-gupta2022maskvit) ⌂
- **iVideoGPT**: Interactive VideoGPTs are scalable world models · NeurIPS 2024 · [ⓘ](../catalog.md#paper-wu2024ivideogpt) ⌂
- **UniPi**: [Learning Universal Policies via Text-Guided Video Generation](<https://arxiv.org/abs/2302.00111>) · NeurIPS 2023 · [ⓘ](../catalog.md#paper-du2023unipi) ⌂
- **RoboDreamer**: [Learning Compositional World Models for Robot Imagination](<https://arxiv.org/abs/2404.12377>) · 2024 · [ⓘ](../catalog.md#paper-robodreamer2024)
- IRASim: A fine-grained world model for robot manipulation · ICCV 2025 · [ⓘ](../catalog.md#paper-zhu2025irasim) ⌂
- Inference-time enhancement of generative robot policies via predictive world modeling · RA-L 2026 · [ⓘ](../catalog.md#paper-qi2026inference) ⌂
- Ctrl-World: A controllable generative world model for robot manipulation · ICLR 2026 · [ⓘ](../catalog.md#paper-guo2026ctrl)
- **WorldPlanner**: [Monte carlo tree search and mpc with action-conditioned visual world models](<https://arxiv.org/abs/2511.03077>) · arXiv 2025 · [ⓘ](../catalog.md#paper-worldplanner2025)
- [Flow matching for generative modeling](<https://arxiv.org/abs/2210.02747>) · arXiv 2022 · [ⓘ](../catalog.md#paper-lipman2022flow) ⌂
- [Flow straight and fast: Learning to generate and transfer data with rectified flow](<https://arxiv.org/abs/2209.03003>) · arXiv 2022 · [ⓘ](../catalog.md#paper-liu2022flow) ⌂
- [WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](<https://arxiv.org/abs/2606.13672>) · arXiv 2026 · [ⓘ](../catalog.md#paper-jain2026texttt) ⌂
- [τ0-WM: A Unified Video-Action World Model for Robotic Manipulation](<https://arxiv.org/abs/2606.01027>) · 2026 · [ⓘ](../catalog.md#paper-zhou2026tau0wm)
- [DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation](<https://arxiv.org/abs/2606.32028>) · arXiv 2026 · [ⓘ](../catalog.md#paper-shan2026dvg) ⌂
- **ODEWorld**: [A Continuous Predictive Architecture via Physical-Time Flow](<https://arxiv.org/abs/2607.27924>) · 2026 · [ⓘ](../catalog.md#paper-liu2026odeworld)
- [Looped world models](<https://arxiv.org/abs/2606.18208>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lu2026loopwm) ⌂
- **CausVid**: [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](<https://arxiv.org/abs/2412.07772>) · CVPR 2025 · [ⓘ](../catalog.md#paper-yin2024causvid) ⌂
- **Self Forcing**: [Bridging the Train-Test Gap in Autoregressive Video Diffusion](<https://arxiv.org/abs/2506.08009>) · arXiv 2025 · [ⓘ](../catalog.md#paper-huang2025selfforcing) ⌂
- [Self-Forcing++: Towards Minute-Scale High-Quality Video Generation](<https://arxiv.org/abs/2510.02283>) · arXiv 2025 · [ⓘ](../catalog.md#paper-cui2025selfforcingpp) ⌂
- [Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination](<https://arxiv.org/abs/2606.10040>) · arXiv 2026 · [ⓘ](../catalog.md#paper-li2026efficientwam)
- [WorldKV: Efficient World Memory with World Retrieval and Compression](<https://arxiv.org/abs/2605.22718>) · arXiv 2026 · [ⓘ](../catalog.md#paper-yi2026worldkv) ⌂
- [MoWorld: A Flash World Model](<https://arxiv.org/abs/2607.06216>) · arXiv 2026 · [ⓘ](../catalog.md#paper-moxin2026moworld) ⌂
- **ACT-JEPA**: [Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning](<https://arxiv.org/abs/2501.14622>) · arXiv 2025 · [ⓘ](../catalog.md#paper-actjepa2025) ⌂
- [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](<https://arxiv.org/abs/2503.02881>) · RSS 2025 · [ⓘ](../catalog.md#paper-xue2025reactive)
- **Flex-π**: [A Multi-Stream World-Action Model with Compute Flexibility](<https://arxiv.org/abs/2608.10860>) · 2026 · [ⓘ](../catalog.md#paper-yan2026flexpi)
- [RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](<https://arxiv.org/abs/2502.15633>) · 2025 · [ⓘ](../catalog.md#paper-yu2025rgbonlygaussiansplattingslam) ⌂
- [Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian Pointmaps](<https://arxiv.org/abs/2507.03737>) · 2025 · [ⓘ](../catalog.md#paper-cheng2025outdoormonocularslamglobal) ⌂
- [LongStream: Long-Sequence Streaming Autoregressive Visual Geometry](<https://arxiv.org/abs/2602.13172>) · 2026 · [ⓘ](../catalog.md#paper-cheng2026longstreamlongsequencestreamingautoregressive) ⌂
- [HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction](<https://arxiv.org/abs/2605.23889>) · 2026 · [ⓘ](../catalog.md#paper-cheng2026horizonstreamlonghorizonattentionstreaming) ⌂
- [Matrix-Game 2.0: An Open-Source, Real-Time, and Streaming Interactive World Model](<https://arxiv.org/abs/2508.13009>) · arXiv 2025 · [ⓘ](../catalog.md#paper-he2025matrixgame2) ⌂
- **Matrix-Game 3.0**: [Real-Time and Streaming Interactive World Model with Long-Horizon Memory](<https://arxiv.org/abs/2604.08995>) · arXiv 2026 · [ⓘ](../catalog.md#paper-wang2026matrixgame3) ⌂
- [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](<https://arxiv.org/abs/2504.08388>) · arXiv 2025 · [ⓘ](../catalog.md#paper-guo2025mineworld) ⌂
- [StreamDiT: Real-Time Streaming Text-to-Video Generation](<https://arxiv.org/abs/2507.03745>) · arXiv 2025 · [ⓘ](../catalog.md#paper-kodaira2025streamdit) ⌂
- [Genie 3: A New Frontier for World Models](<https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>) · 2025 · [ⓘ](../catalog.md#paper-deepmind2025genie3) ⌂
- [Oasis: A Universe in a Transformer](<https://oasis-model.github.io/>) · 2024 · [ⓘ](../catalog.md#paper-decart2024oasis) ⌂
- **SolarWM**: [Open Data and Scalable Training for Long-Horizon Video World Models](<https://arxiv.org/abs/2609.02886>) · 2026 · [ⓘ](../catalog.md#paper-huang2026solarwm) ⌂

