import time 
import cv2 

def gray(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame


def original(frame):
    return frame