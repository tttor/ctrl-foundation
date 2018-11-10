# Sample-based Learning and Search with Permanent and Transient Memories
* icml2008

## problem
* Reinforcement learning is often considered a slow procedure.
  * Outstanding examples of success have, in the past, learned a value function from months of offline computation.

## observation
* Many reinforcement learning methods are fast, incremental, and scalable.
  * When such a reinforcement learning algorithm is applied to simulated experience, using a transient memory,
  it becomes a high performance search algorithm.
    * This search procedure can be made more efficient by generalising across states; and
    * it can be combined with long-term learning, using a permanent memory

## idea: Dyna-2
* Dyna-2 architecture can be summarised as Dyna with
  * Sarsa updates,
  * permanent and transient memories, and
  * linear function approximation
* a memory is defined as:
  * a set of **features** and **corresponding parameters** used by an agent **to estimate the value function**.
* maintains two distinct memories:
  * **a permanent memory**: updated during sample-based learning,
   from the learning distribution and converges on the best overall representation of the value function,
   based on the agent’s past experience.
  * **a transient memory**: updated during sample-based search (planning),
    from the search distribution and tracks the local nuances of the value function,
    based on the agent’s expected future experience.
* The value function is
  * a linear combination of the transient and permanent memories,
  such that the transient memory tracks a local correction to the permanent memory:
    * $\bar{Q}(s,a) = \phi(s,a)^T \theta + \bar{\phi}(s,a)^T \bar{\theta}$

## setup
* 9×9 Computer Go
* a million binary features in the function approximator, based on
templates matching small fragments of the board.

## result
* Using only the transient memory, Dyna-2 performed at least as well as UCT.
* Using both memories combined, it significantly outperformed UCT.

## misc
* spectrum of sample-based search algorithms:
  * from table-lookup to function approximation;
  * from Monte-Carlo learning to bootstrapping; and
  * from permanent to transient memories
* Sample-based planning applies sample-based reinforcement learning methods to simulated experience, e.g. via MCTS-based UCT
* The Dyna architecture (Sutton, 1990) combines sample-based learning with sample-based planning.
