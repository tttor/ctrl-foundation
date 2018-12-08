# Trust Region Policy Optimization
* icml2015
* http://proceedings.mlr.press/v37/schulman15.html
* https://arxiv.org/abs/1502.05477
* https://www.depthfirstlearning.com/2018/TRPO

## problem
*  optimize nonlinear policies with tens of thousands of parameters
* Equation (4) implies that a sufficiently small step ...,
  * but does not give us any guidance on old how big of a step to take.

## observation
* The inability of ADP and gradient-based methods to consistently
  beat gradient-free random search is unsatisfying, since
  gradient-based optimization algorithms enjoy much better
  sample complexity guarantees than gradient-free methods
  (Nemirovski, 2005).
* Continuous gradient-based optimiza-
  tion has been very successful at learning function approxi-
  mators for supervised learning tasks with huge numbers of
  parameters, and extending their success to reinforcement
  learning would allow for efficient training of complex and
  powerful policies.

## idea: TRPO (trust region policy optimization)
*  prove that minimizing a certain surrogate loss function guarantees policy improvement with non-trivial step sizes.

* two variants of this algorithm:
  * **the single-path method**, which can be ap- plied in the model-free setting;
  * **the vine method**, which requires the system to be restored to particular states,
  which is typically only possible in simulation.
* prelim
  * advantage fn: $A_{\pi}(s,a) = Q_{\pi}(s,a) - V_{\pi}(s)$
  * Equ.2 implies that any policy update $\pi \mapsto \bar{\pi}$ that
    has a **nonnegative expected advantage at every state** $s$ is guaranteed to increase
   the policy performance, or leave it constant in the case that the expected advantage is zero everywhere.
  * in the approximate setting, it will typically be unavoidable, due to estimation and approximation error, that
  there will be some states s for which the expected advantage is negative,
    * introduce a local approximation to the policy performance $\nu$, Equ.3
  * conservative policy iteration, for which they could provide explicit lower bounds on the improvement of $\nu$.
* Monotonic Improvement Guarantee for General Stochastic Policies
  * the policy improvement bound in Equation (6) can be extended to general stochastic policies, rather than
    just mixture polices, by replacing $\alpha$ with a distance measure between $\pi$ and $\tilde{\pi}$
    (e.g. total variation distance), and changing the constant $\epsilon$ appropriately
  * Trust region policy optimization is an approximation to Algorithm 1, which
    uses a constraint on the KL divergence rather than a penalty to robustly allow large updates.
* Optimization of Parameterized Policies
  * a trust region constraint:
    * to use a constraint on the **KL divergence** between the new policy and the old policy
  * a heuristic approximation which considers the average KL divergence
* Sample-Based Estimation of the Objective and Constraint
  * approx the objective and constraint functions using Monte Carlo simulation
  * 2 sampling schemes:
    * single path: is based on sampling individual trajectories
    * vine: constructing a rollout set and then performing multiple actions from each state in the rollout set

```
Our principal theoretical result is that the policy improvement
bound in Equation (6) can be extended to general stochas-
tic policies, rather than just mixture polices, by replacing α
with a distance measure between π and π̃, and changing the
constant  appropriately. Since mixture policies are rarely
used in practice, this result is crucial for extending the im-
provement guarantee to practical problems.

In practice, if we used the penalty coefficient C recom-
mended by the theory above, the step sizes would be very
small. One way to take larger steps in a robust way is to use
a constraint on the KL divergence between the new policy
and the old policy, i.e., a trust region constraint:

```

## setup
considered in the compar-
ison: single path TRPO; vine TRPO; reward-weighted re-
gression (RWR), an EM-like policy search method (Peters
& Schaal, 2007); relative entropy policy search (REPS)
(Peters et al., 2010); cross-entropy method (CEM), a
gradient-free method (Szita & Lörincz, 2006); covariance
matrix adaption (CMA), another gradient-free method
(Hansen & Ostermeier, 1996); natural gradient, the classic
natural policy gradient algorithm (Kakade, 2002)

## result
* suggest:
  * The use of recurrent policies with hidden state, could further make it possible to roll state estimation and
  control into the same policy in the partially-observed setting.
  * By combining TRPO with model learning, it would also be possible to substantially reduce its sample complexity,
  making it applicable to real-world settings where samples are expensive.

## background
* policy optimization can be classified into three broad categories:
  * **policy iteration methods**,
    which alternate between estimating the value function under the current policy and improving the policy (Bertsekas, 2005);
  * **policy gradient methods**,
    which use an estimator of the gradient of the expected return (total reward) obtained from sample trajectories (Peters & Schaal, 2008a) (and which, as we later discuss, have a close connection to policy iteration); and
  * **derivative-free optimization methods**,
    which treat the return as a black box function to be optimized
    in terms of the policy parameters (Szita & Lorincz, 2006)
    * the cross-entropy method (CEM) and
    * covariance matrix adaptation (CMA)
* Classic: that the update performed by exact policy iteration, which uses the deterministic policy
  $\pi(s) = argmax_a A_{\pi}(s, a)$ improves the policy if there is at least **one state-action pair**
  with a positive advantage value and nonzero state visitation probability, otherwise
  the algorithm has converged to the optimal policy

## comment
* vital role of KL divergence
* the notion of "trust region" is from optimization
* this trust region still explicitly computes step length via a line search method,
  as in Appendix C, in trust-region opt,
  should not the step length is computed implicitly, simultaneouly with the step direction?
