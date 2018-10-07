# Policy Gradient Methods for Reinforcement Learning with Function Approximation
* Richard S. Sutton, David McAllester, Satinder Singh, Yishay Mansour
* nips2000

## problem
* Function approximation is essential to reinforcement learning, but
  the standard approach of approximating a value function and deter-
  mining a policy from it has so far proven theoretically intractable.

## idea
* the policy
  is explicitly represented by its own function approximator, indepen-
  dent of the value function, and is updated according to the gradient
  of expected reward with respect to the policy parameters.
*  prove that an unbiased estimate of the gradient (1) can be obtained
  from experience using an approximate value function satisfying certain properties.
* two ways of formulating the agent's objective are useful.
  * average-reward:
    One is the average reward formulation, in which policies are ranked according to
    their long-term expected reward per step
  * start-state:
    there is a designated start state,
    and we care only about the long-term reward obtained from it.
* Theorem 1 (Policy Gradient).
* Theorem 2 (Policy Gradient with Function Approximation)
*  the form given above for f w requires
  that it have zero mean for each state: l:a 1r(s, a)fw(s, a) = 0, Vs E S . In this
  sense it is better to think of f w as an approximation of the advantage function,
  A7r(s,a) = Q7r(s,a) - V7r(s) (much as in Baird, 1993), rather than of Q7r .

## result
* the gradient can be written in a form suitable for estimation from experience aided
  by an approximate action-value or advantage function.
* prove for the first time that a version of policy iteration
  with arbitrary differentiable function approximation is convergent to
  a locally optimal policy.

## background
* The value-function approach has worked well in many applications, but has several limitations.
  * First, it is oriented toward finding deterministic
    policies, whereas the optimal policy is often stochastic, selecting different actions with
    specific probabilities (e.g., see Singh, Jaakkola, and Jordan, 1994).
  * Second, an arbitrarily small change in the estimated value of an action can cause it to be, or not be,
    selected. Such discontinuous changes have been identified as a key obstacle to estab-
    lishing convergence assurances for algorithms following the value-function approach
    (Bertsekas and Tsitsiklis, 1996)
* REINFORCE algorithm also finds an unbiased estimate of
  the gradient, but without the assistance of a learned value function
* Learning a value function and using it to reduce the variance
  of the gradient estimate appears to be ess~ntial for rapid learning.

## comment
* this seems to be the very first paper on actor-critic:
  policy grad using value fn approx and where the policy is parameterized, eg. by a neural network
