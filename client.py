"""client : 
1-handle send   =======> main process 
2-handle recieve =======> create thread """
from socket import *
import threading

def recive_thread (s):
    while True:
        x=s.recv(2048)
        print("server: " , x.decode("UTF-8"))

# create connection         
s=socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 7000
# client ask server for connection 
s.connect((host,port))
# when connect accepted client create thread for recieve and use main process for 
recive = threading.Thread(target=recive_thread,args=(s,))
recive.start()
while True:
    s.send(input("clinet: ").encode("UTF-8"))
s.close()
recive_thread.join()
