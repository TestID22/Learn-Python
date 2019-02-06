class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometr = 0

    def full_info(self):
        full_name = ('\n Я езжу на ' + ' ' + self.make + ' ' + str(self.year) + ' года выпуска' 
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
            print('Чувак не хитри, оматать не выйдет!')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_car = Car('Mitsubishi','Outlander','2010')
print(my_car.full_info())
my_car.increment_odometr(30)
my_car.update_odometr(300)
my_car.show_odometr()

my_tesla = ElectricCar('tesla','model s', '2017')
print(my_tesla.full_info())