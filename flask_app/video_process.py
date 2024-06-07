import cv2
import torch 
from ultralytics import YOLO 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('detection_models/yolov8m.pt').to(device)
model.fuse()

def botsort(frame):
    imgsz = 320
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.track(frame, tracker='botsort.yaml', verbose=False, classes=[2,3,5,7], imgsz=imgsz, device='gpu')
    frame = results[0].plot()
    return frame

def bytetrack(frame):
    imgsz = 320
    results = model.track(frame, tracker='bytetrack.yaml', verbose=False, classes=[2,3,5,7], imgsz=imgsz, device='gpu')
    frame = results[0].plot()
    return frame


from flask_app.trackers.sort.sort import Sort 


def original(frame):
    return frame



def ucmc_tracker(frame):
    imgsz = 320
    results = model(frame, verbose=False, classes=[2,3,5,7], imgsz=imgsz)


if __name__ == '__main__':
    print(f'Using device: {device}')