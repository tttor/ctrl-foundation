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
* Stochastic Policy Gradient Theorem:
  * reduces the computation of the performance gradient to a simple expectation;
    eg: by forming a sample-based estimate of this expectation.
  * One issue: how to estimate the action-value function `Q_{\pi}(s, a)`. 
    * simplest approach is to use a sample return, 
      which leads to a variant of the REINFORCE algorithm
* It is often useful **to estimate** the policy gradient **off-policy** from trajectories sampled from 
  a **distinct behaviour policy**, `\beta(a|s) \neq \pi_{\theta}(a|s)`. 
  * In an off-policy setting, the performance objective is typically modified to be 
    the **value function of the target policy**, averaged over the **state distribution of the behaviour policy**
  * leads to 
    * off-policy policy gradients, 
    * Off-Policy Actor-Critic (OffPAC) algorithm: 
      * uses a behaviour policy `\beta(a|s)` to generate trajectories
      * A critic estimates a state-value function, V v(s) ≈ V π(s), **off-policy** from these trajectories, 
        by gradient temporal-difference learning (Sutton et al., 2009). 
      * An actor updates the policy parameters `\theta`, also **off-policy** from these trajectories, 
        by stochastic gradient ascent of Equation 5.
      * Both the actor and the critic use an **importance sampling ratio** to 
        adjust for the fact that actions were selected according to `\pi` rather than `\beta`
        
