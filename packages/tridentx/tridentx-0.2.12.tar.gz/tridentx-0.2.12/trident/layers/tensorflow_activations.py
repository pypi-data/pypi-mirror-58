from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
from ..backend.common import *

import numpy as np
import six
import tensorflow as tf
from tensorflow.keras import backend as K


__all__ = ['Identity','Sigmoid','Tanh','Relu','Relu6','LeakyRelu','LeakyRelu6','SmoothRelu','PRelu','Swish','Elu','HardSigmoid','HardSwish','Selu','LecunTanh','SoftSign','SoftPlus','HardTanh','Logit','LogLog','Mish','Softmax','identity','sigmoid','tanh','relu','relu6','leaky_relu','leaky_relu6','smooth_relu','p_relu','swish','elu','hard_sigmoid','hard_swish','selu','lecun_tanh','soft_sign','soft_plus','hard_tanh','logit','log_log','mish','softmax','get_activation']


def identity(x,name=None):
    with tf.name_scope(name)as scope:
        return x

Identity=tf.keras.layers.Lambda(identity)

def sigmoid(x,name=None):
    return tf.nn.sigmoid(x,name)

Sigmoid=tf.keras.layers.Lambda(sigmoid)

def tanh(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.tanh(x)

Tanh=tf.keras.layers.Lambda(tanh)
def relu(x,upper_limit=None,name=None):
    if upper_limit<=0:
        raise ValueError('Upper limit should greater than 0!')
    with tf.name_scope(name)as scope:
        if upper_limit is not None:
            return K.clip(tf.nn.relu(x),0,upper_limit)
        return tf.nn.relu(x)

def relu6(x,name=None):
    with tf.name_scope(name)as scope:
        return K.clip(tf.nn.relu(x),0,6)


Relu=tf.keras.layers.ReLU
Relu6=tf.keras.layers.Lambda(relu6)

def leaky_relu(x,alpha=0.01,upper_limit=None,name=None):
    with tf.name_scope(name)as scope:
        if upper_limit is not None:
            return K.clip(tf.nn.relu(x,alpha), -np.inf, upper_limit)
        return tf.nn.relu(x,alpha)

def leaky_relu6(x,alpha=0.01,name=None):
    with tf.name_scope(name)as scope:
        return K.clip(tf.nn.relu(x,alpha), -6, 6)

LeakyRelu=tf.keras.layers.LeakyReLU
LeakyRelu6=tf.keras.layers.Lambda(leaky_relu6)

def elu(x,alpha=0.01,upper_limit=None,name=None):
    with tf.name_scope(name)as scope:
        if upper_limit is not None:
            return K.clip(tf.nn.elu(x,alpha),-np.inf,upper_limit)
        return tf.nn.elu(x,alpha)

Elu=tf.keras.layers.ELU
lrelu=leaky_relu


def smooth_relu(x,upper_limit=None,name=None):
    with tf.name_scope(name)as scope:
        if upper_limit is not None:
            return K.clip(tf.math.log(1 + tf.math.exp(x)),-np.inf,upper_limit)
        return tf.math.log(1 + tf.math.exp(x))
SmoothRelu=tf.keras.layers.Lambda(smooth_relu)

def p_relu(x,upper_limit=None,name=None):
    with tf.name_scope(name)as scope:
        if upper_limit is not None:
            return K.clip(tf.keras.layers.PReLU()(x),-np.inf,upper_limit)
        return tf.keras.layers.PReLU()(x)
PRelu=tf.keras.layers.PReLU

def swish(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.sigmoid(x) * x

Swish=tf.keras.layers.Lambda(swish)


def selu(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.selu(x)

Selu=tf.keras.layers.Lambda(selu)



def lecun_tanh(x,name=None):
    with tf.name_scope(name)as scope:
        return 1.7159 * tf.nn.tanh(2/3 * x)

LecunTanh=tf.keras.layers.Lambda(lecun_tanh)

def soft_sign(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.softsign(x)
SoftSign=tf.keras.layers.Lambda(soft_sign)

def soft_plus(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.softplus(x)
SoftPlus=tf.keras.layers.Lambda(soft_plus)

def hard_sigmoid(x,name=None):
    with tf.name_scope(name)as scope:
        return relu6(x+3)/6
HardSigmoid=tf.keras.layers.Lambda(hard_sigmoid)


def hard_tanh(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.keras.backend.clip(x,-1,1)
HardTanh=tf.keras.layers.Lambda(hard_tanh)


def hard_swish(x,name=None):
    with tf.name_scope(name)as scope:
        return  x * hard_sigmoid(x)
HardSwish=tf.keras.layers.Lambda(hard_swish)


def logit(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.math.log.log(x / (1 - x))

Logit=tf.keras.layers.Lambda(logit)

def log_log(x,name=None):
    with tf.name_scope(name)as scope:
        return  1-tf.math.exp(-tf.math.exp(x))

LogLog=tf.keras.layers.Lambda(log_log)


def softmax(x,name=None):
    with tf.name_scope(name)as scope:
        return tf.nn.softmax(x)

Softmax=tf.keras.layers.Softmax

def mish(x,name=None):
    with tf.name_scope(name)as scope:
        return x*tf.nn.tanh(tf.nn.softplus(x))

Mish=tf.keras.layers.Lambda(mish)



def get_activation(fn_name):
    if fn_name is None:
        return None
    fn_modules = ['trident.layers.tensorflow_activations','tensorflow.nn']
    activation_fn = get_function(camel2snake(fn_name), fn_modules)
    return activation_fn





