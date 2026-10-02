# 15. Open Challenges and Future Directions

[Home](../../README.md) · [Reading paths](../reading-paths.md) · [Full catalog](../catalog.md)

The agenda connects action grounding, multimodal contact, query-distribution shift, latency, memory, calibration and auditability to specific evaluation obligations.

## Reading questions

- Which counterfactual queries reveal the gap?
- Which matched-budget comparison can resolve it?
- What evidence would overturn the proposed explanation?

## Interpretation boundary

Proposed utility curves, optimism gaps and reliability margins are research analyses, not measured universal findings.

## Selected annotations

- [PlaNet](../methods.md#paper-hafner2019planet)
- [Dreamer4](../methods.md#paper-hafner2025dreamer4)
- [V-JEPA 2](../methods.md#paper-assran2025vjepa2)
- [ACT-JEPA](../methods.md#paper-actjepa2025)
- [PhysTwin](../methods.md#paper-jiang2025phystwin)
- [Interactive World Simulator (IWS)](../methods.md#paper-interactiveworldsim2026)
- [GE-Sim 2.0](../methods.md#paper-qiu2026gesim2)
- [DreamGen](../methods.md#paper-jang2025dreamgen)
- [DreamDojo](../methods.md#paper-gao2026dreamdojo)
- [WorldEval](../methods.md#paper-li2025worldeval)
- [Cosmos](../methods.md#paper-nvidia2025cosmos)
- [Cosmos 3](../methods.md#paper-nvidia2026cosmos3)
- [Manipulation by Feel](../methods.md#paper-tian2019manipulation)
- [OmniVTA](../methods.md#paper-omnivta2026)
- [Visuo-Tactile World Models](../methods.md#paper-visuotactilewm2026)
- [EgoWAM](../methods.md#paper-egowam2026)
- [VLAW](../methods.md#paper-vlaw2026)
- [WorldSample](../methods.md#paper-xue2026worldsample)
- [World-in-World](../methods.md#paper-worldinworld2025)
- [SafeDreamer](../methods.md#paper-huang2024safedreamer)

## References by argument (137 distinct works)

The groups follow the paper’s citation-bearing subsections, including active tables and figures. A work can support several arguments and appear more than once. For a more flexible reading order, use the [topic index](../paper-index.md). Membership is not a strict closed-loop inclusion judgment.

<a id="argument-093"></a>

### The Prediction-to-Control Gap: Prediction Fidelity vs. Policy Utility

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [Objective Mismatch in Model-based Reinforcement Learning](../catalog.md#paper-lambert2020objective) | Source metadata only |
| 2023 | [A Control-Centric Benchmark for Video Prediction](../catalog.md#paper-tian2023vp2) | [Paper](<https://arxiv.org/abs/2304.13723>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2024 | [Diffusion for World Modeling: Visual Details Matter in Atari](../catalog.md#paper-alonso2024diamond) | [Paper](<https://arxiv.org/abs/2405.12399>) |
| 2017 | [Value-Aware Loss Function for Model-based Reinforcement Learning](../catalog.md#paper-farahmand2017vaml) | Source metadata only |
| 2020 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](../catalog.md#paper-grimm2020value) | Source metadata only |
| 2026 | [EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data](../catalog.md#paper-egowam2026) | [Paper](<https://arxiv.org/abs/2607.08436>) |
| 2026 | [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](../catalog.md#paper-liu2026palm) | Source metadata only |
| 2025 | [Calibrated Value-Aware Model Learning with Probabilistic Environment Models](../catalog.md#paper-voelcker2025calibrated) | [Paper](<https://proceedings.mlr.press/v267/voelcker25a.html>) |
| 2025 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../catalog.md#paper-assran2025vjepa2) | [Paper](<https://arxiv.org/abs/2506.09985>) |
| 2022 | [Deciding What to Model: Value-Equivalent Sampling for Reinforcement Learning](../catalog.md#paper-arumugam2022deciding) | [Paper](<https://arxiv.org/abs/2206.02072>) |
| 2022 | [Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems](../catalog.md#paper-subramanian2022ais) | [Paper](<https://www.jmlr.org/papers/v23/20-1165.html>) |
| 2019 | [Manipulation by Feel: Touch-Based Control with Deep Predictive Models](../catalog.md#paper-tian2019manipulation) | [Paper](<https://arxiv.org/abs/1903.04128>) |

<a id="argument-094"></a>

### Physical Interaction World Models: Contact, Force, and Deformation

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |
| 2025 | [Learning Humanoid Locomotion with World Model Reconstruction](../catalog.md#paper-wmr2025) | [Paper](<https://arxiv.org/abs/2502.16230>) |
| 2025 | [Ego-vision world model for humanoid contact planning](../catalog.md#paper-egovisioncontact2025) | [Paper](<https://arxiv.org/abs/2510.11682>) |

<a id="argument-095"></a>

### Inference Efficiency and the Latency Wall

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [From Slow Bidirectional to Fast Autoregressive Video Diffusion Models](../catalog.md#paper-yin2024causvid) | [Paper](<https://arxiv.org/abs/2412.07772>) |
| 2025 | [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](../catalog.md#paper-huang2025selfforcing) | [Paper](<https://arxiv.org/abs/2506.08009>) |
| 2025 | [Self-Forcing++: Towards Minute-Scale High-Quality Video Generation](../catalog.md#paper-cui2025selfforcingpp) | [Paper](<https://arxiv.org/abs/2510.02283>) |
| 2026 | [WorldKV: Efficient World Memory with World Retrieval and Compression](../catalog.md#paper-yi2026worldkv) | [Paper](<https://arxiv.org/abs/2605.22718>) |
| 2026 | [MoWorld: A Flash World Model](../catalog.md#paper-moxin2026moworld) | [Paper](<https://arxiv.org/abs/2607.06216>) |
| 2025 | [ACT-JEPA: Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning](../catalog.md#paper-actjepa2025) | [Paper](<https://arxiv.org/abs/2501.14622>) |
| 2025 | [Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation](../catalog.md#paper-xue2025reactive) | [Paper](<https://arxiv.org/abs/2503.02881>) |
| 2026 | [Flex-π: A Multi-Stream World-Action Model with Compute Flexibility](../catalog.md#paper-yan2026flexpi) | [Paper](<https://arxiv.org/abs/2608.10860>) |
| 2026 | [Scaling up test-time compute with latent reasoning: A recurrent depth approach](../catalog.md#paper-geiping2025recurrentdepth) | Source metadata only |
| 2026 | [Looped world models](../catalog.md#paper-lu2026loopwm) | [Paper](<https://arxiv.org/abs/2606.18208>) |
| 2025 | [Two-Scale Latent Dynamics for Recurrent-Depth Transformers](../catalog.md#paper-pappone2025twoscale) | [Paper](<https://arxiv.org/abs/2509.23314>) |

<a id="argument-096"></a>

### Streaming, Full-Duplex, and Self-Evolving World Models

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](../catalog.md#paper-yu2025rgbonlygaussiansplattingslam) | [Paper](<https://arxiv.org/abs/2502.15633>) |
| 2025 | [Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian Pointmaps](../catalog.md#paper-cheng2025outdoormonocularslamglobal) | [Paper](<https://arxiv.org/abs/2507.03737>) |
| 2026 | [LongStream: Long-Sequence Streaming Autoregressive Visual Geometry](../catalog.md#paper-cheng2026longstreamlongsequencestreamingautoregressive) | [Paper](<https://arxiv.org/abs/2602.13172>) |
| 2026 | [HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction](../catalog.md#paper-cheng2026horizonstreamlonghorizonattentionstreaming) | [Paper](<https://arxiv.org/abs/2605.23889>) |
| 2025 | [Matrix-Game 2.0: An Open-Source, Real-Time, and Streaming Interactive World Model](../catalog.md#paper-he2025matrixgame2) | [Paper](<https://arxiv.org/abs/2508.13009>) |
| 2026 | [Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory](../catalog.md#paper-wang2026matrixgame3) | [Paper](<https://arxiv.org/abs/2604.08995>) |
| 2025 | [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](../catalog.md#paper-guo2025mineworld) | [Paper](<https://arxiv.org/abs/2504.08388>) |
| 2025 | [StreamDiT: Real-Time Streaming Text-to-Video Generation](../catalog.md#paper-kodaira2025streamdit) | [Paper](<https://arxiv.org/abs/2507.03745>) |
| 2025 | [Genie 3: A New Frontier for World Models](../catalog.md#paper-deepmind2025genie3) | [Paper](<https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>) |
| 2024 | [Oasis: A Universe in a Transformer](../catalog.md#paper-decart2024oasis) | [Paper](<https://oasis-model.github.io/>) |
| 2026 | [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](../catalog.md#paper-huang2026solarwm) | [Paper](<https://arxiv.org/abs/2609.02886>) |
| 2026 | [Stream-T1: Test-Time Scaling for Streaming Video Generation](../catalog.md#paper-tu2026streamt1) | [Paper](<https://arxiv.org/abs/2605.04461>) |
| 2026 | [Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation](../catalog.md#paper-zhao2026ttswam) | [Paper](<https://arxiv.org/abs/2607.17454>) |
| 2023 | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](../catalog.md#paper-bousmalis2023robocat) | [Paper](<https://arxiv.org/abs/2306.11706>) |
| 2025 | [EvoVLA: Self-Evolving Vision-Language-Action Model](../catalog.md#paper-liu2025evovla) | [Paper](<https://arxiv.org/abs/2511.16166>) |
| 2026 | [Self-Evolving World Models for LLM Agent Planning](../catalog.md#paper-zhang2026worldevolver) | [Paper](<https://arxiv.org/abs/2606.30639>) |
| 2024 | [Moshi: a speech-text foundation model for real-time dialogue](../catalog.md#paper-defossez2024moshi) | [Paper](<https://arxiv.org/abs/2410.00037>) |
| 2026 | [DuplexSLA: A Full-Duplex Spoken Language Model with Synchronized Speech, Language, and Action](../catalog.md#paper-zhang2026duplexsla) | [Paper](<https://arxiv.org/abs/2605.20755>) |
| 2026 | [DyaPlex: Full-Duplex Speech-Motion Model for Dyadic Interaction](../catalog.md#paper-nagano2026dyaplex) | [Paper](<https://arxiv.org/abs/2606.03874>) |

<a id="argument-097"></a>

### Memory and Long-Horizon World Models

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [WorldMem: Long-term Consistent World Simulation with Memory](../catalog.md#paper-xiao2025worldmem) | [Paper](<https://arxiv.org/abs/2504.12369>) |
| 2025 | [Video World Models with Long-term Spatial Memory](../catalog.md#paper-wu2025spatialmem) | [Paper](<https://arxiv.org/abs/2506.05284>) |
| 2025 | [Long-Context State-Space Video World Models](../catalog.md#paper-po2025ssmwm) | [Paper](<https://arxiv.org/abs/2505.20171>) |
| 2026 | [DecMem: Towards Minute-Long Consistent World Generation with Decoupled Memory](../catalog.md#paper-yang2026decmem) | [Paper](<https://arxiv.org/abs/2605.31336>) |
| 2026 | [Beyond Pixel Histories: World Models with Persistent 3D State](../catalog.md#paper-garcin2026persist) | [Paper](<https://arxiv.org/abs/2603.03482>) |
| 2026 | [LIVE: Long-horizon Interactive Video World Modeling](../catalog.md#paper-huang2026live) | [Paper](<https://arxiv.org/abs/2602.03747>) |
| 2025 | [Training Agents Inside of Scalable World Models](../catalog.md#paper-hafner2025dreamer4) | [Paper](<https://arxiv.org/abs/2509.24527>) |
| 2022 | [Deep Hierarchical Planning from Pixels](../catalog.md#paper-hafner2022director) | [Paper](<https://arxiv.org/abs/2206.04114>) |
| 2026 | [Hierarchical Planning with Latent World Models](../catalog.md#paper-zhang2026hierarchical) | [Paper](<https://arxiv.org/abs/2604.03208>) |

<a id="argument-098"></a>

### Causal and Counterfactual World Models

| Year | Work | Primary entry |
|---|---|---|
| 2021 | [Causal Reasoning in Simulation for Structure and Transfer Learning of Robot Manipulation Policies](../catalog.md#paper-lee2021crest) | [Paper](<https://doi.org/10.1109/icra48506.2021.9561439>) |
| 2019 | [Causal Confusion in Imitation Learning](../catalog.md#paper-dehaan2019causal) | [Paper](<https://arxiv.org/abs/1905.11979>) |
| 2020 | [Counterfactual Data Augmentation using Locally Factored Dynamics](../catalog.md#paper-pitis2020coda) | [Paper](<https://arxiv.org/abs/2007.02863>) |
| 2021 | [CausalWorld: A Robotic Manipulation Benchmark for Causal Structure and Transfer Learning](../catalog.md#paper-ahmed2021causalworld) | [Paper](<https://arxiv.org/abs/2010.04296>) |
| 2020 | [CoPhy: Counterfactual Learning of Physical Dynamics](../catalog.md#paper-baradel2020cophy) | [Paper](<https://arxiv.org/abs/1909.12000>) |

<a id="argument-099"></a>

### Robotics Scaling Laws

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [World-in-world: World models in a closed-loop world](../catalog.md#paper-worldinworld2025) | [Paper](<https://arxiv.org/abs/2510.18135>) |
| 2026 | [Looped world models](../catalog.md#paper-lu2026loopwm) | [Paper](<https://arxiv.org/abs/2606.18208>) |
| 2026 | [Scaling up test-time compute with latent reasoning: A recurrent depth approach](../catalog.md#paper-geiping2025recurrentdepth) | Source metadata only |
| 2019 | [Learning Latent Dynamics for Planning from Pixels](../catalog.md#paper-hafner2019planet) | [Paper](<https://arxiv.org/abs/1811.04551>) |
| 2024 | [Scaling llm test-time compute optimally can be more effective than scaling model parameters](../catalog.md#paper-snell2024scaling) | [Paper](<https://arxiv.org/abs/2408.03314>) |

<a id="argument-100"></a>

### Synthetic Data Flywheels

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](../catalog.md#paper-mimicgen) | [Paper](<https://arxiv.org/abs/2310.17596>) |
| 2024 | [Gensim: Generating robotic simulation tasks via large language models](../catalog.md#paper-wang2024gensim) | Source metadata only |
| 2026 | [Geometry-Instructed Video Editing](../catalog.md#paper-chang2026geometry) | [Paper](<https://arxiv.org/abs/2606.24225>) |
| 2026 | [ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation](../catalog.md#paper-zhou2026assist) | Source metadata only |
| 2025 | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](../catalog.md#paper-jiang2025phystwin) | [Paper](<https://arxiv.org/abs/2503.17973>) |
| 2024 | [Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation](../catalog.md#paper-torne2024rialto) | [Paper](<https://doi.org/10.15607/RSS.2024.XX.015>) |
| 2024 | [Total-decom: Decomposed 3d scene reconstruction with minimal interaction](../catalog.md#paper-lyu2024total) | Source metadata only |
| 2025 | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](../catalog.md#paper-jang2025dreamgen) | [Paper](<https://arxiv.org/abs/2505.12705>) |
| 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](../catalog.md#paper-interactiveworldsim2026) | [Paper](<https://arxiv.org/abs/2603.08546>) |
| 2025 | [How far are ai-generated videos from simulating the 3d visual world: A learned 3d evaluation approach](../catalog.md#paper-chang2025far) | Source metadata only |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |

<a id="argument-101"></a>

### Safety and Trust Calibration

| Year | Work | Primary entry |
|---|---|---|
| 2019 | [When to Trust Your Model: Model-Based Policy Optimization](../catalog.md#paper-janner2019mbpo) | [Paper](<https://arxiv.org/abs/1906.08253>) |
| 2019 | [Can you trust your model's uncertainty? Evaluating predictive uncertainty under dataset shift](../catalog.md#paper-ovadia2019can) | Source metadata only |
| 2024 | [The safety filter: A unified view of safety-critical control in autonomous systems](../catalog.md#paper-hsu2024safety) | Source metadata only |
| 2023 | [Data-driven safety filters: Hamilton-Jacobi reachability, control barrier functions, and predictive methods for uncertain systems](../catalog.md#paper-wabersich2023data) | Source metadata only |
| 2017 | [Hamilton-Jacobi reachability: A brief overview and recent advances](../catalog.md#paper-bansal2017hamilton) | Source metadata only |
| 2019 | [Control Barrier Functions: Theory and Applications](../catalog.md#paper-ames2019cbf) | [Paper](<https://doi.org/10.23919/ECC.2019.8796030>) |
| 2021 | [A predictive safety filter for learning-based control of constrained nonlinear dynamical systems](../catalog.md#paper-wabersich2021predictive) | Source metadata only |
| 2025 | [Generalizing safety beyond collision-avoidance via latent-space reachability analysis](../catalog.md#paper-nakamura2025generalizing) | Source metadata only |
| 2025 | [Uncertainty-aware latent safety filters for avoiding out-of-distribution failures](../catalog.md#paper-seo2025uncertainty) | Source metadata only |
| 2026 | [AnySafe: Adapting latent safety filters at runtime via safety constraint parameterization in the latent space](../catalog.md#paper-agrawal2026anysafe) | Source metadata only |
| 2026 | [How to train your latent control barrier function: Smooth safety filtering under hard-to-model constraints](../catalog.md#paper-nakamura2026train) | Source metadata only |
| 2018 | [Probabilistically safe robot planning with confidence-based human predictions](../catalog.md#paper-fisac2018probabilistically) | Source metadata only |
| 2020 | [Confidence-aware motion prediction for real-time collision avoidance](../catalog.md#paper-fridovich2020confidence) | Source metadata only |
| 2020 | [MOPO: Model-based Offline Policy Optimization](../catalog.md#paper-mopo) | [Paper](<https://proceedings.neurips.cc/paper_files/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf>) |
| 2022 | [Constrained policy optimization via Bayesian world models](../catalog.md#paper-as2022constrained) | Source metadata only |
| 2024 | [Safedreamer: Safe reinforcement learning with world models](../catalog.md#paper-huang2024safedreamer) | [Paper](<https://arxiv.org/abs/2307.07176>) |
| 2023 | [Closing the loop on runtime monitors with fallback-safe MPC](../catalog.md#paper-sinha2023closing) | Source metadata only |
| 2025 | [Unpacking failure modes of generative policies: Runtime monitoring of consistency and progress](../catalog.md#paper-agia2025unpacking) | Source metadata only |
| 2025 | [Can we detect failures without failure data? Uncertainty-aware runtime failure detection for imitation learning policies](../catalog.md#paper-xu2025can) | Source metadata only |
| 2023 | [Safe planning in dynamic environments using conformal prediction](../catalog.md#paper-lindemann2023safe) | Source metadata only |
| 2024 | [Conformal decision theory: Safe autonomous decisions from imperfect predictions](../catalog.md#paper-lekeufack2024conformal) | Source metadata only |
| 1997 | [Humans and automation: Use, misuse, disuse, abuse](../catalog.md#paper-parasuraman1997humans) | Source metadata only |
| 2004 | [Trust in Automation: Designing for Appropriate Reliance](../catalog.md#paper-leesee2004trust) | [Paper](<https://doi.org/10.1518/hfes.46.1.50_30392>) |
| 2019 | [“Dave... I can assure you... that it's going to be all right...” A definition, case for, and survey of algorithmic assurances in human-autonomy trust relationships](../catalog.md#paper-israelsen2019dave) | Source metadata only |
| 2024 | [A survey of algorithmic methods for competency self-assessments in human-autonomy teaming](../catalog.md#paper-conlon2024survey) | Source metadata only |
| 2016 | [Introspective Perception: Learning to Predict Failures in Vision Systems](../catalog.md#paper-daftry2016introspective) | Source metadata only |
| 2018 | [Learn from experience: Probabilistic prediction of perception performance to avoid failure](../catalog.md#paper-gurau2018learn) | Source metadata only |
| 2020 | [Trust-aware decision making for human-robot collaboration: Model learning and planning](../catalog.md#paper-chen2020trust) | Source metadata only |
| 2016 | [Trust calibration within a human-robot team: Comparing automatically generated explanations](../catalog.md#paper-wang2016trust) | Source metadata only |
| 2020 | [Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making](../catalog.md#paper-zhang2020effect) | Source metadata only |
| 2023 | [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](../catalog.md#paper-ren2023knowno) | [Paper](<https://proceedings.mlr.press/v229/ren23a.html>) |
| 2024 | [Introspective planning: Aligning robots' uncertainty with inherent task ambiguity](../catalog.md#paper-liang2024introspective) | Source metadata only |
| 2026 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](../catalog.md#paper-ups2026) | [Paper](<https://arxiv.org/abs/2602.22474>) |
| 2025 | [Robots that suggest safe alternatives](../catalog.md#paper-jeong2025robots) | Source metadata only |
| 2020 | [Objective Mismatch in Model-based Reinforcement Learning](../catalog.md#paper-lambert2020objective) | Source metadata only |
| 2015 | [Representing autonomous systems' self-confidence through competency boundaries](../catalog.md#paper-hutchins2015representing) | Source metadata only |
| 2025 | [Not all errors are made equal: A regret metric for detecting system-level trajectory prediction failures](../catalog.md#paper-nakamura2025not) | Source metadata only |
| 2025 | [Updating robot safety representations online from natural language feedback](../catalog.md#paper-santos2025updating) | Source metadata only |
| 2023 | [Adaptive conformal prediction for motion planning among dynamic agents](../catalog.md#paper-dixit2023adaptive) | Source metadata only |
| 2019 | [Updates in human-AI teams: Understanding and addressing the performance/compatibility tradeoff](../catalog.md#paper-bansal2019updates) | Source metadata only |
| 2024 | [Verification of neural reachable tubes via scenario optimization and conformal prediction](../catalog.md#paper-lin2024verification) | Source metadata only |

<a id="argument-102"></a>

### Closed-Source Frontier Systems

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Gemini robotics: Bringing ai into the physical world](../catalog.md#paper-team2025gemini) | [Paper](<https://arxiv.org/abs/2503.20020>) |
| 2025 | [Gemini robotics 1.5: Pushing the frontier of generalist robots with advanced embodied reasoning, thinking, and motion transfer](../catalog.md#paper-team2025gemini15) | [Paper](<https://arxiv.org/abs/2510.03342>) |
| 2025 | [Helix: A Vision-Language-Action Model for Generalist Humanoid Control](../catalog.md#paper-figure2025helix) | [Paper](<https://www.figure.ai/news/helix>) |
| 2026 | [Introducing Helix 02: Full-Body Autonomy](../catalog.md#paper-figure2026helix02) | [Paper](<https://www.figure.ai/news/helix-02>) |
| 2025 | [Building the General-Purpose Robotic Brain](../catalog.md#paper-skild2025brain) | [Paper](<https://skild.ai/blogs/building-the-general-purpose-robotic-brain>) |
| 2025 | [1X World Model: Evaluating Bits, not Atoms](../catalog.md#paper-ho2025-1xworldmodel) | [Paper](<https://www.1x.tech/1x-world-model.pdf>) |
| 2026 | [1X World Model: From Video to Action—A New Way Robots Learn](../catalog.md#paper-onex2026worldmodelpolicy) | [Paper](<https://www.1x.tech/discover/world-model-self-learning>) |
| 2024 | [Introducing RFM-1: Giving Robots Human-Like Reasoning Capabilities](../catalog.md#paper-sohn2024rfm1) | [Paper](<https://covariant.ai/insights/introducing-rfm-1-giving-robots-human-like-reasoning-capabilities/>) |
| 2026 | [Field Foundation Models and Belief World Models for General Robot Intelligence](../catalog.md#paper-fieldai2026ffm) | [Paper](<https://www.fieldai.com/>) |
| 2025 | [Cosmos world foundation model platform for physical ai](../catalog.md#paper-nvidia2025cosmos) | [Paper](<https://arxiv.org/abs/2501.03575>) |
| 2025 | [Gr00t n1: An open foundation model for generalist humanoid robots](../catalog.md#paper-nvidia2025groot) | [Paper](<https://arxiv.org/abs/2503.14734>) |

<a id="argument-103"></a>

### Toward World-Model-Centric Robot Learning Systems

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Cosmos 3: Omnimodal World Models for Physical AI](../catalog.md#paper-nvidia2026cosmos3) | [Paper](<https://arxiv.org/abs/2606.02800>) |
| 2026 | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](../catalog.md#paper-gao2026dreamdojo) | [Paper](<https://arxiv.org/abs/2602.06949>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2025 | [WorldGym: World Model as An Environment for Policy Evaluation](../catalog.md#paper-quevedo2025wpe) | [Paper](<https://arxiv.org/abs/2506.00613>) |
| 2026 | [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](../catalog.md#paper-qiu2026gesim2) | [Paper](<https://arxiv.org/abs/2605.27491>) |
| 2026 | [World Action Models are Zero-shot Policies](../catalog.md#paper-ye2026dreamzero) | [Paper](<https://arxiv.org/abs/2602.15922>) |
| 2026 | [Native Video-Action Pretraining for Generalizable Robot Control](../catalog.md#paper-zhang2026lingbotva2) | [Paper](<https://arxiv.org/abs/2607.08639>) |
| 2025 | [Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation](../catalog.md#paper-liao2025genie) | [Paper](<https://arxiv.org/abs/2508.05635>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |

<a id="argument-104"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 1: Role-Specific Leaderboards

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |

<a id="argument-105"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 2: Query-Distribution Evaluation

| Year | Work | Primary entry |
|---|---|---|
| 2017 | [Deep Reinforcement Learning from Human Preferences](../catalog.md#paper-christiano2017preferences) | [Paper](<https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |

<a id="argument-106"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 3: Failure Libraries as Shared Infrastructure

| Year | Work | Primary entry |
|---|---|---|
| 2023 | [Reflect: Summarizing robot experiences for failure explanation and correction](../catalog.md#paper-liu2023reflect) | [Paper](<https://arxiv.org/abs/2306.15724>) |

<a id="argument-107"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 4: Policy-Model Co-Training

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |

<a id="argument-108"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 5: Multimodal Physical Grounding

| Year | Work | Primary entry |
|---|---|---|
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-109"></a>

### A Research Agenda for RL-Centric Robot World Models › Agenda Item 6: Auditable Foundation Robot Systems

| Year | Work | Primary entry |
|---|---|---|
| 2025 | [Towards Safe Robot Foundation Models](../catalog.md#paper-saferobotfoundation2025) | [Paper](<https://arxiv.org/abs/2503.07404>) |
| 2025 | [WorldEval: World Model as Real-World Robot Policies Evaluator](../catalog.md#paper-li2025worldeval) | [Paper](<https://arxiv.org/abs/2505.19017>) |
| 2017 | [Deep Reinforcement Learning from Human Preferences](../catalog.md#paper-christiano2017preferences) | [Paper](<https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html>) |
| 2023 | [Reflect: Summarizing robot experiences for failure explanation and correction](../catalog.md#paper-liu2023reflect) | [Paper](<https://arxiv.org/abs/2306.15724>) |
| 2026 | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](../catalog.md#paper-vlaw2026) | [Paper](<https://arxiv.org/abs/2602.12063>) |
| 2026 | [WorldSample: Closed-loop Real-robot RL with World Modelling](../catalog.md#paper-xue2026worldsample) | [Paper](<https://arxiv.org/abs/2607.02431>) |
| 2026 | [Visuo-Tactile World Models](../catalog.md#paper-visuotactilewm2026) | [Paper](<https://arxiv.org/abs/2602.06001>) |
| 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](../catalog.md#paper-omnivta2026) | [Paper](<https://arxiv.org/abs/2603.19201>) |

<a id="argument-110"></a>

### A Closing Thesis

| Year | Work | Primary entry |
|---|---|---|
| 2020 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](../catalog.md#paper-grimm2020value) | Source metadata only |

