#Libraries
import RPi.GPIO as GPIO
import time
from Ultrasonic import Ultrasonic

sensor1 = Ultrasonic(18, 12)
sensor2 = Ultrasonic(2,21)
try:
    while True:
        dist = sensor1.dis(50)
        print ("OOOOOOOO  %.1f cm" % dist)
        time.sleep(0.5)
        dist = sensor2.dis(50)
        print ("          %.1f cm" % dist)
        time.sleep(0.5)

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

