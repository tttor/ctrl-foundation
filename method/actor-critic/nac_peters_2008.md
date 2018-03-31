# Natural Actor-Critic
* Jan Peters, Stefan Schaal
* Neurocomputing 71 (2008) 1180–1190

## problem


## idea: natural actor-critic
* The actor updates are
  achieved using stochastic policy gradients employing Amari’s natural gradient approach, while
* the critic obtains both the natural policy gradient and
  additional parameters of a value function simultaneously by linear regression.


## setup
* baseball swing robot

## result
* actor improvements with **natural policy gradients** are particularly appealing as
  these are independent of coordinate frame of the chosen policy representation, and
  can be estimated more efficiently **than regular policy gradients**
