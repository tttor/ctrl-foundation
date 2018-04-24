import os

import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'  ## To deactivate SSE Warnings

class ActorNeuralNetwork():## aka Policy Network
    def __init__(self, input_dim, output_dim):
        # built net
        self._build_net(input_dim, output_dim)

        # initiates an interactive TensorFlow session and initialize Variable
        self._session = tf.InteractiveSession()
        self._session.run( tf.global_variables_initializer() )

    def update(self, data):
        feed = {self._x: data['obss'], self._y: data['labels'],
                self._returns: data['returns']}

        return self._session.run(self._train_op, feed)

    def forward_prop(self, x):
        # to compute the probability:
        # because In TensorFlow, the network graph is computed only in the TensorFlow session,
        feed = {self._x: np.reshape(x, (1, -1))}
        probs = self._session.run(self._forward_prop_op, feed)

        probs = probs[0] # from [[...]] to [...]
        return probs

    def _forward_prop(self, x):
        h = tf.matmul(x, self.W1)
        h = tf.nn.relu(h)

        logp = tf.matmul(h, self.W2)
        p = tf.nn.softmax(logp)

        return p

    def _build_net(self, input_dim, output_dim):
        # TODO
        # # Placeholders for passing:
        # # input state, self._x;
        # # predicted action, self.tf.y;
        # # corresponding reward, self.tf_r;
        # self._x = tf.placeholder(dtype=tf.float32, shape=[None, input_dim], name="x")
        # self._y = tf.placeholder(dtype=tf.float32, shape=[None, output_dim], name="y")
        # self._returns = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="returns")

        # with tf.variable_scope('ActorNeuralNetwork'):
        #     hidden_layer = tf.layers.dense( inputs=self._x,
        #                                     units=200,
        #                                     activation=tf.nn.relu,
        #                                     kernel_initializer=tf.random_normal_initializer(0., .1),
        #                                     bias_initializer=tf.constant_initializer(0.1),
        #                                     name='hidden_layer' )
        #     self._output_layer = tf.layers.dense( inputs=hidden_layer,
        #                                           units=output_dim,
        #                                           activation=tf.nn.softmax, # get action probabilities
        #                                           kernel_initializer=tf.random_normal_initializer(0., .1),
        #                                           bias_initializer=tf.constant_initializer(0.1),
        #                                           name='output_layer' )


        # ## forward prop operator
        # self._forward_prop_op = self._forward_prop(self._x)

        # ## loss
        # loss = tf.nn.l2_loss(self._y - self._forward_prop_op)

        # # Define Optimizer, compute and apply gradients
        # optimizer = tf.train.RMSPropOptimizer(learning_rate=1e-3, decay=0.99)

        # tf_grads = optimizer.compute_gradients(loss, var_list=tf.trainable_variables(), grad_loss=self._returns)
        # self._train_op = optimizer.apply_gradients(tf_grads)
