import matplotlib.pyplot as plt


class GraphGenerator:
    @staticmethod
    def remove_repetidos(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l

    def generate(self):
        import networkx as nx

        G = nx.Graph()  # 5x5 grid
        nodes = nx.read_adjlist('graph/nodes.txt')
        file = open('graph/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()
        G.add_nodes_from(nodes)
        adj_list = [sorted([int(adj[0]), int(adj[1])]) for adj in file if
                    float(adj[2]) >= 0.9 and adj[0] != adj[1]]
        adj_list = self.remove_repetidos(adj_list)

        for adj in adj_list:
            G.add_edge(adj[0], adj[1])

        '''for adj in file:
            if float(adj[2]) >= 0.9 and adj[0] != adj[1]:
                G.add_edge(adj[0], adj[1], weight=float(adj[2]))'''

        nx.readwrite.gml.write_gml(G, 'graph/teste.gml')
        # nx.draw(G, with_labels=True)
        # plt.show()


if __name__ == "__main__":
    plt.axis('off')
    GraphGenerator().generate()
