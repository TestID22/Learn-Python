person = {'name': 'Henry Ford',
          'Gender': 'Male',
          'position':'Data Scientist',
          'Planet':'Earth'}
#Добавим ключ и значение в Словарь
person['Friend'] = 'Kolya'
person['Age'] = 33
person_keys = []
#сохраним ключи словаря person в person_keys
for i in person.keys():
    person_keys.append(i)
print(person_keys)

#сделаем список из ключа name
person_name = list(person['name'])
#Юзаем обратный срез и убирем первые пять элементов
print(person_name[:5:-1])
for i in person_name:
    print(i)

for i in person.items():
    print(i)