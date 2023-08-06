import torch
from torch.nn import Linear, AvgPool2d, AdaptiveAvgPool2d

from visualization_core import GraphUtils
from visualization_core.interfaces.VisualizationTechnique import PrintingMode,NonGraphVisualizationTechnique
from visualization_utils.extractors.feature_maps_extractor import InputOutputFeatureMapsExtractor


class ClassActivationMapPlugin(NonGraphVisualizationTechnique):
    def __init__(self) -> None:
        super().__init__('class_activation_map')

    def get_printing_mode(self):
        return PrintingMode.HEAPMAP

    def get_additional_visualizations_maps(self, model, image_tensor, class_index_vector):
        module_list = []
        GraphUtils.flatten_modules(model,module_list)
        linear_layer = self.get_last_linear_layer(module_list)
        class_index = torch.argmax(class_index_vector).item()

        avg_adaptive_pool_index = module_list.index([mod for mod in module_list if isinstance(mod,AdaptiveAvgPool2d)][0])
        last_feature_maps = self.get_module_out_maps(model,image_tensor)[module_list[avg_adaptive_pool_index-1]]
        class_weight_vector = self.get_weight_vector_for_class(linear_layer,class_index)

        out_map = torch.zeros_like(last_feature_maps[0])
        for i in range(len(last_feature_maps)):
            out_map = torch.add(out_map, torch.mul(last_feature_maps[i], class_weight_vector[i]))

        return [out_map]


    def get_last_linear_layer(self,module_list):
        module_list_cpy = module_list.copy()
        module_list_cpy.reverse()
        return [mod for mod in module_list_cpy if isinstance(mod, Linear)][0]

    def get_module_out_maps(self,model,image_tensor):
        extractor = InputOutputFeatureMapsExtractor(model)
        extractor.extract(image_tensor)
        mod_in_maps, mod_out_maps = extractor.get_module_input_and_output_feature_maps_map()
        return mod_out_maps

    def get_weight_vector_for_class(self,linear_layer, class_index):
        # 0dim = out_classes; 1dim=maps_index
        return linear_layer._parameters['weight'][class_index][:]