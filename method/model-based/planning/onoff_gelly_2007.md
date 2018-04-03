# Combining Online and Offline Knowledge in UCT
* Sylvain Gelly, David Silver
* International Conference on Machine Learning, Corvallis, OR, 2007

## problem
* combine the advantages of both approaches.
  * UCT is a sample-based search algorithm (online)
  * the TD(λ) algorithm (offline) with action-value fn approximation

## idea
* 3 approaches for combining offline and online value functions in the UCT algorithm.
  * a: the offline value function is used **as a default policy** during Monte-Carlo simulation.
    (used to complete episodes beyond the UCT search tree.)
  * b: the UCT value function is **combined with** a rapid online estimate of action values.
    (a rapid action value estimate can be used to boost initial learning)
  * c: the offline value function is used **as prior knowledge** in the UCT search tree.
    (used to initialise the value function within the UCT tree)
* combine
  * the general knowledge accumulated by an offline reinforcement learning algorithm, with
  * the local knowledge found online by sample-based search.
* UCT-RAVE forms a rapid action value estimate for action a in state s, and combines this online knowledge into UCT.
  * average the returns of all episodes in which a is selected at any subsequent time.
    (Normally, Monte-Carlo methods estimate the value by
    averaging the return of all episodes in which a is selected immediately.)
  * to use the rapid estimate initially, but use the original UCT estimate in the limit.
    To achieve this, we use a linear combination of the two estimates, with a decaying weight

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
* the UCT algorithm
  (is a value-based reinforcement learning algorithm,
  a tabular method and does not generalise between states)
  * builds a search tree,
  * estimating the value function at each state by Monte-Carlo simulation
  * After each simulated episode,
    * the values in the tree are updated online and
    * the simulation policy is improved with respect to the new values.

## comment
* note: offline using value-based, i.e TD(lambda), not policy-based
