from robotMotion import RobotMotion
from flask import Flask
app = Flask(__name__)
AA3000 = RobotMotion()
VERSION = 1.0

@app.route('/fwd')
def front():

    AA3000.forward(1)
    return "DONE\n"
    GPIO.cleanup()

@app.route('/bwd')
def back():

    AA3000.backwards(1)
    return "DONE\n"
    GPIO.cleanup()
@app.route('/lt')
def left():

    AA3000.right(1)
    return "DONE\n"
    GPIO.cleanup()
@app.route('/rt')
def right():

    AA3000.backright(1)
    return "DONE\n"
    GPIO.cleanup()
if __name__ == "__main__":
    app.run(debug=True, port = 8080, host= '192.168.1.108')
