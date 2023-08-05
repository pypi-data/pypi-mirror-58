import os
import sys
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
from IPython import display

import time
import uuid

from collections import OrderedDict
from functools import partial
import numpy as np
from ..backend.common import addindent, get_time_suffix, format_time, get_terminal_size,get_session,  snake2camel,PrintException
#from ..backend.load_backend import *


__all__ = ['progress_bar', 'OptimizerMixin']

_session=get_session()
_backend=_session.backend
if _backend=='pytorch':
    import torch
    import torch.nn as nn
    from ..backend.pytorch_backend import *
elif _backend=='tensorflow':
    import tensorflow as tf
    from ..backend.tensorflow_backend import *
elif _backend == 'cntk':
    import cntk as C
    from ..backend.cntk_backend import *

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
            try:
                loss.backward()
                self.step()
            except Exception as e:
                PrintException()
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

class LossMixin(object):
    def __init__(self,reduction='mean', loss_func=None,**kwargs):
        super( **kwargs)
        self.reduction=reduction
        self._loss_func = loss_func
        self._loss_func_kwargs = kwargs
        if _backend == 'tensorflow':
            self.fn=loss_func
            self._fn_kwargs=kwargs
    @property
    def loss_func (self):
        return self._loss_func

    @loss_func .setter
    def loss_func (self, value):
        self._loss_func =value
        if _backend == 'tensorflow':
            self.fn=value
    def __call__(self, out,target):
        """Invokes the `LossFunctionWrapper` instance.
        # Arguments
            y_true: Ground truth values.
            y_pred: The predicted values.
        # Returns
            Loss values per sample.
        """
        if self.loss_func is not None:
            return self.loss_func(out,target, **self._loss_func_kwargs)
        if _backend == 'pytorch':
            return super().forward(out,target)
        elif _backend == 'tensorflow':
            return super().call(target,out)
        elif _backend == 'cntk':
            return self.loss_func(out,target, **self._loss_func_kwargs)



class ModelMixin(object):
    def __init__(self, model, optimizer, **kwargs):
        self.model=model
        self.optimizer=optimizer
        self.optimizer_settings=kwargs
        super(model, optimizer, ** kwargs)

        self.callbacks=[]
        self.training_context = {
                                 'losses': None,  # loss_wrapper
                                 'optimizer': None,   # optimizer
                                 'stop_training': False,  # stop training
                                 'current_epoch': -1,  # current_epoch
                                 'current_batch': None, # current_batch
                                 'current_output': None,   # current output
                                 'current_loss': None,# current loss
                                 'current_metrics': None,  # current output
                                 'callbacks': self.callbacks}


        self.device =self.device()





    def reset_training_context(self):
        self.training_context = {'losses': None,  # loss_wrapper
            'optimizer': None,  # optimizer
            'stop_training': False,  # stop training
            'current_epoch': -1,  # current_epoch
            'current_batch': None,  # current_batch
            'current_output': None,  # current output
            'current_loss': None,  # current loss
            'current_metrics': None,  # current output
            'callbacks': self.callbacks}

    def summary(self):
        if _backend == 'pytorch':
            summary(self.model)
        elif  _backend == 'cntk':
            pass
        elif  _backend == 'tensorflow':
            self.model.summary()

    def get_weights(self):
        if _backend == 'pytorch':
            return self.model.parameters()
        elif _backend == 'cntk':
            return self.model.parameters
        elif _backend == 'cntk':
            return self.model.get_weights()
        else:
            return None

    def get_layer(self):
        if _backend == 'pytorch':
            return self.model.parameters()
        elif _backend == 'cntk':
            return self.model.parameters
        elif _backend == 'cntk':
            return self.model.get_weights()
        else:
            return None



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


