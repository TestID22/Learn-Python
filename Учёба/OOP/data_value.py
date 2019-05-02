class FirstClass():
    def __init__(self, name):
        self.name = name 
    def set_data(self, data):
        self.data = data
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Curent value %s еее' % self.data) #вставка в страку данных по средствам %s



x = FirstClass('Garry')
y = SecondClass('Hammy')
y.set_data('Хелоу')
y.display()
#Передаём значение вне класса
x.data = 'Ку'
x.display()
#Передаём значение через метод класса
x.set_data('Привет' + ' ' + x.name) # конкатенация не считается аргументом, ведь это просто \
#склеивание строк
x.display()

