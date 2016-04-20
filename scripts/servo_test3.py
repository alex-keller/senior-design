#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) == 2:
    duty_cycle = float(sys.argv[1])
else:
    print "Error: no input duty_cycle arg"
    sys.exit()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)


p = GPIO.PWM(7,62.5)
p.start(duty_cycle) #1.3ms pulse width

try:
    while True:
        pass
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
