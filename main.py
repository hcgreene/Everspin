from time import sleep, time
import numpy as np
import RPi.GPIO as GPIO
from guizero import App, PushButton


# Raspberry Pi IP Address 10.160.137.201

from motor import motor

#This file will be the main program for the mindfullness wheel. It will launch the GUI, control the motors, and control the microphone

#pin numbers for inner motor
a1i = 0
a2i = 0
b1i = 0
b2i = 0
si = 0

innermotor = motor(a1i, a2i, b1i, b2i, si)

#pin numbers for outer motor
a1o = 0
a2o = 0
b1o = 0
b2o = 0
so = 0

outermotor = motor(a1o, a2o, b1o, b2o, so)

def move():
    innermotor.rotatecw(3, 30)
    outermotor.rotateccw(4, 30)
    print("Rotating")

app = App(title="Hello world")
button = PushButton(app, text="move", command=move)
app.display()