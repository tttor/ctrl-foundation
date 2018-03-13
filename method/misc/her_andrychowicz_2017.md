# Hindsight Experience Replay
Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

## problem
* sparse (and binary, not informative) rewards
* complicated reward engineering

## observation
* One ability humans have is to learn almost as much from achieving an undesired outcome as from the desired one.

## idea: HER (Hindsight Experience Replay)
* to **replay** each episode **with a different goal** than the one the agent was trying to achieve, 
  e.g. one of the goals which was achieved in the episode.
* to **re-examine** this trajectory with a different goal 
  * while this trajectory may not help us learn how to achieve the state g, 
    it definitely tells us something about how to achieve the state $s_T$.
  * This information can be **harvested** by using an off-policy RL algorithm and 
    experience replay where we replace g in the replay buffer by $s_T$.
    
## assumption
* every goal $g \in G$ corresponds to some predicate $f_g: S \mapsto {0, 1}$ and that 
  the agent’s goal is to achieve any state s that satisfies $f_g(s) = 1$.
* given a state s we can easily find a goal g which is satisfied in this state.

## setup
* A motivating example: a bit-flipping environment
* tasks: pushing, sliding, and pick-and-place
* use: DQN, DDPG, UVFA, 

## result
* showed that the policy for the pick-and-place task performs well on the physical robot without any finetuning
* training an agent to perform multiple tasks can be easier than training it to perform only one task

## comment
* now, the fn approx is deep neural nets
* what (useful) info can be harvested on each step?
