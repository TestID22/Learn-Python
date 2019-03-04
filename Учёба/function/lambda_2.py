def func():
    x = 7
    action = (lambda n: x + n) # запоминается x из лок.функ.
    
    return action

x = func()
print(x(2))

###########################
#Обращение из функции к глобальной переменной
num = 22
def tt():
    print(num)

tt()