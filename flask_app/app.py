from flask import Flask,render_template, Response 
from video_player import VideoPlayer
import video_process 

app = Flask(__name__)

base_video = 'video\\test2.mp4'

original_vp = VideoPlayer(process_fucntion=video_process.original_with_fps,
                          path_to_video=base_video)

original_vp = VideoPlayer(process_fucntion=video_process.original_with_fps)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    new_frame = original_vp.get_frames()
    return Response(new_frame,
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/lags', methods=['POST','GET'])
def lags():
    print('YOU CLICK')
    if original_vp.lags:
        original_vp.lags = False 
    else:
        original_vp.lags = True
    return ';',204

if __name__ == '__main__':
    app.run(debug=True)
