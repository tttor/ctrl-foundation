# Chapter 10 On-policy Control with Approximation

# 10.1 Episodic Semi-gradient Control
* episodic semi-gradient one-step Sarsa.
  For a constant policy, this
  method converges in the same way that TD(0) does, with the same kind of error bound (9.14)

# 10.2 Semi-gradient n-step Sarsa
* performance is best if an intermediate level of  bootstrapping is used,
  corresponding to an n larger than 1

# 10.3 Average Reward: A New Problem Setting for Continuing Tasks
* This assumption about the MDP is known as ergodicity.
  * It means that:
    where the MDP starts or any early decision made by the agent can have only a temporary effect;
    in the long run the expectation of being in a state depends only on the policy and the MDP transition probabilities.

# 10.4 Deprecating the Discounted Setting
TODO

# 10.4 Deprecating the Discounted Setting
TODO

# 10.5 Differential Semi-gradient n-step Sarsa
TODO

# 10.6 Summary
* have extended the ideas of parameterized function approximation and
  semi-gradient descent, introduced in the previous chapter, to control.
  * The extension is immediate for the episodic case,
    but for the continuing case we have to introduce a whole
    new problem formulation based on maximizing the average reward setting per time step
