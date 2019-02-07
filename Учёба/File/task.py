while True:
    print('Введите quit - для выхода')
    name_user = input('Введите ваше имя, ну плиз:')
    print('Привет ', name_user)
    if name_user == 'quit':
        break
    with open('guess.txt','a') as guess_book:
        
guess_book.write(name_user + '\n')
   
