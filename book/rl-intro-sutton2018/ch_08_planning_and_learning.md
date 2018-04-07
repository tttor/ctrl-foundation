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
* Planning, acting, and model-learning interact in a circular fashion,
  * each producing what the other needs to improve;
  * most natural approach is for all processes to proceed **asynchronously** and **in parallel**

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
* on one-step updates, they vary primarily along 3 binary dimensions
  * 1: whether they update
    * state values or
    * action values
  * 2: whether they estimate the value
    * for the optimal policy or
    * for an arbitrary given policy.
  * 3: whether the updates are
    * expected updates:
      * considering all possible events that might happen
      * require  a distribution model
      * yield a better estimate because they are uncorrupted by sampling error,
        but they also require more computation (the limiting resource in planning)
    * sample updates:
      * considering a single sample of what might happen.
      * affected by sampling error
      * cheaper computationally because it considers only one next state,
        not all possible next states.
      * likely to be superior to expected updates on problems with
        large stochastic branching factors and too many states to be solved exactly.

## 8.6 Trajectory Sampling
* 2 ways of distributing updates.
  * classical approach, from dynamic programming,
    * to perform sweeps through the entire state (or state–action) space,
      updating each state (or state–action pair) once per sweep; Exhaustive sweeps
    * issues
      * may not be time to complete even one sweep
      * in most tasks, the vast majority of the states are irrelevant because
        they are visited only under very poor policies or with very low probability.
  * second approach
    * to sample from the state or state–action space according to some distribution.
    * variants:
      * sample uniformly, as in the Dyna-Q agent
      * trajectory sampling
        * one simulates explicit individual trajectories and
          performs updates at the state or state-action pairs encountered along the way
        * to distribute updates according to the on-policy distribution
          * according to the distribution observed when following the current policy
          * one simply interacts with the model, following the current policy.
* sampling according to the on-policy distribution can be a great advantage for
  large problems, in particular for problems in which a small subset of
  the state–action space is visited under the on-policy distribution.
  * In the long run, focusing on the on-policy distribution may hurt because
    the commonly occurring states all already have their correct values.

## 8.7 Real-time Dynamic Programming (RTDP)
* RTDP,
  * is an on-policy trajectory-sampling version of
    the value-iteration algorithm of dynamic programming (DP).
  * updates the values of states visited in actual or simulated trajectories by
    means of expected tabular value-iteration updates
  * update order is dictated by the order states are visited in
    real or simulated trajectories
    (is an example of an asynchronous DP algorithm:
    update state values in any order whatsoever)
  * strongly focused on subsets of the states that were relevant to the problem’s objective.
  * advantage
    * is guaranteed to find a policy that is optimal on the relevant states without
      visiting every state infinitely often, or even without visiting some states at all
    * as the value function approaches the optimal value function v* ,
      the policy used by the agent to generate trajectories approaches an optimal policy
      because it is always greedy with respect to the current value function.
* RTDP converges with probability one to a policy that is
  optimal for all the relevant states provided:
  * 1) the initial value of every goal state is zero,
  * 2) there exists at least one policy that guarantees that a goal state will
    be reached with probability one from any start state,
  * 3) all rewards for transitions from non-goal states are strictly negative, and
  * 4) all the initial values are equal to, or greater than, their optimal values
    (which can be satisfied by simply setting the initial values of all states to zero).
* What is needed is an optimal partial policy,
  meaning a policy that is optimal for the relevant states but
  can specify arbitrary actions, or even be undefined for the irrelevant states

## 8.8 Planning at Decision Time
* Planning can be used in at least 2 ways
  * background planning:
    * to use planning to gradually improve a policy or value function on
      the basis of simulated experience obtained from a model
    * Selecting actions is then a matter of comparing
      the current state’s action values obtained from a table in the tabular case, or
      by evaluating a mathematical expression in the approximate methods
    * not focussed on the current state
  * decision time planning:
    * to begin and complete planning after encountering each new state,
      as a computation whose output is the selection of a single action
    * can look much deeper than one-step-ahead and
      evaluate action choices leading to many different predicted state and reward trajectories.
    * focuses on a particular (current) state.
      * so much so that the values and policy created by the planning process are
        typically discarded after being used to select the current action.
        (there are very many states and we are unlikely to return to the same state for a long time)
    * is most useful in applications in which fast responses are not required,
      eg chess playing programs,
* one may want to do a mix of both:
  * focus planning on the current state and
    store the results of planning so as to be that much farther along should
    one return to the same state later.

# 8.9 Heuristic Search
*  In heuristic search,
  * for each state encountered, a large tree of possible continuations is considered.
  * The approximate value function is applied to the leaf nodes and
    then backed up toward the current state at the root.
  * The backing up stops at the state–action nodes for the current state.
  * Once the backed-up values of these nodes are computed, the best of them is chosen as the current action, and
    then all backed-up values are discarded.
* heuristic search can be viewed as an extension of the idea of a greedy policy beyond a single step
  * searching deeper than one step is to obtain better action selections
* Much of the effectiveness of heuristic search is due to
  * its search tree being tightly focused on the states and actions that
    might immediately follow the current state.

## 8.10 Rollout Algorithms
* Rollout algorithms
  * are decision-time planning algorithms based on Monte Carlo control applied to
    simulated trajectories that all begin at the current environment state.
  * estimate action values for a given policy by averaging the returns of many simulated
    trajectories that start with each possible action and then follow the given policy.
  * goal:
    * produce Monte Carlo estimates of action values only for each current state and
      for a given policy usually called the rollout policy.
      (to improve upon the rollout policy; not to find an optimal policy. )
    * not to estimate a complete optimal action-value function, q∗, or
      a complete action-value function for a given policy
* not ordinarily think of rollout algorithms as learning algorithms because
  they do not maintain long-term memories of values or policies.

## 8.11 Monte Carlo Tree Search
* MCTS:
  * is a rollout algorithm, but
    enhanced by the addition of a means for accumulating value estimates obtained from the
    Monte Carlo simulations in order to successively direct simulations toward more highly-
    rewarding trajectories.
  * is a decision-time planning algorithm based on Monte Carlo control applied to
    simulations that start from the root state;
  * is executed after encountering each new state to select the agent’s action for that state;
  * each execution is an iterative process that simulates many trajectories
    starting from the current state and running to a terminal state (or until discounting
    makes any further reward negligible as a contribution to the return).
  * benefits from
    online, incremental, sample-based value estimation and policy improvement
  * avoids the problem of globally approximating an action-value function while
    it retains the benefit of using past experience to guide exploration.
  * focusing the Monte Carlo trials on trajectories whose initial segments are
    common to high-return trajectories previously simulated.
* idea
  * to successively focus multiple simulations starting at the current state by
    extending the initial portions of trajectories that have received high evaluations from
    earlier simulations
* policy:
  * tree policy
    * e.g eps-greedy or UCB selection rule
  * rollout policy
* 4 steps as illustrated in Figure 8.10:
  * Selection.
    * Starting at the root node, a tree policy based on the action values
      attached to the edges of the tree traverses the tree to select a leaf node.
  * Expansion.
    * On some iterations (depending on details of the application), the tree
      is expanded from the selected leaf node by adding one or more child nodes reached
      from the selected node via unexplored actions.
  * Simulation.
    * From the selected node, or from one of its newly-added child nodes (if any),
      simulation of a complete episode is run with actions selected by the rollout
      policy.
    * The result is a Monte Carlo trial with actions selected first by the tree
      policy and beyond the tree by the rollout policy.
  * Backup.
    * The return generated by the simulated episode is backed up to update, or to initialize,
      the action values attached to the edges of the tree traversed by the tree policy in this iteration of MCTS.
    * No values are saved for the states and actions visited by the rollout policy beyond the tree.
