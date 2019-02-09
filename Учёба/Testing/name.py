from name_function import get_formared_name

print('Нажми q для выхода')
while True:
    f_name = input('Введите имя:')
    if f_name == 'q':
        break

    l_name = input('Введите фамилию:')
    if l_name == 'q':
        break

    formated_name = get_formared_name(f_name, l_name)
    print('Тебя звать!', formated_name)
