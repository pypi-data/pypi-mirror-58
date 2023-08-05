import os
import sys
import matplotlib
matplotlib.use('TKAgg')
from IPython import display

import time
import uuid
import cntk as C
from collections import OrderedDict
from functools import partial
import numpy as np
from ..backend.common import addindent, get_time_suffix, format_time, get_terminal_size, snake2camel
from ..backend.cntk_backend import *
from ..optims.cntk_optimizers import *
#from ..optims.cntk_regularizers import *
from ..layers.cntk_constraints import *
from ..misc.visualization_utils import tile_rgb_images,loss_metric_curve
from ..misc.callbacks import *

__all__ = ['progress_bar', 'Model']

_, term_width = get_terminal_size()
term_width = int(term_width)
TOTAL_BAR_LENGTH = 65.
last_time = time.time()
begin_time = last_time


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
    def __init__(self, model: C.Function, optimizer, **kwargs):

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
