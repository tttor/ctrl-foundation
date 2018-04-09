# Mastering the game of Go with deep neural networks and tree search
* David Silver et al
* doi:10.1038/nature16961
* NATURE, 28 JAN 2016

## idea
* uses 
  * value networks to evaluate board positions and 
  * policy networks to select moves.
  * (combines) Monte Carlo simulation with value and policy networks.
    (a combination of **deep neural networks** and **tree search**)
* train deep neural networks by a novel combination of 
  * supervised learning from human expert games, and 
  * reinforcement learning from games of self-play

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
  
