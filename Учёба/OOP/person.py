class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job 
        self.pay = pay
        

darling = Person('Darling')
elliot = Person('Elliot', job='Engineer',pay='40 000')

print(darling.name, darling.pay)
print(elliot.name, elliot.pay)


