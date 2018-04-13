# Deep RL Bootcamp Lecture 4B Policy Gradients Revisited
* aug 2017
* https://www.youtube.com/watch?v=tqrcjHuNdmQ

* stoc policy:
  * allow to do exploration
  * make opt problem smooth

* logp: logitp

* n_neurons, n_params
  * layer1: `(80 * 80) * 200 + 200` # + 200 for bias
  * layer2: `200 * 1 + 1` # +1 for bias
  * total: `~1.3M` params

* tie to supervised learning
  *  assume we have label of correct action at each step
    * we know correct action at each step
  * max `\sum_i log p (y_i | x_i)`
    * max the probability of correct action to take given input
  * but recall in RL we do not have labels, so
    * try bunch of stuff (use rollout policy), see what happens
    * in the future, do more stuff that workED
  * make fake dataset (with fake label) with rollout
    * dataset is a set of (state `s`, action `a`, return `G(s)`)
    * for samples that eventually win:
      * pretend actions we took was the correct label
      * max `log p(y_i | x_i)`
    * for samples that eventually lost:
      * * pretend actions we took was the wrong label
      * max `(-1) * log p(y_i | x_i)`
  * in summary:
    * we have no label, so
      * fake label from action we take
      * sample `y_i \sim p(\cdot|x_i)`
    * once we collect a batch of rollout:
      maximize `\sum_i A_i * log p(y_i | x_i)`
      * `A_i`: scaler, e.g return
      * `A_i` should be **high** if we **want to encourage** this action in the future
      * `A_i` should be **low** if we do **not want to discourage** this action in the future
      * +ve (positive) advantage: make action **more** likely in the future for that state
      * -ve (negative) advantage: make action **less** likely in the future for that state

* follow-up:
  * CNN: conv net
