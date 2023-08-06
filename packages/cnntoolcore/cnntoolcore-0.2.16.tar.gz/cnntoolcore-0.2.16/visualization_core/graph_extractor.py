from visualization_core.graph_utils import GraphUtils
from visualization_core.model.graph_model import FunctionNode


#
#   This class got functions to return node graph and mapping to modules
#
class GraphExtractor():

    #
    #   Returns function node with full structure and associated with modules
    #
    #   Side effect: enriches root_node with tree structure
    #
    def create_graph_and_associate_with_mapping(self, root_node, next_functions, model, grad_fn):
        self.extract_gradient_functions_graph(root_node, next_functions)

        if self.is_node_structure_without_branching(root_node):
            map = self.map_modules_with_nodes_without_branching(root_node, model, grad_fn)
        else:
            module_list = []
            GraphUtils.flatten_modules(model, module_list)
            function_nodes_list = []
            GraphUtils.flatten_function_nodes(root_node, function_nodes_list)
            map = self.map_function_nodes_to_modules_by_variables(module_list, function_nodes_list)

        for function_node in map.keys():
            function_node.associated_module = map[function_node]

        node_list = []
        GraphUtils.flatten_function_nodes(root_node, node_list)

        return root_node

    #   Gets gradient next_functions of output node
    #   Gets parent_function node to new graph structure
    #   Gets dictonary that stores backward functions to make common paths
    #
    #   Sample call requires parent
    #       parent_node = FunctionNode(y.grad_fn.__class__.__name__)
    #       get_gradients(parent_node, y.grad_fn.next_functions)
    #
    #   Outs : None
    #   Side effect: parent node gets enriched with graph structure
    def extract_gradient_functions_graph(self, parent_node, next_functions, backwards_function_node_map={}):
        for next_function in next_functions:
            function_object = next_function[0]
            if function_object.__class__.__name__ == 'AccumulateGrad':
                parent_node.add_variable(function_object.variable)
            elif function_object.__class__.__name__ == 'TBackward':
                parent_node.add_variable(function_object.next_functions[0][0].variable)
            else:
                if function_object != None:
                    if function_object not in backwards_function_node_map:
                        function_node = FunctionNode(
                            self.extract_function_name_from_classname(function_object.__class__.__name__))
                        backwards_function_node_map[function_object] = function_node
                    else:
                        function_node = backwards_function_node_map[function_object]

                    parent_node.add_child(function_node)
                    self.extract_gradient_functions_graph(function_node, function_object.next_functions,
                                                          backwards_function_node_map)

    def extract_function_name_from_classname(self, classname):
        return classname.split('Backward')[0]

    #   Gets flattened module list
    #   Get flattened list of function nodes
    #
    #   Associates node with module but only these with parameters
    #
    #   Sample call
    #         module_list = []
    #         flatten_modules(torch_model_loading, module_list)
    #         function_nodes_list = []
    #         flatten_function_nodes(parent_node, function_nodes_list)
    #
    #         function_nodes_to_modules_map = map_function_nodes_to_modules_by_variables(module_list, function_nodes_list)
    #
    #   Returns:    Map mapping function node to module
    #
    def map_function_nodes_to_modules_by_variables(self, module_list, function_nodes_list):
        module_parameters_map = {mod: set(mod._parameters.values()) for mod in module_list}
        function_nodes_parameters_map = {node: set(node.variables) for node in function_nodes_list}

        function_node_modules_map = {}

        for node in function_nodes_parameters_map:
            if len(function_nodes_parameters_map[node]) > 0:
                function_node_modules_map[node] = \
                    [m for m in module_parameters_map if
                     function_nodes_parameters_map[node] == module_parameters_map[m]][0]

        return function_node_modules_map

    #
    #   Since the torch_model_loading is linear without branching both variable maping and name mapping can be used
    #   The preffered one should be named mappping with variables
    def map_modules_with_nodes_without_branching(self, parent_node, model, grad_fn):
        function_nodes_list = []
        GraphUtils.flatten_function_nodes(parent_node, function_nodes_list)

        if self.is_node_structure_without_branching(parent_node):
            module_list = []
            GraphUtils.flatten_modules(model, module_list)

            reversed_module_list = list(reversed(module_list))

            function_node_modules_by_variable_map = self.map_function_nodes_to_modules_by_variables(
                reversed_module_list,
                function_nodes_list)

            for node in function_node_modules_by_variable_map.keys():
                reversed_module_list.remove(function_node_modules_by_variable_map[node])
                function_nodes_list.remove(node)

            function_node_modules_by_name_map = self.map_function_nodes_to_modules_by_name_without_branching(
                reversed_module_list, function_nodes_list)

            return self.merge_map_overriding_with_first_map_on_conficts(function_node_modules_by_variable_map,
                                                                        function_node_modules_by_name_map)

        else:
            raise ValueError("Model should be without branching!")

    def map_function_nodes_to_modules_by_name_without_branching(self, module_list, function_nodes_list):
        function_node_modules_map = {}

        for module in module_list:
            for node in function_nodes_list:
                if node.function_name.lower().__contains__(
                        module.__class__.__name__.lower()) and node.associated_module == None:
                    node.associated_module = module
                    function_node_modules_map[node] = module
                    break

        return function_node_modules_map

    def is_node_structure_with_branching(self, parent_node):
        if len(parent_node.child_nodes) == 0:
            return False
        if len(parent_node.child_nodes) > 1:
            return True

        return self.is_node_structure_with_branching(parent_node.child_nodes[0])

    def is_node_structure_without_branching(self, parent_node):
        return not self.is_node_structure_with_branching(parent_node)

    def merge_map_overriding_with_first_map_on_conficts(self, first_map, second_map):
        map = {}

        for key in second_map.keys():
            map[key] = second_map[key]
        for key in first_map.keys():
            map[key] = first_map[key]

        return map
