#!/usr/bin/env python
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

if not( cap.isOpened() ):
	cap.open(0)

while(True):
	# capture frame-by-frame
	ret, frame = cap.read()
	print ret
	print cap.get(3)
	print cap.get(4)
	
	
	# operate on frame here
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# when done, release the capture
cap.release()
cv2.destroyAllWindows()
