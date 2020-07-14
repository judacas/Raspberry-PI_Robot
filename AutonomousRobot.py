# Libraries
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import time
from Ultrasonic import Ultrasonic

from Motor import Motor 

minimumSensitivity = 0.35

leftMotor = Motor(24,23,25, minimumSensitivity)
rightMotor = Motor(27,22,17, minimumSensitivity)

overall = 0.8
angle = 0.2

while(true):
    leftMotor.setPower(overall-angle)
    rightMotor.setPower(overall+angle)
