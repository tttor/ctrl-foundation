# Model-based policy gradients with parameter-based exploration by least-squares conditional density estimation
* Voot Tangkaratt et al
* Neural Networks 57 (2014) 128–140

## idea: mpgpe = pgpe + lscde (least-squares conditional density estimation)

## setup
* PGPE, the action is assumed to be a
scalar, and the policy for each dimension is learned independently
for multi-dimensional actions.

## result
* GP-based model estimation is not as flexible as the LSCDE-based method
  when the transition model is not Gaussian
* LSCDE performs rather poorly in high-dimensional problem

## background
* it was shown that the variance of policy gradients can be propor-
tional to the length of an agent’s trajectory, due to the stochastic-
ity of policies (Zhao, Hachiya, Niu, & Sugiyama, 2012).
  * To cope with this problem, .... In PGPE, deterministic policies are
used to suppress irrelevant randomness and useful stochasticity is
introduced by drawing policy parameters from a prior distribution.
  * Then, instead of policy parameters, hyper-parameters included
in the prior distribution are learned from data. Thanks to this
prior-based formulation, the variance of gradient estimates in
PGPE is independent of the length of an agent’s trajectory (Zhao
et al., 2012).
  * However, PGPE still suffers from an instability
problem in small sample cases. To further improve the practical
performance of PGPE, an efficient sample reuse method called
importance-weighted PGPE (IW-PGPE) was proposed recently and
demonstrated to achieve the state-of-the-art performance (Zhao
et al., 2013)

## comment:
* this work, mpgpe = pgpe + lscde
* (-) this is so demanding
> the action is assumed to be a
scalar, and the policy for each dimension is learned independently
for multi-dimensional actions.
* (-) imo, sampling even from a generative model may incur some cost, eg time
> in the model-based scenario, we can draw as many trajectory
samples as we want from the learned transition model without
additional sampling costs.
