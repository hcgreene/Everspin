import time
import numpy as np
import RPi.GPIO as GPIO
from guizero import App, PushButton, Text
import threading


# Raspberry Pi IP Address 10.160.137.201

from motor import motor
from light import light

#This file will be the main program for the mindfullness wheel. It will launch the GUI, control the motors, and control the microphone

#Flags
updating = False
motorsrunning = False

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
    #mtwo.rotateccw(rotations, duration)
    pass

def lights():
    l.lights()

def closedistance():
    t1 = threading.Thread(target=firstmotorclockwise, args = (2, 4,))
    t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3)).start()
    print('Done!')

def fardistance():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (2, 4,))
    t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3)).start()
    print('Done!')

def printwords():
    print("testing testing!")

def getdistance():
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
    return distance

def updatedistance():
    if updating:
        distance = getdistance()
        distance_text.value = f"Distance: {distance} m"
        
        global motorsrunning
        if(not motorsrunning):
            if(distance < 0.25):
                print(f"close distance: {distance:.1f} m")
                motorsrunning = True
                closedistance()

            elif(distance < 0.5):
                print(f"medium distance: {distance:.1f} m")
                motorsrunning = True
                fardistance()

        app.after(500, updatedistance)


def wait_for_threads(t1, t2, t3):
    t1.join()
    t2.join()
    t3.join()
    global motorsrunning
    motorsrunning = False

def stopupdating():
    global updating
    updating = False

def startupdating():
    global updating
    updating = True
    updatedistance()

app = App(title="Everspin")
distance_text = Text(app, text="Distance: -- cm", size=20)
button = PushButton(app, text="start", command=startupdating)
button = PushButton(app, text="stop", command=stopupdating)
app.when_closed = lambda: GPIO.cleanup()
app.display()

#TODO need to update the GUI to have the picture and then have two separate buttons one to start and one to end the session and export the CSV