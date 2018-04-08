# 13: Policy Gradient Methods
* consider methods that learn a parameterized policy that
  can select actions **without** consulting a value function.
  * A value function may still be used to learn the policy parameter,
    but is **not required** for action selection.
* notation:
* goal of policy gradient methods:
  * learning the policy parameter based on the gradient of
    some performance measure `J(\theta)` with respect to the policy parameter.
  * to maximize performance, so their updates approximate gradient ascent in J:
    * `\theta_{t+1} = \theta_t + \alpha \hat{ \grad J(\theta_t) }` ...(13.1)
      * `\hat{ \grad J(\theta_t) }`:
        a **stochastic estimate** whose expectation approximates the gradient of the
        performance measure with respect to its argument
      * `\theta \in R^{d'}`: policy’s parameter vector
      * `d`: dimensionality; the number of components of w
      * `d'`: alternate dimensionality; the number of components of `\theta`
      * `\pi(a|s,\theta) = Pr{A_t = a | S_t = s, \theta_t = \theta}`:
        the probability that action `a` is taken at time `t` given that
        the environment is in state `s` at time t with parameter `\theta`
      * `w \in R^{d}`: value function’s weight vector
      * `\hat{v}(s,w)`: the learned value fn
* actor-critic:
  Methods that learn approximations to **both** policy and value functions
  * `actor` is a reference to the learned policy, and
  * `critic` refers to the learned value function

## 13.1 Policy Approximation and its Advantages
* the policy can be parameterized in any way,as long as 
    * it is differentiable with respect to its parameters
    * the gradient exists and is always finite.
* soft-max in action preferences.
  * The actions with the highest preferences in each state are given the
    highest probabilities of being selected
  * advantage:
    * the approximate policy can approach a deterministic policy, cf eps-greedy
    * enables the selection of actions with arbitrary probabilities.
* advantage of policy parameterization (over action-value parameterization)
  * the policy may be a simpler function to approximate,
  * a good way of **injecting prior knowledge** about the desired form of the policy into the reinforcement learning system.

## 13.2 The Policy Gradient Theorem
* advantages of policy parameterization over ε-greedy
  * the approximate policy can approach a deterministic policy
  * with continuous policy parameterization the action probabilities change smoothly
    as a function of the learned parameter;
    * Largely because of this, stronger convergence guarantees are available for
      policy-gradient methods than for action-value methods.
* In the episodic case,
  * the performance measure:
    * the value of the start state of the episode.
    * `J(\theta) = v_{ \pi_{\theta} } (s_0)` ...(13.4)
* **challenge**:
  _How can we estimate the performance gradient with respect to
  the policy parameter when the gradient depends on
  the unknown effect of policy changes on the state distribution?_
  * **Ans**: policy gradient theorem
    * provides an analytic expression for the gradient of performance with respect to the policy parameter 
      * (which is what we need to approximate for gradient ascent (13.1))
      * that does **not involve** the derivative of the state distribution.
    * `\nabla J(\theta) \propto \sum_s \mu(s) \sum_a q_{\pi}(s,a) \nabla \pi (a|s,\theta)` ...(13.5)
      * the gradients are column vectors of partial derivatives with respect to the components of `\theta`
      * distribution `\mu` is the on-policy distribution under `\pi`

## 13.3 REINFORCE: Monte Carlo Policy Gradient
* The **sample gradients** need only **be proportional to the gradient** 
  * because any constant of proportionality can be absorbed into the step size `\alpha`
* Policy gradient's transformation
  * if `\pi` is followed, then
    * `\nabla J(\theta) = E_{\pi} [ \sum_a q_{\pi}(s,a) \nabla \pi (a|s,\theta) ]`
      * `E_{\pi}` substitutes `\propto \sum_s \mu(s)`
  * if only each term (of the remaining part of the expectation above) were weighted by 
    the probability of selecting the actions according to `\pi (a|s,\theta)`, then
    * `\nabla J(\theta) = E_{\pi} [ G_t \frac{\nabla \pi (A_t|S_t,\theta)}{\pi (A_t|S_t,\theta)} ]`
      * replacing `a` by the sample `A_t \sim \pi`
      * `q_{\pi}(A_t|S_t) = E_{\pi} [G_t | A_t|S_t]`
      * `G_t` is the return
   * The final expression in the brackets of `E_{\pi} [...]` is exactly what is needed, 
     * a quantity that can be sampled on each time step whose **expectation is equal to** the gradient. 
 * Using this sample to instantiate our generic stochastic gradient ascent algorithm (13.1), yields the update
   * `\theta_{t+1} = \theta_t + \alpha G_t \frac{\nabla \pi (A_t|S_t,\theta)}{\pi (A_t|S_t,\theta)}` ...(13.6)
     * `[ G_t \frac{...}{...} ]` substitutes `\hat{ \grad J(\theta_t) }` 

REINFORCE uses the complete return from time t, which includes all future rewards up
until the end of the episode. In this sense REINFORCE is a Monte Carlo algorithm and is well defined
only for the episodic case with all updates made in retrospect after the episode is completed.
As a Monte Carlo method REINFORCE may be of high variance and thus produce slow learning.
As a stochastic gradient method, REINFORCE has good theoretical convergence properties.

REINFORCE with Baseline:
One natural choice for the baseline is an estimate of the state value.
Although the REINFORCE-with-baseline method learns both a policy and a state-value function, we
do not consider it to be an actor–critic method because its state-value function is used only as a
baseline, not as a critic. That is, it is not used for bootstrapping (updating the value estimate for
a state from the estimated values of subsequent states), but only as a baseline for the state whose
estimate is being updated.
REINFORCE with baseline is unbiased and
will converge asymptotically to a local minimum, but like all Monte Carlo methods it tends to learn
slowly (produce estimates of high variance) and to be inconvenient to implement online or for continuing
problems.

For continuing problems without episode boundaries we need to define
performance in terms of the average rate of reward per time step.

Policy-based methods offer practical ways of dealing with large actions spaces, even continuous spaces
with an infinite number of actions. Instead of computing learned probabilities for each of the many
actions, we instead learn statistics of the probability distribution. For example, the action set might be
the real numbers, with actions chosen from a normal (Gaussian) distribution.

## Summary:
* A parameterized policy enables actions to be taken without consulting
action-value estimates—though action-value estimates may still be learned and
used to update the policy parameter.
* policy-gradient methods—meaning methods that
update the policy parameter on each step in the direction of an estimate of
the gradient of performance with respect to the policy parameter.
* Methods that learn and store a policy parameter have many advantages.
  * can learn specific probabilities for taking the actions.
  * can learn appropriate levels of exploration and approach deterministic policies asymptotically
  * can naturally handle continuous state spaces
  * on some problems the policy is just simpler to represent parametrically than the value function;
* policy gradient theorem gives an exact formula for how performance is
affected by the policy parameter that does not involve derivatives of the state distribution
*  The state-value function assigns credit to—critizes—the policy’s action selections, and
accordingly the former is termed the critic and the latter the actor, and
these overall methods are sometimes termed actor–critic methods.

