#motor driver

#import RPi.GPIO as GPIO
from time import sleep

class motor:

    def __init__(self, a1, a2, b1, b2, s):
        #GPIO.setmode(GPIO.BCM)
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.s = s
        #GPIO.setup([a1, a2, b1, b2, s], GPIO.OUT)
        #GPIO.output([a1, a2, b1, b2], [0, 0, 0, 0])

    def cyclecw(self, wait):
        #This function does four steps 
        '''
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [1, 0, 0, 1])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [1, 0, 1, 0])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [0, 1, 1, 0])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [0, 1, 0, 1])
        sleep(wait)
        '''
        return

    def cycleccw(self, wait):
        '''
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [0, 1, 0, 1])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [0, 1, 1, 0])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [1, 0, 1, 0])
        sleep(wait)
        GPIO.output([self.a1, self.a2, self.b1, self.b2], [1, 0, 0, 1])
        sleep(wait)
        '''
        return

    def rotatecw(self, rotations, duration):
        for i in range(50*rotations):
            self.cyclecw(.01) #Need to go back to this and figure out how to calculate the wait time based on rotation and duration

    def rotateccw(self, rotations, duration):
        for i in range(50*rotations):
            self.cycleccw(.01) #Need to go back to this and figure out how to calculate the wait time based on rotation and duration
