# Hindsight Experience Replay
* nips2017: poster
* https://papers.nips.cc/paper/7090-hindsight-experience-replay

## problem
* sparse (and binary, not informative) rewards
* complicated reward engineering

## observation
* One ability humans have is to learn almost as much from achieving an undesired outcome as from the desired one.
* the goal being pursued influences the agent’s actions but **not** the environment dynamics 
  * therefore, we can replay each trajectory with an arbitrary goal assuming that we use an off-policy RL algorithm

## idea: HER (Hindsight Experience Replay)
* to **replay** each episode **with a different goal** than the one the agent was trying to achieve, 
  e.g. one of the goals which was achieved in the episode.
* to **re-examine** this trajectory with a different goal 
  * while this trajectory may not help us learn how to achieve the state g, 
    it definitely tells us something about how to achieve the state $s_T$.
  * This information can be **harvested** by using an off-policy RL algorithm and 
    experience replay where we replace g in the replay buffer by $s_T$.
* after experiencing some episode s0,s1,. .., sT,
  we store in the replay buffer every transition $s_t \mapsto s_{t+1} not only with 
  the original goal used for this episode but also with a subset of other goals. 

## assumption
* every goal $g \in G$ corresponds to some predicate $f_g: S \mapsto {0, 1}$ and that 
  the agent’s goal is to achieve any state s that satisfies $f_g(s) = 1$.
* given a state s we can easily find a goal g which is satisfied in this state.

## setup
* A motivating example: a bit-flipping environment
* tasks: pushing, sliding, and pick-and-place (with MuJoCo)
* use: DQN, DDPG, UVFA, Adam optimizer
* policies are represented as Multi-Layer Perceptrons (MLPs) with Rectified Linear Unit (ReLU)
* Goals is with some fixed tolerance
* the initial position of the gripper is fixed, gripper orientation is fixed
* The **box position** was predicted using a separately trained CNN using **raw** fetch head camera images
* evaluation metric: success rate (average, highest)

## result
* showed that the policy for the pick-and-place task performs well on the physical robot without any finetuning
* training an agent to perform multiple tasks can be easier than training it to perform only one task
* HER learns faster if training episodes contain multiple goals
* Initially, it was not robust to small errors in the box position estimation because 
  it was trained on perfect state coming from the simulation. After retraining the policy with gaussian noise (std=1cm) added to observations

## misc
* HER may be seen as a form of implicit curriculum as the goals used for replay naturally shift from 
  ones which are simple to achieve even by a random agent to more difficult ones

## comment
* now, the fn approx is deep neural nets
* what (useful) info can be harvested on each step?
  * they said this in Subsec 3.3. already
* again, essentially, this learn the dynamic model
* for pickandplace task, it is said "....the target position is in the air and..."
  * well, this is not real pickandplace, it should place the obj back on tabletop :)
* several experiment strategy: hard to understand
  
