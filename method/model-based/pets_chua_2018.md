# Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models
* Kurtland Chua et al
* https://arxiv.org/abs/1805.12114
* https://sites.google.com/view/drl-in-a-handful-of-trials

## problem
* gap in asymptotic performance between model-based and model-free RL
  * Model-based reinforcement learning (RL) algorithms can attain excellent sample efficiency, 
    * but often lag behind the best model-free algorithms in terms of asymptotic performance, 
      especially those with high-capacity parametric function approximators, such as deep networks. 
    
## idea: probabilistic ensembles with trajectory sampling (PETS) 
* combines uncertainty-aware deep network dynamics models with sampling-based uncertainty propagation.
* incorporating uncertainty estimation into the model learning process

## result
* our approach matches the asymptotic performance of model-free algorithms on several challenging benchmark tasks, while 
  requiring significantly fewer samples 
  * (e.g. 25 and 125 times fewer samples than Soft Actor Critic and Proximal Policy Optimization respectively on the half-cheetah task).
*  model-based reinforcement learning with neural
network dynamics models can achieve results that are competitive not only with Bayesian nonpara-
metric models such as GPs, but also on par with model-free algorithms such as PPO and SAC in
terms of asymptotic performance, while attaining substantially more efficient convergence
