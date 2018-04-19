# Mastering the game of Go with deep neural networks and tree search
* David Silver et al
* https://www.nature.com/articles/nature16961
* NATURE, 28 JAN 2016

## observation
* the depth of the search may be reduced by position evaluation: 
  * truncating the search tree at state s and 
  * replacing the subtree below s by an approximate value function v(s) ≈ v*(s) that 
    predicts the outcome from state s. 
* the breadth of the search may be reduced by sampling actions from a policy p(a|s) that is 
  a probability distribution over possible moves a in position s. 
  * For example, Monte Carlo rollouts search to maximum depth without branching at all, 
    by sampling long sequences of actions for both players from a policy p.

## idea
* uses 
  * value networks to evaluate board positions and 
  * policy networks to select moves (sampling actions)
  * (combines) Monte Carlo simulation (MCTS) with value and policy networks.
    (a combination of **deep neural networks** and **tree search**)
* train deep neural networks by a novel combination of 
  * supervised learning from human expert games, and 
  * reinforcement learning from games of self-play
* pipeline
  * train a supervised learning (SL) policy network `p_{\sigma}` directly from expert human moves. 
    * that provides fast, efficient learning updates with immediate feedback and high-quality gradients. 
  * train a fast policy `p_{\pi}` 
    * that can rapidly sample actions during rollouts. 
  * train a reinforcement learning (RL) policy network `p_{\rho}` 
    * that improves the SL policy network by optimizing the final outcome of games of self-play. 
    * that adjusts the policy towards the correct goal of winning games, rather than maximizing predictive accuracy. 
  * train a value network `v_{\theta}` 
    * that predicts the winner of games played by the RL policy network against itself

## setup
* pass in the board position as a 19 × 19 image and 
  use convolutional layers to construct a representation of the position.

## result
* During the match against Fan Hui, AlphaGo evaluated thousands
  of times **fewer positions** than Deep Blue did in its chess match against Kasparov
* AlphaGo has finally reached a professional level in Go

## misc
* `b^d` possible sequences of moves, where 
  `b` is the game’s breadth (number of legal moves per position) and 
  `d` is its depth (game length). 
  * chess (`b ~ 35`, `d ~ 80`) 
  * Go (`b ~ 250`, `d ~ 150`)
  
