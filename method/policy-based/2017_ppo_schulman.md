# Proximal Policy Optimization Algorithms
* John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov
* https://arxiv.org/abs/1707.06347
* https://blog.openai.com/openai-baselines-ppo/
* https://stackoverflow.com/questions/46422845/what-is-the-way-to-understand-proximal-policy-optimization-algorithm-in-rl
* https://www.youtube.com/watch?v=gqX8J38tESw&feature=youtu.be&t=14m1s
* https://www.youtube.com/watch?v=5P7I-xPq8u8
* https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Deep-Reinforcement-Learning-Through-Policy-Optimization
* https://github.com/ikostrikov/pytorch-a2c-ppo-acktr
  * https://github.com/tttor/pytorch-a2c-ppo-acktr
* https://learningai.io/projects/2017/07/28/ai-gym-workout.html
  * https://github.com/pat-coady/trpo
  
## problem
* looking for a method that is
  scalable (to large models and parallel implementations),
  data efficient, and
  robust (i.e., successful on a variety of problems without hyperparameter tuning).
  * Q-learning [Mni+15] (with function approximation) fails on many simple problems and is poorly understood,
    * DQN works well with discrete action spaces,
    * **not been demonstrated** to perform well on continuous control, see Duan et al. [Dua+16].
  * vanilla policy gradient methods, eg A3C
    * have poor data effiency and robustness;
  * TRPO [Sch+15b]:
    * relatively complicated, and
    * not compatible with architectures that include noise (such as dropout) or
      parameter sharing (between the policy and value function, or with auxiliary tasks)

## idea: PPO
* policy gradient methods that alternate between
  * sampling data (from the policy) through interaction with the environment, and
  * optimizing a "surrogate" objective function using stochastic gradient ascent
    (performing several epochs of optimization on the sampled data.)
* a novel objective function
  * that enables multiple epochs of minibatch updates.
    * use multiple epochs of stochastic gradient ascent to perform each policy update
      * cf: standard policy gradient methods perform one gradient update per data sample
    * alternate between sampling data from the policy and
      performing several epochs of optimization on the sampled data
  * with clipped probability ratios,
    * which forms a pessimistic estimate (i.e., lower bound) of the performance of the policy.
    * why clipped?
      * based on empirical experiment
        > Our experiments compare the performance of various different versions of the surrogate objective, and
          find that the version with the clipped probability ratios performs best.
      * Without a constraint, maximization of L CPI would lead to an excessively large policy update
        (L CPI: loss with corservative policy iteration)
* The proposed objective function: $L^{Clipped} = min(L^{UnclippedCPI}, L^{ClippedCPI})$ ... Equ. 7
  * take the minimum of the clipped and unclipped objective,
    * so the final objective is a lower bound (i.e., a pessimistic bound) on the unclipped objective.
  * modify L_CPI, to penalize changes to the policy that move rt(θ) away from 1
  * the KL penalty performed worse than the clipped surrogate objective
* If using a neural network architecture that shares parameters
  between the policy and value function, we must use a loss function that combines the policy
  surrogate and a value function error term.
  * can further be augmented by adding an entropy bonus to ensure sufficient exploration, as suggested in past work
  * Equ 9
* have the stability and reliability of trust-region methods
* much simpler to implement, more general, and have better sample complexity (empirically)

## setup
* Use Adam, SGD
* searching over hyperparameters for each algorithm variant,
  * used 7 simulated robotics tasks2 implemented in OpenAI Gym [Bro+16],
  * do one million timesteps of training on each one.
* a fully-connected MLP with two hidden layers of 64 units, and tanh nonlinearities,
 outputting the mean of a Gaussian distribution, with variable standard deviations, following [Sch+15b; Dua+16].
* NOT share parameters between the policy and value function (so coefficient c1 is irrelevant), and
  we don’t use an entropy bonus.
* Each algorithm was run on all 7 environments, with 3 random seeds on each.
* compare the surrogate objective LCLIP to several natural variations and ablated versions.
* If using a neural network architecture that **shares parameters**
  between the policy and value function, we **must use a loss function that combines** the policy
  surrogate and a value function error term.
  * can further be augmented by adding
    an entropy bonus to ensure sufficient exploration
* hyperparam, used for the Mujoco 1 million timestep benchmark
  * Horizon (T)
  * Adam stepsize
  * Num. epochs
  * Minibatch size
  * Discount (γ)
  * GAE parameter (λ)
  * clip_eps
* a fully-connected MLP with
  * two hidden layers of 64 units,
  * tanh nonlinearities, outputting the mean of a Gaussian distribution, with variable standard deviations,
* don’t share parameters between the policy and value
function (so coefficient c1 is irrelevant), and we don’t use an entropy bonus.
* run on all 7 environments, with 3 random seeds on each.
  * scored each run of the algorithm by
    computing the **average** total reward of the **last 100 episodes**
  * averaged over 21 runs to produce a single scalar for each algorithm setting
  * HalfCheetah, Hopper, InvertedDoublePendulum, InvertedPendulum, Reacher, Swimmer, and Walker2d, all “-v1”

## result
* PPO > TRPO
* On Atari: PPO > A2C > ACER

## comment
* What does this mean?
> With this scheme, we only ignore the change in probability ratio when it would make the objective improve,
and we include it when it makes the objective worse

* Why does clipping depend on A?
>  Figure 1 plots a single term (i.e., a single t) in LCLIP ; note that the probability ratio r is clipped at 1 − eps
or 1 + eps depending on whether the advantage is positive or negative.

* What limits the standard polgrad to one grad update per minibatch or why does PPO not have such limit?
  Is it because the surrogate loss/objective?
  * ans: the paper mentions
    > While it is appealing to perform multiple steps of optimization on this loss LP G using the same
      trajectory, doing so is not well-justified, and empirically it often leads to destructively large policy updates

* Should it be: grad update per minibatch?
> standard policy gradient methods perform one gradient update per data sample
  * note: standard pol grad requires `n_epoch==1` and using full-batch per agent update,
    and the way the grad is calculatee by taking the average of all sample gradient
* ? input dim of actor and critic nets?
  * ans: based on `baselines/baselines/ppo1/pposgd_simple.py`:
    * input: observation only (not like actkr, that uses input=(observ+action)
* ? should not this be:
  * the loss value is clipped \emph{at} its value at the ratio of
    $(1 + \epsilon)$ when $\hat{A} > 0$ \emph{or}  $(1 - \epsilon)$ when $\hat{A} < 0$
>  that the probability ratio r is clipped at $1 − \epsilon$ or $1 + \epsilon$
   depending on whether the advantage is positive or negative.
