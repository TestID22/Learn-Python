import os, sys

print (len(dir(sys)))
print (len(dir(os)))

fobj = open('www.txt', 'wb')#функция open даёт нам интерфейс(функций) 
                            #для взаимодействия с файловой системой 