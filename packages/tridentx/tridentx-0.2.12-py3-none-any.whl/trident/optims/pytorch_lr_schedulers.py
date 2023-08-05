import math
import torch
from torch import nn
from torch.optim.lr_scheduler import _LRScheduler,ReduceLROnPlateau
from torch.optim.optimizer import  Optimizer
import numpy as np

__all__ = ['adjust_learning_rate','reduce_lr_on_plateau','CyclicScheduler']


def warmup_lr_scheduler(func):
    def wrapper(*args, **kwargs):
        x = args[0]
        w = args[1]
        if x.ndim == 3:
            w = np.flipud(w)
            w = np.transpose(w, (1, 2, 0))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 2, 1))
        elif x.ndim == 4:
            w = np.fliplr(np.flipud(w))
            w = np.transpose(w, (2, 3, 0, 1))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 3, 1, 2))
        else:
            w = np.flip(np.fliplr(np.flipud(w)), axis=2)
            w = np.transpose(w, (3, 4, 0, 1, 2))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 4, 1, 2, 3))
        dilation_rate = kwargs.pop('dilation_rate', 1)
        if isinstance(dilation_rate, int):
            dilation_rate = (dilation_rate,) * (x.ndim - 2)
        for (i, d) in enumerate(dilation_rate):
            if d > 1:
                for j in range(w.shape[2 + i] - 1):
                    w = np.insert(w, 2 * j + 1, 0, axis=2 + i)
        y = func(x, w, **kwargs)
        if kwargs['data_format'] == 'channels_last':
            if y.ndim == 3:
                y = np.transpose(y, (0, 2, 1))
            elif y.ndim == 4:
                y = np.transpose(y, (0, 2, 3, 1))
            else:
                y = np.transpose(y, (0, 2, 3, 4, 1))
        return y
    return wrapper



def _set_params(optimizer: Optimizer, **params) -> Optimizer:
    """Change an ``optimizer``'s parameters by the ones passed in ``params``."""
    for name, value in params.items():
        for param_group in optimizer.param_groups:
            param_group[name] = value
    return optimizer

# def adjust_learning_rate(optimizer, epoch, base_lr=0.001,warmup=1,milestones=None):
#     """Sets the learning rate: milestone is a list/tuple"""
#     def to(epoch):
#         if epoch <= warmup:
#             return 1
#         elif warmup < epoch <= milestones[0]:
#             return 0
#         for i in range(1, len(milestones)):
#             if milestones[i - 1] < epoch <= milestones[i]:
#                 return i
#         return len(milestones)
#     n = to(epoch)
#     global lr
#     lr =base_lr * (0.2 ** n)
#     for param_group in optimizer.param_groups:
#         param_group['lr'] = lr

def adjust_learning_rate(optimizer,base_lr=0.001, current_epoch=0,num_epochs=3, power=0.8,warmup=5,verbose=True):
    """Sets the learning rate: milestone is a list/tuple"""

    # def lr_poly(base_lr, iter, max_iter, power):
    #     return base_lr * ((1 - float(iter) / max_iter) ** (power))
    def lr_poly(base_lr, iter, max_iter, power):
        return base_lr * pow(power,max(float(iter)-1,0))
    if current_epoch<warmup:
        lr=1e-5*(current_epoch+1)
    else:
        lr = lr_poly(base_lr, current_epoch, num_epochs, power)
    if verbose==True:
        print('learning rate : {0:.4e}'.format(lr))
    #optimizer.param_groups[0]['lr'] = lr
    _set_params(optimizer, lr= lr)

    return lr

#warmup_lr_scheduler
def reduce_lr_on_plateau(optimizer,base_lr=0.001, current_epoch=0,num_epochs=3, mode='min', factor=0.5, patience=5,threshold=1e-4, warmup=5,verbose=True):
    """Sets the learning rate: milestone is a list/tuple"""
    scheduler = ReduceLROnPlateau(optimizer, mode=mode, factor=factor, patience=patience, verbose=verbose, threshold=threshold,threshold_mode='rel', cooldown=0, min_lr=1e-9, eps=1e-8)
    if current_epoch<warmup:
        lr=1e-5*(current_epoch+1)
        _set_params(optimizer, lr=lr)
    else:
        if  current_epoch==warmup:
            _set_params(optimizer, lr=base_lr)
        lr =scheduler.step()
    if verbose==True:
        print('learning rate : {0:.4e}'.format(lr))
    #optimizer.param_groups[0]['lr'] = lr


    return lr





class CyclicScheduler(_LRScheduler):
    def __init__(self, optimizer, epochs, min_lr_factor=0.05, max_lr=1.0):
        half_epochs = epochs // 2
        decay_epochs = epochs * 0.05

        lr_grow = np.linspace(min_lr_factor, max_lr, half_epochs)
        lr_down = np.linspace(max_lr, min_lr_factor, half_epochs - decay_epochs)
        lr_decay = np.linspace(min_lr_factor, min_lr_factor * 0.01, decay_epochs)
        self.learning_rates = np.concatenate((lr_grow, lr_down, lr_decay)) / max_lr
        super().__init__(optimizer)

    def get_lr(self):
        return [
            base_lr * self.learning_rates[self.last_epoch] for base_lr in self.base_lrs
        ]
