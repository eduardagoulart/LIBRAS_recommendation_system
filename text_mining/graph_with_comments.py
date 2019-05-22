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

        member = graph.community_multilevel(weights=None, return_levels=False)
        print(member)
        igraph.plot(member)
        # self.plot_(member)
        graph.write_ncol("text_mining/graph.ncol")
        graph.write_gml('text_mining/graph.gml')

    def plot_(self, graph, filename="text_mining/libras.png"):
        from igraph import plot
        graph.vs["label"] = graph.vs["name"]
        visual_style = dict()
        visual_style["vertex_size"] = 20
        visual_style["vertex_label_size"] = 30
        visual_style["vertex_label_dist"] = 1
        visual_style["vertex_color"] = 'white'
        visual_style["vertex_label_color"] = "blue"
        visual_style["edge_width"] = 2
        visual_style["layout"] = layout
        visual_style["bbox"] = (1200, 1000)
        visual_style["margin"] = 100
        plot(graph, filename, **visual_style)
        # plot(graph, filename, **visual_style)


if __name__ == "__main__":
    GraphGenerator().using_igraph()
