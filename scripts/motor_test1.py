#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

duty_cycle = 6.70

pwm = GPIO.PWM(7,62.5)
pwm.start(7.05)
print('***Connect Battery & Press ENTER to start')
ctrl = raw_input()
pwm.ChangeDutyCycle(duty_cycle)
print('Starting...')

running = True
try:
    while running:
        pwm.ChangeDutyCycle(duty_cycle)
        ctrl = raw_input()
        if ctrl == 'u':
            duty_cycle = duty_cycle + 0.05
            print(duty_cycle)
        if ctrl == 'd':
            duty_cycle = duty_cycle - 0.05
            print(duty_cycle)
        if ctrl == 'q':
            running = False
finally:
    pwm.stop()
    
#print('***Press ENTER to quit')
#ctrl = raw_input()
pwm.stop()
GPIO.cleanup()
print('TURN THE SWITCH OFF!!!')
