# literature-review: actor critic

* onpolicy, offpolicy
* onpolicy
  * natural actorcritic
  * Vanilla actor-critic methods are on-policy only
* actorcritic vs criric as baseline
* why actorcritic
  * var in actor only
  * bias in critic only
* the timeline, history
* data efficiency and stability

* to ensure exploration in the policy
  * to use entropy regularization to ensure exploration in the policy,
    which is a common practice in policy gradient (Williams & Peng, 1991; Mnih et al., 2016).
  * to use KL-divergence as a constraint on how much deviation is permitted from a prior policy
    (Bagnell & Schneider, 2003; Peters et al., 2010; Schulman et al., 2015; Fox et al., 2015).

* taxonomy, differentiator

<!--
Matthew Hausknecht and Peter Stone. On-policy vs. off-policy updates for deep reinforcement
learning. Deep Reinforcement Learning: Frontiers and Challenges, IJCAI 2016 Workshop, 2016.

Nicolas Heess, David Silver, and Yee Whye Teh. Actor-critic reinforcement learning with energy-
based policies. In JMLR: Workshop and Conference Proceedings 24, pp. 43–57, 2012.
 -->
