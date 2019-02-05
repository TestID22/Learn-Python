class Car():
    def __init__(self, make, model, year):
        '''инициализирует параметры(атрибуты)'''
        self.make = make
        self.model = model
        self.year = year
    def information_about_my_car (self):
        '''Форматируем инфу о машине'''
        long_name = 'Я езжу на ' + self.make + ' модель: ' + self.model  + ' ' + str(self.year) + ' ' +'года!'
        return long_name.title()
        
my_car = Car('audi','a6','2016')
print(my_car.information_about_my_car())