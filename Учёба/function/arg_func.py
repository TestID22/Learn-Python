def changer (a, b): #в параметры функции передаются ссылки на объекты 
    a = 2 
    b[0] = 'lewis'
    b[1] = 'hamylton'

x = 22  # неизменяемы тип данных - целочисленное значение 
l = [1,2] # а список изменяемый тип

changer(x, l)
print(x, l) # поэтому вывод на экран покажет x = не изменился, а список l - изменится 

