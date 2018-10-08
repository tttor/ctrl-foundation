# Where Did My Optimum Go?: An Empirical Analysis of Gradient Descent Optimization in Policy Gradient Methods
* Peter Henderson Joshua Romoff Joelle Pineau
* https://github.com/facebookresearch/WhereDidMyOptimumGo

## problem
* the ideal choice of optimizer for Deep RL remains unclear.
* it is unclear why different optimizers may have
  different behaviours in Deep RL algorithms and whether the theoretical properties of opti-
  mizers in the supervised learning setting generalize to Deep RL algorithms.

## idea
* provide an empirical analysis of the effects that a
  wide range of gradient descent optimizers and their hyperparameters have on policy gradi-
  ent methods, a subset of Deep RL algorithms, for benchmark continuous control tasks.
* Investigate
  * the effect of the learning rate on optimizer performance
  *  the effect of momentum on the performance of PPO and A2C.

## setup
* goal:to examine empirically what effects certain optimizers and learning rates may have
  on learning on policy gradient methods and what effect momentum may have in learning
  (suggesting possible sources of implicit momentum)
* algor:
  * synchronous Advantage Actor Critic (A2C) (Schulman et al., 2017; Mnih et al., 2016) and
  * Proximal Policy Optimization (PPO) (Schulman et al., 2017)
* opt:
  stochastic gradient descent (SGD), SGD with Nesterov momentum (SGDNM) (Nesterov, 1983), Av-
  eraged Stochastic Gradient Descent (ASGD) (Polyak and Juditsky, 1992), Adagrad (Duchi
  et al., 2011), Adadelta (Zeiler, 2012), RMSProp (Hinton et al., 2012), Adam (Kingma
  and Ba, 2014), AMSGrad (Reddi et al., 2018), Adamax (Kingma and Ba, 2014), and Yel-
  lowFin (Zhang et al., 2017).
* env: OpenAI Mujoco
  * Ant
  * HalfCheetah
  * Hopper
  * Reacher
  * Walker2d
* implementations from Kostrikov (2018)
  for A2C and PPO, modifying the codebase to replace the optimizer.
* run 10 random seeds
* run all on CPU to avoid non-determinism in the GPU
* metric
  * asymptotic performance (which is averaged over the last 50 episodes) and
  * average performance (where the average is over all episodes in the training process).
    * gives better insight into the effect on both learning speed and final asymptotic performance.
*  not examine learning rate schedules here. We avoid
  this for two reasons. First, this adds another layer of hyperparameters to optimize (which
  we want to avoid for complex settings). Second, in online settings, it is unclear how a
  schedule would work given that an agent must continuously learn. However, this may be a
  possible factor to examine in future work.

## result
* find that
  * adaptive optimizers have a narrow window of effective learning rates, diverging
    in other cases, and
  * the effectiveness of momentum varies depending on the properties of the environment.
  * the use of default values with
    adaptive optimizers may not be enough for the unique properties of Deep RL
  * SGDNM results in performance that is more stable across a variety of learning rates
    whereas adaptive methods such as Adam and RMSProp diverge entirely at higher learning
    rates with a small window of well-performing values in certain domains
  * for A2C, adaptive methods do find better optima with a well-tuned
    learning rate than we were able to find for SGDNM
  *  certain environments are less susceptible to momentum in both A2C and PPO.
* suggests that
  * there is significant interplay between the
    dynamics of the environment and Deep RL algorithm properties which aren’t necessar ily accounted for by traditional adaptive gradient methods.
  * developing or using adaptive gradient descent optimization methods which account for
    changing loss landscapes in different environments and the unique dynamics of Deep RL
    algorithms.
  * Perhaps different optimizers should be used for the value function and
    policy loss in such cases.

## background
* As an agent improves over time, the optimization target changes and thus the loss landscape (and local
  optima) change.
* commonly used: Adam, RMSProp
* In TD methods especially, there is a staleness to the gradients since the
  value function is bootstrapping off of its own predictions and updates may be biased toward
  previous policies and points in a trajectory.
* the loss landscape in certain environments might change sig-
  nificantly from episode to episode even with a minor change in the policy (e.g, environments
  where the agent might fall over and end the episode early).
* the mean itself provides insight into optimizer performance
  as all sources of randomness are fixed. The variance instead gives an indication as to an
  optimizer’s ability to find a similar optimum in different conditions.

## comment
* mostly describe what happens in the plots,
  better if with deep(er) analysis
* note in PPO paper, best hyperparem is wrt all envs, not per env
