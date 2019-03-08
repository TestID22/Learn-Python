test = lambda x, y: x ** y
print(test(2, 2))
 
test1 = lambda x, y, z: x + ' ' + y + ' ' + z
print(test1('Привет','ты','программист'))
#Лямбда выражение может использовать именнованые аргументы, как и функции
test2 = lambda a='Lewis ', b='Hammilton': a + b
print(test2(b='champion'))

