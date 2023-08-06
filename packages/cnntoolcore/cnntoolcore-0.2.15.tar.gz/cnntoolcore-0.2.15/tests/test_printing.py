import unittest

import torch
from torch import nn

from tests.simple_cnn import SimpleCNN, SimpleCNNWithBranching
from visualization_core.graph_extractor import GraphExtractor
from visualization_core.model.graph_model import FunctionNode
from visualization_printing.graph_printer import GraphPrinter, LinkAttacher, NodeColoringTool


class VisualizationPrintingTests(unittest.TestCase):
    def test_shoud_print_dot_graph(self):
        model = SimpleCNNWithBranching()

        test_input = torch.rand(1, 3, 32, 32)
        y = model.forward(test_input)

        graph_extractor = GraphExtractor()
        parent_node = FunctionNode(y.grad_fn.__class__.__name__)
        graph_extractor.create_graph_and_associate_with_mapping(parent_node, y.grad_fn.next_functions, model, y.grad_fn)

        link_attacher = LinkAttacher("www.google.com")
        coloring_tool = NodeColoringTool("blue" , "lightyellow")
        graph_printer = GraphPrinter(link_attacher, coloring_tool)
        dot_text = graph_printer.convert_graph_to_dot(parent_node)
        print()