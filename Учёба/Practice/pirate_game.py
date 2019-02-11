import random as r

secret = r.randint(1,99)
guess = 0
user_try = 0
print('Эй плешивый пёс, я весёлый космопират Рожер')
print('У меня есть секрет, это число от 1 до 99')
print('Я дам тебе 6 попыток, попробуй угадай')
while guess != secret and user_try < 6:
    guess = int(input('Введи своё число: '))
    if guess < secret:
        print('Ах, ты сухопутная крыса, моё число больше')
    elif guess > secret:
        print('Моё число меньше, ишак тебе кусал')

    user_try += 1

if guess == secret:
    print('Хватит, чебур ты угадал, я отпущу тебя')
else:
    print('Я отпущу тебя на корм акулам')