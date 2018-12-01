#!/usr/bin/env python3
import socket, sys, select
from threading import Thread

#client for chat room

def send_msg(sock):
    while True:
        data = sys.stdin.readline()
        sock.send(data)
        if data.strip()=='exit':
            sock.send('User ending chat...GoodBye')
            sock.close()
            #sys.close()
            break

def recv_msg(sock):
    while True:
        stuff = sock.recv(1024)
        sys.stdout.write(stuff)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 65432)
sock.connect(server_address)
print("Connected to chat")
Thread(target=send_msg, args=(sock,)).start()
Thread(target=recv_msg, args=(sock,)).start()