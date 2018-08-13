# Variance Reduction for Policy Gradient with Action-Dependent Factorized Baselines
* Cathy Wu, Aravind Rajeswaran, Yan Duan, Vikash Kumar, Alexandre M Bayen, Sham Kakade, Igor Mordatch, Pieter Abbeel
* iclr2018: oral
* https://openreview.net/forum?id=H1tSsb-AW
* https://sites.google.com/view/ad-baselines
* https://www.youtube.com/watch?v=3PhtXeM90to
* https://vimeo.com/252186180

## problem
* high variance of gradient estimates.
  * exasperated in problems with long horizons or high-dimensional action spaces
  
## idea
* derive a bias-free **action-dependent** baseline for variance reduction 
  * which fully exploits the structural form of the stochastic policy itself

## result
* action-dependent baselines consistently improve the performance compared to baselines that use only state information 
  * relative performance gain is task-specific, 
  * but in certain tasks, we observe significant speed-up in the learning process
  
## background
* like Q-Prop (Gu et al.,2017) make use of an action-dependent control variate, a technique commonly used in Monte Carlo
methods and recently adopted for RL. Since Q-Prop utilizes off-policy data, it has the potential to
be more sample efficient than pure on-policy methods. However, Q-prop is significantly more com-
putationally expensive, since it needs to perform a large number of gradient updates on the critic
using the off-policy data, thus not suitable with fast simulators. 

## comment
* need to factor actions
* (-) no cmp with eg PPO
* (?) no code?

