# не совсем понятно Использование iF со списками 
topping = []
if topping:
    for top in topping:
        print('adding ', top)
else:
    print('Вы заказали базовую пизу')


#life is so hard when this code work 
avaibale_toppings = ['mushrooms','extra cheese','green peppers'
                     'olivies', 'anchous','pineapple']
request_toppings = ['mushrooms','olivies','french fries','pineapple']

for request_topping in request_toppings:
    if request_topping in avaibale_toppings:
        print('Добавим к заказу ' + request_topping)
    else:
        print('Сорян у нас нету', request_topping)
print('Закончим заказ')