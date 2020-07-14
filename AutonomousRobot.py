#libraries
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import time
from Ultrasonic import Ultrasonic

from Motor import Motor 

mp = 0.3 #minimum Power

# set up motors
leftMotor = Motor(24,23,25, mp,-1)
rightMotor = Motor(27,22,17, mp,-1)

# set up sensors
frontSensor = Ultrasonic(5,26)
leftSensor  = Ultrasonic(6,13)
rightSensor = Ultrasonic(20, 21)


overall = 0
while(True):
    dist = frontSensor.dis(15)
    overall = (dist-50)/50
    print("%5.1f %5.1f" % (dist, overall))
    leftMotor.setPower(overall)
    rightMotor.setPower(overall)
