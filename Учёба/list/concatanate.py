#Лёгкий код
friends = []
old_friend = ['Ellior', 'Tyrel', 'Darling']
while True:
    name = input('Введите имя друга:')
    if name:
        friends.append(name) 
        print('Твой друг ', name , 'добавлен в список' )
    else:
        break
print(friends)
for name in old_friend:
    name = old_friend.pop()
    friends.append(name)
print(friends)