# 9: On-policy Prediction with Approximation

* fn approximator:
  * to approx `v_{\pi}` from experience generated using a known policy `\pi`
  * `\hat{v}_{\pi}`is represented as a parameterized functional form with weight vector `w in R^d`;
    **not** as a table anymore
  * `\hat{v}(s,w) \approx v_{\pi}(s)`
  * `\hat{v}` can be:
    * a linear function in features of the state,
      with `w` the vector of feature weights.
    * a multi-layer artificial neural network,
      with `w` the vector of connection weights in all the layers.
    * a decision tree,
      where `w` is all the numbers defining the split points and leaf values of the tree.
  * the number of weights (the dimensionality of w) is **much less** than the number of states,
    `(d << |S|)`
* generalization
  * changing one weight changes the estimated value of many states
  * when a single state is updated,
    the change generalizes from that state to affect the values of many other states.
* function approximation makes RL applicable to **partially observable** problems,
  * If the parameterized function form for `\hat{v}` does **not allow**
    the estimated value to depend on certain aspects of the state, then
    it is just **as if** those aspects are unobservable.
* function approximation can **not augment**
  the state representation with **memories of past observations**

## 9.1 Value-function Approximation
* updates `s \mapsto u`
  * `s`: the (arbitrary) state updated,
      * cf `S_t`: state encountered in actual experience
  * `u`: the update target that `s`'s estimated value is shifted toward.
  * Monte Carlo update: `S_t \mapsto G_t`
  * TD(0): `S_t \mapsto R_{t+1} + \gamma \hat{v}(S_{t+1},w_t)`
  * n-step TD: `S_t \mapsto G_{t:t+n}`
  * DP: `s \mapsto E_{\pi}[  R_{t+1} + \gamma \hat{v}(S_{t+1},w_t) | S_t = s  ]`
