# Proximal Policy Optimization Algorithms
* John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov

## idea: PPO
* a new family of policy gradient methods for reinforcement learning,
  which alternate between
  * sampling data through interaction with the environment, and
  * optimizing a “surrogate” objective function using stochastic gradient ascent.
* a novel objective function that enables multiple epochs of minibatch updates.
  * use multiple epochs of stochastic gradient ascent to perform each policy update
  * cf:  standard policy gradient methods perform one gradient update per data sample

## result
* PPO > TRPO
  * much simpler to implement, more general, and
    have better sample complexity (empirically).
