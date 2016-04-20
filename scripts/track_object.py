#!/usr/bin/env python
# from http://www.pyimagesearch.com/2015/09/21/opencv-track-object-movement/
# http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
# http://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
# 
# import packages
from collections import deque
import numpy as np
import argparse
import datetime
import imutils
import cv2
# construct the argument parse & parse
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())



