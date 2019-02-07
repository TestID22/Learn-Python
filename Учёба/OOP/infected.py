class Hero():
    def __init__(self, name, hero_type):
        self.name = name
        self.hero_type = hero_type

    def attack (self, enemy):
        print('Вы бьёте ')
        enemy.die()

class Infected():
    def __init__(self, name):
        self.name = name
        
    def die(self):
        print('Ты зачем меня убил?')

        