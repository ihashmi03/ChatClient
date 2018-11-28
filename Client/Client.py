import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket()
s.connect((HOST,PORT))
print('Connected to Server')
s.sendall(b'Hello World!')
data = s.recv(1024)

print('Received', repr(data))