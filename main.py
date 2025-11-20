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

def firstmotorclockwise(rotations, duration):
    m.rotatecw(rotations,duration)

def firstmotorcounterclockwise(rotations, duration):
    m.rotateccw(rotations, duration)

def secondmotor(rotations, duration):
    mtwo.rotateccw(rotations, duration)

def lights():
    l.lights()

def closedistance():
    t1 = threading.Thread(target=firstmotorclockwise, args = (2, 4,))
    #t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    #t2.start()
    t3.start()
    t1.join()
    #t2.join()
    t3.join()
    print('Done!')

def fardistance():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (2, 4,))
    #t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    #t2.start()
    t3.start()
    t1.join()
    #t2.join()
    t3.join()
    print('Done!')

def printwords():
    print("testing testing!")

def main():
    #This code needs to be reworked so that the GUI still works and responds to input
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
            
            if(distance < 0.25):
                print(f"close distance: {distance:.1f} m")
                closedistance()

            elif(distance < 0.5):
                print(f"medium distance: {distance:.1f} m")
                fardistance()


            time.sleep(.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

app = App(title="Everspin")
button = PushButton(app, text="start", image="everspin poster-2.png", command=main)
app.display()

#TODO need to update the GUI to have the picture and then have two separate buttons one to start and one to end the session and export the CSV