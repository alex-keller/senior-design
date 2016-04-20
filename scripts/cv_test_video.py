#!/usr/bin/env python
# from pyimagesearch.com
# import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
# resolution
X = 640
Y = 480

camera = PiCamera()
camera.resolution = (X, Y)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(X, Y) )

# warmup time
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then intiialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	# show the frame
	cv2.imshow("Frame",image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	
	# if 'q' key is pressed, break from the loop
	if key == ord("q"):
		break
