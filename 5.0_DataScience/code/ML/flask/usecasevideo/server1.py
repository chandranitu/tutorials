import socket
import time
import cv2
import sys
import numpy as np
import output
capture = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 5050))

while True:
    ret, frame = capture.read()
    print (sys.getsizeof(frame))
    print (frame)
    cv2.imshow('frame',frame)
    sock.sendall(cv2.imencode(frame))
    
