from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://news.meta.ua/')
bso = BeautifulSoup(url)
print(bso)