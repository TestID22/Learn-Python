#Пример записи решения задачи о nonlocal функции в областях видимости
class Tester():
    def __init__(self, start): #__init__ конструктор объекта, вызывается при создании объектов класса
        self.state = start     # сохранение информации в новом объекте
    def nested(self, label):     #каждый раз когда вызывается метод, прибаляет +1 
        print(label , self.state)
        self.state += 1
        

f = Tester(2)  #СОЗДАСТ ОБЪЕКТ(экземляр класса Tester) вызовет __init__
f.nested('Два')


g = Tester(15)
g.nested('State')
g.nested('London')