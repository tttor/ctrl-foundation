# Q-Prop: Sample-Efficient Policy Gradient with An Off-Policy Critic
* Shixiang Gu, Timothy Lillicrap, Zoubin Ghahramani, Richard E. Turner, Sergey Levine
* iclr2017: oral
* https://openreview.net/forum?id=SJ3rcZcxl

## problem
*  high sample complexity of deep RL in the real world

## idea: q-prop
* aim to develop methods that combine
  * the stability of policy gradients with
  * the efficiency of off-policy RL
* Q-Prop,
  * a policy gradient method that
    uses a Taylor expansion of the off-policy critic as a control variate.
* use control variate theory to derive two variants of Q-Prop
  with conservative and aggressive adaptation

## setup
* task:
  * OpenAI Gym’s MuJoCo

## result
* Q-Prop
  * is both sample efficient and stable, and
  * effectively combines the benefits of on-policy and off-policy methods.
* conservative Q-Prop
  * provides substantial gains in sample efficiency over TRPO with GAE
  * improves stability over deep deterministic policy gradient (DDPG)
* Q-prop > (TRPO, DDPG)

## comment
* TODO: finish!
