import socket,subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.106", 8081))
result = s.recv(1024)
print("Message", result.decode("utf-8"))
subprocess.call("cmd")
s.close()
