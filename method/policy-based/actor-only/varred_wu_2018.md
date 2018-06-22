# Variance Reduction for Policy Gradient with Action-Dependent Factorized Baselines
* Cathy Wu, Aravind Rajeswaran, Yan Duan, Vikash Kumar, Alexandre M Bayen, Sham Kakade, Igor Mordatch, Pieter Abbeel
* iclr2018: oral
* https://openreview.net/forum?id=H1tSsb-AW

## problem
* high variance of gradient estimates.
  * exasperated in problems with long horizons or high-dimensional action spaces
  
## idea
* derive a bias-free **action-dependent** baseline for variance reduction 
  * which fully exploits the structural form of the stochastic policy itself
