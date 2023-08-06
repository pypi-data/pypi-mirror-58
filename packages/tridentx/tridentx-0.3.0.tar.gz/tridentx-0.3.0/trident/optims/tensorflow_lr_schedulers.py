from ..backend.common import get_function,get_class,snake2camel

__all__ = ['get_lr_scheduler']


def get_lr_scheduler(lr_scheduler_name):
    if lr_scheduler_name is None:
        return None
    lr_scheduler_modules = ['trident.optims.tensorflow_lr_schedulers','tensorflow.python.keras.optimizers']
    lr_scheduler_fn=None
    if isinstance(lr_scheduler_name,str):
        if lr_scheduler_name in __all__:
            lr_scheduler_fn=get_function(lr_scheduler_name,lr_scheduler_modules)
    else:
        try:
            lr_scheduler_fn = get_function(lr_scheduler_name, lr_scheduler_modules)
        except Exception :
            lr_scheduler_fn = get_function(snake2camel(lr_scheduler_name), lr_scheduler_modules)
    return lr_scheduler_fn


