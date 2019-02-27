
from urllib.request import urlopen
from bs4 import BeautifulSoup



#Скрапим HTML 
html = urlopen('http://grompe.org.ru/static/prog_comp_matrix_ru.html')

#Создаём объект класса BS
beautifulsoup_object = BeautifulSoup(html.read())
#Распарсим супом тем заголовка H1
print(beautifulsoup_object.html.body.h1)

print(beautifulsoup_object)

input()

