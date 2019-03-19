names = ['name', 'age', 'pay']
values = ['Elliot', 'Angella', 'Darling']

fsociety = list(zip(names, values))
print(fsociety)

darling = dict(zip(names, values))
print(darling)
#созданик словаря с ключами но неизвестными значениями
field = ['name', 'age', 'pay']
record = dict.fromkeys(field, '?')
print(record)