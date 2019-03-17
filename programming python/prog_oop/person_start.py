class Person():
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    
    def lastName(self):
        return self.name.split()[-1]
        
    def giveRaise(self, percent):
        self.pay *= (1 + percent)

if __name__ == "__main__":
    elliot = Person('Elliot Anderson', 33, pay=40000,job='CyberSecurity')
    darling = Person('Darling', 35, pay=1000,)
    print(elliot.name,darling.job)
    #Увеличим нищинскую зарплату Дарлин
    darling.giveRaise(.20)
    print(elliot.lastName())
    print(darling.pay)