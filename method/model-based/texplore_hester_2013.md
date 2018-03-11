# TEXPLORE: real-time sample-efficient reinforcement learning for robots
https://link.springer.com/article/10.1007/s10994-012-5322-7

## problems
* robots must learn in very few samples, while continually taking actions in real-time.
* the algorithm must learn efficiently in the face of noise, sensor/actuator delays, and continuous state features.
* algorithm must take actions continually in real-time (while learning), in time-constrained domains

## ideas
* TEXPLORE is a model-based RL method that learns a random forest model of the domain which generalizes dynamics to unseen states.
* parallelize model learning, planning, and acting onto 3 parallel threads
* utilize an anytime sample-based planning algorithm
