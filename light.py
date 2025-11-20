import RPi.GPIO as GPIO

from time import sleep

class light:
    frequency = 100
    s = 0.01

    def __init__(self, red, green, blue):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)

        self.r = GPIO.PWM(red, self.frequency)
        self.g = GPIO.PWM(green, self.frequency)
        self.b = GPIO.PWM(blue, self.frequency)

        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

        self.on = 'none'


    def off(self):
        #Check the self.on variable to see what is on currently and fade it off
        
        match self.on:
            case 'red':
                for i in range(100):
                    self.r.ChangeDutyCycle(100-i)
                    sleep(self.s)
            case 'green':
                for i in range(100):
                    self.g.ChangeDutyCycle(100-i)
                    sleep(self.s)
            case 'blue':
                for i in range(100):
                    self.b.ChangeDutyCycle(100-i)
                    sleep(self.s)

        self.r.ChangeDutyCycle(0)
        self.g.ChangeDutyCycle(0)
        self.b.ChangeDutyCycle(0)
        self.on = 'none' 
        #Ensure all of the lights are acutally off and update the self.on variable to reflect that they're all off
    
    def red(self):
        #make sure everything is off and then fade red in
        self.off()
        for i in range(100):
            self.r.ChangeDutyCycle(i)
            sleep(self.s)
        self.on = 'red'
    
    def green(self):
        #make sure everything is off and then fade green in
        self.off()
        for i in range(100):
            self.g.ChangeDutyCycle(i)
            sleep(self.s)
        self.on = 'green'
    
    def blue(self):
        #make sure everything is off and then fade blue in
        self.off()
        for i in range(100):
            self.b.ChangeDutyCycle(i)
            sleep(self.s)
        self.on = 'blue'

    def lights(self):
        sleep(0.5)
        self.red()
        sleep(0.5)
        self.green()
        sleep(0.5)
        self.blue()
        sleep(0.5)
        self.off()