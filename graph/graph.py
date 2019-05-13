import networkx as nx
import matplotlib.pyplot as plt


class GraphGenerator:
    @staticmethod
    def generate():
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()  # 5x5 grid
        nodes = nx.read_adjlist('graph/nodes.txt')
        file = open('graph/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()
        G.add_nodes_from(nodes)
        count =0

        for adj in file:
            if float(adj[2]) >= 0.9 and adj[0] != adj[1]:
                G.add_edge(adj[0], adj[1], weight=float(adj[2]))
                print(f'adj[0]: {adj[0]}, adj[1]: {adj[1]}')
                count += 1
        nx.readwrite.gml.write_gml(G, 'graph/teste.gml')
        print(count)
        nx.draw(G, with_labels=True)
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
