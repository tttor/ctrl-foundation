## 8: Planning and Learning with Tabular Methods
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
