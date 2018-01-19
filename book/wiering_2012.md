# wiering_2012.md
@book{Wiering2012,
 author = {Wiering, Marco and van Otterlo, Martijn},
 title = {Reinforcement Learning: State-of-the-Art},
 year = {2012},
 isbn = {364244685X, 9783642446856},
 publisher = {Springer Publishing Company, Incorporated},
}

## 18: Reinforcement Learning in Robotics: A Survey

## 19: Conclusions, Future Directions and Outlook
Online planning:
* Monte Carlo Tree Search (MCTS)
* Model-based predictive control (MPC)

To use adaptive state partitioning to cluster similar states in an abstract
state, and to estimate transition probabilities between abstract states given some
discrete action. This approach may lead to models which do not obey the Markov
property anymore, and therefore it can make sense to combine them with memory
of previous states and actions.

Safe exploration and issues for real-time learning. When RL is applied directly
on robots or for controlling other physical devices, it would be very important that
the system is not damaged by the adaptive controllers that often learn without any
form of a-priori knowlegde, i.e., from Tabula Rasa. Also in the case of training RL
agents that interact with human users, it is not desirable that the RL agent explores
many actions so that the human user can be frustrated by the stupid actions of the
agent (Westra, 2011). Therefore, in such cases it may be necessary to combine RL
with pre-existing, safe, controllers. RL can then be used to change the output of the
controller in many circumstances, but the controller may also prevent the RL agent
from changing its generated actions.

19.2.1 Things That Are Not Yet Known:
* What is the best function approximator?
* Convergence proofs for general algorithms.
* Optimal exploration.
* Scaling up issues: to solve basically any control problem
* How does the brain do RL?

19.2.3 Interesting Directions
* Better world modelling techniques.
* Highly parallel RL.
* Combining RL with learning from demonstration.
* Novel queueing problems.
* RL for learning to play very complex games.

19.2.4 Experts on Future Developments
* Ashvin Shah:
autonomous development of useful abstractions and hierarchies so that re-
liance on prior knowledge and guidance can continue to be limited.
* Lucian Busoniu:
the scarcity of convincing benchmarks, especially in the
area of RL applied to physical systems, where RL is often still benchmarked on
problems that are simple and/or solvable by more classical techniques, such as the
car on the hill, inverted pendulum, or bicycle balancing. In this context of real-time
control of physical systems, a fundamental requirement that has to be addressed is
guaranteeing safety: the learning process must not damage the system or endanger
its users. The interplay between this requirement and exploration is expected to play
a key role here, as are control-theoretic insights such as those into the stability of
systems.
* Todd Hester:
will focus on algorithms that
are simultaneously sample efficient enough to work with limited data even in large,
continuous state spaces and computationally efficient enough to work in real time.
Model-based RL
* Lihong Li:
What we need is a mathematical theory on generalization for function approximation in RL.
* Ann Nowé:
multi-agent RL: in heterogeneous, unknown interactions.
* Frans Oliehoek:
to deepen our understanding of generalization and function approximation, especially in combination with feature selection methods.
The
problem with the notion of state and the associated Markov property is that they
trivialize the dynamic prediction problem. The curse of dimensionality is a direct
consequence of this and I believe that it can be mitigated by explicitly learning,
representing and exploiting the influence of state variables, features and actions on
each other.
* Jan Peters:
return back to the basic questions and solve these with more solid answers
as done in supervised learning, while working on better applications;
to look more at the primal problem
of RL (as done e.g., in (Peters et al, 2010)) and look how changes in the primal
change the dual.
* Shimon Whiteson:
will probably place an increasing emphasis on getting humans in the loop;
much remains to be done to exploit
developments from the field of human-computer interaction, better understand what
kinds of prior knowledge humans can express, and devise methods for learning from
the implicit and explicit feedback they can provide. The field of RL could benefit
from the development of both richer representations for learning and more practical
strategies for exploration;
In addition, even the most efficient strategies for exploration are
much too dangerous for many realistic tasks. An important goal is the development
of practical strategies for safely exploring in tasks with substantial risk of catas-
trophic failure.

## comments
* priority:
  * 19 Conclusions, Future Directions and Outlook
  * 18 Reinforcement Learning in Robotics: A Survey
  * 11 Bayesian Reinforcement Learning
  * 4 Learning and Using Models
  * 7 Reinforcement Learning in Continuous State and Action Spaces
