from person_start import Person
from manager import Manager

elliot = Person('Elliot', 33, 40000)
darling = Person('Darling', 35, 1000)
tyrell = Manager ('Tyrell', 34, 100000)

fsociety = [elliot, darling, tyrell]
'''Полиморфизм Пояснение
Так как, метод в классе Manager переопределён на 0.2 кэф
то следовательно для Эллиота и Дарлин кэф будет 0.1
а для объектов класса Manager 0,2
'''
for i in fsociety:
    i.giveRaise(.10)
    print('Полиморфизм в действии')
    print(i.name, str(i.pay))