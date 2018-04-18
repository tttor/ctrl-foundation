# https://www.alexirpan.com/2018/02/14/rl-hard.html
* Deep Reinforcement Learning Can Be Horribly Sample Inefficient
* Many Problems are Better Solved by Other Methods
(If You Just Care About Final Performance)
* Reward Function Design is Difficult
* Even Given a Good Reward, Local Optima Can Be Hard To Escape
* Even When Deep RL Works, It May Just Be Overfitting to Weird Patterns In the Environment
* Even Ignoring Generalization Issues, The Final Results Can be Unstable and Hard to Reproduce
*  outside of these successes, it’s hard to find cases where deep RL has created practical real world value.
* The problem with trying to solve everything with RL is that you’re trying to solve several very different environments with the same approach. It’s only natural that it won’t work all the time.
* common properties that make learning easier:
  * It is easy to generate near unbounded amounts of experience.
  * The problem is simplified into an easier form.
  * There is a way to introduce self-play into learning.
  * There’s a clean way to define a learnable, ungameable reward
  * If the reward has to be shaped, it should at least be rich
* some futures
  * Local optima are good enough
  * Hardware solves everything
  * Add more learning signal
  * Model-based learning unlocks sample efficiency
  * Use reinforcement learning just as the fine-tuning step
  * Reward functions could be learnable
  * Transfer learning saves the day
  * Good priors could heavily reduce learning time
  * Harder environments could paradoxically be easier
