# 2002_aoarl_kakade.md
* http://hunch.net/~jl/projects/RL/aoarl/Final.tex

# idea
* consider a settting in which an algorithm is given an access to
  * a restrart distribution
  * "approximate" greedy policy chooser
* propose a conservative policy iteration
  * the policy improve in a more uniform manner over the state space
  * a more conservative policy update

# background
* value-based method:
  * suffer from a lack of strong theoretical performance guarantees
  * for approximate method, the time required to obtain some performance level is not well understood
* policy-based, ie policy gradient, method:
  * require unreasonably large number of samples in order to determine the gradient accurately,
    due to intertwining of exploration and exploitation
  * estimating the gradient direction is difficult
