name = 23
list = ["Тут Типо Привет", "Пошёл ты", name]


print(list[-1])

hello = input("Привет Путник " )
print (hello , " - рыцарь смерти")

cars = ["Honda","Nissan","BMW","Mersedes - Benz"]
print(hello + " хотел купить ", cars[-1])
#cars before adding список машин перед добовлением
print(cars)
#cars with replacment машина с заменой первого элемента
print("\t Добавим в начало списка Ауди")
cars[0] = "Audi"
print(cars)
#cars with adding append - method
print("\t Добавим в конец Мазду")
cars.append("Mazda")
print(cars)
#ДОБОВЛЯЕТ ЭЛЕМЕНТ В КОНКРЕТНОЕ МЕСТО СПИСКА
print("\t Добавим Масерати в конкретное место")

cars.insert(0, "Maseratti")
print(cars)

#своё пример кода my sample code - Goal
print('\t Пользовательский ввод - добавим в список')
chose_your_car = input("Ваша любимая марка Автомобиля")
cars.append(chose_your_car)
print(cars)
#удалим 5 элемент - Мазду
print('\t Удаляем Мазду ')
del cars[5]
print(cars)