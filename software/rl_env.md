# Environment for RL
* see also: [simulator](https://github.com/tttor/rl-foundation/blob/master/software/simulator.md)

# OpenAI Gym
* https://github.com/openai/gym
* https://github.com/openai/gym/wiki/Table-of-environments
* https://stackoverflow.com/questions/44404281/openai-gym-understanding-action-space-notation-spaces-box
> `Box` means that you are dealing with real valued quantities
* v1 vs v2: https://stackoverflow.com/questions/48861523/how-to-solve-environment-error-in-open-ai-gym
> 2018-01-24: All continuous control environments now use mujoco_py >= 1.50. Versions have been updated accordingly to -v2, e.g. HalfCheetah-v2. Performance should be similar (see https://github.com/openai/gym/pull/834) but there are likely some differences due to changes in MuJoCo.
* https://stackoverflow.com/questions/48980368/list-all-environment-id-in-openai-gym

## observ and action dims
| env id | observ dim | action dim |
| :---   | :---       | :---       |
| Ant-v2 | 111 | 8 |
| HalfCheetah-v2 | 17 | 6 |

# Others
* https://github.com/openai/universe
* https://github.com/openai/roboschool
* https://github.com/openai/retro
