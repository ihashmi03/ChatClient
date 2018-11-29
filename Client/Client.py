import socket
import select
import sys

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket()
s.connect((HOST,PORT))
print('Connected to Server')

while True:
    sockets_list = [sys.stdin, s]

    read_sockets,write_socket,error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == s:
            message = socks.recv(1024)
            print message
        else:
            message = sys.stdin.readline()
            s.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
s.close()