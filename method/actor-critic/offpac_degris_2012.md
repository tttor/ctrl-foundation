# off-Policy Actor-Critic
* Thomas Degris, et al
* Proceedings of the 29 th International Conference on Machine Learning, Edinburgh, Scotland, UK, 2012.

## problem
* Previous work on actor-critic algorithms is limited to the on-policy setting and
  does not take advantage of the recent advances in off-policy gradient temporal-di↵erence learning.

## observation
* Off-policy techniques, such as Greedy-GQ, enable a target policy to be learned while
  following and obtaining data from another (behavior) policy.
* For many problems, actor-critic methods are more practical than action value methods (like Greedy-GQ)
  * because they explicitly represent the policy;
  * consequently, the policy can be stochastic and utilize a large action space.

## idea:  Off-PAC (Off-Policy Actor-Critic)
* online and incremental, and its per-time-step complexity scales linearly
  with the number of learned weights

## result
* an incremental, linear time and space complexity algorithm that
  * includes eligibility traces, prove convergence under assumptions
    similar to previous o↵-policy algorithms,
* Off-PAC
  * converges in a stan-dard off-policy setting.
  * has the best final performance on three benchmark problems and
  * consistently has the lowest standard error.
  * is a significant step toward robust off-policy control.

## comment
* TODO: read more
