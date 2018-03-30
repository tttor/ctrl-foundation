# The reactor : a fast and sample - efficient actor-critic agent for reinforcement l earning
* Audrūnas Gruslys
* Published as a conference paper at ICLR 2018

## problem
* Data-efficiency and off-policy learning are essential for
  many real-world domains where interactions with the environment are expensive.

## method: reactor (Retrace-Actor)
* Distributional Retrace,
  * a new policy evaluation algorithm which brings multi-step off-policy updates to the
    distributional reinforcement learning setting
* β-leave-one-out policy gradient algorithm,
  * which improves the trade-off between variance and bias by using action values as a baseline.

## setup
* Atari 2600 benchmarks from the Arcade Learning Environment (ALE)

## result
* an agent with
  * higher sample-efficiency than Prioritized Dueling DQN (Wang et al., 2017) and
    Categorical DQN (Bellemare et al., 2017), while giving
  * better run-time performance than A3C (Mnih et al., 2016).

## misc
* Much of the recent work can be divided into two categories
  * those of which that, often building on the DQN framework,
    act eps-greedily according to an action-value function and
    train using mini-batches of transitions sampled from an experience replay buffer
    * value-function agents benefit from improved sample complexity,
    * but tend to suffer from long runtimes
  * the actor-critic agents,
    * train on transitions collected by multiple actors running, and
    * often training, in parallel (Schulman et al., 2017; Vezhnevets et al., 2017).
    * train on each trajectory only once, and thus tend to have worse sample complexity.
