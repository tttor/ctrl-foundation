# Bridging the Gap Between Value and Policy Based Reinforcement Learning
* Ofir Nachum1 Mohammad Norouzi Kelvin Xu1 Dale Schuurmans
* 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.
* https://arxiv.org/abs/1702.08892

## problem
* how best to combine the advantages of value and policy based RL approaches in 
  the presence of deep function approximators, while mitigating their shortcomings
  * this issue is not yet settled, and 
  * the intricacies of each perspective are exacerbated by deep models.
* off-policy learning under function approximation remain potentially unstable and 
 require specialized algorithmic and theoretical development as well as delicate tuning to be effective in practice

## observation
* for the softmax value function `V^*` in (8), 
  the quantity `exp{V^*(s)/ \tau}` also serves as the normalization factor of the optimal policy `\pi^*∗(a|s)` in (7)
  
## idea: Unified Path Consistency Learning (Unifie PCL)
* connection between value and policy based reinforcement learning (RL) based on a relationship between 
  * softmax temporal value consistency and 
  * policy optimality under entropy regularization.
* exploit a relationship between 
  * policy optimization under entropy regularization and 
  * softmax value consistency to obtain a new form of stable off-policy learning.
* PCL
  * minimizes a notion of soft consistency error along multi-step action sequences extracted from both on- and off-policy traces
  * can be interpreted as generalizing both actor-critic and Q-learning algorithms.
  * resembles actor-critic in that it maintains and jointly learns a model of the state values and a model of the policy, and 
  * is similar to Q-learning in that it minimizes a measure of temporal consistency error
* Unified PCL 
  * which maintains a single model for both the policy and the values
  * optimizes the same objective as PCL but differs by combining the policy and value function into a single model.
  * Merging the policy and value function models in this way is significant because 
    * it presents a new actor-critic paradigm where the policy (actor) is **not distinct** from the values (critic).
    * in practice, beneficial to apply updates to `\rho` from `V_{\rho}` and `\pi_{\rho}` using **different learning rates**
    
## result
* softmax consistent action values correspond to optimal entropy regularized policy probabilities along 
  any action sequence, regardless of provenance. 
* PCL significantly outperforms strong actor-critic and Q-learning baselines across several benchmarks
* contrib:
  * identify a strong form of path consistency that relates optimal policy probabilities under entropy regularization to
    softmax consistent state values for any action sequence; 
  * use this result to formulate a novel optimization objective that allows for a stable form of 
    off-policy actor-critic learning; 
  * observe that under this objective the actor and critic can be unified in a single model that 
    coherently fulfills both roles.
* it is **not necessary** to have a **separate** actor and critic; the actor itself can serve as its own critic.
* PCL generalizes
  * Q-learning:
    the notion of temporal consistency proposed in this paper as a sound generalization of 
    the one-step temporal consistency given by hard-max Q-values.
  * A2C:
    takes PCL with `\tau \rightarrow 0` and omits the replay buffer
  
## misc
* Actor-critic methods have thus become popular [39, 40, 42], because 
  they use value approximators to replace rollout estimates and reduce variance, at the cost of some bias.
* one-hot distribution that assigns a probability of 1 to an action with maximal return and 0 elsewhere  
* **Entropy regularization** encourages exploration and helps prevent early convergence to sub-optimal policies,

## comment
* the idea of merging actor and critic models roughly similar to 
  use the same network (shared params) for both actor and critic
  * unexpectedly, the authors suggest using diff learning rate to updates `\rho` from `V_{\rho}` and `\pi_{\rho}` in practice
  
