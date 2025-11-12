import time
import numpy as np
import RPi.GPIO as GPIO
import threading

from motor import motor
from light import light

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

headers = ['inner motor direction', 'number of rotations', 'steps', 'period', 'outer motor direction', 'number of rotations', 'steps', 'period', 'duration']
data = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def firstmotor(rotations, duration):
    data[0] = 'CW'
    data[1] = rotations
    data[2] = rotations*200
    start = time.time()
    m.rotatecw(rotations,duration)
    end = time.time()
    duration = end-start
    data[8] = duration
    data[3] = duration/rotations

def secondmotor(rotations, duration):
    mtwo.rotateccw(rotations, duration)

def lights():
    time.sleep(0.5)
    l.red()
    time.sleep(2)
    l.green()
    time.sleep(2)
    l.blue()
    time.sleep(2)
    l.off()

def trythreading():
    t1 = threading.Thread(target=firstmotor, args = (5, 10,))
    t2 = threading.Thread(target=secondmotor, args = (8, 10,))
    t3 = threading.Thread(target=lights, args = ())

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('Done!')


def testmotor():
    start = time.time()
    m.rotateccw(5, 10)
    duration = time.time()-start
    print(duration)

def testleds():
    print("testing leds")
    l.red()
    time.sleep(2)
    l.green()
    time.sleep(2)
    l.blue()
    time.sleep(2)
    l.off()

#testmotor()
#trythreading()
lights()

GPIO.cleanup()