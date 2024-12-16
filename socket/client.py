import socket

c= socket.socket()

c.connect(("LocalHost",9999))

print(c.recv(1024).decode())