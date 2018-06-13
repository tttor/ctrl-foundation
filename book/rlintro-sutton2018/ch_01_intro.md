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
