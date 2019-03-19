NAME, AGE, PAY = ['Elliot Anderson', 32, 40000]
#print(NAME,PAY) 

elliot = [['name','Ellot Anderson'],['age', 32],['pay',40000]]
darling = [['name','Darling'],['age', 35],['pay', 1000]]

fsociety = [elliot, darling]
#береём индексы и выводим имена и зарплату
for hackers in fsociety:
    print(hackers[0][1], hackers[2][1])

#генератор списков для всех имеён в списке fsociety
hackers_name = [name[0][1] for name in fsociety]
print(hackers_name)
