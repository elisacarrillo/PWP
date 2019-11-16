from robotMotion import RobotMotion
from flask import Flask
#from communication import x
app = Flask(__name__)
AA3000 = RobotMotion()
VERSION = 1.0

@app.route('/fwd/<int:x>')
def front(x):

    AA3000.forward(x)
    return "DONE\n"
    

@app.route('/bwd/<int:x>')
def back(x):

    AA3000.backwards(x)
    return "DONE\n"
    
@app.route('/lt/<int:x>')
def left(x):

    AA3000.right(x)
    return "DONE\n"
    
@app.route('/rt/<int:x>')
def right(x):

    AA3000.backright(x)
    return "DONE\n"
    
if __name__ == "__main__":
    app.run(debug=True, port = 8080, host= '192.168.1.108')
