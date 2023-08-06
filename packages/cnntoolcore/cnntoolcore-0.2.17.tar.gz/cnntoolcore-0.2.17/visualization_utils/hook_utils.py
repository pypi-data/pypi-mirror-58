

class HookUtils():
    @staticmethod
    def deep_hook_register(model, hook, mode = 'forward'):
        if len(model._modules) > 0:
            for module in model._modules:
                HookUtils.deep_hook_register(model._modules[module],hook)
        else:
            if mode == 'forward':
                model.register_forward_hook(hook)
            elif mode == 'backward':
                model.register_backward_hook(hook)
            else:
                raise ValueError('Wrong mode')

    @staticmethod
    def deep_hook_register_for_subtype(model, hook, module_type, mode='forward'):
        if len(model._modules) > 0:
            for module in model._modules:
                HookUtils.deep_hook_register(model._modules[module], hook)
        else:
            if issubclass(model.__class__, module_type):
                if mode == 'forward':
                    model.register_forward_hook(hook)
                elif mode == 'backward':
                    model.register_backward_hook(hook)
                else:
                    raise ValueError('Wrong mode')