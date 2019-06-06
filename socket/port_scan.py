import socket
import msvcrt
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
portlist = [20,21,80,443]

def portScan(host, port):
    try:
        sock.connect((host,port))
        print("Port -" , port , "is opened")
    except ConnectionRefusedError:
        print("Port closed")
    except TimeoutError:
        print("Комп разъединяет Порт скорее всего Открыт.")

def allRange(host):
    for port in range(1, 255):
        try:
            if sock.connect((host,port)):
                print("Port -", port ," is opened")
        except ConnectionRefusedError:
            print("PORT - ",port ,"closed")
    
    
if __name__ == "__main__":
    print("1 - Press 1 for scan all ports")
    print("2 - Press 2 for change port")
    menu = msvcrt.getwch()
    flag = True
    while flag:
        if menu == "1":
            host = input("Введите хост: ") 
            allRange(host)
        elif menu == "2":
            host = input("Введите хост: ")
            port = int(input("Вdедите порт: "))
            portScan(host, port)
        else:
            flag = False

        

         


    