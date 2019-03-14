class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job 
        self.pay = pay
    def secondName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        return int(self.pay * (1 + percent))
    def __str__(self):
        #тут могла бы быть ваша реклама
        return 'Члены fsociety: %s, Должность:%s, Зарплата: %s' %(self.name ,self.job, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
        

        


if __name__ == "__main__":
    darling = Person('Darling',pay=100)

    elliot = Person('Elliot Anderson', job='Engineer', pay=40000)

    tyrell = Manager('Tyrell Wellick','Tech Dir',100000)
    for i in (darling, elliot, tyrell):
        i.giveRaise(.10)
        print(i)


#split разбивает строку в список по пробелам
print('Фамилия сотрудника:', elliot.secondName())
print('Поднимем зарплату на 10%: ', elliot.giveRaise(.10))
tyrell.giveRaise(.10)
darling.giveRaise(10)
#print(darling.name, darling.pay)
#print(elliot.name, elliot.pay)
print('Заработная плата сотрудника с учётом giveRaise', elliot.pay)

print(darling)
print(elliot)
print(tyrell)