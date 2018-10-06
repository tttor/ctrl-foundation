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

## Q-learning for continuous actions
* Gu, Shixiang, Lillicrap, Timothy, Sutskever, Ilya, and Levine, Sergey. 
  Continuous deep q-learning with model-based acceleration. 
  In International Conference on Ma- chine Learning, pp. 2829–2838, 2016.
* Metz, Luke, Ibarz, Julian, Jaitly, Navdeep, and Davidson, James. 
  Discrete sequential prediction of continuous actions for deep rl. 
  arXiv preprint arXiv:1705.05035, 2017
* Tavakoli, Arash, Pardo, Fabio, and Kormushev, Petar. 
  Action branching architectures for deep reinforcement learning. 
  arXiv preprint arXiv:1711.08946, 2017.

## others
* SARSA (Rummery & Niranjan, 1994)
* multi-step Q-learning
  * (-) theoretical justification is lacking, since
        rewards received after a non-optimal action no longer relate to the hard-max Q-values
* LSPI, LSTD
  * Finite-Sample Analysis of Least-Squares Policy Iteration, Alessandro Lazaric
  * Least-Squares Policy Iteration, Michail G. Lagoudakis

## tutor
* https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/03_Q_learning_cartpole.py
* https://github.com/darksigma/Fundamentals-of-Deep-Learning-Book/blob/master/fdl_examples/chapter9/dqn.py
* https://ai.intel.com/demystifying-deep-reinforcement-learning/
* https://github.com/devsisters/DQN-tensorflow
* http://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
