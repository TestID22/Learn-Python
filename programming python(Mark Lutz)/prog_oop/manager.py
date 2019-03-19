from person_start import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1 + percent + bonus)

if __name__ == "__main__":
    tyrell = Manager('Tyrell Wellick', 36, 100000)
    tyrell.giveRaise(.20)
    #Класс Manager наследует от Person все методы, и атрибуты, и переопределяет метод
    #giveRaise - переопределяет, так как в области имён интерпретатор ведёт поиск снизу вверх
    print(tyrell.lastName() + ' Зарплатка ' + str(tyrell.pay))
