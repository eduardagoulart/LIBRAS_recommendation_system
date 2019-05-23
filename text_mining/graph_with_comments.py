import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities
import igraph


class PlotResults:
    @staticmethod
    def remove_repetidos(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l

    def making_plot(self):
        # graph = igraph.Graph()
        # graph.add_vertices(range(0, 121))

        file = open('text_mining/weight.txt', 'r')
        file = file.read().split("\n")
        file = [i.split(" ") for i in file]
        file.pop()

        adj_list = [sorted([int(adj[0]), int(adj[1])]) for adj in file if float(adj[2]) >= 0.9 and adj[0] != adj[1]]
        adj_list = self.remove_repetidos(adj_list)

        # graph.add_edges(adj_list)
        graph = igraph.Graph(vertex_attrs={"label": range(0, 121)}, edges=adj_list)
        visual_style = {"bbox": (1200, 1200), "margin": 20}

        member = graph.community_multilevel(weights=None, return_levels=False)
        print(member)
        igraph.plot(member, **visual_style)
        # self.plot_(member)
        graph.write_ncol("text_mining/graph.ncol")
        graph.write_gml('text_mining/graph.gml')


if __name__ == "__main__":
    PlotResults().making_plot()
