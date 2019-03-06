def find_min_func(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
            return res

print(find_min_func(1, 91, 20, -1, 23, 13))

#изи функция нахождения минимума рукописная
def easy_min(*args):
    data = list(args)
    data.sort()
    return data[0]
print(easy_min(2,5,98,2,10,-2))

############################

#поиск минимум через функцию min
data_min = list(range(-100,100))
print(min(data_min))

############################
#функция больше - меньше
def max_num(x,y):
    if x > y:
        print(x,' Максимальное')
    elif x < y:
        print(y, ' Максимальное')
    else:
        print(x, y, 'РАВЕНСТВО')

first_num = input('Введите первое число: ')
second_num = input('Введите втророе число: ')
max_num(int(first_num),int(second_num))