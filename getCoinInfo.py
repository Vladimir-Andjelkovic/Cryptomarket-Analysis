import requests
from bs4 import BeautifulSoup
from datetime import datetime, date


def get_info():

    coin_urls = []

    with open('08-01-2023.txt', 'r') as rf:
        for line in rf:
            coin_urls.append(line.strip('\n'))

    for coin_url in coin_urls:
        url = 'https://coinmarketcap.com' + coin_url

        try:
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')

            coin_name = soup.find('div', class_='sc-aef7b723-0 jPJwrb nameHeader').find('h2').find('span').find(
                'span').text
            coin_price = soup.find('div', class_='priceValue').find('span').text.strip('$')
            current_time = str(datetime.now().strftime('%H:%M:%S'))
            current_date = str(date.today().strftime('%d-%m-%Y'))

            with open('Coins/' + coin_name + '.txt', 'a+') as af:
                af.write(f"""{current_date} {current_time} - {coin_price}\n""")

        except Exception as e:
            print('Error: ' + type(e).__name__)
