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

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] >= 1.0]
        print(elarge)
        print(len(elarge))
        # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.9]
        # pos = nx.get_node_attributes(G, 'pos')

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=10)

        # edges
        # nx.draw_networkx_edges(G, pos, edgelist=elarge,
        #                        width=6, alpha=0.2, edge_color='a')
        # nx.draw_networkx_edges(G, pos, edgelist=esmall,
        #                        width=1, alpha=0.2, edge_color='b', style='dashed')

        # labels
        nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')

        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    plt.axis('off')
    '''
    G = nx.random_geometric_graph(200, 0.125)
    # position is stored as node attribute data for random_geometric_graph
    pos = nx.get_node_attributes(G, 'pos')

    # find node near center (0.5,0.5)
    dmin = 1
    ncenter = 0
    for n in pos:
        x, y = pos[n]
        d = (x - 0.5) ** 2 + (y - 0.5) ** 2
        if d < dmin:
            ncenter = n
            dmin = d

    # color by path length from node near center
    p = dict(nx.single_source_shortest_path_length(G, ncenter))

    plt.figure(figsize=(8, 8))
    nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
    nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()),
                           node_size=80,
                           node_color=list(p.values()),
                           cmap=plt.cm.Reds_r)

    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    plt.show()
    
    '''
    GraphGenerator().generate()
