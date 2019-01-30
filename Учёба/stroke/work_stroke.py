#Перебор строк из списка
list = ['Anton','Sergey','Alex','John','Snow']
for attack in list:
    #FUNC title() обявлет заглавную букву
    print(attack.title(),  " was ddos site")
    print("Police find hacker: ", attack.title() ,"\n")
print('Это был супер взлом')
print('Но полиция поймала всех')

squares = []
for value in range(1,11):
    squares.append(value**3)
print(squares)