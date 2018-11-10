# 3: Finite Markov Decision Processes

# 3.1 The Agent–Environment Interface
* emphasizes that the next reward and next state, Rt+1 and St+1, are jointly determined

# 3.2
* In particular, the reward signal is not the place to impart to the agent prior knowledge
  about how to achieve what we want it to do.
  * Better places for imparting this kind of prior knowledge are the initial policy or initial
    value function, or in influences on these.

# 3.3 Returns and Episodes
* episodic vs continuing tasks
  * in episodic task:
    * agent–environment interaction breaks naturally into subsequences, which we call episodes
  * in continuing task:
    * the agent–environment interaction does not break
      naturally into identifiable episodes, but goes on continually without limit

# 3.4 Unified Notation for Episodic and Continuing Tasks
* the special absorbing state corresponds to the end of an episode.

# 3.5 Policies and Value Functions

* Reinforcement learning methods specify how the agent’s policy is changed as a result of
its experience.

# 3.7
The online nature of reinforcement learning makes it possible to approximate
optimal policies in ways that put more e↵ort into learning to make good decisions for
frequently encountered states, at the expense of less e↵ort for infrequently encountered
states. This is one key property that distinguishes reinforcement learning from other
approaches to approximately solving MDPs.
