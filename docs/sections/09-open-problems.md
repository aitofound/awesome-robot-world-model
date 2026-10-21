# 9 · Open Problems

[Home](../../README.md) · [← 8 · The Outer Loop: From Deployment Experience to Model Improvement](08-outer-loop.md) · [10 · Conclusion →](10-conclusion.md)

Every design dial is an open trade-off, and the Prediction-to-Control Gap prevents settling any of them in isolation. The open problems cover the gap itself, one problem per dial, and two deployment questions: safety and trust calibration, and auditable closed systems. Each is paired with a comparison that would make progress measurable.

This section cites 105 works. A work cited in several subsections appears under each; ⌂ marks the subsection where the README lists it.

<a id="sec-9-1"></a>

## 9.1 The Prediction-to-Control Gap

*Representative works (Figure 2):* what to preserve before the consumer is known

- Objective Mismatch in Model-based Reinforcement Learning · Proceedings of the 2nd Conference on Learning for Dynamics and Control 2020 · [ⓘ](../catalog.md#paper-lambert2020objective)
- **VP²**: [A Control-Centric Benchmark for Video Prediction](<https://arxiv.org/abs/2304.13723>) · ICLR 2023 · [ⓘ](../catalog.md#paper-tian2023vp2) ⌂
- **WorldEval**: [World Model as Real-World Robot Policies Evaluator](<https://arxiv.org/abs/2505.19017>) · arXiv 2025 · [ⓘ](../catalog.md#paper-worldeval2025)
- [Diffusion for World Modeling: Visual Details Matter in Atari](<https://arxiv.org/abs/2405.12399>) · NeurIPS 2024 · [ⓘ](../catalog.md#paper-alonso2024diamond)
- [Calibrated Value-Aware Model Learning with Probabilistic Environment Models](<https://proceedings.mlr.press/v267/voelcker25a.html>) · ICML 2025 · [ⓘ](../catalog.md#paper-voelcker2025calibrated) ⌂
- **V-JEPA 2-AC**: [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](<https://arxiv.org/abs/2506.09985>) · arXiv 2025 · [Code](<https://github.com/facebookresearch/vjepa2>) · [ⓘ](../catalog.md#paper-assran2025vjepa2)
- **Manipulation by Feel**: [Touch-Based Control with Deep Predictive Models](<https://arxiv.org/abs/1903.04128>) · ICRA 2019 · [ⓘ](../catalog.md#paper-tian2019manipulation)
- [Deep Reinforcement Learning from Human Preferences](<https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html>) · NeurIPS 2017 · [ⓘ](../catalog.md#paper-christiano2017preferences)

<a id="sec-9-2"></a>

## 9.2 Physical Grounding and Causal Structure

*Representative works (Figure 2):* contact, deformation, interventions

- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026)
- **WMR**: [Learning Humanoid Locomotion with World Model Reconstruction](<https://arxiv.org/abs/2502.16230>) · 2025 · [ⓘ](../catalog.md#paper-wmr2025)
- **Ego-Vision Contact Planning**: [Ego-vision world model for humanoid contact planning](<https://arxiv.org/abs/2510.11682>) · arXiv 2025 · [ⓘ](../catalog.md#paper-egovisioncontact2025)
- [Causal Reasoning in Simulation for Structure and Transfer Learning of Robot Manipulation Policies](<https://doi.org/10.1109/icra48506.2021.9561439>) · ICRA 2021 · [ⓘ](../catalog.md#paper-lee2021crest) ⌂
- [Causal Confusion in Imitation Learning](<https://arxiv.org/abs/1905.11979>) · NeurIPS 2019 · [ⓘ](../catalog.md#paper-dehaan2019causal) ⌂
- [Counterfactual Data Augmentation using Locally Factored Dynamics](<https://arxiv.org/abs/2007.02863>) · NeurIPS 2020 · [ⓘ](../catalog.md#paper-pitis2020coda) ⌂
- [CausalWorld: A Robotic Manipulation Benchmark for Causal Structure and Transfer Learning](<https://arxiv.org/abs/2010.04296>) · ICLR 2021 · [ⓘ](../catalog.md#paper-ahmed2021causalworld) ⌂
- [CoPhy: Counterfactual Learning of Physical Dynamics](<https://arxiv.org/abs/1909.12000>) · ICLR 2020 · [ⓘ](../catalog.md#paper-baradel2020cophy)

<a id="sec-9-3"></a>

## 9.3 Action Following and the Coupling of Prediction and Action

*Representative works (Figure 2):* off-demonstration queries, joint vs. separate

- **DreamZero**: [World Action Models are Zero-shot Policies](<https://arxiv.org/abs/2602.15922>) · arXiv 2026 · [ⓘ](../catalog.md#paper-ye2026dreamzero)
- [Genie 3: A New Frontier for World Models](<https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>) · 2025 · [ⓘ](../catalog.md#paper-deepmind2025genie3)
- [Oasis: A Universe in a Transformer](<https://oasis-model.github.io/>) · 2024 · [ⓘ](../catalog.md#paper-decart2024oasis)
- [Introducing Oasis 3: First Interactive World Model for Physical AI](<https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai>) · 2026 · [ⓘ](../catalog.md#paper-decart2026oasis3) ⌂

<a id="sec-9-4"></a>

## 9.4 Data, Scaling, and Synthetic Experience

*Representative works (Figure 2):* grounded vs. abundant data, synthetic flywheels

- **World-in-World**: [World models in a closed-loop world](<https://arxiv.org/abs/2510.18135>) · ICLR 2026 · [ⓘ](../catalog.md#paper-worldinworld2025)
- [Looped world models](<https://arxiv.org/abs/2606.18208>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lu2026loopwm)
- Scaling up test-time compute with latent reasoning: A recurrent depth approach · NeurIPS 2026 · [ⓘ](../catalog.md#paper-geiping2025recurrentdepth) ⌂
- **PlaNet**: [Learning Latent Dynamics for Planning from Pixels](<https://arxiv.org/abs/1811.04551>) · ICML 2019 · [ⓘ](../catalog.md#paper-hafner2019planet)
- [Scaling llm test-time compute optimally can be more effective than scaling model parameters](<https://arxiv.org/abs/2408.03314>) · arXiv 2024 · [ⓘ](../catalog.md#paper-snell2024scaling) ⌂
- How far are ai-generated videos from simulating the 3d visual world: A learned 3d evaluation approach · ICCV 2025 · [ⓘ](../catalog.md#paper-chang2025far) ⌂
- **WorldEval**: [World Model as Real-World Robot Policies Evaluator](<https://arxiv.org/abs/2505.19017>) · arXiv 2025 · [ⓘ](../catalog.md#paper-worldeval2025)
- **VLAW**: [Iterative Co-Improvement of Vision-Language-Action Policy and World Model](<https://arxiv.org/abs/2602.12063>) · arXiv 2026 · [ⓘ](../catalog.md#paper-vlaw2026)
- **WorldSample**: [Closed-loop Real-robot RL with World Modelling](<https://arxiv.org/abs/2607.02431>) · arXiv 2026 · [ⓘ](../catalog.md#paper-xue2026worldsample)
- **REFLECT**: [Summarizing robot experiences for failure explanation and correction](<https://arxiv.org/abs/2306.15724>) · arXiv 2023 · [ⓘ](../catalog.md#paper-liu2023reflect)
- [Robomind: Benchmark on multi-embodiment intelligence normative data for robot manipulation](<https://arxiv.org/abs/2412.13877>) · arXiv 2024 · [ⓘ](../catalog.md#paper-wu2024robomind) ⌂
- **RoboNet**: [Large-Scale Multi-Robot Learning](<https://arxiv.org/abs/1910.11215>) · 2019 · [ⓘ](../catalog.md#paper-robonet)
- **Open X-Embodiment**: [Robotic Learning Datasets and RT-X Models](<https://arxiv.org/abs/2310.08864>) · ICRA 2024 · [Code](<https://github.com/google-deepmind/open_x_embodiment>) · [ⓘ](../catalog.md#paper-openxembodiment2023)
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026)
- [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](<https://arxiv.org/abs/2410.21845>) · 2024 · [ⓘ](../catalog.md#paper-luo2024hilserl) ⌂

<a id="sec-9-5"></a>

## 9.5 Latency and Memory

*Representative works (Figure 2):* control deadlines, long horizons

- Scaling up test-time compute with latent reasoning: A recurrent depth approach · NeurIPS 2026 · [ⓘ](../catalog.md#paper-geiping2025recurrentdepth)
- [Looped world models](<https://arxiv.org/abs/2606.18208>) · arXiv 2026 · [ⓘ](../catalog.md#paper-lu2026loopwm)
- [Two-Scale Latent Dynamics for Recurrent-Depth Transformers](<https://arxiv.org/abs/2509.23314>) · 2025 · [ⓘ](../catalog.md#paper-pappone2025twoscale) ⌂
- **WorldMem**: [Long-term Consistent World Simulation with Memory](<https://arxiv.org/abs/2504.12369>) · arXiv 2025 · [ⓘ](../catalog.md#paper-xiao2025worldmem) ⌂
- [Video World Models with Long-term Spatial Memory](<https://arxiv.org/abs/2506.05284>) · arXiv 2025 · [ⓘ](../catalog.md#paper-wu2025spatialmem) ⌂
- [Long-Context State-Space Video World Models](<https://arxiv.org/abs/2505.20171>) · arXiv 2025 · [ⓘ](../catalog.md#paper-po2025ssmwm) ⌂
- [DecMem: Towards Minute-Long Consistent World Generation with Decoupled Memory](<https://arxiv.org/abs/2605.31336>) · arXiv 2026 · [ⓘ](../catalog.md#paper-yang2026decmem) ⌂
- **PERSIST**: [Beyond Pixel Histories: World Models with Persistent 3D State](<https://arxiv.org/abs/2603.03482>) · arXiv 2026 · [ⓘ](../catalog.md#paper-garcin2026persist) ⌂
- [LIVE: Long-horizon Interactive Video World Modeling](<https://arxiv.org/abs/2602.03747>) · arXiv 2026 · [ⓘ](../catalog.md#paper-huang2026live) ⌂
- **Dreamer 4**: [Training Agents Inside of Scalable World Models](<https://arxiv.org/abs/2509.24527>) · arXiv 2025 · [ⓘ](../catalog.md#paper-hafner2025dreamer4) ⌂
- [Deep Hierarchical Planning from Pixels](<https://arxiv.org/abs/2206.04114>) · arXiv 2022 · [ⓘ](../catalog.md#paper-hafner2022director) ⌂
- [Hierarchical Planning with Latent World Models](<https://arxiv.org/abs/2604.03208>) · arXiv 2026 · [ⓘ](../catalog.md#paper-zhang2026hierarchical) ⌂

<a id="sec-9-6"></a>

## 9.6 Safety and Trust Calibration

*Representative works (Figure 2):* [latent safety filters](../catalog.md#paper-seo2025uncertainty), calibrated reliance

- **MBPO**: [When to Trust Your Model: Model-Based Policy Optimization](<https://arxiv.org/abs/1906.08253>) · NeurIPS 2019 · [ⓘ](../catalog.md#paper-janner2019mbpo)
- Can you trust your model's uncertainty? Evaluating predictive uncertainty under dataset shift · NeurIPS 2019 · [ⓘ](../catalog.md#paper-ovadia2019can) ⌂
- The safety filter: A unified view of safety-critical control in autonomous systems · Annual Review of Control, Robotics, and Autonomous Systems 2024 · [ⓘ](../catalog.md#paper-hsu2024safety) ⌂
- Data-driven safety filters: Hamilton-Jacobi reachability, control barrier functions, and predictive methods for uncertain systems · IEEE Control Systems Magazine 2023 · [ⓘ](../catalog.md#paper-wabersich2023data) ⌂
- Hamilton-Jacobi reachability: A brief overview and recent advances · CDC 2017 · [ⓘ](../catalog.md#paper-bansal2017hamilton) ⌂
- [Control Barrier Functions: Theory and Applications](<https://doi.org/10.23919/ECC.2019.8796030>) · ECC 2019 · [ⓘ](../catalog.md#paper-ames2019cbf) ⌂
- A predictive safety filter for learning-based control of constrained nonlinear dynamical systems · Automatica 2021 · [ⓘ](../catalog.md#paper-wabersich2021predictive) ⌂
- Generalizing safety beyond collision-avoidance via latent-space reachability analysis · RSS 2025 · [ⓘ](../catalog.md#paper-nakamura2025generalizing) ⌂
- Uncertainty-aware latent safety filters for avoiding out-of-distribution failures · CoRL 2025 · [ⓘ](../catalog.md#paper-seo2025uncertainty) ⌂
- AnySafe: Adapting latent safety filters at runtime via safety constraint parameterization in the latent space · ICRA 2026 · [ⓘ](../catalog.md#paper-agrawal2026anysafe) ⌂
- How to train your latent control barrier function: Smooth safety filtering under hard-to-model constraints · Learning for Dynamics and Control Conference 2026 · [ⓘ](../catalog.md#paper-nakamura2026train) ⌂
- Probabilistically safe robot planning with confidence-based human predictions · RSS 2018 · [ⓘ](../catalog.md#paper-fisac2018probabilistically) ⌂
- Confidence-aware motion prediction for real-time collision avoidance · The International Journal of Robotics Research 2020 · [ⓘ](../catalog.md#paper-fridovich2020confidence) ⌂
- **MOPO**: [Model-based Offline Policy Optimization](<https://proceedings.neurips.cc/paper_files/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf>) · NeurIPS 2020 · [ⓘ](../catalog.md#paper-mopo)
- Constrained policy optimization via Bayesian world models · ICLR 2022 · [ⓘ](../catalog.md#paper-as2022constrained) ⌂
- **SafeDreamer**: [Safe reinforcement learning with world models](<https://arxiv.org/abs/2307.07176>) · ICLR 2024 · [Code](<https://github.com/PKU-Alignment/SafeDreamer>) · [ⓘ](../catalog.md#paper-huang2024safedreamer)
- Closing the loop on runtime monitors with fallback-safe MPC · CDC 2023 · [ⓘ](../catalog.md#paper-sinha2023closing)
- Unpacking failure modes of generative policies: Runtime monitoring of consistency and progress · CoRL 2025 · [ⓘ](../catalog.md#paper-agia2025unpacking)
- Can we detect failures without failure data? Uncertainty-aware runtime failure detection for imitation learning policies · RSS 2025 · [ⓘ](../catalog.md#paper-xu2025can) ⌂
- Safe planning in dynamic environments using conformal prediction · RA-L 2023 · [ⓘ](../catalog.md#paper-lindemann2023safe) ⌂
- Conformal decision theory: Safe autonomous decisions from imperfect predictions · ICRA 2024 · [ⓘ](../catalog.md#paper-lekeufack2024conformal) ⌂
- Humans and automation: Use, misuse, disuse, abuse · Human Factors 1997 · [ⓘ](../catalog.md#paper-parasuraman1997humans) ⌂
- [Trust in Automation: Designing for Appropriate Reliance](<https://doi.org/10.1518/hfes.46.1.50_30392>) · Human Factors 2004 · [ⓘ](../catalog.md#paper-leesee2004trust) ⌂
- “Dave... I can assure you... that it's going to be all right...” A definition, case for, and survey of algorithmic assurances in human-autonomy trust relationships · CSUR 2019 · [ⓘ](../catalog.md#paper-israelsen2019dave) ⌂
- A survey of algorithmic methods for competency self-assessments in human-autonomy teaming · ACM Computing Surveys 2024 · [ⓘ](../catalog.md#paper-conlon2024survey) ⌂
- Introspective Perception: Learning to Predict Failures in Vision Systems · IROS 2016 · [ⓘ](../catalog.md#paper-daftry2016introspective) ⌂
- Learn from experience: Probabilistic prediction of perception performance to avoid failure · The International Journal of Robotics Research 2018 · [ⓘ](../catalog.md#paper-gurau2018learn) ⌂
- Trust-aware decision making for human-robot collaboration: Model learning and planning · THRI 2020 · [ⓘ](../catalog.md#paper-chen2020trust) ⌂
- Trust calibration within a human-robot team: Comparing automatically generated explanations · HRI 2016 · [ⓘ](../catalog.md#paper-wang2016trust) ⌂
- Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making · Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency 2020 · [ⓘ](../catalog.md#paper-zhang2020effect) ⌂
- **KnowNo**: [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](<https://proceedings.mlr.press/v229/ren23a.html>) · CoRL 2023 · [ⓘ](../catalog.md#paper-ren2023knowno)
- Introspective planning: Aligning robots' uncertainty with inherent task ambiguity · NeurIPS 2024 · [ⓘ](../catalog.md#paper-liang2024introspective) ⌂
- [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](<https://arxiv.org/abs/2602.22474>) · RSS 2026 · [ⓘ](../catalog.md#paper-yuan2026act) ⌂
- Robots that suggest safe alternatives · IROS 2025 · [ⓘ](../catalog.md#paper-jeong2025robots) ⌂
- Objective Mismatch in Model-based Reinforcement Learning · Proceedings of the 2nd Conference on Learning for Dynamics and Control 2020 · [ⓘ](../catalog.md#paper-lambert2020objective)
- Representing autonomous systems' self-confidence through competency boundaries · Proceedings of the Human Factors and Ergonomics Society Annual Meeting 2015 · [ⓘ](../catalog.md#paper-hutchins2015representing) ⌂
- Not all errors are made equal: A regret metric for detecting system-level trajectory prediction failures · CoRL 2025 · [ⓘ](../catalog.md#paper-nakamura2025not) ⌂
- Updating robot safety representations online from natural language feedback · ICRA 2025 · [ⓘ](../catalog.md#paper-santos2025updating) ⌂
- Adaptive conformal prediction for motion planning among dynamic agents · Learning for Dynamics and Control Conference 2023 · [ⓘ](../catalog.md#paper-dixit2023adaptive) ⌂
- Updates in human-AI teams: Understanding and addressing the performance/compatibility tradeoff · AAAI 2019 · [ⓘ](../catalog.md#paper-bansal2019updates) ⌂
- Verification of neural reachable tubes via scenario optimization and conformal prediction · Learning for Dynamics and Control Conference 2024 · [ⓘ](../catalog.md#paper-lin2024verification) ⌂
- Plate: Visually-grounded planning with transformers in procedural tasks · RA-L 2022 · [ⓘ](../catalog.md#paper-sun2022plate) ⌂
- Adversarial inverse reinforcement learning with self-attention dynamics model · RA-L 2021 · [ⓘ](../catalog.md#paper-sun2021adversarial) ⌂
- The politics of autonomous vehicles · Humanities and Social Sciences Communications 2022 · [ⓘ](../catalog.md#paper-stilgoe2022politics) ⌂
- [Guidelines and Recommendations for ADS Safety Requirements, Assessments and Test Methods to Inform Regulatory Development](<https://unece.org/transport/publications/guidelines-and-recommendations-ads-safety-requirements-assessments-and-test>) · 2025 · [ⓘ](../catalog.md#paper-unece2025ads) ⌂
- When physicians and AI work together, who is accountable? How to lay out medical liability · Nature 2026 · [ⓘ](../catalog.md#paper-lam2026physicians) ⌂
- World models: The safety perspective · ISSREW 2024 · [ⓘ](../catalog.md#paper-zeng2024world) ⌂
- **World-model risk survey**: [Safety, Security, and Cognitive Risks in World Models](<https://arxiv.org/abs/2604.01346>) · 2026 · [ⓘ](../catalog.md#paper-worldmodelrisks2026)
- [Emerging cyber attack risks of medical ai agents](<https://arxiv.org/abs/2504.03759>) · arXiv 2025 · [ⓘ](../catalog.md#paper-qiu2025emerging) ⌂
- [Clawsbench: Evaluating capability and safety of llm productivity agents in simulated workspaces](<https://arxiv.org/abs/2604.05172>) · arXiv 2026 · [ⓘ](../catalog.md#paper-li2026clawsbench) ⌂

<a id="sec-9-7"></a>

## 9.7 Closed and Auditable Systems

*Representative works (Figure 2):* [Gemini Robotics](../catalog.md#paper-team2025gemini), [Helix](../catalog.md#paper-figure2025helix), [1X world model](../catalog.md#paper-ho2025-1xworldmodel)

- **Gemini Robotics**: [Bringing ai into the physical world](<https://arxiv.org/abs/2503.20020>) · arXiv 2025 · [ⓘ](../catalog.md#paper-team2025gemini) ⌂
- [Gemini robotics 1.5: Pushing the frontier of generalist robots with advanced embodied reasoning, thinking, and motion transfer](<https://arxiv.org/abs/2510.03342>) · arXiv 2025 · [ⓘ](../catalog.md#paper-team2025gemini15) ⌂
- **Helix**: [A Vision-Language-Action Model for Generalist Humanoid Control](<https://www.figure.ai/news/helix>) · 2025 · [ⓘ](../catalog.md#paper-figure2025helix) ⌂
- [Introducing Helix 02: Full-Body Autonomy](<https://www.figure.ai/news/helix-02>) · 2026 · [ⓘ](../catalog.md#paper-figure2026helix02) ⌂
- [Building the General-Purpose Robotic Brain](<https://skild.ai/blogs/building-the-general-purpose-robotic-brain>) · 2025 · [ⓘ](../catalog.md#paper-skild2025brain) ⌂
- **1X world model**: [Evaluating Bits, not Atoms](<https://www.1x.tech/1x-world-model.pdf>) · 2025 · [ⓘ](../catalog.md#paper-ho2025-1xworldmodel) ⌂
- [1X World Model: From Video to Action—A New Way Robots Learn](<https://www.1x.tech/discover/world-model-self-learning>) · 2026 · [ⓘ](../catalog.md#paper-onex2026worldmodelpolicy) ⌂
- [Introducing RFM-1: Giving Robots Human-Like Reasoning Capabilities](<https://covariant.ai/insights/introducing-rfm-1-giving-robots-human-like-reasoning-capabilities/>) · 2024 · [ⓘ](../catalog.md#paper-sohn2024rfm1) ⌂
- [Field Foundation Models and Belief World Models for General Robot Intelligence](<https://www.fieldai.com/>) · 2026 · [ⓘ](../catalog.md#paper-fieldai2026ffm) ⌂
- **Cosmos**: [Cosmos world foundation model platform for physical ai](<https://arxiv.org/abs/2501.03575>) · arXiv 2025 · [ⓘ](../catalog.md#paper-nvidia2025cosmos)
- **GR00T**: [Gr00t n1: An open foundation model for generalist humanoid robots](<https://arxiv.org/abs/2503.14734>) · arXiv 2025 · [ⓘ](../catalog.md#paper-nvidia2025groot)
- [Towards Safe Robot Foundation Models](<https://arxiv.org/abs/2503.07404>) · 2025 · [ⓘ](../catalog.md#paper-saferobotfoundation2025)
- **WorldEval**: [World Model as Real-World Robot Policies Evaluator](<https://arxiv.org/abs/2505.19017>) · arXiv 2025 · [ⓘ](../catalog.md#paper-worldeval2025)
- [Deep Reinforcement Learning from Human Preferences](<https://proceedings.neurips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html>) · NeurIPS 2017 · [ⓘ](../catalog.md#paper-christiano2017preferences)
- **REFLECT**: [Summarizing robot experiences for failure explanation and correction](<https://arxiv.org/abs/2306.15724>) · arXiv 2023 · [ⓘ](../catalog.md#paper-liu2023reflect)
- **VLAW**: [Iterative Co-Improvement of Vision-Language-Action Policy and World Model](<https://arxiv.org/abs/2602.12063>) · arXiv 2026 · [ⓘ](../catalog.md#paper-vlaw2026)
- **WorldSample**: [Closed-loop Real-robot RL with World Modelling](<https://arxiv.org/abs/2607.02431>) · arXiv 2026 · [ⓘ](../catalog.md#paper-xue2026worldsample)
- **VT-WM**: [Visuo-Tactile World Models](<https://arxiv.org/abs/2602.06001>) · 2026 · [ⓘ](../catalog.md#paper-visuotactilewm2026)
- **OmniVTA**: [Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](<https://arxiv.org/abs/2603.19201>) · 2026 · [ⓘ](../catalog.md#paper-omnivta2026)

