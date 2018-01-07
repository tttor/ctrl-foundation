# Kober: Survey on RL in robotics

@article{doi:10.1177/0278364913495721,
author = {Jens Kober and J. Andrew Bagnell and Jan Peters},
title ={Reinforcement learning in robotics: A survey},
journal = {The International Journal of Robotics Research},
volume = {32},
number = {11},
pages = {1238-1274},
year = {2013},
doi = {10.1177/0278364913495721},
URL = {https://doi.org/10.1177/0278364913495721},
}

RL is for auto discovery of behaviour through trial-and-error interaction with the environments.
The control engineer is to provide feedback in forms of scalar objective function that measure one-step performance.
Challenges for RL in robotics include:
* high-dimensional, continuous states and actions
* \emph{unrealistic} to assume that the true state is completely observable and noise-free
* experience on a real physical system is tedious to obtain, expensive and often hard to reproduce.
* need to be robust with respect to models that do not capture all
      the details of the real system, also referred to as under-modeling, and to model uncertainty.
* specifying good reward functions in robotics requires a fair amount of domain knowledge and
      may often be hard in practice.

In robotics, the most relevant model is commonly episodic tasks with finite-horizon models.
Note that the optimal control law can be unstable if the discount factor~$\lambda   $ (with $0 \le \lambda < 1$) is too low.
Furthermore, the average reward is also more suitable in robotics as
there is no need to choose a discount factor and to explicitly consider time in the derivation.
The average-reward criterion is $J = lim_{H \mapsto \inf} E(\frac{1}{H} \sum_{h=0}^H R_h)$.

Policy search is more appropriate and natural in robotics because:
* allows for a natural integration of expert knowledge, e.g.,
    through both structure and initializations of the policy
* allows domain-appropriate pre-structuring of the policy in an approximate form
    without changing the original problem
* optimal policies often have many fewer parameters than optimal value functions.
* local search in policy space can directly lead to good results
* constraints can be incorporated naturally, e.g., regularizing the change in the path distribution.
* better scalability
* usually only consider the current policy and its neighborhood in order to gradually improve performance.

