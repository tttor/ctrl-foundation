## 8.13 Summary of Part I: Dimensions
* 3 key ideas of the methods we have explored so far:
  * they all seek to estimate value functions;
  * they all operate by backing up values along actual or possible state trajectories; and
  * they all follow the general strategy of generalized policy iteration (GPI), meaning that
    they maintain an approximate value function and an approximate policy, and
    they continually try to improve each on the basis of the other.
* important dimensions wrt the kind of update used to improve the value function, Figure 8.11
  * The horizontal dimension is
    * whether they are sample updates (based on a sample trajectory) or
    expected updates (based on a distribution of possible trajectories).
  * The vertical dimension corresponds to
    * the depth of updates, that is, to the degree of bootstrapping.
  * corners
    *  dynamic programming,
    * TD,
    * Monte Carlo.
    * exhaustive search
  * from one-step TD updates to full-return Monte Carlo updates
    * the sample-update methods,
    * methods based on n-step updates
* third dimension (perpendicular to the plane of the page in Figure 8.11)
  * on-policy and
    * agent learns the value function for the policy it is currently following
  * off-policy methods.
    * agent learns the value function for the policy for a different policy,
      often the one that the agent currently thinks is best.
      * The policy generating behavior is typically different from what is currently
        thought best because of the need to explore.
* other dim:
  * Definition of return
    * Is the task episodic or continuing, discounted or undiscounted?
  * Action values vs. state values vs. afterstate values
    * What kind of values should be estimated?
    * If only state values are estimated, then either a model or a separate
      policy (as in actor–critic methods) is required for action selection.
  * Action selection/exploration
    * How are actions selected to ensure a suitable trade-off between exploration and exploitation?
    * eg: ε-greedy, optimistic initialization of values, soft-max, and upper confidence bound.
  * Synchronous vs. asynchronous
    * Are the updates for all states performed simultaneously or one by one in some order?
  * Real vs. simulated
    * Should one update based on real experience or simulated experience?
    * If both, how much of each?
  * Location of updates
    * What states or state–action pairs should be updated?
    * Model- free methods can choose only among the states and state–action pairs actually encountered,
    * but model-based methods can choose arbitrarily.
  * Timing of updates
    * Should updates be done as part of selecting actions, or only after-ward?
  * Memory for updates
    * How long should updated values be retained?
    * Should they be retained permanently, or
      only while computing an action selection, as in heuristic search?

<!--
In model learning, the goal is to estimate a model from experience $$ \{S_1, A_1, R_2, ..., S_t \} $$.
That is a supervised learning problem, where:
$(S_1, A_1) \mapsto (S_2, R_2), (S_2, A_2) \mapsto (S_3, R_3), \ldots, (S_{t-1}, A_{t-1}) \mapsto (S_t, R_t)$.
Learning $s, a \mapsto r$ is a regression problem, whereas
learning $s, a \mapsto s'$ is a density estimation problem.
 -->
