# Addressing Function Approximation Error in Actor-Critic Methods
* Scott Fujimoto, Herke van Hoof, David Meger,
* https://arxiv.org/abs/1802.09477
* https://github.com/sfujim/TD3 # pytorch

## problem
* function approximation errors lead to
  overestimated value estimates and
  the accumulation of error in temporal difference methods and
  suboptimal policies
  * present in an actor-critic setting

## idea
* takes the minimum value between a pair of critics to restrict overestimation and
  delays policy updates to reduce per-update error
* a clipped Double Q-learning variant which
  * favors underestimations by
    bounding situations where Double Q-learning does poorly.
* address variance reduction by
  * show that target networks, a common approach in deep Q-learning methods, are
    critical for variance reduction.
  * to address the coupling of value and policy,
    we propose delaying policy updates until each target has converged
  * introduce a novel regularization strategy, where
    a SARSA-style update bootstraps similar action estimates to further reduce variance.
* maintains a pair of critics along with a single actor.

## setup
* openai gym mujoco task
  * nets: ?
  * optim: Adam
  * activ-fn: relu, relu, tanh

## result

## comment
* fn approx err is indeed present
* td3= ddpg + doubleQlearning
* (-) no atari xprmt
