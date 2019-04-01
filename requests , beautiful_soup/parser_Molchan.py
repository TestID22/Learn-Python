from urllib.request import urlopen
from bs4 import BeautifulSoup

site = urlopen('http://www.girnyk.dn.ua')
beautiful_site = BeautifulSoup(site.read())
print(beautiful_site.h1)


