
import RPi.GPIO as GPIO
from time import sleep


class RobotMotion:
    def __init__(self):
        # Motor A, RIGHT Side GPIO CONSTANTS
        self.ENA = 21  # ENA - H-Bridge enable pin
        self.IN1 = 26  # IN1 - Forward Drive
        self.IN2 = 19  # IN2 - Reverse Drive
        # Motor B, LEFT Side GPIO CONSTANTS
        self.ENB = 5  # ENB - H-Bridge enable pin
        self.IN3 = 13  # IN1 - Forward Drive
        self.IN4 = 20  # IN2 - Reverse Drive

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)

        self.rightMotor = GPIO.PWM(self.ENA, 6.75)
        self.leftMotor = GPIO.PWM(self.ENB, 6.75)

    def forward(self, time):
        self.rightMotor.start(54)
        self.leftMotor.start(45)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        sleep(time)

    def right(self, time):
        self.rightMotor.start(54)
        self.leftMotor.start(45)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        sleep(time)
    def backwards(self,time):
        self.rightMotor.start(54)
        self.leftMotor.start(45)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        sleep(time)

    def wait(self, time):
        self.rightMotor.start(0)
        self.leftMotor.start(0)
        sleep(time)

GPIO.cleanup()
AA3000 = RobotMotion()
AA3000.forward(1.65)
AA3000.wait(.6)
AA3000.right(.5)
AA3000.wait(.6)
AA3000.forward(1.7)
AA3000.wait(.6)
AA3000.backwards(1)

GPIO.cleanup()


