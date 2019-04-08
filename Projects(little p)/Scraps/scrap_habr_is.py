from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://habr.com/ru/hub/infosecurity/')
soup = BeautifulSoup(html)
city = soup.findAll('a', {'class':'post__title_link'})
for i in city:
    if 'href' in i.attrs:
        print(i.attrs['href'])
        print(i.get_text())