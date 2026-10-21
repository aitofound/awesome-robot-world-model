# Glossary of loop terms

[Home](../README.md)

Glossary of loop terms used in the survey.

*Source: Appendix A.4.*

| Term | Meaning in this survey | Loop variable | Common ambiguity avoided |
|---|---|---|---|
| **World model** | learned model that predicts action-dependent future consequences (Section 2.2) | queryable rollout p<sub>θ</sub>(y<sub>t+1:t+H</sub>\| z<sub>t</sub>,a<sub>t:t+H-1</sub>) | not every large model is automatically a world model |
| **Prediction-to-Control Gap** | the observation that accurate predictions need not improve decisions | ΔJ in Eq. (1) | prediction metrics are not utility |
| **Consumer** | learner, policy, planner, evaluator or monitor that reads the model's output | queries Q and sensitivity ∂J/∂ŷ | model quality is relative to the consumer |
| **Design dial** | one of four questions that specify a world model, each with a trade-off | Y, C, D, M | routes are dial settings, not rival paradigms |
| **Prediction space (Y)** | what the model predicts, from pixels to task quantities | ŷ | not the same as the feature pathway |
| **Conditioning (C)** | what the prediction is conditioned on, from passive video to robot actions or joint generation | query interface | instruction conditioning is not action conditioning |
| **Knowledge source (D)** | where the model's knowledge comes from: web or human video, simulation, robot interaction | training and pretraining data | abundance is not action grounding |
| **Computation (M)** | how a prediction is computed and how long it takes | rollout mechanism, memory, latency | a slow model cannot serve a fast consumer |
| **Pathway** | what the model hands to its consumer; labels a use, not a paper | features, experience, scores, decisions, residuals | one system may use several pathways |
| **Features pathway** | prediction shapes the state a policy acts on | z<sub>t</sub> or predictive training loss | no rollout is needed at decision time |
| **Experience pathway** | generated trajectories or demonstrations serve as training data | D̂ | generated data must be judged by downstream transfer |
| **Scores pathway** | model returns reward, success, progress or cost estimates | r̂, Q̂, success score, cost | scores become optimization targets |
| **Decisions pathway** | predicted futures of candidate actions select the current action | action or subgoal ranking | plan visualization is not enough |
| **Residuals pathway** | difference between prediction and observation corrects behavior without parameter updates | e<sub>t</sub>=Δ(o<sub>t</sub>,ô<sub>t\| t-1</sub>) | correction is not adaptation of parameters |
| **Outer loop** | deployment data refit the model or the policy | update rule O<sub>WM</sub> in Eq. (4) | queries drift as the policy improves |
| **Closed-loop utility** | improvement in robot behavior caused by using the model in the loop | success, return, sample efficiency, safety, transfer | not the same as open-loop prediction quality |
| **Imagination** | use of predicted futures for planning, training, or evaluation | latent/video rollout | not necessarily photorealistic generation |
| **Neural simulator** | learned model used as an environment surrogate for policy training or evaluation | synthetic experience and policy ranking | stronger claim than open-loop prediction |
| **Monitor** | deployment component that tracks uncertainty, OOD state, contact mismatch, or predicted failure | intervention and fallback decisions | monitoring cost includes false positives |
| **Failure library** | structured record of predicted and real failed episodes | reusable negative data | failures should be categorized by pathway |
| **Query distribution** | states and actions on which the model is actually used by a consumer | planner proposals, policy rollouts, deployment shifts | random held-out test data may be insufficient |
| **Model exploitation** | planner or policy finds behavior that maximizes model score but fails in reality | optimized model errors | especially important for decisions and learned rewards |
| **Support constraint** | offline-RL or safety condition that limits out-of-distribution actions | feasible update region | uncertainty is useful only if it affects decisions |
| **Foundation prior** | pretrained knowledge that initializes representation, policy, prediction, critic, or simulator | initial state/action/world knowledge | foundation scale does not imply closed-loop evidence |
| **VLA policy** | vision-language-action model that maps context to robot actions | action prior and representation | a consumer of predictions; a world model only if it predicts action-dependent futures |
| **World foundation model** | large model trained to predict or simulate broad world dynamics | simulator/imagination prior | must still be grounded in robot control utility |
| **Tactile grounding** | use of touch/contact signals to improve prediction, planning, or correction | contact state and error signal | modality count is not the contribution |
| **Closed-loop utility** | measured improvement in learned or executed policy | success, return, data efficiency | distinct from model quality |
| **Deployment reliability** | behavior under real-world shift, failures, and interventions | safety, recovery, maintenance | success rate alone can hide unsafe execution |
| **Evidence boundary** | explicit statement of what a paper's evidence does not prove | claim calibration | especially needed for technical reports and demos |
| **Pathway-removal ablation** | experiment disabling or replacing a claimed world-model pathway | causal evidence for pathway utility | architecture ablations alone are insufficient |
| **Action-conditioned metric** | metric evaluated under candidate actions relevant to control | action ranking and outcome prediction | avoids passive prediction bias |
| **Generated-data ablation** | comparison of real-only, generated-only, and mixed training | data contribution | prevents synthetic data from being assumed helpful |
| **Calibration** | agreement between predicted confidence/scores and real outcomes | uncertainty, reward, risk | essential for scores and monitors |
| **Human correction** | intervention, preference, instruction, or repair signal from a person | reward/update/fallback signal | human input is part of the loop, not only annotation |
| **Auditable system** | system with inspectable pathways, evidence, failures, and fallback conditions | reproducibility and trust | important for closed-source frontier systems |
