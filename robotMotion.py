#FINAL VERSION OF ROBOT MOVEMENT CODE
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

        self.rightMotor = GPIO.PWM(self.ENA, 1000)
        self.leftMotor = GPIO.PWM(self.ENB, 1000)

    # was 6

    def forward(self, time):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

        self.rightMotor.start(55.75)
        self.leftMotor.start(42.25)

        sleep(time)

        self.rightMotor.stop()
        self.leftMotor.stop()

    def right(self, time):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

        self.rightMotor.start(55.75)
        self.leftMotor.start(42.5)

        sleep(time)

        self.rightMotor.stop()
        self.leftMotor.stop()

    def backwards(self, time):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)

        self.rightMotor.start(55.75)
        self.leftMotor.start(42.25)

        sleep(time)

        self.rightMotor.stop()
        self.leftMotor.stop()

    def backright(self, time):  # right backwards left forward

        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)

        self.rightMotor.start(55.75)
        self.leftMotor.start(42.25)

        sleep(time)

        self.rightMotor.stop()
        self.leftMotor.stop()

    def wait(self, time):
        self.rightMotor.start(0)
        self.leftMotor.start(0)
        sleep(time)


