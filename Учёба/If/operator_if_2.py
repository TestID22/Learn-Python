

age = int(input('введите ваш возраст: '))
if age <12:
    price = 0
elif age <18:
    price = 5
elif age >65:
    price = 2
else:
    price = 50
print('Ваша стоимость билета:'+ str(price) + 'долларов')
print(age)