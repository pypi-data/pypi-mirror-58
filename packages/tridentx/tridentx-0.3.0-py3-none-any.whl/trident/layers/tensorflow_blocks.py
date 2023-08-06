from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from functools import reduce
from functools import wraps
import math
import collections
import itertools
import tensorflow as tf
from torch._six import container_abcs
import tensorflow.keras.backend as K
from tensorflow_core.python.keras.utils import conv_utils
from tensorflow.python.framework import tensor_shape
from tensorflow.python.keras.engine.input_spec import InputSpec
from tensorflow.python.ops import nn_ops
from tensorflow.python.client import device_lib
from .tensorflow_activations import get_activation
from .tensorflow_normalizations import get_normalization
from .tensorflow_layers import *
from itertools import repeat
import inspect

from collections import OrderedDict
from ..backend.common import get_session, gcd, get_divisors, isprime, next_prime, prev_prime, nearest_prime,unpack_singleton,enforce_singleton,snake2camel




_tf_data_format= 'channels_last'

__all__ = ['Conv2d_Block', 'TransConv2d_Block']


_session = get_session()

def compose(*funcs):
    """Compose arbitrarily many functions, evaluated left to right.
    Reference: https://mathieularose.com/function-composition-in-python/
    """
    # return lambda x: reduce(lambda v, f: f(v), funcs, x)
    if funcs:
        return reduce(lambda f, g: lambda *a, **kw: g(f(*a, **kw)), funcs)
    else:
        raise ValueError('Composition of empty sequence not supported.')

def Conv2d_Block( kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,activation='relu6',normalization='instance',  use_bias=False,dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0):
    flow_list = []
    if add_noise:
        noise = tf.keras.layers.GaussianNoise(noise_intensity)
        flow_list.append(noise)
    conv = Conv2d(kernel_size=kernel_size, num_filters=num_filters, strides=strides, auto_pad=auto_pad, activation=None,
                  use_bias=use_bias, dilation=dilation, groups=groups)
    flow_list.append(conv)

    norm = get_normalization(normalization)
    if norm:
        flow_list.append(norm)

    activation = get_activation(snake2camel(activation))
    if activation:
        flow_list.append(activation)
    if dropout_rate > 0:
        drop = Dropout(dropout_rate)
        flow_list.append(drop)

    return flow_list





def TransConv2d_Block( kernel_size=(3,3), num_filters=32, strides=1, auto_pad=True,activation='relu6',normalization='instance',  use_bias=False,dilation=1, groups=1,add_noise=False,noise_intensity=0.005,dropout_rate=0):
    flow_list = []
    if add_noise:
        noise = tf.keras.layers.GaussianNoise(noise_intensity)
        flow_list.append(noise)
    conv = TransConv2d(kernel_size=kernel_size, num_filters=num_filters, strides=strides, auto_pad=auto_pad, activation=None,
                  use_bias=use_bias, dilation=dilation, groups=groups)
    flow_list.append(conv)

    norm = get_normalization(normalization)
    if norm:
        flow_list.append(norm)

    activation = get_activation(snake2camel(activation))
    if activation:
        flow_list.append(activation)
    if dropout_rate > 0:
        drop = Dropout(dropout_rate)
        flow_list.append(drop)

    return flow_list

