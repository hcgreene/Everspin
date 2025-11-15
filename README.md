# Before, between, beyond: Everspin
Firmware for Everspin, a mindfulness wheel to help us overcome the anxiety that comes with the passing of time and big changes in life.

## Description
Everspin consists of an inner motor that represents the self and an outer motor that represents one's surroundings. RGB LEDs will signal activation of the device as well as the time period the user reflects on: past, present, or future. The device as a whole will be activated by voice using speech recognition programs. The code found in this repository is to be executed on a Raspberry Pi to control each of these components.

## Getting Started

### Dependencies
* Python 3.13.0
  * Libraries: RPi.GPIO, NumPy, time, guizero, threading

### Installing
Install main.py, motor.py, and light.py to the same directory. 

### Executing program
To use the program, run the main.py file. This will launch the GUI which has a button labeled 'move' which calls the functions in motor.py to rotate the motors.

The motor.py file is the driver for the stepper motors. It contains functions for rotating clockwise and counter clockwise.

The light.py file is the driver for the RGB LEDs. There are functions for turning the lights red, green, blue, and off.

## Authors

* Elisabeth Everhart [eeverhart@wm.edu]

* Hayden Greene [hcgreene@wm.edu]

* Kamila Miles [kmmiles@wm.edu]

## Changelog

* v0.1 (11/5/25)
  * Initial release, pseudo test code for motors and RGB LEDs
* v0.2 (11/12/25)
  * Added threading to rotate two motors and flash the LEDs simultaneously
  * Filled in pseudo code with GPIO pins (subject to change)
  * Created testing.py file to demonstrate control of all components with various test cases
