# policy-based
Here is for model-free policy-based approaches. </br>
For model-based policy-based approaches, goto [method/model-based/planning/policy-based](https://github.com/tttor/rl-foundation/tree/master/method/model-based/planning/policy-based).

## taxonomy
* gradient-free
  * cross-entropy method
* gradient-based: 
  * analytical (closed-form) solution:
    PILCO, PEGASUS 2000
  * based on policy gradient theorem: stochastic and deterministic
    * actor-critic:
      Deep DPG (Lilicrap, 2016), Recurrent DPG
    * actor-only:       
      TRPO (Schulman, 2015), PPO (Schulman, 2017), GPS (Levine, 2013)

## tutor
* Quora
  * https://www.quora.com/Why-does-the-policy-gradient-method-have-a-high-variance
  * https://www.quora.com/What-is-the-difference-between-policy-gradient-methods-and-actor-critic-methods
* Jan Peter: Policy Search: Methods and Applications
  * https://icml.cc/2015/tutorials/PolicySearch.pdf
* http://karpathy.github.io/2016/05/31/rl/
  * https://www.youtube.com/watch?v=tqrcjHuNdmQ
  * https://www.youtube.com/watch?v=PDbXPBwOavc
  * https://medium.com/@dhruvp/956b57d4f6e0
* https://theneuralperspective.com/2016/11/25/reinforcement-learning-rl-policy-gradients-i/
  * https://theneuralperspective.com/2016/11/26/1656/
  * https://github.com/GokuMohandas/the-neural-perspective/tree/master/reinforcement-learning
* https://cgnicholls.github.io/reinforcement-learning/2016/08/20/reinforcement-learning.html
  * https://cgnicholls.github.io/reinforcement-learning/2016/08/21/reinforcement-learning-2.html
  * https://github.com/cgnicholls/reinforcement-learning/blob/master/cartpole/crossentropy.py
  * https://github.com/cgnicholls/reinforcement-learning/blob/master/cartpole/vanillapolicygradient.py
* https://github.com/dennybritz/reinforcement-learning/tree/master/PolicyGradient
* https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/7_Policy_gradient_softmax
* https://www.oreilly.com/ideas/reinforcement-learning-with-tensorflow
