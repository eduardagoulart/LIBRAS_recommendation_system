import pandas as pd
from datetime import datetime
import calendar


class PreProcessamentoDados:

    def __init__(self):
        self.file = pd.read_csv('video.csv')

    def video_age(self):
        data_time = self.file['data_de_publicação']
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        time = []
        for value in data_time:
            data_splited = value.split(" ")
            data_splited[1] = data_splited[1].replace(",", "")
            age = datetime.now() - datetime(int(data_splited[2]), abbr_to_num[data_splited[0]], int(data_splited[1]))
            time_in_seconds = (age.days * 86400) + age.seconds
            time.append(time_in_seconds)
        return time

    def age_normalize(self):
        age = self.video_age()
        standard = age.copy()
        standard.sort(reverse=True)
        max_value = standard[0]
        standard = [value/max_value for value in standard]
        return standard

    def duration(self):
        data = self.file['duração_do_video']
        time = []
        for video in data:
            rcv_data = video.split(" ")
            if rcv_data[1] == 'minutes,':
                time.append(self.minutes_plus_seconds(rcv_data))

            elif rcv_data[1] == 'minutes':
                time.append(self.only_minutes(rcv_data))
            elif rcv_data[1] == 'hour,':
                time.append(self.hour_plus_minutes(rcv_data))
            else:
                time.append(rcv_data[0])
        return time

    def minutes_plus_seconds(self, rcv_data):
        duration_time = 0
        duration_time += int(rcv_data[0]) * 60
        if rcv_data[3] == 'seconds':
            duration_time += int(rcv_data[2])
        return duration_time

    def hour_plus_minutes(self, rcv_data):
        duration_time = 0
        duration_time += int(rcv_data[0]) * 3600
        if rcv_data[3] == 'minutes':
            duration_time += int(rcv_data[2]) * 60
        return duration_time

    def only_minutes(self, rcv_data):
        return int(rcv_data[0]) * 60

    def author(self):
        authors_list = self.file['autor']
        referential = authors_list[0]
        authors_list[37] = authors_list[37].split('"')[0]
        final_result = [1 if i == referential else 0 for i in authors_list]
        return final_result


if __name__ == '__main__':
    PreProcessamentoDados().author()
