from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
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
from itertools import repeat
import inspect

from collections import OrderedDict
from ..backend.common import get_session, gcd, get_divisors, isprime, next_prime, prev_prime, nearest_prime,unpack_singleton,enforce_singleton

_tf_data_format= 'channels_last'

__all__ = ['Dense', 'Flatten', 'Concatenate','Concate','Add','Subtract', 'Conv1d', 'Conv2d', 'Conv3d',  'TransConv2d', 'TransConv3d','Reshape','Dropout','Lambda']


_session = get_session()

_device='CPU'
for device in device_lib.list_local_devices():
      if tf.DeviceSpec.from_string(device.name).device_type == 'GPU':
          _device='GPU'
          break

_epsilon = _session.epsilon


def _ntuple(n):
    def parse(x):
        if isinstance(x, container_abcs.Iterable):
            return x
        return tuple(repeat(x, n))

    return parse


_single = _ntuple(1)
_pair = _ntuple(2)
_triple = _ntuple(3)
_quadruple = _ntuple(4)





class Dense(tf.keras.layers.Dense):
    def __init__(self, output_shape, use_bias=True, activation=None, ):
        super(Dense, self).__init__(units=output_shape,use_bias=use_bias,activation=get_activation(activation))



class Flatten(tf.keras.layers.Flatten):
    def __init__(self ):
        super(Flatten, self).__init__()


class Concate(tf.keras.layers.Concatenate):
    def __init__(self, axis=-1 ):
        super(Concate, self).__init__(axis=axis)

Concatenate=Concate


class Add(tf.keras.layers.Add):
    def __init__(self ):
        super(Add, self).__init__()


class Subtract(tf.keras.layers.Subtract):
    def __init__(self ):
        super(Subtract, self).__init__()



def _conv_extra_repr(self):
    s = 'kernel_size={kernel_size}, {filters},strides={strides}'
    if 'activation' in self.__dict__ and self.__dict__['activation'] is not None:
        if inspect.isfunction(self.__dict__['activation']):
            s += ', activation={0}'.format(self.__dict__['activation'].__name__)
        elif isinstance(self.__dict__['activation'],tf.keras.layers.Layer ):
            s += ', activation={0}'.format(self.__dict__['activation']).__repr__()
    s += ',auto_pad={0}'.format(self.padding=='same')+',use_bias={use_bias} ,dilation={dilation}'
    if self.groups != 1:
        s += ', groups={groups}'
    if self.input_shape is not None:
        s += ', input_shape={0}, input_filter={1}'.format(self.input_shape,self.input_shape[0])
    if self.output_shape is not None:
        s += ', output_shape={0}'.format(self.output_shape)
    #     if self.bias is None:
    #         s += ', use_bias=False'
    return s.format(**self.__dict__)



class Conv1d(tf.keras.layers.Conv1D):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _single(kernel_size)
        strides = _single(strides)
        dilation = _single(dilation)
        activation = get_activation(activation)
        super(Conv1d, self).__init__(self,filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',**kwargs)


Conv1d.extra_repr=_conv_extra_repr

def  Conv2d(kernel_size, num_filters, strides=1, auto_pad=True, activation=None, use_bias=False, dilation=1, groups=1, **kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        return tf.keras.layers.Conv2D(filters=num_filters, kernel_size=kernel_size, strides=strides,  padding='same'if auto_pad else 'valid', dilation_rate=dilation, activation=activation, use_bias=use_bias,data_format='channels_last',**kwargs)

Conv2d.extra_repr=_conv_extra_repr


class Conv3d(tf.keras.layers.Conv2D):
    def __init__(self, kernel_size, num_filters, strides=1, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        activation = get_activation(activation)
        super(Conv3d, self).__init__(self, filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last', **kwargs)

Conv2d.extra_repr = _conv_extra_repr


class TransConv2d(tf.keras.layers.Conv2DTranspose):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(TransConv2d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last', **kwargs)

TransConv2d.extra_repr = _conv_extra_repr

class TransConv3d(tf.keras.layers.Conv3DTranspose):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)
        activation = get_activation(activation)
        super(TransConv3d, self).__init__( filters=num_filters, kernel_size=kernel_size, strides=strides,
                                     padding='same' if auto_pad else 'valid', dilation_rate=dilation,
                                     activation=activation, use_bias=use_bias,data_format='channels_last', **kwargs)
TransConv3d.extra_repr = _conv_extra_repr


class Lambda(tf.keras.layers.Lambda):
    """
    Applies a lambda function on forward()
    Args:
        lamb (fn): the lambda function
    """

    def __init__(self, function):
        super(Lambda, self).__init__(function=function, output_shape=None, arguments={})
        self.function = function



Reshape=tf.keras.layers.Reshape




class Dropout(tf.keras.layers.Dropout):
    def __init__(self, dropout_rate=0 ):
        super(Dropout, self).__init__(dropout_rate)
