from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import init
from torch.nn.parameter import Parameter
from ..backend.common import epsilon,get_function,get_session
from ..backend.pytorch_backend import Modulex
import numpy as np


__all__ = ['InstanceNorm2d','BatchNorm','BatchNorm2d','BatchNorm3d','GroupNorm2d','LayerNorm2d','get_normalization']
_session = get_session()
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_epsilon=_session.epsilon


class InstanceNorm2d(Modulex):
    def __init__(self,  momentum=0.1, affine=True):
        """
        http://pytorch.org/docs/stable/nn.html#batchnorm1d

        Args:
            dim: 1d, 2d, or 3d BatchNorm
         eps: nn.BatchNorm parameter
            momentum: nn.BatchNorm parameter
            affine: nn.BatchNorm parameter
            track_running_stats: nn.BatchNorm parameter
        """
        super().__init__()
        self.momentum=momentum
        self.affine=affine
        self.norm_kwargs = dict(eps=_epsilon,
            momentum=self.momentum,
            affine=self.affine)
        self.normalizer = None
        self.weight = None
        self.bias = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.normalizer is None:
            self.normalizer = nn.InstanceNorm2d(self.input_filters, **self.norm_kwargs).to(_device)
            self._is_built = True
    def forward(self, x):
        return self.normalizer(x)

class BatchNorm(Modulex):
    def __init__(self,  momentum=0.1, affine=True, track_running_stats=True):
        """
        http://pytorch.org/docs/stable/nn.html#batchnorm1d

        Args:
            dim: 1d, 2d, or 3d BatchNorm
         eps: nn.BatchNorm parameter
            momentum: nn.BatchNorm parameter
            affine: nn.BatchNorm parameter
            track_running_stats: nn.BatchNorm parameter
        """
        super().__init__()

        self.eps = _epsilon
        self.momentum = momentum
        self.affine = affine
        self.track_running_stats = track_running_stats
        self.weight=None
        self.bias = None


    def reset_running_stats(self):
        if self.track_running_stats:
            self.running_mean.zero_()
            self.running_var.fill_(1)
            self.num_batches_tracked.zero_()

    def reset_parameters(self):
        self.reset_running_stats()
        if self.affine :
            init.ones_(self.weight)
            init.zeros_(self.bias)
    def build_once(self, input_shape):
        if self._is_built == False:
            if self.affine:
                self.weight = Parameter(torch.Tensor(self.input_filters))
                self.bias = Parameter(torch.Tensor(self.input_filters))

            if self.track_running_stats:
                self.register_buffer('running_mean', torch.zeros(self.input_filters))
                self.register_buffer('running_var', torch.ones(self.input_filters))
                self.register_buffer('num_batches_tracked', torch.tensor(0, dtype=torch.long))
            else:
                self.register_parameter('running_mean', None)
                self.register_parameter('running_var', None)
                self.register_parameter('num_batches_tracked', None)
            self.reset_parameters()
            self.to(_device)
            self._is_built = True
    def forward(self, x):
        if self.momentum is None:
            exponential_average_factor = 0.0
        else:
            exponential_average_factor = self.momentum

        if self.training and self.track_running_stats:
            # TODO: if statement only here to tell the jit to skip emitting this when it is None
            if self.num_batches_tracked is not None:
                self.num_batches_tracked += 1
                if self.momentum is None:  # use cumulative moving average
                    exponential_average_factor = 1.0 / float(self.num_batches_tracked)
                else:  # use exponential moving average
                    exponential_average_factor = self.momentum

        return F.batch_norm(x, self.running_mean, self.running_var, self.weight, self.bias, self.training or not self.track_running_stats, exponential_average_factor, self.eps)
    def extra_repr(self):
        return '{input_filters}, eps={eps}, momentum={momentum}, affine={affine}, ' \
               'track_running_stats={track_running_stats}'.format(**self.__dict__)

    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict,
                              missing_keys, unexpected_keys, error_msgs):
        version = local_metadata.get('version', None)

        if (version is None or version < 2) and self.track_running_stats:
            # at version 2: added num_batches_tracked buffer
            #               this should have a default value of 0
            num_batches_tracked_key = prefix + 'num_batches_tracked'
            if num_batches_tracked_key not in state_dict:
                state_dict[num_batches_tracked_key] = torch.tensor(0, dtype=torch.long)

        super(_BatchNorm, self)._load_from_state_dict(
            state_dict, prefix, local_metadata, strict,
            missing_keys, unexpected_keys, error_msgs)

BatchNorm2d=BatchNorm
BatchNorm3d=BatchNorm



class GroupNorm2d(Modulex):
    def __init__(self, num_groups,affine=True):
        super().__init__()
        self.affine=affine
        self.norm_kwargs = dict(eps=_epsilon, affine=self.affine)
        self.num_groups = num_groups
        self.normalizer = None
        self._is_built = False

    def build_once(self, input_shape):
        if self._is_built == False or self.normalizer is None:
            assert self.input_filters % self.num_groups == 0, 'number of groups {} must divide number of channels {}'.format(self.num_groups, self.input_filters)
            self.normalizer = nn.GroupNorm(self.num_groups, self.input_filters, **self.norm_kwargs).to(_device)
            self._is_built = True
    def forward(self, x):
        return self.normalizer(x)


class LayerNorm2d(Modulex):
    def __init__(self, momentum=0.1, affine=True, track_running_stats=True):
        """
        http://pytorch.org/docs/stable/nn.html#batchnorm1d

        Args:
            dim: 1d, 2d, or 3d BatchNorm
         eps: nn.BatchNorm parameter
            momentum: nn.BatchNorm parameter
            affine: nn.BatchNorm parameter
            track_running_stats: nn.BatchNorm parameter
        """
        super().__init__()
        self.norm_kwargs = dict(eps=_epsilon, momentum=momentum, affine=affine, track_running_stats=track_running_stats)
        self.bias = None
        self._is_built = False
        self.normalizer = None
    def build_once(self, input_shape):
        if self._is_built == False or self.normalizer is None:
            self.normalizer =_LayerNorm(self.input_filters, **self.norm_kwargs).to(_device)
            self._is_built=True
    def forward(self, x):
        return self.normalizer(x)

class _LayerNorm(nn.Module):
    """
    Layer Normalization (https://arxiv.org/pdf/1607.06450.pdf).
    """
    def __init__(self, last_dim_size, eps=1e-6):
        """
        :param last_dim_size: Size of last dimension.
        :param eps: Small number for numerical stability (avoid division by zero).
        """
        super(_LayerNorm, self).__init__()
        self._a_2 = nn.Parameter(torch.ones(last_dim_size))
        self._b_2 = nn.Parameter(torch.zeros(last_dim_size))
        self._eps = eps
    def forward(self, x):
        """
        :param x: Tensor to be layer normalized.
        :return: Layer normalized Tensor.
        """
        mean = x.mean(dim=-1, keepdim=True).detach()
        std = x.std(dim=-1, keepdim=True).detach()
        return self._a_2 * (x - mean) / (std + self._eps) + self._b_2

def get_normalization(fn_name):
    if fn_name is None:
        return None
    if isinstance(fn_name, str):
        if fn_name.lower().strip() in ['instance','in','i']:
            return InstanceNorm2d()
        elif  fn_name.lower().strip() in ['batch','b']:
            return BatchNorm()
        elif  fn_name.lower().strip() in ['group','g']:
            return GroupNorm2d(num_groups=16)
    fn_modules = ['trident.layers.pytorch_normalizations']
    normalization_fn_ = get_function(fn_name, fn_modules)
    normalization_fn = normalization_fn_
    return normalization_fn
