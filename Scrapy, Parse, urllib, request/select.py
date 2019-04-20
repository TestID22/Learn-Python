import requests
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    return html.text

def get_select(html):
    soup = BeautifulSoup(html)
    get_h1 = soup.select('h1')
    return get_h1



def main():
    url = 'https://tproger.ru/tag/python/'
    html = get_html(url)
    h1 = get_select(html)
    print(h1)


if __name__ == "__main__":
    main()