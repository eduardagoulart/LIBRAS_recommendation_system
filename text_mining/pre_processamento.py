import pandas as pd
from datetime import datetime
import calendar


class PreProcessamentoDados:
    def __init__(self):
        self.file = pd.read_csv('video.csv')

    def video_age(self):
        data_time = self.file['data_de_publicação']
        # data_time[0] = data_time[0].split(" ")
        aux = data_time[0].split(" ")
        # print(data_time)
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        aux[1] = aux[1].replace(",", "")
        print(type(aux[1]))
        age = datetime.now() - datetime(int(aux[2]), abbr_to_num[aux[0]], int(aux[1]))
        print(age.seconds)


if __name__ == '__main__':
    PreProcessamentoDados().video_age()