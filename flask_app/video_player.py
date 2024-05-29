import cv2 
import time 

class VideoPlayer:
    def __init__(self,  process_fucntion, path_to_video=''):
        if path_to_video:
            self.start_video(path_to_video)
        self.process_function = process_fucntion

    def start_video(self, path_to_video):
        self.cap = cv2.VideoCapture(path_to_video) 

    

    def get_frames(self, display_fps = True):
        while self.cap.isOpened():
            start_time = time.time()
            ret, frame = self.cap.read()

            if not ret:
                raise Exception('Видео не доступно')
            else:
                frame = self.process_function(frame, time.time()-start_time)
             
            compression_level = 100
            buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY, compression_level])[1]
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')    
            