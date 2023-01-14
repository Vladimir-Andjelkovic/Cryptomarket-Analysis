import requests
from bs4 import BeautifulSoup
from datetime import date


def get_coin_urls():
    coin_urls = []
    target_url = 'https://coinmarketcap.com/new/'  # Page of recently added coins
    html_text = requests.get(target_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    get_coin_table = soup.find('table', class_='sc-f7a61dda-3 hWJOxP cmc-table').find('tbody')
    get_coin_rows = get_coin_table.find_all('tr')

    for row in get_coin_rows:
        coin_link = row.find('a', class_='cmc-link')
        coin_urls.append(coin_link['href'])

    file_name = str(date.today().strftime('%d-%m-%Y')) + '.txt'
    with open(file_name, 'w') as f:
        for link in coin_urls:
            f.write(link + '\n')
