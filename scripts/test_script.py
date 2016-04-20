#!/usr/bin/env python
import RPi.GPIO as gpio 
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)

gpio.output(11,gpio.HIGH)
time.sleep(1)
gpio.output(11,gpio.LOW)
time.sleep(1)
gpio.cleanup()
print "ALL DONE"
 
