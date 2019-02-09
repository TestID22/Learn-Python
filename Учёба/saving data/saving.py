import json

numbers = list(range(1,10))
#обозначаем имя файла, в котором будем хрантиь данные
filename = 'numbers.json'
#открываем файл.json с атрибутом 'w' записи данных
with open(filename, 'w')as f_obj:
    #json.dump функция используется для записи в файл
    json.dump(numbers, f_obj)
