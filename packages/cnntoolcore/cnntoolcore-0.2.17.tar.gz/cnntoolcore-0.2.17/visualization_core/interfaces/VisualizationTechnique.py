from enum import Enum


class VisualizationTechnique():

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    # Checks if loaded torch_model_loading can be put into this technique
    # By convention torch_model_loading should be pretrained and ready for the visualization task
    def is_applicable_for(self, model):
        return True

    def get_printing_mode(self):
        return PrintingMode.NORMAL


class PrintingMode(Enum):
    NORMAL = 0
    HEAPMAP = 1

class GraphVisualizationTechnique(VisualizationTechnique):
    def __init__(self, name) -> None:
        super().__init__(name)

    # Visualizations which can be connected with graph nodes
    def get_module_visualizations_list_map(self, model, image_tensor, class_index_vector):
        pass


class NonGraphVisualizationTechnique(VisualizationTechnique):
    def __init__(self, name) -> None:
        super().__init__(name)

    # Visulaizations not connected with graph nodes
    def get_additional_visualizations_maps(self, model, image_tensor, class_index_vector):
        pass
