# Combining Online and Offline Knowledge in UCT
* Sylvain Gelly, David Silver
* International Conference on Machine Learning, Corvallis, OR, 2007

## idea
* 3 approaches for combining offline and online value functions in the UCT algorithm.
  * a: the offline value function is used **as a default policy** during Monte-Carlo simulation.
    (used to complete episodes beyond the UCT search tree.)
  * b: the UCT value function is **combined with** a rapid online estimate of action values.
    (a rapid action value estimate can be used to boost initial learning)
  * c: the offline value function is used **as prior knowledge** in the UCT search tree.
    (used to initialise the value function within the UCT tree)

## setup
* 9 × 9 Go against GnuGo 3.7.10.

## result
* on 3 proposed approaches
  * a: The first algorithm performs better than UCT with a random simulation policy, but
    surprisingly, worse than UCT with a weaker, handcrafted simulation policy.
  * b: The second algorithm outperforms UCT altogether.
  * c: The third algorithm outperforms UCT with hand-crafted prior knowledge.
* By learning a value function offline using TD(λ),
  we have demonstrated how the requirement for domain knowledge can be removed altogether.

## misc
* With larger branching factors it becomes increasingly important to
  simulate accurately, accelerate initial learning, and incorporate prior knowledge.
