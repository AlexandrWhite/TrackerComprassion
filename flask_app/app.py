from flask import Flask,render_template, Response 
from video_player import VideoPlayer
import video_process 

app = Flask(__name__)

base_video = 'video/test.mp4'

original_vp = VideoPlayer(process_fucntion=flask_app.video_process.original, 
                          path_to_video=base_video)

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
