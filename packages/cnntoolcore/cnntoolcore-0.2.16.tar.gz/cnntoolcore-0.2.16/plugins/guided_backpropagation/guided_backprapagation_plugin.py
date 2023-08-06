import torch
from torch.nn import ReLU

from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique
from visualization_utils.conversion_utils import ConversionUtils
from visualization_utils.hook_utils import HookUtils


class GuidedBackpropagationPlugin(GraphVisualizationTechnique):

    def __init__(self) -> None:
        super().__init__('guided_backpropagation')
        self.module_forward_relu_outputs = {}
        self.module_grad_outputs = {}

    def backward_hook(self, module, grad_in, grad_out):
        if isinstance(module, ReLU):
            output = torch.mul(torch.clamp(grad_in[0], min=0.0),
                               self.gt_zero_value_replace(self.module_forward_relu_outputs[module], on_gt_zero=1))

            self.module_grad_outputs[module] = ConversionUtils.convert_3d_map_to_list_of_2d_maps(output[0])
            return output

        self.module_grad_outputs[module] = ConversionUtils.convert_3d_map_to_list_of_2d_maps(grad_in[0][0])


    def relu_forward_hook_function(self,module, ten_in, ten_out):
        if isinstance(module, ReLU):
            self.module_forward_relu_outputs[module] = ten_out

    def gt_zero_value_replace(self, tensor, on_gt_zero):
        res = tensor.clone()
        res[tensor > 0] = on_gt_zero
        return res


    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        HookUtils.deep_hook_register_for_subtype(model,self.relu_forward_hook_function, ReLU, 'forward')
        HookUtils.deep_hook_register_for_subtype(model,self.backward_hook, ReLU, 'backward')

        model_output = model.forward(image_tensor)
        model.zero_grad()
        model_output.backward(gradient=class_index_vector)
        return self.module_grad_outputs



