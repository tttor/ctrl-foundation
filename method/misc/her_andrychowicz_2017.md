# Hindsight Experience Replay
Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

## problem
* sparse (and binary) rewards
* complicated reward engineering

## observation
* One ability humans have is to learn almost as much from achieving an undesired outcome as from the desired one.

## idea: HER (Hindsight Experience Replay)
* to **replay** each episode **with a different goal** than the one the agent was trying to achieve, 
  e.g. one of the goals which was achieved in the episode.

## setup
* tasks: pushing, sliding, and pick-and-place
* demonstrated that with DQN and DDPG

## result
* showed that the policy for the pick-and-place task performs well on the physical robot without any finetuning
