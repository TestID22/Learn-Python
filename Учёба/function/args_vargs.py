order = []
#*args - передаёт неизвестное количество аргументов
def arg_func(*args):
    order.append(*args)
    print(order)

arg_func('пеперони, яблоки, картофель-фри')
############################################
#при передаче неизветного количества аргуметнов функция вернёт кортеж
def func(*args):
    print(args)

func(1, 2, 4, 5)

#ДВЕ ЗВЁДОЧКИ ВЕРНЁТ СЛОВАРЬ - это прям супер важно(С) Winderton
def func_1(**args):
    print(args)

func_1(lewis='mersedes', tyre='soft')
