import cv2
import torch 
from ultralytics import YOLO 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('detection_models/yolov8n.pt').to(device)


def gray(frame):
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgsz = 320
    #frame = cv2.resize(frame, (imgsz, imgsz), interpolation=cv2.INTER_LINEAR)
    results = model.predict(frame, verbose=False, classes=[2,3,5,7], imgsz=imgsz)

    #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame = results[0].plot()

    return frame



def original(frame):
    return frame

if __name__ == '__main__':
    print(f'Using device: {device}')