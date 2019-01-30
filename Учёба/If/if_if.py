new_order = []
topping = ['mushrooms','peperonni','4 chease']
if 'mushrooms' in topping:
    new_order.append('Pizzas with mushrooms')
if '4 chease' in topping:
    new_order.append('Pizzas with 4 chease')
print(new_order)

alien_color = 'green'
if alien_color == 'green':
    print('Вы подбили корабль и получили 5 очков')
elif alien_color == 'yellow':
    print('Вы заработали 12')
elif alien_color == 'red':
    print('Вы заработали 154 очков')
else:
    print('вы заработали 10 очков')


#taks for if operation
print('Переиод жизни человека')
age = int(input('Введите ваш возраст'))

if age == 1:
    print('Вы младенец')
elif age > 1 and age <5:
    print('малыш')
elif age >5 and age <10:
    print('вы юнец')
elif age >10 and age <20:
    print('вы красавчик ')
elif age > 20 and age <50:
    print('средний возраст')
elif age >50 and age <89:
    print('вы пенсия')
else:
    print('скорее всего вы эльф')