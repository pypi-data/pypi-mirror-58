

class GraphPrinter():

    def __init__(self, link_attacher, coloring_tool) -> None:
        super().__init__()
        self.link_attacher = link_attacher
        self.coloring_tool = coloring_tool

    #
    #
    #
    def convert_graph_to_dot(self, root_node):
        graph_nodes = []
        graph_edges = []
        self.extract_nodes_and_edges(root_node, graph_nodes, graph_edges)

        return "digraph G {\n" + '\n'.join(graph_nodes) + '\n' + '\n'.join(graph_edges) + '}'


    def extract_nodes_and_edges(self, root_node, graph_nodes, graph_edges):

        #target="_parent" to make links leave iframe
        graph_nodes.append(str(root_node.id) + ' [href="' + self.link_attacher.get_sublink(root_node) + '", ' + 'label="' + root_node.function_name + '",' + self.coloring_tool.dot_color_attributes(root_node) + ' target="_parent"]' )

        for child in root_node.child_nodes:
            edge = str(child.id) + "->" + str(root_node.id)

            #Preventing redundante edges
            if edge not in graph_edges:
                graph_edges.append(str(child.id) + "->" + str(root_node.id))
            self.extract_nodes_and_edges(child, graph_nodes, graph_edges)


#
#   Gets base url and creates subpage links for given nodes by ids
#
class LinkAttacher():
    def __init__(self, link_base_url) -> None:
        super().__init__()
        self.link_base_url = link_base_url

    def get_sublink(self, node):
        if node.associated_module != None:
            return self.link_base_url + "/" + str(node.id)
        else:
            return ""


#
#   Checks if node should be colored
#   !!!! Node should already have assigned modules
#
class NodeColoringTool():
    def __init__(self, color, fillcolor=None) -> None:
        super().__init__()
        self.color = color
        self.fillcolor = fillcolor

    def dot_color_attributes(self, node):
        if node.associated_module != None:
            fill_part = ""
            if self.fillcolor != None:
                fill_part = ' style=filled, ' + 'fillcolor="' + self.fillcolor + '", '

            return 'color="' + self.color + '",' + fill_part
        else:
            return ''
