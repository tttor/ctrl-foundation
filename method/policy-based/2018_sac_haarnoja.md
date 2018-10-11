# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor
* Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel & Sergey Levine
* icml2008, nips2017: workshop
* http://proceedings.mlr.press/v80/haarnoja18b.html
* https://arxiv.org/abs/1801.01290
* https://github.com/haarnoja/sac
* https://openreview.net/forum?id=HJjvxl-Cb
* sites.google.com/view/soft-actor-critic

## problem
* model-free RL: very high sample complexity
  * due to on-policy learning: some of the most commonly used
    deep RL algorithms, such as TRPO (Schulman et al., 2015),
    PPO (Schulman et al., 2017b) or A3C (Mnih et al., 2016),
    require new samples to be collected for each gradient step
* model-free RL: brittle convergence properties,
  * which necessitate meticulous hyperparameter tuning;
    hyperparameters: learning rates, exploration constants

## observation
* One cause for the poor sample efficiency of deep RL methods is on-policy learning
  * eg TRPO, A3C require new samples to be collected for each gradient step on the policy
* Off-policy algorithms
  * aim to reuse past experience.
  * not directly feasible with conventional policy gradient formulations
    * but is relatively straightforward for Q-learning based methods
  * the combination of off-policy learning and high-dimensional,
    nonlinear function approximation with neural networks presents
    a major challenge for stability and convergence
* deep deterministic policy gradient (DDPG)
  * provide sample-efficient learning,
  * but extreme brittleness and hyperparameter sensitivity
* the maximum entropy formulation
  * provides a substantial improvement in exploration and robustness:
  * robust in the face of modeling and estimation errors,
    * improve exploration by acquiring diverse behaviors.
* previously proposed maximum entropy methods generally do not exceed
  the performance of state-of-the-art off-policy algorithms, such as DDPG, when learning from scratch,
  * though they may have other benefits, such as improved exploration and ease of finetuning.

## idea: soft actor-critic (SAC)
* an off-policy actor-critic deep RL algorithm based on
  the maximum entropy reinforcement learning framework.
* the actor aims to
  * maximize expected reward while also
  * maximizing entropy
  * that is, succeed at the task while acting as randomly as possible.
* incorporates three key ingredients:
  * an actor-critic architecture with eparate policy and value function networks,
  * an off-policy formulation that enables reuse of previously collected data for efficiency, and
  * entropy maximization to enable stability and exploration.
* combines off-policy actor-critic training with a stochastic actor, and
  further aims to maximize the entropy of this actor with an entropy maximization objective.
* The entropy appears in both the policy and value
function.
  * In the policy, it prevents premature convergence of
    the  policy variance (Equation 10).
  * In the value function, it encourages exploration by increasing the value of regions of
    state space that lead to high-entropy behavior (Equation 5).
* 3 ingredient
  * an actor-critic architecture with separate policy and
    value function networks, 
  * an off-policy formulation that enables reuse of previously collected data for efficiency, and
  * entropy maximization to enable stability and exploration.

## setup
* to understand how the **sample complexity** and **stability** of our method
  compares with prior off-policy and on-policy deep reinforcement learning algorithms
* train 5 different instances of each algorithm with different random
  seeds, with each performing one evaluation rollout every
  1000 environment steps
* use an exponentially moving
  average, with a smoothing constant τ , to update the target
  value network weights
* task:
  * mujoco cont ctrl
* baseline
  * TRPO
  * DDPG
* 2 hidden layers, with 256 neurons
* use reward scale

## result
* SAC > (DDPG, PPO)
  * overall, SAC performs **comparably**
    to the baseline methods on the easier tasks and **outperforms
    them on the harder tasks** with a large margin, both in terms
    of learning speed and the final performance
*  SAC also learns considerably faster than PPO as a consequence of
  the large batch sizes PPO needs to learn stably on more
  high-dimensional and complex tasks.
* SAC:
  * provides sample-efficient learning while
  * retaining the benefits of entropy maximization and stability
* soft policy iteration converge to the optimal policy (present a convergence proof)
* outperforms state-of-the-art model-free deep RL methods,
  * including the off-policy DDPG algorithm and the on-policy TRPO algorithm.
* stochastic, entropy maximizing reinforcement learning algorithms can provide
  a promising avenue for improved robustness and stability,
* The individual seeds attain much more consistent performance with SAC,
  * while DDPG exhibits very high variability across seeds, indicating substantially worse stability.
* the inclusion of entropy regularization is a critical component
* show that soft policy iteration converge to the optimal policy
* stochasticity can stabilize training as the variability between the
  seeds becomes much higher with a deterministic policy.
  * Soft actor-critic performs much more consistently,
    while the deterministic variant exhibits very high variability
    across seeds, indicating substantially worse stability
* Soft actor-critic is sensitive to reward scaling since it is related to the
  temperature of the optimal policy.
* found two Q-functions significantly speed
  up training, especially on harder tasks.

## background
* off-policy: DDPG algorithm
* on-policy: PPO algorithm
* popular off-policy actor-critic variant is based on the deterministic
  policy gradient (Silver et al., 2014) and its deep counterpart, DDPG
  * uses a Q-function estimator to enable off-policy learning, and
    a deterministic actor that maximizes this Q-function.
  * difficult to stabilize and brittle to hyperparameter settings
* Maximum entropy reinforcement learning optimizes policies to maximize both
  * the expected return and
  * the expected entropy of the policy.
* It is common to use a separate target value network that
  slowly tracks the actual value function to improve stability
*  several
papers have noted the connection between Q-learning and
policy gradient methods in the framework of maximum en-
tropy learning (O’Donoghue et al., 2016; Haarnoja et al.,
2017; Nachum et al., 2017a; Schulman et al., 2017a).

## comment
* note that a2c implementation in openai baseline uses the idea of maximum entropy
