# Active Reinforcement Learning
* Arkady Epshteyn et al
* icml2008

## problem
* The optimal policy computed offline in an
imperfectly modeled world may turn out to be subop-
timal when executed in the actual environment.

## observation
* while all of the transition probabilities and rewards in the model may be misspecified, 
  * it is not important to know all of them to determine the optimal policy.

## idea: active RL
* allows domain experts to specify possibly inaccurate models of the world offline. 
  * However, instead of using this model for planning, our algorithm uses it as a blueprint for exploration.
* uses sensitivity analysis to determine how the optimal policy in the expert-specified MDP is affected by 
  changes in transition probabilities and rewards of individual actions. 
  * This analysis **guides the exploration process** by forcing the agent to sample the most sensitive actions first. 
  
## background
* Bayesian re- inforcement learning (Dearden et al., 1999), 
  * imposes a prior distribution over possible worlds and updates it based on interactions with the environment.
  * However, this approach makes use of unrealistic as-
    sumptions on the shapes of probability distributions
    and approximate sampling to ensure tractability. The
    largest problem to which it was applied is two orders of
    magnitude smaller than the problems we solve in this
    work. In addition, we present an approximate version
    of our algorithm which is able to handle much larger
    (possibly continuous) state/action spaces.
