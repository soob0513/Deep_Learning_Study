import cv2
from flask import Flask, Response, render_template

app = Flask(__name__)
camera = cv2.VideoCapture('videos/puppy.mp4')

def gen_frames():
    while True:
        # Capture frame-by-frame
        _, frame = camera.read()
        _, frame = cv2.cvtColor(camera, 127, 255, cv2.THRESH_BINARY)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        # frame concat
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_show')
def video_show():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__' : 
    app.run()