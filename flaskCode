from robotMotion import RobotMotion
from flask import Flask
app = Flask(__name__)
AA3000 = RobotMotion()
VERSION = 1.0

@app.route('/')
def ver_top():
    return "Hello World {}\n".format(VERSION)
@app.route('/fwd')
def good_bye():
    AA3000.forward()
    return "goodbyr \n<br>"

if __name__ == "__main__":
    app.run()
