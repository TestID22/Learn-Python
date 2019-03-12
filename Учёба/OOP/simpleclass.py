class FirstClass():
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Текущее значение:"%s"' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other


x = FirstClass()
y = FirstClass()
#объект z (экземпляр) унаследовал от FirstClass метод setdata
z = SecondClass()
#
z.setdata('42')

#Создаём третий объект
a = ThirdClass('Abc')
a.display()
print(a)
#__str__ передаёт объекту возможность строчного типа данных
b = a + 'xyz'
print(b)
#mul изменяет сам объект
a.mul(3)
print(a)

x.setdata('Don Juan Matus')
y.setdata(23)

x.display()
y.display()

z.display()

x.data = 12
x.display()
