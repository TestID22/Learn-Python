from person_start import Person

elliot = Person('Elliot', 33, 40000)
darling = Person('Darling', 35, 1000)

fsociety = [elliot, darling]
for person in fsociety:
    print(person.name, person.pay)

x = [(person.name, person.pay)for person in fsociety] # генератором списков создадим данные 
print(x)

y = [rec.name for rec in fsociety if rec.age < 34] #sql подобный запрос
print(y)