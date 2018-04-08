# NIPS 2015 Workshop Deep Reinforcement Learning

## (Mnih) 15492 Asynch RL
* training neural networks using a planner (Guo et al 2014)
* visual deep rl
  * video input, delayed reward
  * exploration, the input distrib can be highly non-stationary
* DQN is computationally expensive
  * Gorilla: massively distributed DQN
    * training over multiple machine
* asynch-RL
  * parallel actor learner using cpu treads
  * online hogwild for asych updates
  * no replay, but paralel actor learners
  * choise of rl: on/off policy, value/policy based
* pong, breakout, montezuma revenge, torch
