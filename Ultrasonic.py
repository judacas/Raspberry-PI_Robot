import RPi.GPIO as GPIO
import time
class Ultrasonic(object):
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def distance(self):
      # set Trigger to HIGH
        GPIO.output(self.trig, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
     
        StartTime = time.time()
        # save StartTime
        while GPIO.input(self.echo) == 0:
            
            if time.time()-StartTime > 0.001:
                return 0

        StartTime = time.time()
        # save time of arrival
        while GPIO.input(self.echo) == 1:
            
            if time.time()-StartTime > 0.023:
                return 0

        StopTime = time.time()
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = round(TimeElapsed * 17150)
 
        return distance

    def dis(self, accuracy):
        x = 0
        y = 0
        distances = [0] * accuracy
        while x<accuracy:
            distances[x] = self.distance()
            if distances[x] == 0:
                y+=1
                if y == accuracy:
                    return 0
            else:
                x+=1
        distances.sort()
        print(distances)
        return distances[round(accuracy/2)]
