#Libraries
import RPi.GPIO as GPIO
import time
from Ultrasonic import Ultrasonic
import numpy as np
from PIL import Image

sensor = Ultrasonic(18, 12)
try:
    i = 0
    array = np.zeros([100,25], dtype=np.uint8)
    while True:
        dist = sensor.dis(50)
        if dist == 0:
           print("nothing found")
        else:
           if array[dist,0] <245:
               array[dist,:] +=10
           print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
    img = Image.fromarray(array)
    img.save('UltrasensorTest.png')
