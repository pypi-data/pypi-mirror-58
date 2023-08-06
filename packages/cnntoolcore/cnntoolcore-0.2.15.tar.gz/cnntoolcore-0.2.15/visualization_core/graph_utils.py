class GraphUtils():
    @staticmethod
    def flatten_function_nodes(function_node, function_node_list):
        if function_node not in function_node_list:
            function_node_list.append(function_node)
        for node in function_node.child_nodes:
            GraphUtils.flatten_function_nodes(node, function_node_list)

    # Sample call where torch_model_loading is pytorch torch_model_loading
    # module_list = []
    # self.flatten_modules(mode l, module_list)
    @staticmethod
    def flatten_modules(module, module_list):
        if len(module._modules) > 0:
            for mod in module._modules:
                GraphUtils.flatten_modules(module._modules[mod], module_list)
        else:
            module_list.append(module)


    @staticmethod
    def find_node_by_id(parent_node,id):
        nodes = []
        GraphUtils.flatten_function_nodes(parent_node, nodes)
        return [x for x in nodes if x.id == int(id)][0]

    @staticmethod
    def deep_freezing(model):
        if len(model._modules) > 0:
            for module in model._modules:
                GraphUtils.deep_freezing(model._modules[module])
        else:
            for param in model._parameters:
                model._parameters[param].requires_grad = False
