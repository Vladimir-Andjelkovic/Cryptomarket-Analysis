from datetime import datetime

TIME_FORMAT = '%H:%M:%S'
DATE_FORMAT = '%d-%m-%Y'
DATETIME_FORMAT = f"""{DATE_FORMAT} {TIME_FORMAT}"""


def calc_growth(data):  # Calculates overall growth

    coin_price = []
    for i in data:
        coin_price.append(float(i[1]))

    general_growth = coin_price[-1] * 100 / coin_price[0] - 100

    return round(general_growth, 2)


def calc_growth_24h(data):
    pass


