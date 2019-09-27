
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.IN)
# ///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 21  # ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 26  # IN1 - Forward Drive
REVERSE_LEFT_PIN = 19  # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 5  # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = GPIO.PWM(PWM_DRIVE_LEFT, 1000)
driveRight = GPIO.PWM(PWM_DRIVE_RIGHT, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = GPIO.OUTPUT(FORWARD_LEFT_PIN, GPIO.IN)
reverseLeft = GPIO.PWM(REVERSE_LEFT_PIN, 1000)
forwardRight = GPIO.OUTPUT(FORWARD_RIGHT_PIN, GPIO.IN)


# reverseRight = GPIO.PWM(REVERSE_RIGHT_PIN,1000)


# def allStop():
#     forwardLeft.value = False
#     reverseLeft.value = False
#     forwardRight.value = False
#     reverseRight.value = False
#     driveLeft.value = 0
#     driveRight.value = 0

def forwardDrive(x):

    forwardRight.start(x)
    driveRight.start(x)

    sleep(5)
# driveLeft.start(1)
#
#
# forwardLeft.start(1)
# forwardRight.start(1)


# def reverseDrive():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 1.0
#     driveRight.value = 1.0

# def spinLeft():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = True
#     reverseRight.value = False
#     driveLeft.value = 1.0
#     driveRight.value = 1.0

# def SpinRight():
#     forwardLeft.value = True
#     reverseLeft.value = False
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 1.0
#     driveRight.value = 1.0

# def forwardTurnLeft():
#     forwardLeft.value = True
#     reverseLeft.value = False
#     forwardRight.value = True
#     reverseRight.value = False
#     driveLeft.value = 0.2
#     driveRight.value = 0.8

# def forwardTurnRight():
#     forwardLeft.value = True
#     reverseLeft.value = False
#     forwardRight.value = True
#     reverseRight.value = False
#     driveLeft.value = 0.8
#     driveRight.value = 0.2

# def reverseTurnLeft():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 0.2
#     driveRight.value = 0.8

# def reverseTurnRight():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value =s True
#     driveLeft.value = 0.8
#     driveRight.value = 0.2
forwardDrive(5)

def main():
    # allStop()
    forwardDrive(5)
    sleep(5)

main()
# reverseDrive()
# sleep(5)
# spinLeft()
# sleep(5)
# SpinRight()
# sleep(5)
# forwardTurnLeft()
# sleep(5)
# forwardTurnRight()
# sleep(5)
# reverseTurnLeft()
# sleep(5)
# reverseTurnRight()
# sleep(5)
# allStop()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
