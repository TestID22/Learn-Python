#Инструкция Continue если не тру, то возвращает в начало цикла
while True:
    username = input('Введите имя: ')
    if username.title() == 'Alex':
        print('Привет ', username.title())
    else:
        continue
    userpass = input('Введите пароль: ')
    if userpass == '1':
        break
print('Fck you Lamo')