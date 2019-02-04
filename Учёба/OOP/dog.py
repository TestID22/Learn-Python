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

print('Мою собаку зовут', dog_1.name.title())
print('Ей',dog_1.age)
dog_1.sit()
dog_1.rolling()
