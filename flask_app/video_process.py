import cv2
import torch 
from ultralytics import YOLO 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('detection_models/yolov8n.pt').to(device)
model.fuse()

def yolo(frame):
    imgsz = 320
    results = model.predict(frame, verbose=False, classes=[2,3,5,7], imgsz=imgsz)
    frame = results[0].plot()
    return frame

def original(frame):
    return frame

from .trackers.UCMCTrack.demo import Detection
from .trackers.UCMCTrack.demo import Detector 
detector = Detector()
detector.load()

def ucmc_tracker(frame):
    

    imgsz = 320
    results = model(frame, verbose=False, classes=[2,3,5,7], imgsz=imgsz)


if __name__ == '__main__':
    print(f'Using device: {device}')