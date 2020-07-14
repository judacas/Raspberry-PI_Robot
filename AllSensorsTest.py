#Libraries
import RPi.GPIO as GPIO
import time
from Ultrasonic import Ultrasonic

sensor1 = Ultrasonic(5,26)
sensor2 = Ultrasonic(6,13)
sensor3 = Ultrasonic(20, 21)
try:
    while True:
        dist1 = sensor1.distance()
        time.sleep(0.05)
        dist2= sensor2.distance()
        time.sleep(0.05)
        dist3 = sensor3.distance()
        time.sleep(0.05)
        print (" %5.0f  %5.0f  %5.0f" % (dist1, dist2, dist3))

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
