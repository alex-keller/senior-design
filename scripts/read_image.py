#!/usr/bin/env python
import numpy as np
import cv2
from matplotlib import pyplot as plt

# load a color image in grayscale

img = cv2.imread('image.jpg',0)
plt.imshow(img, cmap='gray', imterpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # hides tick values on both axes
plt.show()
