# Bridging the Gap Between Value and Policy Based Reinforcement Learning
* Ofir Nachum1 Mohammad Norouzi Kelvin Xu1 Dale Schuurmans
* nips2017: poster
* https://arxiv.org/abs/1702.08892
* https://media.nips.cc/nipsbooks/nipspapers/paper_files/nips30/reviews/1564.html

## problem
* the intricacies of actor and critic perspectives are exacerbated by deep models.
* off-policy learning under function approximation 
  * remain potentially unstable and 
  * require specialized algorithmic and theoretical development as well as delicate tuning to be effective in practice

## observation
* for the softmax value function `V^*` in (8), 
  the quantity `exp{V^*(s)/ \tau}` also serves as the normalization factor of the optimal policy `\pi^*∗(a|s)` in (7)
  
## idea: Unified Path Consistency Learning (Unified PCL)
* connection between value and policy based RL based on a relationship between 
  * softmax temporal value consistency and 
  * policy optimality under entropy regularization.
* exploit a relationship between 
  * policy optimization under entropy regularization and 
  * softmax value consistency to obtain a new form of stable off-policy learning.
* PCL
  * minimizes a notion of soft consistency error along multi-step action sequences extracted from 
    both on- and off-policy traces
  * can be interpreted as generalizing both actor-critic and Q-learning algorithms.
  * resembles actor-critic in that it maintains and jointly learns a model of the state values and a model of the policy, and 
  * is similar to Q-learning in that it minimizes a measure of temporal consistency error
  * the multi-step path-wise consistencies which allow the resulting algorithms to 
    utilize multi-step trajectories from off-policy samples in addition to on-policy samples
  * easily amenable to incorporate expert trajectories
* Unified PCL 
  * which maintains a single model for both the policy and the values
  * optimizes the same objective as PCL but differs by combining the policy and value function into a single model.
  * Merging the policy and value function models in this way is significant because 
    * it presents a new actor-critic paradigm where the policy (actor) is **not distinct** from the values (critic).
    * in practice, beneficial to apply updates to `\rho` from `V_{\rho}` and `\pi_{\rho}` using **different learning rates**

## setup
* compare to: 
  * A3C
  * DQN with double Q-learning
* experiment with seeding the replay buffer with 10 randomly sampled expert trajectories
* average reward across 5 random training runs (10 for Synthetic Tree) after choosing best hyperparameters.
* task: tasks such as Copy, Reverse, and RepeatCopy

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
  
## background
* Actor-critic methods have thus become popular [39, 40, 42], because 
  they use value approximators to replace rollout estimates and reduce variance, at the cost of some bias.
* one-hot distribution that assigns a probability of 1 to an action with maximal return and 0 elsewhere  
* **Entropy regularization** encourages exploration and helps prevent early convergence to sub-optimal policies,

## comment
* the idea of merging actor and critic models roughly similar to 
  use the same network (shared params) for both actor and critic
  * unexpectedly, the authors suggest using diff learning rate to updates `\rho` from `V_{\rho}` and `\pi_{\rho}` in practice
* why use uncommon tasks: Copy, Reverse, and RepeatCopy?
