# Sample efficient actor-critic with experience replay
* ZiyuWang et al
* iclr2017: poster
* https://arxiv.org/abs/1611.01224
* https://openreview.net/forum?id=HyM25Mqel
* https://github.com/openai/baselines/tree/master/baselines/acer

## idea: acer
* with experience replay, off-policy
* innovations
  * truncated importance sampling with bias correction, 
  * stochastic dueling network architectures, and 
  * a new trust region policy optimization method.

## setup
* task
  * discrete 57-game Atari domain
  * mujoco: cartpole (1D), reacher (3D), cheetah (6D), fish (5D), walker (6D) and humanoid (21D).
* baseline
  * A3C and Trust-A3C.
  * Trust-TIS and TIS (truncated importance sampling)
* show the mean and standard deviation of the best 5 out of 30 hyper-parameter settings 

## result
* ACER > A3C (in continuous control)
* acer: stable, sample efficient
* trust region optimization method can result in huge improvements over the baselines
* Retrace and off- policy correction, SDNs, and trust region are critical
