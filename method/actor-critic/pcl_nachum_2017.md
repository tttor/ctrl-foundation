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

## idea: Path Consistency Learning (PCL)
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
    
## misc
* Actor-critic methods have thus become popular [39, 40, 42], because 
  they use value approximators to replace rollout estimates and reduce variance, at the cost of some bias.
  
