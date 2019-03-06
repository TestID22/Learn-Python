def func(a, b, c):
    print(a, b, c)
    
func(1, 2, 4)
#именованные параметры функции.
def func_1(a=1,b=2,c=3):
    print(a, b, c)
#через именованный аргумент функции можно задавать значения, в любом порядке.
func_1(c=6)
################################
#обязательные аргументы, и по умолчанию
def super_f1_func(lewis, hammy, tyre='soft', car='mersedes'):
    print(lewis, hammy, tyre, car)

super_f1_func('seb', 'fettel', 'medium','ferrari')
super_f1_func('')
##########################
def func_arg(word, times=1):
    print(word * times)

func_arg('Alex ', 5)
