from urllib.request import urlopen
from bs4 import BeautifulSoup

site = urlopen('https://auto.ria.com/car/mercedes-benz/')
soup = BeautifulSoup(site.read())
get_my_mers = soup.findAll('span',{'class':'blue bold'})
for mers in get_my_mers:
    print(mers)

