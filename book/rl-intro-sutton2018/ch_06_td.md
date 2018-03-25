# 6: Temporal-Difference Learning
* TD is a combination of _Monte Carlo_ and _dynamic programming (DP)_ ideas
  * Like Monte Carlo methods, TD methods can learn directly from raw experience without
    a model of the environment’s dynamics
  * Like DP, TD methods update estimates based in part on other learned estimates, without
    waiting for a final outcome (they **bootstrap**)
* TD methods combine the sampling of Monte Carlo with the bootstrapping of DP.

## 6.1: TD Prediction
* the policy evaluation or prediction problem:
  * the problem of estimating the value function for a given policy
* Monte Carlo (MC) vs DP vs TD(0)
  * target in value fn updates:
    * MC: $G_t$, the actual return following time t
    * TD: $R_{t+1} + \gamma V(S_{t+1})
  * target is an estimate:
    * MC target is an estimate because the expected value in (6.3) is not known;
      a sample return is used in place of the real expected return.
    * DP target is an estimate not because of the expected values,
      which are assumed to be completely provided by model of the environment, but
      because $v(S_{t+1}) is not known and the current estimate, $V(St+1)$, is used instead.
    * TD target is an estimate for both reasons:
      * it samples the expected values in (6.4) and
      * it uses the current estimate V instead of the true
  * update
    * MC, TD do sample updates:
      involve looking ahead to a sample successor state (or state–action pair),
      using the value of the successor and the reward along the way to compute a backed-up value, and
      then updating the value of the original state (or state–action pair) accordingly.
      The simplest TD update is: $V(S_t) \leftarrow V(S_t) + \alpha [ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) ]$
    * DP does expected update:
      based on a single sample successor rather than on a complete distribution of all possible successors.
   * need model? (of the environment, of its reward and next-state probability distributions)
     * TD: not require
     * DP: require
* TD-error: $\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$
  * available at t+1
  * if the array V does not change during the episode (as it does not in Monte Carlo methods), then
    the Monte Carlo error can be written as a sum of TD errors

## 6.2: Advantages of TD Prediction Methods
* For any fixed policy, TD(0) has been proved to converge to $v_{\pi}$ , ....
* In practice, TD methods have usually been found to converge faster than constant-α MC methods on stochastic tasks,

## 6.3: Optimality of TD(0)
*  batch updating:
  * Given a finite amount of experience, to present the experience repeatedly until the method converges upon an answer.
  * updates are made only after processing each complete batch of training data.

## 6.4: Sarsa: On-policy TD Control
* The SARSA (on-policy)
  * Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~Q(S_{t+1},A_{t+1}) - Q(S_{t},A_{t})]

## 6.5 Q-learning: Off-policy TD Control
* Q-learning (off-policy)
  * Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~max_a Q(S_{t+1},a) - Q(S_{t},A_{t})]
* the learned action-value function, Q, directly approximates q∗ , the optimal action-value function,
  **independent** of the policy being followed (note: **max** operator)
* Example 6.6: Cliff Walking:
  * Although Q-learning actually learns the values of the optimal policy,
    its on-line performance is worse than that of Sarsa, which learns the roundabout policy.

## 6.6 Expected Sarsa
* like Q-learning except that instead of the maximum over next state-action pairs,
  it uses the expected value, taking into account how likely each action is under the current policy.
* Given the next state, $S_{t+1}$, this algorithm moves deterministically in the same direction as Sarsa move in expectation
* Expected Sarsa eliminates the variance due to random selection of $A_{t+1}$, but
  more computationally complex than Sarsa

## 6.7 Maximization Bias and Double Learning
* maximization in the construction of the target policies.
  * Q-learning: the target policy is the greedy policy given the current action values, which is defined with a max,
  * Sarsa: the policy is often ε-greedy, which also involves a maximization operation.
* maximization bias
  * may occur when a maximum over estimated values is used implicitly as an estimate of the maximum value,
    which can lead to a significant positive bias.
  * potential solution: **double learning**
* double learning:
  * Suppose we divided the plays in two sets and
  * used those 2 sets to learn 2 independent estimates, Q1 (a) and Q2 (a),
  * each an estimate of the true value q(a), for all a ∈ A.
  * use Q1, to determine the maximizing action `$A^* = argmax_a Q_1(a)$`,
  * use Q2 , to provide the estimate of its value, `$Q_2(A^*) = Q2 (argmax_a Q_1(a))$`.
  * This estimate will then be unbiased in the sense that `$E[Q_2(A^*)] = q(A^*)$`.

## 6.8 Games, Afterstates, and Other Special Cases
* Afterstates are
  * useful when we have knowledge of an initial part of the environment’s dynamics but
    not necessarily of the full dynamics.
  * For example, we know for each possible chess move what the resulting position will be,
    but not how our opponent will reply.
