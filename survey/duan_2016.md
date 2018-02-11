# Benchmarking Deep Reinforcement Learning for Continuous Control

## Task
* Basic (5):
  * Cart-Pole Balancing (Stephenson, 1908; Donaldson, 1960; Widrow, 1964; Michie & Chambers, 1968), 
  * Cart-Pole Swing Up (Kimura & Kobayashi, 1999; Doya, 2000), 
  * Mountain Car (Moore, 1990), 
  * Acrobot Swing Up (DeJong &Spong, 1994; Murray&Hauser, 1991; Doya, 2000), and 
  * Double Inverted Pendulum Balancing (Furuta et al., 1978).
* Locomotion (6):
  * Swimmer (Purcell, 1977; Coulom, 2002; Levine & Koltun, 2013; Schulman et al., 2015a), 
  * Hopper (Murthy & Raibert, 1984; Erez et al., 2011; Levine & Koltun, 2013; Schulman et al., 2015a), 
  * Walker (Raibert&Hodgins, 1991; Erez et al., 2011; Levine & Koltun, 2013; Schulman et al., 2015a), 
  * Half-Cheetah (Wawrzynski, 2007; Heess et al., 2015b), 
  * Ant (Schulman et al., 2015b), Simple Humanoid (Tassa et al., 2012; Schul- man et al., 2015b), and 
  * Full Humanoid (Tassa et al., 2012).
* Partially Observable (on basic tasks: 3 x 5):
  * Limited Sensors
  * Noisy Observations and Delayed Actions
  * System Identification
* Hierarchical
  * Locomotion + Food Collection
  * Locomotion + Maze
  
## Algorithms
* Batch Algorithms
  * REINFORCE (Williams, 1992)
  * Truncated Natural Policy Gradient (TNPG) (Peters et al., 2003; Bagnell & Schneider, 2003; Schulman et al., 2015a)
  * Reward-Weighted Regression (RWR) (Peters & Schaal, 2007; Kober & Peters, 2009) _(no hyperparameter tuning)_
  * Relative Entropy Policy Search (REPS) (Peters et al., 2010)
  * Trust Region Policy Optimization (TRPO) (Schulman et al., 2015a)
  * Cross Entropy Method (CEM) (Rubinstein, 1999; Szita & Lorincz, 2006) _(gradient-free)_
  * Covariance Matrix Adaption Evolution Strategy (CMA-ES) (Hansen & Ostermeier, 2001) _(gradient-free)_
* Online Algorithms
  * Deep Deterministic Policy Gradient (DDPG) (Lillicrap et al., 2015)
* Recurrent Variants

## Experiment Setup
* Hyperparameter Tuning
  * a grid search of hyperparameters is performed
  * Each choice of hyperparameters is executed under five random seeds.
  * The criterion for the best hyperparameters: `mean(returns) − std(returns)`. 
    This metric selects against large fluctuations of performance due to overly large step sizes.
  * try both of the best hyperparameters found in the same category, and 
    report the better performance of the two. 
    This gives us insights into both the maximum possible performance when extensive hyperparameter tuning is performed, 
    and the robustness of the best hyperparameters across different tasks.  
* Baseline
  * a linear function as the baseline with a time-varying feature vector
  * subtract a baseline from the empirical return to re- duce variance of the optimization (?)
 
 ## Results
 * Both TNPG and TRPO:
   * outperform other batch algorithms by a large margin on most tasks, 
   * confirming that constraining the change in the policy distribution results in more stable learning
 * TRPO , compared to TNPG,
   * offers better control over each policy update by performing a line search in the natural gradient direction to 
   ensure an improvement in the surrogate loss function.
 * CEM (grad-free):
   * Even when training deep neural network policies with thousands of parameters, 
     CEM achieves very good performance on cerain basic tasks such as Cart-Pole Balancing and Mountain Car, 
     suggesting that the dimension of the searching parameter is not always the limiting factor of the method. 
   * However, the performance degrades quickly as the system dynamics becomes more complicated.
 * DDPG: 
   * able to converge significantly faster on certain tasks like Half-Cheetah due to its greater sample efficiency. 
   * However, it was less stable than batch algorithms, and 
   * the performance of the policy can degrade significantly during training. 
   * more susceptible to scaling of the reward.
 * Partially Observable Tasks:
   * recurrent policies can find better solutions than feed-forward policies in Partially Observable Tasks but 
   recurrent policies are also more difficult to train.
   * derivative-free algorithms like CEM and CMA-ES work considerably worse with recurrent policies
 * Hierarchical Tasks:
   * all of our implemented algorithms achieve poor performance on the hierarchical tasks
   * an interesting direction to develop algorithms that can automatically discover and 
   exploit the hierarchical structure in these tasks.
* Among the implemented algorithms, TNPG, TRPO, and DDPG are effective methods for training deep neural network policies.
