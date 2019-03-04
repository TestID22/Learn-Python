x = 100
#функция glob превращает переменную x в глобальную 
def glob():
    #теперь переменная x ссылается на x за пределами функции
    global x
    x = 99

glob()
print(x)
#################################################
z, y  = 1, 2

def glob_z():
    global w
    w = z + y

glob_z()
print(w)
###################################################
x = 99

def func_1():
    global x
    x = 100

def func_2():
    global x
    x = 1

func_2()
print(x)
func_1()
print(x)