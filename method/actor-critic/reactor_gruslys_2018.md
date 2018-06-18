# The reactor : a fast and sample-efficient actor-critic agent for reinforcement learning
* Audrūnas Gruslys et al
* iclr2018: poster
* https://openreview.net/pdf?id=rkHVZWZAZ
* https://openreview.net/forum?id=rkHVZWZAZ
* https://arxiv.org/abs/1704.04651

## problem
* data-efficiency and off-policy learning
  * essential when interactions with the environment are expensive.
* time-efficiency
  * directly impacts an algorithm’s applicability through resource costs

## idea: reactor (retrace-actor)
* based on an **off-policy multi-step return** actor-critic architecture
  * maintains a memory buffer filled with past experiences
* the actor and the learner to run in parallel
  * decoupled acting from learning
* The network outputs
  * a target policy π (the actor),
  * an action-value Q-function (the critic) evaluating the current policy π, and
  * an estimated behavioural policy $\hat{\mu}$ which we use for off-policy correction.
* training
  * critic: trained by the multi-step off-policy **Retrace algorithm**
  * actor: trained by **beta-leave-one-out policy gradient estimate**
* contrib 1: beta-leave-one-out policy gradient estimate
  * uses both the off-policy corrected return and the estimated Q-function
  * improves the trade-off between variance and bias by using action values as a baseline.
* contrib 2: distributional retrace (as a policy evaluation algorithm)
  * brings multi-step off-policy updates to the distributional RL setting
  * use the off-policy corrected return computed by the Retrace algorithm, which 
    produces a (biased) estimate of Qπ(ˆa) but whose bias vanishes asymptotically (Munos et al., 2016).
* contrib 3: prioritized replay algorithm for sequences,
  * exploits the temporal locality of neighboring observations for
    more efficient replay prioritization.

## setup
* pol grad estimate: 
  * beta-LOO
* critic: 
  * distributional Retrace algorithm (off-policy)
  * prioritized experiment replay
* nets:
  * arch: LSTM
  * optim: ADAM
* on discrete-action Atari
  * 200 or 500 million frames
  * metric:
    * normalized score
    * mean rank
    * elo

## result
* Reactor > (Prioritized Dueling DQN, Categorical DQN) in terms of sample-efficiency
* Reactor > A3C in term of better run time
* Reactor is
  * sample-efficient due to the use of memory replay, and
  * numerical efficient since it uses multi-step returns.
* contrib:
  Distributional Retrace,
  beta-LOO policy gradient estimate, and
  contextual priority tree (prioritized sequence replay)

## background
* Much of the recent work can be divided into two categories
  * those of which that, often building on the DQN framework,
    act eps-greedily according to an action-value function and
    train using mini-batches of transitions sampled from an experience replay buffer
    * value-function agents benefit from improved sample complexity,
    * but tend to suffer from long runtimes
      (e.g. DQN requires approximately a week to train on Atari).
  * the actor-critic agents,
    * train on transitions collected by multiple actors running, and
      often training, in parallel (Schulman et al., 2017; Vezhnevets et al., 2017).
    * train on each trajectory only once,
      thus tend to have worse sample complexity.
* In off-policy learning it is very difficult to produce an unbiased sample $R(\hat{a})$ of $Q^{\pi}(\hat{a}) 
  when following another policy $\mu$. 
  * This would require using full importance sampling correction along the trajectory.

## comment
* essentially: Reactor = DQN + A3C + Retrace + beta-leave-one-out + prioritized experiment replay
* new policy grad estimate: beta-leave-one-out
* for comparisons, this work uses reported scores from other papers
* (-) no xprmt on continuous action space; only atari tasks
* (?) numerical efficent=... ? is this computational efficient, so fast to compute?
 * ans: yes, it is about the speed of reward propagation

