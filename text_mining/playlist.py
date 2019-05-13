from cosine_distance import VideoDistance
import sys
import pandas as pd
import csv


class Playlist:
    def __init__(self, id_first):
        self.first = id_first
        self.distances = VideoDistance().simillarity_matrix()
        self.distances_without_author = VideoDistance().simillarity_without_author()
        self.file = pd.read_csv("video.csv")

    def playlist_generator_with_author(self):
        first = self.distances[self.first]
        f = open('text_mining/distances.txt', 'w')
        for i in first:
            f.write(str(i))
            f.write('\n')

        f.close()
        d = {}
        i = 0
        j = 0
        video = []
        for referential in self.distances:
            for values in referential:
                d['a'] = {j, values}
                j += 1
            i += 1

        list_recomendation = []

        with open("graph/datas.csv", mode='w') as csv_file:
            fieldnames = ["node1", "node2", "weigh"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(d)

        nodes = open("graph/nodes.txt", "w")
        weight = open("graph/weight.txt", "w")
        ref = 0
        for referential in self.distances:
            ultimo = 0
            for values in referential:
                weight.write(str(ref))
                weight.write(" ")
                weight.write(str(ultimo))
                weight.write(" ")
                weight.write(str(values))
                weight.write('\n')
                ultimo += 1
            nodes.write(str(ref))
            nodes.write("\n")
            ref += 1
        nodes.close()
        weight.close()

        for i in range(0, 10):
            value = max(first)
            list_recomendation.append(self.file["nome_do_vídeo"][first.index(value)])
            new = self.distances[first.index(value)]
            first[first.index(value)] = -1
            first = [first[j] + new[j] for j in range(0, len(new))]
        file = open("com_autor.txt", 'w')
        for i in list_recomendation:
            file.write(i)
            file.write('\n')
        return list_recomendation

    def playlist_generator_without_author(self):
        first = self.distances_without_author[self.first]
        print(first[0])

        list_recomendation = []
        for i in range(0, 10):
            value = min(first)
            list_recomendation.append(self.file["nome_do_vídeo"][first.index(value)])
            new = self.distances[first.index(value)]
            first[first.index(value)] = 100000000000000000000
            first = [first[j] + new[j] for j in range(0, len(new))]

        file = open("sem_autor.txt", 'w')
        for i in list_recomendation:
            file.write(i)
            file.write('\n')
        print(list_recomendation)
        return list_recomendation


if __name__ == '__main__':
    try:
        id_video = sys.argv[1]
    except:
        print("Argumento inválido para começar a playlist")
        exit(404)

    Playlist(int(id_video)).playlist_generator_with_author()
