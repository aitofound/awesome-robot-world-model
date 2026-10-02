# Browse by functional role

[Home](../README.md) · [Scope and taxonomy](scope-and-taxonomy.md)

A system can appear in several roles. The entry kind and evidence boundary qualify each placement.

<a id="role-representation"></a>

## Representation

Learn task-relevant state or predictive features used by a downstream policy.

| Entry | Kind | Consumer and change |
|---|---|---|
| [World Models](methods.md#paper-ha2018worldmodels) | `world-model-use` | A controller consumes the learned state and predictive environment. |
| [DreamerV2](methods.md#paper-hafner2021dreamerv2) | `world-model-use` | Imagination updates the actor and value function. |
| [DINO-WM](methods.md#paper-zhou2025dinowm) | `world-model-use` | Planning consumes predicted features to select controls. |
| [V-JEPA 2](methods.md#paper-assran2025vjepa2) | `world-model-use` | A planning consumer connects predictions to robotic decisions. |
| [ACT-JEPA](methods.md#paper-actjepa2025) | `representation-prior` | Representation learning affects downstream policy learning. |
| [Causal-JEPA](methods.md#paper-nam2026causaljepa) | `representation-prior` | Downstream uses consume object-aware predictive representations. |
| [Cosmos](methods.md#paper-nvidia2025cosmos) | `generative-context` | Robot-specific adaptation can consume these priors. |
| [Cosmos 3](methods.md#paper-nvidia2026cosmos3) | `generative-context` | Downstream embodied systems can adapt the learned priors. |
| [RoboPack](methods.md#paper-ai2024robopack) | `world-model-use` | Predicted contact dynamics support dense-packing decisions. |
| [VIRDO++](methods.md#paper-wi2022virdopp) | `world-model-use` | Predictive perception provides deformable-state estimates. |
| [ContactWorld](methods.md#paper-zhang2026contactworld) | `world-model-use` | Contact-aware representations support manipulation-facing predictions. |
| [Sparsh](methods.md#paper-higuera2024sparsh) | `representation-prior` | Downstream sensing and policy systems consume the features. |
| [AnyTouch](methods.md#paper-feng2025anytouch) | `representation-prior` | Downstream systems reuse tactile features. |
| [OmniVTLA](methods.md#paper-cheng2025omnivtla) | `policy-context` | The learned policy predicts actions. |
| [TactAlign](methods.md#paper-tactalign2026) | `policy-context` | The transferred policy uses contact-related information. |
| [EgoZero](methods.md#paper-egozero2025) | `policy-context` | The robot policy is trained using grounded human-derived supervision. |
| [OpenVLA](methods.md#paper-openvla2024) | `policy-context` | It supplies a policy baseline or consumer for world-model training and evaluation. |
| [pi0](methods.md#paper-pi0) | `policy-context` | It supplies an action policy or downstream world-model consumer. |
| [GR00T N1.7](methods.md#paper-nvidia2026groot17) | `policy-context` | Downstream embodied systems consume its policy interface. |

<a id="role-prediction"></a>

## Prediction and imagination

Predict consequences or futures for a decision or learning consumer.

| Entry | Kind | Consumer and change |
|---|---|---|
| [World Models](methods.md#paper-ha2018worldmodels) | `world-model-use` | A controller consumes the learned state and predictive environment. |
| [PlaNet](methods.md#paper-hafner2019planet) | `world-model-use` | Online planning selects actions through imagined latent trajectories. |
| [Dreamer](methods.md#paper-hafner2019dreamer) | `world-model-use` | Actor and value learning use imagination; the deployed actor can act without an explicit rollout planner. |
| [DreamerV2](methods.md#paper-hafner2021dreamerv2) | `world-model-use` | Imagination updates the actor and value function. |
| [DreamerV3](methods.md#paper-hafner2023dreamerv3) | `world-model-use` | Model-generated trajectories train behavior and value estimates. |
| [Dreamer4](methods.md#paper-hafner2025dreamer4) | `world-model-use` | Policies learn inside a predictive environment. |
| [DayDreamer](methods.md#paper-wu2022daydreamer) | `world-model-use` | Imagined experience supports robot policy learning. |
| [TD-MPC2](methods.md#paper-hansen2024tdmpc2) | `world-model-use` | Model-predictive control selects actions. |
| [DINO-WM](methods.md#paper-zhou2025dinowm) | `world-model-use` | Planning consumes predicted features to select controls. |
| [V-JEPA 2](methods.md#paper-assran2025vjepa2) | `world-model-use` | A planning consumer connects predictions to robotic decisions. |
| [ACT-JEPA](methods.md#paper-actjepa2025) | `representation-prior` | Representation learning affects downstream policy learning. |
| [Causal-JEPA](methods.md#paper-nam2026causaljepa) | `representation-prior` | Downstream uses consume object-aware predictive representations. |
| [ODEWorld](methods.md#paper-liu2026odeworld) | `generative-context` | The interface predicts futures at physical-time queries. |
| [PointWorld](methods.md#paper-pointworld2026) | `world-model-use` | MPPI planning produces robot action sequences. |
| [PhysTwin](methods.md#paper-jiang2025phystwin) | `world-model-use` | The reconstructed simulation supports interaction reasoning. |
| [WorldPlanner](methods.md#paper-worldplanner2025) | `world-model-use` | Global Monte Carlo tree search and local MPC choose actions. |
| [Large Video Planner](methods.md#paper-chen2025largevideoplanner) | `world-model-use` | Retargeting produces actions for physical execution. |
| [RoboDreamer](methods.md#paper-robodreamer2024) | `world-model-use` | Predicted futures provide a task-facing imagination interface. |
| [Robotic World Model (RWM)](methods.md#paper-li2025roboticworldmodel) | `world-model-use` | MBPO-PPO optimizes policies using model-generated experience. |
| [Interactive World Simulator (IWS)](methods.md#paper-interactiveworldsim2026) | `world-model-use` | Generated demonstrations train downstream robot policies. |
| [GE-Sim 2.0](methods.md#paper-qiu2026gesim2) | `world-model-use` | Successful-rollout filtering supplies behavior-cloning updates. |
| [GeniWorld](methods.md#paper-gu2026geniworld) | `world-model-use` | Synthetic condition augmentation supports policy improvement. |
| [DreamGen](methods.md#paper-jang2025dreamgen) | `world-model-use` | Synthetic demonstrations supply policy-training supervision. |
| [DreamDojo](methods.md#paper-gao2026dreamdojo) | `world-model-use` | Adapted world-model rollouts support robot-facing uses. |
| [WoVR](methods.md#paper-nsim-wovr) | `world-model-use` | RL post-trains VLA policies in the predictive simulator. |
| [RoboWorld](methods.md#paper-nsim-roboworld) | `world-model-use` | Generated outcomes rank or assess policies. |
| [WorldEval](methods.md#paper-li2025worldeval) | `world-model-use` | Evaluation compares robot policy checkpoints. |
| [Cosmos](methods.md#paper-nvidia2025cosmos) | `generative-context` | Robot-specific adaptation can consume these priors. |
| [Cosmos 3](methods.md#paper-nvidia2026cosmos3) | `generative-context` | Downstream embodied systems can adapt the learned priors. |
| [Genie](methods.md#paper-bruce2024genie) | `generative-context` | Agents can consume an interactive generated environment. |
| [Manipulation by Feel](methods.md#paper-tian2019manipulation) | `world-model-use` | Model-predictive control uses touch predictions to choose actions. |
| [RoboPack](methods.md#paper-ai2024robopack) | `world-model-use` | Predicted contact dynamics support dense-packing decisions. |
| [VIRDO++](methods.md#paper-wi2022virdopp) | `world-model-use` | Predictive perception provides deformable-state estimates. |
| [ContactWorld](methods.md#paper-zhang2026contactworld) | `world-model-use` | Contact-aware representations support manipulation-facing predictions. |
| [OmniVTA](methods.md#paper-omnivta2026) | `world-model-use` | A reflex interface corrects actions during contact-rich manipulation. |
| [Visuo-Tactile World Models](methods.md#paper-visuotactilewm2026) | `world-model-use` | A planning interface produces contact-rich robot actions. |
| [DexTacWAM](methods.md#paper-yuan2026dextacwam) | `world-model-use` | Predictive tactile supervision influences dexterous manipulation policies. |
| [VTAM](methods.md#paper-yuan2026vtam) | `world-model-use` | The joint predictive-action interface supports physical interaction. |
| [VT-WAM](methods.md#paper-tian2026vtwam) | `world-model-use` | Action generation consumes multimodal predictive information. |
| [Dream-Tac](methods.md#paper-lou2026dreamtac) | `world-model-use` | The learned action interface supports manipulation. |
| [Tactile-WAM](methods.md#paper-wu2026tactilewam) | `world-model-use` | Touch-aware predictive-action features influence actions. |
| [EgoWAM](methods.md#paper-egowam2026) | `world-model-use` | A predictive-action learner transfers information to robot behavior. |
| [AnyWorld](methods.md#paper-chen2026anyworld) | `world-model-use` | Recomposition supplies missing training combinations for cross-embodiment use. |
| [Zero-WAM](methods.md#paper-zhou2026zerowam) | `world-model-use` | Context changes the predictions and generated actions. |
| [WAM-TTT](methods.md#paper-feng2026wamttt) | `world-model-use` | Test-time learning changes fast model weights. |
| [VLAW](methods.md#paper-vlaw2026) | `world-model-use` | Iterative model and policy improvement changes both learners through distinct updates. |
| [WorldSample](methods.md#paper-xue2026worldsample) | `world-model-use` | Online policy learning consumes real and selectively generated transitions. |
| [WAM-RL](methods.md#paper-wamrl2026) | `world-model-use` | Actor RL and world-model video SFT change different parameter sets. |
| [Model-Based Runtime Monitoring](methods.md#paper-liu2024runtime) | `world-model-use` | A monitor requests human intervention; later interaction supports learning. |
| [Sirius-Fleet](methods.md#paper-liu2025siriusfleet) | `world-model-use` | Monitoring and human assistance influence collection and policy improvement. |
| [Planning with Online World Models](methods.md#paper-liu2025onlinewm) | `world-model-use` | Feedback can change predictive parameters and later decisions. |
| [SafeDreamer](methods.md#paper-huang2024safedreamer) | `world-model-use` | World-model planning consumes task and safety information to choose actions. |

<a id="role-simulation"></a>

## Simulation and data generation

Supply reusable generated interaction, demonstrations or training trajectories.

| Entry | Kind | Consumer and change |
|---|---|---|
| [Dreamer](methods.md#paper-hafner2019dreamer) | `world-model-use` | Actor and value learning use imagination; the deployed actor can act without an explicit rollout planner. |
| [DreamerV2](methods.md#paper-hafner2021dreamerv2) | `world-model-use` | Imagination updates the actor and value function. |
| [DreamerV3](methods.md#paper-hafner2023dreamerv3) | `world-model-use` | Model-generated trajectories train behavior and value estimates. |
| [Dreamer4](methods.md#paper-hafner2025dreamer4) | `world-model-use` | Policies learn inside a predictive environment. |
| [DayDreamer](methods.md#paper-wu2022daydreamer) | `world-model-use` | Imagined experience supports robot policy learning. |
| [PhysTwin](methods.md#paper-jiang2025phystwin) | `world-model-use` | The reconstructed simulation supports interaction reasoning. |
| [Robotic World Model (RWM)](methods.md#paper-li2025roboticworldmodel) | `world-model-use` | MBPO-PPO optimizes policies using model-generated experience. |
| [Interactive World Simulator (IWS)](methods.md#paper-interactiveworldsim2026) | `world-model-use` | Generated demonstrations train downstream robot policies. |
| [Hi-WM](methods.md#paper-li2026hiwm) | `world-model-use` | Corrected trajectories support robot policy post-training. |
| [GE-Sim 2.0](methods.md#paper-qiu2026gesim2) | `world-model-use` | Successful-rollout filtering supplies behavior-cloning updates. |
| [GeniWorld](methods.md#paper-gu2026geniworld) | `world-model-use` | Synthetic condition augmentation supports policy improvement. |
| [DreamGen](methods.md#paper-jang2025dreamgen) | `world-model-use` | Synthetic demonstrations supply policy-training supervision. |
| [DreamDojo](methods.md#paper-gao2026dreamdojo) | `world-model-use` | Adapted world-model rollouts support robot-facing uses. |
| [WoVR](methods.md#paper-nsim-wovr) | `world-model-use` | RL post-trains VLA policies in the predictive simulator. |
| [VLA-RFT](methods.md#paper-vlarft2025) | `world-model-use` | GRPO updates the VLA policy while the world model is frozen. |
| [World-Gymnast](methods.md#paper-worldgymnast2026) | `world-model-use` | RL updates robot policies using generated task experience. |
| [Cosmos](methods.md#paper-nvidia2025cosmos) | `generative-context` | Robot-specific adaptation can consume these priors. |
| [Genie](methods.md#paper-bruce2024genie) | `generative-context` | Agents can consume an interactive generated environment. |
| [Gen2Act](methods.md#paper-bharadhwaj2025gen2act) | `world-model-use` | A robot-learning pipeline consumes generated behavior supervision. |
| [Dreamitate](methods.md#paper-liang2025dreamitate) | `world-model-use` | Generated supervision updates robot policies. |
| [AnyWorld](methods.md#paper-chen2026anyworld) | `world-model-use` | Recomposition supplies missing training combinations for cross-embodiment use. |
| [VLAW](methods.md#paper-vlaw2026) | `world-model-use` | Iterative model and policy improvement changes both learners through distinct updates. |
| [WorldSample](methods.md#paper-xue2026worldsample) | `world-model-use` | Online policy learning consumes real and selectively generated transitions. |
| [WAM-RL](methods.md#paper-wamrl2026) | `world-model-use` | Actor RL and world-model video SFT change different parameter sets. |
| [REGEN](methods.md#paper-govind2026regen) | `world-model-use` | Replayed experience supports policy retention as new tasks arrive. |

<a id="role-planning"></a>

## Planning and search

Compare candidate actions, plans or skills using model outputs.

| Entry | Kind | Consumer and change |
|---|---|---|
| [PlaNet](methods.md#paper-hafner2019planet) | `world-model-use` | Online planning selects actions through imagined latent trajectories. |
| [TD-MPC2](methods.md#paper-hansen2024tdmpc2) | `world-model-use` | Model-predictive control selects actions. |
| [DINO-WM](methods.md#paper-zhou2025dinowm) | `world-model-use` | Planning consumes predicted features to select controls. |
| [V-JEPA 2](methods.md#paper-assran2025vjepa2) | `world-model-use` | A planning consumer connects predictions to robotic decisions. |
| [PointWorld](methods.md#paper-pointworld2026) | `world-model-use` | MPPI planning produces robot action sequences. |
| [WorldPlanner](methods.md#paper-worldplanner2025) | `world-model-use` | Global Monte Carlo tree search and local MPC choose actions. |
| [Large Video Planner](methods.md#paper-chen2025largevideoplanner) | `world-model-use` | Retargeting produces actions for physical execution. |
| [Manipulation by Feel](methods.md#paper-tian2019manipulation) | `world-model-use` | Model-predictive control uses touch predictions to choose actions. |
| [RoboPack](methods.md#paper-ai2024robopack) | `world-model-use` | Predicted contact dynamics support dense-packing decisions. |
| [Visuo-Tactile World Models](methods.md#paper-visuotactilewm2026) | `world-model-use` | A planning interface produces contact-rich robot actions. |
| [Planning with Online World Models](methods.md#paper-liu2025onlinewm) | `world-model-use` | Feedback can change predictive parameters and later decisions. |
| [SafeDreamer](methods.md#paper-huang2024safedreamer) | `world-model-use` | World-model planning consumes task and safety information to choose actions. |

<a id="role-evaluation"></a>

## Evaluation, reward and safety

Judge outcomes, policies, rewards or constraints using model information.

| Entry | Kind | Consumer and change |
|---|---|---|
| [Interactive World Simulator (IWS)](methods.md#paper-interactiveworldsim2026) | `world-model-use` | Generated demonstrations train downstream robot policies. |
| [GE-Sim 2.0](methods.md#paper-qiu2026gesim2) | `world-model-use` | Successful-rollout filtering supplies behavior-cloning updates. |
| [WoVR](methods.md#paper-nsim-wovr) | `world-model-use` | RL post-trains VLA policies in the predictive simulator. |
| [RoboWorld](methods.md#paper-nsim-roboworld) | `world-model-use` | Generated outcomes rank or assess policies. |
| [WorldEval](methods.md#paper-li2025worldeval) | `world-model-use` | Evaluation compares robot policy checkpoints. |
| [VLA-RFT](methods.md#paper-vlarft2025) | `world-model-use` | GRPO updates the VLA policy while the world model is frozen. |
| [World-Gymnast](methods.md#paper-worldgymnast2026) | `world-model-use` | RL updates robot policies using generated task experience. |
| [WorldArena](methods.md#paper-shang2026worldarena) | `benchmark` | Evaluation protocols compare model behavior and decision utility. |
| [EWMBench](methods.md#paper-yue2025ewmbench) | `benchmark` | Quality tests assess predictive outputs. |
| [World-in-World](methods.md#paper-worldinworld2025) | `benchmark` | Online planning protocols assess generated environments. |
| [SafeDreamer](methods.md#paper-huang2024safedreamer) | `world-model-use` | World-model planning consumes task and safety information to choose actions. |

<a id="role-adaptation"></a>

## Adaptation and monitoring

Use feedback to correct behavior, update context, request help or improve models and policies.

| Entry | Kind | Consumer and change |
|---|---|---|
| [DayDreamer](methods.md#paper-wu2022daydreamer) | `world-model-use` | Imagined experience supports robot policy learning. |
| [Hi-WM](methods.md#paper-li2026hiwm) | `world-model-use` | Corrected trajectories support robot policy post-training. |
| [OmniVTA](methods.md#paper-omnivta2026) | `world-model-use` | A reflex interface corrects actions during contact-rich manipulation. |
| [MuSe](methods.md#paper-clark2026muse) | `policy-context` | Policy adaptation incorporates new sensory information. |
| [WAM-TTT](methods.md#paper-feng2026wamttt) | `world-model-use` | Test-time learning changes fast model weights. |
| [TactAlign](methods.md#paper-tactalign2026) | `policy-context` | The transferred policy uses contact-related information. |
| [VLAW](methods.md#paper-vlaw2026) | `world-model-use` | Iterative model and policy improvement changes both learners through distinct updates. |
| [WorldSample](methods.md#paper-xue2026worldsample) | `world-model-use` | Online policy learning consumes real and selectively generated transitions. |
| [WAM-RL](methods.md#paper-wamrl2026) | `world-model-use` | Actor RL and world-model video SFT change different parameter sets. |
| [Model-Based Runtime Monitoring](methods.md#paper-liu2024runtime) | `world-model-use` | A monitor requests human intervention; later interaction supports learning. |
| [Sirius-Fleet](methods.md#paper-liu2025siriusfleet) | `world-model-use` | Monitoring and human assistance influence collection and policy improvement. |
| [REGEN](methods.md#paper-govind2026regen) | `world-model-use` | Replayed experience supports policy retention as new tasks arrive. |
| [Planning with Online World Models](methods.md#paper-liu2025onlinewm) | `world-model-use` | Feedback can change predictive parameters and later decisions. |
