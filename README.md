# rl-foundation

## Topics in RL:
Deep RL,
Bayesian RL,
RL in POMDP,
Transfer learning in RL,
Hierarchical RL,
Curriculum learning,
Inverse RL (imitation/apprenticeship learning),
Multiagent RL,
Evolutionary RL,

## Major taxonomy
* model-based **vs** model-free
* value-iteration **vs** policy-search
* episodic **vs** continuing tasks
* cumulative discounted **vs** average rewards

## Quotes
Richard S. Sutton: <br />
Reinforcement Learning: Past, Present and Future?:
"Just as reinforcement learning present took a step away from the ultimate goal of reward to
focus on value functions, so reinforcement learning future may take a further step
away to focus on the structures that enable value function estimation [...] In psy-
chology, the idea of a developing mind actively creating its representations of the
world is called constructivism. My prediction is that for the next tens of years rein-
forcement learning will be focused on constructivism."

Marco Wiering, Martijn van Otterlo: <br/>
Two dominant books:
* Introduction to reinforcement learning by Rich Sutton and Andy Barto from 1998.
  From an artificial intelligence perspective.
* Neuro-dynamic programming by Dimitri Bertsekas and John Tsitsiklis in 1996.
  From the standpoint of operations research.

## Misc, anonymous, untracked, unknown sources
RL is formalized as MDP, but in which agents only knows about the sets of possible states and actions.
The dynamics, $P(s'|s,a)$, and the reward function, $R(s,a,s')$ are initially unknown; otherwise we have planning problems.

RL is difficult because:
* the blame attribution problem:
  the responsible action may have occurred a long time before the reward was received
* even if the dynamics of the world does not change,
  the effect of an action of the agent depends on what the agent will do in the future.
* the explore-exploit dilemma

RL: learning through interaction with the environment with limited prior knowledge and guidance
