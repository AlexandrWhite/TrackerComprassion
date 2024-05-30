import time 
import cv2 

def gray(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)
    return frame


def original(frame):
    return frame