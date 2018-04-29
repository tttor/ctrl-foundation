# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor
* Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel & Sergey Levine
* 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.
* https://github.com/haarnoja/sac
* https://arxiv.org/abs/1801.01290

## problem
* model-free RL
  * very high sample complexity
  * brittle convergence properties,
    which necessitate meticulous hyperparameter tuning;
    hyperparameters: learning rates, exploration constants

## observation
* One cause for the poor sample efficiency of deep RL methods is on-policy learning
  * eg TRPO, A3C require new samples to be collected for each gradient step on the policy
* Off-policy algorithms
  * aim to reuse past experience.
  * not directly feasible with conventional policy gradient formulations
    * but is relatively straightforward for Q-learning based methods
  * the combination of off-policy learning and high-dimensional,
    nonlinear function approximation with neural networks presents
    a major challenge for stability and convergence
* deep deterministic policy gradient (DDPG)
  * provide sample-efficient learning,
  * but extreme brittleness and hyperparameter sensitivity
* the maximum entropy formulation
  * provides a substantial improvement in exploration and robustness:
  * robust in the face of modeling and estimation errors,
    * improve exploration by acquiring diverse behaviors.
* previously proposed maximum entropy methods generally do not exceed
  the performance of state-of-the-art off-policy algorithms, such as DDPG, when learning from scratch,
  * though they may have other benefits, such as improved exploration and ease of finetuning.

## idea: soft actor-critic (SAC)
* soft actor-critic,
  an off-policy actor-critic deep RL algorithm based on
  the maximum entropy reinforcement learning framework.
* the actor aims to
  * maximize expected reward while also
  * maximizing entropy
  * that is, succeed at the task while acting as randomly as possible.
* incorporates three key ingredients:
  * an actor-critic architecture with eparate policy and value function networks,
  * an off-policy formulation that enables reuse of previously collected data for efficiency, and
  * entropy maximization to enable stability and exploration.
* combines off-policy actor-critic training with a stochastic actor, and
  further aims to maximize the entropy of this actor with an entropy maximization objective.

## result
* SAC:
  * provides sample-efficient learning while
  * retaining the benefits of entropy maximization and stability
* soft policy iteration converge to the optimal policy (present a convergence proof)
* outperforms state-of-the-art model-free deep RL methods,
  * including the off-policy DDPG algorithm and the on-policy TRPO algorithm.
* stochastic, entropy maximizing reinforcement learning algorithms can provide
  a promising avenue for improved robustness and stability,

## misc
* popular off-policy actor-critic variant is based on the deterministic
  policy gradient (Silver et al., 2014) and its deep counterpart, DDPG
  * uses a Q-function estimator to enable off-policy learning, and
    a deterministic actor that maximizes this Q-function.
  * difficult to stabilize and brittle to hyperparameter settings
* Maximum entropy reinforcement learning optimizes policies to maximize both
  * the expected return and
  * the expected entropy of the policy.

## comment
* note that a2c implementation in openai baseline uses the idea of maximum entropy
* actor-critic as the core of dyna full rl loop?
  * actor: learn via direct RL
  * critic: learn via indirect RL: planning + model learning

<!--
B. O’Donoghue, R. Munos, K. Kavukcuoglu, and V. Mnih. PGQ: Combining policy gradient and
Q-learning. arXiv preprint arXiv:1611.01626, 2016.

J. Schulman, P. Abbeel, and X. Chen. Equivalence between policy gradients and soft Q-learning.
arXiv preprint arXiv:1704.06440, 2017.

 -->
