from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six

from .load_backend import *
from .load_backend import get_backend,get_image_backend,PrintException
from .load_backend import  get_session , get_trident_dir , epsilon , set_epsilon , floatx , set_floatx , camel2snake , snake2camel , addindent , format_time , get_time_suffix , get_function , get_class , get_terminal_size , gcd , get_divisors , isprime , next_prime , prev_prime , nearest_prime
from .load_backend import  Identity , Sigmoid , Tanh , Relu , Relu6 , LeakyRelu , LeakyRelu6 , SmoothRelu , PRelu , Swish , Elu , HardSigmoid , HardSwish , Selu , LecunTanh , SoftSign , SoftPlus , HardTanh , Logit , LogLog , Mish , Softmax, identity , sigmoid , tanh , relu , relu6 , leaky_relu , leaky_relu6 , smooth_relu , p_relu , swish , elu , hard_sigmoid , hard_swish , selu , lecun_tanh , soft_sign , soft_plus , hard_tanh , logit , log_log , mish , softmax, get_activation


from .load_backend import to_numpy,to_tensor

from .load_backend import tile_rgb_images,loss_metric_curve,steps_histogram
from .load_backend import get_faces,crop_faces
from .load_backend import AbstractCallback, StoppingCriterionCallback, EarlyStoppingCriterionCallback, NumberOfEpochsStoppingCriterionCallback
from .load_backend import accuracy,psnr,mean_absolute_error,mean_squared_error,mean_squared_logarithmic_error,mae,mse,rmse,msle,get_metrics
from .load_backend import max_norm, non_neg, unit_norm, min_max_norm, maxnorm, nonneg, unitnorm, minmaxnorm, get_constraints
from .load_backend import read_image,read_mask,save_image,save_mask,image2array,array2image,mask2array,array2mask,list_pictures,normalize,resize,add_noise,backend_adaptive,random_channel_shift,random_cutout
from .load_backend import l1_reg, l2_reg, orth_reg, get_reg
from .load_backend import  Adam , SGD , Adadelta , Adagrad , RMSprop , RAdam , PlainRAdam , AdamW , Lookahead,get_optimizer

from ..layers import *
from ..data import *
from ..data import ImageReader,ImageThread
from ..optims import *

if get_backend()=='pytorch':

    from .pytorch_ops import reduce_min,reduce_max,reduce_mean,reduce_sum,argmax,expand_dims,meshgrid,element_cosine_distance
    from .pytorch_backend import to_numpy,to_tensor,print_network,plot_tensor_grid,summary,calculate_flops,Modulex,Sequential,Input,get_device,load
    from .load_backend import BertGELU, GPTGELU, bert_gelu, gpt_gelu,total_variation_norm_reg

    from .load_backend import TrainingItem, TrainingPlan,summary

    from .load_backend import adjust_learning_rate, reduce_lr_on_plateau
    from .load_backend import InstanceNorm2d, BatchNorm,BatchNorm2d, BatchNorm3d, GroupNorm2d, LayerNorm2d, get_normalization
    from .load_backend import MSELoss, CrossEntropyLoss, make_onehot, MS_SSIM, CrossEntropyLabelSmooth, \
        mixup_criterion, DiceLoss, FocalLoss, SoftIoULoss, LovaszSoftmax, TripletLoss, CenterLoss, make_onehot, \
        mixup_data,PerceptionLoss
    from .load_backend import Dense,Concatenate, Modulex, Input, Flatten, Conv1d, Conv2d, Conv3d, TransConv1d, TransConv2d, \
        TransConv3d, SeparableConv2d, GcdConv2d, GcdConv2d_1,  Lambda, Reshape, CoordConv2d, Sequential, \
        UpsamplingBilinear2d, Droupout, AlphaDroupout,SelfAttention

    from .load_backend import Ranger
    from .load_backend import mixup_data, cutout
    from .load_backend import Conv2d_Block, TransConv2d_Block, GcdConv2d_Block_1, GcdConv2d_Block, ShortCut2d, \
        Classifier1d

elif get_backend()=='tensorflow':
    from .tensorflow_backend import to_numpy, to_tensor
    from .load_backend import register_keras_custom_object


