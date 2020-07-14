#Libraries
import RPi.GPIO as GPIO
import time
from Ultrasonic import Ultrasonic

sensor1 = Ultrasonic(2,3)
sensor2 = Ultrasonic(6,13)
sensor3 = Ultrasonic(20, 21)
try:
    while True:
        dist1 = sensor1.dis(50)
        time.sleep(0.25)
        dist2= sensor2.dis(50)
        time.sleep(0.25)
        dist3 = sensor2.dis(50)
        time.sleep(0.25)
        print (" %5.1f  %5.1f  %5.1f" % (dist1, dist2, dist3))

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
