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

## idea: value iteration network (VIN)
* a fully differentiable neural network with a planning module embedded within.
  * a **NN-based policy** that can effectively learn to plan.
  * has a differentiable ‘planning program’ embedded within the NN structure
    * differentiable so it can be trained using standard backpropagation

* key:
  * a novel differentiable pproximation of the value-iteration algorithm, 
    * which can be represented as a convolutional neural network, and 
      trained end-to-end using standard backpropagation.

## setup
* task:
  * on discrete and continuous path-planning domains,
  * on a natural-language based search task; WebNav challenge 
  
## result
* by learning an explicit planning computation, VIN policies generalize better to new, unseen domains
* "VIN policies learn an approximate planning computation" leads to better generalization in a diverse set of tasks, 
  ranging from simple gridworlds that are amenable to value iteration, to continuous control, and 
  even to navigation of Wikipedia links.
  
## misc


## comment
* better generalization
* learn to plan
* RL for task and motion planning
* is not this: plan to lean
> @intro: ... The sequential nature of decision making in RL is inherently different than the one-step decisions
  in supervised learning, and in general **requires some form of planning**..
