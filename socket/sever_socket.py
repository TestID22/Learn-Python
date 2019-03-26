'''
Сервер - создаём объект сокета, передаём ему данные об IP и порт
биндим наши переменные
слушаем 1 запрос клиента

'''

from socket import *

myHost = 'localhost'
myPort = 9000

socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.bind((myHost, myPort))
socket_object.listen(1)

while True:
    connecetion, adress = socket_object.accept()#ждём запрос
    print(' server connect ', adress)

    while True:
        data = connecetion.recv(1024)
        if not data: break
        connecetion.send(b'Echo =>' + data)
    connecetion.close()