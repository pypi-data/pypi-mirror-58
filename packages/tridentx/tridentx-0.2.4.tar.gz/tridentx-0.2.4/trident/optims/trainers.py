import os
import sys
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
from IPython import display

import time
import uuid
import torch
import torch.nn as nn
from collections import OrderedDict
from functools import partial
import numpy as np
from ..backend.common import addindent, get_time_suffix, format_time, get_terminal_size,get_session,  snake2camel

_session=get_session()
_backend=_session.backend
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

_, term_width = get_terminal_size()
term_width = int(term_width)
TOTAL_BAR_LENGTH = 65.
last_time = time.time()
begin_time = last_time



class OptimizerMixin(object):
    def __init__(self, parameters,lr=0.01,**kwargs):
        if _backend == 'pytorch':
            kwargs['lr']=lr
            self.base_lr=lr
            super(parameters,kwargs)
        elif _backend == 'tensorflow':
            self.set_value(self.lr, lr)
            kwargs['learning_rate '] = lr
            super(kwargs)
            self.parameters=parameters
        elif _backend == 'cntk':
            kwargs['lr'] = lr
            self.base_lr = lr
            super(parameters, **kwargs)

    def adjust_learning_rate(self,new_lr,verbose=True):
        if _backend=='pytorch':
            old_lr=self.param_groups[0]['lr']
            if old_lr!=new_lr:
                self.param_groups[0]['lr'] =new_lr
                if verbose:
                    print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr,new_lr))
        elif _backend=='tensorflow':
            old_lr = self.get_value('lr')
            if old_lr != new_lr:
                self.set_value(self.lr, new_lr)
                if verbose:
                    print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr,new_lr))

        elif _backend=='cntk':
            old_lr = self.learning_rate()
            if old_lr!= new_lr:
                self.reset_learning_rate(new_lr)
                if verbose:
                    print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr,new_lr))

    @property
    def default_setting(self):
        if _backend == 'pytorch':
            return self.defaults
        elif _backend == 'tensorflow':
            return self.__dict__

    @default_setting.setter
    def default_setting(self, value):
        if _backend == 'pytorch':
            self.defaults=value
        elif _backend == 'tensorflow':
            self.__dict__.update(value)


    @property
    def optimizer(self):
        return super()

    @property
    def parameters(self):
        if _backend == 'pytorch':
            return self.param_groups
        elif _backend == 'tensorflow':
            return self.get_weights()
        elif _backend == 'cntk':
            return self.parameters

    @parameters.setter
    def parameters(self, params):
        if _backend == 'pytorch':
            self.param_groups= [{'params': list(params)}]
        elif _backend == 'tensorflow':
            self.set_weights(params)
        elif _backend == 'cntk':
            self.parameters=params

    @property
    def base_lr(self):
        return self._base_lr

    @base_lr.setter
    def base_lr(self, value):
        self._base_lr=value


    def get_gradients(self,loss):
        if _backend == 'pytorch':
            return loss.grad
        elif _backend == 'tensorflow':
            return self.get_gradients( loss,self.parameters)

    def updates(self, loss,training_context):
        for callback in training_context['callbacks']:
            callback.post_backward_calculation(training_context)

        if _backend == 'pytorch':
            loss.backward()
            self.step()
        elif _backend == 'tensorflow':
            self.get_updates(loss, self.parameters)

        for callback in training_context['callbacks']:
            callback.pre_optimization_step(training_context)


    def before_batch_train(self):
        if _backend == 'pytorch':
            self.zero_grad()
        else:
            pass

# class ModelMixin(object):
#     def __init__(self,model,optimizer:OptimizerMixin,losses,metrics):
#         if _backend == 'pytorch':
#
#
#         elif _backend == 'tensorflow':
#
#         elif _backend == 'cntk':
#

#
#
# class LossMixin(object):
#     def fly(self):
#         print 'I am flying'
#
# class Metrics(object):
#     def fly(self):
#         print 'I am flying'



def progress_bar(current, total, msg=None):
    global last_time, begin_time
    if current == 0:
        begin_time = time.time()  # Reset for new bar.
    cur_len = max(int(TOTAL_BAR_LENGTH * float(current) / total), 1)
    rest_len = int(TOTAL_BAR_LENGTH - cur_len) - 1 + cur_len
    # sys.stdout.write(' [')
    # for i in range(cur_len):
    #     sys.stdout.write('=')
    # sys.stdout.write('>')
    # for i in range(rest_len):
    #     sys.stdout.write('.')
    # sys.stdout.write(']')
    cur_time = time.time()
    step_time = cur_time - last_time
    last_time = cur_time
    tot_time = cur_time - begin_time
    L = []
    L.append('  Step: {0:<8s}'.format(format_time(step_time)))
    L.append(' | Tot: {0:<8s}'.format(format_time(tot_time)))
    if msg:
        L.append(' | ' + msg)
    msg = ''.join(L)
    sys.stdout.write(msg)
    for i in range(term_width - int(TOTAL_BAR_LENGTH) - len(msg) - 3):
        sys.stdout.write(' ')
    sys.stdout.write(' ( %d/%d )' % (current, total))
    sys.stdout.write('\n')
    sys.stdout.flush()  # # Go back to the center of the bar.  # for i in range(term_width-int(TOTAL_BAR_LENGTH/2)+2):  #     sys.stdout.write('\b')  # sys.stdout.write(' %d/%d ' % (current+1, total))  # if current < total-1:  #     sys.stdout.write('\r')  # else:  #     sys.stdout.write('\n')  # sys.stdout.flush()



class Model(object):
    def __init__(self, model: nn.Module, optimizer, **kwargs):

        self.model = model
        self.optimizer = optimizer
        self.optimizer_settings = kwargs
        self.reg = None
        self.constraint = None
        self._losses = OrderedDict()
        self._metrics = OrderedDict()
        self.base_lr = None
        self._is_optimizer_initialized = False
        self._is_optimizer_warmup = False
        self.batch_loss_history = {}
        self.batch_metric_history = {}
        self.epoch_loss_history = {}
        self.epoch_metric_history = {}
        self.weights_history = OrderedDict()
        self.gradients_history = OrderedDict()
        self.input_history = []
        self.target_history =[]

        if isinstance(self.optimizer, str):
            optimizer_class = get_optimizer(self.optimizer)
            self.optimizer = optimizer_class(self.model.parameters(), **self.optimizer_settings)
            self._is_optimizer_initialized = True
        else:
            self.optimizer = self.optimizer(self.model.parameters(), **self.optimizer_settings)
            self._is_optimizer_initialized = True

        self.base_lr = kwargs.get('lr', 1e-3)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def extra_repr(self):
        return ''

    def __str__(self):
        self.__repr__()

    def _get_name(self):
        return self.__class__.__name__

    def __repr__(self):
        # We treat the extra repr like the sub-module, one item per line
        extra_lines = []
        extra_repr = self.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
        child_lines = []
        for key, value in self.__dict__.items():
            if isinstance(value, OrderedDict):
                for subkey, subvalue in value.items():
                    mod_str = repr(subvalue)
                    mod_str = addindent(mod_str, 2)
                    child_lines.append('(' + key + '): ' + mod_str)
            else:
                mod_str = repr(value)
                mod_str = addindent(mod_str, 2)
                child_lines.append('(' + key + '): ' + mod_str)
        lines = extra_lines + child_lines

        main_str = self._get_name() + '('
        if lines:
            # simple one-liner info, which most builtin Modules will use
            if len(extra_lines) == 1 and not child_lines:
                main_str += extra_lines[0]
            else:
                main_str += '\n  ' + '\n  '.join(lines) + '\n'

        main_str += ')'
        return main_str

    def __dir__(self):
        module_attrs = dir(self.__class__)
        attrs = list(self.__dict__.keys())

        losses = list(self._losses.keys())
        metrics = list(self._metrics.keys())
        keys = module_attrs + attrs + losses + metrics

        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)

    def is_optimizer_initialized(self):
        return self._is_optimizer_initialized

    def update_optimizer(self):
        if isinstance(self.optimizer, str):
            optimizer_class = get_optimizer(self.optimizer)
            self.optimizer = optimizer_class(self.model.parameters(), **self.optimizer_settings)
            self._is_optimizer_initialized = True
        else:
            self.optimizer = self.optimizer(self.model.parameters(), **self.optimizer_settings)
            self._is_optimizer_initialized = True
        if self._is_optimizer_warmup == True:
            self.optimizer.param_groups[0]['lr'] = 1e-5

    def with_loss(self, loss, **kwargs):
        if hasattr(loss, 'forward'):
            self._losses[loss.__name__] = loss(**kwargs)
            if hasattr(self._losses[loss.__name__], 'reduction'):
                setattr(self._losses[loss.__name__], 'reduction', 'mean')
        elif callable(loss):
            self._losses[loss.__name__] = partial(loss, **kwargs)
        return self

    def with_metrics(self, metrics, **kwargs):
        if hasattr(metrics, 'forward'):
            self._metrics[metrics.__name__] = metrics(**kwargs)
            if hasattr(self._metrics[metrics.__name__], 'reduction'):
                setattr(self._metrics[metrics.__name__], 'reduction', 'mean')
        elif callable(metrics):
            self._metrics[metrics.__name__] = partial(metrics, **kwargs)
        return self

    def with_regularizers(self, reg, **kwargs):
        if reg is None:
            self.reg = None
        elif isinstance(reg, str):
            reg_fn = get_reg(reg)
            self.reg = partial(reg_fn, **kwargs)
        else:
            reg_fn = reg
            self.reg = partial(reg_fn, **kwargs)
        return self

    def with_constraints(self, constraint, **kwargs):
        if constraint is None:
            self.constraint = partial(min_max_norm, max_value=3, min_value=-3)
        elif isinstance(constraint, str):
            constraint_fn = get_constraints(constraint)
            self.constraint = partial(constraint_fn, **kwargs)
        else:
            constraint_fn = constraint
            self.constraint = partial(constraint_fn, **kwargs)
        return self


