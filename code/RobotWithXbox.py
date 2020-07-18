import RPi.GPIO as GPIO
GPIO.setwarnings(False)


import evdev
from evdev import InputDevice, categorize, ecodes

from multipledispatch import dispatch #allows for method overloading


# GPIO.cleanup()

class Motor(object) :
    def __init__(self, in1, in2, pwm, MP):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm
        self.MP = MP
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        self.p=GPIO.PWM(pwm,1000)
        self.p.start(50)
        print("motor Initialized")
        
    def setPower(self, power):
#         print(power)
        
        if abs(power) < minimumSensitivity:
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(0)
#             print("stop")
        elif power > 0:
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(max(0,min(abs(power*(100-self.MP)+self.MP),100)))
#             print("fwd")
        else:
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            self.p.ChangeDutyCycle(max(0,min(abs(power*(100-self.MP)-self.MP),100)))
#             print("bckwd")
        
               
               
minimumSensitivity = 0

leftMotor = Motor(24,23,25, 0)
rightMotor = Motor(27,22,17, 0)

gamepad = InputDevice('/dev/input/event2')

while(1):
    overall = (gamepad.absinfo(10).value - gamepad.absinfo(9).value)/gamepad.absinfo(9).max
    angle = (gamepad.absinfo(0).value - gamepad.absinfo(0).max/2)/gamepad.absinfo(0).max
    leftMotor.setPower(overall-angle)
    rightMotor.setPower(overall+angle)
    print(overall)

