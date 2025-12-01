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

message1 = "Thank you for carrying everything I couldn't. You've taken me farther than I ever imagined."
message2 = "You did the best you could with the understanding and tools you had then. Growth doesn't erase you; it honors you."
message3 = "I'm here with you. Let's take things one breath, one step at a time."
message4 = "It's okay to be a work in progress. Your present moments don't have to be perfect to be meaningful."
message5 = "I'm proud of you. The choices you're making now are building the life I get to enjoy."
message6 = "You dono't need to predict the path. Just trust that you'll grow into the strength and clarity needed when the time comes."

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

def secondmotorclockwise(rotations, duration):
    mtwo.rotatecw(rotations, duration)

def secondmotorcounterclockwise(rotations, duration):
    mtwo.rotateccw(rotations, duration)

def lights():
    l.lights()

def red():
    l.red()

def green():
    l.green()

def blue():
    l.blue()

def closedistance():
    t1 = threading.Thread(target=firstmotorclockwise, args = (2, 4,))
    t2 = threading.Thread(target=secondmotorcouterclockwise, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3)).start()
    print('Done!')

def fardistance():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (2, 4,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3)).start()
    print('Done!')

#Start the threads for running the two motors and the LEDs
def activate(t1, t2, t3):
    mindfulness_message.value = "Wheels are turning"
    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3)).start()

#How the wheel should behave when activated at the first height
#The first motor (inner) will rotate 10 times counter clockwise
#The second motor will rotate 5 times clockwise
#The duration is 30 seconds
#The LEDs will light up blue
def behavior1():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (5, 30,))
    t3 = threading.Thread(target=blue, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message1

#Second height
#Inner motor 5 times counter clockwise
#Outer motor 10 times clockwise
#Duration 30 seconds
#LEDs blue
def behavior2():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (10, 30,))
    t3 = threading.Thread(target=blue, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message2

#Third height
#Inner motor 5 times clockwise
#Outer motor 10 times counter clockwise
#Duration 30 secdonds
#LEDs green
def behavior3():
    t1 = threading.Thread(target=firstmotorclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (10, 30,))
    t3 = threading.Thread(target=green, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message3

#Fourth height
#Inner motor 10 times clockwise
#Outer motor 5 times counter clockwise
#Duration 30 seconds
#LEDs green
def behavior4():
    t1 = threading.Thread(target=firstmotorclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (5, 30,))
    t3 = threading.Thread(target=green, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message4

#Fifth height
#Inner motor 10 times clockwise
#Outer motor 5 times clockwise
#Duration 30 seconds
#LEDs red
def behavior5():
    t1 = threading.Thread(target=firstmotorclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (5, 30,))
    t3 = threading.Thread(target=red, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message5

#Sixth height
#Inner motor 5 times counter clockwise
#Outer motor 10 times counter clockwise
#Duration 30 seconds
#LEDs red
def behavior6():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (10, 30,))
    t3 = threading.Thread(target=red, args = ())

    activate(t1, t2, t3)
    mindfulness_message.value = message6

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
        
        global motorsrunning
        if(not motorsrunning):
            if(distance < 0.147):
                print("behavior 1")
                motorsrunning = True
                behavior1()

            elif(distance < 0.194):
                print("behavior 2")
                motorsrunning = True
                behavior2()
            
            elif(distance < 0.241):
                print("behavior 3")
                motorsrunning = True
                behavior3()

            elif(distance < 0.288):
                print("behavior 4")
                motorsrunning = True
                behavior4()

            elif(distance < 0.335):
                print("behavior 5")
                motorsrunning = True
                behavior5()

            elif(distance < 0.382):
                print("behavior 6")
                motorsrunning = True
                behavior6()

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
button = PushButton(app, text="start", command=startupdating)
button = PushButton(app, text="stop", command=stopupdating)
mindfulness_message = Text(app, text="Welcome to Everspin", size=20)
app.when_closed = lambda: GPIO.cleanup()
app.display()

#TODO need to update the GUI to have the picture and then have two separate buttons one to start and one to end the session and export the CSV
