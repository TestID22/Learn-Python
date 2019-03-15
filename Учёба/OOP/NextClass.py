class NextClass():
    def printer(self, text):
        print(text)

x = NextClass()
x.printer('Привет')
#Прямой вызов метода класса через экземпляр x
NextClass.printer(x, 'Я робот')
