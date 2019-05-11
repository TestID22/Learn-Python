
print('''
u   u aaaa h   h  tttttttt ooooooo    $$  $$  $$$$$  $$$$
u   u a  a h   h     tt    oo   oo    $$  $$  $$     $$  $$
u   u aaaa hhhhh     tt    oo   oo    $$  $$     $$  $$  $$
uuuuu a  a h   h     tt    ooooooo    $$$$$$  $$$$$  $$$$

''')


print("Конвертер Гривны в Долар и Обратно")
uah_per_usd = 0.038
cost = float(input("Введите вашу сумму "))
currency = input("Введите для гривны 'g' для доляра 'd' ")

if currency == 'g':
    print("За твои", cost , "гривен дадут", cost * uah_per_usd, "бачей")
elif currency == 'd':
    print("За твои", cost , "баксов дадут", cost / uah_per_usd, "гривастых")
else: 
    print("Четстно говоря, я такого ещё не видал")