# 13: Policy Gradient Methods
In this chapter we consider methods that instead learn a parameterized policy that
can select actions without consulting a value function.
A value function may still be used to learn the policy parameter, but is not required for action selection.

we consider methods for learning the policy parameter based on the gradient of some
performance measure J(θ) with respect to the policy parameter. These methods seek to maximize
performance, so their updates approximate gradient ascent in J:

Methods that learn approximations to both policy and value functions are often called actor–critic methods, where
* `actor` is a reference to the learned policy, and
* `critic` refers to the learned value function, usually a state-value function.

the policy can be parameterized in any way, as long as
it is differentiable with respect to its parameters, that is,
as long as the gradient exists and is always finite.
In practice, to ensure exploration we generally require that the policy never becomes deterministic.

Of course, one could
select according to a softmax over action values, but this alone would not allow the policy to approach
a deterministic policy. Instead, the action-value estimates would converge to their corresponding true
values, which would differ by a finite amount, translating to specific probabilities other than 0 and 1.

advantage that policy parameterization
* the policy may be a simpler function to approximate,
  if this is the case, then it will typically learn faster and yield a superior asymptotic policy
* sometimes a good way of injecting prior
  knowledge about the desired form of the policy into the reinforcement learning system.
* with continuous policy parameterization the action probabilities change smoothly
  as a function of the learned parameter;
  Largely because of this stronger convergence guarantees are available for
  policy-gradient methods than for action-value methods.

Inthe episodic case,
the performance measure:
the value of the start state of the episode.

the policy gradient theorem provides
an analytic expression for the gradient of performance with respect to the
policy parameter (which is what we need to approximate for gradient ascent (13.1))
that does not involve the derivative of the state distribution.
The policy gradient theorem establishes that...where
the gradients are column vectors of partial derivatives with respect to the components of θ,
and π denotes the policy corresponding to parameter vector θ.

Recall our overall strategy of stochastic gradient ascent (13.1), which
requires a way to obtain samples such that the expectation of the
sample gradient is proportional to the actual gradient of the performance measure as a function of the parameter.

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

Summary:
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
