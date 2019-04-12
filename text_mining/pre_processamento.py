import pandas as pd
from datetime import datetime
import calendar


class PreProcessamentoDados:
    def __init__(self):
        self.file = pd.read_csv('video.csv')

    def video_age(self):
        data_time = self.file['data_de_publicação']
        splited_data = data_time[0].split(" ")
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        splited_data[1] = splited_data[1].replace(",", "")
        age = datetime.now() - datetime(int(splited_data[2]), abbr_to_num[splited_data[0]], int(splited_data[1]))
        time_in_seconds = (age.days * 86400) + age.seconds
        return time_in_seconds


if __name__ == '__main__':
    PreProcessamentoDados().video_age()