#
users = ['admin','eric','oliver','lars','jimmy']

for user in users:
    if user == 'admin':
        print('Hello Админастратор ', users[0])
    elif user == 'eric':
        print('Heloу мазифака по имени', user)
    elif user == 'oliver':
        print('Heloу мазифака по имени', user)
    elif user == 'lars':
        print('Heloу мазифака по имени', user)
    


#Таск 2
users = []

if users:
    print('Добавим юзера')
else:
    print('Так нет никого')

#Task 3 перербираем элементы одного в другом, если совпадают то True принтуем, остальных на выход else
curent_user = ['admin','eric','oliver','lars','jimmy']
new_user = ['admin','ant','legolas','gimly','lars']

for user in new_user:
    if user in curent_user:
        print('Такое тело есть', user)
    else:
        print('Этих бичей нету', user)

#task 4 with numbers

num = list(range(1,10))

for i in num:
    if i == 1:
        print(i,"st")
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    else:
        print(str(i) + 'th')

print(type(num))