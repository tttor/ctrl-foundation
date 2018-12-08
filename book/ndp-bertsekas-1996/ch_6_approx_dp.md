# ch_6_approx_dp.md

* interested in approximation of cost-to-go fn $J^{\mu}$ of a given policy $\mu$
  * via a fn that given a state $i$ produces an approx $\tilde{J}(i, r)$ of $J^{\mu}(i)$
    * or given a contrl $u$, an approximation $\tilde{Q}(i, u, r)$ of $Q^{\star}(i, u)$
    * involving a parameter vector $r$
    * Q: why does $\tilde{Q}$ always approximate $Q^{\star}$?
      can it approximate $Q$?
* look up table as a limiting form of an approximate representation
* choices of
  * approximation architecture
  * training algorithm
* Once approximation is introduced,
  * convergence to $J^{\star}$ can not be expected,
    eg simply because it may not within the set of fn thah can be represented exactly
    by the chosen architecture
  * finiteness of the state space is no longer required
* aim to investigate: does a given algor converge?
  * leading to:
    * if it does, is the limit desirable, eg close to $J^{\star}$?
    * if not, does it oscillate within some small neighborhood of $J^{\star}$?
  * introduce:
    * epsilon, that characterize the power of the approx architecture,
      eg $\epsilon$ as the minimum of $||\tilde{J} - J^{\star}$
      * depends on the number of free parameter in the fn approx and
        the smoothness properties of the fn to be approximated
    * an amplification factor of at most $c$,
      if an algor is guaranteed to converge to a region of radius $c \times \epsilon$
      around $J^{\star}$
      * consider the worst case over all possible problems, so $c$ is problem independent

# 6.1 Generic Issues
TODO
