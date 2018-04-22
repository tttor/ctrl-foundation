import numpy as np
import tensorflow as tf

class ActorNeuralNetwork():## aka Policy Network
    def __init__(self, input_dim, output_dim):
        hidden_dim = 200 # := n_hidden_units
        eta = 1e-3
        decay = 0.99

        # Placeholders for passing:
        # input state, self.tf_x;
        # predicted action, self.tf.y;
        # corresponding reward, self.tf_r;
        self.tf_x = tf.placeholder(dtype=tf.float32, shape=[None, input_dim], name="tf_x")
        self.tf_y = tf.placeholder(dtype=tf.float32, shape=[None, output_dim], name="tf_y")
        self.tf_returns = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="tf_returns")

        # Weights; initialized using Xavier initialization
        xavier_l1 = tf.truncated_normal_initializer(mean=0, stddev=1. / np.sqrt(input_dim), dtype=tf.float32)
        self.W1 = tf.get_variable("W1", [input_dim, hidden_dim], initializer=xavier_l1)

        xavier_l2 = tf.truncated_normal_initializer(mean=0, stddev=1. / np.sqrt(hidden_dim), dtype=tf.float32)
        self.W2 = tf.get_variable("W2", [hidden_dim, output_dim], initializer=xavier_l2)

        # Define Optimizer, compute and apply gradients
        self.tf_aprob = self._policy_forward(self.tf_x)
        loss = tf.nn.l2_loss(self.tf_y - self.tf_aprob)

        optimizer = tf.train.RMSPropOptimizer(eta, decay=decay)
        tf_grads = optimizer.compute_gradients(loss, var_list=tf.trainable_variables(), grad_loss=self.tf_returns)
        self.train_op = optimizer.apply_gradients(tf_grads)

        # Initialize Variable
        init = tf.global_variables_initializer()

        # initiates an interactive TensorFlow session
        self.session = tf.InteractiveSession()
        self.session.run(init)

    def update(self, data):
        # feed = {tf_x: np.vstack(xs), tf_epr: np.vstack(rs), tf_y: np.vstack(ys)}
        # self._actor_net.update(feed)
        pass

    def _policy_forward(self, x): #x ~ [1,D]
        # a two-layer NN: to provide the probability of moving the paddle UP, given an input observation state
        # The network takes the processed image of the state of the game and
        # generates a single number denoting the probability of moving the paddle UP.
        h = tf.matmul(x, self.W1)
        h = tf.nn.relu(h)

        logp = tf.matmul(h, self.W2)
        p = tf.nn.softmax(logp)

        return p
