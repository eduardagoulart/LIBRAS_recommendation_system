import igraph
import networkx as nx
import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go



class GraphGenerator:
    @staticmethod
    def generate():
        initial_graph = nx.Graph()
        edges = nx.read_edgelist('graph/edges.txt')
        nodes = nx.read_adjlist('graph/nodes.txt')
        file = open('graph/weight.txt', 'r')
        file = file.read().split("\n")
        file = [tuple(i.split(" ")) for i in file]
        weight = nx.read_weighted_edgelist('graph/weight.txt')

        for i in range(0, len(file)):
            try:
                initial_graph.add_weighted_edges_from(file[i], file[i + 1])
            except:
                break
        # initial_graph.add_edges_from(edges.edges)
        initial_graph.add_nodes_from(nodes)
        print(initial_graph.nodes())
        # initial_graph.add_weighted_edges_from([file[60], file[116]])
        nx.draw(initial_graph, with_labels=True)
        plt.draw()

    def teste(self):
        G = nx.random_geometric_graph(200, 0.125)
        pos = nx.get_node_attributes(G, 'pos')

        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - 0.5) ** 2 + (y - 0.5) ** 2
            if d < dmin:
                ncenter = n
                dmin = d



if __name__ == "__main__":
    GraphGenerator().generate()
