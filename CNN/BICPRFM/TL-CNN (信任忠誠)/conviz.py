
# coding: utf-8

# In[1]:


from __future__ import print_function

import tensorflow as tf
import numpy as np
np.set_printoptions(threshold=np.inf)



# Parameters
learning_rate = 0.05
training_iters = 10
batch_size = 128
display_step = 10

# Network Parameters
n_input = 28  # MNIST data input (img shape: 28*28)
n_classes = 2  # MNIST total classes (0-9 digits)
dropout = 0.75  # Dropout, probability to keep units

# tf Graph input
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)  # dropout (keep probability)


def conv2d(x_, filter_sizex,  filter_sizey, filter_num, stride=1):
    """
    Wrapper of a convolutional layer
    :param x_: tensor, input to convolutional layer
    :param filter_size: int, size of a convolutional kernel
    :param filter_num: int, number of convolutional kernels
    :param stride: int, optional, stride
    :return: tensor
    """
    # get number of channels in input
    channels = x_.get_shape()[3].value

    # create weights tensor
    weights = tf.Variable(tf.random_normal([filter_sizex, filter_sizey, channels, filter_num]))

    # add weights tensor to collection
    tf.add_to_collection('conv_weights', weights)

    # create bias tensor
    bias = tf.Variable(tf.random_normal([filter_num]))

    # apply weights and biases
    preactivations = tf.nn.conv2d(x_, weights, strides=[1, stride, stride, 1], padding='SAME')
    preactivations = tf.nn.bias_add(preactivations, bias)

    # apply activation function, this is layer output
    activations = tf.nn.relu(preactivations)

    # add output to collection
    tf.add_to_collection('conv_output', activations)

    return activations


def fc(x_, nodes, keep_prob_=1, act=tf.nn.relu):
    """
    Wrapper for fully-connected layer
    :param x_: tensor, input to fully-connected alyer
    :param nodes: int, number of nodes in layer
    :param keep_prob_: float, optional, keep probability for dropout operation
    :param act: tf.nn method, optional, activation function
    :return: tensor
    """
    #print(7)
    shape = x_.get_shape()

    # if rank of input tensor is greater than 2
    # we need to reshape it
    if shape.ndims > 1:
        n = 1
        for s in shape[1:]:
            n *= s.value
        x_ = tf.reshape(x_, tf.stack([-1, n]))
        x_.set_shape([None, n])

    # get number of column in input tensor
    n = x_.get_shape()[1].value
    print("n=",n)

    # create weights
    weights = tf.Variable(tf.random_normal([n, nodes]))

    # create biases
    bias = tf.Variable(tf.random_normal([nodes]))

    # apply weights and bias
    preactivate = tf.add(tf.matmul(x_, weights), bias)
    out = preactivate

    # apply activation function if not None
    if act is not None:
        out = act(preactivate)

    # apply dropout
    out = tf.nn.dropout(out, keep_prob_)

    return out


def maxpool(x_, sizex, sizey, stridex, stridey):
    """
    Wrapper for max-pooling layer
    :param x_: tensor, input to max-pooling layer
    :param size: int
    :param stride: int
    :return: tensor
    """
    return tf.nn.max_pool(x_,
                          ksize=[1, sizey, sizex, 1],
                          strides=[1, stridey, stridex, 1],
                          padding='SAME')


# Reshape inputs
x_reshaped = tf.reshape(x, shape=[-1, 7, 4, 1])
#x_reshaped = tf.reshape(x, shape=[-1, 2, 4, 1])
# First convolutional layer
predictions = conv2d(x_reshaped, filter_sizex=4, filter_sizey=7, filter_num=7)

# First max-pooling layer
predictions = maxpool(predictions, 2, 1, 2, 1)

# Second convolutional layer
predictions = conv2d(predictions, filter_sizex=2, filter_sizey=7, filter_num=14)

# Second max-pooling layer
predictions = maxpool(predictions, 2, 1, 2, 1)

# Fully-connected layer
predictions = fc(predictions, 4, keep_prob)

# Output layer, no activation function
# This layer returns logits
predictions = fc(predictions, n_classes, keep_prob, act=None)

# Define loss operation
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions,  labels=y))

# Define optimizer
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

# Define accuracy operation
correct_predictions = tf.equal(tf.argmax(predictions, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
tf_metric, tf_metric_update=tf.metrics.precision(y,predictions,name="my_metric")
running_vars = tf.get_collection(tf.GraphKeys.LOCAL_VARIABLES, scope="my_metric")
running_vars_initializer = tf.variables_initializer(var_list=running_vars)

# Initializing the variables
init = tf.initialize_all_variables()
running_vars_initializer = tf.variables_initializer(var_list=running_vars)

#############################################################
#sess = tf.Session()
#sess.run(tf.global_variables_initializer())
from MKPicSet import PicSet as PS

MP = PS()
MP.Addtest('./TraingData10/')
#MP.show()
NumberOfOneTraing = 2024 #每單次訓練的使用的圖象數量

from test import PicSet as TPS

TMP = TPS()
#print(1)
TMP.Addtest('./TraingData10/')
#print(2)
#MP.show()
TNumberOfOneTraing = 2163
###########################################################
#print(3)
with tf.Session() as sess:
    sess.run(init)
    sess.run(running_vars_initializer)
#    step = 1
    # Keep training until reach max iterations
    for i in range(1): #訓練次數
        
        batch_x, batch_y = MP.batch(NumberOfOneTraing)
        #print(batch_x,batch_y)
        # Run optimization op (backprop)
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,keep_prob: dropout})
        sess.run(tf_metric_update, feed_dict={x: batch_x, y: batch_y,keep_prob: dropout})
        precision = sess.run(tf_metric)
        print("train Accuracy:",sess.run(accuracy, feed_dict={x: batch_x,y: batch_y, keep_prob: 1.}))
        print(len(batch_x))
        
        MP.reset()
    print("\rOptimization Finished!")

    # Calculate accuracy for 256 mnist test images
    test_xs, test_ys = TMP.batch(TNumberOfOneTraing)
    print("Testing Accuracy:",sess.run(accuracy, feed_dict={
                                        x: test_xs,
                                        y: test_ys,
                                        keep_prob: 1.}))
    print(sess.run(correct_predictions, feed_dict={x: test_xs,y: test_ys,keep_prob: 1.}))
