elliot = {'name':'Elliot Anderson','age': 32, 'pay':40000}
darling = {'name': 'Darling', 'age':35, 'pay': 1000}

#функция split разбивают строку по пробелам в список
print(elliot['name'].split()[-1])
#поднимем нищенскую зарпалту Дарлин
darling['pay'] *= 1.10
print(darling['pay'])

#При использовании словарей мы повышаем удобочитаемость кода
#создание словаря через функцию dict причём все ключи будут строками
tyrell = dict(name='Tyrell Wellick', age=42, pay=10000)

tyrell['pay'] *= 1.50 
print(tyrell['name'].split()[-1], tyrell['pay'])
#создаём пустой словарь
fsociety = {}
#добавим в словарь данные
fsociety['name'] = 'Angella Moss'
fsociety['age'] = 30
fsociety['pay'] = 25000
print(fsociety)