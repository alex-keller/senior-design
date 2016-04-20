#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,62.5)
p.start(9.69) #1.55ms pulse width

try:
    while True:
        p.ChangeDutyCycle(9.69) #1.55ms
        print "9.69" #"Left"
        time.sleep(2.5)
        p.ChangeDutyCycle(8.13) #1.3ms
        print "8.13"  #Center"
        time.sleep(2.5)
        p.ChangeDutyCycle(6.56) #1.05ms pulse width
        print "6.56" #"Right"
        time.sleep(2.5)
        p.ChangeDutyCycle(8.13) #1.3ms
        print "8.13"  #Center"
        time.sleep(2.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
