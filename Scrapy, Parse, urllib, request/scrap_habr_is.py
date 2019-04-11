from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://habr.com/ru/hub/infosecurity/')
soup = BeautifulSoup(html)
site = soup.findAll('a', {'class':'post__title_link'})

all_links = []

print('\nСтатьи на Хабре про Информационную безопастность\n')

for links in site:
    if 'href' in links.attrs:
        all_links.append(links.attrs['href'])

        
        print(links.get_text())
        print(links.attrs['href'])


