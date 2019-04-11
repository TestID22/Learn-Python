numbers = [1,4,5,7,80,23,634,4]
sum_num = 0
for i in numbers:
    sum_num += i
print('Сумма всех чисел списка numbers = ', sum_num)

def min_func(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
            return res
        
print('Минимальное число аргументов функции равно : ', min_func(1,45,56,56,12,5,7,-2))

for_min = [1,9,24,6,1,3,-3]
res = []
start = for_min[0]
for i in for_min[1:]:
    if i < start:
        start = i
        res.append(i)
        print(res)
###########################        


