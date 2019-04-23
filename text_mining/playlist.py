from cosine_distance import VideoDistance
import sys
import pandas as pd


class Playlist:
    def __init__(self, id_first):
        self.first = id_first
        self.distances = VideoDistance().simillarity_matrix()
        self.distances_without_author = VideoDistance().simillarity_without_author()
        self.file = pd.read_csv("video.csv")

    def playlist_generator_with_author(self):
        first = self.distances[self.first]
        list_recomendation = []
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
        print(list_recomendation)
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