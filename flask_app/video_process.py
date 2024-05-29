import time 
import cv2 

def original(frame):
    return frame

def original_with_avg_fps(frame, read_frame_time):
    pass

def original_with_fps(frame, read_frame_time):
    start = time.time()

    processing_time = read_frame_time+time.time()-start

    if  processing_time != 0:
        fps = 1/processing_time 
        fps = 'FPS:' + str(int(fps))
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(frame, fps, (7, 70), font, 1, (100, 255, 0), 3, cv2.LINE_AA) 

    return frame