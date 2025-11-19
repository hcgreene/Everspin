import time
import numpy as np
import RPi.GPIO as GPIO
from guizero import App, PushButton
import threading


# Raspberry Pi IP Address 10.160.137.201

from motor import motor
from light import light

#This file will be the main program for the mindfullness wheel. It will launch the GUI, control the motors, and control the microphone

a1i = 17
a2i = 27
b1i = 22
b2i = 23

a1o = 16 #no!
a2o = 26
b1o = 5
b2o = 6

red = 13
green = 25
blue = 12

l = light(red, green, blue)
m = motor(a1i, a2i, b1i, b2i)
mtwo = motor(a1o, a2o, b1o, b2o)

trigger = 16 #hopefully this doesn't cause problems
GPIO.setup(trigger, GPIO.OUT)

echo = 21
GPIO.setup(echo, GPIO.IN)

GPIO.output(trigger, 0)
time.sleep(2)

soundspeed = 343

def firstmotor(rotations, duration):
    m.rotatecw(rotations,duration)

def secondmotor(rotations, duration):
    mtwo.rotateccw(rotations, duration)

def lights():
    l.lights()

def motorsandlights():
    t1 = threading.Thread(target=firstmotor, args = (5, 10,))
    #t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    #t2.start()
    t3.start()
    t1.join()
    #t2.join()
    t3.join()
    print('Done!')

def main():
    try:
        while(True):
            GPIO.output(trigger, 1)
            for i in range(180):
                pass
            GPIO.output(trigger, 0)

            while(GPIO.input(echo) == 0):
                pass

            if(GPIO.input(echo) == 1):
                start = time.time()
                
            while(GPIO.input(echo) == 1):
                end = time.time()

            duration = end-start

            distance = soundspeed*duration/2 
            
            if(distance < 0.5):
                print(f"{distance:.1f} m {distance*100:.1f} cm {distance*1000:.1f} mm {distance*100*0.394:.1f} in")
                motorsandlights()
            time.sleep(.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

app = App(title="Everspin")
button = PushButton(app, text="clockwise", command=main)
app.display()