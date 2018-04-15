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
* define an **option** `\omega = \langle \pi{\omega}, \gamma_{\omega} \rangle`...
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
* success of a reinforcement learning application strongly depends on
  * how well the reward signal frames the goal of the application’s designer and
  * how well the signal assesses progress in reaching that goal
* By designing a reward signal we mean
  * designing the part of an agent’s environment that is responsible for
    * computing each scalar reward `R_t` and
    * sending it to the agent at each time `t`.
* recall at the end of Chapter 14,
  * `R_t` is **more like** a signal generated inside an animal's brain **than**
    it is like an object or event in the animal’s external environment.
* the problem of sparse reward
  * State–action pairs that clearly deserve to trigger reward may be **few and far between**, and
  * rewards that mark progress toward a goal can be infrequent because
    progress is difficult or even impossible to detect.
  * The agent may wander aimlessly for long periods of time
  * are not just problems with the reward signal;
    they are also problems with an agent’s policy in
    preventing the agent from frequently encountering rewarding states.
* solution to sparse reward
  * A better way to provide such guidance is
    * to leave the reward signal alone and
    * augment the value-function approximation with an initial guess of
      what it should ultimately be, or
    * augment it with initial guesses as to what certain parts of it should be.
  * shaping technique
  * imitation learning, learning from demonstration, and apprenticeship learning.
    * to benefit from the expert agent but leave open the possibility of eventually performing better
    * Learning from an expert’s behavior can be done either
      * by learning directly by supervised learning or
      * by extracting a reward signal using what is known as “inverse reinforcement learning” and
      * then using a reinforcement learning algorithm with that reward signal to learn a policy.
  * to automate the trial-and-error search for a good signal that we mentioned above
    * by defining a space of feasible candidates and applying an optimization algorithm.
    * The optimization algorithm
      * evaluates each candidate reward signal by running the reinforcement learning system with that signal for some number of steps, and
      * then scoring the overall result by a “high-level” objective function intended to encode the designer’s true goal,
        ignoring the limitations of the agent.
* intrinsically-motivated reinforcement learning

## 17.5 Remaining Issues
* Roughly speaking,
  * that approach is based on model-free and model-based methods working together, as in the Dyna architecture,
  * combined with function approximation as developed in Part II.
  * on online and incremental algorithms, which we see as fundamental even to model-based methods, and
  * on how these can be applied in off-policy training situations.
* six further issues for future research.
* **issue 1:**
  powerful parametric function approximation methods that
  work well in fully incremental and online settings
  * Methods based on deep learning and artificial neural networks
    * **only** work well with
      * batch training on large data sets,
      * training from extensive off-line self play, or
      * learning from the interleaved experience of multiple agents on the same task.
    * struggle to learn rapidly in the incremental, online settings that
      are most natural for the reinforcement learning
    * Most current deep learning research is directed toward working around
      this limitation rather than removing it.
* **issue 2:**
  methods for learning features such that subsequent learning generalizes well.
  * an instance of a general problem variously called “representation learning,” “constructive induction,” and “meta-learning”
  * how can we use experience not just to learn a given desired function, but
    to learn inductive biases such that future learning generalizes better and is thus faster?
* **issue 3:**
  scalable methods for **planning** with **learned environment models**
  * cases of full model-based reinforcement learning, in which
    the environment model is learned from data and then used for planning, are **rare**.
  * effective planning with learned models
  * the learning of the model needs to be selective because
    the scope of a model strongly affects planning efficiency.
    * If a model focuses on the key consequences of the most important options, 
      * then planning can be efficient and rapid,
    * (but) if a model includes details of unimportant consequences of options that
      are unlikely to be selected, 
      * then planning may be almost useless.
  * Environment models should be constructed judiciously with regard to
    both their states and dynamics with the goal of optimizing the planning process.
  * The various parts of the model should be continually monitored as to the degree
    to which they contribute to, or detract from, planning efficiency.
  * to design model-learning methods that take into account their implications.
* **issue 4:**
  that of automating the choice of tasks on which an agent works and
  uses to structure its developing competence.
  * want the agent to make its own choices about what tasks it should try to master.
  * making these task choices automatically, particularly
    when they derive from what the agent has previously constructed as
    a result of representation learning or experience with previous subproblems.
* **issue 5:**
  that of the interaction between behavior and learning via some computational analog of curiosity.
  * The actions taken will of course influence this stream of experience, which
    in turn will determine how much learning occurs and which tasks are learned.
* **issue 6:**
  that of developing methods to make it acceptably safe to
  embed reinforcement learning agents into physical environments,

## 17.6 Reinforcement Learning and the Future of Artificial Intelligence
* deep reinforcement learning
  * reinforcement learning with function approximation by deep neural networks.
* key feature of reinforcement learning that
  * it takes long-term consequences of decisions into account.
* A reinforcement learning agent can learn by interacting with either
  * the real world or
  * a simulation of some piece of the real world, or
    * provide safe environments
    * can make virtually unlimited data available for learning, generally
      at less cost than needed to obtain real experience, and
    * learning can often occur more quickly than if it relied on real experience
  * by a mixture of these two sources of experience.
* the full potential of reinforcement learning requires reinforcement learning
  agents to be embedded into the flow of real-world experience, where they act, explore,
  and learn in our world
  * able to survive in nonstationary and hostile environments
* it is often difficult, sometimes impossible, to simulate real-world experience
  with enough fidelity to make the resulting policies, whether derived by reinforcement
  learning or by other methods, work well—and safely—when directing real actions.
* Careful design of reward signals is essential if an agent is to act in the real world with no
  opportunity for human vetting of its actions or means to easily interrupt its behavior.
* How do you make sure that an agent gets enough experience to learn a
  high-performing policy, all the while not harming its environment, other agents, or itself
  (or more realistically, while keeping the probability of harm acceptably low)?
