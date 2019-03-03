from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html')
bs = BeautifulSoup(html)
for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
