#!/usr/bin/env python3
import socket
import select
import sys
from thread import *

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Created Successfully'
    
    s.bind((HOST, PORT))
    
    s.listen(25)
    
    list_of_clients = []

    def groupthread(conn, addr):
        #send a greeting
        conn.send('Welcome to this chat')

        while True:
            try:
                data = conn.recv(1024)
                if data:
                    print "<" + addr[0] + "> " + data
                    #print data 
                    message = sys.stdin.readline() 
                    conn.send('<Server> '+message) 
                    sys.stdout.write("<You>") 
                    sys.stdout.write(message) 
                    sys.stdout.flush()
                    message_to_send = "<" + addr[0] + "> " + data 
                    broadcast(message_to_send, conn)

                else:

                    remove(conn)
                
            except:
                continue

    #broadcast function
    def broadcast(message, connection):
        for clients in list_of_clients:
            if clients!=connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    remove(clients)

    #function to remove clients
    def remove(connection):
        if connection in list_of_clients:
            list_of_clients.remove(connection)

    while True:

        conn, addr = s.accept()
        list_of_clients.append(conn)

        print addr[0] + ' connected'

        start_new_thread(groupthread,(conn,addr))
        
except socket.error as err:
    print 'socket creation failed with error %s' %(err)

conn.close()
s.close()
