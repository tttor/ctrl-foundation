# Combining policy gradient and q-learning
* Brendan O’Donoghue, Rémi Munos, Koray Kavukcuoglu & Volodymyr Mnih
* Published as a conference paper at ICLR 2017

## problem
* vanilla online variants are
  * on-policy only and
  * not able to take advantage of off-policy data

## idea:  PGQL: policy gradient and Q-learning.
* combines policy gradient with off-policy Q-learning,
  drawing experience from a replay buffer.
* a connection between the fixed points of the regularized policy gradient algorithm and the Q-values
  * allows us to estimate the Q-values from the action preferences of the policy,
    to which we apply Q-learning updates
  *  allows us to derive an estimate of the Q-values from the current policy,
    which we can refine using off-policy data and Q-learning.

## result
* establish an equivalency between action-value fitting techniques and actor-critic algorithms,
  * showing that regularized policy gradient techniques can be interpreted as
    advantage function learning algorithms
* better data efficiency and stability of PGQL when compared to actor-critic or Q-learning alone
* tested PGQL on the full suite of Atari games and
  achieved performance exceeding that of both asynchronous advantage actor-critic (A3C) and Q-learning

## comment
* TODO: read more
