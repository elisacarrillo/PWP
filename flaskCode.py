from robotMotion import RobotMotion
from flask import Flask, request, send_from_directory
from picamera import PiCamera
from time import sleep
#from communication import x
app = Flask(__name__, static_url_path = '')
AA3000 = RobotMotion()
VERSION = 1.0

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/fwd/<int:x>')
def front(x):

    AA3000.forward(x)
    return "DONE\n"
    GPIO.cleanup()

@app.route('/bwd/<int:x>')
def back(x):

    AA3000.backwards(x)
    return "DONE\n"
    GPIO.cleanup()
@app.route('/lt/<int:x>')
def left(x):

    AA3000.right(x)
    return "DONE\n"
    GPIO.cleanup()
@app.route('/rt/<int:x>')
def right(x):

    AA3000.backright(x)
    return "DONE\n"
    GPIO.cleanup()
if __name__ == "__main__":
    app.run(debug=True, port = 8080, host= '192.168.1.108')
