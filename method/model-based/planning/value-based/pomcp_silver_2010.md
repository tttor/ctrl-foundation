# POMCP: Partially Observable Monte Carlo Planning
* David Silver; Joel Veness
* nips2010
* https://papers.nips.cc/paper/4031-monte-carlo-planning-in-large-pomdps

## idea: pomcp
* POMCP consists of 
  * UCT search that selects action at each time step and
  * a particle filter that updates the agent's belief state.
* POMCP extends MCTS to partially observable environments.

## background
* mcts: to evaluate each state in a search tree by the average outcome of simulations from that state.
  * It is a highly selective, best-first search that quickly focuses on the most promising regions of the search space. 
  * It breaks the curse of dimensionality by sampling state transitions instead of considering all possible state transitions. 
  * It only requires a black box simulator, and 
    can be applied in problems that are too large or too complex to represent with explicit probability distributions. 
  * It uses random simulations to estimate the potential for long-term reward, so that it plans over large horizons, and 
    is often effective without any search heuristics or prior domain knowledge [8]. 
    If exploration is controlled appropriately then MCTS converges to the optimal policy. 
  * it is anytime, computationally efficient, and highly parallelisable.
  
## comment
* pomcp is for discrete actions
  * "large pomdp" here means large state spaces
* POMCP brings monte-carlo method (which is model-free technique in RL lit) to planning
