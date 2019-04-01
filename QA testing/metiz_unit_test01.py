from func_than_i_testing import get_formated_name

print('Введите "q", если захотите выйти!')
while True:
    first = input('Введите имя:')
    if first == 'q':
        break
    last = input('Введите фамилию:')
    if last == 'q': break

    formated_name = get_formated_name(first, last)
    print(formated_name)