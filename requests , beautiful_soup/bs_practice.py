from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    url = urlopen(url)
    scrapy = BeautifulSoup(url.read())
    print(scrapy.h1.get_text())
    

getTitle('http://novogrodovka-rada.gov.ua/')