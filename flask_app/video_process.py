import time 
import cv2 

def gray(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_LINEAR)
    return frame


def original(frame):
    return frame

if __name__ == '__main__':
    import torch
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using device: {device}')
    print(torch.version.git_version)