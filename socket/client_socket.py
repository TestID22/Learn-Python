import sys 
from socket import *

serverHost = 'localhost'
serverPort = 9000

message = [b'Hello Server'] # Передаём сообщение нашему серверу в виде байтов "b' или str.encode

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sock_obj = socket(AF_INET, SOCK_STREAM)
sock_obj.connect((serverHost, serverPort))
for line in message:
    sock_obj.send(line)
    data = sock_obj.recv(1024)
    print('cleint recieved', data)
sock_obj.close()