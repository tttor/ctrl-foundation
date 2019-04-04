# ch 04 dynamic programming

* Although DP ideas can be applied to problems with continuous state and action spaces,
  exact solutions are possible only in special cases.
  * Which special cases?
* A common way of obtaining approximate solutions for tasks with
  continuous states and actions is
  * to quantize the state and action spaces and
  * then apply finite-state DP methods.
    * meaning: finite-state and finite-action DP methods?

# 4.1 Policy Evaluation (Prediction)
* ... also refer to it as the prediction problem.
  * Why? is it because given a policy, we want to determine its value fn
    by some prediction method?
* The existence and uniqueness of $v_\pi$ are guaranteed as long as
  either $\gamma < 1$ or
  eventual termination is guaranteed from all states under the policy $\pi$
  * Why so exactly? need to look at Puterman book!
* Iterative Policy Evaluation, for estimating $V \approx v_\pi$
  * The in-place algorithm usually converges faster than the two-array version,
    * because it uses new data as soon as they are available

# 4.2 Policy Improvement
* the policy improvement theorem
  * carries through for the stochastic case.
    * if there are ties in policy improvement steps such then (in the stochastic case)
      * need not select a single action from among them.
      * Instead, each maximizing action can be given a portion of the probability
        of being selected in the new greedy policy.
* policy improvement.
  * The process of making a new policy that improves on an original policy, by
    making it greedy with respect to the value function of the original policy
  * Policy improvement thus must give us
    a strictly better policy except when the original policy is already optimal.
  * The greedy policy takes the action that looks best in the short term,
    after one step of lookahead, according to $v_\pi$

# 4.3 Policy Iteration
* Box page 80
  * each policy evaluation, itself an iterative computation,
    is started with the value function for the previous policy.
* One drawback to policy iteration is
  that each of its iterations involves policy evaluation,
  which may itself be a protracted iterative computation requiring
  multiple sweeps through the state set.

# 4.4 Value Iteration
* observation:
  * the policy evaluation step of policy iteration can be truncated in several ways
    without losing the convergence guarantees of policy iteration.
* value iteration
  * when policy evaluation is stopped after just one sweep (one update of each state)
  * as a particularly simple update operation that
    combines the policy improvement and truncated policy evaluation steps
  * Box page 83
    * note: there is no policy improvement in the loop, so why saying:
      "...combines the policy improvement and truncated policy evaluation steps..."
      * ANS: the policy improvement comes from the max operation

# 4.5 Asynchronous Dynamic Programming
* Asynchronous DP algorithms are
  * in-place iterative DP algorithms that are not organized
    in terms of systematic sweeps of the state set
  * update the values of states in any order whatsoever,
    using whatever values of other states happen to be available.

# 4.6 Generalized Policy Iteration
* term generalized policy iteration (GPI)
  * to refer to the general idea of letting policy-evaluation and
    policy-evaluation improvement processes interact,
    independent of the granularity and other details of the two processes

# 4.7 Efficiency of Dynamic Programming
* A DP method is guaranteed to find an optimal policy in
  polynomial time even though the total number of (deterministic) policies is $k^n$.
  * DP is exponentially faster than any direct search in policy space could be,
    because direct search would have to exhaustively examine each policy to provide the
    same guarantee.
  * Linear programming methods can also be used to solve MDPs, and
    in some cases their worst-case convergence guarantees are better than
    those of DP methods.
    * But linear programming methods become impractical at a much smaller number of states
      than do DP methods (by a factor of about 100).
* DP is sometimes thought to be of limited applicability because of
  the curse of dimensionality, the fact that the number of states often grows exponentially with the number of state variables.
  * Large state sets do create difficulties, but these are inherent difficulties
    of the problem, not of DP as a solution method.
* Both policy iteration and value iteration are widely used, and
  * it is not clear which, if either, is better in general.
* For some problems, even this much memory and computation is impractical,
  yet the problem is still potentially solvable because relatively few states occur along
  optimal solution trajectories.
*  GPI is the general idea of two interacting processes revolving
  around an approximate policy and an approximate value function.
  * One process takes the policy as given and performs some form of policy
    evaluation, changing the value function to be more like the true value function
    for the policy.
  * The other process takes the value function as given and performs some form
    of policy improvement, changing the policy to make it better,
    assuming that the value function is its value function.
* In some cases, GPI can be proved to converge,
  most notably for the classical DP methods that we have presented in this chapter.
  * In other cases convergence has not been proved, but still the idea of GPI
    improves our understanding of the methods.
* DP methods update estimates of the values of states based on estimates of
  the values of successor states.
  * That is, they update estimates on the basis of other estimates.
    * We call this general idea bootstrapping.
