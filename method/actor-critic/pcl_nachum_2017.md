# Bridging the Gap Between Value and Policy Based Reinforcement Learning
* Ofir Nachum1 Mohammad Norouzi Kelvin Xu1 Dale Schuurmans
* 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

## idea: Path Consistency Learning (PCL)
* connection between value and policy based reinforcement learning (RL) based on a relationship between 
  * softmax temporal value consistency and 
  * policy optimality under entropy regularization.
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
