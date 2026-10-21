# Minimum reporting checklist

[Home](../README.md)

Minimum reporting checklist for future robot world-model papers.

*Source: Appendix A.3.*

| Category | Report | Reason | Common omission |
|---|---|---|---|
| **Pathway** | what the model hands over, to which consumer, and when | determines the evidence standard | calling the whole system a world model without specifying the pathway |
| **Robot/task scope** | embodiments, sensors, action spaces, tasks, horizons | defines transfer and deployment boundaries | aggregate task counts without physical variables |
| **Training data** | real/sim/generated mixture, demonstrations, failures, human labels | reveals support and possible bias | no breakdown of generated vs. real data effect |
| **Optimization signal** | imitation loss, reward, value, calibration, uncertainty, intervention | links model learning to policy improvement | architecture described without update rule |
| **Query distribution** | demonstration, planner proposal, policy rollout, deployment shift | exposes where model accuracy matters | evaluating only random held-out trajectories |
| **Baselines** | policy-only, model-free, scripted reward, simulator-only, real-data-only | tests whether the world-model pathway adds value | comparing only to weaker architecture variants |
| **Metrics** | model quality, closed-loop utility, deployment reliability | prevents prediction quality from replacing utility | reporting success without safety or intervention cost |
| **Failure cases** | negative examples, uncertainty, recovery, suspected pathway failure | makes errors reusable and interpretable | only successful videos or averaged results |
| **Artifacts** | code, data, benchmark, model, videos, logs, or evidence label | calibrates reproducibility | unclear boundary between demos and evaluated trials |
