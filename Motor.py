import RPi.GPIO as GPIO
class Motor(object) :
    def __init__(self, in1, in2, pwm, MP, sign):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm
        self.MP = MP
        self.sign = sign
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        self.p=GPIO.PWM(pwm,1000)
        self.p.start(50)
        print("motor Initialized")
        
    # Takes in a value between -1 and 1 inclusive. Where 1 is forward full speed and -1 is backwards full speed
    def setPower(self, power):
        power *= self.sign
        if abs(power) < self.MP:
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(0)

        elif power > 0:
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            self.p.ChangeDutyCycle(max(0,min(abs(power*(100-self.MP)+self.MP),100)))
        else:
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            self.p.ChangeDutyCycle(max(0,min(abs(power*(100-self.MP)-self.MP),100)))
