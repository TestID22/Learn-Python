def greater_user(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
while 1:
    '''Введи имя елси чего пуш "quit" '''
    f_name = input('Эй, ламер введи имя :')
    if f_name == 'quit':
        break
    s_name = input('Кто по жизни будешь :')
    if s_name == 'quit':
        break

    name = greater_user(f_name,s_name)
    print('Редкий Днарь',name)