# A Deeper Look at Planning as Learning from Replay
* Harm van Seijen et al
* icml2015

## observation
* The distinction between model-free and model-based (and similarly, learning and planning) is not always clear.
* While such methods do not store an explicit transition model, 
  they share many characteristics with model-based methods, 
  such as increased computational requirements and improved sample efficiency, which 
  has led some people to argue that **a stored set of samples** should also be considered a model.

## idea: forgetful LSTD(λ)
* show an exact equivalence between the sequence of value functions found by 
  a model-based policy-evaluation method and by a model-free method with replay. 
* present a general replay method that can mimic a spectrum of methods ranging from 
  the explicitly model- free (TD(0)) to the explicitly model-based (linear Dyna)

## result
* there is a close relation between **replaying experience** and **exploiting a model**
  * there are instances where replaying the past results in the same learning function as planning with a learned model. 

## background
* the notions of experi- ence replay, and of planning as learning from replayed experience, 
  have long been used to find good policies with minimal training data. 
* Replay can be seen either 
  * as model-based reinforcement learning, where the store of past experiences serves as the model, or 
  * as a way to avoid a conventional model of the environment altogether
  
