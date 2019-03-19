elliot = ['Elliot Anderson', 31, 40000, 'Security']
darling = ['Darling', 34, 100, 'Hacker']

#print(elliot[0].split()[-1])
#darling[2] *= 1.10
#print(darling)

fsociety = [elliot, darling]
for people in fsociety:
    print(people[0].split()[-1])
    

for person in fsociety:
    person[2] *= 1.20
    print(people[2])
    
#работа генератора практика
pays = [person[2] for person in fsociety]
print(pays)

#map и лямбда - выражение
lambda_pays = map((lambda x: x[2],), person)

#функция sum 
sum_pays = sum(person[2] for person in fsociety)
print(sum_pays)

#Добавим Тирела
fsociety.append(['Tyller Wellick', 39, 100000,'Tech Dir'])
print(fsociety)

#функция len
print('Количество человек в Ф.обществе:', len(fsociety))