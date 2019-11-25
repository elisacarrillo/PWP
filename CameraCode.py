from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180

camera.start_preview()
for i in range(2):
    sleep(5)
    camera.capture('image%s.jpg' % i)

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

camera.stop_preview()
