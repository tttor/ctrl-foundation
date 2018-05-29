# DESPOT: Determinized Sparse Partially Observable Tree
* Nan Ye, Adhiraj Somani, David Hsu, Wee Sun Lee
* https://arxiv.org/abs/1609.03250

## problems
* online POMDP planning

## ideas
* determinized sparsed believe tree:
  * a fixed set of $K$ randomly sampled scenarios, similar to~\cite{Ng2000}
  * sampling states from a belief and sampling observations
  * has $O(|A|^D K)$ belief nodes, instead of $O(|A|^D |Z|^D)$
  * deterministic simulative model
* regularized weighted discounted utility
  * regularize the empirical value of a policy by adding a term that penalizes large policy size; 
    a policy optimized for finitely many sampled scenarios may not be optimal in general, as many scenarios are not sampled.
  * to control overfitting the sampled scenarios;
  * balances between the estimated performance value of a policy and the policy size

## setups
* sampling and anytime heuristic search,
* branch and bound pruning,
* the belief as a set of sampled states,
* a standard particle filtering method, sequential importance resampling (SIR),

## results
* $K \in O(|\phi| ln(|\phi||A||Z|))$ is sufficient
* metrics (with one standard deviation): expected total reward
* tasks: tag, laser tag, rock sample, pocman, bridge crossing
* DESPOT outperforms SARSOP, AEMS2, POMCP in most tasks
* used to control the vehicle speed along the planned path;
for autonomous golf-cart driving in a crowded, dynamic environment (Bai2015)

## misc
* as part of the APPL library\footnote{\url{http://bigbird.comp.nus.edu.sg/pmwiki/farm/appl/}}.
* IS-DESPOT~\cite{Luo2016} applies importance sampling to DESPOT.
It samples states based on their ``importance'', instead of their occurance probability.
It avoids missing ``critical'' states with large reward/penalty but having low probability.
IS-DESPOT learns the function of expectation and variance of $(v|s,\pi)$.
It extracts features from every state.
The learning data are generated from many offline runs of DESPOT.
