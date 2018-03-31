# Natural Actor-Critic
* Jan Peters, Stefan Schaal
* Neurocomputing 71 (2008) 1180–1190
* https://www.sciencedirect.com/science/article/pii/S0925231208000532

## problem
* When applied with continuous function approximation, many algorithms based on value function approximation have 
  failed to generalize, and few convergence guarantees could be obtained
  * reason: the greedy or eps-greedy policy updates of most techniques, because
    * it does not ensure a policy improvement when applied with an approximate value function [8]. 
    * During a greedy update, small errors in the value function can cause large changes in the policy which in return 
      can cause large changes in the value function. 
    * This process, when applied repeatedly, can result in oscillations or divergence of the algorithms.
* when applied to simple examples with rather few states, policy-gradient methods often turn out to be quite inefficient,
  * reason: partially caused by the large plateaus in the expected return landscape where the gradients are small and 
    often do not point directly towards the optimal solution

## observation
* Similar as in supervised learning, the steepest ascent with respect to the **Fisher information metric** [3], 
  called the **‘natural’ policy gradient**, turns out to be significantly **more efficient** than normal gradients.
  
## idea: natural actor-critic (NAC)
* actor-critic:
  * The actor updates are
    achieved using stochastic policy gradients employing Amari’s natural gradient approach, while
  * the critic obtains both the natural policy gradient and
    additional parameters of a value function simultaneously by linear regression.
* do not follow the steepest direction in parameter space but the steepest direction with respect to the Fisher metric
* properties of the natural policy gradient 
  * **Convergence to a local minimum** guaranteed as for ‘vanilla gradients’ [3].
  * By choosing a more direct path to the optimal solution in parameter space, the natural gradient has, 
    from empirical observations, **faster convergence and avoids premature convergence** of ‘vanilla gradients’ (cf. Fig. 1).
  * The natural policy gradient can be shown to be covariant, i.e., 
    **independent of the coordinate frame chosen** for expressing the policy parameters (cf. Section 3.1).
  * As the natural gradient analytically averages out the influence of the stochastic policy 
    (including the baseline of the function approximator), it requires **fewer data point** for 
    a good gradient estimate than ‘vanilla gradients’.
     
## setup
* baseball swing robot

## result
* actor improvements with **natural policy gradients** are particularly appealing as
  these are independent of coordinate frame of the chosen policy representation, and
  can be estimated more efficiently **than regular policy gradients**

## misc
* policy iteration architectures consist of two steps, 
  * a policy evaluation step
    * requirement: makes efficient usage of experienced data
  * a policy improvement step.
    * requirement: improve the policy on every step until convergence while being efficient
     
