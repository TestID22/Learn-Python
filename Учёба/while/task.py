#Task к While циклам
message = ''
active = True
text = 'Введите добавки:'
text += '\nВведите "quit" для выхода'
while active:
    print(text)
    message = input('')
    if message == 'quit':
        active = False
    else:
        print('Вы добрали ',message)

#Task num2
age = int(input('Введите свой возраст:'))
if age < 12:
    print('цена вашего билета ничтожна - 5 басков')
elif age <18:
    print('тебе повезло меньше. твоя цена чирик')
elif age <30:
    print('С тебя сдеру все 20')
else:
    print('Тебе вообще нельзя')