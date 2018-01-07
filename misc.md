# misc, untracked, unknown sources

Most existing RL approaches assume full observability, running on MDP.
RL is formalized as MDP, but in which agents only knows about the sets of possible states and actions.
The dynamics, $P(s'|s,a)$, and the reward function, $R(s,a,s')$ are initially \emph{unknown};
otherwise we have planning problems.

RL is difficult because:
* the blame attribution problem:
the responsible action may have occurred a long time before the reward was received
* even if the dynamics of the world does not change,
the effect of an action of the agent depends on what the agent will do in the future.
* the explore-exploit dilemma

