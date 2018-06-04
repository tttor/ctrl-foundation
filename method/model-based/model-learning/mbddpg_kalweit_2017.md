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
