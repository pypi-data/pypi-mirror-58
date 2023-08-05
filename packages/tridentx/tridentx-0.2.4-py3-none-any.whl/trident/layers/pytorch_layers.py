from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import math
from functools import partial, wraps, update_wrapper
from itertools import islice
import torch

import torch.nn as nn
import torch.utils.hooks as hooks
from torch.nn import Module
from torch.nn import init
from torch.nn.parameter import Parameter
import torch.nn.functional as F  # import torch functions
from torch._six import container_abcs
from torch._jit_internal import List
from itertools import repeat
from collections import OrderedDict
from ..backend.common import get_session, gcd, get_divisors, isprime, next_prime, prev_prime, nearest_prime
from ..backend.pytorch_backend import to_numpy, to_tensor, Modulex, Sequential
from .pytorch_activations import get_activation
from .pytorch_normalizations import *
import numpy as np

__all__ = ['Dense', 'Flatten','Concatenate' ,'Conv1d', 'Conv2d', 'Conv3d', 'TransConv1d', 'TransConv2d', 'TransConv3d',
           'SeparableConv1d', 'SeparableConv2d', 'SeparableConv3d', 'DepthwiseConv1d', 'DepthwiseConv2d',
           'DepthwiseConv3d', 'GcdConv2d', 'GcdConv2d_1',  'Lambda', 'Reshape', 'CoordConv2d',
           'UpsamplingBilinear2d','Droupout','AlphaDroupout']

_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon = _session.epsilon


def _ntuple(n):
    def parse(x):
        if x is None:
            return x
        elif isinstance(x, container_abcs.Iterable):
            if len(x) == n:
                return x
            else:
                return _ntuple(n - len(x))(1) + x
        return tuple(repeat(x, n))

    return parse


_single = _ntuple(1)
_pair = _ntuple(2)
_triple = _ntuple(3)
_quadruple = _ntuple(4)

class Dense(Modulex):
    r"""Applies a linear transformation to the incoming data: :math:`y = xA^T + b`

    Args:
        in_features: size of each input sample
        out_features: size of each output sample
        bias: If set to ``False``, the layer will not learn an additive bias.
            Default: ``True``

    Shape:
        - Input: :math:`(N, *, H_{in})` where :math:`*` means any number of
          additional dimensions and :math:`H_{in} = \text{in\_features}`
        - Output: :math:`(N, *, H_{out})` where all but the last dimension
          are the same shape as the input and :math:`H_{out} = \text{out\_features}`.

    Attributes:
        weight: the learnable weights of the module of shape
            :math:`(\text{out\_features}, \text{in\_features})`. The values are
            initialized from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})`, where
            :math:`k = \frac{1}{\text{in\_features}}`
        bias:   the learnable bias of the module of shape :math:`(\text{out\_features})`.
                If :attr:`bias` is ``True``, the values are initialized from
                :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where
                :math:`k = \frac{1}{\text{in\_features}}`

    Examples::

        >>> m = nn.Linear(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    def __init__(self, output_shape, use_bias=True,activation=None,):
        super(Dense, self).__init__()

        if isinstance(output_shape,int):
            self.output_shape=_single(output_shape)
        elif isinstance(output_shape,list):
            self.output_shape = tuple(output_shape)
        elif isinstance(output_shape, tuple):
            self.output_shape =output_shape
        else:
            raise ValueError('output_shape should be integer, list of integer or tuple of integer...')

        self.weight = None
        self.bias = None
        self.use_bias=use_bias
        self.activation = get_activation(activation)



    def build_once(self, input_shape):
        if self._is_built == False:
            self.weight =Parameter(torch.Tensor(*self.output_shape,self.input_filters ))
            if self.use_bias:
                self.bias = Parameter(torch.Tensor(*self.output_shape))
            self.reset_parameters()
            self.to(self.device)
            self._is_built = True
    def reset_parameters(self):
        init.kaiming_uniform_(self.weight)
        if self.use_bias==True and self.bias is not None:
            init.zeros_(self.bias)

    def forward(self, x):
        x=F.linear(x, self.weight, self.bias)
        if self.activation is not None:
            x = self.activation(x)
        return x

    def extra_repr(self):
        return 'input_shape={}, output_shape={}, bias={}'.format(self._input_shape[1:], self.output_shape, self.use_bias is not None
        )


class Flatten(Modulex):
    r"""Flatten layer to flatten a tensor after convolution."""
    def __init__(self):
        super(Flatten, self).__init__()
        self._is_built = True
    def forward(self,  x: torch.Tensor) -> torch.Tensor:
        return  x.view(x.size(0), -1)


class Concatenate(Modulex):
    r"""Flatten layer to flatten a tensor after convolution."""
    def __init__(self,axis=1):
        super(Concatenate, self).__init__()
        self.axis=axis
        self._is_built = False
    def forward(self,  x: torch.Tensor) -> torch.Tensor:
        if self._is_built == False:
            if not isinstance(x, list) or len(x) < 2:
                raise ValueError('A `Concatenate` layer should be called on a list of at least 2 inputs')

            if all([k.size()is None for k in x]):
                return

            reduced_inputs_shapes = [list(k.size()) for k in x]
            shape_set = set()
            for i in range(len(reduced_inputs_shapes)):
                del reduced_inputs_shapes[i][self.axis]
                shape_set.add(tuple(reduced_inputs_shapes[i]))
            if len(shape_set) > 1:
                raise ValueError('A `Concatenate` layer requires inputs with matching shapes except for the concat axis. Got inputs shapes: %s' % (shape_set))
            self._is_built =True
        x=torch.cat(x,dim=self.axis)
        return  x

class Add(Modulex):
    r"""Flatten layer to flatten a tensor after convolution."""
    def __init__(self,axis=1):
        super(Add, self).__init__()
        self.axis=axis
        self._is_built = True
    def forward(self,  x: torch.Tensor) -> torch.Tensor:
        if not isinstance(x, list):
            raise ValueError('A merge layer should be called on a list of inputs.')
        x=torch.cat(x,dim=self.axis)
        return  x


_gcd = gcd
_get_divisors = get_divisors
_isprime = isprime


class _ConvNd(Modulex):
    __constants__ = ['kernel_size', 'num_filters', 'strides', 'auto_pad', 'activation', 'padding', 'use_bias',
                     'dilation', 'groups']

    def __init__(self, kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, transposed, **kwargs):
        super(_ConvNd, self).__init__()

        self.num_filters = kwargs['out_channels'] if 'out_channels' in kwargs else num_filters
        self.kernel_size = kernel_size
        self.padding = 0  # padding if padding is not None else 0in_channel
        self.strides = kwargs['stride'] if 'stride' in kwargs else strides
        self.auto_pad = auto_pad
        self.dilation = dilation
        self.transposed = transposed
        self.groups = groups

        self.transposed = transposed
        self.padding_mode = kwargs.get('padding_mode', 'replicate')
        self.weight = None
        self.bias = None
        self.use_bias = use_bias

        # self.input_filters = kwargs.get('in_channels', None)
        #         # if self.input_filters is not None:
        #         #     self.build_once(self.input_filters)
        #
        # if self.input_filters is not None and self.input_filters % groups != 0:
        #     raise ValueError('in_channels must be divisible by groups')
        # if self.num_filters % groups != 0:
        #     raise ValueError('out_channels must be divisible by groups')

        self.to(self.device)

    def reset_parameters(self):
        init.kaiming_uniform_(self.weight, mode='fan_in')
        if self.use_bias == True and self.bias is not None:
            if isinstance(self.init_bias, int):
                self.bias.data = np.ones(list(self.bias.size())) * self.init_bias
            else:
                fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
                bound = 1 / math.sqrt(fan_in)
                self.bias.data =torch.clamp(np.ones(list(self.bias.size())), -bound, bound)


    def build_once(self, input_shape):
        if self._is_built == False:
            if self.transposed:
                self.weight = Parameter( torch.Tensor(self.input_filters, self.num_filters // self.groups, *self.kernel_size))
            else:
                self.weight = Parameter( torch.Tensor(self.num_filters, self.input_filters // self.groups, *self.kernel_size))  #

            if self.use_bias:
                self.bias = Parameter(torch.Tensor(self.num_filters))
            self.reset_parameters()
            self.to(self.device)
            self._is_built = True

    def extra_repr(self):
        s = (
            'kernel_size={kernel_size}, {num_filters}, strides={strides}, activation={activation}, auto_pad={auto_pad} , dilation={dilation}')
        #     if self.groups != 1:
        #         s += ', groups={groups}'
        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)

    def __setstate__(self, state):
        super(_ConvNd, self).__setstate__(
            state)  # if not hasattr(self, 'padding_mode'):  #     self.padding_mode = 'zeros'


class Conv1d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _single(kernel_size)
        strides = _single(strides)
        dilation = _single(dilation)
        super(Conv1d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, False,
                                     **kwargs)
        self.activation = get_activation(activation)
        if 'padding' in kwargs:
            self.padding = kwargs['padding']
            self.padding = _single(self.padding)
            self.auto_pad = False
        else:
            self.padding = _single(0)

    def conv1d_forward(self, x):
        if self.auto_pad == True:
            iw = x.size()[-1]
            kw = self.weight.size()[-1]
            sw = self.strides[-1]
            dw = self.dilation[-1]
            ow = math.ceil(iw / sw), math.ceil(iw / sw)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2], mode='replicate')
        return F.conv1d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, self.groups)

    def forward(self, x):
        x = self.conv1d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class Conv2d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides=1, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)

        super(Conv2d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, False, **kwargs)
        self.activation = get_activation(activation)

        self.padding = kwargs.get('padding', None)
        if self.padding is not None:
            if isinstance(self.padding, int):
                if self.padding > 0:
                    self.auto_pad = False
                self.padding = _pair(self.padding)
        else:
            self.padding = _pair(0)

    def conv2d_forward(self, x):
        if self.auto_pad == True:
            ih, iw = x.size()[-2:]
            kh, kw = self.kernel_size[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = self.dilation[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')
        return F.conv2d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, self.groups)

    def forward(self, x):
        x=self.conv2d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class Conv3d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        super(Conv3d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, False,
                                     **kwargs)
        self.activation = get_activation(activation)
        if 'padding' in kwargs:
            self.padding = kwargs['padding']
            self.padding = _triple(self.padding)
            self.auto_pad = False
        else:
            self.padding = _triple(0)

    def conv3d_forward(self, x):
        if self.auto_pad == True:
            iz, ih, iw = x.size()[-3:]
            kz, kh, kw = self.kernel_size[-3:]
            sz, sh, sw = self.strides[-3:]
            dz, dh, dw = self.dilation[-3:]
            oz, oh, ow = math.ceil(iz / sz), math.ceil(ih / sh), math.ceil(iw / sw)
            pad_z = max((oz - 1) * sz + (kz - 1) * dz + 1 - iz, 0)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_z > 0 or pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2, pad_z // 2,
                              pad_z - pad_z // 2], mode='replicate')
        return F.conv3d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, self.groups)

    def forward(self, x):
        x = self.conv3d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class TransConv1d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _single(kernel_size)
        strides = _single(strides)
        dilation = _single(dilation)
        super(TransConv1d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, True,
                                          **kwargs)
        self.activation = get_activation(activation)

        if 'padding' in kwargs:
            self.padding = kwargs['padding']
            self.padding = _single(self.padding)
            self.auto_pad = False
        else:
            self.padding = _single(0)
        self.output_padding = _single(0)

    def conv1d_forward(self, x):
        if self.auto_pad == True:
            iw = x.size()[-1]
            kw = self.kernel_size[-1]
            sw = self.strides[-1]
            dw = self.dilation[-1]
            ow = math.ceil(iw / sw), math.ceil(iw / sw)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_w > 0:
                self.padding = [pad_w]
                self.output_padding = _single(1)
        return F.conv_transpose1d(x, self.weight, self.bias, self.strides, padding=self.padding, dilation=self.dilation, groups=self.groups)

    def forward(self, x):
        x = self.conv1d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class TransConv2d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides=1, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _pair(kernel_size)
        strides = _pair(strides)
        dilation = _pair(dilation)

        super(TransConv2d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, True,
                                          **kwargs)
        self.activation = get_activation(activation)

        if 'padding' in kwargs:
            self.padding = kwargs['padding']
            self.padding = _pair(self.padding)
            self.auto_pad = False if self.padding[0] + self.padding[1] > 0 else True
        else:
            self.padding = _pair(0)
        self.output_padding = _pair(0)

    def conv2d_forward(self, x):
        if self.auto_pad == True:
            ih, iw = x.size()[-2:]
            kh, kw = self.kernel_size[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = self.dilation[-2:]
            # oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            # pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            # pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)

            oh, ow = (ih - 1) * sh + kh, (iw - 1) * sw + kw

            pad_h = ih * sh - oh
            pad_w = iw * sw - oh
            if pad_h != 0 or pad_w != 0:
                self.output_padding = (pad_h % 2 if pad_h < 0 else pad_h, pad_w % 2 if pad_w < 0 else pad_w)
                pad_h = -1 * (pad_h - self.output_padding[0]) // 2 if pad_h < 0 else 0
                pad_w = -1 * (pad_w - self.output_padding[1]) // 2 if pad_w < 0 else 0
                self.padding = (pad_h, pad_w)
        return F.conv_transpose2d(x, self.weight, self.bias, self.strides, padding=self.padding,  output_padding=self.output_padding, dilation=self.dilation, groups=self.groups)

    def forward(self, x):
        x = self.conv2d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class TransConv3d(_ConvNd):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 groups=1, **kwargs):
        kernel_size = _triple(kernel_size)
        strides = _triple(strides)
        dilation = _triple(dilation)
        super(TransConv3d, self).__init__(kernel_size, num_filters, strides, auto_pad, use_bias, dilation, groups, True,
                                          **kwargs)
        if 'padding' in kwargs:
            self.padding = _triple(kwargs.get('padding'))
            self.auto_pad = False
        else:
            self.padding = _triple(0)
        self.output_padding = _triple(0)

    def conv3d_forward(self, x):
        if self.auto_pad == True:
            iz, ih, iw = x.size()[-3:]
            kz, kh, kw = self.kernel_size[-3:]
            sz, sh, sw = self.strides[-3:]
            dz, dh, dw = self.dilation[-3:]
            oz, oh, ow = math.ceil(iz / sz), math.ceil(ih / sh), math.ceil(iw / sw)
            pad_z = max((oz - 1) * sz + (kz - 1) * dz + 1 - iz, 0)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)

            if pad_z > 0 or pad_h > 0 or pad_w > 0:
                self.padding = [pad_z, pad_w, pad_h]
                self.output_padding = _triple(1)
        return F.conv_transpose3d(x, self.weight, self.bias, self.strides, padding=self.padding,
                                  output_padding=self.output_padding, dilation=self.dilation, groups=self.groups)

    def forward(self, x):
        x = self.conv3d_forward(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class SeparableConv1d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(SeparableConv1d, self).__init__()
        self.kernel_size = _single(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _single(dilation)
        self.strides = _single(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self.pointwise = None
    

    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv1d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)
            self.pointwise = torch.nn.Conv1d(self.num_filters, self.num_filters, 1, 1, 0, 1, 1, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            iw = x.size()[-1]
            kw = self.weight.size()[-1]
            sw = self.strides[-1]
            dw = self.dilation[-1]
            ow = math.ceil(iw / sw), math.ceil(iw / sw)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2], mode='replicate')

        x = self.conv1(x)
        x = self.pointwise(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class SeparableConv2d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(SeparableConv2d, self).__init__()
        self.kernel_size = _pair(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _pair(dilation)
        self.strides = _pair(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self.pointwise = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv2d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)
            self.pointwise = torch.nn.Conv2d(self.input_filters, self.num_filters, 1, 1, 0, 1, 1, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            ih, iw = x.size()[-2:]
            kh, kw = self.weight.size()[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = self.dilation[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')
        x = self.conv1(x)
        x = self.pointwise(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class SeparableConv3d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(SeparableConv3d, self).__init__()
        self.kernel_size = _triple(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _triple(dilation)
        self.strides = _triple(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self.pointwise = None


    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv3d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)
            self.pointwise = torch.nn.Conv3d(self.input_filters, self.num_filters, 1, 1, 0, 1, 1, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            iz, ih, iw = x.size()[-3:]
            kz, kh, kw = self.kernel_size[-3:]
            sz, sh, sw = self.strides[-3:]
            dz, dh, dw = self.dilation[-3:]
            oz, oh, ow = math.ceil(iz / sz), math.ceil(ih / sh), math.ceil(iw / sw)
            pad_z = max((oz - 1) * sz + (kz - 1) * dz + 1 - iz, 0)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_z > 0 or pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2, pad_z // 2,
                              pad_z - pad_z // 2], mode='replicate')
        x = self.conv1(x)
        x = self.pointwise(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class DepthwiseConv1d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(DepthwiseConv1d, self).__init__()
        self.kernel_size = _single(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _single(dilation)
        self.strides = _single(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv1d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            iw = x.size()[-1]
            kw = self.weight.size()[-1]
            sw = self.strides[-1]
            dw = self.dilation[-1]
            ow = math.ceil(iw / sw), math.ceil(iw / sw)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2], mode='replicate')

        x = self.conv1(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class DepthwiseConv2d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(DepthwiseConv2d, self).__init__()
        self.kernel_size = _pair(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _pair(dilation)
        self.strides = _pair(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv2d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            ih, iw = x.size()[-2:]
            kh, kw = self.weight.size()[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = self.dilation[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')
        x = self.conv1(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class DepthwiseConv3d(Modulex):
    def __init__(self, kernel_size, depth_multiplier=1, strides=1, auto_pad=True, activation=None, use_bias=False,
                 dilation=1, groups=1, **kwargs):
        super(DepthwiseConv3d, self).__init__()
        self.kernel_size = _triple(kernel_size)
        self.num_filters = kwargs.get('num_filters')
        self.depth_multiplier = 1
        self.dilation = _triple(dilation)
        self.strides = _triple(strides)
        self.use_bias = use_bias
        self.auto_pad = auto_pad

        self.activation = get_activation(activation)
        self.conv1 = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.conv1 is None:
            self.num_filters = self.input_filters * self.depth_multiplier if self.depth_multiplier is not None else self.num_filters
            self.conv1 = torch.nn.Conv3d(self.input_filters, self.num_filters, kernel_size=self.kernel_size,
                                         stride=self.strides, padding=0, dilation=self.dilation,
                                         groups=self.input_filters, bias=self.use_bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad == True:
            iz, ih, iw = x.size()[-3:]
            kz, kh, kw = self.kernel_size[-3:]
            sz, sh, sw = self.strides[-3:]
            dz, dh, dw = self.dilation[-3:]
            oz, oh, ow = math.ceil(iz / sz), math.ceil(ih / sh), math.ceil(iw / sw)
            pad_z = max((oz - 1) * sz + (kz - 1) * dz + 1 - iz, 0)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_z > 0 or pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2, pad_z // 2,
                              pad_z - pad_z // 2], mode='replicate')
        x = self.conv1(x)
        if self.activation is not None:
            x = self.activation(x)
        return x


class GcdConv1d(Modulex):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 divisor_rank=0, self_norm=True, is_shuffle=False, **kwargs):
        super(GcdConv1d, self).__init__()
        self.kernel_size = _single(kernel_size)
        self.num_filters = num_filters
        self.strides = _single(strides)
        self.auto_pad = auto_pad
        self.padding=0

        self.activation = get_activation(activation)
        self.dilation = _single(dilation)
        self.self_norm = self_norm
        self.norm=None
        self.is_shuffle = is_shuffle
        self.use_bias = use_bias
        self.divisor_rank = divisor_rank
        self.crossgroup_fusion = False
        self.weight = None
        self.bias = None
        self.groups = 1
        self._is_built = False

    def calculate_gcd(self):
        if self.input_filters is None or not isinstance(self.input_filters, int):
            raise ValueError('in_channels must be integer ')
        gcd_list = gcd(self.input_filters, self.num_filters)
        if len(gcd_list) == 0:
            self.groups = self.input_filters
            self.num_filters_1 = self.input_filters
        else:
            self.gcd = gcd_list[0]
            self.groups = gcd_list[min(int(self.divisor_rank), len(gcd_list))]

        if self.input_filters == self.num_filters or self.input_filters == self.gcd or self.num_filters == self.gcd:
            self.groups = gcd_list[min(int(self.divisor_rank + 1), len(gcd_list))]

    def build_once(self, input_shape):
        if self._is_built == False :
            self.calculate_gcd()
            print('input:{0} -> output:{1}   {2}  {3}  gcd:{4} group:{5}   通道縮放倍數:{5} '.format(self.input_filters,
                                                                                               self.num_filters,
                                                                                               self.input_filters // self.groups,
                                                                                               self.num_filters // self.groups,
                                                                                               self.gcd, self.groups,
                                                                                               self.num_filters / self.num_filters))

            self.channel_kernal = 2  if self.crossgroup_fusion == True and self.groups > 3 else 1
            self.channel_dilation = 1
            if self.crossgroup_fusion == True and self.groups > 4:
                self.channel_dilation = 2
            self.kernel_size = (self.channel_kernal,) + _pair(self.kernel_size)
            self.dilation = (self.channel_dilation,) + _pair(self.dilation)
            self.strides = (1,) + _pair(self.strides)
            reshape_input_shape = [-1, self._input_shape[0] // self.groups, self.groups, self._input_shape[1]]


            self.weight = Parameter(torch.Tensor(self.num_filters // self.groups, self._input_shape[0] // self.groups, *self.kernel_size))  #

            torch.nn.init.kaiming_uniform(self.gcd_conv3d.weight, mode='fan_in')
            if self.use_bias:
                self.bias = Parameter(torch.Tensor(self.num_filters // self.groups))

            if self.self_norm == True:
                self.norm = nn.BatchNorm1d(self.num_filters, momentum=0.1, affine=True, track_running_stats=True).to(
                    self.device)
                init.ones_(self.norm.weight)
                init.zeros_(self.norm.bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        if self.auto_pad:
            ih, iw = x.size()[-2:]
            kh, kw = self.kernel_size[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = _pair(self.dilation)[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')

        x = x.view(x.size(0), x.size(1) // self.groups, self.groups, x.size(2))
        pad_g = max((self.groups - 1) * 1 + (self.channel_kernal - 1) * self.channel_dilation + 1 - self.groups, 0)
        x = F.pad(x, [0, 0, 0, 0, pad_g // 2, pad_g - pad_g // 2], mode='reflect')

        x = F.conv2d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, 1)
        if self.is_shuffle == True:
            x = x.transpose([2, 1])
        x = x.view(x.size(0), x.size(1) * x.size(2), x.size(3))
        if self.self_norm == True:
            x = self.norm(x)
        if self.activation is not None:
            x = self.activation(x)
        if torch.isnan(x).any():
            print(self._get_name() + '  nan detected!!')
            raise ValueError('')
        return x

    def extra_repr(self):
        s = (
            'kernel_size={kernel_size}, {num_filters}, strides={strides}, activation={activation}, auto_pad={auto_pad} , dilation={dilation}')
        #     if self.groups != 1:
        #         s += ', groups={groups}'
        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)


class GcdConv2d(Modulex):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
                 divisor_rank=0, self_norm=True, is_shuffle=False, crossgroup_fusion=True, reshape_back=True,
                 need_reshape=True, **kwargs):
        super(GcdConv2d, self).__init__()
        self.kernel_size = _pair(kernel_size)
        self.num_filters = num_filters
        self.input_filters = None
        self.strides = _pair(strides)
        self.auto_pad = auto_pad
        self.padding = 0
        self.activation = get_activation(activation)
        self.dilation = _pair(dilation)
        self.self_norm = self_norm
        self.norm=None
        self.is_shuffle = is_shuffle
        self.use_bias = use_bias
        self.divisor_rank = divisor_rank

        self.groups = 1

        self.crossgroup_fusion = crossgroup_fusion

        self.weight=None
        self.bias=None
        self._is_built = False

    def calculate_gcd(self):
        if self.input_filters is None or not isinstance(self.input_filters, int):
            raise ValueError('in_channels must be integer ')
        gcd_list = gcd(self.input_filters, self.num_filters)
        if len(gcd_list) == 0:
            self.groups = self.input_filters
            self.num_filters_1 = self.input_filters
        else:
            self.gcd = gcd_list[0]
            self.groups = gcd_list[min(int(self.divisor_rank), len(gcd_list))]

        if self.input_filters == self.num_filters or self.input_filters == self.gcd or self.num_filters == self.gcd:
            self.groups = gcd_list[min(int(self.divisor_rank + 1), len(gcd_list))]

    def build_once(self, input_shape):
        if self._is_built == False :
            self.calculate_gcd()
            print('input:{0} -> output:{1}   {2}  {3}  gcd:{4} group:{5}   通道縮放倍數:{5} '.format(self.input_filters,
                                                                                               self.num_filters,
                                                                                               self.input_filters // self.groups,
                                                                                               self.num_filters // self.groups,
                                                                                               self.gcd, self.groups,
                                                                                               self.num_filters / self.num_filters))
            self.channel_kernal = 2 if self.crossgroup_fusion == True and self.groups > 3 else 1
            self.channel_dilation = 1
            if self.crossgroup_fusion == True and self.groups > 4:
                self.channel_dilation = 2

            reshape_input_shape = [-1, self._input_shape[0] // self.groups, self.groups,self._input_shape[1], self._input_shape[2]]

            self.kernel_size = (self.channel_kernal,) + _pair(self.kernel_size)
            self.dilation = (self.channel_dilation,) + _pair(self.dilation)
            self.strides = (1,) + _pair(self.strides)
            self.weight = Parameter(torch.Tensor(self.num_filters // self.groups, self._input_shape[0] // self.groups, *self.kernel_size))  #
            if self.use_bias:
                self.bias = Parameter(torch.Tensor(self.num_filters // self.groups))

            torch.nn.init.kaiming_uniform(self.weight, mode='fan_in')

            if self.self_norm == True:
                self.norm = nn.BatchNorm2d(self.num_filters,momentum=0.1, affine=True, track_running_stats=True).to(self.device)
                init.ones_(self.norm.weight)
                init.zeros_(self.norm.bias)


            self.to(self.device)
            self._is_built = True

    def forward(self, x):
        # if x.dim() == 5:
        #     self.need_reshape=False
        #     self.build_once(x.size(1)*x.size(2))
        # 
        # elif x.dim() == 4:
        #     self.need_reshape=True
        #     self.build_once(x.size(1))
        # else:
        #     raise ValueError('only dim=4 or 5 is compatable for Gcd_Conv2d')

        if self.auto_pad:
            ih, iw = x.size()[-2:]
            kh, kw = self.kernel_size[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = _pair(self.dilation)[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')


        x = x.view(x.size(0), x.size(1) // self.groups, self.groups, x.size(2), x.size(3))
        if self.crossgroup_fusion == True:
            pad_g = max((self.groups - 1) * 1 + (self.channel_kernal - 1) * self.channel_dilation + 1 - self.groups, 0)
            x = F.pad(x, [0, 0, 0, 0, pad_g // 2, pad_g - pad_g // 2], mode='circular')

        x =F.conv3d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, 1)
        if self.is_shuffle == True:
            x = x.transpose([2, 1])

        x = x.view(x.size(0), x.size(1) * x.size(2), x.size(3), x.size(4))
        if self.self_norm == True:
            x = self.norm(x)
        if self.activation is not None:
            x = self.activation(x)
        if torch.isnan(x).any():
            print(self._get_name() + '  nan detected!!')
            raise ValueError('')
        return x

    def extra_repr(self):
        s = (
            'kernel_size={kernel_size}, {num_filters}, strides={strides}, activation={activation}, auto_pad={auto_pad} , dilation={dilation}')
        #     if self.groups != 1:
        #         s += ', groups={groups}'
        #     if self.bias is None:
        #         s += ', use_bias=False'
        return s.format(**self.__dict__)


class GcdConv2d_1(Modulex):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False,
                 divisor_rank=0, dilation=1, self_norm=True, **kwargs):
        super(GcdConv2d_1, self).__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.input_filters = 3
        self.strides = _pair(strides)
        self.auto_pad = auto_pad
        self.padding = 0

        self.activation = get_activation(activation)
        self.dilation = dilation
        self.self_norm = self_norm
        self.norm=None
        self.use_bias = use_bias

        self.weight = None
        self.bias = None
        self.divisor_rank = divisor_rank
        self.groups = 1
        self._is_built = False

    def calculate_gcd(self):
        gcd_list = _gcd(self.input_filters, self.num_filters)
        if len(gcd_list) == 0:
            self.groups = self.input_filters
            self.num_filters_1 = self.input_filters
        else:
            self.gcd = gcd_list[0]
            self.groups = gcd_list[min(int(self.divisor_rank), len(gcd_list))]

            self.num_filters_1 = self.gcd
            self.num_filters_2 = self.num_filters
            factors = _get_divisors(self.num_filters // self.gcd)

        if self.input_filters == self.num_filters or self.input_filters == self.gcd or self.num_filters == self.gcd:
            self.groups = gcd_list[min(int(self.divisor_rank + 1), len(gcd_list))]

    def build_once(self, input_shape):
        if self._is_built == False:
            self.calculate_gcd()
            print('input:{0} -> output:{1}   {2}  {3}  gcd:{4} group:{5}   通道縮放倍數:{5} '.format(self.input_filters,
                                                                                               self.num_filters,
                                                                                               self.input_filters // self.groups,
                                                                                               self.num_filters // self.groups,
                                                                                               self.gcd, self.groups,
                                                                                               self.num_filters / self.num_filters))

            self.weight = Parameter( torch.Tensor(self.input_filters, self.num_filters // self.groups, *self.kernel_size)) #
            if self.use_bias:
                self.bias = Parameter(torch.Tensor(self.num_filters // self.groups))

            torch.nn.init.kaiming_uniform(self.weight, mode='fan_in')
            torch.nn.init.kaiming_uniform(self.gcd_conv2d.weight, mode='fan_in')

            if self.self_norm == True:
                self.norm = nn.BatchNorm2d(self.num_filters, momentum=0.1, affine=True, track_running_stats=True).to( self.device)
                init.ones_(self.norm.weight)
                init.zeros_(self.norm.bias)

            self.to(self.device)
            self._is_built = True

    def forward(self, x):

        if self.auto_pad:
            ih, iw = x.size()[-2:]
            kh, kw = self.gcd_conv2d.weight.size()[-2:]
            sh, sw = self.strides[-2:]
            dh, dw = _pair(self.dilation)[-2:]
            oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
            pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
            pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
            if pad_h > 0 or pad_w > 0:
                x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')

        x = F.conv2d(x, self.weight, self.bias, self.strides, self.padding, self.dilation, self.groups)
        if self.self_norm == True:
            x = self.norm(x)

        if self.activation is not None:
            x = self.activation(x)
        return x

#
# class GcdConv2d_2(Modulex):
#     def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, dilation=1,
#                  divisor_rank=0, self_norm=True, is_shuffle=False, **kwargs):
#         super(GcdConv2d_2, self).__init__()
#         self.kernel_size = _pair(kernel_size)
#         self.num_filters = num_filters
#         self.input_filters = None
#         self.strides = _pair(strides)
#         self.auto_pad = auto_pad
#
#         self.activation = get_activation(activation)
#         self.dilation = _pair(dilation)
#         self.self_norm = self_norm
#         self.is_shuffle = is_shuffle
#         self.use_bias = use_bias
#         self.divisor_rank = divisor_rank
#
#         self.groups = 1
#         self.weight = None
#         self.bias = None
#         self._is_built = False
#
#     def calculate_gcd(self):
#         if self.input_filters is None or not isinstance(self.input_filters, int):
#             raise ValueError('in_channels must be integer ')
#         gcd_list = gcd(self.input_filters, self.num_filters)
#         if len(gcd_list) == 0:
#             self.groups = self.input_filters
#             self.num_filters_1 = self.input_filters
#         else:
#             self.gcd = gcd_list[0]
#             self.groups = gcd_list[min(int(self.divisor_rank), len(gcd_list))]
#
#         if self.input_filters == self.num_filters or self.input_filters == self.gcd or self.num_filters == self.gcd:
#             self.groups = gcd_list[min(int(self.divisor_rank + 1), len(gcd_list))]
#
#     def build_once(self, input_shape):
#         if self._is_built == False :
#             self.calculate_gcd()
#             print('input:{0} -> output:{1}   {2}  {3}  gcd:{4} group:{5}   通道縮放倍數:{5} '.format(self.input_filters,
#                                                                                                self.num_filters,
#                                                                                                self.input_filters // self.groups,
#                                                                                                self.num_filters // self.groups,
#                                                                                                self.gcd, self.groups,
#                                                                                                self.num_filters / self.num_filters))
#             self.channel_kernal = 2 if self.groups > 3 else 1
#             self.channel_dilation = 1
#             if self.groups > 4:
#                 self.channel_dilation = 2
#
#             self.gcd_conv3d = Conv3d((self.channel_kernal,) + _pair(self.kernel_size), self.num_filters // self.groups,
#                                      (1,) + _pair(self.strides), auto_pad=False, activation=None,
#                                      use_bias=self.use_bias, dilation=(self.channel_dilation,) + _pair(self.dilation),
#                                      groups=1).to(_device)
#             self.gcd_conv3d.build_once(self.input_filters // self.groups)
#             torch.nn.init.kaiming_uniform(self.gcd_conv3d.weight, mode='fan_in')
#
#             if self.self_norm == True:
#                 self.norm = nn.BatchNorm2d(self.num_filters, momentum=0.1, affine=True, track_running_stats=True).to(
#                     self.device)
#                 init.ones_(self.norm.weight)
#                 init.zeros_(self.norm.bias)
#
#             self.to(self.device)
#             self._is_built = True
#
#     def forward(self, x):
#         # self.build_once(x.size(1))
#         if self.auto_pad:
#             ih, iw = x.size()[-2:]
#             kh, kw = self.kernel_size[-2:]
#             sh, sw = self.strides[-2:]
#             dh, dw = _pair(self.dilation)[-2:]
#             oh, ow = math.ceil(ih / sh), math.ceil(iw / sw)
#             pad_h = max((oh - 1) * sh + (kh - 1) * dh + 1 - ih, 0)
#             pad_w = max((ow - 1) * sw + (kw - 1) * dw + 1 - iw, 0)
#             if pad_h > 0 or pad_w > 0:
#                 x = F.pad(x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2], mode='replicate')
#
#         x = x.view(x.size(0), x.size(1) // self.groups, self.groups, x.size(2), x.size(3))
#         pad_g = max((self.groups - 1) * 1 + (self.channel_kernal - 1) * self.channel_dilation + 1 - self.groups, 0)
#         x = F.pad(x, [0, 0, 0, 0, pad_g // 2, pad_g - pad_g // 2], mode='circular')
#
#         x = self.gcd_conv3d(x)
#         if self.is_shuffle == True:
#             x = x.transpose([2, 1])
#         x = x.view(x.size(0), x.size(1) * x.size(2), x.size(3), x.size(4))
#         if self.self_norm == True:
#             x = self.norm(x)
#         if self.activation is not None:
#             x = self.activation(x)
#         if torch.isnan(x).any():
#             print(self._get_name() + '  nan detected!!')
#             raise ValueError('')
#         return x
#
#     def extra_repr(self):
#         s = (
#             'kernel_size={kernel_size}, {num_filters}, strides={strides}, activation={activation}, auto_pad={auto_pad} , dilation={dilation}')
#         #     if self.groups != 1:
#         #         s += ', groups={groups}'
#         #     if self.bias is None:
#         #         s += ', use_bias=False'
#         return s.format(**self.__dict__)
#




class GlobalAvgPool1d(Modulex):
    def __init__(self):
        super(GlobalAvgPool1d, self).__init__()
    def build_once(self, input_shape):
        pass
    def forward(self, x):
        assert len(x.size()) == 3, x.size()
        B, C, L = x.size()
        return F.avg_pool1d(x, L)


class GlobalAvgPool2d(Modulex):
    def __init__(self):
        super(GlobalAvgPool2d, self).__init__()
    def build_once(self, input_shape):
        pass
    def forward(self, x):
        assert len(x.size()) == 4, x.size()
        B, C, W, H = x.size()
        return F.avg_pool2d(x, (W, H))


class Lambda(Modulex):
    """
    Applies a lambda function on forward()
    Args:
        lamb (fn): the lambda function
    """

    def __init__(self, lam):
        super(Lambda, self).__init__()
        self.lam = lam

    def forward(self, x):
        return self.lam(x)


class Reshape(Modulex):
    """
    Reshape the input volume
    Args:
        *shape (ints): new shape, WITHOUT specifying batch size as first
        dimension, as it will remain unchanged.
    """

    def __init__(self, shape):
        super(Reshape, self).__init__()
        if isinstance(shape, tuple):
            self.shape = [shape[i] for i in range(len(shape))]
        elif isinstance(shape, list):
            self.shape = shape

    def forward(self, x):
        shp = self.shape.copy()
        shp.insert(0, x.size(0))
        shp = tuple(shp)
        return torch.reshape(x, shp)


class SelfAttention(Modulex):
    """ Self attention Layer"""

    def __init__(self, reduction_factor=8):
        super(SelfAttention, self).__init__()
        #self.activation = activation
        self.reduction_factor=reduction_factor
        self.query_conv = None
        self.key_conv =  None
        self.value_conv = None
        
        self.gamma = nn.Parameter(torch.zeros(1))

        self.softmax = nn.Softmax(dim=-1)  #
    def build_once(self,input_shape ):
        self.query_conv = nn.Conv2d(in_channels=self.input_filters, out_channels=self.input_filters // self.reduction_factor, kernel_size=1)
        self.key_conv = nn.Conv2d(in_channels=self.input_filters, out_channels=self.input_filters // self.reduction_factor, kernel_size=1)
        self.value_conv = nn.Conv2d(in_channels=self.input_filters, out_channels=self.input_filters, kernel_size=1)
        self.to(_device)
    def forward(self, x):
        """
            inputs :
                x : input feature maps( B X C X W X H)
            returns :
                out : self attention value + input feature 
                attention: B X N X N (N is Width*Height)
        """
        B, C, width, height = x.size()
        proj_query = self.query_conv(x).view(B, -1, width * height).permute(0, 2, 1)  # B X CX(N)
        proj_key = self.key_conv(x).view(B, -1, width * height)  # B X C x (*W*H)
        energy = torch.bmm(proj_query, proj_key)  # transpose check
        attention = self.softmax(energy)  # BX (N) X (N) 
        proj_value = self.value_conv(x).view(B, -1, width * height)  # B X C X N

        out = torch.bmm(proj_value, attention.permute(0, 2, 1))
        out = out.view(B, C, width, height)

        out = self.gamma * out + x
        return out, attention







"""
Implementation of the CoordConv modules from https://arxiv.org/abs/1807.03247
"""


def _append_coords(input_tensor, with_r=False):
    batch_size, _, x_dim, y_dim = input_tensor.size()

    xx_channel = torch.arange(x_dim).repeat(1, y_dim, 1)
    yy_channel = torch.arange(y_dim).repeat(1, x_dim, 1).transpose(1, 2)

    xx_channel = xx_channel.float() / (x_dim - 1)
    yy_channel = yy_channel.float() / (y_dim - 1)

    xx_channel = xx_channel * 2 - 1
    yy_channel = yy_channel * 2 - 1

    xx_channel = xx_channel.repeat(batch_size, 1, 1, 1).transpose(2, 3)
    yy_channel = yy_channel.repeat(batch_size, 1, 1, 1).transpose(2, 3)

    ret = torch.cat([input_tensor, xx_channel.type_as(input_tensor), yy_channel.type_as(input_tensor), ], dim=1, )

    if with_r:
        rr = torch.sqrt(
            torch.pow(xx_channel.type_as(input_tensor) - 0.5, 2) + torch.pow(yy_channel.type_as(input_tensor) - 0.5, 2))
        ret = torch.cat([ret, rr], dim=1)

    return ret


"""
An alternative implementation for PyTorch with auto-infering the x-y dimensions.
https://github.com/mkocabas/CoordConv-pytorch/blob/master/CoordConv.py
"""


class CoordConv2d(Modulex):
    def __init__(self, kernel_size, num_filters, strides, auto_pad=True, activation=None, use_bias=False, group=1,
                 dilation=1, with_r=False, **kwargs):
        super().__init__()
        self.kernel_size = kernel_size
        self.num_filters = num_filters
        self.strides = strides
        self.auto_pad = auto_pad
        self.use_bias = use_bias
        self.group = group
        self.dilation = dilation
        self._conv_settings = kwargs
        self.activation = get_activation(activation)
        self.addcoords = partial(_append_coords, with_r=with_r)
        self.conv = None

    def build_once(self, input_shape):
        if self._is_built == False:
            self.conv = Conv2d(self.kernel_size, self.num_filters, self.strides, auto_pad=self.auto_pad,
                               activation=self.activation, use_bias=self.use_bias, group=self.group,
                               dilation=self.dilation, **self._conv_settings)
            self._is_built = True

    def forward(self, x):
        ret = self.addcoords(x)
        ret = self.conv(ret)
        return ret


UpsamplingBilinear2d = nn.UpsamplingBilinear2d



class Droupout(Modulex):
    def __init__(self, dropout_rate=0, ):
        super(Droupout, self).__init__()
        self.inplace = True
        if dropout_rate < 0 or dropout_rate > 1:
            raise ValueError("dropout probability has to be between 0 and 1, ""but got {}".format(dropout_rate))
        self.dropout_rate=dropout_rate

    def forward(self, x):
        return F.dropout(x, self.p, self.training, self.inplace)
    def extra_repr(self):
        return 'p={}, inplace={}'.format(self.p, self.inplace)

class AlphaDroupout(Modulex):
    '''
     .. _Self-Normalizing Neural Networks: https://arxiv.org/abs/1706.02515
    '''
    def __init__(self, dropout_rate=0, ):
        super(AlphaDroupout, self).__init__()
        self.inplace = True
        if dropout_rate < 0 or dropout_rate > 1:
            raise ValueError("dropout probability has to be between 0 and 1, ""but got {}".format(dropout_rate))
        self.dropout_rate=dropout_rate

    def forward(self, x):
        return F.alpha_dropout(x, self.p, self.training, self.inplace)
    def extra_repr(self):
        return 'p={}, inplace={}'.format(self.p, self.inplace)
