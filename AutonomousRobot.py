#libraries
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import time
from Ultrasonic import Ultrasonic

from Motor import Motor 

minimumSensitivity = 0.35

leftMotor = Motor(24,23,25, minimumSensitivity,-1)
rightMotor = Motor(27,22,17, minimumSensitivity,-1)

frontSensor = Ultrasonic(5,26)
leftSensor  = Ultrasonic(6,13)
rightSensor = Ultrasonic(20, 21)

overall = 0.8
angle = 0
x = 0.36
while(True):
    dist = frontSensor.dis(15)
#    overall = (dist-25)/20+minimumSensitivity
 #   print("%5.1f %5.1f" % (dist, overall))
    x-=0.001
    overall = x
    print(x)
    leftMotor.setPower(overall-angle)
    rightMotor.setPower(overall+angle)

