from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import numpy as np
from collections import OrderedDict

from itertools import islice
import tensorflow as tf

from tensorflow.python.framework import ops
from tensorflow.python.eager import context

from ..layers.tensorflow_layers import *
from ..layers.tensorflow_normalizations import *
from ..layers.tensorflow_activations import *
from ..layers.tensorflow_normalizations import *
from ..data.tensorflow_datasets import *
from ..backend.common import floatx,addindent, get_time_suffix, format_time, get_terminal_size, snake2camel, PrintException,to_list,unpack_singleton,enforce_singleton

__all__ = ['register_keras_custom_object','to_numpy','to_tensor','get_flops','Input','Sequential']


version=tf.version
sys.stderr.write('Tensorflow version:{0}.\n'.format(version.VERSION))

if version.VERSION<'2.0.0':
    raise ValueError('Not support Tensorflow below 2.0' )


physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
    tf.config.experimental.set_memory_growth(gpus[0], True)

    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)




def register_keras_custom_object(cls):
    tf.keras.utils.get_custom_objects()[cls.__name__] = cls
    return cls

def to_numpy(x) -> np.ndarray:

    """
    Convert whatever to numpy array
    :param x: List, tuple, PyTorch tensor or numpy array
    :return: Numpy array
    """
    if isinstance(x, np.ndarray):
        return x
    # elif isinstance(x,EagerTensor):
    #     return x.numpy()
    elif hasattr(x, 'numpy'):
        with context.eager_mode():
            return x.numpy()
    elif isinstance(x, (tf.Tensor,tf.Variable)):
        return tf.keras.backend.get_value(x)
    # elif isinstance(x, tf.Variable):
    #     sess = tf.compat.v1.Session()
    #     x = sess.run(x.value())
    #     return x
    # elif isinstance(x, ops.Tensor):
    #     sess = tf.compat.v1.Session()
    #     x= sess.run(x)
    #     return x

    elif isinstance(x, (list, tuple, int, float)):
        return np.array(x)
    else:
        try:
            x = tf.keras.backend.get_value(x)
            if isinstance(x, np.ndarray):
                return x
        except:
            raise ValueError("Unsupported type")


def to_tensor(x, dtype=None) ->ops.Tensor:
    return ops.convert_to_tensor(x, dtype=dtype)



def get_flops(model):
    run_meta = tf.compat.v1.RunMetadata()
    opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()

    # We use the Keras session graph in the call to the profiler.
    flops = tf.compat.v1.profiler.profile(graph=tf.compat.v1.keras.backend.get_session().graph,
                                run_meta=run_meta, cmd='op', options=opts)

    return flops.total_float_ops  # Prints the "flops" of the model.




def Sequential( *layers,name=''):
    if len(layers)>1:
        layer_list=[]
        for layer in layers:
            if isinstance(layer,tf.keras.Sequential):
                layer_list.extend(layer.layers)
            elif isinstance(layer,(tuple,list)):
                layer_list.extend(list(layer))
            else:
                layer_list.append(layer)
        layers=layer_list
    elif len(layers)==1 and isinstance(layers[0],tf.keras.layers.Layer):
        layers =[layers[0]]
    elif len(layers) == 1 and isinstance(layers[0], list):
        layers = layers[0]
    return tf.keras.Sequential(layers=layers,name=name)



def Input( input_shape: (list, tuple,int) = None,batch_size=None,name=''):
        if isinstance(input_shape,int):
            input_shape=input_shape,
        elif isinstance(input_shape,list):
            input_shape=tuple(input_shape)
        return tf.keras.Input(shape=input_shape,batch_size=batch_size,name=name,dtype=tf.float32)


class ConcatContainer(tf.keras.layers.Layer):
    r"""A sequential container.
    Modules will be added to it in the order they are passed in the constructor.
    Alternatively, an ordered dict of modules can also be passed in.

    To make it easier to understand, here is a small example::

        # Example of using Sequential
        model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )

        # Example of using Sequential with OrderedDict
        model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))
    """

    def __init__(self, *args):
        super(ConcatContainer, self).__init__()
        self._modules=OrderedDict()
        self._built = False
        self.axis = 1
        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for key, module in args[0].items():
                self._modules[len(self._modules)]=module
        else:
            for idx, module in enumerate(args):
                self._modules[idx] = module
        self.to(self.device)



    def _get_item_by_idx(self, iterator, idx):
        """Get the idx-th item of the iterator"""
        size = len(self)
        idx = idx.__index__()
        if not -size <= idx < size:
            raise IndexError('index {} is out of range'.format(idx))
        idx %= size
        return next(islice(iterator, idx, None))

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.__class__(OrderedDict(list(self._modules.items())[idx]))
        else:
            return self._get_item_by_idx(self._modules.values(), idx)

    def __setitem__(self, idx, module):
        key = self._get_item_by_idx(self._modules.keys(), idx)
        return setattr(self, key, module)

    def __delitem__(self, idx):
        if isinstance(idx, slice):
            for key in list(self._modules.keys())[idx]:
                delattr(self, key)
        else:
            key = self._get_item_by_idx(self._modules.keys(), idx)
            delattr(self, key)

    def __len__(self):
        return len(self._modules)

    def __dir__(self):
        keys = super(ConcatContainer, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def call(self, x, **kwargs):
        results=[]
        for module in self._modules.values():
            x1 = module(x)
            results.append(x1)
        return tf.keras.concatenate(results,dim=-1)

class ShortcutContainer(tf.keras.layers.Layer):
    r"""A sequential container.
    Modules will be added to it in the order they are passed in the constructor.
    Alternatively, an ordered dict of modules can also be passed in.

    To make it easier to understand, here is a small example::

        # Example of using Sequential
        model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )

        # Example of using Sequential with OrderedDict
        model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))
    """

    def __init__(self, *args):
        super(ShortcutContainer, self).__init__()
        self._built = False
        self.axis = 1

        if len(args) == 1 and isinstance(args[0], OrderedDict):
            for key, module in args[0].items():
                self.add_module(key, module)
        else:
            for idx, module in enumerate(args):
                self.add_module(str(idx), module)
        self.to(self.device)



    def _get_item_by_idx(self, iterator, idx):
        """Get the idx-th item of the iterator"""
        size = len(self)
        idx = idx.__index__()
        if not -size <= idx < size:
            raise IndexError('index {} is out of range'.format(idx))
        idx %= size
        return next(islice(iterator, idx, None))

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return self.__class__(OrderedDict(list(self._modules.items())[idx]))
        else:
            return self._get_item_by_idx(self._modules.values(), idx)

    def __setitem__(self, idx, module):
        key = self._get_item_by_idx(self._modules.keys(), idx)
        return setattr(self, key, module)

    def __delitem__(self, idx):
        if isinstance(idx, slice):
            for key in list(self._modules.keys())[idx]:
                delattr(self, key)
        else:
            key = self._get_item_by_idx(self._modules.keys(), idx)
            delattr(self, key)

    def __len__(self):
        return len(self._modules)

    def __dir__(self):
        keys = super(ShortcutContainer, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def forward(self, x):
        results=0
        for module in self._modules.values():
            x1 = module(x)
            results=results+x1
        return results














