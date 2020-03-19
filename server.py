"""  
server :
1- handle clients (accept connection )  =======> main process do that
2- handle send/recieve for each client  =======>create 2 threads for each client   """
# import socket lib used for client_server 
from socket import *
#import threading libraries  
from _thread import *
import threading
# to send and recieve at the the time we need two threads one for send and one for recieve 
def recive_thread(c,):   
    while True:
        x=c.recv (2048) # during session the recieve thread will recieve all the time
        print("client : ",x.decode("UTF-8"))

def client_thread (c):
    # create the other thread as recieve thread and make the first one as send thread
    reciev = threading.Thread (target=recive_thread,args=(c,))
    reciev.start()
    while True:
        c.send(input("server : ").encode("UTF-8")) # during the session the send thread will send all the time 


# creating server and configure session 
s=socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 7000
s.bind((host,port))
s.listen(5)
# server will remain waiting untill a client connect we use while loop to solve multi client at the same time 
while True:
    # when client connect server accept session and create a thread 
    #the other thread will be created automatically when the first one start
    c , ad = s.accept()
    print("connection form",ad[0])
    start_new_thread(client_thread,(c,))   # shortcut to create thread 
c.close()
recive_thread.join() 
