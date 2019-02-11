class Dog():
    '''Создаём класс собаки'''
    def __init__(self, name, age):
        '''инициализирует атрибуты собачие'''
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title(), 'сидит')
    def rolling(self):
        print(self.name.title(),'кувыркается')
        

dog_1 = Dog('jess','12')
dog_2 = Dog('Adelle','8')

print(dog_2.name)

