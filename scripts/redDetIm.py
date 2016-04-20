#!/usr/bin/env python
# from http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# import packages
import numpy as np
import argparse
import cv2
# contruct the argument parse and parse the arguments!
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load image
image = cv2.imread(args["image"])

# define list of boundaries for each color BGR
boundaries = [
	([1, 1, 100], [50, 56, 255]),		# red
#	([86, 31, 4], [220, 88, 50]),]		# blue
#	([25, 146, 190], [62, 174, 250]),	# yellow
#	([103, 86, 65], [145, 133, 128]),	# gray
    ]
#print boundaries
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	print lower
	upper = np.array(upper, dtype = "uint8")
	print upper
	
	# find the colors within the specified boundaries and apply the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	imSave = np.hstack([image, output])
	cv2.imwrite("stopSignDetected.jpg", imSave)
    
    # show the images
    #Create a window for display.
	cv2.namedWindow( "Color Detect", cv2.WINDOW_NORMAL)
	cv2.imshow("Color Detect", np.hstack([image, output]))
	cv2.waitKey(0)

