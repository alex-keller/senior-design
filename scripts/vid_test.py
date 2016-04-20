#!/usr/bin/env python
import picamera
import time

cam = picamera.PiCamera()

cam.start_recording('sample.h264')
time.sleep(10)
cam.stop_recording()

