import random
import unittest

import torch

from tests.simple_cnn import SimpleCNN
from visualization_core.graph_utils import GraphUtils
from visualization_core.graph_extractor import GraphExtractor
from visualization_core.graph_visualization_attacher import GraphVisualizationAttacher
from visualization_core.model.graph_model import FunctionNode, VisualizationMaps




class GraphModelTests(unittest.TestCase):
    def test_should_extract_graph_with_associations(self):
        model = SimpleCNN()
        test_input = torch.rand(1, 3, 32, 32)
        y = model.forward(test_input)

        graph_extractor = GraphExtractor()
        parent_node = FunctionNode(y.grad_fn.__class__.__name__)
        graph_extractor.create_graph_and_associate_with_mapping(parent_node,y.grad_fn.next_functions,model,y.grad_fn)
        print()


    def test_should_attach_visualization_maps(self):
        model = SimpleCNN()
        test_input = torch.rand(1, 3, 32, 32)
        y = model.forward(test_input)

        graph_extractor = GraphExtractor()
        parent_node = FunctionNode(y.grad_fn.__class__.__name__)
        graph_extractor.create_graph_and_associate_with_mapping(parent_node, y.grad_fn.next_functions, model, y.grad_fn)

        flattened_nodes_list = []
        GraphUtils.flatten_function_nodes(parent_node, flattened_nodes_list)

        nodes_with_modules_list = [node for node in flattened_nodes_list if node.associated_module != None]

        num_samples = 2
        nodes_sample = []
        indecies = list(range(len(nodes_with_modules_list)))
        random.shuffle(indecies)
        indecies = indecies[:num_samples]

        for i in range(num_samples):
            nodes_sample.append(nodes_with_modules_list[indecies[i]])

        module_visualizations_map = {}
        for node in nodes_sample:
            module_visualizations_map[node.associated_module] = VisualizationMaps('my-visualization')

        GraphVisualizationAttacher.attach_visualizations_to_graph(parent_node,module_visualizations_map)

        self.assertEquals(num_samples, len([node for node in flattened_nodes_list if len(node.get_visualization_maps())>0]))

def sample_gen(n, forbid):
    state = dict()
    track = dict()
    for (i, o) in enumerate(forbid):
        x = track.get(o, o)
        t = state.get(n - i - 1, n - i - 1)
        state[x] = t
        track[t] = x
        state.pop(n - i - 1, None)
        track.pop(o, None)
    del track
    for remaining in range(n - len(forbid), 0, -1):
        i = random.randrange(remaining)
        yield state.get(i, i)
        state[i] = state.get(remaining - 1, remaining - 1)
        state.pop(remaining - 1, None)
