import socket
import cv2
import numpy as np
import time
import sys

HOST = socket.gethostname()
PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

while True:
   
    data = conn.recv(10000000*100000000)
    print(sys.getsizeof(data))
    frame = cv2.imdecode(data)
    print (frame)
    
    cv2.imshow('frame',frame)
    
