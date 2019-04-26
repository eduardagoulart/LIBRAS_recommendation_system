import igraph
import networkx as nx
import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go



class GraphGenerator:
    @staticmethod
    def generate():
        G = nx.Graph()
        edges = nx.read_edgelist('graph/edges.txt')
        # nx.read_weighted_edgelist()
        nodes = nx.read_adjlist('graph/nodes.txt')
        file = open('graph/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        # print(file)
        file.pop()
        for adj in file:
            G.add_edge(adj[0], adj[1], weight=float(adj[2]))
        weight = nx.read_weighted_edgelist('graph/weight.txt')
        # G.add_edges_from(edges.edges)
        G.add_nodes_from(nodes)
        # G.add_weighted_edges_from(weight.edges())
        # print(G.edges())
        nx.draw(G, with_labels=True)
        plt.draw()

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=6)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,
                               width=2, alpha=0.5, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        plt.axis('off')
        plt.show()
        
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
