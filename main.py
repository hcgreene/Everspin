from time import sleep, time
import numpy as np
import RPi.GPIO as GPIO
from guizero import App, PushButton


# Raspberry Pi IP Address 10.160.137.201

from motor import motor
from light import light

#This file will be the main program for the mindfullness wheel. It will launch the GUI, control the motors, and control the microphone

#pin numbers for inner motor
a1i = 17
a2i = 27
b1i = 22
b2i = 23

a1o = 19
a2o = 13
b1o = 5
b2o = 6

red = 26
green = 25
blue = 12

innermotor = motor(a1i, a2i, b1i, b2i)
outermotor = motor(a1o, a2o, b1o, b2o)
l = light(red, green, blue)

def clockwise():
    print("Rotating")
    innermotor.rotatecw(3, 10)
    print("Done rotating?")

def counterclockwise():
    innermotor.rotateccw(3, 30)
    print("Rotating")
'''
app = App(title="Hello world")
button = PushButton(app, text="clockwise", command=clockwise)
button = PushButton(app, text="counter clockwise", command = counterclockwise())
app.display()
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
sleep(5)
GPIO.cleanup()

#clockwise()