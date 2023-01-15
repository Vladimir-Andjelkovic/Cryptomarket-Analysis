from datetime import datetime
import os
from Predict.calculateGrowth import calc_growth
from Predict.calculateAverageGrowth import calculate_avg


def get_growth():

    TIME_FORMAT = '%H:%M:%S'
    DATE_FORMAT = '%d-%m-%Y'
    DATETIME_FORMAT = f"""{DATE_FORMAT} {TIME_FORMAT}"""

    dir_list = os.listdir('Coins/')

    for path in dir_list:

        coin_data = []
        with open('Coins/' + path, 'r') as rf:
            for line in rf:
                coin_data.append(line.strip('\n'))

        coin_data_clean = []  # Easier data for calculation
        for data in coin_data:
            entry = data.split(' - ')
            coin_data_clean.append([datetime.strptime(entry[0], DATETIME_FORMAT), entry[1]])  # [0]Date and time, [1]price for that time

        growth = calc_growth(coin_data_clean)  # Overall growth
        avg_growth = calculate_avg(coin_data_clean)  # Average growth per hour

        with open('Reports/DailyReport.txt', 'a+') as af:
            af.write(f"""{path.strip('.txt')}: Growth since the release: {growth}% - Average growth per hour: {
            round(avg_growth, 2)}%\n""")
