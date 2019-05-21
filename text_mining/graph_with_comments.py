import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities


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

        G = nx.dodecahedral_graph()
        file = open('text_mining/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()

        G.add_nodes_from(range(0, 121))
        adj_list = [sorted([int(adj[0]), int(adj[1])]) for adj in file if
                    float(adj[2]) >= 0.9 and adj[0] != adj[1]]
        adj_list = self.remove_repetidos(adj_list)

        for adj in adj_list:
            G.add_edge(adj[0], adj[1])

        partition = greedy_modularity_communities(G)
        print(type(partition))
        values = [partition(node) for node in G.nodes()]
        print(f'values: {values}')
        partition = [list(x) for x in partition]
        # print(len(partition))
        # print(f'C: {partition}')

        pos = nx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        plt.axis('off')
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()

        # write ncol
        # nx.readwrite.gml.write_gml(G, 'graph/teste.gml')
        # nx.draw(G, with_labels=True)

        # plt.show()

    def using_igraph(self):
        import igraph
        graph = igraph.Graph()
        graph.add_vertices(range(0, 121))

        file = open('text_mining/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()

        adj_list = [sorted([int(adj[0]), int(adj[1])]) for adj in file if float(adj[2]) >= 0.9 and adj[0] != adj[1]]
        adj_list = self.remove_repetidos(adj_list)
        graph.add_edges(adj_list)

        graph.community_multilevel(weights=None, return_levels=True)
        self.plot_(graph)

    def plot_(self, graph, filename="social_network.png"):
        from igraph import plot
        layout = graph.layout("circle")
        visual_style = dict()
        visual_style["vertex_size"] = 20
        visual_style["vertex_label_size"] = 30
        visual_style["vertex_label_dist"] = 2
        visual_style["vertex_color"] = "white"
        visual_style["vertex_label_color"] = "blue"
        visual_style["vertex_label"] = graph.vs["name"]
        visual_style["edge_width"] = 2
        visual_style["layout"] = layout
        visual_style["bbox"] = (1200, 1000)
        visual_style["margin"] = 100
        print(visual_style)
        plot(graph, filename, **visual_style)


if __name__ == "__main__":
    GraphGenerator().using_igraph()
