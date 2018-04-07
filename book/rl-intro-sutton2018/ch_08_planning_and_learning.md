# 8: Planning and Learning with Tabular Methods
* model-based vs model-free RL:
  * Model-based RL
    * requires a model of the environment
    * rely on planning as their primary component
    * eg: dynamic programming and heuristic search
  * model-free RL.
    * **not** requires a model of the environment
    * primarily rely on learning
    * eg: Monte Carlo and temporal-difference
  * similarities.
    * the computation of value functions.
    * based on looking ahead to future events,
      computing a backed-up value, and
      then using it as an update target for an approximate value function.

## 8.1 Models and Planning
* Model
  * refers to anything that an agent can use to predict how the environment will respond to its actions.
  * Given a state and an action, a model produces a prediction of the resultant next state and next reward
  * is used to simulate the environment and produce simulated experience.
  * types:
    * distribution models:
      * produce a description of all possibilities and their probabilities
    * sample models:
      * produce just one of the possibilities, sampled according to the probabilities
* term `planning`
  * refers to any computational process that takes a model as input and produces or
    improves a policy for interacting with the modeled environment:
  * types in AI:
    * State-space planning,
      * is viewed primarily as a search through the state space for
        an optimal policy or an optimal path to a goal.
    * plan-space planning,
      * planning is a search through the space of plans.
      * difficult to apply efficiently to the stochastic sequential decision problems that
        are the focus in reinforcement learning
* A unified view of (state-space) planning and learning is based on two basic ideas:
  (means that many ideas and algorithms can be transferred between planning and learning.)
  * all state-space planning methods involve computing value functions as
    a key intermediate step toward improving the policy, and
  * they compute value functions by backup operations applied to simulated experience.
* to integrate learning and planning processes
  * allowing both to update the same estimated value function.
  * Any of the learning methods can be converted into planning methods simply by
    applying them to simulated (model-generated) experience rather than to real experience.
  * The most natural approach is for all processes to proceed asynchronously and in parallel.

## 8.2 Dyna: Integrated Planning, Acting, and learning
* When planning is done on-line, while interacting with the environment:
  * New information gained from the interaction may change the model and thereby interact with planning.
  * It may be desirable to customize the planning process in some way to
    the states or decisions currently under consideration, or expected in the near future.
  * Dyna-Q, a simple architecture integrating the major functions needed in an on-line planning agent.
  * Planning should be done online in very small steps.
* Within a (online) planning agent, there are at least two roles for real experience:
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
* Dyna-Q:
  * includes planning, acting, model-learning, and direct RL, all occurring continually.
  * the same reinforcement learning method is used both for
    learning from real experience and for planning from simulated experience.
    * The planning method:
      is the random-sample one-step tabular Q-planning method
    * The direct RL method:
      is one-step tabular Q-learning.
  * The model-learning method
    * is table-based and
    * assumes the environment is deterministic.
  * Learning and planning are deeply integrated in the sense that
    * they share almost all the same machinery,
    * differing only in the source of their experience.
  * The agent is always reactive and always deliberative,
    responding  instantly to the latest sensory information
    and yet always planning and model-learning in the background.
    (As the model changes, the ongoing planning process will gradually compute
    a different way of behaving to match the new model).

## 8.3 When the Model Is Wrong
* Models may be incorrect because
  * the environment is stochastic and only a limited number of samples have been observed, or
  * the model was learned using function approximation that has generalized imperfectly, or
  * the environment has changed and its new behavior has not yet been observed.
* example:
  * Example 8.2: Blocking Maze
  * Example 8.3: Shortcut Maze
* The Dyna-Q+ agent;
  * keeps track for each state-action pair of
    how many time steps have elapsed since the pair was last tried in a real interaction with the environment.
    * The more time that has elapsed, the greater (we might presume) the chance that
      the dynamics of this pair has changed and that the model of it is incorrect.
  * To encourage behavior that tests long-untried actions, a special "bonus reward" is
    given on simulated experiences involving  these actions.

## 8.4 Prioritized Sweeping
* to work back not just from goal states but from any state whose value has changed.
* backward focusing of planning computations:
  work backward from arbitrary states that have changed in value,
  either performing useful updates or terminating the propagation.
* prioritized sweeping:
  * A queue is maintained of every state-action pair whose
    estimated value would change nontrivially if updated,
    prioritized by the size of the change.
  * When the top pair in the queue is updated, the effect on each of
    its predecessor pairs is computed.
    * If the effect is greater than some small threshold, then
      the pair is inserted in the queue with the new priority
      (if there is a previous entry of the pair in the queue, then
      insertion results in only the higher priority entry remaining in the queue).
    * In this way the effects of changes are efficiently propagated backward until quiescence.
* Extensions to stochastic environments
  * The model is maintained by keeping counts of the number of times
    each state-action pair has been experienced and of what the next states were.
  * to update each pair not with a sample update, as we have been using so far, but
    with an expected update, taking into account all possible next states and
    their probabilities of occurring.
* forward focusing:
  * to focus on states according to how easily they can be reached from the states that
    are visited frequently under the current policy

## 8.5 Expected vs. Sample Updates



<!--
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
 -->
