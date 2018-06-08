# Continuous Deep Q-Learning with Model-based Acceleration
* Shixiang Gu et al

## idea: normalized advantage function (NAF)
* avoids the need for a second actor or policy
function, resulting in a simpler algorithm.
  * The simpler optimization objective and the choice of value function pa-
rameterization result in an algorithm that is substantially
more sample-efficient when used with large neural network
function approximators on a range of continuous control
domains.
* approach to incorporating learned mod-
els into our continuous-action Q-learning algorithm based
on imagination rollouts: on-policy samples generated un-
der the learned model, analogous to the Dyna-Q method
(Sutton, 1990).
* to represent the Q-function Q(xt , ut ) in Q-learning in such a way that
its maximum, arg maxu Q(xt , ut ), can be determined eas-
ily and analytically during the Q-learning update
  * Decomposing Q into an advantage term A and a state-value term V
  * representations:
    is based on a neural network that separately outputs a value
    function term V (x) and an advantage term A(x, u), which
    is parameterized as a quadratic function of nonlinear fea-
    tures of the state:

## result
* NAF > DDPG
*  although Q-learning can incorporate off-policy experience,
learning primarily from off-policy exploration (via model-
based planning) only rarely improves the overall sample
efficiency of the algorithm.
  * We postulate that this caused by the need to observe both successful and unsuccessful
actions, in order to obtain an accurate estimate of the Q-
function.
  * We demonstrate that an alternative method based
on synthetic on-policy rollouts achieves substantially im-
proved sample complexity, but only when the model learn-
ing algorithm is chosen carefully.
* contrib
  * derive and evaluate a Q-function representation that allows
for effective Q-learning in continuous domains.
  * evaluate several naı̈ve options for incorporating learned
models into model-free Q-learning, and we show that they
are minimally effective on our continuous control tasks.
  * to combine locally linear models with
local on-policy imagination rollouts to accelerate model-
free continuous Q-learning, and show that this produces a
large improvement in sample complexity.

## background
* For continuous action problems, Q-learning becomes diffi-
cult, because it requires maximizing a complex, nonlinear
function at each update.
  * For this reason, continuous domains are often tackled using actor-critic methods

## comment
* seems a breaktrough: Q-learning for continuous actions
* ?: how decomposing Q into (A + V) and using nets to represent V, A
  can make solving max of Q?
