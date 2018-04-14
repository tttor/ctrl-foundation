# Deterministic Policy Gradient Algorithms
* David Silver et al

## problem
* computing the stochastic policy gradient may require more samples, especially if the action space has many dimensions.

## idea: deterministic policy gradients
* vs stochastic case
  * In the stochastic case: the policy gradient integrates over both state and action spaces, 
  * in the deterministic case: it only integrates over the state space.
* to choose actions according to a stochastic behaviour policy (to ensure adequate exploration), but 
  to learn about a deterministic target policy (exploiting the ef- ficiency of the deterministic policy gradient)
* use the deterministic policy gradient to derive an off-policy actor-critic algorithm that 
  estimates the action-value function using a differentiable function approximator, and 
  then updates the policy parameters in the direction of the approximate action-value gradient. 
* introduce a notion of **compatible function approximation** for deterministic policy gradients, 
  to ensure that the approximation does not bias the policy gradient.

## setup
* task
  * bandit with 50 continuous action dimensions
  * a high-dimensional task for controlling an octopus arm

## result
* show that the deterministic policy gradient does indeed exist, and 
  it has a simple model-free form that simply follows the gradient of the action-value function
* the deterministic policy gradient can be **estimated much more efficiently** than the usual stochastic policy gradient.
* our algorithms require no more computation than prior methods: 
  the computational cost of each update is linear in the action dimensionality and the number of policy parameters

## misc
* Policy gradient algorithms typically proceed by sampling this stochastic policy and 
  adjusting the policy parameters in the direction of greater cumulative reward.
  
