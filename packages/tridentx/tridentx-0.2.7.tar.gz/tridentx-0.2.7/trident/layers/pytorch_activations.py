from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from pydoc import locate
import six
from functools import partial
import math

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.modules.activation as af
from torch.nn.parameter import Parameter
from ..backend.common import get_function,camel2snake
from ..backend.pytorch_backend import Modulex
__all__ = ['Identity','Sigmoid','Tanh','Relu','Relu6','LeakyRelu','LeakyRelu6','SmoothRelu','PRelu','Swish','Elu','HardSigmoid','HardSwish','Selu','LecunTanh','SoftSign','SoftPlus','HardTanh','Logit','LogLog','Mish','Softmax','BertGELU','GPTGELU','identity','sigmoid','tanh','relu','relu6','leaky_relu','leaky_relu6','smooth_relu','p_relu','swish','elu','hard_sigmoid','hard_swish','selu','lecun_tanh','soft_sign','soft_plus','hard_tanh','logit','log_log','mish','softmax','bert_gelu','gpt_gelu','get_activation']

'''
'''
class Identity(Modulex):
    def __init__(self, ):
        super(Identity, self).__init__()
        self._is_built = True
    def forward(self, x):
        return x

'''identity activation function 
'''
def identity(x):
    return x

class Relu(Modulex):
    def __init__(self, ):
        super(Relu, self).__init__()
    def forward(self, x):
        return relu(x)

'''relu activation function 
'''
def relu(x):
    return torch.relu(x)


class Relu6(Modulex):
    def __init__(self, ):
        super(Relu6, self).__init__()
    def forward(self, x):
        return relu6(x)
'''relu6 activation function 
'''
def relu6(x):
    return F.relu6(x)

class LeakyRelu(Modulex):
    def __init__(self, ):
        super(LeakyRelu, self).__init__()
    def forward(self, x):
        return leaky_relu(x)

'''leaky_relu activation function 
'''
def leaky_relu(x):
    return F.leaky_relu(x)


class LeakyRelu6(Modulex):
    def __init__(self):
        super(LeakyRelu6, self).__init__()
        self._is_built = True
    def forward(self, x):
        return leaky_relu6(x)

'''leaky_relu6 activation function 
'''
def leaky_relu6(x):
    return torch.clamp(F.leaky_relu(x),-6,6)


class SmoothRelu(Modulex):
    def __init__(self):
        super(SmoothRelu, self).__init__()
        self._is_built = True
    def forward(self, x):
        return smooth_relu(x)


'''smooth_relu activation function 
'''
def smooth_relu(x):
    return  torch.log(1 + torch.exp(x))



'''PRelu activation function Layer
'''
class PRelu(Modulex):
    def __init__(self,num_parameters=1,init=0.25):
        super(PRelu, self).__init__()
        self.num_parameters = num_parameters
        self.weight = Parameter(torch.Tensor(num_parameters).fill_(init))
        self._is_built = True
    def forward(self, x):
        return p_relu(x)

'''p_relu activation function 
'''
p_relu=torch.prelu

'''Softmax activation function layer
'''
class Sigmoid(Modulex):
    """Softmax activation function.
       # Arguments
           x: Input tensor.
           axis: Integer, axis along which the softmax normalization is applied.

       # Returns
           Tensor, output of softmax transformation.

       # Raises
           ValueError: In case `dim(x) == 1`.
       """
    def __init__(self):
        super(Sigmoid, self).__init__()
        self._is_built = True
    def forward(self, x):
        return sigmoid(x)

'''softmax activation function 
'''

def sigmoid(x):
    return  torch.sigmoid(x)

class Tanh(Modulex):
    def __init__(self):
        super(Tanh, self).__init__()
        self._is_built = True
    def forward(self, x):
        return tanh(x)

'''tanh activation function 
'''
def tanh(x):
    return  torch.tanh(x)


class Swish(Modulex):
    def __init__(self):
        super(Swish, self).__init__()
        self._is_built = True
    def forward(self, x):
        return swish(x)


'''swish activation function 
'''
def swish(x):
    return x * sigmoid(x)

class HardSigmoid(Modulex):
    def __init__(self, inplace=False):
        super(HardSigmoid, self).__init__()
        self._is_built = True
        self.inplace = inplace
    def forward(self, x):
        return hard_sigmoid(x, inplace=self.inplace)

def hard_sigmoid(x, inplace=False):
    return F.relu6(x + 3, inplace) / 6

class HardSwish(Modulex):
    def __init__(self, inplace=False):
        super(HardSwish, self).__init__()
        self._is_built = True
        self.inplace = inplace
    def forward(self, x):
        return hard_swish(x, inplace=self.inplace)

def hard_swish(x, inplace=False):
    return x * hard_sigmoid(x, inplace)


class HardTanh(Modulex):
    def __init__(self,):
        super(HardTanh, self).__init__()
        self._is_built = True
    def forward(self, x):
        return hard_tanh(x)

def hard_tanh(x):
    return  torch.clamp(x,-1,1)


class Selu(Modulex):
    def __init__(self, inplace=False):
        super(Selu, self).__init__()
        self._is_built = True
        self.inplace = inplace
    def forward(self, x):
        return selu(x)


'''selu activation function 
'''
def selu(x):
    return torch.selu(x)


class Elu(Modulex):
    def __init__(self):
        super(Elu, self).__init__()
        self._is_built = True
    def forward(self, x):
        return elu(x)


def elu(x):
    return F.elu(x)



class LecunTanh(Modulex):
    def __init__(self):
        super(LecunTanh, self).__init__()
        self._is_built = True
    def forward(self, x):
        return hard_swish(x)

def lecun_tanh(x):
    return 1.7159 * torch.tanh(2 / 3 * x)


class SoftSign(Modulex):
    def __init__(self):
        super(SoftSign, self).__init__()
        self._is_built = True
    def forward(self, x):
        return soft_sign(x)

def soft_sign(x):
    return x.exp().add(1).log()



class SoftPlus(Modulex):
    def __init__(self):
        super(SoftPlus, self).__init__()
        self._is_built = True
    def forward(self, x):
        return soft_plus(x)

def soft_plus(x):
    return F.softplus(x)



class Logit(Modulex):
    def __init__(self,):
        super(Logit, self).__init__()
    def forward(self, x):
        return logit(x)

def logit(x):
    return  (x / (1 - x)).log()


class LogLog(Modulex):
    def __init__(self,):
        super(LogLog, self).__init__()
        self._is_built = True
    def forward(self, x):
        return log_log(x)

def log_log(x):
    return   1-torch.exp(-torch.exp(x))




class Mish(Modulex):
    '''
        #Mish - "Mish: A Self Regularized Non-Monotonic Neural Activation Function"
        #https://arxiv.org/abs/1908.08681v1
    '''
    def __init__(self):
        super().__init__()
        self._is_built = True
    def forward(self, x):
        return mish(x)

'''mish activation function 
'''
def mish(x):
    return x *( torch.tanh(F.softplus(x)))


class Softmax(Modulex):
    def __init__(self):
        super(Softmax, self).__init__()
    def forward(self, x):
        return softmax(x)

def softmax(x):
    return torch.softmax(x,dim=-1)




class BertGELU(Modulex):
    r"""Bert uses GELU as the activation function for the position-wise network.
    """
    def __init__(self):
        super(BertGELU, self).__init__()
        self._is_built = True
    def forward(self, x):
        return bert_gelu(x)

def bert_gelu(x):
    return x * 0.5 * (1.0 + torch.erf(x / math.sqrt(2.0)))


class GPTGELU(Modulex):
    r"""For information: OpenAI GPT's GELU is slightly different (and gives
    slightly different results).
    """
    def forward(self, x):
        self._is_built = True
        return gpt_gelu(x)

def gpt_gelu(x):
    return 0.5 * x * (1 + torch.tanh(math.sqrt(2 /math.pi) * (x + 0.044715 * torch.pow(x, 3))))


def get_activation(fn_name):
    if fn_name is None:
        return None
    fn_modules = ['trident.layers.pytorch_activations']
    try:
        if fn_name in __all__:
            activation_fn = get_function(fn_name, fn_modules)
            return activation_fn
        else:
            activation_fn = get_function(camel2snake(fn_name), fn_modules)
            return activation_fn
    except Exception:
        return None

