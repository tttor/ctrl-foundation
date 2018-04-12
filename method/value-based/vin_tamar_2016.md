# Value Iteration Networks
* Aviv Tamar, Yi Wu, Garrett Thomas, Sergey Levine, and Pieter Abbeel
* 30th Conference on Neural Information Processing Systems (NIPS 2016), Barcelona, Spain.

## problem
* few recent works investigate policy architectures that are specifically tailored for planning under uncertainty, 
* current RL theory and benchmarks rarely investigate the generalization properties of a trained policy 
* deep RL works  employed NN architectures that 
  * are very **similar** to the standard networks used in supervised learning tasks, 
  * which typically consist of 
    * CNNs for feature extraction, and 
    * fully connected layers that map the features to a probability distribution over actions
  * Such networks are inherently reactive, and in particular, lack explicit planning computation. 
  * The **success of** reactive policies in sequential problems is 
    * due to the learning algorithm, which 
      essentially trains a reactive policy to select actions that have good long-term consequences in its training domain
* standard CNN-based networks do not generalize well to new tasks outside this set, because 
  they do not understand the goal-directed nature of the behavior.
* with enough training data that covers all possible task configurations, and a rich enough policy representation, 
  * a reactive policy can learn to map each task to its optimal policy. 
  * this is often too expensive, and 
    need a more data-efficient approach by exploiting a flexible prior about 
    the planning computation underlying the behavior.

## observation
* The sequential nature of decision making in RL is inherently different than the one-step decisions
  in supervised learning, and in general **requires some form of planning**
* a natural solution to many tasks involves **planning on some model** of the domain.

## idea: value iteration network (VIN)
* a fully differentiable neural network with a planning module embedded within.
  * a **NN-based policy** that can effectively learn to plan.
  * has a differentiable ‘planning program’ embedded within the NN structure
    * differentiable so it can be trained using standard backpropagation
* key:
  * a novel differentiable pproximation of the value-iteration algorithm, 
    * which can be represented as a convolutional neural network, and 
      trained end-to-end using standard backpropagation.
* to equip the policy with the ability to 
  * to learn and solve `\bar{M}`, and 
  * to add the solution of `\bar{M}` as an element in the policy 
* approach is based on 2 important observations. 
  * the vector of values `\bar{V}^*(s) \forall s` encodes all the information about the optimal plan in `\bar{M}` 
    * Thus, adding the vector `\bar{V}^*` as **additional features** to the policy `\pi` is sufficient for 
      extracting information about the optimal plan in `\bar{M}`
  * the MDP has a local connectivity structure, 
    the states for which `\bar{P} (\bar{s}_0|\bar{s}, \bar{a}) > 0` is a small subset of S̄, 
    such as in the grid-world example above,
    * Thus, an attention module that outputs a vector of (attention modulated) values `\psi(s)`, 
      which is added as additional features to a reactive policy
* VI Module
  * is simply a NN architecture that has the capability of performing an approximate VI computation. 
    * learning the MDP parameters and reward function by backpropagating through the network, similarly to a standard CNN. 
  * is a NN that encodes a differentiable planning computation.
  
  * observation:
     * each iteration of VI may be seen as passing the previous value function Vn and reward function R through 
       a convolution layer and max-pooling layer. 
     * In this analogy, each channel in the convolution layer corresponds to the Q-function for a specific action, and
       convolution kernel weights correspond to the discounted transition probabilities. 
     * Thus by recurrently applying a convolution layer K times, K iterations of VI are effectively performed.
* Value Iteration Networks
  * the reward, transitions, and attention can be defined by parametric functions, and trained with the whole policy

## setup
* task:
  * on discrete and continuous path-planning domains,
    * Grid-World Domain
    * Mars Rover Navigation
    * Continuous Control
  * on a natural-language based search task; WebNav challenge 
  
## result
* by learning an explicit planning computation, VIN policies generalize better to new, unseen domains
* "VIN policies learn an approximate planning computation" leads to better **generalization in a diverse set of tasks**, 
  ranging from simple gridworlds that are amenable to value iteration, to continuous control, and 
  even to navigation of Wikipedia links.
* conjecture that by learning the optimal policy for several instances of this domain, 
  a VIN policy would learn the planning computation required to solve a new, unseen, task.
* VIN can learn to plan such a ‘high- level’ plan, and also exploit that plan within 
  its ‘low-level’ continuous control policy. 
  * with continuous states and continuous actions (which cannot be solved using VI) and therefore
    a VIN perform ‘high-level’ planning on a discrete, coarse, grid-world representation of the continuous domain.

## misc
* In MDPs where the state space is very large or continuous, or when the MDP transitions or rewards are 
  not known in advance, 
  * planning algorithms cannot be applied. 
  * In these cases, a policy can be learned from either 
     * expert supervision – IL, 
       * a dataset of N state observations and corresponding optimal actions is generated by an expert. 
       * Learning a policy then becomes an instance of supervised learning
     * by trial and error – RL.
       * the optimal action is not available,
       * the agent can act in the world and observe the rewards and state transitions its actions effect. 

## comment
* better generalization over  diverse set of tasks because 
  reward, transitions, and attention can be defined by parametric functions, and trained with the whole policy
* RL for task and motion planning
* is not this: plan to leatn? NO, VIN learns a planning computation using standard RL and IL algorithms (learn to plan)
  > @intro: ... The sequential nature of decision making in RL is inherently different than the one-step decisions
  in supervised learning, and in general **requires some form of planning**..
* what kind of planning used in:
  > @sec 3: ... any standard planning algorithm can be used to obtain the value function
  * is it Q-learning in equ(1)
