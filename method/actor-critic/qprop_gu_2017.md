# Q-Prop: Sample-Efficient Policy Gradient with An Off-Policy Critic
* Shixiang Gu, Timothy Lillicrap, Zoubin Ghahramani, Richard E. Turner, Sergey Levine
* iclr2017: oral
* https://openreview.net/forum?id=SJ3rcZcxl

## problem
* high sample complexity of deep RL in the real world
  * policy gradient methods can only **effectively use on-policy samples**, 
    * they require collecting large amounts of on-policy experiences after each parameter update to the policy.
* DeepRL tend to be **sensitive to hyperparameter settings**, 
  * often requiring extensive hyperparameter sweeps to find good values,
  * Poor hyperparameter settings tend to produce unstable or non-convergent learning.

## observation
* Off- policy methods can instead use all samples, including off-policy samples, 
  by adopting temporal difference learning with experience replay. 
  * (+) much more sample-efficient. 
  * (-) convergence is in general not guaranteed with non-linear function approximators, and 
  * (-) practical convergence and instability issues typically mean that 
        extensive hyperparameter tuning is required to attain good results.
  * such as Q-learning and off-policy actor-critic methods 

## idea: q-prop
* aim to develop methods that combine
  * the stability of policy gradients with
  * the efficiency of off-policy RL
* to use the first-order Taylor expansion of the critic as a control variate, resulting in 
  * an analytical gradient term through the critic and 
  * a Monte Carlo policy gradient term consisting of the residuals in advantage approximations.
* use control variate theory to derive two variants of Q-Prop
  with conservative and aggressive adaptation

## setup
* task:
  * OpenAI Gym’s MuJoCo

## result
* Q-Prop
  * is both sample efficient and stable, and
  * effectively combines the benefits of on-policy and off-policy methods.
  * a policy gradient method that
    uses a **Taylor expansion** of the off-policy critic as a control variate.
  * can reduce the variance of gradient estimator without adding bias
* conservative Q-Prop
  * provides substantial gains in sample efficiency over TRPO with GAE
  * improves stability over deep deterministic policy gradient (DDPG)
* Q-prop > (TRPO, DDPG)

## comment
* TODO: finish!
