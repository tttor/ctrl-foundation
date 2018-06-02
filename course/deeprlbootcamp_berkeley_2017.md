# Deep RL Bootcamp; 26-27 August 2017; Berkeley CA

# Lec4a-policy-gradients-actor-critic, p abbeel
* stoc policy class to smooth out the optimization problems
* (vanilla) policy gradient is on-policy
* Gradient  tries to:
  * Increase probability of  paths with  positive R
  * Decrease probability of  paths with negative R

# Lec5-advanced-policy-gradient-methods, j schulman
* limitation of vanilla pol grad
  * hard to choose stepsizes
    * Input data is nonstationary due to changing policy
    * Bad step is more damaging than in supervised learning, since
      it affects visitation distribution
  * sample efficiency
* importance sampling derivation for policy gradient
* trust region is from optimization field
* because the prob dists are simple, then
  KL and other prob distrib distances will work almost equally
* KL to constrain size of update
* PPO same performance as TRPO, but only first-order optimization
* PPO: use penalty instead of constraint
* ACKTR: Limitation:
  works straightforwardly for feedforward nets (including convolutions),
  less straightforward for RNNs or architectures with shared weights

# Lec6-nuts-and-bolts-deep-rl-research; John Schulman
* john pendulum problem (with 2 dim of state) to get started
* medium problem: pong, hopper
* Plot time series for observations and rewards.
  Are they on a reasonable scale?
* Histogram observations and rewards
* use human control to test feasibility
* multiple random seeds, multiple tasks
* a cloud computing platform (Microsoft Azure, Amazon EC2, Google Compute Engine
* If observations have unknown range, standardize:
  * Compute running estimate of mean and standard deviation
* Rescale the rewards, but don’t shift mean,
  as that affects agent’s will to live
* Look at min/max/stdev of episode returns, along with mean
* Look at episode lengths: sometimes provides additional information

