print("Программа для расчёта суммы трёх чисел,\
     и их среднего арифметического числа ")
    
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
    

def sum_num(first, second, third, *args):
    sum_n = first + second + third
    return sum_n

def average(first, second, third):
    divider = int(input("Введите количество цифр:"))
    average = (first + second + third) / divider
    return average

#Основной цикл программы
while True:  
    logic = int(input("\nВведите 1 - для расчёта суммы\n\
        Введите 2 - для расчёта среднего арифметического "))
    if logic == 1:
        print(sum_num(second,first, third))
    elif logic == 2:
        print("Среднее арифметическое равно: ")
        print("Среднее арифметическое равно: ", average(first,second,third))
    else:
        print("Выввели неправильное значение")
