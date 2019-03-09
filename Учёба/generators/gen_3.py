#генератор выражений - это как генератор списков, только 
#возвращает итерируемый объект
g = (x * 4 for x in 'spam')

i = iter(g)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#функции - генераторы
def timesfour():
    for i in 'LEWIS':
        yield i * 4

timesfour()
iter_func = iter(timesfour())
print(next(iter_func))
print(next(iter_func))
