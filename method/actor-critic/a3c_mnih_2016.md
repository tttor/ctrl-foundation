# Asynchronous Methods for Deep Reinforcement Learning
33rd International Conference on Machine Learning, New York, NY, USA, 2016

## idea: A3C
* framework for deep reinforcement learning that uses asynchronous gradient descent for
  optimization of deep neural network controllers.

## setup
* Atari domain

## result
* The best performing method, **an asynchronous variant of actor-critic**, surpasses
  the current state-of-the-art on the Atari domain while training for
  half the time on **a single multi-core CPU** instead of a GPU.
* using parallel actorlearners to update a shared model had
  a stabilizing effect on the learning process of the three value-based methods
