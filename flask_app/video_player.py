import cv2 
import time 
import threading
from imutils.video import FPS

          

class VideoPlayer:

    def __init__(self,  process_fucntion, path_to_video=0):
        #self.start_video(path_to_video)
        self.path_to_video = path_to_video
        self.process_function = process_fucntion
    
    def count_frames_per_second(self):
        while self.cap.isOpened():
            old_frame_cnt = self.frames_cnt
            time.sleep(1)
            current_frame_cnt = self.frames_cnt
            print(self.fps)
            self.fps = current_frame_cnt-old_frame_cnt

    def start_video(self):
        self.cap = cv2.VideoCapture(self.path_to_video)
        
        self.start = time.time()
        self.frames_cnt = 0

        self.fps = 0
        self.time_thread = threading.Thread(target=self.count_frames_per_second) 
        self.time_thread.start()

        print(self.cap.get(cv2.CAP_PROP_FPS))
    
   

    def display_fps(self,frame):
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(frame, f'Frames {self.frames_cnt}', (7, 170), font, 1, (200, 255, 0), 3, cv2.LINE_AA) 
        # cv2.putText(frame, f'Time {int(elapsed_time)//60}:{int(elapsed_time)%60}', (7, 70), font, 1, (200, 255, 0), 3, cv2.LINE_AA)
        cv2.putText(frame, f'FPS {self.fps}', (7, 40), font, 1, (200, 255, 0), 3, cv2.LINE_AA)

    
    def get_frames(self):

        while self.cap.isOpened():
            start_time = time.time()
            ret, frame = self.cap.read()
            


            if not ret:
                self.cap.release()
                return None
            else:
                frame = self.process_function(frame)
                self.frames_cnt += 1

                self.display_fps(frame)
                
                compression_level = 30
                buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY, compression_level])[1]
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
    
    
        