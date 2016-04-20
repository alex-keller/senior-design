#!/usr/bin/env python
import picamera
import time

cam = picamera.PiCamera()

cam.capture('image.jpg')

