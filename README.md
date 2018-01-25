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

## People
### young: >= 2008
* Hanna Kurniawati, 2008
* David Silver, 2009: sampling-based planning (for go games)
* Arthur Quez, 2015
* Stephane Ross, 2013
* Jens Kober, 2012
* Pieter Abbeel, 2008: inverse rl (for flying helicopters)
* Todd Hester, 2012
* George Konidaris, 2011

### old: < 2008
* Richard Sutton
* Andrew Barto
* Csaba Szepesvári
* Andrew Ng, 2003
* Michael Littman
* Sebastian Thrun
* Leslie Kaebling
* Joelle Pineau, 2004
* Jan Peters
* Masashi Sugiyama
* Satinder Singh

