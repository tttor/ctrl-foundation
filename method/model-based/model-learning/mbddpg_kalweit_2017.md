# Uncertainty-driven Imagination for Continuous Deep Reinforcement Learning
* Gabriel Kalweit, Joschka Boedecker
* corl2017

## problem
* high sample complexity of the Deep Deterministic Policy Gradient (DDPG)

## idea: Model-assisted Bootstrapped DDPG
* a method to reduce system interaction through synthetic data when
  appropriate to achieve this balance
* To counteract adverse effects of inaccurate artificial data,
  the uncertainty of the agent is measured and incorporated to
  limit training on the generated data set.

## result
* contrib
  * that a massive increase of updates per step does lead to stability issues in DDPG.
  * extend the replay memory of DDPG by artificial transitions from a neural model and
    show that this leads to a much smaller demand for real-world transitions.
  * extend the critic to a bootstrapped neural network, so as to
    limit articifial data usage for high uncertainty.
* future work
  * instead of setting a fixed rollout-length,
    the augmentation depth and model usage should be limited by model-error.
  *  The effect of mixed minibatches, instead of distinct real and imaginary,

## background
* NAF:
  * not able to apply neural models successfully and used locally linear models.
    * Whereas locally linear models are very efficient to learn, these models
      lack in expressiveness and do not generalize as well as neural models.
  * the model had to be switched off after a certain amount of episodes, since
    further training on artificial samples led to performance decrease.

<!--
T. Lampe and M. Riedmiller. Approximate model-assisted neural fitted q-iteration. In Neural
Networks (IJCNN), 2014 International Joint Conference on, pages 2698–2704. IEEE, 2014.

S. Gu, T. P. Lillicrap, I. Sutskever, and S. Levine. Continuous deep q-learning with model-
based acceleration. pages 2829–2838, 2016.

T. Weber, S. Racanière, D. P. Reichert, L. Buesing, A. Guez, D. J. Rezende, A. P. Badia,
O. Vinyals, N. Heess, Y. Li, et al. Imagination-augmented agents for deep reinforcement
learning. arXiv preprint arXiv:1707.06203, 2017.
 -->
