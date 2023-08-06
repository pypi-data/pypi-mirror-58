from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique, PrintingMode
from visualization_utils.extractors.feature_maps_extractor import InputOutputFeatureMapsExtractor


class OutputFeatureMapsPlugin(GraphVisualizationTechnique):
    def __init__(self) -> None:
        super().__init__('output_feature_maps')

    def is_applicable_for(self, model):
        return True

    # Image tensor should be preporcessed
    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        super().get_module_visualizations_list_map(model, image_tensor,class_index_vector)

        map_extactor = InputOutputFeatureMapsExtractor(model)
        map_extactor.extract(image_tensor)

        module_input_feature_maps_map, module_output_feature_maps_map = map_extactor.get_module_input_and_output_feature_maps_map()

        return module_output_feature_maps_map

    def get_printing_mode(self):
        return PrintingMode.HEAPMAP