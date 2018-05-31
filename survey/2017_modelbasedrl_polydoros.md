# Survey of Model-Based Reinforcement Learning: Applications on Robotics
* Athanasios S. Polydoros · Lazaros Nalpantidis
* J Intell Robot Syst (2017) 86:153–173
* DOI 10.1007/s10846-017-0468-y

## intro
* In model-based methods there exists a model of the transition dynamics which is used for the derivation of the rewards and opti- mal actions. Thus the policies are optimized at the model and the optimal policy is applied at the phys- ical system.
* its main disad- vantage is that model-based RL algorithms heavily depend on the model’s ability to accurately represent the transition dynamics.

* value fn vs policy search approaches

* Policy search involves approaches such as:
  * gradient- based methods that update the parametrized set using hill-climbing approaches on the gradient of the reward function,
  * Expectation-Maximization (EM)methods that infer the parameters by maximizing the log- likelihood probability of the rewards,
  * Information Theory (Inf.Th.) methods that exploit concepts such as entropy for the derivation of optimized policies,
  * Bayesian optimization methods, and v) Evolu- tionary computation. Figure

* value function methods are sorted in four classes: i) Dynamic Programming (DP) methods that require a model of the transition dynamics, ii) Monte Carlo (MC) methods that are based on sampling, iii) Temporal Difference Learning (TDL) methods that take into account the difference of the value function between two state transitions, and iv) Differential Dynamic Programming methods (DDP).

## policy search methods
* PILCO is the state of the art approach for solving RL problems since it requires small amount of data for learning the policy and is time efficient.
  * employs a gradient method for the policy improvement
  * utilizes Gaussian Process as a method for learning transition dynamics

* PEGASUS: sampling based approaches that have been applied for policy search on model-baseds

* Information Theory Information theory approaches exploit the concept of entropy which is used as the basis for optimizing the parameters of the policy
* In the context of model-based RL, entropy is used for the evaluation of a trajectory generated from a policy compared to a reference trajectory—usually obtained from an external demonstrator. The

## conclusion
* model-based RL requires much fewer interactions with the environment compared to model-free RL.
  * due to the use of transition models and
  * is preferable because by minimizing the interactions with the environment
    the hazard of accidents and the robot’s wear and tear are also minimized.
* policy search methods appear to be more capable of dealing with the requirements posed by collabora- tive robotics applications. This is due to their ability to reduce the dimensionality of the policy learning problem by parameterizing the policy function and inferring the appropriate parameters. Among these methods, the most promising are the gradient and sampling-based ones.
