
#Extracted from backwards pass
from visualization_core.id_generator import get_id_generator


class FunctionNode():

    def __init__(self, name) -> None:
        super().__init__()
        self.id = get_id_generator().get_id()
        self.function_name = name
        self.child_nodes = []
        self.associated_module = None

        #Used for variable mapping
        self.variables = []

        #   List of VizualizationMaps Object
        self.visualization_maps = []


    def add_child(self, child):
        if not child in self.child_nodes:
            self.child_nodes.append(child)

    def add_variable(self, var):
        self.variables.append(var)

    def add_visualization_maps(self, maps):
        self.visualization_maps.append(maps)

    def get_visualization_maps(self):
        return self.visualization_maps

# Contains list of maps for given visualization
class VisualizationMaps():

    def __init__(self,group_name):
        self.group_name = group_name
        self.map_list= []

    def set_map_list(self, map_list):
        self.map_list = map_list

    def add_map(self,map):
        self.map_list.append(map)

    def get_map_list(self):
        return self.map_list

#Stores single map
# class SingleVisualizartionMap():
#     def __init__(self, map):
#         self.map = map


class NonGraphVisualizationMapsContainer():
    def __init__(self):
        self.group_name_visualizations_maps_map = {}

    def set_visualizations_maps(self, group_name, visualizations_maps):
        self.group_name_visualizations_maps_map[group_name] = visualizations_maps

    def set_visualizations_maps_for_group(self, group_name):
        return self.group_name_visualizations_maps_map[group_name]

    def get_visualization_maps(self, group_name):
        return self.group_name_visualizations_maps_map[group_name]