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

## 4. Integrating Monte Carlo Tree Search and Reinforcement Learning
### 4.1 A Representation Policy for Reinforcement Learning
* RL theory offers a rich description of the MCTS backpropagation phase, whereas 
  MCTS introduces into RL the distinction between a memorized and non-memorized part of the state space.
### 4.2 Assumptions About Playout Estimates
### 4.3 The Temporal-Difference Tree Search Framework
* Traditional RL methods can benefit from several MCTS-inspired mechanics, implemented by the TDTS framework, such as incremental representations, ingenuous generalizations (MCTS enhance- ments) of the state space that is not memorized in the main representation, and strong heuristic con- trol policies (especially for the playout phase)
* what MCTS methods do – 
  * for the states near the root they store all the information (in a tabular tree representation) with high accuracy, 
  * but for the (usually) vast state space visited in the playouts they either omit the estimates or 
    apply low-accuracy generalization methods that estimate the states that are not memorized in the tree
* Gelly and Silver (2007) describe the UCT algorithm as “a value-based reinforcement-learning algorithm that focusses exclusively on the start state and the tree of subsequent states”
