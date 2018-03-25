# Reinforcement Learning: An Introduction
* 2nd-edition: http://www.incompleteideas.net/book/the-book-2nd.html
* 1st-edition: http://incompleteideas.net/book/ebook/the-book.html or 
[via UQ Lib](https://ebookcentral-proquest-com.ezproxy.library.uq.edu.au/lib/uql/detail.action?docID=3338821)
* https://github.com/ShangtongZhang/reinforcement-learning-an-introduction
* https://github.com/dennybritz/reinforcement-learning

## 6: Temporal-Difference Learning
* TD is a combination of _Monte Carlo_ and _dynamic programming (DP)_ ideas
  *  Like Monte Carlo methods, TD methods can learn directly from raw experience without 
  a model of the environment’s dynamics
  * Like DP, TD methods update estimates based in part on other learned estimates, without 
  waiting for a final outcome (they bootstrap)
* TD methods combine the sampling of Monte Carlo with the bootstrapping of DP.

### TD Prediction
* the policy evaluation or prediction problem:
  * the problem of estimating the value function for a given policy
* Monte Carlo (MC) vs DP vs TD(0)
  * target in value fn updates:
    * MC: $G_t$, the actual return following time t
    * TD: $R_{t+1} + \gamma V(S_{t+1})
  * target is an estimate:
    * MC target is an estimate because the expected value in (6.3) is not known; 
      a sample return is used in place of the real expected return. 
    * DP target is an estimate not because of the expected values, 
      which are assumed to be completely provided by model of the environment, but 
      because $v(S_{t+1}) is not known and the current estimate, $V(St+1)$, is used instead. 
    * TD target is an estimate for both reasons: 
      * it samples the expected values in (6.4) and 
      * it uses the current estimate V instead of the true
  * update
    * MC, TD do sample updates:
    involve looking ahead to a sample successor state (or state–action pair), 
    using the value of the successor and the reward along the way to compute a backed-up value, and 
    then updating the value of the original state (or state–action pair) accordingly. 
    The simplest TD update is: $V(S_t) \leftarrow V(S_t) + \alpha [ R_{t+1} + \gamma V(S_{t+1}) - V(S_t) ]$
    * DP does expected update:
     based on a single sample successor rather than on a complete distribution of all possible successors.
   * need model? (of the environment, of its reward and next-state probability distributions)
     * TD: not require
     * DPL require
* TD-error: $\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$
  * available at t+1
  * if the array V does not change during the episode (as it does not in Monte Carlo methods), then
    the Monte Carlo error can be written as a sum of TD errors

### Advantages of TD Prediction Methods
* For any fixed policy π, TD(0) has been proved to converge to $v_{\pi}$ , ....
*  In practice, TD methods have usually been found to converge faster than constant-α MC methods on stochastic tasks,

### Optimality of TD(0)
*  batch updating:
  * Given a finite amount of experience, to present the experience repeatedly until the method converges upon an answer.
  * updates are made only after processing each complete batch of training data.

###  Sarsa: On-policy TD Control
* The SARSA (on-policy) 
  * Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~Q(S_{t+1},A_{t+1}) - Q(S_{t},A_{t})]
* Q-learning (off-policy)
  * Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha [R_{t+1} + \gamma~max_a Q(S_{t+1},a) - Q(S_{t},A_{t})]

## 13: Policy Gradient Methods
In this chapter we consider methods that instead learn a parameterized policy that
can select actions without consulting a value function.
A value function may still be used to learn the policy parameter, but is not required for action selection.

we consider methods for learning the policy parameter based on the gradient of some
performance measure J(θ) with respect to the policy parameter. These methods seek to maximize
performance, so their updates approximate gradient ascent in J:

Methods that learn approximations to both policy and value functions are often called actor–critic methods, where
* `actor` is a reference to the learned policy, and
* `critic` refers to the learned value function, usually a state-value function.

the policy can be parameterized in any way, as long as
it is differentiable with respect to its parameters, that is,
as long as the gradient exists and is always finite.
In practice, to ensure exploration we generally require that the policy never becomes deterministic.

Of course, one could
select according to a softmax over action values, but this alone would not allow the policy to approach
a deterministic policy. Instead, the action-value estimates would converge to their corresponding true
values, which would differ by a finite amount, translating to specific probabilities other than 0 and 1.

advantage that policy parameterization
* the policy may be a simpler function to approximate,
  if this is the case, then it will typically learn faster and yield a superior asymptotic policy
* sometimes a good way of injecting prior
  knowledge about the desired form of the policy into the reinforcement learning system.
* with continuous policy parameterization the action probabilities change smoothly
  as a function of the learned parameter;
  Largely because of this stronger convergence guarantees are available for
  policy-gradient methods than for action-value methods.

Inthe episodic case,
the performance measure:
the value of the start state of the episode.

the policy gradient theorem provides
an analytic expression for the gradient of performance with respect to the
policy parameter (which is what we need to approximate for gradient ascent (13.1))
that does not involve the derivative of the state distribution.
The policy gradient theorem establishes that...where
the gradients are column vectors of partial derivatives with respect to the components of θ,
and π denotes the policy corresponding to parameter vector θ.

Recall our overall strategy of stochastic gradient ascent (13.1), which
requires a way to obtain samples such that the expectation of the
sample gradient is proportional to the actual gradient of the performance measure as a function of the parameter.

REINFORCE uses the complete return from time t, which includes all future rewards up
until the end of the episode. In this sense REINFORCE is a Monte Carlo algorithm and is well defined
only for the episodic case with all updates made in retrospect after the episode is completed.
As a Monte Carlo method REINFORCE may be of high variance and thus produce slow learning.
As a stochastic gradient method, REINFORCE has good theoretical convergence properties.

REINFORCE with Baseline:
One natural choice for the baseline is an estimate of the state value.
Although the REINFORCE-with-baseline method learns both a policy and a state-value function, we
do not consider it to be an actor–critic method because its state-value function is used only as a
baseline, not as a critic. That is, it is not used for bootstrapping (updating the value estimate for
a state from the estimated values of subsequent states), but only as a baseline for the state whose
estimate is being updated.
REINFORCE with baseline is unbiased and
will converge asymptotically to a local minimum, but like all Monte Carlo methods it tends to learn
slowly (produce estimates of high variance) and to be inconvenient to implement online or for continuing
problems.

For continuing problems without episode boundaries we need to define
performance in terms of the average rate of reward per time step.

Policy-based methods offer practical ways of dealing with large actions spaces, even continuous spaces
with an infinite number of actions. Instead of computing learned probabilities for each of the many
actions, we instead learn statistics of the probability distribution. For example, the action set might be
the real numbers, with actions chosen from a normal (Gaussian) distribution.

Summary:
* A parameterized policy enables actions to be taken without consulting
action-value estimates—though action-value estimates may still be learned and
used to update the policy parameter.
* policy-gradient methods—meaning methods that
update the policy parameter on each step in the direction of an estimate of
the gradient of performance with respect to the policy parameter.
* Methods that learn and store a policy parameter have many advantages.
  * can learn specific probabilities for taking the actions.
  * can learn appropriate levels of exploration and approach deterministic policies asymptotically
  * can naturally handle continuous state spaces
  * on some problems the policy is just simpler to represent parametrically than the value function;
* policy gradient theorem gives an exact formula for how performance is
affected by the policy parameter that does not involve derivatives of the state distribution
*  The state-value function assigns credit to—critizes—the policy’s action selections, and
accordingly the former is termed the critic and the latter the actor, and
these overall methods are sometimes termed actor–critic methods.

## 1: intro
* Most distinguishing features of RL:
  * being a close loop
  * no direct instruction on what action to take
  * action consequences play out over extended period
  * trade-off between exploration and exploitation
  * trying to maximize a reward signal instead of trying to find hidden structure
  * learning from interaction
  * toward simpler and fewer general principles of artificial intelligence
  * time really matters (sequential, not iid)

* Most work in planning does not consider planning's role in real-time decision making (specifically offline planning) or
the question of where the predictive models necessary for planning would come from.
When reinforcement learning involves planning, it has to address the interplay between planning and real-time action selection,
as well as the question of how environment models are acquired and improved.
Note also that, the most important component of almost all reinforcement learning algorithms we consider is
a method for efficiently estimating values

* Four subelements of RL:
  * a policy
  * a reward signal
  * a value function
  * a model of environment (optional\footnote{used for planning in model-based RL})

* Evolutionary methods for RL evaluate the lifetime behavior of, typically, many non-learning agents,
each using a different policy for interacting with its environment,
and select those that are able to obtain the most reward.
Evolutionary methods have advantages on problems in which the learning agent cannot accurately
sense the state of its environment, or if the space of policies is sufficiently small, or
can be structured so that good policies are common or easy to find
or if a lot of time is available for the search.

* In Tic-Tac-Toe, one learns a model of the opponent’s behavior, up to some level of confidence,
and then apply dynamic programming to compute an optimal solution given the approximate opponent model.

## 8: 
Model-based RL requires a model of the environment, model-free RL does not.
Model-based methods rely on planning as their primary component, while model-free methods primarily rely on learning.
Model here refers to anything that an agent can use to predict how the environment will respond to its actions.

A unified view of planning and learning is based on two basic ideas:
* all state-space planning methods involve computing value functions as
a key intermediate step toward improving the policy, and
* they compute value functions by backup operations applied to simulated experience.

One way to integrate learning and planning processes is simply by allowing both
to update the same estimated value function.
Any of the learning methods can be converted into planning methods simply by
applying them to simulated (model-generated) experience rather than to real experience.
The most natural approach is for all processes to proceed asynchronously and in parallel.

Planning should be done online in very small steps.
Within a (online) planning agent, there are at least two roles for real experience:

* used to improve the model (to make it more accurately match the real environment),
i.e model learning, or system identification (in adaptive control)
  * make fuller use of a limited amount of experience and thus
  achieve a better policy with fewer environmental interactions.
  * can efficiently learn model by supervised learning methods
  * can reason about model uncertainty
  * two sources of approximation error: model and value function
* used to directly improve the value function and policy using some kinds of
reinforcement learning methods, i.e. direct RL (model-free learning)
  * much simpler and
  * are not affected by biases in the design of the model.

In Dyna-Q algorithm, the same reinforcement learning method is used both for
learning from real experience and for planning from simulated experience.

There are two ways of thinking about planning:
* background planning:
using simulated experience to gradually improve a policy or value function,
* decision time planning:
using simulated experience to select an action for the current state,
this is also called online planning;
the values and policy are specific to the current state and the action choices available there,
so much so that the values and policy created by the planning process are typically discarded after
being used to select the current action.

In model learning, the goal is to estimate a model from experience $$ \{S_1, A_1, R_2, ..., S_t \} $$.
That is a supervised learning problem, where:
$(S_1, A_1) \mapsto (S_2, R_2), (S_2, A_2) \mapsto (S_3, R_3), \ldots, (S_{t-1}, A_{t-1}) \mapsto (S_t, R_t)$.
Learning $s, a \mapsto r$ is a regression problem, whereas
learning $s, a \mapsto s'$ is a density estimation problem.

## priority
* 13 Policy Gradient Methods
* 9 On-policy Prediction with Approximation


