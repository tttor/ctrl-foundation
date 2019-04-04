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
