import re 

#Поиск эмейлов 1.Создаём регулярное выражения для поиска эмейлов
email_regex = re.compile('[A-Za-z0-9\._+]+@[A-Za-z]+\.(com)')
#используем генератор для создания объекта(*файла)
file = [x.rstrip() for x in open('email_list.txt')]
#конвертируем в тип Str
e_finder = email_regex.search(str(file))
print(e_finder.group())
