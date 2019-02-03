#Начинаем с двух списков пользователей для проверки
#и пустого списка с проверенными пользователями 

unconfirmed_user = ['alex','alice','elliot']
confirmed_user = []

#Проверяем пользователей, пока остаются непроверенные 
#пользователи. Каждый проверенный пользователь, 
#перемещается в проверенный список пользователей.
while unconfirmed_user:
    curent_users = unconfirmed_user.pop()

    print('Проверенный юзер', curent_users.title())
    confirmed_user.append(curent_users)

#вывод всех проверенных пользователей
print('Были проверены:')
for user in confirmed_user:
    print(user.title())