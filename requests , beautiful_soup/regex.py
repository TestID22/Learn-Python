import re

#Чтоб искать в регулярных выражениях скобки пример (\(\d\d\d\))-(\d\d\d\d)
#Создаём регулярное выражение \d\d\d - будет приравнено шаблону 
#Пишем шаблон в соотвествии с поисковым запросом включая пробелы
phone = re.compile(r'(\(\d\d\d\))-(\d\d\d\d\d\d\d)')
# Метод serch - ищет соответсвия нашему шаблону.
mo = phone.search('Тут текст и всё, ну и три циферки для регулярных выражений (812)-4532345')
#Метод group - выводит ответ 
print('Шаблон регулярного выражения = (\(\d\d\d\))-(\d\d\d\d\d)')
print('Найденый ответ :',mo.group())
#Возвращает первую группу блока регулярного выражения (\d\d\d\) - первый блок отделён скобками
print('Выводим на экран первую группу, выражения:',mo.group(1))
#Возвращает вторую группу
print('Выводим вторую группу:',mo.group(2))
#Трюк с групповым присвоением переменных
first_group, second_group = mo.groups()
print('Групповое присвоение переменных:',first_group)
#Возвращает группу в виде кортежа 
l = mo.groups()
#Создадим список из изяътых блоков, для удобной работы, списки изменяемый тип данных
new_l = list(l)
print('Код города:' + new_l[0] + ' а номер телефона ' + new_l[1] )

