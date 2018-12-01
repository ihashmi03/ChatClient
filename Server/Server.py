#!/usr/bin/env python3
import socket, select, sys
from thread import *

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port 


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket Created Successfully'
    
    s.bind((HOST, PORT))
    
    s.listen(25)
    
    list_of_clients = []

    def recvthread(conn, addr):
        #send a greeting
        #conn.send('Welcome to this chat')
        while True:
            try:
                data = conn.recv(1024)
                if data:
                    sys.stdout.write("<" + addr[0] + "> " + data)
                    message_to_send = "<" + addr[0] + "> " + data 
                    broadcast(message_to_send, conn)
                else:
                    remove(conn)
            except:
                continue

    def sendthread(conn, addr):
        while True:
            try:
                serverresponse = sys.stdin.readline()
                if serverresponse:
                    conn.send('<Server> '+serverresponse) 
                    # sys.stdout.write("<You>") 
                    # sys.stdout.write(serverresponse) 
                    # sys.stdout.flush()
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

        start_new_thread(recvthread,(conn,addr))
        start_new_thread(sendthread,(conn,addr))

except socket.error as err:
    print 'socket creation failed with error %s' %(err)

conn.close()
s.close()
