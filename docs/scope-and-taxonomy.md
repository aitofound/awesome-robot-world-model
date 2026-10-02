# Scope and taxonomy

[Home](../README.md) · [Functional roles](roles.md) · [Reading paths](reading-paths.md)

The Atlas follows the companion survey’s **Prediction-to-Control Gap**: plausible predictions must be connected to useful robot decisions or learning. It distinguishes the model’s fitting objective from its downstream use.

## The strict operational criterion

A strict closed-loop robot world-model case combines:

1. **Action-intervenable, interaction-consistent consequence prediction.** The model represents outcomes under queried actions, rather than merely proposing an action or generating an unconstrained video.
2. **Implemented decision or learning coupling.** A controller, planner, policy learner, evaluator or other consumer actually uses its outputs.
3. **Execution feedback and downstream evidence.** Report how interaction returns information to the system and which tested outcome supports the claimed use.

Learning-time and execution-time closure differ. An actor trained through latent imagination can deploy without running a planner. A planner can use a frozen model while updating its action choice. Neither fact, alone, establishes online model-parameter learning.

## Entry kinds

| Kind | Meaning in the Atlas |
|---|---|
| `world-model-use` | A predictive use discussed in the survey. Read its consumer and boundary before deciding whether the strict criterion holds. |
| `representation-prior` | Features or predictive representation objectives used as components or context. |
| `policy-context` | Action policies, sensory adaptation or transfer baselines related to world-model consumers. |
| `generative-context` | General predictive or generative priors whose robot action grounding and utility need separate evidence. |
| `benchmark` | An evaluation protocol or interface, rather than a model method. |

The complete citation catalog is broader than the strict criterion. It preserves the paper’s background, competing methods and resource literature. **Being cited is not being certified as a closed-loop world model.**

## Keep classification axes separate

| Axis | Examples | Question answered |
|---|---|---|
| Functional role | Representation; prediction; simulation; planning; evaluation; adaptation | What does the model contribute to the loop? |
| Representation substrate | Pixel/video; predictive latent; 3D/object; structured physics; causal | Which task-relevant state is represented? |
| Modeling mechanics | RSSM; autoregression; diffusion; flow; physical-time ODE | How are predictive computations performed? |
| Learning regime | Imitation; offline RL; online model-based RL; planning; transfer | How does the consumer use experience or predictions? |
| Embodiment and task | Manipulation; navigation; humanoids; driving; cross-robot control | Which physical and informational constraints matter? |
| Evidence scope | Model behavior; policy effect; deployment behavior; stated boundary | Which claim is actually supported? |

Roles can overlap. Architectures and modalities do not determine a role. A video model can generate demonstrations, provide a search interface or evaluate a policy; those uses require different evidence.

## Feedback destinations

Record the object changed by feedback: observation context, action selection, policy memory, physical parameters, neural world-model weights, policy weights or collection strategy. Keep the destination and its update cadence explicit.

An observed failed transition can be valid dynamics supervision while its action is an unsuitable behavior-cloning target. A model-free policy trained with world-model-generated data can still be a world-model consumer at learning time.

## Resource capability profiles

The paper distinguishes **Model**, **Decision**, **Learning** and **Deployment** interfaces. These capabilities are non-nested. A static trajectory dataset may support model fitting but cannot independently test branching decisions or physical deployment. A predictive evaluation harness may compare policies without providing a policy optimizer.

Check released interfaces and required metadata directly. Avoid deriving a capability profile from a paper title, source prestige or a single repository link.
