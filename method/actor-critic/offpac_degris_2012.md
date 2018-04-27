# off-Policy Actor-Critic
* Thomas Degris, et al
* Proceedings of the 29 th International Conference on Machine Learning, Edinburgh, Scotland, UK, 2012.

## problem
* Previous work on actor-critic algorithms is limited to the on-policy setting and
  does not take advantage of the recent advances in off-policy gradient temporal-difference learning.
* practical online methods with convergence guarantees have been restricted to
  the on-policy setting, in which the agent learns only about the policy it is executing.

## observation
* Off-policy techniques, such as Greedy-GQ, enable a target policy to be learned while
  following and obtaining data from another (behavior) policy.
* For many problems, actor-critic methods are more practical than action value methods (like Greedy-GQ)
  * because they explicitly represent the policy;
  * consequently, the policy can be stochastic and utilize a large action space.

## idea:  Off-PAC (Off-Policy Actor-Critic)
* online and incremental, and its per-time-step complexity scales linearly
  with the number of learned weights
* Off-PAC has two learners:
  * the actor:
    * updates the policy weights.
  * the critic:
    * learns an off-policy estimate of the value function for the current actor policy,
      different from the (fixed) behavior policy.
    * This estimate of the value function is then used by the actor to update the policy.
    * uses GTD(lambda) (Maei, 2011),
      a gradient-TD method with eligibitity traces for learning state-value functions.

## result
* an incremental, linear time and space complexity algorithm that
  * includes eligibility traces, prove convergence under assumptions
    similar to previous o↵-policy algorithms,
* Off-PAC
  * converges in a standard off-policy setting.
  * has the best final performance on three benchmark problems and
  * consistently has the lowest standard error.
  * is a significant step toward robust off-policy control.
  * The time and space complexity
    * is linear in the number of learned weights.
* contrib
  * define a new objective for our policy weights and derive
    a valid backward-view update using eligibility traces.
  * an o↵-policy policy-gradient theorem and a convergence proof for
    O↵-PAC when = 0, under assumptions similar to
    previous o↵-policy gradient-TD proofs.
  * an empirical comparison of
    Q( ), Greedy-GQ, O↵-PAC, and a soft-max version of
    Greedy-GQ that we call Softmax-GQ, on three bench-
    mark problems in an o↵-policy setting.

## comment
* TODO: read more
