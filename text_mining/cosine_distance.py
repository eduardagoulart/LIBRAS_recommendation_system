import numpy as np
from pre_processing import PreProcessamentoDados
from similarity import matrix


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
        comments = matrix()
        sum_values = [[float(age[i]) - float(duration[i]) - float(view[i]) - float(likes[i]) - float(
            deslikes[i] - float(comment[i][0])) for i in range(0, len(age))] for comment in comments]
        return sum_values

    def adding_authors(self):
        authors = self.obj.author()
        sum_values = self.matrix_pre_process()
        return [[abs(float(sum_values[j][i]) - authors[j][i]) for i in range(0, len(authors[j]))] for j in range(0, len(authors))]

    def normallize_sum_with_author(self):
        matrix = self.adding_authors()
        standard = [[value / max(internal_list) for value in internal_list] for internal_list in matrix]
        print(standard[0])
        return standard

    def simillarity_matrix(self):
        original_matrix = self.normallize_sum_with_author()
        value = [[self.cosine_distance(referential, list_value) for list_value in original_matrix] for referential in
                 original_matrix]
        return value

    def normalize_sum(self):
        matrix = self.matrix_pre_process()
        return [internal_list / max(matrix) for internal_list in matrix]

    def simillarity_without_author(self):
        norma = self.normalize_sum()
        return [[abs(referential - value) for value in norma] for referential in norma]


if "__main__" == __name__:
    u = [1, 2, 3, 4, 5, 7]
    # v = [2, 3, 7, 8, 9, 6]
    v = [1, 2, 3, 4, 5, 7]
    # VideoDistance().cosine_distance(u, v)
    VideoDistance().normallize_sum_with_author()
