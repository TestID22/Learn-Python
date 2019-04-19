import requests
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text

def get_game(html):
    soup = BeautifulSoup(html, 'html.parser')
    get_team = soup.findAll('td', class_='cell_ab team-home  bold')
    return get_team

def main():
    url = 'https://www.myscore.com.ua/football/italy/serie-a/'
    html = get_html(url)
    data = get_game(html)

    for i in data:
        print(i)
    

if __name__ == "__main__":
    main()