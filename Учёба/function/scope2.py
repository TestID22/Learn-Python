#Глобальная область
x = 99

def loc_scope(y):
    #локальная область видимости
    z = x + y
    return z

print(loc_scope(1))

#GLOBAL
num = 100
def loc_num():
    #LOCAL
    num = 10

loc_num()
print(num)