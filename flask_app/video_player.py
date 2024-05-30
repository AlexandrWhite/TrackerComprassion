import cv2 
import time 
from imutils.video import FPS

class VideoPlayer:
    def __init__(self,  process_fucntion, path_to_video=0):
        self.start_video(path_to_video)
        self.process_function = process_fucntion

    def start_video(self, path_to_video=0):
        self.cap = cv2.VideoCapture(path_to_video)
        self.fps = FPS().start()
        self.start = time.time() 
        self.frames_cnt = 0 
        print(self.cap.get(cv2.CAP_PROP_FPS))
    
    def display_fps(self,frame):
        #frames_cnt = self.cap.get(cv2.CAP_PROP_POS_FRAMES)

        frames_cnt = self.frames_cnt
        elapsed_time = time.time()-self.start
        fps = frames_cnt/elapsed_time

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, f'Frames {frames_cnt}', (7, 170), font, 1, (200, 255, 0), 3, cv2.LINE_AA) 
        cv2.putText(frame, f'Time {int(elapsed_time)//60}:{int(elapsed_time)%60}', (7, 70), font, 1, (200, 255, 0), 3, cv2.LINE_AA)
        cv2.putText(frame, f'FPS {round(frames_cnt/elapsed_time)}', (7, 290), font, 1, (200, 255, 0), 3, cv2.LINE_AA)

    def get_frames(self):    
        while self.cap.isOpened():
            start_time = time.time()
            ret, frame = self.cap.read()

            if not ret:
                self.fps.stop()
                print("[INFO] elasped time: {:.2f}".format(self.fps.elapsed()))
                print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))
                return None
            else:
                frame = self.process_function(frame, time.time()-start_time)
                self.frames_cnt += 1
                self.display_fps(frame)


                compression_level = 100
                buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY, compression_level])[1]
                frame = buffer.tobytes()
                self.fps.update()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
    
    
        