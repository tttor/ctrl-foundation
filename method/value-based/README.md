# value-based

## Q-learning (Watkins, 1989)
* as off-policy TD Control
* is guaranteed to converge to the optimal policy for the tabular (non-approximate) case,
* may diverge when using linear function approximation (Baird, 1995).

### variant
* multi-step Q-learning
  * (-) theoretical justification is lacking, since
    rewards received after a non-optimal action no longer relate to the hard-max Q-values
* Deep Q-network (DQN)
  * (-) suffers from potentially slowlearning caused by single-step temporal difference updates,
  * variants:
    * double Q-learning with prioritized experience replay
    * Rainbow: https://arxiv.org/abs/1710.02298
* NAF: Continuous Deep Q-Learning with Model-based Acceleration

## others
* SARSA (Rummery & Niranjan, 1994)

## tutor
* https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/03_Q_learning_cartpole.py
* https://github.com/darksigma/Fundamentals-of-Deep-Learning-Book/blob/master/fdl_examples/chapter9/dqn.py
* https://ai.intel.com/demystifying-deep-reinforcement-learning/
* https://github.com/devsisters/DQN-tensorflow
* http://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
