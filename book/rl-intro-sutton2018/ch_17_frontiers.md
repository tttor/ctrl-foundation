# 17: Frontiers

## 17.1 General Value Functions and Auxiliary Tasks
* a general value function, or GVF

## 17.2 Temporal Abstraction via Options
* Can the MDP framework be stretched to cover all the levels simultaneously?
* to formalize an MDP at a detailed level, with a small time step, yet
  enable planning at higher levels using extended courses of action that
  correspond to many base-level time steps.
  * need a notion of course of action that
    * extends **over many time steps** and
    * includes a notion of termination.
* define an **option** `\omega = < \pi{\omega}, \gamma_{\omega}`...
* a hierarchical policy:
  selects from options rather than actions, where
  options, when selected, execute until termination

## 17.3 Observations and State
* in many cases of interest, the sensory input gives only **partial** information about the state of the world.
* It is somewhat surprising and not widely recognized that
  function approximation includes important aspects of partial observability.
  * Nevertheless, there are many issues that cannot be investigated without a more explicit
    treatment of partial observability.
* 4 step for a more explicit treatment of partial observability.
  * change the problem: environment would emit not its states, but only observations
    * observation: signals that depend on its state but,
      like a robot’s sensors, provide only partial information about it.
    * assume that the reward is a direct, known function of the observation
      (perhaps the observation is a vector, and the reward is one of is components)
  * recover the idea of state (as used in this book) from the sequence of
    observations and actions.
    * To be a summary of the history, the state must be a function of history, St = f (Ht ), and
    * to be as useful for predicting the future as the whole history,
      it must have what is known as the Markov property.
  * use state-update functions,
    * by the popular Bayesian approach known as Partially Observable MDPs, or POMDPs.
      * belief state:
        the distribution over the latent states given the history
    * by Predictive State Representations, or PSRs.
      * the semantics of the agent state is grounded in predictions about future observations and actions,
        which are readily observable.
        (in POMDPs, the semantics of its agent state St are grounded in the environment state, Xt,
        which is never observed and thus is difficult to learn about)
      * a Markov state is defined as a d-vector of the probabilities of d specially chosen “core” tests
      * The vector is then updated by a state-update function u that is analogous to Bayes rule, but
        with a semantics grounded in observable data, which arguably makes it easier to learn
      * see Observable Operator Models (OOMs) and Sequential Systems (Thon, 2017)
  * work with an approximate notion of state
    * simplest example: just the latest observation, `S_t = O_t` .
* Learning the state-update function for an approximate state is
  a major part of the **representation learning** problem as it arises in reinforcement learning.

## 17.4 Designing Reward Signals
TODO
