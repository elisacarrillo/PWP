
import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()

# ///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, RIGHT Side GPIO CONSTANTS
ENA = 21  # ENA - H-Bridge enable pin
IN1 = 26  # IN1 - Forward Drive
IN2 = 19  # IN2 - Reverse Drive
# Motor B, LEFT Side GPIO CONSTANTS
ENB = 5  # ENB - H-Bridge enable pin
IN3 = 13  # IN1 - Forward Drive
IN4 = 20  # IN2 - Reverse Drive



GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)

p = GPIO.PWM(ENA,7)
p2 = GPIO.PWM(ENB,7)

p.start(54)
p2.start(45)

class RobotMotion:
    def __init__(self, time):
        self.time = time
    def forward(self):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        sleep(self.time)


twoForward = RobotMotion(1.95)
twoForward.forward()

GPIO.cleanup()
