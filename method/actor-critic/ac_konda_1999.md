# Actor-Critic Algorithms
* Vijay R. Konda, John N. Tsitsiklis
* https://papers.nips.cc/paper/1786-actor-critic-algorithms

## idea: Actor-critic methods
* two-time-scale algorithms in which
  * the critic uses TD learning with a linear approximation architecture and
  * the actor is updated in an approximate gradient direction based on information provided by the critic
* hold the promise of delivering faster convergence (due to variance reduction), when
  compared to actor-only methods.
* view actor critic-algorithms as stochastic gradient algorithms on the parameter space of the actor.
  * When the actor parameter vector is `\theta`,
    the job of the critic is to compute an approximation of the projection `\pi_{\theta} q_{\theta}` of `q_{\theta}` onto `\psi_{\theta}`.
  * The actor uses this approximation to update its policy in an approximate gradient direction.

## result
* the critic should ideally compute a certain "projection" of the value function onto
  a low-dimensional subspace spanned by a set of "basis functions," that
  are completely determined by the parameterization of the actor
* in actor-critic methods, the actor parameterization and the critic parameterization **need not**, and
  **should not** be chosen independently
  * Rather, an appropriate approximation architecture for the critic is
    directly prescribed by the parameterization used in actor.

## misc
* majority of Reinforcement Learning (RL) and Neuro-Dynamic Programming (NDP)
  * Actor-only methods
    * work with a parameterized family of policies.
    * drawback:
      * large variance
      * as the policy changes, a new gradient is estimated **independently** of past estimates;
        Hence, there is no "learning," in the sense of accumulation and consolidation of older information.
  * Critic-only methods
    * rely exclusively on value function approximation and
    * aim at learning an approximate solution to the Bellman equation, which will
      then hopefully prescribe a near-optimal policy.
* Since our actor-critic algorithms are gradient-based, one cannot expect to prove
  convergence to a globally optimal policy
* the TD(\alpha) critic will generally converge to an approximation of the desired
  projection of the value function,
