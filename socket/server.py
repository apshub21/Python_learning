import socket

s= socket.socket()

print("Socket created")

s.bind(("LocalHost",9999))
s.listen(3)
print("waiting for connection")

while True:
    c , addr =s.accept()
    print("client connected" ,addr)
    print(bytes("Welcome to server","utf-8"))