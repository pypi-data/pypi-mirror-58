from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import matplotlib
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from collections import deque
import six
import logging
import os
import sys
import re
import warnings
from collections import OrderedDict
from functools import partial,wraps,update_wrapper
from itertools import islice
import operator
import torch
import torch.nn as nn
import torchvision
from collections import OrderedDict
import numpy as np


__all__ = ['to_numpy','to_tensor','print_network','plot_tensor_grid','summary','calculate_flops','Modulex','Sequential','Input','ShortcutContainer','ConcatContainer','get_device','load']

version=torch.__version__
sys.stderr.write('Pytorch version:{0}.\n'.format(version))
if version<'1.2.0':
    raise ValueError('Not support Pytorch below 1.2' )
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if torch.cuda.is_available() :
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = True


def get_device():
    return  _device

load=torch.load


import sys

from functools import partial
from typing import List, IO, Union, Tuple, Type, Callable





def to_numpy(x) -> np.ndarray:

    """
    Convert whatever to numpy array
    :param x: List, tuple, PyTorch tensor or numpy array
    :return: Numpy array
    """
    if isinstance(x, np.ndarray):
        return x
    elif isinstance(x, torch.Tensor):
        return x.cpu().detach().numpy()
    elif isinstance(x, (list, tuple, int, float)):
        return np.array(x)
    else:
        raise ValueError("Unsupported type")

def to_tensor(x, dtype=torch.float32) -> torch.Tensor:
    if isinstance(x,  torch.Tensor):
        if dtype is not None:
            x = x.type(dtype)
        x=x.to(_device)
        return x

    if isinstance(x, (list, tuple)):
        x = np.ndarray(x)

    if isinstance(x, np.ndarray):
        npdtype=x.dtype
        x = torch.from_numpy(x)
        if 'int64' in str(npdtype):
            x = x.type(torch.int64)
        else:
            x = x.type(dtype)
        x = x.to(_device)
        return x
    else:
        raise ValueError("Unsupported input type" + str(type(x)))


class Modulex(nn.Module):
    """
    Applies a lambda function on forward()
    Args:
        lamb (fn): the lambda function
    """

    def __init__(self):
        super(Modulex, self).__init__()
        self._is_built= False
        self._build_hook=None
        self._input_shape=None
        self.input_filters =None
        self.batch_size=-1
        self.output_shape = None
        self.dump_patches = True
        self._fn = []


        self.regist_shape_infer_hook()

    @property
    def device(self):
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @property
    def input_shape(self):
        return self._input_shape

    @input_shape.setter
    def input_shape(self, value):
        if self._is_built == False:
            if isinstance(value,list):
                self._input_shape = value
            elif isinstance(value,tuple):
                self._input_shape = [int(value[i]) for i in range(len(value))]
            elif isinstance(value, torch.Tensor) and value.dim()<=1:
                self._input_shape = to_numpy(value.int()).tolist()
            elif isinstance(value, np.ndarray) and value.ndim<=1:
                self._input_shape = value.astype(np.uint8).tolist()
            else:
                raise ValueError('not valid input_shape')


            self.input_filters = self._input_shape[0]
            self.build_once(self._input_shape)
            batch_input_shape=self._input_shape.copy()
            batch_input_shape.insert(0,2)
            x = torch.from_numpy(np.random.standard_normal(batch_input_shape).astype(np.float32)).to(self.device)
            self.forward(x)


    def regist_shape_infer_hook(self):
        def hook(module, input):
            if module._is_built == False and isinstance(input,list) and callable(getattr(module, 'build_once')):
                module.input_shape = [inp.size()[1:] for inp in input]
            elif module._is_built == False and callable(getattr(module, 'build_once')):
                module.input_shape=input[0].size()[1:]

        if (isinstance(self, Modulex)  and not isinstance(self, Sequential) and self._is_built== False):
            self._build_hook=self.register_forward_pre_hook(hook)

    def reset_parameters(self):
        pass
    def build_once(self,input_shape ):
        pass  #pass if no need shape infer
    def shape_infer(self,input_shape):
        self.input_shape=input_shape
    def __call__(self, *input, **kwargs):
        for hook in self._forward_pre_hooks.values():
            result = hook(self, input)
            if result is not None:
                if not isinstance(result, tuple):
                    result = (result,)
                input = result
        if self._build_hook is not None:
            self._build_hook.remove()
        if isinstance(input[0],Input):
            inp=input[0]
            inp._fn.append(self)
            return inp
        if torch._C._get_tracing_state():
            result = self._slow_forward(*input, **kwargs)
        else:
            result = self.forward(*input, **kwargs)
        for hook in self._forward_hooks.values():
            hook_result = hook(self, input, result)
            if hook_result is not None:
                result = hook_result
        if len(self._backward_hooks) > 0:
            var = result
            while not isinstance(var, torch.Tensor):
                if isinstance(var, dict):
                    var = next((v for v in var.values() if isinstance(v, torch.Tensor)))
                else:
                    var = var[0]
            grad_fn = var.grad_fn
            if grad_fn is not None:
                for hook in self._backward_hooks.values():
                    wrapper = partial(hook, self)
                    update_wrapper(wrapper, hook)
                    grad_fn.register_hook(wrapper)
        return result


class Input(Modulex):
    def __init__(self, inputshape: (list, tuple) = None, batch_shape: (list, tuple) = None,
                 inputtensor: torch.tensor = None):
        super().__init__()
        if inputtensor is not None:
            self.inputtensor = inputtensor
            self.batch_shape = list(to_numpy(inputtensor.size()))
            self.inputshape = self.batch_shape[1:]
        else:
            if self.batch_shape is not None:
                if isinstance(batch_shape, tuple):
                    self.batch_shape = [int(batch_shape[i]) for i in range(len(batch_shape))]
                else:
                    self.batch_shape = batch_shape
                self.inputshape = self.batch_shape[1:]
            else:
                if isinstance(inputshape, tuple):
                    self.inputshape = [int(inputshape[i]) for i in range(len(inputshape))]
                else:
                    self.inputshape = inputshape

                self.batch_shape = self.inputshape.copy()
                self.batch_shape.insert(0, 1)

    def forward(self, x):
        if x is None:
            return torch.tensor(np.zeros(self.batch_shape, dtype=np.float32))
        else:
            return x

class Sequential(Modulex):
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
        super(Sequential, self).__init__()
        self._is_built = False

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
        keys = super(Sequential, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def forward(self, x):
        for module in self._modules.values():
            x = module(x)
        return x

class ConcatContainer(Modulex):
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
        self._is_built = False
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
        keys = super(ConcatContainer, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def forward(self, x):
        results=[]
        for module in self._modules.values():
            x1 = module(x)
            results.append(x1)
        return torch.cat(results,dim=1)

class ShortcutContainer(Modulex):
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
        self._is_built = False
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



def print_network(net, verbose=False):
    num_params = 0
    for i, param in enumerate(net.parameters()):
        num_params += param.numel()
    if verbose:
        logging.info(net)
    logging.info('Total number of parameters: %d\n' % num_params)




def plot_tensor_grid(batch_tensor, save_filename=None):
    ''' Helper to visualize a batch of images.
        A non-None filename saves instead of doing a show()'''

    grid_img = torchvision.utils.make_grid(batch_tensor, nrow=5)
    plt.imshow(grid_img.permute(1, 2, 0))
    if save_filename is not None:
        torchvision.utils.save_image(batch_tensor, save_filename, padding=5)
    else:
        plt.show()



def calculate_flops(gen:nn.Module):
    """
    Calculate the flops given a generator of pytorch model.
    It only compute the flops of forward pass.

    Example:
        >>> net = torchvision.models.resnet18()
        >>> calculate_flops(net.children())
    """
    flops = 0
    mods=gen.named_modules()
    mods=list(mods)[1:]
    param_nums = []
    param_sizes = []
    for mod_name,mod in mods:
        p = list(mod.parameters())
        modsz = []
        all_params = 0
        for j in range(len(p)):
            modsz.append(np.array(p[j].size()))
            all_params += np.prod(p[j].size())

        param_nums.append(all_params)
        param_sizes.append(modsz)

    return np.array(param_nums).sum()


# net = torchvision.models.resnet18()
# flops = calculate_flops(net.children())
# print(flops / 10 ** 9, 'G')  # 11.435429919 G



def summary(model, input_size, batch_size=-1, device="cuda"):
    def register_hook(module):
        def hook(module, input, output):
            class_name = str(module.__class__).split(".")[-1].split("'")[0]
            module_idx = len(summary)

            m_key = "%s-%i" % (class_name, module_idx + 1)
            summary[m_key] = OrderedDict()
            summary[m_key]["input_shape"] = list(input[0].size())
            summary[m_key]["input_shape"][0] = batch_size
            if isinstance(output, (list, tuple)):
                summary[m_key]["output_shape"] = [
                    [-1] + list(o.size())[1:] for o in output
                ]
            else:
                summary[m_key]["output_shape"] = list(output.size())
                summary[m_key]["output_shape"][0] = batch_size

            params = 0
            summary[m_key]["flops"]=np.array([0],dtype=np.float64)
            summary[m_key]["macc"] = np.array([0], dtype=np.float64)
            if hasattr(module, "weight") and hasattr(module.weight, "size"):
                params += torch.prod(torch.LongTensor(list(module.weight.size())))
                summary[m_key]["weight"] =list(module.weight.size())
                summary[m_key]["trainable"] = module.weight.requires_grad
                summary[m_key]["flops"] += (2*np.prod(np.array(summary[m_key]["weight"]).astype(np.float64))-1) * np.prod(np.array(summary[m_key]["output_shape"][2:]).astype(np.float64))
                summary[m_key]["macc"] += np.prod(np.array(summary[m_key]["weight"]).astype(np.float64)) * np.prod(np.array(summary[m_key]["output_shape"][2:]).astype(np.float64))

            if hasattr(module, "bias") and hasattr(module.bias, "size"):
                params += torch.prod(torch.LongTensor(list(module.bias.size())))
                summary[m_key]["bias"] =list(module.bias.size())
                summary[m_key]["flops"]+=np.prod(np.array(summary[m_key]["bias"]).astype(np.float64))*np.prod(np.array( summary[m_key]["output_shape"][2:]).astype(np.float64))
            summary[m_key]["nb_params"] = params

        if (
            not isinstance(module, nn.Sequential)
            and not isinstance(module, nn.ModuleList)
            and not (module == model)
        ):
            hooks.append(module.register_forward_hook(hook))

    device = device.lower()
    assert device in [
        "cuda",
        "cpu",
    ], "Input device is not valid, please specify 'cuda' or 'cpu'"

    if device == "cuda" and torch.cuda.is_available():
        dtype = torch.cuda.FloatTensor
    else:
        dtype = torch.FloatTensor

    # multiple inputs to the network
    if isinstance(input_size, tuple):
        input_size = [input_size]

    if isinstance(input_size, int):
        x = [torch.rand(2, input_size).type(dtype)]
    else:
        # batch_size of 2 for batchnorm
        x = [torch.rand(2, *in_size).type(dtype) for in_size in input_size]
    # p    rint(type(x[0]))

    # create properties
    summary = OrderedDict()
    hooks = []

    # register hook
    model.apply(register_hook)

    # make a forward pass
    # print(x.shape)
    model(*x)

    # remove these hooks
    for h in hooks:
        h.remove()

    print("--------------------------------------------------------------------------------------------------------------------------------")
    line_new = "{:>40} {:>30}  {:>30} {:>15}  {:>15}  {:>15}".format("Layer (type)", "Output Shape","Weight Shape","Bias Shape", "Param #", "FLOPS #")
    print(line_new)
    print("===========================================================================================================")
    total_params = 0
    total_output = 0
    trainable_params = 0
    flops=0
    macc=0
    for layer in summary:
        # input_shape, output_shape, trainable, nb_params
        line_new = "{:>40} {:>30}  {:>30} {:>15}  {:>15}  {:>15}".format(
            layer,
            str(summary[layer]["output_shape"]),
            str(summary[layer]["weight"] if 'weight' in summary[layer] else ''),
            str(summary[layer]["bias"] if 'bias' in summary[layer] else ''),
            "{0:,}".format(summary[layer]["nb_params"]),
            "{0:,}".format(summary[layer]["flops"][0]),
        )
        total_params += summary[layer]["nb_params"]
        flops+= float(summary[layer]["flops"][0])
        macc += float(summary[layer]["macc"][0])
        total_output += np.prod(summary[layer]["output_shape"])
        if "trainable" in summary[layer]:
            if summary[layer]["trainable"] == True:
                trainable_params += summary[layer]["nb_params"]
        print(line_new)

    # assume 4 bytes/number (float on cuda).
    total_input_size = abs(np.prod(input_size) * batch_size * 4. / (1024 ** 2.))
    total_output_size = abs(2. * total_output * 4. / (1024 ** 2.))  # x2 for gradients
    total_params_size = abs(total_params.numpy() * 4. / (1024 ** 2.))
    total_size = total_params_size + total_output_size + total_input_size

    print("================================================================")
    print("Total params: {0:,}".format(total_params))
    print("Trainable params: {0:,}".format(trainable_params))
    print("Non-trainable params: {0:,}".format(total_params - trainable_params))
    print("Total MACC: {0:,}".format(round(macc,0)))
    print("Total FLOPs: {0:.5f} GFLOPs".format(round(flops / 10.**9, 5)))
    print("----------------------------------------------------------------")
    print("Input size (MB): %0.2f" % total_input_size)
    print("Forward/backward pass size (MB): %0.2f" % total_output_size)
    print("Params size (MB): %0.2f" % total_params_size)
    print("Estimated Total Size (MB): %0.2f" % total_size)
    print("----------------------------------------------------------------")
    # return summary




def get_input_shape(x):
    input_shape=None
    if hasattr(x,'shape'):
        input_shape=getattr(x,'shape')
    elif hasattr(x,'calculated_output_shape'):
        input_shape = getattr(x, 'calculated_output_shape')
    return input_shape

def get_out_shape(x:nn.Module,input_shape):
    test_tensor = torch.Tensor(np.ones(input_shape, dtype=np.float32))

    if nn.Module is nn.Sequential or nn.Module is nn.Sequential:
        for module in x._modules.values():
            test_tensor = module(test_tensor)
        return test_tensor.shape
    else:
        test_tensor = x(test_tensor)
    calculated_output_shape = test_tensor.shape
    return calculated_output_shape






def summary_str(model):
    """ Get a string representation of model building blocks and parameter counts. """
    indent_list, name_list, count_list = [], [], []
    def module_info(m, name, indent_level):
        count_list.append(sum([np.prod(list(p.size())) for p in m.parameters()]))
        indent_list.append(indent_level)
        name_list.append(name)
        for name, child in m.named_children():
            if name.isdigit():
                name = child._get_name()
            module_info(child, name, indent_level+1)
    module_info(model, model._get_name(), 0)
    max_indent = max(indent_list)*4
    max_name = max(len(x) for x in name_list)+max_indent+2
    max_param = len(str(count_list[0]))+max_name+2
    out = ['Blocks{:>{w}}'.format('Params', w=max_param-6)]
    out += ['-'*max_param]
    for indent, name, param in zip(indent_list, name_list, count_list):
        s0 = '    '*indent
        s1 = '{:{w}}'.format(name, w=max_name-len(s0))
        s2 = '{:>{w}}'.format(param, w=max_param-len(s1)-len(s0))
        out += [s0+s1+s2]
    return '\n'.join(out)



import gc
import subprocess

import numpy as np
import pandas as pd
import torch


class ModelSummary(object):

    def __init__(self, model, mode='full'):
        '''
        Generates summaries of model layers and dimensions.
        '''
        self.model = model
        self.mode = mode
        self.in_sizes = []
        self.out_sizes = []

        self.summarize()

    def __str__(self):
        return self.summary.__str__()

    def __repr__(self):
        return self.summary.__str__()

    def named_modules(self):
        if self.mode == 'full':
            mods = self.model.named_modules()
            mods = list(mods)[1:]  # do not include root module (LightningModule)
        elif self.mode == 'top':
            # the children are the top-level modules
            mods = self.model.named_children()
        else:
            mods = []
        return list(mods)

    def get_variable_sizes(self):
        '''Run sample input through each layer to get output sizes'''
        mods = self.named_modules()
        in_sizes = []
        out_sizes = []
        input_ = self.model.example_input_array

        if self.model.on_gpu:
            input_ = input_.cuda(0)

        if self.model.trainer.use_amp:
            input_ = input_.half()

        with torch.no_grad():

            for _, m in mods:
                if type(input_) is list or type(input_) is tuple:  # pragma: no cover
                    out = m(*input_)
                else:
                    out = m(input_)

                if type(input_) is tuple or type(input_) is list:  # pragma: no cover
                    in_size = []
                    for x in input_:
                        if type(x) is list:
                            in_size.append(len(x))
                        else:
                            in_size.append(x.size())
                else:
                    in_size = np.array(input_.size())

                in_sizes.append(in_size)

                if type(out) is tuple or type(out) is list:  # pragma: no cover
                    out_size = np.asarray([x.size() for x in out])
                else:
                    out_size = np.array(out.size())

                out_sizes.append(out_size)
                input_ = out

        self.in_sizes = in_sizes
        self.out_sizes = out_sizes
        assert len(in_sizes) == len(out_sizes)
        return

    def get_layer_names(self):
        '''Collect Layer Names'''
        mods = self.named_modules()
        names = []
        layers = []
        for name, m in mods:
            names += [name]
            layers += [str(m.__class__)]

        layer_types = [x.split('.')[-1][:-2] for x in layers]

        self.layer_names = names
        self.layer_types = layer_types
        return

    def get_parameter_sizes(self):
        '''Get sizes of all parameters in `model`'''
        mods = self.named_modules()
        sizes = []
        for _, m in mods:
            p = list(m.parameters())
            modsz = []
            for j in range(len(p)):
                modsz.append(np.array(p[j].size()))
            sizes.append(modsz)

        self.param_sizes = sizes
        return

    def get_parameter_nums(self):
        '''Get number of parameters in each layer'''
        param_nums = []
        for mod in self.param_sizes:
            all_params = 0
            for p in mod:
                all_params += np.prod(p)
            param_nums.append(all_params)
        self.param_nums = param_nums
        return

    def make_summary(self):
        '''
        Makes a summary listing with:

        Layer Name, Layer Type, Input Size, Output Size, Number of Parameters
        '''

        cols = ['Name', 'Type', 'Params']
        if self.model.example_input_array is not None:
            cols.extend(['In_sizes', 'Out_sizes'])

        df = pd.DataFrame(np.zeros((len(self.layer_names), len(cols))))
        df.columns = cols

        df['Name'] = self.layer_names
        df['Type'] = self.layer_types
        df['Params'] = self.param_nums
        df['Params'] = df['Params'].map(get_human_readable_count)

        if self.model.example_input_array is not None:
            df['In_sizes'] = self.in_sizes
            df['Out_sizes'] = self.out_sizes

        self.summary = df
        return

    def summarize(self):
        self.get_layer_names()
        self.get_parameter_sizes()
        self.get_parameter_nums()

        if self.model.example_input_array is not None:
            self.get_variable_sizes()
        self.make_summary()


def print_mem_stack():  # pragma: no cover
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
                print(type(obj), obj.size())
        except Exception:
            pass


def count_mem_items():  # pragma: no cover
    nb_params = 0
    nb_tensors = 0
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
                obj_type = str(type(obj))
                if 'parameter' in obj_type:
                    nb_params += 1
                else:
                    nb_tensors += 1
        except Exception:
            pass

    return nb_params, nb_tensors


def get_memory_profile(mode):
    """
    'all' means return memory for all gpus
    'min_max' means return memory for max and min
    :param mode:
    :return:
    """
    memory_map = get_gpu_memory_map()

    if mode == 'min_max':
        min_mem = 1000000
        min_k = None
        max_mem = 0
        max_k = None
        for k, v in memory_map:
            if v > max_mem:
                max_mem = v
                max_k = k
            if v < min_mem:
                min_mem = v
                min_k = k

        memory_map = {min_k: min_mem, max_k: max_mem}

    return memory_map


def get_gpu_memory_map():
    """Get the current gpu usage.

    Returns
    -------
    usage: dict
        Keys are device ids as integers.
        Values are memory usage as integers in MB.
    """
    result = subprocess.check_output(
        [
            'nvidia-smi', '--query-gpu=memory.used',
            '--format=csv,nounits,noheader'
        ], encoding='utf-8')
    # Convert lines into a dictionary
    gpu_memory = [int(x) for x in result.strip().split('\n')]
    gpu_memory_map = {}
    for k, v in zip(range(len(gpu_memory)), gpu_memory):
        k = 'gpu_{k}'
        gpu_memory_map[k] = v
    return gpu_memory_map


def get_human_readable_count(number):
    """
    Abbreviates an integer number with K, M, B, T for thousands, millions,
    billions and trillions, respectively.
    Examples:
        123     -> 123
        1234    -> 1 K       (one thousand)
        2e6     -> 2 M       (two million)
        3e9     -> 3 B       (three billion)
        4e12    -> 4 T       (four trillion)
        5e15    -> 5,000 T
    :param number: a positive integer number
    :returns a string formatted according to the pattern described above.
    """
    assert number >= 0
    labels = [' ', 'K', 'M', 'B', 'T']
    num_digits = int(np.floor(np.log10(number)) + 1 if number > 0 else 1)
    num_groups = int(np.ceil(num_digits / 3))
    num_groups = min(num_groups, len(labels))  # don't abbreviate beyond trillions
    shift = -3 * (num_groups - 1)
    number = number * (10 ** shift)
    index = num_groups - 1
    return '{int(number):,d} {labels[index]}'











