import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger = 3
GPIO.setup(trigger, GPIO.OUT)

echo = 22
GPIO.setup(echo, GPIO.IN)

GPIO.output(trigger, 0)
time.sleep(2)

soundspeed = 343

while(True):
    GPIO.output(trigger, 1)
    time.sleep(.000001)
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
    time.sleep(.5)


    
