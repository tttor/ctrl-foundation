# ABT: Adaptive Belief Tree
abt_kurniawati_2013.md

## problem
* POMDP model changes during runtime (required when a robot operates in dynamic environments);
  * changes should occurs gradually, or only to some part of the environment;
  * changes here include any type of changes, namely:
    changes in transition, observation, and reward functions, as well as
    in state, action, observation spaces

## observation
* a change in the POMDP model is directly reflected as a change in the robot's behaviour at a particular set of state
* a change in one optimal mapping from a belief $b$, may affect the optimal policy at other beliefs that can reach $b$

## idea: ABT
* reuse, improve the existing policy (in the form of belief trees) from previous planning steps;
avoiding building the tree from scratch on each planning step
* explicitly represents the relation between beliefs, states, and their reachability information
via belief tree and associated episodes
* to identify which parts of the policy need to be updated, ABT only needs to find the episodes in $H$ that
contain states that are affected by the changes in the POMDP model
* structure the sampled states in a range tree

## setup
* monte carlo tree search~\cite{Browne2012},
* generative models,
* particle filters,
* UCB1 algorightm to select an action,
* Exp3 to select heuristics to do rollout,
* offline POMDP planning to obtain initial policy.

## results
* tasks (requiring the POMDP model to be modified several times during runtime):
  * underwater navigation:
  the number of states reduces while the number of observation increases
  * homecare and target finding:
  changes in transition functions
* metrics (with 0.95 confidence interval):
  * expected total reward
  * computation time: offline and online planning
* ABT significantly outperforms POMCP in all tasks

## misc
* implementation is available in TAPIR~\cite{Klimenko2014}.
* In terms of reusing some parts of the tree, there exists work such as \cite{Kearns1999, Ross2008,Chaib-draa2007};
  on policy deformation of offline POMDP in changing environment~\cite{Kurniawati2013}.
* The work of Kearns in "Approximate Planning in Large POMDPs via Reusable Trajectories" (arXiv:1011.1669v3)
  is relevant in terms of reusing some parts of the tree.
  It poses two interesting questions, namely:
  * how many calls to generative model must we make in order to have enough data to obtain an optimal policy? and
  * which calls should be made to the generative model in order to minimize the number of calls required?

## comments
* How many portion of the already-built tree is reused?
  * The paper does not report any percentage of reused subtrees.
* ABT is useful to adapt the plan whenever the POMDP model changes.
  * Notice, however, that the changes should be partial.
  * Otherwise, if the changes are extreme, then the chances of reusing subtrees are very low.
  * In one extreme where there are many changes, it is unlikely that previous subtrees remain relevant.
  * On the other extreme where there is no changes, ABT performance is relatively similar to POMCP, as stated in~\cite{Klimenko2014}.
  * How partial should the changes be? How to quantify such changes?
  * Also note that standard online approaches actually can deal with changing environments as they replan in every step.
  * Hsu said that they handles dynamic environment changes naturally, also as in~\cite{Shani2005}.
* confusing statement in Intro:
  "...-models only the known part of the environment and its dynamics (both stochastic and deterministic),...",
  * surely in planning, the model is given (being known) so the agent can not model something unknown;
    otherwise we have model-based RL (which consists of model learning and planning)
* the policy representation, i.e. a policy as a pair of belief and action, is \emph{not} new since
  by definition, a policy is a mapping from a belief to an action
* a statement in 4.2 Handling changes in the POMDP model:
  "...not focus on how to identify changes in the POMDP model... assume that
  either changes in the POMDP model can be identified easily by identifying changes
  in the environment map, or the user provides information on the set of affected state...";
  * this statement is somewhat unnecessary because the paper presents planning, not RL;
  * one interesting point is that the change identification is only approximate, for example, via learning;
  * however the paper seems to assume the exact change information is given
* need to include other online planning methods (in addition to POMCP) and
  other standard planning problems, such as rock-sample, tag
