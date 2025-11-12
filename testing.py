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
si = 0

a1o = 0
a2o = 0
b1o = 0
b2o = 0
so = 0

red = 26
green = 25
blue = 12

l = light(red, green, blue)
m = motor(a1i, a2i, b1i, b2i)
mtwo = motor(a1o, a2o, b1o, b2o)

def firstmotor(rotations, duration):
    m.rotatecw(rotations,duration)

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
    mtwo.rotateccw(5, 10)
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

testmotor()
#trythreading()