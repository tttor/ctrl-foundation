# Deep Reinforcement Learning that Matters
https://arxiv.org/abs/1709.06560

## Intro
* focus on model-free policy-gradient for continuous control

## Problem
* reproducing deep RL results is seldom straightforward

## Factors affecting the reproducibility
* hyperparameters
  * the range consideres when tuning the hyperparams
* network architecture
  * e.g. ReLU, Leaky ReLU
  * suggest that the network arch is part of the algorithm methodology
* reward scale
* random seeds and number of trials
  * the variance in results due to environment stochasticity or stochasticity in the learning process 
    (e.g. random weight initialization). 
    * As such, even averaging several learning results together across totally different random seeds can lead to 
      the reporting of misleading results.
  * the variance between runs is enough to create statistically different distributions just from varying random seeds
    * report only the top-N trials from among several trials can be misleading
  * good to have: number of trials specified as a recommendation
* environment
  * to show not only **returns** but also **demonstrations** of the learned policy in action.
* codebases
  * the necessity
    * that implementation details be enumerated, codebases packaged with publications, and 
    * that performance of baseline experiments in novel works matches the original baseline publication code
