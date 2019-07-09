# survey, benchmark, review

## paper
* [2019: Wang: Benchmarking Model-Based Reinforcement Learning](?)
* [2018: Busonio: Reinforcement learning for control: Performance, stability, and deep approximators](?)
* [2018: Mahmood: Benchmarking Reinforcement Learning Algorithms on Real-World Robots](https://arxiv.org/abs/1809.07731)
* [2018: Colas: How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments](https://arxiv.org/abs/1806.08295)
* [2018: Recht: A Tour of Reinforcement Learning: The View from Continuous Control](https://arxiv.org/abs/1806.09460)
* [2018: Sigaud: Policy Search in Continuous Action Domains: an Overview](https://arxiv.org/abs/1803.04706)
* [2017: Machado: Revisiting the ALE: Evaluation Protocols and Open Problems for General Agents](https://arxiv.org/abs/1709.06009)
* [2017: Vodopivec: On Monte Carlo Tree Search and Reinforcement Learning](https://www.jair.org/media/5507/live-5507-10333-jair.pdf)
* [2017: Henderson: Deep Reinforcement Learning that Matters](https://arxiv.org/abs/1709.06560)
* [2017: Polydoros: Survey of Model-Based Reinforcement Learning: Applications on Robotics](https://link.springer.com/article/10.1007/s10846-017-0468-y)
* [2017: Arulkumaran: Deep Reinforcement Learning: A Brief Survey](http://ieeexplore.ieee.org/document/8103164/)
* [2017: Gorges: Relations between Model Predictive Control and Reinforcement Learning](https://www.sciencedirect.com/science/article/pii/S2405896317311941)
* [2016: Duan: Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778)
* [2016: Castronovo: Benchmarking for Bayesian Reinforcement Learning](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0157088)
* [2015: Garcia: A Comprehensive Survey on Safe Reinforcement Learning](http://jmlr.org/papers/v16/garcia15a.html)
* [2015: Ghavamzadeh: Bayesian Reinforcement Learning: A Survey](https://arxiv.org/abs/1609.04436)
* [2014: Mayne: Model predictive control: Recent developments and future promise](https://www.sciencedirect.com/science/article/pii/S0005109814005160)
* [2013: Kober: Reinforcement learning in robotics: A survey](http://journals.sagepub.com/doi/abs/10.1177/0278364913495721)
* [2013: Deisenroth: A Survey on Policy Search for Robotics](https://spiral.imperial.ac.uk/bitstream/10044/1/12051/7/fnt_corrected_2014-8-22.pdf)
* [2012: Grondman: A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients](http://ieeexplore.ieee.org/abstract/document/6392457/)
* [2012: Browne: A Survey of Monte Carlo Tree Search Methods](https://ieeexplore.ieee.org/document/6145622/)
* [2011: Nguyen-Tuong: Model learning for robot control: a survey](https://link.springer.com/article/10.1007/s10339-011-0404-1)
* [2009: Taylor: Transfer Learning for Reinforcement Learning Domains: A Survey](http://www.jmlr.org/papers/v10/taylor09a.html)
* [2009: Mahadevan: Learning Representation and Control in Markov Decision Processes: New Frontiers](?)
* [2008: Ross: Online planning algorithms for POMDPs](http://www.jair.org/papers/paper2567.html)
* [2008: Partalas: Reinforcement learning and automated planning: a survey](https://www.igi-global.com/chapter/reinforcement-learning-automated-planning/5322)
* [2004: Greensmith: Variance Reduction Techniques for Gradient Estimates in Reinforcement Learning](?)
* [2003: Barto: Recent Advances in Hierarchical Reinforcement Learning](https://link.springer.com/article/10.1023/A:1022140919877)
* [2000: Hauskreht: Value-Funtion Approximations for Partially Observable Markov Deision Processes](https://www.jair.org/media/678/live-678-1858-jair.pdf)
* [1998: Kaebling: Planning and acting in partially observable stochastic domains](https://www.sciencedirect.com/science/article/pii/S000437029800023X)
* [1996: Kaebling: Reinforcement Learning: A Survey](https://www.jair.org/media/301/live-301-1562-jair.pdf)
* [1996: Mahadevan: Average Reward Reinforcement Learning: Foundations, Algorithms, and Empirical Results](?)

## (rough) dimensions of challenges:
* MDP (fully observable states) _...to..._ POMDP (partially observable states) model/formulations
* stationary (fixed) _...to..._ non-stationary (changing) models
* short _...to..._ long planning horizon
* simulated (kinematic) _...to..._ real (dynamic,physics-intensive) evaluation/robot/world
* noObstacle _...to..._ fullObstacle (clutter) workspace
* single _...to..._ multiple agents
* single _...to..._ multiple (similar but not same) tasks
* single _...to..._ multiple goals/objectives
* low _...to..._ high dof robots
* discrete _...to..._ continuous time (discretization time-step decreases to 0)
* discrete (small) _...to..._ continuous (large numbers of) states, actions, observations
* deterministic _...to..._ stochastic target policy

## topics
Deep RL,
Bayesian RL,
RL in POMDP,
Hierarchical RL,
Inverse RL,
Safe RL,
Transfer learning in RL,
Curriculum learning in RL,
Multiagent RL,
Evolutionary RL,
...

## succinct background
* @article{DBLP:journals/corr/abs-1802-09477,
  author    = {Scott Fujimoto and
               Herke van Hoof and
               Dave Meger},
  title     = {Addressing Function Approximation Error in Actor-Critic Methods},
  journal   = {CoRR},
  volume    = {abs/1802.09477},
  year      = {2018},
  url       = {http://arxiv.org/abs/1802.09477},
  archivePrefix = {arXiv},
  eprint    = {1802.09477},
  timestamp = {Fri, 02 Mar 2018 13:46:22 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1802-09477},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

## misc
[1999: Richard S. Sutton: Reinforcement Learning: Past, Present and Future?](https://link.springer.com/chapter/10.1007/3-540-48873-1_26)
> Just as reinforcement learning present took a step away from the ultimate goal of reward to
> focus on value functions, so reinforcement learning future may take a further step
> away to focus on the structures that enable value function estimation [...] In psy-
> chology, the idea of a developing mind actively creating its representations of the
> world is called constructivism. My prediction is that for the next tens of years rein-
> forcement learning will be focused on constructivism
