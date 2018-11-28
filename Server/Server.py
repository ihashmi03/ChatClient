#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Created Successfully'
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    #with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
        #conn.close()
except socket.error as err:
    print 'socket creation failed with error %s' %(err)
finally:
    if conn:
        conn.close()
