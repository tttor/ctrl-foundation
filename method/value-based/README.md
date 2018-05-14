# value-based

## Deep Q-network (DQN)
* pros and cons
  * (-) suffers from potentially slowlearning caused by single-step temporal difference updates,

* variants:
  * Rainbow: https://arxiv.org/abs/1710.02298
  * Double Q-learning
  * Prioritized Dueling DQN (Wang et al., 2017)
  * NAF: Continuous Deep Q-Learning with Model-based Acceleration

## Q-learning (Watkins, 1989)
* as off-policy TD Control
* is guaranteed to converge to the optimal policy for the tabular (non-approximate) case,
* may diverge when using linear function approximation (Baird, 1995).

## others
* SARSA (Rummery & Niranjan, 1994)
* multi-step Q-learning
  * (-) theoretical justification is lacking, since
        rewards received after a non-optimal action no longer relate to the hard-max Q-values

## tutor
* https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/03_Q_learning_cartpole.py
* https://github.com/darksigma/Fundamentals-of-Deep-Learning-Book/blob/master/fdl_examples/chapter9/dqn.py
* https://ai.intel.com/demystifying-deep-reinforcement-learning/
* https://github.com/devsisters/DQN-tensorflow
* http://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
