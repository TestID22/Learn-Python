class Car():
    def __init__(self, name , make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year 
        self.odometr = 0

    def full_info(self):
        full_name = ('\n ' + self.name + ' ' + 'ездит на ' + ' ' + self.make + ' ' + str(self.year) + ' года выпуска' 
                        +' ' + self.model + ' модели.' )
        return full_name.title()
    
    def show_odometr(self):
        print('Пробег твоей каракатицы :', self.odometr)

    def increment_odometr(self, km):
        self.odometr += km

    def update_odometr (self, miles):
        if miles >= self.odometr:
            self.odometr = miles
        else:
            print('Чувак не хитри, отматать не выйдет!')
            
#Наследование от класса Car
class ElectricCar(Car):
    ''' тут атрибуты объекта электромобиля'''
    def __init__(self, name, make, model, year):
        ''' инициализация предка суперкласса'''
        super().__init__(name, make, model, year)
        self.battery = Battery()
        
#Класс Батареи 
class Battery():
    '''Простая модель батарейки - Тесломобилей(электрокаров)'''
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        '''Выводит информацию о мощности аккумулятора'''
        print('Мощность АКБ в машине на которой ездит '
                 +  ' ' + str(self.battery_size))
    
    def range (self):
        if self.battery_size == 70:
            print('Вы сможете проехать на ней 240 км')
        elif self.battery_size == 80:
            print('Вы сможете проехать на этой машине 300 км')


alex_tesla = ElectricCar('алекс','tesla x','model s','2017')
print(alex_tesla.full_info())
alex_tesla.battery.describe_battery()
alex_tesla.battery.range()