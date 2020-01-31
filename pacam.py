
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from cv2 import *

camera = PiCamera()
try:
    camera.start_preview()
    sleep(1)
    camera.capture('image.jpg')
    camera.stop_preview()
finally:
    camera.stop_preview()
width = 1280
height = 720
dim = (width, height)

# display the image on screen and wait for a keypress
k = cv2.resize(image, dim)
cv2.waitKey(0)
