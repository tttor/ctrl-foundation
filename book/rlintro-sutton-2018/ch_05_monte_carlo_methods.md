# ch_05_monte_carlo_methods.md

# 5.5 Off-policy Prediction via Importance Sampling
* target policy
  * one that is learned about and that becomes the optimal policy,
  * is the policy being learned about
* behaviour policy
  * one that is more exploratory and is used to generate behavior.
  * the policy used to generate behavior
* off-policy learning
  * learning is from data “off” the target policy, and
