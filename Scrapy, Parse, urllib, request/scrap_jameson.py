import requests
from bs4 import BeautifulSoup

#Этот скрипт разработан исключительно в ознакомительных целях, и для частного
#использования(моего отца)
#Для определения оптимальной стоимости виски
headers = {'User-Agent':\
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) \
            AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4'}

def get_html(url):
    html = requests.get(url, headers=headers)
    return html.text

def get_price_alcomag(html):
    soup = BeautifulSoup(html, "html.parser")
    get_name = soup.find('h1').text.rstrip()
    get_price = soup.find('div', class_='snt-detail-price').text
    return get_name, get_price

def get_my_wiskey(html):
    soup = BeautifulSoup(html, "html.parser")
    get_name = soup.find('h1').text
    get_price = soup.find('div', class_='cust-content-inner cust-content-indent').find('span', class_='detail-price-uah').text
    return get_name, get_price

def main():
    url = 'https://alcomag.com.ua/viski-jameson-0-7-l/'
    url_rozetka = 'https://rozetka.com.ua/jameson_5011007003005/p4718917/'
    html = get_html(url)
    price = get_price_alcomag(html)
    print('Магазин Алкомаг\n', price[0], '\nЦЕНА', price[1].strip(),'грн')
    html_rozetka = get_html(url_rozetka)
    price_rozetka = get_my_wiskey(html_rozetka)
    print('Магазин Розетка\n', price_rozetka[0], '\nЦЕНА', price_rozetka[1])
    input('Нажмите "Enter" для выхода')


if __name__ == "__main__":
    main()