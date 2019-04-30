import igraph
import networkx as nx
import matplotlib.pyplot as plt


class GraphGenerator:
    @staticmethod
    def generate():
        G = nx.Graph()
        nodes = nx.read_adjlist('graph/nodes.txt')
        file = open('graph/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()
        for adj in file:
            G.add_edge(adj[0], adj[1], weight=float(adj[2]))

        G.add_nodes_from(nodes)

        nx.draw(G, with_labels=True)
        plt.draw()

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] < 0.3]
        print(elarge)
        print(len(elarge))
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.9]

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=122)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=1)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,
                               width=1, alpha=0.2, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')

        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    GraphGenerator().generate()
