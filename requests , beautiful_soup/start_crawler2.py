from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#создадим множество функция set() создаёт множество.list() - список str() - строку
pages = set()
def get_link(pageurl):
    global pages
    html = ('https://ru.wikipedia.org/' + pageurl)
    bs = BeautifulSoup('html')
    for link in bs.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                get_link(newPage)
get_link('')
