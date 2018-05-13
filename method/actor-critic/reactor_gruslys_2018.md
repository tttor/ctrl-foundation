# The reactor : a fast and sample-efficient actor-critic agent for reinforcement learning
* Audrūnas Gruslys et al
* iclr2018: poster
* https://openreview.net/pdf?id=rkHVZWZAZ
* https://openreview.net/forum?id=rkHVZWZAZ
* https://arxiv.org/abs/1704.04651

## problem
* Data-efficiency and off-policy learning 
  * are essential for many real-world domains where interactions with the environment are expensive.

## idea: reactor (retrace-actor)
* based on an **off-policy multi-step return** actor-critic architecture
* maintains a memory buffer filled with past experiences
* decoupled acting from learning by allowing the actor and the learner to run in parallel
* The network outputs 
  * a target policy π (the actor), 
  * an action-value Q-function (the critic) evaluating the current policy π, and 
  * an estimated behavioural policy `\hat{\mu}` which we use for off-policy correction.
* training
  * critic: trained by the multi-step off-policy **Retrace algorithm**
  * actor: trained by **β-leave-one-out policy gradient estimate**
    * uses both the off-policy corrected return and the estimated Q- function).
    * improves the trade-off between variance and bias by using action values as a baseline.
* Distributional Retrace,
  * a policy evaluation algorithm which 
    brings multi-step off-policy updates to the distributional reinforcement learning setting

## setup
* Atari 2600 benchmarks from the Arcade Learning Environment (ALE)
* uses a deep **recurrent** neural network, ie LSTM

## result
* higher sample-efficiency 
  * than Prioritized Dueling DQN (Wang et al., 2017) and
    Categorical DQN (Bellemare et al., 2017), while giving
* better run-time performance 
  * than A3C (Mnih et al., 2016).
* The Reactor is 
  * sample-efficient due to the use of memory replay, and 
  * numerical efficient since it uses multi-step returns.
* contrib:
  beta-LOO, distributional retrace, prioritized sequence replay
  
## background
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
 * essentially: Reactor = DQN + A3C + Retrace + beta-leave-one-out
 * no xprmt on continuous action space; only atari tasks
 * numerical efficent=... ? is this computational efficient, so fast to compute?
   * ans: yes, it is about the speed of reward propagation
 
