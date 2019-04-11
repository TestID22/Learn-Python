from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://auto.ria.com/search/?region.id[0]=13&city.id[0]=114&sort[0].order=price.asc&abroad.not=0&custom.not=1&brand.id[0]=79')
soup = BeautifulSoup(html.read())
h1 = soup.find_all('span',{'class':'bold green size22'})
for i in h1:
    if '$' in i.get_text():
        continue
    print(i.get_text(),'USD')
   