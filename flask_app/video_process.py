import cv2
import torch 
from ultralytics import YOLO 
import numpy as np 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO('detection_models/yolov8m.pt').to(device)
model.fuse()

def botsort(frame):
    imgsz = 320
    results = model.track(frame, tracker='botsort.yaml', verbose=False, classes=[2,3,5,7], imgsz=imgsz, device='gpu')
    frame = results[0].plot()
    return frame

def bytetrack(frame):
    imgsz = 320
    results = model.track(frame, tracker='bytetrack.yaml', verbose=False, classes=[2,3,5,7], imgsz=imgsz, device='gpu')
    frame = results[0].plot()
    return frame


import staff
from trackers.sort.sort import Sort 
sort_tracker = Sort(max_age=20, min_hits=8, iou_threshold=0.50)

import supervision as sv 
label_annotator = sv.LabelAnnotator()

def sort(frame):
    imgsz = 320
    results = model.predict(frame, verbose=False, classes=[2,3,5,7], imgsz=imgsz, device='gpu')
    det_list = staff.get_results(results)

    if len(det_list) == 0:
        det_list = np.empty((0,5))

    res = sort_tracker.update(det_list)
    boxes_track = res[:,:-1]
    boxes_ids = res[:,-1].astype(int)        

    frame = staff.draw_bounding_boxes_with_id(frame, boxes_track, boxes_ids)

    return frame

def original(frame):
    return frame




if __name__ == '__main__':
    print(f'Using device: {device}')