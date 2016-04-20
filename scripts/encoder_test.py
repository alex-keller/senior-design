#!/usr/bin/env python 
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

pinA = 27
pinI = 17

gpio.setup(pinI,gpio.IN)

time.sleep(0.25)

while gpio.input(pinI)==0:
	pulse_start = time.time()

print "First loop done"

while gpio.input(pinI)==1:
	pulse_end = time.time()

print "Stuff is happening"
gpio.cleanup() 
