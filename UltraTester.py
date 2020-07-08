#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 12
accuracy = 10
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
print("code Started")
time.sleep(2)
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        
        if time.time()-StartTime > 0.001:
            return 0

    StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        
        if time.time()-StartTime > 0.023:
            return 0

    StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = round(TimeElapsed * 17150)
 
    return distance

def dis(accuracy):
    x = 0
    y = 0
    distances = [0] * accuracy
    while x<accuracy:
        distances[x] = distance()
        if distances[x] == 0:
            y+=1
            if y == accuracy:
                return 0
        else:
            x+=1
    distances.sort()
    print(distances)
    return distances[round(accuracy/2)]

 
try:
    while True:
        dist = dis(50)
        if dist == 0:
           print("nothing found") 
        else:
           print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

