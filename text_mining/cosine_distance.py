import numpy as np
from pre_processing import PreProcessamentoDados


class VideoDistance:
    def __init__(self):
        self.obj = PreProcessamentoDados()

    @staticmethod
    def cosine(u, v):
        dist = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
        print(dist)
        return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

    def matrix_pre_process(self):
        age = self.obj.age_normalize()
        duration = self.obj.duration()
        view = self.obj.views_relative_age()
        likes = self.obj.likes_relative_views()
        deslikes = self.obj.deslikes_relative_views()
        authors = self.obj.author()
        sum_values = [age[i] + duration[i] + view[i] + likes[i] + deslikes[i] for i in range(0, len(age))]
        sum_values = [[sum_values[i] + authors[i] for i in range(0, len(j))] for j in authors]
        return sum_values
    

    def simillarity_matrix(self):
        pass


if "__main__" == __name__:
    u = [1, 2, 3, 4, 5, 7]
    v = [2, 3, 7, 8, 9, 6]
    # VideoDistance().cosine(u, v)
    VideoDistance().matrix_pre_process()
