# AEMS: Anytime Error Minimization Search

AEMS~\cite{Chaib-draa2007} does heuristic search in an OR-AND graph, where
belief states are represented as OR-nodes (must choose an action child node) and
actions are represented as AND-nodes (must choose all belief state chile nodes,
associated to different possible observations).

## idea
* to expand the fringe nodes that have highest expected errors contribution to the current belief.
  * Errors here refer to the estimation of the utilization value $V(b)$ in the current belief.
  * They formulated the actual errors as $\hat{\epsilon}(b) = U(b) - L(b)$.
