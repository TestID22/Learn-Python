from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen('http://news.meta.ua/')
#создаём объект супа
bso = BeautifulSoup(url)
print(bso.a)
#ищем по тегам выборки
namelist = bso.findAll({'h1','h2','a'})
for name in namelist:
    #name.get_text() отделяет текс от тегов
    print(name.get_text())
input()
