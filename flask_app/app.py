from flask import Flask,render_template, Response 
from video_player import VideoPlayer
import video_process 
import os 

#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

app = Flask(__name__)

base_video = 'video/evening.mp4'
original_vp = VideoPlayer(process_fucntion=video_process.yolo, path_to_video=base_video)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    original_vp.start_video()
    new_frame = original_vp.get_frames()
    return Response(new_frame,mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
