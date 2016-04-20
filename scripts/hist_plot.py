#!/usr/bin/env python
# import packages
import numpy as np
import argparse
from matplotlib import pyplot as plt
import cv2
# contruct the argument parse and parse the arguments!
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load image
image = cv2.imread(args["image"])

# change to grayscale
imGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# use CLAHE contrast limited adaptive histogram EQ
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(imGray)

cv2.imshow('image',cl1)
#cv2.imwrite('clahe_2.jpg',cl1)


#color = ('b','g','r')
#for i,col in enumerate(color):
#	histr = cv2.calcHist([image],[i],None,[256],[0,256])
#	plt.plot(histr,color = col)
#	plt.xlim([0,256])
#plt.show()
