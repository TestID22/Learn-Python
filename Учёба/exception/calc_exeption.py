#исключения и ошибки в приложениях, обходим аварийное завершение программ
print('Красная Королева: Напишите два числа, а я их поделю')
print('quit - для выхода')
while True:
    first_number = input('Введите первое число:')
    if first_number == 'quit':
        break
    second_number = input('Введите второе число:')
    if second_number == 'quit':
        break
    try:
        divide = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Ну нельзя на нолик делить')
    except ValueError:
        print('Флоаты тоже не делим')
    else:
        print(divide)
