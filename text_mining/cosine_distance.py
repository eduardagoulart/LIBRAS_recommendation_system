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
        print(f'age: {age[0]}')
        duration = self.obj.duration()
        print(f'duration: {duration[0]}')
        view = self.obj.views_relative_age()
        print(f'view: {view[0]}')
        likes = self.obj.likes_relative_views()
        print(f'likes: {likes[0]}')
        deslikes = self.obj.deslikes_relative_views()
        print(f'deslikes: {deslikes[0]}')
        sum_values = [age[i] + duration[i] + view[i] + likes[i] + deslikes[i] for i in range(0, len(age))]
        print(sum_values)

    def simillarity_matrix(self):
        pass


if "__main__" == __name__:
    u = [1, 2, 3, 4, 5, 7]
    v = [2, 3, 7, 8, 9, 6]
    # VideoDistance().cosine(u, v)
    VideoDistance().matrix_pre_process()
