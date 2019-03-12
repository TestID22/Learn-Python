class FirstClass():
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Текущее значение:"%s"' % self.data)


x = FirstClass()
y = FirstClass()
#объект z (экземпляр) унаследовал от FirstClass метод setdata
z = SecondClass()
#
z.setdata('42')

x.setdata('Don Juan Matus')
y.setdata(23)

x.display()
y.display()

z.display()

x.data = 12
x.display()
