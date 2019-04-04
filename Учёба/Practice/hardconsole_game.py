import random

tries = 6
secret_num = random.randint(1, 100)

print('Я весёлый каретчик Кaреткин')
print('Помоги мне выйти на работу')
print('У меня всего 6 попыток')
print('УГАДАЙ ЧИСЛО от 1 до 100, и я выйду на работу')
username = input('Введите ваше имя:')
while tries > 0:
    guess = int(input('Введи число от 1 до 100:\n'))
    if guess < secret_num:
       print('Ваше число меньше Секретного кода\n')
       tries = tries - 1
    elif guess > secret_num:
        print('Ваше чилсо больше Секретного Кода\n')
        tries = tries - 1
    else:
        print('УРА! ЭДЯ ВЫШЕЛ НА РАБОТУ!')
        break
else:
    print('Васильевич жестоко уволил', username ,'с ПОЗОРОМ!')
