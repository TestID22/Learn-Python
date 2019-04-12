import requests
from bs4 import BeautifulSoup


url = 'https://www.olx.ua/elektronika/don/q-%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80/'
headers = {
            'User-Agent':\
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) \
            AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4'
            }
#Захват страницы, возьмём код HTML
def getHtml(url):
    html = requests.get(url, headers=headers) #response - это объект реквеста запроса
    return html.text # метод текст возвращает html

#Захват ссылок на товар
def getAllLinks(html):
    soup = BeautifulSoup(html)
    find_links = soup.find('table', id='offers_table').find_all('tr', class_='wrap')
    links = []
    for tr in find_links:
        a = tr.find('a').get('href')
        links.append(a)

    return links

    

            
def main():
    html = getHtml(url)
    parse_links = getAllLinks(html)
    for i in parse_links:
        print(i)
    




if __name__ == "__main__":
    main()