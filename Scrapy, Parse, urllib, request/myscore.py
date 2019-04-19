import requests
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text

def get_game(html):
    soup = BeautifulSoup(html, 'html.parser')
    get_team = soup.find('table', class_='soccer').find_all('span')
    td = []
    for i in get_team:
        td.append(i)
    return td

def main():
    url = 'https://www.myscore.com.ua/football/italy/serie-a/'
    html = get_html(url)
    data = get_game(html)
    print(type(data))
    for i in data:
        print(i)
    

if __name__ == "__main__":
    main()