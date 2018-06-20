# Continuous Deep Q-Learning with Model-based Acceleration
* Shixiang Gu et al
* http://proceedings.mlr.press/v48/gu16.html
* https://icml.cc/2016/reviews/1274.txt

## problem
* high sample complexity of model-free algorithms, 
  * particularly when using very high-dimensional function approximators
* Using model-based RL also improves efficiency, 
  * but limits the policy to only be as good as the learned model.
  * ineffective at accelerating learning. 
    * due in part to the nature of value function estimation algorithms,
      which must experience both good and bad state transitions
      to accurately model the value function landscape
  * Dyna-Q style methods to accelerate model-free RL 
    * is very effective when the learned model perfectly matches the true model, 
    * but degrades rapidly as the model becomes worse. 

## idea: normalized advantage function (NAF)
* avoids the need for a second actor or policy function, resulting in a simpler algorithm.
  * The simpler optimization objective and the choice of value function pa-
rameterization result in an algorithm that is substantially
more sample-efficient when used with large neural network
function approximators on a range of continuous control
domains.
* on imagination rollouts: on-policy samples generated under the learned model, analogous to the Dyna-Q method
  * iteratively fitting local linear models to the latest batch of on-policy or off-policy rollouts provides 
    sufficient local accuracy to achieve substantial improvement using short imagination rollouts 
    in the vicinity of the real-world samples.


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

* although Q-learning can incorporate off-policy experience,
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
  * derive and evaluate a Q-function representation that allows for effective Q-learning in continuous domains.
  * evaluate several naı̈ve options for incorporating learned models into model-free Q-learning, and 
    we show that they are minimally effective on our continuous control tasks.
  * to combine **locally linear models** with local on-policy imagination rollouts to accelerate 
    model-free continuous Q-learning, and show that this produces a large improvement in sample complexity.

## background
* For continuous action problems, Q-learning becomes difficult, 
  * because it requires maximizing a complex, nonlinear function at each update.
  * For this reason, continuous domains are often tackled using actor-critic methods
* model-based RL to accelerate learning

## comment
* address low sample efficiency via
  * Q-learning (value-based) for cont actions
  * model-based (toward Dyna)
* ?: so NAF for both direct and indirect polucy update?
* ?: how decomposing Q into (A + V) and using nets to represent V, A
  can make solving max of Q?
* ?: how imagination rollout differ from Dyna?
  * ans:  iteratively fitting local linear models ...
* from the reviewer:
> The main advantages of the proposed method over comparable actor-critic methods seem to be that the quadratic assumption acts as a regularizer and that the learning signal for all of the estimators comes directly from the environment

