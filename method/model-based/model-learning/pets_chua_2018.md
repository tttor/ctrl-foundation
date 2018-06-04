# Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models
* Kurtland Chua et al
* https://arxiv.org/abs/1805.12114
* https://sites.google.com/view/drl-in-a-handful-of-trials

## problem
* gap in asymptotic performance between model-based and model-free RL
  * Model-based reinforcement learning (RL) algorithms can attain excellent sample efficiency, 
    * but often lag behind the best model-free algorithms in terms of asymptotic performance,
      (tend to converge to more suboptimal solutions)
      especially those with high-capacity parametric function approximators, such as deep networks. 
* current model-free reinforcement learning algorithms are quite expensive to train
* NN struggle with the opposite problem: in the low-data regime in which MBRL always starts, 
  * they tend to overfit and make poor predictions far into the future. 

## observation
* A promising direction to reducing sample complexity is to explore model-based reinforcement learning (MBRL) methods,
  * which proceed by first acquiring a predictive model of the world, and then using that model to make decisions
  * the dynamics model is reward-independent and therefore can generalize to new tasks in the same environment, and 
  * can easily benefit from all of the advances in deep supervised learning to utilize high-capacity models.
*  model capacity is a critical ingredient in the success of MBRL methods: 
  * while efficient models such as Gaussian processes can learn extremely quickly,
    they struggle to represent very complex and discontinuous dynamical systems 

## idea: probabilistic ensembles with trajectory sampling (PETS) 
* combines uncertainty-aware deep network dynamics models with sampling-based uncertainty propagation.
* incorporating uncertainty estimation into the model learning process
* use high-capacity NN models that incorporate uncertainty via an ensemble of bootstrapped models, 
 where each model encodes distributions (opposed to point predictions),
* Our trajectory sampling (TS) propagation technique 
  * uses our dynamics model to re-sample each particle (with associated bootstrap) according to its probabilistic prediction
at each point in time, up until MPC-horizon
* Planning via Model Predictive Control:
  *  recompute at each time-step and applies the first action of each action sequence, up until the task-horizon

## result
* our approach matches the asymptotic performance of model-free algorithms on several challenging benchmark tasks, while 
  requiring significantly fewer samples 
  * (e.g. 25 and 125 times fewer samples than Soft Actor Critic and Proximal Policy Optimization respectively on the half-cheetah task).
*  model-based reinforcement learning with neural
network dynamics models can achieve results that are competitive not only with Bayesian nonpara-
metric models such as GPs, but also on par with model-free algorithms such as PPO and SAC in
terms of asymptotic performance, while attaining substantially more efficient convergence
