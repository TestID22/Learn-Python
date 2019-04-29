
s = 'Hello'
a, b, c, d ,e = s
print("Распаковываем интерируемый объект", a + b + c + d)
#используем срез
print(s[0])


record = ['Acme', 50, 98, (22, '09', 1989),(3, 2, 2009)]
name, num, price, *dates = record #распаковка звёздочкой, такая же как при n аргументов в функциях
print(dates)

items = ['1','4', '54','13', 44]
head, *tails = items
print(tails)
