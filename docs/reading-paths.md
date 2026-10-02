# Reading paths

[Home](../README.md) · [All annotations](methods.md) · [Full catalog](catalog.md)

Each route joins the paper’s argument, concrete interfaces and the tests needed to assess them. The sequences are reading suggestions, not performance rankings.

## Establish the loop

Read [the learning-loop view](chapters/03-foundations.md), [functional roles](chapters/04-roles.md) and [evaluation](chapters/11-evaluation.md).

Then compare [PlaNet](methods.md#paper-hafner2019planet), [Dreamer](methods.md#paper-hafner2019dreamer) and [DayDreamer](methods.md#paper-wu2022daydreamer). Track which consumer selects actions, which learner is updated and whether prediction runs during deployment.

## Plan robot actions

Start with [representations and mechanics](chapters/05-representations.md), then [embodiment constraints](chapters/10-embodiments.md).

Compare [DINO-WM](methods.md#paper-zhou2025dinowm), [V-JEPA 2](methods.md#paper-assran2025vjepa2), [PointWorld](methods.md#paper-pointworld2026) and [WorldPlanner](methods.md#paper-worldplanner2025). Inspect the action-query interface, plan horizon, full decision latency and actual execution feedback. Retain PointWorld’s open-loop physical execution boundary.

## Model touch and contact

Read [tactile and contact world models](chapters/08-tactile-contact.md).

Follow [Manipulation by Feel](methods.md#paper-tian2019manipulation), [RoboPack](methods.md#paper-ai2024robopack), [Visuo-Tactile World Models](methods.md#paper-visuotactilewm2026), [OmniVTA](methods.md#paper-omnivta2026) and [DexTacWAM](methods.md#paper-yuan2026dextacwam). Compare hidden contact state, predictive touch and direct sensor conditioning. Use [Sparsh](methods.md#paper-higuera2024sparsh) as a representation-prior contrast and [OmniVTLA](methods.md#paper-cheng2025omnivtla) as policy context.

## Ground human and egocentric data

Read [human and egocentric data](chapters/09-human-egocentric.md).

Compare [Gen2Act](methods.md#paper-bharadhwaj2025gen2act), [DreamDojo](methods.md#paper-gao2026dreamdojo), [EgoWAM](methods.md#paper-egowam2026) and [AnyWorld](methods.md#paper-chen2026anyworld). For deployment adaptation, contrast [Zero-WAM](methods.md#paper-zhou2026zerowam) with [WAM-TTT](methods.md#paper-feng2026wamttt). Track visual/sensing, kinematic, contact/dynamics and action-label gaps separately.

## Learn or evaluate in neural simulation

Read [foundation priors and neural simulation](chapters/07-foundation-priors.md), then [resources](chapters/12-resources.md).

Compare [RWM](methods.md#paper-li2025roboticworldmodel), [IWS](methods.md#paper-interactiveworldsim2026), [Hi-WM](methods.md#paper-li2026hiwm), [GE-Sim 2.0](methods.md#paper-qiu2026gesim2), [DreamGen](methods.md#paper-jang2025dreamgen) and [WoVR](methods.md#paper-nsim-wovr). Keep demonstrations, filtered BC and RL distinct. Contrast those learning routes with evaluation-only evidence from [RoboWorld](methods.md#paper-nsim-roboworld) and [WorldEval](methods.md#paper-li2025worldeval).

## Understand the outer loop

Read [interaction to model improvement](chapters/14-interaction-learning.md).

Compare [VLAW](methods.md#paper-vlaw2026), [VLA-RFT](methods.md#paper-vlarft2025), [WAM-RL](methods.md#paper-wamrl2026), [WorldSample](methods.md#paper-xue2026worldsample), [Sirius-Fleet](methods.md#paper-liu2025siriusfleet) and [REGEN](methods.md#paper-govind2026regen). Write down the separate model and policy objectives, frozen components, intervention policy, transition provenance and retention tests.

## Choose an evaluation protocol

Read [evaluation](chapters/11-evaluation.md) and use the [worksheet](evaluation.md).

Compare [EWMBench](methods.md#paper-yue2025ewmbench), [WorldArena](methods.md#paper-shang2026worldarena) and [World-in-World](methods.md#paper-worldinworld2025). Match a protocol to the claim: perceptual prediction, action consequences, downstream utility or deployment reliability. Then select an appropriate [upstream environment or dataset](resources.md). There is no pooled success-rate leaderboard across different robots, task distributions and budgets.
