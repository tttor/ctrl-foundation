# Combining policy gradient and q-learning
* Brendan O’Donoghue, Rémi Munos, Koray Kavukcuoglu & Volodymyr Mnih
* iclr2017: poster
* https://arxiv.org/abs/1611.01626
* https://openreview.net/forum?id=B1kJ6H9ex

## problem
?

## idea: PGQL: policy gradient and Q-learning.
* combines policy gradient with off-policy Q-learning,
  drawing experience from a replay buffer.
* a connection between **the fixed points of the regularized policy gradient algorithm** and **the Q-values**
  * allows us to estimate the Q-values from the action preferences of the policy,
    to which we apply Q-learning updates
  * allows us to derive an estimate of the Q-values from the current policy,
    which we can refine using off-policy data and Q-learning.

## setup
* Atari task

## result
* PGQL > A3C
* establish an equivalency between action-value fitting techniques and actor-critic algorithms,
  * showing that regularized policy gradient techniques can be interpreted as
    advantage function learning algorithms
* better data efficiency and stability of PGQL
  when compared to actor-critic or Q-learning alone
* show that TD-actor-critic (Konda & Tsitsiklis, 2003) is equivalent to
  expected-SARSA (Sutton & Barto, 1998, Exercise 6.10) with Boltzmann exploration where
  the Q-values are decomposed into advantage function and value function.

## background
* vanilla online variants are
  * on-policy only and
  * not able to take advantage of off-policy data

## comment
?
