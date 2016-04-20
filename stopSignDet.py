#!/usr/bin/env python
# using code from http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# import packages
import numpy as np
import argparse
import cv2

# create display window for testing
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# build ideal octagon
octagon = [np.array([[653,130], \
    [347,130], \
    [130,347], \
    [130,653], \
    [347,870], \
    [653,870], \
    [870,653], \
    [870,347]], dtype=np.int32)]
octagon = sorted(octagon, key = cv2.contourArea, reverse = True)[:10]
#print octagon
#cv2.waitKey(0)

# create black image and show contours
ideal = np.zeros([1000, 1000], np.uint8)
for cnt in octagon:
    _octagon = [cnt]

# approximate the contour so it has the same format as the test contour
# oct is the contour against which to compare
cv2.drawContours(ideal,octagon,-1,(255,255,255),2)
# just need to make it, don't need to show it
#cv2.imshow("image", ideal)
#cv2.waitKey(0)

# get contour points
im2, octagonContour, hierarchy = cv2.findContours(ideal.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
octagonContour= sorted(octagonContour, key = cv2.contourArea, reverse = True)[:10]
#for i in contours:
#print contours
# pick the biggest (by area) contour
oct = octagonContour[0]
# dont print or wait
#print oct
#cv2.waitKey(0)

# select input image
# contruct the argument parse and parse the arguments!
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load image
image = cv2.imread(args["image"])
#print args["image"]
# define list of boundaries for each color BGR
boundaries = [
	([0, 0, 100], [77, 77, 255]),		# red
#	([86, 31, 4], [220, 88, 50]),]		# blue
#	([25, 146, 190], [62, 174, 250]),	# yellow
#	([103, 86, 65], [145, 133, 128]),	# gray
    ]
#print boundaries
# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
#    print lower
    upper = np.array(upper, dtype = "uint8")
#    print upper
    
    # find the colors within the specified boundaries and apply the mask
    # make gray scale version of found color and threshold to B&W
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

z,bw = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#print z
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", bw)
cv2.waitKey(0)

# some morphological operations
kernel = np.ones((3,3), np.uint8)
bwMorph = bw
# could replace with a close operation
bwMorph = cv2.dilate(bwMorph, kernel, iterations = 1)
bwMorph = cv2.erode(bwMorph, kernel, iterations = 1)
edges = cv2.Canny(bwMorph, 50, 200)
# dont show edges
cv2.imshow("image", edges)
cv2.waitKey(0)

# get contour points from edge map
im2, contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
#for i in contours:
#print contours
# pick the biggest (by area) contour
cnt = contours[0]
#M = cv2.moments(cnt)
#print M
# approximate the contour. gets rid of jagged edges. adjust epsilon as needed
epsilon = 0.02*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
# dont print or show
#print approx
cv2.drawContours(image, approx, -1, (0,255,0), 3)
cv2.imshow("image", image)
cv2.imwrite("test_" + args["image"], image)
cv2.waitKey(0)

# match shape to ideal octagon
match = cv2.matchShapes(oct, approx, 1, 0)
# collect several match quantities - [0,1]; 0 is closer match, 1 is not match
# need to develop threshold for correct match
print match

# maybe try for speed
# get convex hull


#cv2.imwrite('bw_img.jpg', bw)
# show results

#cv2.drawContours(bw, approx, 0, (0,255,0), 3)
#cv2.waitKey(0)
