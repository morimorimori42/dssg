""" function for visualization of the DSSG """
from networkx.drawing import nx_pydot
import pygraphviz as pgv


def create_pgv(G, filename):
    """ takes the graph G and visualize the graph as png file using pygraphviz """
    G_pydot = nx_pydot.to_pydot(G)
    G_pgv = pgv.AGraph(G_pydot.to_string())
    for node, attr in G.nodes(data=True):
        G_pgv.get_node(node).attr['label'] = str(node)
        if attr['type'] == 'c':
            G_pgv.get_node(node).attr['shape'] = 'diamond'
            G_pgv.get_node(node).attr['style'] = 'filled'
            G_pgv.get_node(node).attr[
                'fillcolor'] = 'white'
            G_pgv.get_node(node).attr[
                'color'] = 'black'
        elif attr['type'] == 'f':
            G_pgv.get_node(node).attr['shape'] = 'ellipse'
            G_pgv.get_node(node).attr['style'] = 'filled'
            G_pgv.get_node(node).attr[
                'fillcolor'] = 'white'
            G_pgv.get_node(node).attr[
                'color'] = 'black'
            G_pgv.get_node(node).attr['parent'] = str(attr['parent'])

    for u, v, d in G.edges(data=True):
        G_pgv.get_edge(u, v).attr['label'] = d['label']
        G_pgv.get_edge(u, v).attr['fontsize'] = 10
        G_pgv.get_edge(u, v).attr['fontcolor'] = 'black'

    # G_pgv.graph_attr.update(label="Disassembly Sequence Structure Graph (DSSG)", labelloc="t", fontsize="12")
    G_pgv.layout(prog="dot")
    G_pgv.draw(f"{filename}.pdf", format="pdf")

