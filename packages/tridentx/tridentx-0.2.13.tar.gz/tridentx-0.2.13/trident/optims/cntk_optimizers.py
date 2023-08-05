import os
import sys
import time
import itertools as it
from shutil import copyfile
import uuid
import math
import cntk as C
from cntk import cntk_py, NDArrayView, asarray
from cntk.internal import typemap
import  cntk.learners as optim
from collections import OrderedDict,defaultdict
from functools import partial
import numpy as np
from ..backend.common import get_session,addindent,get_time_suffix,get_class,format_time,get_terminal_size,snake2camel,camel2snake
from ..backend.cntk_backend import *
from .trainers import OptimizerMixin

__all__ = ['Adam','SGD','get_optimizer']

class Adam(C.learners.Learner,OptimizerMixin):
    pass
class SGD(C.learners.Learner,OptimizerMixin):
    pass




def get_optimizer(optimizer_name):
    if optimizer_name is None:
        return None
    optimizer_modules = ['trident.optims.cntk_optimizers','cntk.learners']
    try:
        optimizer_class = get_class(snake2camel(optimizer_name), optimizer_modules)
    except Exception :
        optimizer_class = get_class(optimizer_name, optimizer_modules)
    return optimizer_class
