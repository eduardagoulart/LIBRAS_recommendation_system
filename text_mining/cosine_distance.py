import numpy as np
from pre_processing import PreProcessamentoDados


class VideoDistance:
    def __init__(self):
        self.obj = PreProcessamentoDados()

    @staticmethod
    def cosine_distance(u, v):
        return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

    def matrix_pre_process(self):
        age = self.obj.age_normalize()
        duration = self.obj.duration()
        view = self.obj.views_relative_age()
        likes = self.obj.likes_relative_views()
        deslikes = self.obj.deslikes_relative_views()
        authors = self.obj.author()
        sum_values = [age[i] + duration[i] + view[i] + likes[i] + deslikes[i] for i in range(0, len(age))]
        sum_values = [[float(sum_values[i]) + author[i] for i in range(0, len(author))] for author in authors]
        return sum_values

    def normallize_sum(self):
        matrix = self.matrix_pre_process()
        standard = [[value / max(internal_list) for value in internal_list] for internal_list in matrix]
        return standard

    def simillarity_matrix(self):
        original_matrix = self.normallize_sum()
        value = [[self.cosine_distance(referential, list_value) for list_value in original_matrix]for referential in original_matrix]
        return value


if "__main__" == __name__:
    u = [1, 2, 3, 4, 5, 7]
    # v = [2, 3, 7, 8, 9, 6]
    v = [1, 2, 3, 4, 5, 7]
    # VideoDistance().cosine_distance(u, v)
    VideoDistance().simillarity_matrix()
