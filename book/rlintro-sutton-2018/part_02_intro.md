# part_02_intro.md
to extend the tabular methods presented in the first part
* to apply to problems with arbitrarily large state spaces,
* to find a good approximate solution using limited computational resources.

problem with large state spaces
* the memory needed for large tables,
* the time and data needed to fill them accurately.
* almost every state encountered will never have been seen before;
  requiring generalization capability:
  * function approximation
    because it takes examples from a desired function (e.g., a value function) and attempts
    to generalize from them to construct an approximation of the entire function.
  * Function approximation is an instance of supervised learning,

Reinforcement learning with function approximation involves a number of new issues
(that do not normally arise in conventional supervised learning,) such as
* nonstationarity,
* bootstrapping, and
* delayed targets.

policy-gradient methods,
* which approximate the optimal policy directly and need never form an approximate value function
* (although they may be much more efficient if they do approximate a value function as well the policy).
