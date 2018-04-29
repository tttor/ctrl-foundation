# The reactor : a fast and sample-efficient actor-critic agent for reinforcement learning
* Audrūnas Gruslys et al
* Published as a conference paper at ICLR 2018
* https://arxiv.org/abs/1704.04651

## problem
* Data-efficiency and off-policy learning are essential for
  many real-world domains where interactions with the environment are expensive.

## idea: reactor (retrace-actor)
* based on an **off-policy multi-step return** actor-critic architecture
* maintains a memory buffer filled with past experiences
* decoupled acting from learning by allowing the actor and the learner to run in parallel
* The network outputs 
  * a target policy π (the actor), 
  * an action-value Q-function (the critic) evaluating the current policy π, and 
  * an estimated behavioural policy `\hat{\mu}` which we use for off-policy correction.
* training
  * The critic is trained by the multi-step off-policy **Retrace algorithm**
  * the actor is trained by a novel **β-leave-one-out policy gradient estimate**
    (which uses both the off-policy corrected return and the estimated Q- function).
* Distributional Retrace,
  * a new policy evaluation algorithm which brings multi-step off-policy updates to the
    distributional reinforcement learning setting
* β-leave-one-out policy gradient algorithm,
  * which improves the trade-off between variance and bias by using action values as a baseline.

## setup
* Atari 2600 benchmarks from the Arcade Learning Environment (ALE)
* uses a deep **recurrent** neural network, ie LSTM

## result
* an agent with
  * higher sample-efficiency than Prioritized Dueling DQN (Wang et al., 2017) and
    Categorical DQN (Bellemare et al., 2017), while giving
  * better run-time performance than A3C (Mnih et al., 2016).
* The Reactor is 
  * sample-efficient thanks to the use of memory replay, and 
  * numerical efficient since it uses multi-step returns.

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
    
 ## comment
 * TODO: finish!
 * essentially: Reactor = DQN + A3C + Retrace + beta-leave-one-out
 * numerical efficent=... ? is this computational efficient, so fast to compute?
   * ans: yes, it is about the speed of reward propagation
 
