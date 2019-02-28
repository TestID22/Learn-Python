from bs4 import BeautifulSoup
from urllib.request import urlopen

html = ('https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D1%81%D1%82%D0%B5%D1%80_%D0%A0%D0%BE%D0%B1%D0%BE%D1%82')
html_open = urlopen(html)
bs = BeautifulSoup(html_open)

for link in bs.findAll('a'): #ищем все упоминания тега 'a'
    if 'href' in link.attrs: 
        print(link.attrs['href'])