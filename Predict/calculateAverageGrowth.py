
def calculate_avg(data):

    coin_price = []
    for i in data:
        coin_price.append(float(i[1]))

    values = []
    try:
        for i in range(len(coin_price)):
            values.append(coin_price[i+1] * 100 / coin_price[i] - 100)
    except IndexError as e:
        pass

    total = 0.0
    for value in values:
        total += value

    return round(total / len(values), 4)
