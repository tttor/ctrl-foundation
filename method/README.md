# Method
* Witsenhausen's counterexample: https://en.wikipedia.org/wiki/Witsenhausen%27s_counterexample

# Base for iteration
* `policy-based`
  * directly optimize parameters of a stochastic policy through local gradient information obtained by
    interacting with the environment using the current policy.
  * operate by increasing the log probability of actions proportional to the future rewards influenced by these actions.
    * On average, actions which perform better will acquire higher probability, and
      the policy’s expected performance improves.
  * learn a parameterized policy that can select actions without consulting a value function
  * a step in the policy gradient direction should increase the probability of better-than-average actions and
    decrease the probability of worse-than-average actions
  * pros and cons
    * (+) a policy may be easier to learn than action values or action advantages;
          eg when Q-fn is too complex
    * (+) parameterized policies allows
       * if with continuous policy parameterization,
         the action probabilities change smoothly as a function of the learned parameter,
         Largely because of this, stronger convergence guarantees are available for policy-gradient methods than
         for action-value methods.
    * (+) allows task-appropriate pre-structured policies, such as
      * movement primitives to be integrated straightforwardly,
      * imitation learning from an expert's demonstrations can be used to
        obtain an initial estimate for the policy parameters
    * (+) directly optimize the quantity of interest while remaining stable under function approximation
          (given a sufficiently small learning rate)
    * (+) In many problems, the policy is simpler than the value function
    * (+) In many problems, the optimal policy is stochastic
    * (+) To enable smoother change in policies
    * (+) To avoid a search on every step (the max)
    * (+) To better relate to biology
    * (+) less susceptible to error in the presence of noise on properties of the controlled POMDP
    * (-) high variance, because the gradient is estimated using Monte Carlo samples
    * (-) tend to converge to a local optimal
    * (-) sample inefficiency, because
      * policy gradients are estimated from rollouts the variance is often extreme
      * requires on-policy samples
* `value-based`
  * learned the values of actions and then selected actions based on their estimated action values;
    (their policies would not even exist without the action-value estimates)
  * Bellman equ is fundamental to value fn learning:
    * relates the value of $(s,a)$ to the value os the subsequent $(s', a')$
  * the learning obj is to minimize the Bellman error
    * $L(\theta^Q) = \mathbb{E}[\big( Q(s_t, a_t|\theta^Q) - y_t \big)^2]$,
      where $y_t = r(s_t, a_t) + \gamma Q(s_{t+1}, a_{t+1})$
  * pros and cons
    * (+) low variance; more stable performance
    * (+) more sample efficient when they work (does not mean computationally efficient)
    * (-) high bias (due to bootstrapping)
    * (-) value function approximation turns out to be a very difficult problem
          in high-dimensional state and action spaces;
          need to discretize action for continuous action space
    * (-) often discontinuous, especially when the non-myopic policy differs
          from a myopic policy; For instance, the value function of the under-powered pendulum swing-up is
          discontinuous along the manifold where the applicable torque is
          just not sufficient to swing the pendulum up
    * (-)  a small change in the action-value function can cause large changes
          in the policy, which creates difficulties for convergence proofs and
          for some real-time applications.
    * (-) have **no** natural way of finding stochastic optimal policies
    * (-) mis-specification of value function models can lead to an inappropriate policy even in very simple problems
    * (-) control policies can vary drastically in each iteration

# Source of experience
* `model-free` (direct RL): `source= world`
  * the agent directly learns an optimal (or good) action-selection strategy from the collected data.
  * (in policy-search) is a general approach to learn policies based on **sampled trajectories**
  * based on whether there exist **discrepancy** between _the world for training_ and _the world for testing_:
    (note:
    the world can be either real or simulated (using a generative model),
    testing means execution)
    * _true_ model-free:
      * **no discrepancy** between _the world for training_ and _the world for testing_
      * training online: interleaved or in parallel (in background) with (during) execution
      * in Atari games, it is always true model-free
        because the worlds for both training and testing are always the same
      * to run true model-free experiment in simulator: use simulated world
    * _pseudo_ model-free:
      * **there exists discrepancy** between _the world for training_ and _the world for testing_
      * the discrepancy is inherited from the fact that **no model** can perfectly approximate the real world
      * training offline, before execution
      * in robotics, experience with the world is expensive, so
        pseudo model-free can be used in order to get a learned policy before any execution
        using interaction with simulated world (hence, this can can be thought of as offline planning), then
        there exists sim2real gap problem when deploying the trained policy to the world
        (because there exist the above-mentioned discrepancy)
  * pros and cons
    * (+) have the advantage of handling arbitrary dynamical systems with minimal bias
    * (+) learning a policy is often easier than learning an accurate forward model;
          may be more efficient in cases where the solution space (e.g., policy space)
          exhibits more regularity than the underlying dynamics
    * (+) less computational resources
    * (+) not affected by biases in the design (or estimation) of the model.
    * (+) makes little assumptions beyond a reward function
    * (+) effective for learning complex policies
    * (-) less sample-efficient, high sample complexity
    * (-) require policies with carefully designed, low-dimensional parameterizations
    * (-) necessary to interact with the (real(in true model-free)) robot,
          which can be time consuming and challenging in practice
    * (-) brittle convergence properties,
          which necessitate meticulous hyperparameter tuning.
    * (-) not transferable across tasks
* `model-based` (indirect RL): `source= model`
  * the agent uses the collected data to first build a model of the domain’s dynamics and
    then uses this model to optimize its policy.
  * use the sampled trajectories to first build a model of the state dynamics, and,
    subsequently, use this model for policy improvement.
  * consists of: planning and model learning
  * pros and cons
    * (+) sample-efficient; better results with less interaction with the world (experience)
    * (+) model learning transfers across tasks and environment configurations (learning physics)
    * (+) potentially to efficiently generalize to unforeseen situations
    * (-) suffer from significant bias, complex unknown dynamics cannot always be modeled accurately enough
    * (-) 2 sources of approximation error: learn model, estimate a value function using the learned model
    * (-) lead to control strategies that are not robust to model errors,
          Since the learned policy is inherently based on internal simulations with the learned model, inaccurate models;
          (can be alleviated by using models that explicitly account for model errors)

# Policy for learning
* term
  * the target policy is the policy being learned about
  * the behavior policy is the policy generating the trajectory data
* `on-policy`
  * by estimating quantities defined by the **current policy**, either
    on-policy data must be used, or updating must be sufficiently slow to avoid significant bias.
  * the agent learns only about the policy it is executing.
  * is when the target and behavious policies are the same
  * pros and cons
    * (+) unbiasedness
    * (+) better stability
    * (-) sample inefficient; poor sample complexity
* `off-policy`
  * an agent learns about a policy or policies different from the one it is executing.
  * separate the evaluation/target policy from the behaviour policy
  * is learning about the value of a policy other than the policy being used to generate the trajectory
  * pros and cons
    * (+) able to exploit data from other sources, such as experts,
          making them inherently more sample efficient than on-policy methods
    * (+) able to learn about an optimal policy while executing an exploratory policy
    * (+) able to learn multiple tasks in parallel from
          a single sensorimotor interaction with an environment
    * (+) much more sample-efficient.
    * (-) does **not stably** interact with function approximation
          (need extensive hyperparameter tuning can be required to obtain stable behavior)
    * (-) require complex approximate inference procedures in continuous action spaces.
    * (-) convergence is in general not guaranteed with non-linear function approximators, and
    * (-) practical convergence and instability issues typically mean that
          extensive hyperparameter tuning is required to attain good results.

# Stochasticity of the policy
* `stochastic`
  * stochastic policy gradient theorem
    * the policy gradient integrates over both state and action spaces
    * computing the stochastic policy gradient may require more samples
  * the best approximate policy may be stochastic, eg
    * in card games with **imperfect information** the optimal play is
      often to do two different things with specific probabilities, such as when bluffing in Poker.
* `deterministic`
  * deterministic policy gradient theorem
    * the policy gradient integrates over state only

# When policy compiled/learned with respect to execution/action time
* `offline`
  * policy learned (planned) before execution
  * consider all contingencies so does not scale up
* `online`
  * aka: decision-time planning
  * plan from the **current** belief (typically, each step), so
    * potentially can handle large-scale planning
    * handle model changes naturally
  * policy learned:
    in between 2 execution (interleaved) and **in background** (in paralel with execution)

# Other dimensions:
plain _vs_ hierarchical structure,
episodic _vs_ continuing tasks,
average _vs_ cumulative discounted rewards,
without-prior (non-Bayesian) _vs_ with-prior (Bayesian),
see also [this](https://github.com/tttor/rl-foundation/blob/master/book/rl-intro-sutton2018/part_01_summary.md)

# MDP-related formulas
* state-value function
  * how good it is for the agent to be in a given state
  * $V^{\pi}(s) := \mathbb{E}_{\pi} [R_t | S_t = s]$
  * $V^{\pi}(s) = \sigma_a \pi(a|s) Q^{\pi}(s, a)$
* action-value function
  * how good it is to perform a given action in a given state
  * $Q^{\pi}(s, a) = \mathbb{E}_{\pi} [R_t | S_t = s, A_t = a]$
* advantage function
  * $A^{\pi}(s, a) := Q^{\pi}(s, a) - V^{\pi}(s)$
* a policy
  * is a mapping from states to probabilities of selecting each possible action
* state transition probabilities
  * $T: \mathcal{S} \times \mathcal{S} \times \mathcal{A} \mapsto [0, 1]$

# Misc
* Temporal Difference (TD):
  MonteCarlo and DynamicsProgramming
* generalised policy iteration: interleaving policy evaluation with policy improvement
  * Policy evaluation:
    * estimate the action-value function,
    * eg, by Monte-Carlo evaluation or temporal-difference learning.
  * Policy improvement:
    * update the policy with respect to the (estimated) action-value function
    * eg, a greedy maximisation (or soft maximisation) of the action-value function
* https://mathoverflow.net/questions/44677/is-there-mdps-markow-decision-process-which-have-a-non-deterministic-optimal-p
* the interpretation of the discount factor, $\gamma$
  * $\gamma = 0$: short-sighted, the agent only values immediate reward,
    * eg, because the agent (believes that it) is going to die right after receiving that immediate reward
  * https://stats.stackexchange.com/questions/221402/understanding-the-role-of-the-discount-factor-in-reinforcement-learning
  * https://en.wikipedia.org/wiki/Q-learning
> while a factor approaching 1 will make it strive for a long-term high reward. If the discount factor meets or exceeds 1, the action values may diverge
