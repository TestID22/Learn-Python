import time
#скорость работы функции
def my_func():
    my_number = 1
    for i in range(1, 100000):
        my_number = my_number * i
    return my_number

start_time = time.time()
result = my_func()
end_time = time.time()
print('Скорость работы функции :', end_time - start_time)
print('Длина результата...ого.', len(str(result)))