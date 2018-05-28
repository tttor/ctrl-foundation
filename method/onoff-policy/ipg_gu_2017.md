ipg_gu_2017.md
# Interpolated Policy Gradient: Merging On-Policy and Off-Policy Gradient Estimation for Deep Reinforcement Learning
* Shixiang Gu et al

## problem
* to merging on- and off-policy updates for deep reinforcement learning

## idea
*  interpolated policy gradient methods, a family of policy gradient
algorithms that allow mixing off-policy learning with on-policy learning while satisfying performance
bounds

## result
*  interpolated gradients have improved
sample-efficiency and stability over the prior state-of-the-art methods, and the theoretical results
provide intuition for analyzing the cases in which the different methods perform well or poorly
*  off-policy updates with a value function estimator can be interpolated
with on-policy policy gradient updates whilst still satisfying performance bounds.
