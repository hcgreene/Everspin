import time
import numpy as np
import RPi.GPIO as GPIO
from guizero import App, PushButton, Text
import threading
from pygame import mixer


# Raspberry Pi IP Address 10.160.137.201

from motor import motor
from light import light

#This file is the main program for the mindfullness wheel.
#It launches a GUI and then controls the movement of the motors and lights based on a distance sensor

#Flags
updating = False
motorsrunning = False

t = 0

message1 = "Thank you for carrying everything I couldn't. You've taken me farther than I ever imagined."
message2 = "You did the best you could with the understanding and tools you had then. Growth doesn't erase you; it honors you."
message3 = "I'm here with you. Let's take things one breath, one step at a time."
message4 = "It's okay to be a work in progress. Your present moments don't have to be perfect to be meaningful."
message5 = "I'm proud of you. The choices you're making now are building the life I get to enjoy."
message6 = "You don't need to predict the path. Just trust that you'll grow into the strength and clarity needed when the time comes."

audiofiles = {
    message1: 'message1.mp3',
    message2: 'message2.mp3',
    message3: 'message3.mp3',
    message4: 'message4.mp3',
    message5: 'message5.mp3',
    message6: 'message6.mp3'
}
mixer.init()

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

l = light(red, green, blue)
m = motor(a1i, a2i, b1i, b2i)
mtwo = motor(a1o, a2o, b1o, b2o)

trigger = 16
GPIO.setup(trigger, GPIO.OUT)

echo = 21
GPIO.setup(echo, GPIO.IN)

GPIO.output(trigger, 0)
time.sleep(2)

soundspeed = 343

#A series of functions that then call functions from the light and motor classes
#This allows for more easy interfacing with threading

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

#Start the threads for running the two motors and the LEDs and calls the wait_for_threads function
def activate(t1, t2, t3, message):
    mindfulness_message.value = "Wheels are turning"
    global t
    t = time.time()
    t1.start()
    t2.start()
    t3.start()
    threading.Thread(target=wait_for_threads, args=(t1, t2, t3, message)).start()

#How the wheel should behave when activated at the first height
#The first motor (inner) will rotate 10 times counter clockwise
#The second motor will rotate 5 times clockwise
#The duration is 30 seconds
#The LEDs will light up blue
def behavior1():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (5, 30,))
    t3 = threading.Thread(target=blue, args = ())

    activate(t1, t2, t3, message1)

#Second height
#Inner motor 5 times counter clockwise
#Outer motor 10 times clockwise
#Duration 30 seconds
#LEDs blue
def behavior2():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (10, 30,))
    t3 = threading.Thread(target=blue, args = ())

    activate(t1, t2, t3, message2)

#Third height
#Inner motor 5 times clockwise
#Outer motor 10 times counter clockwise
#Duration 30 secdonds
#LEDs green
def behavior3():
    t1 = threading.Thread(target=firstmotorclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (10, 30,))
    t3 = threading.Thread(target=green, args = ())

    activate(t1, t2, t3, message3)

#Fourth height
#Inner motor 10 times clockwise
#Outer motor 5 times counter clockwise
#Duration 30 seconds
#LEDs green
def behavior4():
    t1 = threading.Thread(target=firstmotorclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (5, 30,))
    t3 = threading.Thread(target=green, args = ())

    activate(t1, t2, t3, message4)

#Fifth height
#Inner motor 10 times clockwise
#Outer motor 5 times clockwise
#Duration 30 seconds
#LEDs red
def behavior5():
    t1 = threading.Thread(target=firstmotorclockwise, args = (10, 30,))
    t2 = threading.Thread(target=secondmotorclockwise, args = (5, 30,))
    t3 = threading.Thread(target=red, args = ())

    activate(t1, t2, t3, message5)

#Sixth height
#Inner motor 5 times counter clockwise
#Outer motor 10 times counter clockwise
#Duration 30 seconds
#LEDs red
def behavior6():
    t1 = threading.Thread(target=firstmotorcounterclockwise, args = (5, 30,))
    t2 = threading.Thread(target=secondmotorcounterclockwise, args = (10, 30,))
    t3 = threading.Thread(target=red, args = ())

    activate(t1, t2, t3, message6)

#Function to trigger the distance sensor and convert the time to distance based on the speed of sound
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

#Calls the getdistance function and determines if and how to activate the wheel
#Function loops using app.after to update every 500ms
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

#Manages the timing of the threads and updates the mindfulness message and lights after the wheel is done spinning
def wait_for_threads(t1, t2, t3, message):
    t1.join()
    t2.join()
    t3.join()
    duration = time.time()-t
    global motorsrunning
    global t
    motorsrunning = False
    mindfulness_message.value = message
    mixer.music.load(audiofiles[message])
    mixer.music.set_volume(0.7)
    mixer.music.play()
    l.off()
    mindfulness_message.value = "Welcome to Everspin"

#Stops the program from triggering the wheel based on the distance sensor. Distance is still measured
def stopupdating():
    global updating
    updating = False

#Starts the programs response to the distance sensor
def startupdating():
    global updating
    updating = True
    updatedistance()

#Runs GPIO.cleanup() and ends the program
def do_this_when_closed():
    #This should additionally export the CSV file
    GPIO.cleanup()
    app.destroy()

#Main code for the GUI of the program
app = App(title="Everspin")
button = PushButton(app, text="start", command=startupdating)
button = PushButton(app, text="stop", command=stopupdating)
mindfulness_message = Text(app, text="Welcome to Everspin", size=20)
app.when_closed = do_this_when_closed
app.display()
