import cv2 
import time 
import threading
import time     

class VideoPlayer:

    def __init__(self,  process_fucntion, path_to_video=0):
        self.path_to_video = path_to_video
        self.process_function = process_fucntion
    
    def count_frames_per_second(self):
        while self.cap.isOpened():
            old_frame_cnt = self.frames_cnt
            time.sleep(1)
            current_frame_cnt = self.frames_cnt
            self.fps = current_frame_cnt-old_frame_cnt
            

    def start_video(self):
        self.cap = cv2.VideoCapture(self.path_to_video, cv2.CAP_FFMPEG)
        self.frames_cnt = 0

        self.start_time = time.time() 

        self.fps = 0
        self.time_thread = threading.Thread(target=self.count_frames_per_second) 
        self.time_thread.start()
    
   

    def display_fps(self,frame):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'FPS: {self.fps}', (7, 50), font, 1, (0, 0, 0), 10, cv2.LINE_AA)
        cv2.putText(frame, f'FPS: {self.fps}', (7, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    def display_videotime(self, frame):
        videofile_msec = self.cap.get(cv2.CAP_PROP_POS_MSEC)
        seconds = videofile_msec/1000
        font = cv2.FONT_HERSHEY_SIMPLEX
       
        cv2.putText(frame, f'Video time: {int(seconds//60)}:{int(seconds)%60}', (7, 100), font, 1, (0, 0, 0), 10, cv2.LINE_AA)
        cv2.putText(frame, f'Video time: {int(seconds//60)}:{int(seconds)%60}', (7, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    def display_realtime(self, frame):
        elapsed_time = (time.time() - self.start_time)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame, f'Real time: {int(elapsed_time)//60}:{int(elapsed_time)%60}', (7, 150), font, 1, (0, 0, 0), 10, cv2.LINE_AA)
        cv2.putText(frame, f'Real time: {int(elapsed_time)//60}:{int(elapsed_time)%60}', (7, 150), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    def get_frames(self):

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            
            if not ret:
                self.cap.release()
                return None
            else:
                frame = self.process_function(frame)
                self.frames_cnt += 1

                #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                self.display_fps(frame)
                self.display_realtime(frame)
                self.display_videotime(frame)

                compression_level = 80
                buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY, compression_level])[1]
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
    
    
        