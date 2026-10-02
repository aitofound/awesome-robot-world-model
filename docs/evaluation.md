# Evaluate the interface and its utility

[Home](../README.md) · [Paper section 11](chapters/11-evaluation.md) · [Resources](resources.md)

This worksheet adapts the survey’s reporting distinctions. It is a comparison protocol, not a claim that the listed methods have all passed it.

## Describe the system before scoring it

| Field | Record |
|---|---|
| Predicted quantity | Observation, latent state, 3D state, contact variable, reward, constraint or outcome |
| Conditioning | Observation/history, queried action, goal, instruction, embodiment and controller metadata |
| Fitting objective | Prediction, representation, reconstruction or other training loss |
| Consumer | Planner, actor learner, demonstration learner, policy evaluator, monitor or safety filter |
| Changed object | Action sequence, policy weights, world-model weights, context, memory or physical parameters |
| Feedback | Real transitions, human corrections, task verification, synthetic trajectories; update timing |
| Scope | Robot, sensors, controller, tasks, initial states, horizons and policy families |
| Version | Paper/model/code version and released artifacts actually used |

## Separate four reporting layers

1. **Model behavior:** task-relevant predictive error, temporal consistency, contact and geometry validity, action-intervention sensitivity and uncertainty.
2. **Policy effect:** task success, return, sample efficiency or assistance reduction against a strong consumer baseline with matched budgets.
3. **Deployment behavior:** decision latency, failures, recovery, correction, retention and performance under the deployed query distribution.
4. **Evidence boundary:** tested platforms, task coverage, policy families, paper versions, uncertainty intervals and unsupported transfers.

Model quality, policy utility and deployment reliability should appear as distinct outcomes. Do not replace policy utility with video quality or hardware reliability with short rollout accuracy.

## Match the use to a discriminating test

| Use | Compare | Preserve the boundary |
|---|---|---|
| Planning | Same model/control budget with and without the predictive decision interface | Report candidate actions, search horizon, replanning cadence and full planner latency |
| Synthetic demonstration learning | Matched real data and policy-training budget, with and without generated valid supervision | Include model construction, generation, filtering and pseudo-action costs |
| Imagined policy optimization | Matched real interaction and compute, varying model-generated learning experience | Separate real/model transitions and test model exploitation under the learned policy |
| Policy evaluation | Generated versus independent physical outcomes on held-out policy families | Measure absolute calibration as well as ranking agreement |
| Tactile predictive control | Predictive touch versus direct tactile conditioning under matched sensors and policy capacity | Report contact timing, control rate and closed- versus open-loop execution |
| Adaptation and monitoring | Feedback destination, update cadence, interventions and old-task retention | Detection, human choice, policy update and model update are separate events |

## Report a complete cost budget

Separate shared pretraining from per-robot costs. Include real collection, model adaptation, inference, planning, judging, resets, rejected samples and policy optimization. An inference FPS figure is not the full control latency. Matched final dataset size is not matched total collection and model-building cost.

## Keep reliability claims testable

Model-to-real disagreement alone does not diagnose deliberate exploitation. Ranking correlation does not establish absolute success-probability calibration. A matched-budget utility curve or optimism-gap analysis is a proposed evaluation construct; it needs actual measurements before being reported as a result.

Evaluate feasible off-expert action queries, task-relevant history, held-out policy families and shifted conditions. Report the uncertainty in the outcomes rather than pooling incompatible success rates.

## Record failures and interventions

A useful failure record contains the observation/history, queried action, predicted consequence, actual outcome, consumer decision, intervention and update destination. Separate the **observed failure** from the **suspected cause**. Record the collection policy and whether human intervention censored the trajectory.

An unsuccessful outcome can provide valid dynamics information while its action remains an invalid imitation target. Evaluate both new-task improvement and retained behavior when replay or continual adaptation is used.
