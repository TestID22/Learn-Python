class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job 
        self.pay = pay
    def secondName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        return int(self.pay * (1 + percent))


        
if __name__ == "__main__":
    darling = Person('Darling')
    elliot = Person('Elliot Andersen', job='Engineer',pay=40000)
#split разбивает строку в список по пробелам
print('Фамилия сотрудника:', elliot.secondName())
print('Поднимем зарплату на 10%', elliot.giveRaise(.10))
print(darling.name, darling.pay)
print(elliot.name, elliot.pay)
print('Заработная плата сотрудника с учётом giveRaise', elliot.pay)

