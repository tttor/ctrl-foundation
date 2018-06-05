# On Monte Carlo Tree Search and Reinforcement Learning

## 3: The Connection Between Monte Carlo Tree Search and Reinforcement Learning 
* The key difference is the source of experience: 
  whether it comes from real interaction with the environment (in learning) or from simulated interaction (in planning)
* This im- plies that any learning method can be used for planning, when applied to a simulated environment. 
* Thereafter, given that MCTS is regarded as a search and planning method, its search mechanics are comparable with those of sample-based RL methods, and the overall MCTS framework is compa- rable with RL applied to planning.
* In RL, trajectories are guided by a control policy, which dictates what actions will be performed, and, 
  consequently, which states will be visited. It encompasses the MCTS’s tree policy and default policy. 
* From an RL point of view, an agent might be acting using one or two control policies. 
In on-policy control the agent is evaluating and simultaneously improving the exact policy that it follows. 
Con- versely, in off-policy control, the agent is following one policy, but may be evaluating another – it is following a behaviour policy while evaluating a target policy (Sutton & Barto, 2017).
* Summing the above, the search mechanics ofMCTSare comparable to those of Monte Carlo control (and to TD control with λ = 1).

### 3.3 The Differences: The Novelties of Monte Carlo Tree Search
* the key difference between these two classes of methods, to the aspects of MCTS that we have not linked with RL yet:
  **the MCTS concepts of playout and expansion.**
* Silver et al. (2012) explicitly noted that 
> once all states have been visited and added into the search tree, 
  Monte-Carlo tree search is equivalent to Monte-Carlo control using table lookup
* two main memorization approaches when solving tasks where it is infeasible to directly memorize the whole state space due to its size: 
  * (1) describing the whole state space by approximation, or 
  * (2) keeping in memory only a part of the state space at once.
* MCTS are usually tabular, but memorize only the part of the state space that is considered most relevant.
  * This relevancy is sometimes defined with heuristic criteria, but 
    most often it is directly entrusted to the selection policy – 
    * an MCTS method usually expects that its tree policy will guide the exploration towards 
      the most relevant part of the state space, which should as such be worth memorizing.
