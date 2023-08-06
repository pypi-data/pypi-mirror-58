import os
import sys
import matplotlib
import platform
if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
from IPython import display
import inspect
import time
import uuid
import torch
import torch.nn as nn
from collections import OrderedDict
from functools import partial
import numpy as np

import tensorflow as tf
from tensorflow.python.eager import context,tape,function
from tensorflow.python.eager.backprop import GradientTape
from tensorflow.python.keras import backend
from tensorflow.python.ops.losses import util as tf_losses_utils
from tensorflow.python.keras.utils import losses_utils
from tensorflow.python.keras.engine import training_utils
from tensorflow.python.client import device_lib
from ..backend.tensorflow_backend import *
from ..optims.tensorflow_optimizers import get_optimizer
from ..optims.tensorflow_regularizers import *
from ..optims.tensorflow_lr_schedulers import get_lr_scheduler
from ..optims.tensorflow_constraints import get_constraint
from ..optims.tensorflow_losses import *
from ..optims.tensorflow_metrics import get_metric
from ..misc.visualization_utils import tile_rgb_images,loss_metric_curve
from ..misc.callbacks import *
from .trainers import ModelBase,OptimizerMixin,progress_bar
from ..backend.common import addindent, get_time_suffix, format_time, get_terminal_size, snake2camel, PrintException,to_list,unpack_singleton,enforce_singleton

__all__ = ['Model']

_device='CPU'
for device in device_lib.list_local_devices():
      if tf.DeviceSpec.from_string(device.name).device_type == 'GPU':
          _device='GPU'
          break

def _to_tuple(x):
    if isinstance(x, tuple):
        return x
    elif isinstance(x, list):
        return tuple(x)
    else:
        return x,



class Model(ModelBase):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(Model, self).__init__(inputs, output, input_shape)

    def _initial_graph(self, inputs=None, output=None, input_shape=None):
        if output is None:
            raise ValueError('There is at least one output')

        if inputs is None:
            if input_shape is None:
                raise ValueError('You should assign inputs or input shape')
            else:
                input_shape = _to_tuple(input_shape)
                input_name = 'input_{0}'.format(len(self.inputs))
                input_var =Input(input_shape, name=input_name)
                self.inputs[input_name] = input_var
        elif isinstance(inputs,tf.keras.Input):
            self.inputs[inputs.__name__] =Input(input_shape=inputs.input_shape,name=inputs.__name__)
        elif isinstance(inputs,Input):
            input_name = inputs.name if inputs.name!='' else 'input_{0}'.format(len(self.inputs))
            input_shape=inputs.input_shape
            self.inputs[input_name] = inputs
        elif isinstance(inputs, (tuple, list)):
            for inp in inputs:
                if isinstance(inp,Input):
                    input_name = inp.name if inp.name != '' else 'input_{0}'.format(len(self.inputs))
                    self.inputs[input_name] = inp
        elif isinstance(inputs,dict):
            for k,v in inputs.items():
                if isinstance(v,tf.keras.Input):
                    self.inputs[k] =Input(input_shape=v.input_shape,name=k)

        if isinstance(output, tf.keras.layers.Layer):
            # output.call = function(output.call, autograph=True)
            # output.predict = function(output.predict, autograph=True)
            # self.model=output
            model_input=None
            if len(self.inputs)==1:
                #model_input=unpack_singleton(list(self.inputs.values()))
                self.model = output

            elif  len(self.inputs)>1:
                model_input = unpack_singleton(list(self.inputs.values()))
                output.input_spec =model_input.input_shape
                output=output(self.inputs)
                self.model = tf.keras.Model(self.inputs,output)
            elif len(self.inputs)==0:
                if output.built:
                    self.model =output
                    self.inputs[output.input.name]=Input(output.input_shape,name=output.input.name)
                else:
                    raise  ValueError('There should at least one input')
        elif isinstance(output, (list,tuple)):
            output_list=[]

            if len(self.inputs.values())==1:
                inp=list(self.inputs.values())[0]
                for op in output:
                    if isinstance(op, tf.keras.layers.Layer):
                        op1=op(inp)
                        output_list.append(op1)
                        target_name = 'target_{0}'.format(len(self.targets))
                        self.targets[target_name] = Input(op1.output.int_shape, name=target_name)
                self.model = tf.keras.Model(inp, output_list)


            else:
                self.model = tf.keras.Model(self.inputs, output)




            self.model =tf.keras.Model(inputs)
        else:
            raise ValueError('Invalid output')

        self.device = _device
        self.training_context['current_model'] = self.model
        return self

    @property
    def layers(self):
        return self.model._nodes
    #
    # def complie(self, optimizer, losses=None, metrics=None, loss_weights=None, sample_weight_mode=None,
    #             weighted_metrics=None, target_tensors=None):
    #     self.with_optimizer(optimizer)
    #     if losses is not None and isinstance(losses, (list, tuple)):
    #         for loss in losses:
    #             self.with_loss(loss)
    #     if metrics is not None and isinstance(metrics, (list, tuple)):
    #         for metric in metrics:
    #             self.with_metric(metric)
    #
    #     return self

    def with_optimizer(self, optimizer, **kwargs):
        if isinstance(optimizer, str):
            optimizer_class = get_optimizer(optimizer)
            self.optimizer = optimizer_class(**kwargs)

        else:
            self.optimizer = optimizer(**kwargs)
        # self.lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True, mode='min',
        #                                                                factor=0.5, patience=5, threshold=1e-4,
        #                                                                cooldown=0, min_lr=1e-10, eps=1e-8)
        self.base_lr = kwargs.get('lr', kwargs.get('learning_rate', 1e-3))
        self.training_context['optimizer'] = self.optimizer
        self.training_context['base_lr'] = self.base_lr
        self.training_context['current_lr'] = self.base_lr
        return self

    def with_loss(self, loss, loss_weight=1,output_idx=0,name='',**kwargs):
        if isinstance(loss, str):
            loss = get_loss(loss)
        alias=name
        if inspect.isclass(loss):
            alias=loss.__name__ if len(alias)==0 else alias
        if len(alias)==0 and hasattr(loss,'__name__') :
             alias=  loss.__name__
        with backend.name_scope(alias):
            if inspect.isclass(loss):
                #keras (y_true,y_pred)
                 self._losses[alias] =loss(**kwargs)
            elif callable(loss):
                self._losses[alias] =loss
        return self

    def with_metric(self, metric, output_idx=0,name='', **kwargs):
        if isinstance(metric, str):
            metric = get_metric(metric)
        alias = name
        if inspect.isfunction(metric):
            alias = metric.__name__ if len(alias) == 0 else alias
        if len(alias) == 0 and hasattr(metric, 'name'):
            alias = metric.name
        with backend.name_scope(alias):
            if inspect.isclass(metric):
                # keras (y_true,y_pred)
                self._metrics[alias] = metric(**kwargs)
            elif callable(metric):
                self._metrics[alias] = metric
        return self

    def with_regularizer(self, reg, **kwargs):
        if reg is None:
            return self
        reg_fn = None
        alias = None
        if isinstance(reg, str):
            reg_fn = get_reg(reg)
            alias=reg
        elif reg is callable:
            reg_fn = reg
            alias=reg_fn.__name__


        args = reg_fn.__code__.co_varnames
        if 'reg_weight' in args:
            if 'model' in args:
                self._model_regs[alias+'_Loss'] = reg_fn(self.model.get_weights(),**kwargs)

            elif 'output' in args:
                self._output_regs[alias+'_Loss'] = reg_fn( self.model.output,**kwargs)
        return self

    def with_constraint(self, constraint, **kwargs):
        if constraint is None:
            return self
        constraint_fn = None
        if isinstance(constraint, str):
            constraint_fn = get_constraint(constraint)

        if hasattr(constraint_fn, 'forward') and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = constraint_fn(**kwargs)

        elif callable(constraint_fn) and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = partial(constraint_fn, **kwargs)

        return self

    def with_learning_rate_scheduler(self, lr_schedule, warmup=0, **kwargs):
        if lr_schedule is None:
            return self
        if isinstance(lr_schedule,str):
            lr_schedule=get_lr_scheduler(lr_schedule)
        if callable(lr_schedule) :
           self.lr_scheduler= lr_schedule(self.optimizer,**kwargs)
        self.warmup = warmup
        if self.warmup > 0:
            self.optimizer.adjust_learning_rate(1e-5,False)
            self.training_context['current_lr'] =1e-5
        return self

    def adjust_learning_rate(self,lr,verbose=True):
        new_lr=lr
        old_lr=self.optimizer.lr
        self.optimizer._set_hyper('learning_rate', new_lr)
        self.training_context['current_lr']=new_lr
        if verbose:
            if verbose:
                print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr, new_lr))

    def do_on_training_start(self):
        #self.model.compile(self.optimizer,loss={**self._losses, **self._model_regs,**self._output_regs},metrics=self._metrics,loss_weights=self.loss_weights)
        tf.executing_eagerly()
        self.model.run_eagerly=True

    def do_on_training_end(self):
        pass

    def do_on_epoch_start(self):
        if self.training_context['current_epoch'] < self.warmup:
            lr = 1e-5 * (self.training_context['current_epoch'] + 1)
            self.adjust_learning_rate(lr,False)
        elif self.training_context['current_epoch'] == self.warmup:
            self.adjust_learning_rate(self.base_lr,False)


    def do_on_epoch_end(self):
        if self.training_context['current_epoch'] > self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
                self.training_context['current_lr'] = self.optimizer.lr
            if self.optimizer.lr < 1e-8:
                self.optimizer.param_groups[0]['lr'] = 0.05 * self.base_lr
                self.training_context['current_lr'] =  0.05 * self.base_lr
        elif self.training_context['current_epoch'] == self.warmup:
            self.optimizer.adjust_learning_rate(self.base_lr, True)
            self.training_context['current_lr'] =self.base_lr
        elif self.training_context['current_epoch'] < self.warmup:
            self.optimizer.adjust_learning_rate(1e-5*(self.training_context['current_epoch']+1), True)
            self.training_context['current_lr'] = 1e-5*(self.training_context['current_epoch']+1)

    def do_on_data_received(self, input=None, target=None):
        if not self.model.built:
            input_var=Input(input_shape=input.shape[1:],batch_size=input.shape[0])
            out = self.model(input_var)
            target_name = 'target_{0}'.format(len(self.targets))
            self.targets[target_name] = Input(out.shape, name=target_name)
        input=to_tensor(input)
        target=to_tensor(target)
        return input,target


    def do_preparation_for_loss(self):
        pass


    def do_post_loss_calculation(self):
        pass

    def do_gradient_update(self,log_gradients=False):
        if log_gradients:
            self.gradients_history.append(to_numpy(self.training_context['grads']))

        self.optimizer.apply_gradients(zip(self.training_context['grads'], self.model.trainable_variables))
        # loss, metrics = self.model.train_on_batch(self.training_context['current_input'], self.training_context['current_target'])
        # if self.training_context['is_collect_data']:
        #     if len(loss)==1:
        #         self.training_context['losses']['total_losses'] = loss[0]
        #         self.training_context['current_loss']= loss[0]
        #         k=list(self.losses.keys())[0]
        #         if  k not in self.training_context['losses']:
        #             self.training_context['losses'][k] = []
        #         self.training_context['losses'][k]= loss[0]
        #     else:
        #         self.training_context['losses']['total_losses'] = loss[0]
        #         self.training_context['current_loss'] = loss[0]
        #         n=1
        #         for k, v in self._losses.items():
        #             if k not in self.training_context['losses']:
        #                 self.training_context['losses'][k] = []
        #                 self.training_context['losses'][k] = loss[n]
        #                 n+=1
        #     n=0
        #     for k, v in self._metrics.items():
        #         if k not in self.training_context['metrics']:
        #             self.training_context['metrics'][k] = []
        #             self.training_context['metrics'][k] = metrics[n]
        #             n += 1



    def do_post_gradient_update(self):
        pass

    def do_on_progress_end(self):
        if self.training_context['current_epoch'] > self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
                self.training_context['current_lr'] = self.optimizer.lr

    def log_gradient(self,grads=None):
        grad_dict = {}
        for k, v in grads:
            grad_dict[k] = to_numpy(v.grad.clone())
        self.gradients_history.append(grad_dict)


    def log_weight(self,weghts=None):
        self.weights_history.append(self.model.get_weights()[0])


    def save_model(self,file_path=None):
        for callback in self.training_context['callbacks']:
            callback.on_start_save_model(self.training_context)
        self.model.eval()
        if file_path is not None:
            self.model.save(file_path)
        elif 'save_path' in self.training_context and self.training_context['save_path'] is not None:
            self.model.save(self.training_context['save_path'])

        else:
            if 'Models' is not None and len('Models') > 1 and not os.path.exists('Models'):
                try:
                    os.makedirs('Models')
                except Exception as e:
                    pass
            save_full_path = os.path.join('Models/', 'model_{0}_epoch{1}.pth'.format(self.model.__name__,self.training_context['current_epoch']))
            self.model.save(self.training_context['save_full_path'])

        self.model.train()


    def save_onnx(self, file_path):
        pass
        # import torch.onnx
        # input_names = ["input_0"]
        # output_names = ["output0"]
        # dummy_input = torch.randn(1,*self.model.input_shape.tolist(), device='cuda')
        # torch.onnx.export(self.model, dummy_input,file_path, verbose=True, input_names=input_names,
        #                   output_names=output_names)

    def train_model(self,input,target,current_epoch,current_batch,total_epoch,total_batch,is_collect_data=True,is_print_batch_progress=True,is_print_epoch_progress=True,log_gradients=False,log_weights=False,cumlative_grad=False):
        try:
            self.training_context['current_epoch'] =current_epoch
            self.training_context['current_batch'] = current_batch
            self.training_context['total_epoch'] = total_epoch
            self.training_context['total_batch'] = total_batch
            self.training_context['is_collect_data']=is_collect_data
            self.training_context['log_gradients'] = log_gradients
            self.training_context['log_weights'] = log_weights
            self.sample_collect_history.append(1 if  is_collect_data else 0)

            if self.training_context['current_batch'] == 0:
                if self.training_context['current_epoch'] == 0:
                    self.do_on_training_start()
                self.training_context['print_batch_progress_frequency'] = 1
                self.training_context['print_epoch_progress_frequency'] = 1
                self.training_context['losses'] = {}
                self.training_context['losses']['total_losses'] = []
                self.training_context['metrics'] = {}
                self.do_on_epoch_start()
                for callback in self.callbacks:
                    callback.on_epoch_start(self.training_context)
            self.do_on_batch_start()

            input, target = self.do_on_data_received(input, target)
            self.training_context['current_input'] = input
            self.training_context['current_target'] = target
            self.training_context['current_model'] = self.model

            if cumlative_grad == False:
                self.training_context['current_loss'] = 0
                self.do_preparation_for_loss()
                self.training_context['current_model'] = self.model
                self.training_context['optimizer'] = self.optimizer


            with tf.GradientTape() as tape:
                output = self.model(input)
                self.training_context['current_model'] = self.model
                self.training_context['current_output'] = output

                # losss
                for k, v in self._losses.items():
                    if k not in self.training_context['losses']:
                        self.training_context['losses'][k] = []
                    loss_weight = 1
                    if k in self.loss_weights:
                        loss_weight = self.loss_weights[k]
                    this_loss = v.call(target,output) if hasattr(v, 'forward') else v(target,output)
                    self.training_context['current_loss'] = self.training_context[ 'current_loss'] + this_loss * loss_weight
                    if is_collect_data:
                        self.training_context['losses'][k].append(this_loss.numpy() * loss_weight)

                self.do_post_loss_calculation()
                for callback in self.callbacks:
                    callback.post_loss_calculation(self.training_context)

                grads = tape.gradient(self.training_context['current_loss'] , self.model.trainable_variables)
                self.training_context['grads']=grads

                self.training_context['optimizer'] = self.optimizer
                self.do_pre_optimization_step()
                # ON_PRE_OPTIMIZATION_STEP
                for callback in self.training_context['callbacks']:
                    callback.on_optimization_step_starting(self.training_context)

                self.do_gradient_update(log_gradients and is_collect_data)
                self.training_context['optimizer'] = self.optimizer
                self.training_context['current_lr'] = self.optimizer.lr

                # ON_POSTBACKWARD_CALCULATION
                self.do_post_gradient_update()
                for callback in self.training_context['callbacks']:
                    callback.on_optimization_step_end(self.training_context)



                    #regularizer
                # for k, v in self._output_regs.items():
                #     if k + '_Loss' not in self.training_context['losses']:
                #         self.training_context['losses'][k + '_Loss'] = []
                #     this_loss = v(output)
                #     self.training_context['current_loss'] = self.training_context['current_loss']+ this_loss#self.training_context['current_loss'] + this_loss
                #     if is_collect_data:
                #         self.training_context['losses'][k + '_Loss'].append(float(to_numpy(this_loss)))
                #
                # for k, v in self._model_regs.items():
                #     if k + '_Loss' not in self.training_context['losses']:
                #         self.training_context['losses'][k + '_Loss'] = []
                #     this_loss=v(self.model)
                #     self.training_context['current_loss'] =self.training_context['current_loss']+this_loss
                #     if is_collect_data:
                #         self.training_context['losses'][k + '_Loss'].append(float(to_numpy( this_loss)))



            if is_collect_data:
                self.training_context['losses']['total_losses'].append(self.training_context['current_loss'].numpy())

            #model comfirm
            for k, v in self._constraints.items():
                v(self.model)

            if log_weights and is_collect_data:
                self.log_weight()


            output = self.model(input,training=False)
            self.training_context['current_model'] = self.model
            self.training_context['current_output'] = output

            # ON_EVALUATION_START
            self.do_on_metrics_evaluation_start()
            for callback in self.training_context['callbacks']:
                callback.on_metrics_evaluation_start(self.training_context)

            for k, v in self._metrics.items():
                if k not in self.training_context['metrics']:
                    self.training_context['metrics'][k] = []
                if is_collect_data:
                    self.training_context['metrics'][k].append(v.call(target,output).numpy() if hasattr(v, 'forward') else v( target,output).numpy())

                #ON_EVALUATION_END
                self.do_on_metrics_evaluation_end()
                for callback in self.training_context['callbacks']:
                    callback.on_metrics_evaluation_end(self.training_context)

                if is_print_batch_progress:
                    self.do_on_progress_start()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_start(self.training_context)

                    self.print_batch_progress(self.training_context['print_batch_progress_frequency'])
                    self.training_context['print_batch_progress_frequency']=1
                    self.do_on_progress_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_end(self.training_context)
                else:
                    self.training_context['print_batch_progress_frequency']+=1

                # ON_BATCH_END
                self.do_on_batch_end()
                for callback in self.training_context['callbacks']:
                    callback.on_batch_end(self.training_context)

            if self.training_context['current_batch']==self.training_context['total_batch']-1:
                #epoch end
                if self.training_context['current_epoch'] == 0:
                    self.batch_loss_history = self.training_context['losses']
                    self.batch_metric_history = self.training_context['metrics']
                    for k, v in self.training_context['losses'].items():
                        self.epoch_loss_history[k] = []
                        self.epoch_loss_history[k].append(np.array(v).mean())
                    for k, v in  self.training_context['metrics'] .items():
                        self.epoch_metric_history[k] = []
                        self.epoch_metric_history[k].append(np.array(v).mean())


                else:
                    [self.batch_loss_history[k].extend(v) for k, v in self.training_context['losses'].items()]
                    [self.batch_metric_history[k].extend(v) for k, v in  self.training_context['metrics'] .items()]
                    for k, v in self.training_context['losses'].items():
                        self.epoch_loss_history[k].append(np.array(v).mean())
                    for k, v in  self.training_context['metrics'] .items():
                        self.epoch_metric_history[k].append(np.array(v).mean())

                if is_print_epoch_progress:
                    self.do_on_progress_start()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_start(self.training_context)
                    self.print_epoch_progress(self.training_context['print_epoch_progress_frequency'])
                    self.training_context['print_epoch_progress_frequency']=1
                    self.do_on_progress_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_end(self.training_context)
                else:
                    self.training_context['print_epoch_progress_frequency']+=1

                self.training_context['loss_history']=self.epoch_loss_history
                self.training_context['metric_history']=self.epoch_metric_history
                self.do_on_epoch_end()
                for callback in self.training_context['callbacks']:
                    callback.on_epoch_end(self.training_context)

                self.training_context['current_lr'] = self.optimizer.lr
                if self.training_context['current_epoch']==self.training_context['total_epoch']-1:
                    self.do_on_training_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_training_end(self.training_context)
        except Exception:
            PrintException()

    def summary(self):
        raise self.model.summary()

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
        module_attrs = dir(self.model.__class__)
        optimizer_attrs = dir(self.optimizer.__class__)
        attrs = list(self.__dict__.keys())
        losses = list(self._losses.keys())
        metrics = list(self._metrics.keys())
        output_regs = list(self._output_regs.keys())
        model_regs = list(self._model_regs.keys())
        constraints = list(self._constraints.keys())
        keys = module_attrs +optimizer_attrs+ attrs + losses + metrics+output_regs+model_regs+constraints
        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)