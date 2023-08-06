from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique
from visualization_utils.extractors.filters_extractor import FilterExtractor
from visualization_utils.extractors.gradient_extractor import GradientExtractor


class FiltersPlugin(GraphVisualizationTechnique):
    def __init__(self) -> None:
        super().__init__('filters')

    def is_applicable_for(self, model):
        return True

    # Image tensor should be preporcessed
    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        super().get_module_visualizations_list_map(model, image_tensor,class_index_vector)

        filters_extactor = FilterExtractor(model)
        filters_extactor.extract()

        filter_map = filters_extactor.get_module_filters_map()

        return filter_map
