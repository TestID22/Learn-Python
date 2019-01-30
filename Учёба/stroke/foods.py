#копируем список и сохраним в переменную срез [:] - означает, весь список
foods = ['pizza','fish','potato Free']
friend_foods = foods[:]
print('Myfavourites foods is:')
print(foods)

print('My friend favourites foods is:')
print(friend_foods)
#добавили по блюду через метод append
foods.append('hot dog')
friend_foods.append('nachos')

print('Myfavourites foods is:')
print(foods)

print('My friend favourites foods is:')
print(friend_foods)