cars = ['lamba','bmw','mersedes-benz','audi']
for i in cars:
    if i == 'bmw':
        print('Вы нашли БМВ УРА:\n ',cars[1],'это новенькая e39')
    else:
        print('Это не беха а всего лишь:',i.upper())

#not , in 
banned = ['david','vanya']
user = ['marry']
if user not in banned:
    banned.append(user)
    print(user[0], 'забаннен, ура')
print(banned)
#условия в ветвлении IF - AND
user_age = str(input('введите ваш возраст'))
user = 100
if user_age > '18' and user_age > '21':
    print('Вам разрешенно ошиваться тут')

#изи задание для выполнения оператора IF
age = int(input('Сколько тебе лет'))
if age < 12:
    print('Вам бесплатно')
elif age < 18:
    print('5 баксов в кассу')
else:
    print('Гони полтишок')
