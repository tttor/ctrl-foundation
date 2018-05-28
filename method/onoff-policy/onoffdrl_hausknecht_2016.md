# On-Policy vs. Off-Policy Updates for Deep Reinforcement Learning
* Matthew Hausknecht and Peter Stone
* Deep Reinforcement Learning: Frontiers and Challenges, IJCAI 2016 Workshop


## result
* for the DDPG algorithm in a continuous
  action space, mixing on-policy and off-policy
  update targets exhibits superior performance and
  stability compared to using exclusively one or the other.
  * The same technique applied to DQN
    in a discrete action space drastically slows down learning

## background
* Like TD methods, Monte
  Carlo methods also learn online directly from experience.
  However, unlike TD-methods, Monte Carlo methods do not
  bootstrap value estimates and instead learn directly from re-
  turns.
* sOn-policy MC employs on-
  policy updates without any bootstrapping, while Q-Learning
  uses off-policy updates with bootstrapping.
