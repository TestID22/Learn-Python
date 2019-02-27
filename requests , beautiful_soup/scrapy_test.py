from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen('http://grompe.org.ru/static/prog_comp_matrix_ru.html')
#создаём объект супа
bso = BeautifulSoup(url)
print(bso.a)
#ищем по тегам выборки
word_tags = {'h1','h2','h3','a'}
namelist = bso.findAll(word_tags)

for name in namelist:
    #name.get_text() отделяет текс от тегов
    print(name.get_text())
input()
