#!/usr/bin/env python
# import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow camera to warm up
time.sleep(0.1)

# grab image from camera
camera.capture(rawCapture, format ="bgr")
image = rawCapture.array

# display image on screen and wait for a keypress
cv2.imshow("Image",image)
cv2.waitKey(0)
