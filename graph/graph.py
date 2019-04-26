import igraph
import networkx as nx
import matplotlib.pyplot as plt


class GraphGenerator:
    @staticmethod
    def generate():
        initial_graph = nx.Graph()
        edges = nx.read_edgelist('edges.txt')
        nodes = nx.read_adjlist('nodes.txt')
        file = open('weight.txt', 'r')
        file = file.read().split("\n")
        file = [tuple(i.split(" ")) for i in file]
        """
        for i in file:
            i = i.split(" ")
            i = tuple(i)
            print(i)
            initial_graph.add_weighted_edges_from(i)"""
        weight = nx.read_weighted_edgelist('weight.txt')
        # initial_graph.add_edges_from(edges.edges)
        initial_graph.add_nodes_from(nodes)
        initial_graph.add_weighted_edges_from([file[60], file[116]])
        nx.draw(initial_graph, with_labels=True)
        plt.draw()


if __name__ == "__main__":
    GraphGenerator().generate()
